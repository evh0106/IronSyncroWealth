from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from kis_auth import issue_access_token, issue_access_token_revoke, issue_ws_approval_key


def main() -> None:
    access = issue_access_token()
    access_token = access.get("access_token")
    print("[ACCESS TOKEN]")
    print(f"token_type: {access.get('token_type')}")
    print(f"expires_in: {access.get('expires_in')}")
    print(f"has_access_token: {bool(access_token)}")

    approval = issue_ws_approval_key()
    print("\n[WS APPROVAL]")
    print(f"approval_key: {approval.get('approval_key')}")
    print(f"message: {approval.get('message') or approval.get('msg1')}")

    if access_token:
        revoke = issue_access_token_revoke(access_token)
        print("\n[TOKEN REVOKE]")
        print(f"code: {revoke.get('code')}")
        print(f"message: {revoke.get('message')}")


if __name__ == "__main__":
    main()
