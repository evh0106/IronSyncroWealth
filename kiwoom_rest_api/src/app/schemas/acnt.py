"""계좌 API 요청/응답 스키마."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field

ServerMode = Literal["real", "mock"]


class AcntApiRequest(BaseModel):
    """계좌 API 범용 요청.

    ``api_id`` 에 해당하는 API를 호출합니다.
    ``body`` 에는 해당 API의 요청 필드를 넣습니다.  빈 바디(``{}``)도 허용됩니다.
    """

    server_mode: ServerMode = Field("real", description="서버 모드 (real/mock)")
    body: dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Kiwoom API 요청 바디. api_id에 따라 필요한 필드를 채워 넣습니다. "
            "필드가 없는 API(예: ka00001)는 빈 오브젝트 {} 전달."
        ),
    )


class AcntApiResponse(BaseModel):
    """계좌 API 범용 응답 래퍼."""

    server_mode: ServerMode
    api_id: str
    data: dict[str, Any] = Field(description="Kiwoom API 원본 응답")


class AcntApiSpec(BaseModel):
    """단일 계좌 API 스펙 (Swagger 용)."""

    api_id: str
    name: str
    overview: str
    fields: list[dict[str, Any]]
    request_example: dict[str, Any]


class AcntApiSpecListResponse(BaseModel):
    """계좌 API 스펙 목록 응답."""

    total: int
    specs: list[AcntApiSpec]
