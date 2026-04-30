"""Token service for FastAPI auth endpoints."""

from __future__ import annotations

from kis_auth import (
    issue_access_token,
    issue_access_token_revoke,
    issue_cached_access_token,
    issue_ws_approval_key,
)
from kis_config import load_config

from app.core.exceptions import ApiError
from app.schemas.auth import ApprovalIssueResponse, TokenIssueResponse, TokenRevokeResponse, TokenStatusResponse


class TokenService:
    def _host(self, server_mode: str) -> str:
        cfg = load_config()
        return cfg["my_url_vts"] if server_mode == "demo" else cfg["my_url"]

    def get_cached_token_status(self, server_mode: str = "real") -> TokenStatusResponse:
        cached = issue_cached_access_token(env_dv=server_mode)
        return TokenStatusResponse(
            server_mode=server_mode,
            host=self._host(server_mode),
            has_cached_token=bool(cached and cached.get("access_token")),
            cached_token=(cached or {}).get("access_token"),
        )

    def issue_token(self, server_mode: str = "real", reuse_cached: bool = True) -> TokenIssueResponse:
        try:
            data = issue_access_token(env_dv=server_mode, reuse_cached=reuse_cached)
        except Exception as exc:
            raise ApiError("토큰 발급 실패", code="TOKEN_ISSUE_FAILED", status_code=502, detail={"reason": str(exc)}) from exc

        token = str(data.get("access_token", "") or "")
        if not token:
            raise ApiError("토큰 발급 응답에 access_token이 없습니다.", code="TOKEN_EMPTY", status_code=502, detail=data)

        return TokenIssueResponse(
            server_mode=server_mode,
            host=self._host(server_mode),
            reused_cached_token=bool(data.get("_from_cache")),
            token=token,
            token_type=str(data.get("token_type", "Bearer") or "Bearer"),
            expires_at=str(data.get("access_token_token_expired", "") or ""),
            raw=data,
        )

    def revoke_token(self, server_mode: str = "real", token: str | None = None) -> TokenRevokeResponse:
        revoked_token = token or ((issue_cached_access_token(env_dv=server_mode) or {}).get("access_token"))
        if not revoked_token:
            raise ApiError("폐기할 토큰이 없습니다.", code="TOKEN_NOT_FOUND", status_code=404)

        try:
            data = issue_access_token_revoke(revoked_token, env_dv=server_mode)
        except Exception as exc:
            raise ApiError("토큰 폐기 실패", code="TOKEN_REVOKE_FAILED", status_code=502, detail={"reason": str(exc)}) from exc

        return TokenRevokeResponse(
            server_mode=server_mode,
            host=self._host(server_mode),
            revoked_token=revoked_token,
            code=str(data.get("code", "") or ""),
            message=str(data.get("message", "") or ""),
            raw=data,
        )

    def issue_approval_key(self, server_mode: str = "real") -> ApprovalIssueResponse:
        try:
            data = issue_ws_approval_key(env_dv=server_mode)
        except Exception as exc:
            raise ApiError("웹소켓 승인키 발급 실패", code="APPROVAL_ISSUE_FAILED", status_code=502, detail={"reason": str(exc)}) from exc

        return ApprovalIssueResponse(
            server_mode=server_mode,
            host=self._host(server_mode),
            approval_key=str(data.get("approval_key", "") or ""),
            message=str(data.get("message") or data.get("msg1") or ""),
            raw=data,
        )


def get_token_service() -> TokenService:
    return TokenService()