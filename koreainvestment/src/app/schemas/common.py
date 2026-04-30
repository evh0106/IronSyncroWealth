"""Common schemas for generic API calls."""

from typing import Any, Literal

from pydantic import BaseModel, Field


ServerMode = Literal["real", "demo"]


class ApiSpecSummary(BaseModel):
    key: str
    name: str
    tr_id: str
    method: str
    url: str


class ApiCallRequest(BaseModel):
    server_mode: ServerMode = Field(default="real")
    access_token: str | None = Field(default=None, description="Optional access token override")
    query_params: dict[str, str] = Field(default_factory=dict)
    body_params: dict[str, str] = Field(default_factory=dict)
    save_db: bool = Field(default=True, description="Persist result to DB when saver exists")
    tr_id: str | None = Field(default=None, description="Optional TR_ID override for trading APIs")


class ApiCallResponse(BaseModel):
    key: str
    name: str
    tr_id: str
    method: str
    url: str
    request: dict[str, Any] = Field(default_factory=dict)
    saved_rows: int = 0
    response: dict[str, Any] = Field(default_factory=dict)