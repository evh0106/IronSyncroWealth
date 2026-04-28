"""WebSocket 세션 제어 API 요청/응답 스키마."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

ServerMode = Literal["real", "mock"]

# 종목 기반 실시간 타입
REALTIME_TYPE_MAP: dict[str, str] = {
    "0B": "주식체결",
    "0C": "주식우선호가",
    "0D": "주식호가잔량",
    "0A": "주식기세",
    "0E": "주식시간외호가",
    "0F": "주식당일거래원",
    "0G": "ETF NAV",
    "0H": "주식예상체결",
    "0g": "주식종목정보",
    "0w": "종목프로그램매매",
    "1h": "VI발동/해제",
    # 계좌 기반 (item 불필요)
    "00": "주문체결 (계좌)",
    "04": "잔고 (계좌)",
    "0s": "장시작시간 (계좌)",
    "0J": "업종지수",
    "0U": "업종등락",
    "0I": "국제금환산가격",
    "0m": "ELW 이론가",
    "0u": "ELW 지표",
}

# 종목코드(item) 불필요한 계좌/공통 타입
ACCOUNT_TYPES = frozenset({"00", "04", "0s", "0J", "0U", "0I", "0m", "0u"})


class WsStartRequest(BaseModel):
    """WebSocket 백그라운드 세션 시작 요청."""

    server_mode: ServerMode = Field("real", description="서버 모드 (real/mock)")
    items: list[str] = Field(
        default_factory=list,
        description=(
            "종목/업종코드 목록. 계좌 기반 타입(00/04/0s 등)만 사용할 경우 빈 배열 가능.  \n"
            "KRX: '005930', NXT: '005930_NX', SOR: '005930_AL'"
        ),
    )
    types: list[str] = Field(
        ...,
        min_length=1,
        description="실시간 항목 타입 코드 목록 (예: ['0B', '0C']). GET /api/v1/ws/types 참조.",
    )
    group_no: str = Field("1", description="WebSocket 그룹 번호 (기본값 '1')")


class WsRegisterRequest(BaseModel):
    """실시간 항목 추가/해제 요청 (세션 실행 중에만 가능)."""

    items: list[str] = Field(
        default_factory=list,
        description="종목/업종코드 목록. 계좌 기반 타입은 빈 배열 가능.",
    )
    types: list[str] = Field(
        ...,
        min_length=1,
        description="실시간 항목 타입 코드 목록",
    )
    group_no: str = Field("1", description="WebSocket 그룹 번호")


class WsSessionStatus(BaseModel):
    """WebSocket 세션 현재 상태."""

    running: bool = Field(description="백그라운드 세션 실행 중 여부")
    server_mode: ServerMode | None = Field(None, description="실행 중인 세션의 서버 모드")
    items: list[str] = Field(default_factory=list, description="등록된 종목코드 목록")
    types: list[str] = Field(default_factory=list, description="등록된 실시간 타입 코드 목록")
    started_at: datetime | None = Field(None, description="세션 시작 시각")
    group_no: str | None = Field(None, description="그룹 번호")


class WsTypeInfo(BaseModel):
    """단일 실시간 타입 정보."""

    code: str
    name: str
    needs_item: bool = Field(description="종목코드(item) 필요 여부")


class WsTypeListResponse(BaseModel):
    """실시간 타입 목록 응답."""

    total: int
    types: list[WsTypeInfo]


class WsOperationResult(BaseModel):
    """세션 제어 결과."""

    success: bool
    message: str
    detail: dict[str, Any] = Field(default_factory=dict)
