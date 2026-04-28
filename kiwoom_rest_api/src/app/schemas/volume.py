"""거래량 API 요청/응답 스키마 (국내주식 > 순위정보 / 종목정보)."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

ServerMode = Literal["real", "mock"]


# ─────────────────────────────────────────────
# 공통 응답 래퍼
# ─────────────────────────────────────────────

class VolumeApiResponse(BaseModel):
    """거래량 API 공통 응답 래퍼."""

    server_mode: ServerMode
    api_id: str
    data: dict[str, Any] = Field(description="Kiwoom API 원본 응답")


# ─────────────────────────────────────────────
# 순위정보 요청 스키마
# ─────────────────────────────────────────────

class VolumeSurgeRequest(BaseModel):
    """거래량급증요청 (ka10023)."""

    server_mode: ServerMode = Field("real", description="서버 모드 (real/mock)")
    mrkt_tp: str = Field("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥")
    sort_tp: str = Field("1", description="정렬구분: 1=급증량, 2=급증률")
    tm_tp: str = Field("2", description="시간구분: 1=분전, 2=일전")
    trde_qty_tp: str = Field("5", description="거래량구분: 1=전체, 2=백주, 3=천주, 4=만주, 5=십만주")
    tm: str = Field("", description="시간(분전·일전 입력)")
    stk_cnd: str = Field("0", description="종목조건: 0=전체")
    pric_tp: str = Field("0", description="가격구분: 0=전체")
    stex_tp: str = Field("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합")


class TodayVolumeRankRequest(BaseModel):
    """당일거래량상위요청 (ka10030)."""

    server_mode: ServerMode = Field("real")
    mrkt_tp: str = Field("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥")
    sort_tp: str = Field("1", description="정렬구분: 1=거래량")
    mang_stk_incls: str = Field("0", description="관리종목포함: 0=불포함, 1=포함")
    crd_tp: str = Field("0", description="신용구분: 0=전체")
    trde_qty_tp: str = Field("0", description="거래량구분: 0=전체")
    pric_tp: str = Field("0", description="가격구분: 0=전체")
    trde_prica_tp: str = Field("0", description="거래대금구분: 0=전체")
    mrkt_open_tp: str = Field("0", description="시장개폐구분: 0=전체")
    stex_tp: str = Field("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합")


class PrevVolumeRankRequest(BaseModel):
    """전일거래량상위요청 (ka10031)."""

    server_mode: ServerMode = Field("real")
    mrkt_tp: str = Field("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥")
    qry_tp: str = Field("1", description="조회구분: 1=전체, 2=상위")
    rank_strt: str = Field("0", description="순위 시작")
    rank_end: str = Field("20", description="순위 끝")
    stex_tp: str = Field("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합")


class TradeAmountRankRequest(BaseModel):
    """거래대금상위요청 (ka10032)."""

    server_mode: ServerMode = Field("real")
    mrkt_tp: str = Field("001", description="시장구분: 001=코스피, 101=코스닥")
    mang_stk_incls: str = Field("1", description="관리종목포함: 0=불포함, 1=포함")
    stex_tp: str = Field("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합")


# ─────────────────────────────────────────────
# 종목정보 요청 스키마
# ─────────────────────────────────────────────

class VolumeUpdateRequest(BaseModel):
    """거래량갱신요청 (ka10024)."""

    server_mode: ServerMode = Field("real")
    mrkt_tp: str = Field("000", description="시장구분: 000=전체, 001=코스피, 101=코스닥")
    cycle_tp: str = Field("5", description="주기구분: 1=1분, 2=3분, 3=5분, 4=10분, 5=30분")
    trde_qty_tp: str = Field("5", description="거래량구분: 1=전체, 2=백주, 3=천주, 4=만주, 5=십만주")
    stex_tp: str = Field("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합")


class BrokerInstantVolumeRequest(BaseModel):
    """거래원순간거래량요청 (ka10052)."""

    server_mode: ServerMode = Field("real")
    mmcm_cd: str = Field(..., description="회원사코드 (예: 888=외국계합계, 001=키움증권)")
    mrkt_tp: str = Field("0", description="시장구분: 0=전체, 1=코스피, 2=코스닥, 3=종목")
    stk_cd: str = Field("", description="종목코드 (mrkt_tp=3일 때 필수, 예: 005930)")
    qty_tp: str = Field("0", description="수량구분: 0=전체")
    pric_tp: str = Field("0", description="가격구분: 0=전체")
    stex_tp: str = Field("3", description="거래소구분: 1=KRX, 2=NXT, 3=통합")


class TodayPrevContractsRequest(BaseModel):
    """당일전일체결량요청 (ka10055)."""

    server_mode: ServerMode = Field("real")
    stk_cd: str = Field(..., description="종목코드 (예: 005930)")
    tdy_pred: str = Field("1", description="당일전일구분: 1=당일, 2=전일")
