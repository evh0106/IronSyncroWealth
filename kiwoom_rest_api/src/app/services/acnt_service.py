"""계좌 조회 서비스 (국내주식 > 계좌 / ka*, kt* 조회 API 33종).

기존 acnt.acnt 의 HTTP 호출 패턴을 FastAPI 서비스 레이어로 이관합니다.
스펙 기반 범용 POST 호출 방식을 사용합니다.
"""

from __future__ import annotations

from app.core.exceptions import ApiError
from app.schemas.acnt import AcntApiResponse, AcntApiSpec, ServerMode
from app.services.kiwoom_client import kiwoom_post
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL, load_api_keys
from oauth2.oauth import get_unrevoked_token
from acnt.specs import ACCOUNT_API_SPECS

_SERVER_HOSTS: dict[str, str] = {
    "real": HOST_REAL,
    "mock": HOST_MOC,
}

_ACNT_URL_PATH = "/api/dostk/acnt"

# api_id → spec dict 인덱스
_SPEC_INDEX: dict[str, dict] = {s["api_id"]: s for s in ACCOUNT_API_SPECS}


class AcntService:
    def _resolve_token(self, server_mode: ServerMode) -> tuple[str, str]:
        host = _SERVER_HOSTS.get(server_mode)
        if host is None:
            raise ApiError(
                message=f"Unsupported server_mode: {server_mode}",
                code="INVALID_SERVER_MODE",
                status_code=400,
            )
        app_key, _ = load_api_keys(host=host)
        token = get_unrevoked_token(app_key)
        if not token:
            raise ApiError(
                message="No valid access token found. Issue a token first via POST /api/v1/auth/token",
                code="TOKEN_NOT_FOUND",
                status_code=401,
            )
        return host, token

    def list_specs(self) -> list[AcntApiSpec]:
        """사용 가능한 계좌 API 스펙 목록을 반환합니다."""
        return [
            AcntApiSpec(
                api_id=s["api_id"],
                name=s["name"],
                overview=s.get("overview", ""),
                fields=s.get("fields", []),
                request_example=s.get("request_example", {}),
            )
            for s in ACCOUNT_API_SPECS
        ]

    async def call(
        self,
        server_mode: ServerMode,
        api_id: str,
        body: dict,
    ) -> AcntApiResponse:
        """지정된 계좌 API를 호출합니다."""
        if api_id not in _SPEC_INDEX:
            raise ApiError(
                message=f"Unknown acnt api_id: {api_id}",
                code="UNKNOWN_API_ID",
                status_code=400,
                detail={"api_id": api_id, "valid_ids": sorted(_SPEC_INDEX.keys())},
            )
        host, token = self._resolve_token(server_mode)
        data = await kiwoom_post(
            host=host,
            url_path=_ACNT_URL_PATH,
            api_id=api_id,
            token=token,
            body=body,
        )
        return AcntApiResponse(server_mode=server_mode, api_id=api_id, data=data)


def get_acnt_service() -> AcntService:
    return AcntService()
