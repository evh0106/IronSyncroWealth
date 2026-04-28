"""주문 API 요청/응답 스키마."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

ServerMode = Literal["real", "mock"]

# 주문 변경 발생 API (주의 필요)
ORDER_MUTATION_API_IDS = frozenset({
    "kt10000",  # 주식 매수주문
    "kt10001",  # 주식 매도주문
    "kt10002",  # 주식 정정주문
    "kt10003",  # 주식 취소주문
    "kt50000",  # 금현물 매수주문
    "kt50001",  # 금현물 매도주문
    "kt50002",  # 금현물 정정주문
    "kt50003",  # 금현물 취소주문
})


class OrdrApiRequest(BaseModel):
    """주문 API 범용 요청.

    **주문 변경 API** (kt10000/kt10001/kt10002/kt10003/kt50000~kt50003) 호출 시에는
    ``confirm=true`` 를 반드시 지정해야 합니다. 실수로 인한 실 매매 방지 장치입니다.
    """

    server_mode: ServerMode = Field("real", description="서버 모드 (real/mock)")
    body: dict[str, Any] = Field(
        default_factory=dict,
        description="Kiwoom API 요청 바디. api_id에 따라 필요한 필드를 채워 넣습니다.",
    )
    confirm: bool = Field(
        False,
        description=(
            "주문 변경 API(매수/매도/정정/취소) 호출 시 true로 설정해야 합니다. "
            "이중 확인 안전장치입니다."
        ),
    )

    @model_validator(mode="after")
    def _check_confirm_for_mutation(self) -> "OrdrApiRequest":
        # api_id는 route path param에서 오므로 여기서는 검사 불가.
        # 서비스 레이어에서 api_id와 함께 재검사합니다.
        return self


class OrdrApiResponse(BaseModel):
    """주문 API 범용 응답 래퍼."""

    server_mode: ServerMode
    api_id: str
    data: dict[str, Any] = Field(description="Kiwoom API 원본 응답")


class OrdrApiSpec(BaseModel):
    """단일 주문 API 스펙 (Swagger 용)."""

    api_id: str
    name: str
    overview: str
    fields: list[dict[str, Any]]
    request_example: dict[str, Any]
    is_mutation: bool = Field(description="실제 주문 변경 여부 (매수/매도/정정/취소)")


class OrdrApiSpecListResponse(BaseModel):
    """주문 API 스펙 목록 응답."""

    total: int
    specs: list[OrdrApiSpec]
