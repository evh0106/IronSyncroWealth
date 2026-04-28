"""주문 서비스 (국내주식 > 주문 / kt10000~kt10003, kt50000~kt50003).

기존 ordr.ordr 의 HTTP 호출 패턴을 FastAPI 서비스 레이어로 이관합니다.
주문 변경 API (매수/매도/정정/취소) 는 confirm=True 가 반드시 필요합니다.
"""

from __future__ import annotations

from app.core.exceptions import ApiError
from app.schemas.ordr import (
    ORDER_MUTATION_API_IDS,
    OrdrApiResponse,
    OrdrApiSpec,
    ServerMode,
)
from app.services.kiwoom_client import kiwoom_post
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL, load_api_keys
from oauth2.oauth import get_unrevoked_token
from ordr.specs import ORDR_API_SPECS

_SERVER_HOSTS: dict[str, str] = {
    "real": HOST_REAL,
    "mock": HOST_MOC,
}

_ORDR_URL_PATH = "/api/dostk/ordr"

# api_id → spec dict 인덱스
_SPEC_INDEX: dict[str, dict] = {s["api_id"]: s for s in ORDR_API_SPECS}


class OrdrService:
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

    def list_specs(self) -> list[OrdrApiSpec]:
        """사용 가능한 주문 API 스펙 목록을 반환합니다."""
        return [
            OrdrApiSpec(
                api_id=s["api_id"],
                name=s["name"],
                overview=s.get("overview", ""),
                fields=s.get("fields", []),
                request_example=s.get("request_example", {}),
                is_mutation=s["api_id"] in ORDER_MUTATION_API_IDS,
            )
            for s in ORDR_API_SPECS
        ]

    def call(
        self,
        server_mode: ServerMode,
        api_id: str,
        body: dict,
        confirm: bool,
    ) -> OrdrApiResponse:
        """지정된 주문 API를 호출합니다.

        주문 변경 API (is_mutation=True) 는 confirm=True 필수입니다.
        """
        if api_id not in _SPEC_INDEX:
            raise ApiError(
                message=f"Unknown ordr api_id: {api_id}",
                code="UNKNOWN_API_ID",
                status_code=400,
                detail={"api_id": api_id, "valid_ids": sorted(_SPEC_INDEX.keys())},
            )

        if api_id in ORDER_MUTATION_API_IDS and not confirm:
            raise ApiError(
                message=(
                    f"'{api_id}' is an order-mutation API. "
                    "Set confirm=true in the request body to proceed."
                ),
                code="ORDER_CONFIRM_REQUIRED",
                status_code=422,
                detail={"api_id": api_id, "is_mutation": True},
            )

        host, token = self._resolve_token(server_mode)
        data = kiwoom_post(
            host=host,
            url_path=_ORDR_URL_PATH,
            api_id=api_id,
            token=token,
            body=body,
        )
        return OrdrApiResponse(server_mode=server_mode, api_id=api_id, data=data)


def get_ordr_service() -> OrdrService:
    return OrdrService()
