"""Common API exceptions and handlers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from .logging import get_logger


@dataclass(slots=True)
class ApiError(Exception):
    message: str
    code: str = "API_ERROR"
    status_code: int = 400
    detail: dict[str, Any] | None = None



def _error_body(request: Request, code: str, message: str, detail: Any = None) -> dict[str, Any]:
    return {
        "error": {
            "code": code,
            "message": message,
            "detail": detail,
        },
        "path": request.url.path,
        "request_id": getattr(request.state, "request_id", None),
    }



def register_exception_handlers(app: FastAPI) -> None:
    logger = get_logger()

    @app.exception_handler(ApiError)
    async def handle_api_error(request: Request, exc: ApiError):
        return JSONResponse(
            status_code=exc.status_code,
            content=_error_body(request, exc.code, exc.message, exc.detail),
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content=_error_body(request, "VALIDATION_ERROR", "Request validation failed", exc.errors()),
        )

    @app.exception_handler(StarletteHTTPException)
    async def handle_http_error(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=_error_body(request, "HTTP_ERROR", str(exc.detail), None),
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exc: Exception):
        logger.exception("unhandled_exception path=%s", request.url.path)
        return JSONResponse(
            status_code=500,
            content=_error_body(request, "INTERNAL_SERVER_ERROR", "Unexpected server error", None),
        )
