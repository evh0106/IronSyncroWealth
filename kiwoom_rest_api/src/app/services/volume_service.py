"""거래량 조회 서비스 (ka10023/30/31/32/24/52/55).

기존 volume.rank / volume.stkinfo 의 HTTP 호출 로직을 FastAPI 서비스 레이어로 이관합니다.
"""

from __future__ import annotations

from app.core.exceptions import ApiError
from app.schemas.volume import (
    BrokerInstantVolumeRequest,
    PrevVolumeRankRequest,
    TodayPrevContractsRequest,
    TodayVolumeRankRequest,
    TradeAmountRankRequest,
    VolumeApiResponse,
    VolumeSurgeRequest,
    VolumeUpdateRequest,
    ServerMode,
)
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

_RKINFO_URL_PATH = "/api/dostk/rkinfo"
_STKINFO_URL_PATH = "/api/dostk/stkinfo"


class VolumeService:
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

    def _wrap(self, server_mode: ServerMode, api_id: str, data: dict) -> VolumeApiResponse:
        return VolumeApiResponse(server_mode=server_mode, api_id=api_id, data=data)

    # ─────────────────────────────────────────────
    # 순위정보 (rkinfo)
    # ─────────────────────────────────────────────

    async def volume_surge(self, req: VolumeSurgeRequest) -> VolumeApiResponse:
        """거래량급증요청 (ka10023)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "mrkt_tp": req.mrkt_tp,
            "sort_tp": req.sort_tp,
            "tm_tp": req.tm_tp,
            "trde_qty_tp": req.trde_qty_tp,
            "tm": req.tm,
            "stk_cnd": req.stk_cnd,
            "pric_tp": req.pric_tp,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _RKINFO_URL_PATH, "ka10023", token, body)
        return self._wrap(req.server_mode, "ka10023", data)

    async def today_volume_rank(self, req: TodayVolumeRankRequest) -> VolumeApiResponse:
        """당일거래량상위요청 (ka10030)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "mrkt_tp": req.mrkt_tp,
            "sort_tp": req.sort_tp,
            "mang_stk_incls": req.mang_stk_incls,
            "crd_tp": req.crd_tp,
            "trde_qty_tp": req.trde_qty_tp,
            "pric_tp": req.pric_tp,
            "trde_prica_tp": req.trde_prica_tp,
            "mrkt_open_tp": req.mrkt_open_tp,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _RKINFO_URL_PATH, "ka10030", token, body)
        return self._wrap(req.server_mode, "ka10030", data)

    async def prev_volume_rank(self, req: PrevVolumeRankRequest) -> VolumeApiResponse:
        """전일거래량상위요청 (ka10031)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "mrkt_tp": req.mrkt_tp,
            "qry_tp": req.qry_tp,
            "rank_strt": req.rank_strt,
            "rank_end": req.rank_end,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _RKINFO_URL_PATH, "ka10031", token, body)
        return self._wrap(req.server_mode, "ka10031", data)

    async def trade_amount_rank(self, req: TradeAmountRankRequest) -> VolumeApiResponse:
        """거래대금상위요청 (ka10032)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "mrkt_tp": req.mrkt_tp,
            "mang_stk_incls": req.mang_stk_incls,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _RKINFO_URL_PATH, "ka10032", token, body)
        return self._wrap(req.server_mode, "ka10032", data)

    # ─────────────────────────────────────────────
    # 종목정보 (stkinfo)
    # ─────────────────────────────────────────────

    async def volume_update(self, req: VolumeUpdateRequest) -> VolumeApiResponse:
        """거래량갱신요청 (ka10024)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "mrkt_tp": req.mrkt_tp,
            "cycle_tp": req.cycle_tp,
            "trde_qty_tp": req.trde_qty_tp,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _STKINFO_URL_PATH, "ka10024", token, body)
        return self._wrap(req.server_mode, "ka10024", data)

    async def broker_instant_volume(self, req: BrokerInstantVolumeRequest) -> VolumeApiResponse:
        """거래원순간거래량요청 (ka10052)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "mmcm_cd": req.mmcm_cd,
            "stk_cd": req.stk_cd,
            "mrkt_tp": req.mrkt_tp,
            "qty_tp": req.qty_tp,
            "pric_tp": req.pric_tp,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _STKINFO_URL_PATH, "ka10052", token, body)
        return self._wrap(req.server_mode, "ka10052", data)

    async def today_prev_contracts(self, req: TodayPrevContractsRequest) -> VolumeApiResponse:
        """당일전일체결량요청 (ka10055)."""
        host, token = self._resolve_token(req.server_mode)
        body = {
            "stk_cd": req.stk_cd,
            "tdy_pred": req.tdy_pred,
        }
        data = await kiwoom_post(host, _STKINFO_URL_PATH, "ka10055", token, body)
        return self._wrap(req.server_mode, "ka10055", data)


def get_volume_service() -> VolumeService:
    return VolumeService()
