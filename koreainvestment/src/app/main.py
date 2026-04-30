"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import load_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import request_logging_middleware, setup_logging


def create_app() -> FastAPI:
    settings = load_settings()
    setup_logging()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
    )

    app.middleware("http")(request_logging_middleware)
    register_exception_handlers(app)

    @app.get("/")
    def root() -> dict[str, str]:
        return {
            "service": settings.app_name,
            "version": settings.app_version,
            "env": settings.env,
            "docs": "/docs",
        }

    app.include_router(api_router, prefix=settings.api_prefix)
    return app


app = create_app()