"""업종 조회 서비스 (ka20001).

기존 sect.sector_price 의 HTTP 호출 로직을 FastAPI 서비스 레이어로 이관합니다.
"""

from __future__ import annotations

from fastapi import Depends

from app.core.exceptions import ApiError
from app.schemas.sect import SectCurrentPriceResponse, ServerMode
from app.services.kiwoom_client import kiwoom_post
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL, load_api_keys
from oauth2.oauth import get_unrevoked_token

_SERVER_HOSTS: dict[str, str] = {
    "real": HOST_REAL,
    "mock": HOST_MOC,
}

_SERVER_ACCOUNT: dict[str, str] = {
    "real": "65120003",
    "mock": "81241972",
}

_SECT_URL_PATH = "/api/dostk/sect"


class SectService:
    def _resolve_token(self, server_mode: ServerMode) -> tuple[str, str]:
        """서버 모드에 맞는 호스트와 유효한 캐시 토큰을 반환합니다."""
        host = _SERVER_HOSTS.get(server_mode)
        if host is None:
            raise ApiError(
                message=f"Unsupported server_mode: {server_mode}",
                code="INVALID_SERVER_MODE",
                status_code=400,
            )
        app_key, _ = load_api_keys(host=host)
        token = get_unrevoked_token(app_key)
        if not token:
            raise ApiError(
                message="No valid access token found. Issue a token first via POST /api/v1/auth/token",
                code="TOKEN_NOT_FOUND",
                status_code=401,
            )
        return host, token

    async def get_current_price(
        self,
        server_mode: ServerMode,
        mrkt_tp: str,
        sect_cd: str,
    ) -> SectCurrentPriceResponse:
        """업종현재가요청 (ka20001)."""
        host, token = self._resolve_token(server_mode)
        body = {
            "mrkt_tp": mrkt_tp,
            "inds_cd": sect_cd,
        }
        data = await kiwoom_post(
            host=host,
            url_path=_SECT_URL_PATH,
            api_id="ka20001",
            token=token,
            body=body,
        )
        return SectCurrentPriceResponse(
            server_mode=server_mode,
            api_id="ka20001",
            data=data,
        )


def get_sect_service() -> SectService:
    return SectService()
