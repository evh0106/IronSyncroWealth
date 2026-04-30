"""API router composition."""

from fastapi import APIRouter

from .routes.auth import router as auth_router
from .routes.health import router as health_router
from .routes.quotations import router as quotations_router
from .routes.ranking import router as ranking_router
from .routes.trading import router as trading_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(ranking_router)
api_router.include_router(quotations_router)
api_router.include_router(trading_router)