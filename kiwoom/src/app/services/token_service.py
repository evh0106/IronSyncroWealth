"""FastAPI-facing token service built on top of the existing Kiwoom OAuth modules."""

from __future__ import annotations

from pathlib import Path
import json

import requests

from app.core.exceptions import ApiError
from app.schemas.auth import TokenIssueResponse, TokenRevokeResponse, TokenStatusResponse
from logger import log_http_request, log_http_response
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL, load_api_keys
from oauth2.oauth import get_unrevoked_token, save_au10001_response, save_au10002_response
from oauth2.specs_request import OAUTH2_API_SPECS


_REQ_SPEC = {spec["api_id"]: spec for spec in OAUTH2_API_SPECS}
_SERVER_HOSTS = {
    "real": HOST_REAL,
    "mock": HOST_MOC,
}
_SERVER_ACCOUNT = {
    "real": "65120003",
    "mock": "81241972",
}


def _is_idempotent_revoke_message(message: str) -> bool:
    """이미 폐기되었거나 만료/무효 토큰 케이스를 멱등 성공으로 판단합니다."""
    text = (message or "").lower()
    keywords = (
        "already",
        "revoked",
        "expired",
        "invalid token",
        "not found",
        "폐기",
        "만료",
        "유효하지",
        "존재하지",
        "없습니다",
    )
    return any(word in text for word in keywords)


def _normalize_revoke_token(token: str | None) -> str | None:
    """Swagger 기본 플레이스홀더 입력을 무시하고 실제 토큰만 반환합니다."""
    if token is None:
        return None

    value = token.strip()
    if not value:
        return None

    placeholders = {"string", "null", "none", "undefined", "-"}
    if value.lower() in placeholders:
        return None

    return value


class TokenService:
    def _host_for_mode(self, server_mode: str) -> str:
        host = _SERVER_HOSTS.get(server_mode)
        if host is None:
            raise ApiError(
                message=f"Unsupported server_mode: {server_mode}",
                code="INVALID_SERVER_MODE",
                status_code=400,
            )
        return host

    def _account_source_for_mode(self, server_mode: str) -> str:
        account_no = _SERVER_ACCOUNT[server_mode]
        return f"conf/{account_no}_appkey.txt"

    def _build_request_body(self, api_id: str, values: dict[str, str]) -> dict[str, str]:
        spec = _REQ_SPEC[api_id]
        return {field["element"]: values[field["element"]] for field in spec["fields"]}

    def get_cached_token_status(self, server_mode: str) -> TokenStatusResponse:
        host = self._host_for_mode(server_mode)
        app_key, _ = load_api_keys(host=host)
        cached_token = get_unrevoked_token(app_key)
        return TokenStatusResponse(
            server_mode=server_mode,
            host=host,
            app_key_source=self._account_source_for_mode(server_mode),
            has_cached_token=bool(cached_token),
            cached_token=cached_token,
        )

    def issue_token(self, server_mode: str, reuse_cached: bool = True) -> TokenIssueResponse:
        host = self._host_for_mode(server_mode)
        app_key, app_secret = load_api_keys(host=host)

        if reuse_cached:
            cached_token = get_unrevoked_token(app_key)
            if cached_token:
                return TokenIssueResponse(
                    server_mode=server_mode,
                    host=host,
                    reused_cached_token=True,
                    app_key_source=self._account_source_for_mode(server_mode),
                    token=cached_token,
                    token_type="Bearer",
                    expires_dt="",
                    return_code=0,
                    return_msg="DB cached token reused",
                )

        spec = _REQ_SPEC["au10001"]
        url = host + spec["url"]
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        payload = self._build_request_body(
            "au10001",
            {
                "grant_type": "client_credentials",
                "appkey": app_key,
                "secretkey": app_secret,
            },
        )

        req_id = ""
        try:
            _, req_id = log_http_request(
                api_id="au10001",
                url=url,
                request_headers=headers,
                request_body=json.dumps(payload, ensure_ascii=False),
                log_name="fastapi",
            )
        except Exception:
            req_id = ""

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            response.raise_for_status()
        except requests.RequestException as exc:
            if req_id and getattr(exc, "response", None) is not None:
                try:
                    log_http_response(
                        req_id=req_id,
                        response_status=exc.response.status_code,
                        response_headers=exc.response.headers,
                        response_body=exc.response.text,
                        log_name="fastapi",
                    )
                except Exception:
                    pass
            raise ApiError(
                message="Failed to issue Kiwoom access token",
                code="TOKEN_ISSUE_REQUEST_FAILED",
                status_code=502,
                detail={"reason": str(exc)},
            ) from exc

        if req_id:
            try:
                log_http_response(
                    req_id=req_id,
                    response_status=response.status_code,
                    response_headers=response.headers,
                    response_body=response.text,
                    log_name="fastapi",
                )
            except Exception:
                pass

        result = response.json()

        try:
            save_au10001_response(app_key, "client_credentials", result)
        except Exception as exc:
            raise ApiError(
                message="Token was issued but saving token history failed",
                code="TOKEN_DB_SAVE_FAILED",
                status_code=500,
                detail={"reason": str(exc)},
            ) from exc

        if result.get("return_code") != 0:
            raise ApiError(
                message=result.get("return_msg", "Token issue failed"),
                code="TOKEN_ISSUE_FAILED",
                status_code=502,
                detail=result,
            )

        return TokenIssueResponse(
            server_mode=server_mode,
            host=host,
            reused_cached_token=False,
            app_key_source=self._account_source_for_mode(server_mode),
            token=result.get("token", ""),
            token_type=result.get("token_type", "Bearer"),
            expires_dt=result.get("expires_dt", ""),
            return_code=result.get("return_code", 0),
            return_msg=result.get("return_msg", ""),
        )

    def revoke_token(self, server_mode: str, token: str | None = None) -> TokenRevokeResponse:
        host = self._host_for_mode(server_mode)
        app_key, app_secret = load_api_keys(host=host)
        requested_token = _normalize_revoke_token(token)
        revoke_target = requested_token or get_unrevoked_token(app_key)
        if not revoke_target:
            raise ApiError(
                message="No token was provided and no cached token exists",
                code="TOKEN_NOT_FOUND",
                status_code=404,
            )

        spec = _REQ_SPEC["au10002"]
        url = host + spec["url"]
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        payload = self._build_request_body(
            "au10002",
            {
                "appkey": app_key,
                "secretkey": app_secret,
                "token": revoke_target,
            },
        )

        req_id = ""
        try:
            _, req_id = log_http_request(
                api_id="au10002",
                url=url,
                request_headers=headers,
                request_body=json.dumps(payload, ensure_ascii=False),
                log_name="fastapi",
            )
        except Exception:
            req_id = ""

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
        except requests.RequestException as exc:
            raise ApiError(
                message="Failed to revoke Kiwoom access token",
                code="TOKEN_REVOKE_REQUEST_FAILED",
                status_code=502,
                detail={"reason": str(exc)},
            ) from exc

        if req_id:
            try:
                log_http_response(
                    req_id=req_id,
                    response_status=response.status_code,
                    response_headers=response.headers,
                    response_body=response.text,
                    log_name="fastapi",
                )
            except Exception:
                pass

        try:
            result = response.json()
        except ValueError as exc:
            raise ApiError(
                message="Failed to parse revoke response as JSON",
                code="TOKEN_REVOKE_RESPONSE_PARSE_FAILED",
                status_code=502,
                detail={
                    "status_code": response.status_code,
                    "response_text": response.text,
                },
            ) from exc

        try:
            save_au10002_response(app_key, revoke_target, result)
        except Exception as exc:
            raise ApiError(
                message="Token revoke response received but saving revoke history failed",
                code="TOKEN_REVOKE_DB_SAVE_FAILED",
                status_code=500,
                detail={"reason": str(exc)},
            ) from exc

        return_msg = str(result.get("return_msg", ""))
        if response.status_code >= 400:
            if _is_idempotent_revoke_message(return_msg):
                return TokenRevokeResponse(
                    server_mode=server_mode,
                    host=host,
                    revoked_token=revoke_target,
                    return_code=result.get("return_code", response.status_code),
                    return_msg=return_msg,
                )
            raise ApiError(
                message="Failed to revoke Kiwoom access token",
                code="TOKEN_REVOKE_REQUEST_FAILED",
                status_code=502,
                detail={
                    "status_code": response.status_code,
                    "result": result,
                },
            )

        if result.get("return_code") != 0:
            if _is_idempotent_revoke_message(return_msg):
                return TokenRevokeResponse(
                    server_mode=server_mode,
                    host=host,
                    revoked_token=revoke_target,
                    return_code=result.get("return_code", ""),
                    return_msg=return_msg,
                )
            raise ApiError(
                message=return_msg or "Token revoke failed",
                code="TOKEN_REVOKE_FAILED",
                status_code=502,
                detail=result,
            )

        return TokenRevokeResponse(
            server_mode=server_mode,
            host=host,
            revoked_token=revoke_target,
            return_code=result.get("return_code", 0),
            return_msg=return_msg,
        )



def get_token_service() -> TokenService:
    return TokenService()
