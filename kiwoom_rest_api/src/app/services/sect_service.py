"""업종 조회 서비스 (ka20001).

기존 sect.sector_price 의 HTTP 호출 로직을 FastAPI 서비스 레이어로 이관합니다.
"""

from __future__ import annotations

import asyncio
from datetime import datetime

from fastapi import Depends

from app.core.exceptions import ApiError
from app.schemas.sect import SectCurrentPriceResponse
from app.services.kiwoom_client import kiwoom_post
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL
from oauth2.oauth import get_current_unrevoked_token
from sect.sector_price import save_ka20001

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
    def _resolve_token(self) -> tuple[str, str, str]:
        """현재 토큰의 서버 모드/호스트/토큰을 반환합니다."""
        token_ctx = get_current_unrevoked_token()
        if not token_ctx:
            raise ApiError(
                message="No valid access token found. Issue a token first via POST /api/v1/auth/token",
                code="TOKEN_NOT_FOUND",
                status_code=401,
            )
        server_mode, token = token_ctx
        host = _SERVER_HOSTS.get(server_mode)
        if host is None:
            raise ApiError(
                message=f"Unsupported server_mode: {server_mode}",
                code="INVALID_SERVER_MODE",
                status_code=400,
            )
        return server_mode, host, token

    async def get_current_price(
        self,
        mrkt_tp: str,
        sect_cd: str,
    ) -> SectCurrentPriceResponse:
        """업종현재가요청 (ka20001)."""
        server_mode, host, token = self._resolve_token()
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

        request_params = {
            "req_dt": datetime.now().strftime("%Y%m%d"),
            "mrkt_tp": mrkt_tp,
            "sect_cd": sect_cd,
        }
        try:
            await asyncio.to_thread(save_ka20001, data, request_params)
        except Exception:
            # 저장 실패가 응답 자체를 막지 않도록 합니다.
            pass

        return SectCurrentPriceResponse(
            server_mode=server_mode,
            api_id="ka20001",
            data=data,
        )


def get_sect_service() -> SectService:
    return SectService()
