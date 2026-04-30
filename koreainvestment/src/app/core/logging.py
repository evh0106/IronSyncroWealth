"""Logging setup and request logging middleware."""

from __future__ import annotations

import logging
from logging.config import dictConfig
from time import perf_counter
from uuid import uuid4

from fastapi import Request
from starlette.responses import Response

from logger import log_http_request, log_http_response


LOGGER_NAME = "koreainvestment.fastapi"


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


def _bytes_to_text(raw: bytes) -> str:
    if not raw:
        return ""
    return raw.decode("utf-8", errors="replace")


async def _read_response_body(response: Response) -> bytes:
    chunks: list[bytes] = []
    async for chunk in response.body_iterator:
        chunks.append(chunk)
    return b"".join(chunks)


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
    try:
        _, req_id = log_http_request(
            api_id="fastapi_inbound",
            url=str(request.url),
            request_headers=dict(request.headers),
            request_body=req_body_text,
            log_name="koreainvestment",
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
                log_name="koreainvestment",
            )
        except Exception:
            logger.exception("response_logging_failed id=%s", request_id)

    logger.info(
        "request id=%s method=%s path=%s status=%s elapsed_ms=%.2f",
        request_id,
        request.method,
        request.url.path,
        final_response.status_code,
        elapsed_ms,
    )
    return final_response