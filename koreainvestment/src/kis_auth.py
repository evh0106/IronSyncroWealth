from __future__ import annotations

from typing import Any
from oauth2.koreainvestment_oauth2 import (
    get_access_token,
    get_approval_key,
    revoke_access_token,
)


def issue_access_token(grant_type: str = "client_credentials") -> dict[str, Any]:
    return get_access_token(grant_type=grant_type)


def issue_ws_approval_key(grant_type: str = "client_credentials") -> dict[str, Any]:
    return get_approval_key(grant_type=grant_type)


def issue_access_token_revoke(token: str) -> dict[str, Any]:
    return revoke_access_token(token=token)
