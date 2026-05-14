"""Logging setup and request logging middleware."""

from __future__ import annotations

import asyncio
import json
import logging
from logging.config import dictConfig
from time import perf_counter
from urllib.parse import urlparse
from uuid import uuid4

from fastapi import Request
from starlette.responses import Response

import db
from logger import log_http_request, log_http_response


LOGGER_NAME = "kiwoom.fastapi"

_CREATE_FASTAPI_HTTP_LOG = """
CREATE TABLE IF NOT EXISTS fastapi_http_log (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    request_id VARCHAR(64) NOT NULL,
    method VARCHAR(16) NOT NULL,
    path VARCHAR(255) NOT NULL,
    query_string TEXT,
    req_headers JSON,
    req_body LONGTEXT,
    rsp_status INT,
    rsp_headers JSON,
    rsp_body LONGTEXT,
    elapsed_ms DOUBLE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_request_id (request_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""

_INSERT_FASTAPI_HTTP_LOG = """
INSERT INTO fastapi_http_log (
    request_id, method, path, query_string,
    req_headers, req_body,
    rsp_status, rsp_headers, rsp_body,
    elapsed_ms
) VALUES (
    %(request_id)s, %(method)s, %(path)s, %(query_string)s,
    %(req_headers)s, %(req_body)s,
    %(rsp_status)s, %(rsp_headers)s, %(rsp_body)s,
    %(elapsed_ms)s
)
"""

_fastapi_http_log_table_ensured = False


def _ensure_fastapi_http_log_table() -> None:
    global _fastapi_http_log_table_ensured
    if _fastapi_http_log_table_ensured:
        return

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(_CREATE_FASTAPI_HTTP_LOG)
        conn.commit()
        _fastapi_http_log_table_ensured = True
    finally:
        conn.close()


def _save_fastapi_http_log(
    *,
    request_id: str,
    method: str,
    path: str,
    query_string: str,
    req_headers: dict,
    req_body: str,
    rsp_status: int,
    rsp_headers: dict,
    rsp_body: str,
    elapsed_ms: float,
) -> None:
    _ensure_fastapi_http_log_table()
    row = {
        "request_id": request_id,
        "method": method,
        "path": path,
        "query_string": query_string,
        "req_headers": json.dumps(req_headers, ensure_ascii=False),
        "req_body": req_body,
        "rsp_status": rsp_status,
        "rsp_headers": json.dumps(rsp_headers, ensure_ascii=False),
        "rsp_body": rsp_body,
        "elapsed_ms": elapsed_ms,
    }

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(_INSERT_FASTAPI_HTTP_LOG, row)
        conn.commit()
    finally:
        conn.close()


def _bytes_to_text(raw: bytes) -> str:
    if not raw:
        return ""
    return raw.decode("utf-8", errors="replace")


async def _read_response_body(response: Response) -> bytes:
    chunks: list[bytes] = []
    async for chunk in response.body_iterator:
        chunks.append(chunk)
    return b"".join(chunks)



def setup_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "level": "INFO",
                }
            },
            "loggers": {
                LOGGER_NAME: {
                    "handlers": ["console"],
                    "level": "INFO",
                    "propagate": False,
                }
            },
        }
    )



def get_logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)


def _is_local_swagger_request(request: Request) -> bool:
    path = request.url.path or ""
    if path == "/openapi.json" or path.startswith("/docs") or path.startswith("/redoc"):
        return True

    referer = (request.headers.get("referer") or "").strip()
    host = (request.headers.get("host") or "").strip()
    if not referer:
        return False

    parsed = urlparse(referer)
    if "/docs" not in (parsed.path or ""):
        return False

    if not parsed.netloc:
        return True

    if host and parsed.netloc == host:
        return True

    return parsed.hostname in {"localhost", "127.0.0.1"}


async def request_logging_middleware(request: Request, call_next):
    logger = get_logger()
    request_id = request.headers.get("x-request-id") or str(uuid4())
    request.state.request_id = request_id

    req_body_bytes = await request.body()
    req_body_text = _bytes_to_text(req_body_bytes)

    consumed = False

    async def receive() -> dict:
        nonlocal consumed
        if consumed:
            return {"type": "http.request", "body": b"", "more_body": False}
        consumed = True
        return {"type": "http.request", "body": req_body_bytes, "more_body": False}

    request = Request(request.scope, receive)
    request.state.request_id = request_id

    req_id = ""
    skip_file_log = _is_local_swagger_request(request)
    if not skip_file_log:
        try:
            _, req_id = log_http_request(
                api_id="fastapi_inbound",
                url=str(request.url),
                request_headers=dict(request.headers),
                request_body=req_body_text,
                log_name="fastapi",
            )
        except Exception:
            req_id = ""

    started = perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        logger.exception(
            "request_failed id=%s method=%s path=%s",
            request_id,
            request.method,
            request.url.path,
        )
        raise

    elapsed_ms = (perf_counter() - started) * 1000

    rsp_body_bytes = await _read_response_body(response)
    rsp_body_text = _bytes_to_text(rsp_body_bytes)
    response_headers = dict(response.headers)
    response_headers["x-request-id"] = request_id

    final_response = Response(
        content=rsp_body_bytes,
        status_code=response.status_code,
        headers=response_headers,
        media_type=response.media_type,
        background=response.background,
    )

    if req_id:
        try:
            log_http_response(
                req_id=req_id,
                response_status=final_response.status_code,
                response_headers=response_headers,
                response_body=rsp_body_text,
                log_name="fastapi",
            )
        except Exception:
            pass

    try:
        await asyncio.to_thread(
            _save_fastapi_http_log,
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            query_string=request.url.query,
            req_headers=dict(request.headers),
            req_body=req_body_text,
            rsp_status=final_response.status_code,
            rsp_headers=response_headers,
            rsp_body=rsp_body_text,
            elapsed_ms=elapsed_ms,
        )
    except Exception:
        # 로깅 실패가 API 응답 자체를 막지 않도록 무시합니다.
        pass

    logger.info(
        "request id=%s method=%s path=%s status=%s elapsed_ms=%.2f",
        request_id,
        request.method,
        request.url.path,
        final_response.status_code,
        elapsed_ms,
    )
    return final_response
