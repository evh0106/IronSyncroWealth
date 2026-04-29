"""Kiwoom REST API 공통 HTTP 클라이언트.

기존 CLI 모듈의 requests 호출 패턴을 FastAPI 서비스에서 재사용하기 위한
얇은 래퍼입니다.  print/log 의존성 없이 순수하게 HTTP POST → dict 반환.

6단계에서 httpx.AsyncClient 기반 비동기 구현으로 전환했습니다.
"""

from __future__ import annotations

import asyncio
import json

import httpx

from app.core.exceptions import ApiError
import db
from logger import log_http_request, log_http_response


_CREATE_FASTAPI_API_LOG = """
CREATE TABLE IF NOT EXISTS fastapi_api_log (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    api_id VARCHAR(20) NOT NULL,
    host VARCHAR(255) NOT NULL,
    url_path VARCHAR(255) NOT NULL,
    req_headers JSON,
    req_body JSON,
    rsp_status INT,
    rsp_code INT,
    rsp_msg VARCHAR(500),
    rsp_headers JSON,
    rsp_payload JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

_INSERT_FASTAPI_API_LOG = """
INSERT INTO fastapi_api_log (
    api_id, host, url_path,
    req_headers, req_body,
    rsp_status, rsp_code, rsp_msg,
    rsp_headers, rsp_payload
) VALUES (
    %(api_id)s, %(host)s, %(url_path)s,
    %(req_headers)s, %(req_body)s,
    %(rsp_status)s, %(rsp_code)s, %(rsp_msg)s,
    %(rsp_headers)s, %(rsp_payload)s
)
"""

_fastapi_api_log_table_ensured = False


def _ensure_fastapi_api_log_table() -> None:
    global _fastapi_api_log_table_ensured
    if _fastapi_api_log_table_ensured:
        return
    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(_CREATE_FASTAPI_API_LOG)
        conn.commit()
        _fastapi_api_log_table_ensured = True
    finally:
        conn.close()


def _save_fastapi_api_log(
    *,
    api_id: str,
    host: str,
    url_path: str,
    req_headers: dict,
    req_body: dict,
    rsp_status: int,
    rsp_headers: dict,
    rsp_payload: dict,
) -> None:
    _ensure_fastapi_api_log_table()
    row = {
        "api_id": api_id,
        "host": host,
        "url_path": url_path,
        "req_headers": json.dumps(req_headers, ensure_ascii=False),
        "req_body": json.dumps(req_body, ensure_ascii=False),
        "rsp_status": rsp_status,
        "rsp_code": rsp_payload.get("return_code"),
        "rsp_msg": rsp_payload.get("return_msg", ""),
        "rsp_headers": json.dumps(rsp_headers, ensure_ascii=False),
        "rsp_payload": json.dumps(rsp_payload, ensure_ascii=False),
    }

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(_INSERT_FASTAPI_API_LOG, row)
        conn.commit()
    finally:
        conn.close()


async def kiwoom_post(host: str, url_path: str, api_id: str, token: str, body: dict) -> dict:
    """Kiwoom API 서버에 비동기 POST 요청을 보내고 JSON 응답을 반환합니다.

    Parameters
    ----------
    host:
        베이스 호스트 URL (예: ``https://api.kiwoom.com``)
    url_path:
        호스트 이후의 경로 (예: ``/api/dostk/sect``)
    api_id:
        Kiwoom API 식별자 (예: ``ka20001``)
    token:
        Bearer 액세스 토큰
    body:
        요청 바디 dict

    Returns
    -------
    dict
        Kiwoom API JSON 응답

    Raises
    ------
    ApiError
        HTTP 오류 또는 API 업무 오류 시
    """
    url = host.rstrip("/") + url_path
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "authorization": f"Bearer {token}",
        "cont-yn": "N",
        "next-key": "",
        "api-id": api_id,
    }

    req_body_raw = json.dumps(body, ensure_ascii=False)
    req_id = ""
    try:
        _, req_id = log_http_request(
            api_id=api_id,
            url=url,
            request_headers=headers,
            request_body=req_body_raw,
            log_name="fastapi",
        )
    except Exception:
        req_id = ""

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, headers=headers, json=body)
            resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
        if req_id:
            try:
                log_http_response(
                    req_id=req_id,
                    response_status=exc.response.status_code,
                    response_headers=dict(exc.response.headers),
                    response_body=exc.response.text,
                    log_name="fastapi",
                )
            except Exception:
                pass
        raise ApiError(
            message=f"Kiwoom API HTTP error: {exc.response.status_code}",
            code="KIWOOM_HTTP_ERROR",
            status_code=502,
            detail={"api_id": api_id, "status_code": exc.response.status_code},
        ) from exc
    except httpx.RequestError as exc:
        raise ApiError(
            message=f"Kiwoom API request failed: {exc}",
            code="KIWOOM_REQUEST_ERROR",
            status_code=502,
            detail={"api_id": api_id},
        ) from exc

    if req_id:
        try:
            log_http_response(
                req_id=req_id,
                response_status=resp.status_code,
                response_headers=dict(resp.headers),
                response_body=resp.text,
                log_name="fastapi",
            )
        except Exception:
            pass

    data: dict = resp.json()

    try:
        await asyncio.to_thread(
            _save_fastapi_api_log,
            api_id=api_id,
            host=host,
            url_path=url_path,
            req_headers=headers,
            req_body=body,
            rsp_status=resp.status_code,
            rsp_headers=dict(resp.headers),
            rsp_payload=data,
        )
    except Exception:
        # 로깅/적재 실패가 API 기능 자체를 막지 않도록 무시합니다.
        pass

    return_code = data.get("return_code")
    if return_code is not None and return_code != 0:
        raise ApiError(
            message=data.get("return_msg", "Kiwoom API returned non-zero code"),
            code="KIWOOM_API_ERROR",
            status_code=502,
            detail={"api_id": api_id, "return_code": return_code},
        )
    return data
