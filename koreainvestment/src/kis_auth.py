from __future__ import annotations

from typing import Any

from oauth2.oauth import (
    get_access_token,
    get_cached_access_token,
    get_approval_key,
    revoke_access_token,
)


def issue_access_token(
    grant_type: str = "client_credentials",
    env_dv: str | None = None,
    reuse_cached: bool = True,
) -> dict[str, Any]:
    return get_access_token(grant_type=grant_type, env_dv=env_dv, reuse_cached=reuse_cached)


def issue_cached_access_token(env_dv: str | None = None) -> dict[str, Any] | None:
    return get_cached_access_token(env_dv=env_dv)


def issue_ws_approval_key(
    grant_type: str = "client_credentials",
    env_dv: str | None = None,
) -> dict[str, Any]:
    return get_approval_key(grant_type=grant_type, env_dv=env_dv)


def issue_access_token_revoke(token: str, env_dv: str | None = None) -> dict[str, Any]:
    return revoke_access_token(token=token, env_dv=env_dv)
