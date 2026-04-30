"""Authentication and token schemas."""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


ServerMode = Literal["real", "demo"]


class TokenIssueRequest(BaseModel):
    server_mode: ServerMode = Field(default="real", description="KIS server mode")
    reuse_cached: bool = Field(default=True, description="Reuse DB cached token if available")


class TokenIssueResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    server_mode: ServerMode
    host: str
    reused_cached_token: bool
    token: str
    token_type: str = "Bearer"
    expires_at: str = ""
    raw: dict[str, Any] = Field(default_factory=dict)


class TokenRevokeRequest(BaseModel):
    server_mode: ServerMode = Field(default="real", description="KIS server mode")
    token: str | None = Field(default=None, description="Token to revoke; if omitted cached token is used")


class TokenRevokeResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    server_mode: ServerMode
    host: str
    revoked_token: str
    code: str = ""
    message: str = ""
    raw: dict[str, Any] = Field(default_factory=dict)


class TokenStatusResponse(BaseModel):
    server_mode: ServerMode
    host: str
    has_cached_token: bool
    cached_token: str | None = None


class ApprovalIssueRequest(BaseModel):
    server_mode: ServerMode = Field(default="real", description="KIS server mode")


class ApprovalIssueResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    server_mode: ServerMode
    host: str
    approval_key: str = ""
    message: str = ""
    raw: dict[str, Any] = Field(default_factory=dict)