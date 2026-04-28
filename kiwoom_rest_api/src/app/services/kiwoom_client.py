"""Kiwoom REST API 공통 HTTP 클라이언트.

기존 CLI 모듈의 requests 호출 패턴을 FastAPI 서비스에서 재사용하기 위한
얇은 래퍼입니다.  print/log 의존성 없이 순수하게 HTTP POST → dict 반환.

6단계에서 httpx.AsyncClient 기반 비동기 구현으로 전환했습니다.
"""

from __future__ import annotations

import httpx

from app.core.exceptions import ApiError


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
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, headers=headers, json=body)
            resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
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

    data: dict = resp.json()
    return_code = data.get("return_code")
    if return_code is not None and return_code != 0:
        raise ApiError(
            message=data.get("return_msg", "Kiwoom API returned non-zero code"),
            code="KIWOOM_API_ERROR",
            status_code=502,
            detail={"api_id": api_id, "return_code": return_code},
        )
    return data
