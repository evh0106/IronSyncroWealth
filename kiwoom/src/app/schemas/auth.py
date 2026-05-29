"""Authentication and token schemas."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


ServerMode = Literal["real", "mock"]


class TokenIssueRequest(BaseModel):
    server_mode: ServerMode = Field(default="real", description="Kiwoom server mode")
    reuse_cached: bool = Field(default=True, description="Reuse non-revoked token from DB if available")


class Au10001Request(BaseModel):
    grant_type: str = Field(..., description="client_credentials")
    appkey: str = Field(..., description="Kiwoom app key")
    secretkey: str = Field(..., description="Kiwoom secret key")


class TokenIssueResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    server_mode: ServerMode
    host: str
    reused_cached_token: bool
    app_key_source: str
    token: str
    token_type: str = "Bearer"
    expires_dt: str = ""
    return_code: int | str = 0
    return_msg: str = ""


class TokenRevokeRequest(BaseModel):
    server_mode: ServerMode = Field(default="real", description="Kiwoom server mode")
    token: str | None = Field(default=None, description="Token to revoke; if omitted, try current cached token")


class Au10002Request(BaseModel):
    appkey: str = Field(..., description="Kiwoom app key")
    secretkey: str = Field(..., description="Kiwoom secret key")
    token: str = Field(..., description="Access token to revoke")


class TokenRevokeResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    server_mode: ServerMode
    host: str
    revoked_token: str
    return_code: int | str
    return_msg: str


class TokenStatusResponse(BaseModel):
    server_mode: ServerMode
    host: str
    app_key_source: str
    has_cached_token: bool
    cached_token: str | None = None
