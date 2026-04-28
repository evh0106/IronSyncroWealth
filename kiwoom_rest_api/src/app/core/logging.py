"""Logging setup and request logging middleware."""

from __future__ import annotations

import logging
from logging.config import dictConfig
from time import perf_counter
from uuid import uuid4

from fastapi import Request


LOGGER_NAME = "kiwoom.fastapi"



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


async def request_logging_middleware(request: Request, call_next):
    logger = get_logger()
    request_id = request.headers.get("x-request-id") or str(uuid4())
    request.state.request_id = request_id

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
    response.headers["x-request-id"] = request_id

    logger.info(
        "request id=%s method=%s path=%s status=%s elapsed_ms=%.2f",
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        elapsed_ms,
    )
    return response
