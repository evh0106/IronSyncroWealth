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
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="거래량급증요청 (ka10023)",
)
@router.post(
    "/surge",
    response_model=VolumeApiResponse,
    summary="거래량급증요청 (ka10023)",
)
async def get_volume_surge(
    mrkt_tp: str = Query("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥"),
    sort_tp: str = Query("1", description="정렬구분: 1:급증량, 2:급증률, 3:급감량, 4:급감률"),
    tm_tp: str = Query("2", description="시간구분: 1:분, 2:전일"),
    trde_qty_tp: str = Query("5", description="거래량구분: 5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상"),
    tm: str = Query("", description="시간: 분 입력"),
    stk_cnd: str = Query("0", description="종목조건: 0:전체조회, 1:관리종목제외, 3:우선주제외, 11:정리매매종목제외, 4:관리종목,우선주제외, 5:증100제외, 6:증100만보기, 13:증60만보기, 12:증50만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기, 17:ETN제외, 14:ETF제외, 18:ETF+ETN제외, 15:스팩제외, 20:ETF+ETN+스팩제외"),
    pric_tp: str = Query("0", description="가격구분: 0:전체조회, 2:5만원이상, 5:1만원이상, 6:5천원이상, 8:1천원이상, 9:10만원이상"),
    stex_tp: str = Query("3", description="거래소구분: 1:KRX, 2:NXT 3.통합"),
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
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="당일거래량상위요청 (ka10030)",
)
@router.post(
    "/today-rank",
    response_model=VolumeApiResponse,
    summary="당일거래량상위요청 (ka10030)",
)
async def get_today_volume_rank(
    mrkt_tp: str = Query("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥"),
    sort_tp: str = Query("1", description="정렬구분: 1:거래량, 2:거래회전율, 3:거래대금"),
    mang_stk_incls: str = Query("0", description="관리종목포함: 0:관리종목 포함, 1:관리종목 미포함, 3:우선주제외, 11:정리매매종목제외, 4:관리종목, 우선주제외, 5:증100제외, 6:증100마나보기, 13:증60만보기, 12:증50만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기, 14:ETF제외, 15:스팩제외, 16:ETF+ETN제외"),
    crd_tp: str = Query("0", description="신용구분: 0:전체조회, 9:신용융자전체, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 8:신용대주"),
    trde_qty_tp: str = Query("0", description="거래량구분: 0:전체조회, 5:5천주이상, 10:1만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:500만주이상, 1000:백만주이상"),
    pric_tp: str = Query("0", description="가격구분: 0:전체조회, 1:1천원미만, 2:1천원이상, 3:1천원~2천원, 4:2천원~5천원, 5:5천원이상, 6:5천원~1만원, 10:1만원미만, 7:1만원이상, 8:5만원이상, 9:10만원이상"),
    trde_prica_tp: str = Query("0", description="거래대금구분: 0:전체조회, 1:1천만원이상, 3:3천만원이상, 4:5천만원이상, 10:1억원이상, 30:3억원이상, 50:5억원이상, 100:10억원이상, 300:30억원이상, 500:50억원이상, 1000:100억원이상, 3000:300억원이상, 5000:500억원이상"),
    mrkt_open_tp: str = Query("0", description="장운영구분: 0:전체조회, 1:장중, 2:장전시간외, 3:장후시간외"),
    stex_tp: str = Query("3", description="거래소구분: 1:KRX, 2:NXT 3.통합"),
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
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="전일거래량상위요청 (ka10031)",
)
@router.post(
    "/prev-rank",
    response_model=VolumeApiResponse,
    summary="전일거래량상위요청 (ka10031)",
)
async def get_prev_volume_rank(
    mrkt_tp: str = Query("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥"),
    qry_tp: str = Query("1", description="조회구분: 1:전일거래량 상위100종목, 2:전일거래대금 상위100종목"),
    rank_strt: str = Query("0", description="순위시작: 0 ~ 100 값 중에  조회를 원하는 순위 시작값"),
    rank_end: str = Query("20", description="순위끝: 0 ~ 100 값 중에  조회를 원하는 순위 끝값"),
    stex_tp: str = Query("3", description="거래소구분: 1:KRX, 2:NXT 3.통합"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = PrevVolumeRankRequest(
        mrkt_tp=mrkt_tp, qry_tp=qry_tp, rank_strt=rank_strt,
        rank_end=rank_end, stex_tp=stex_tp,
    )
    return await service.prev_volume_rank(req)


@router.get(
    "/trade-amount-rank",
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="거래대금상위요청 (ka10032)",
)
@router.post(
    "/trade-amount-rank",
    response_model=VolumeApiResponse,
    summary="거래대금상위요청 (ka10032)",
)
async def get_trade_amount_rank(
    mrkt_tp: str = Query("001", description="시장구분: 000=전체, 001=코스피, 101=코스닥"),
    mang_stk_incls: str = Query("1", description="관리종목포함: 0=관리종목 미포함, 1=관리종목 포함"),
    stex_tp: str = Query("3", description="거래소구분: 1=KRX, 2=NXT 3.통합"),
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
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="거래량갱신요청 (ka10024)",
)
@router.post(
    "/update",
    response_model=VolumeApiResponse,
    summary="거래량갱신요청 (ka10024)",
)
async def get_volume_update(
    mrkt_tp: str = Query("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥"),
    cycle_tp: str = Query("5", description="주기구분: 5:5일, 10:10일, 20:20일, 60:60일, 250:250일"),
    trde_qty_tp: str = Query("5", description="거래량구분: 5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상"),
    stex_tp: str = Query("3", description="거래소구분: 1:KRX, 2:NXT 3.통합"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = VolumeUpdateRequest(
        mrkt_tp=mrkt_tp, cycle_tp=cycle_tp, trde_qty_tp=trde_qty_tp, stex_tp=stex_tp,
    )
    return await service.volume_update(req)


@router.get(
    "/broker-instant",
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="거래원순간거래량요청 (ka10052)",
)
@router.post(
    "/broker-instant",
    response_model=VolumeApiResponse,
    summary="거래원순간거래량요청 (ka10052)",
)
async def get_broker_instant_volume(
    mmcm_cd: str = Query(..., description="회원사코드: 회원사 코드는 ka10102 조회"),
    mrkt_tp: str = Query("0", description="시장구분: 0:전체, 1:코스피, 2:코스닥, 3:종목"),
    stk_cd: str = Query("", description="종목코드: 거래소별 종목코드(KRX:039490,NXT:039490_NX,SOR:039490_AL)"),
    qty_tp: str = Query("0", description="수량구분: 0:전체, 1:1000주, 2:2000주, 3:, 5:, 10:10000주, 30: 30000주, 50: 50000주, 100: 100000주"),
    pric_tp: str = Query("0", description="가격구분: 0:전체, 1:1천원 미만, 8:1천원 이상, 2:1천원 ~ 2천원, 3:2천원 ~ 5천원, 4:5천원 ~ 1만원, 5:1만원 이상"),
    stex_tp: str = Query("3", description="거래소구분: 1:KRX, 2:NXT 3.통합"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = BrokerInstantVolumeRequest(
        mmcm_cd=mmcm_cd, mrkt_tp=mrkt_tp, stk_cd=stk_cd,
        qty_tp=qty_tp, pric_tp=pric_tp, stex_tp=stex_tp,
    )
    return await service.broker_instant_volume(req)


@router.get(
    "/today-prev-contracts",
    include_in_schema=False,
    response_model=VolumeApiResponse,
    summary="당일전일체결량요청 (ka10055)",
)
@router.post(
    "/today-prev-contracts",
    response_model=VolumeApiResponse,
    summary="당일전일체결량요청 (ka10055)",
)
async def get_today_prev_contracts(
    stk_cd: str = Query(..., description="종목코드: 거래소별 종목코드(KRX:039490,NXT:039490_NX,SOR:039490_AL)"),
    tdy_pred: str = Query("1", description="당일전일: 1:당일, 2:전일"),
    service: VolumeService = Depends(get_volume_service),
) -> VolumeApiResponse:
    req = TodayPrevContractsRequest(
        stk_cd=stk_cd, tdy_pred=tdy_pred,
    )
    return await service.today_prev_contracts(req)
