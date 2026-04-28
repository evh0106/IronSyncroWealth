"""API router composition."""

from fastapi import APIRouter

from .routes.acnt import router as acnt_router
from .routes.auth import router as auth_router
from .routes.health import router as health_router
from .routes.ordr import router as ordr_router
from .routes.sect import router as sect_router
from .routes.volume import router as volume_router
from .routes.ws import router as ws_router

api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(sect_router)
api_router.include_router(volume_router)
api_router.include_router(acnt_router)
api_router.include_router(ordr_router)
api_router.include_router(ws_router)
