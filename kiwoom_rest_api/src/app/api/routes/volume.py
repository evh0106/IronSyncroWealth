"""거래량 조회 API 라우터 (국내주식 > 순위정보 / 종목정보)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from app.schemas.volume import VolumeApiResponse
from app.services.volume_service import VolumeService, get_volume_service
from app.schemas.volume import (
    VolumeSurgeRequest,
    TodayVolumeRankRequest,
    PrevVolumeRankRequest,
    TradeAmountRankRequest,
    VolumeUpdateRequest,
    BrokerInstantVolumeRequest,
    TodayPrevContractsRequest,
)

router = APIRouter(prefix="/volume", tags=["거래량"])


# ─────────────────────────────────────────────
# 순위정보 (rkinfo)
# ─────────────────────────────────────────────

@router.get(
    "/surge",
    response_model=VolumeApiResponse,
    summary="거래량급증요청 (ka10023)",
)
async def get_volume_surge(
    mrkt_tp: str = Query("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥"),
    sort_tp: str = Query("1", description="정렬구분: 1=급증량, 2=급증률"),
    tm_tp: str = Query("2", description="시간구분: 1=분전, 2=일전"),
    trde_qty_tp: str = Query("5", description="거래량구분: 1=전체…5=십만주"),
    tm: str = Query("", description="시간 값"),
    stk_cnd: str = Query("0", description="종목조건: 0=전체"),
    pric_tp: str = Query("0", description="가격구분: 0=전체"),
    stex_tp: str = Query("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = VolumeSurgeRequest(
        mrkt_tp=mrkt_tp, sort_tp=sort_tp, tm_tp=tm_tp,
        trde_qty_tp=trde_qty_tp, tm=tm, stk_cnd=stk_cnd,
        pric_tp=pric_tp, stex_tp=stex_tp,
    )
    return await service.volume_surge(req)


@router.get(
    "/today-rank",
    response_model=VolumeApiResponse,
    summary="당일거래량상위요청 (ka10030)",
)
async def get_today_volume_rank(
    mrkt_tp: str = Query("000"),
    sort_tp: str = Query("1"),
    mang_stk_incls: str = Query("0"),
    crd_tp: str = Query("0"),
    trde_qty_tp: str = Query("0"),
    pric_tp: str = Query("0"),
    trde_prica_tp: str = Query("0"),
    mrkt_open_tp: str = Query("0"),
    stex_tp: str = Query("3"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = TodayVolumeRankRequest(
        mrkt_tp=mrkt_tp, sort_tp=sort_tp, mang_stk_incls=mang_stk_incls,
        crd_tp=crd_tp, trde_qty_tp=trde_qty_tp, pric_tp=pric_tp,
        trde_prica_tp=trde_prica_tp, mrkt_open_tp=mrkt_open_tp, stex_tp=stex_tp,
    )
    return await service.today_volume_rank(req)


@router.get(
    "/prev-rank",
    response_model=VolumeApiResponse,
    summary="전일거래량상위요청 (ka10031)",
)
async def get_prev_volume_rank(
    mrkt_tp: str = Query("000"),
    qry_tp: str = Query("1"),
    rank_strt: str = Query("0"),
    rank_end: str = Query("20"),
    stex_tp: str = Query("3"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = PrevVolumeRankRequest(
        mrkt_tp=mrkt_tp, qry_tp=qry_tp, rank_strt=rank_strt,
        rank_end=rank_end, stex_tp=stex_tp,
    )
    return await service.prev_volume_rank(req)


@router.get(
    "/trade-amount-rank",
    response_model=VolumeApiResponse,
    summary="거래대금상위요청 (ka10032)",
)
async def get_trade_amount_rank(
    mrkt_tp: str = Query("001"),
    mang_stk_incls: str = Query("1"),
    stex_tp: str = Query("3"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = TradeAmountRankRequest(
        mrkt_tp=mrkt_tp, mang_stk_incls=mang_stk_incls, stex_tp=stex_tp,
    )
    return await service.trade_amount_rank(req)


# ─────────────────────────────────────────────
# 종목정보 (stkinfo)
# ─────────────────────────────────────────────

@router.get(
    "/update",
    response_model=VolumeApiResponse,
    summary="거래량갱신요청 (ka10024)",
)
async def get_volume_update(
    mrkt_tp: str = Query("000"),
    cycle_tp: str = Query("5", description="주기구분: 1=1분, 2=3분, 3=5분, 4=10분, 5=30분"),
    trde_qty_tp: str = Query("5"),
    stex_tp: str = Query("3"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = VolumeUpdateRequest(
        mrkt_tp=mrkt_tp, cycle_tp=cycle_tp, trde_qty_tp=trde_qty_tp, stex_tp=stex_tp,
    )
    return await service.volume_update(req)


@router.get(
    "/broker-instant",
    response_model=VolumeApiResponse,
    summary="거래원순간거래량요청 (ka10052)",
)
async def get_broker_instant_volume(
    mmcm_cd: str = Query(..., description="회원사코드 (예: 888=외국계합계, 001=키움증권)"),
    mrkt_tp: str = Query("0", description="시장구분: 0=전체, 1=코스피, 2=코스닥, 3=종목"),
    stk_cd: str = Query("", description="종목코드 (mrkt_tp=3일 때 필수)"),
    qty_tp: str = Query("0"),
    pric_tp: str = Query("0"),
    stex_tp: str = Query("3"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = BrokerInstantVolumeRequest(
        mmcm_cd=mmcm_cd, mrkt_tp=mrkt_tp, stk_cd=stk_cd,
        qty_tp=qty_tp, pric_tp=pric_tp, stex_tp=stex_tp,
    )
    return await service.broker_instant_volume(req)


@router.get(
    "/today-prev-contracts",
    response_model=VolumeApiResponse,
    summary="당일전일체결량요청 (ka10055)",
)
async def get_today_prev_contracts(
    stk_cd: str = Query(..., description="종목코드 (예: 005930)"),
    tdy_pred: str = Query("1", description="당일전일구분: 1=당일, 2=전일"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = TodayPrevContractsRequest(
        stk_cd=stk_cd, tdy_pred=tdy_pred,
    )
    return await service.today_prev_contracts(req)
