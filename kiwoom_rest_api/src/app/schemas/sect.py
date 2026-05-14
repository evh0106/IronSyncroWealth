"""업종 API 요청/응답 스키마."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

ServerMode = Literal["real", "mock"]


class SectCurrentPriceRequest(BaseModel):
    """업종현재가요청 (ka20001) 파라미터."""

    mrkt_tp: str = Field(
        "0",
        description="시장구분: 0=코스피, 1=코스닥, 2=코스피200",
    )
    sect_cd: str = Field(
        "001",
        description=(
            "업종코드: 001=종합(KOSPI), 002=대형주, 003=중형주, 004=소형주, "
            "101=종합(KOSDAQ), 201=KOSPI200, 302=KOSTAR, 701=KRX100"
        ),
    )


class SectCurrentPriceResponse(BaseModel):
    """업종현재가요청 (ka20001) 응답 래퍼."""

    server_mode: ServerMode
    api_id: str = "ka20001"
    data: dict[str, Any] = Field(description="Kiwoom API 원본 응답")
