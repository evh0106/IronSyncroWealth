"""거래량 조회 서비스 (ka10023/30/31/32/24/52/55).

기존 volume.rank / volume.stkinfo 의 HTTP 호출 로직을 FastAPI 서비스 레이어로 이관합니다.
"""

from __future__ import annotations

import asyncio
from datetime import datetime

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
)
from app.services.kiwoom_client import kiwoom_post
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL
from oauth2.oauth import get_current_unrevoked_token
from volume.rank import save_ka10023, save_ka10030, save_ka10031, save_ka10032
from volume.stkinfo import save_ka10024, save_ka10052, save_ka10055

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

    def _wrap(self, server_mode: str, api_id: str, data: dict) -> VolumeApiResponse:
        return VolumeApiResponse(server_mode=server_mode, api_id=api_id, data=data)

    async def _save_today_volume_rank(self, req: TodayVolumeRankRequest, data: dict) -> None:
        items = data.get("tdy_trde_qty_upper", [])
        if data.get("return_code") != 0 or not items:
            return

        request_params = {
            "req_dt": datetime.now().strftime("%Y%m%d"),
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

        try:
            await asyncio.to_thread(save_ka10030, items, request_params)
        except Exception:
            # CLI 경로와 동일하게 저장 실패가 응답 자체를 막지 않도록 합니다.
            pass

    async def _save_prev_volume_rank(self, data: dict) -> None:
        items = data.get("pred_trde_qty_upper", [])
        if data.get("return_code") != 0 or not items:
            return

        try:
            await asyncio.to_thread(save_ka10031, items)
        except Exception:
            # CLI 경로와 동일하게 저장 실패가 응답 자체를 막지 않도록 합니다.
            pass

    async def _save_volume_surge(self, data: dict) -> None:
        items = data.get("trde_qty_sdnin", [])
        if data.get("return_code") != 0 or not items:
            return

        try:
            await asyncio.to_thread(save_ka10023, items)
        except Exception:
            pass

    async def _save_trade_amount_rank(self, data: dict) -> None:
        items = data.get("trde_prica_upper", [])
        if data.get("return_code") != 0 or not items:
            return

        try:
            await asyncio.to_thread(save_ka10032, items)
        except Exception:
            pass

    async def _save_volume_update(self, data: dict) -> None:
        items = data.get("trde_qty_updt", [])
        if data.get("return_code") != 0 or not items:
            return

        try:
            await asyncio.to_thread(save_ka10024, items)
        except Exception:
            pass

    async def _save_broker_instant_volume(self, data: dict) -> None:
        items = data.get("trde_ori_mont_trde_qty", [])
        if data.get("return_code") != 0 or not items:
            return

        try:
            await asyncio.to_thread(save_ka10052, items)
        except Exception:
            pass

    async def _save_today_prev_contracts(self, req: TodayPrevContractsRequest, data: dict) -> None:
        items = data.get("tdy_pred_cntr_qty", [])
        if data.get("return_code") != 0 or not items:
            return

        try:
            await asyncio.to_thread(save_ka10055, items, req.stk_cd)
        except Exception:
            pass

    # ─────────────────────────────────────────────
    # 순위정보 (rkinfo)
    # ─────────────────────────────────────────────

    async def volume_surge(self, req: VolumeSurgeRequest) -> VolumeApiResponse:
        """거래량급증요청 (ka10023)."""
        server_mode, host, token = self._resolve_token()
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
        await self._save_volume_surge(data)
        return self._wrap(server_mode, "ka10023", data)

    async def today_volume_rank(self, req: TodayVolumeRankRequest) -> VolumeApiResponse:
        """당일거래량상위요청 (ka10030)."""
        server_mode, host, token = self._resolve_token()
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
        await self._save_today_volume_rank(req, data)
        return self._wrap(server_mode, "ka10030", data)

    async def prev_volume_rank(self, req: PrevVolumeRankRequest) -> VolumeApiResponse:
        """전일거래량상위요청 (ka10031)."""
        server_mode, host, token = self._resolve_token()
        body = {
            "mrkt_tp": req.mrkt_tp,
            "qry_tp": req.qry_tp,
            "rank_strt": req.rank_strt,
            "rank_end": req.rank_end,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _RKINFO_URL_PATH, "ka10031", token, body)
        await self._save_prev_volume_rank(data)
        return self._wrap(server_mode, "ka10031", data)

    async def trade_amount_rank(self, req: TradeAmountRankRequest) -> VolumeApiResponse:
        """거래대금상위요청 (ka10032)."""
        server_mode, host, token = self._resolve_token()
        body = {
            "mrkt_tp": req.mrkt_tp,
            "mang_stk_incls": req.mang_stk_incls,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _RKINFO_URL_PATH, "ka10032", token, body)
        await self._save_trade_amount_rank(data)
        return self._wrap(server_mode, "ka10032", data)

    # ─────────────────────────────────────────────
    # 종목정보 (stkinfo)
    # ─────────────────────────────────────────────

    async def volume_update(self, req: VolumeUpdateRequest) -> VolumeApiResponse:
        """거래량갱신요청 (ka10024)."""
        server_mode, host, token = self._resolve_token()
        body = {
            "mrkt_tp": req.mrkt_tp,
            "cycle_tp": req.cycle_tp,
            "trde_qty_tp": req.trde_qty_tp,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _STKINFO_URL_PATH, "ka10024", token, body)
        await self._save_volume_update(data)
        return self._wrap(server_mode, "ka10024", data)

    async def broker_instant_volume(self, req: BrokerInstantVolumeRequest) -> VolumeApiResponse:
        """거래원순간거래량요청 (ka10052)."""
        server_mode, host, token = self._resolve_token()
        body = {
            "mmcm_cd": req.mmcm_cd,
            "stk_cd": req.stk_cd,
            "mrkt_tp": req.mrkt_tp,
            "qty_tp": req.qty_tp,
            "pric_tp": req.pric_tp,
            "stex_tp": req.stex_tp,
        }
        data = await kiwoom_post(host, _STKINFO_URL_PATH, "ka10052", token, body)
        await self._save_broker_instant_volume(data)
        return self._wrap(server_mode, "ka10052", data)

    async def today_prev_contracts(self, req: TodayPrevContractsRequest) -> VolumeApiResponse:
        """당일전일체결량요청 (ka10055)."""
        server_mode, host, token = self._resolve_token()
        body = {
            "stk_cd": req.stk_cd,
            "tdy_pred": req.tdy_pred,
        }
        data = await kiwoom_post(host, _STKINFO_URL_PATH, "ka10055", token, body)
        await self._save_today_prev_contracts(req, data)
        return self._wrap(server_mode, "ka10055", data)


def get_volume_service() -> VolumeService:
    return VolumeService()
