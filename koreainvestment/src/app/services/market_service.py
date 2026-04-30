"""Generic market API service wrappers for ranking, quotations, and trading."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from kis_auth import issue_access_token
from quotations.quotations import call_quotations_api, save_quotations_result
from quotations.specs_request import QUOTATIONS_API_SPECS
from ranking.ranking import call_ranking_api, save_ranking_result
from ranking.specs_request import RANKING_API_SPECS
from trading.specs_request import TRADING_API_SPECS
from trading.trading import call_trading_api, save_trading_result

from app.core.exceptions import ApiError
from app.schemas.common import ApiCallResponse, ApiSpecSummary


SpecList = list[dict[str, Any]]


def _spec_key(spec: dict[str, Any], marker: str) -> str:
    url = str(spec.get("url", "") or "")
    if marker in url:
        return url.split(marker, 1)[1].strip("/").replace("/", "__")
    return url.rstrip("/").split("/")[-1]


def _resolve_trading_tr_id(spec: dict[str, Any], server_mode: str, override: str | None = None) -> str:
    if override:
        return override
    if server_mode == "demo":
        demo = str(spec.get("tr_id_demo", "") or "").strip()
        if demo and "미지원" not in demo:
            return demo
    return str(spec.get("tr_id", "") or "")


class MarketApiService:
    def __init__(
        self,
        *,
        marker: str,
        specs: SpecList,
        caller: Callable[..., dict[str, Any]],
        saver: Callable[..., int],
        kind: str,
    ) -> None:
        self.marker = marker
        self.specs = specs
        self.caller = caller
        self.saver = saver
        self.kind = kind
        self._by_key = {self._make_key(spec): spec for spec in specs}
        self._by_tr_id = {str(spec.get("tr_id", "")).lower(): spec for spec in specs if spec.get("tr_id")}

    def _make_key(self, spec: dict[str, Any]) -> str:
        return _spec_key(spec, self.marker)

    def list_specs(self) -> list[ApiSpecSummary]:
        return [
            ApiSpecSummary(
                key=self._make_key(spec),
                name=str(spec.get("name", "") or ""),
                tr_id=str(spec.get("tr_id", "") or ""),
                method=str(spec.get("method", "GET") or "GET"),
                url=str(spec.get("url", "") or ""),
            )
            for spec in self.specs
        ]

    def _get_spec(self, api_key: str) -> tuple[str, dict[str, Any]]:
        normalized = (api_key or "").strip()
        spec = self._by_key.get(normalized) or self._by_tr_id.get(normalized.lower())
        if spec is None:
            raise ApiError(
                f"등록되지 않은 API입니다: {api_key}",
                code="API_NOT_FOUND",
                status_code=404,
            )
        return self._make_key(spec), spec

    def _ensure_token(self, server_mode: str, access_token: str | None) -> str:
        if access_token:
            return access_token
        data = issue_access_token(env_dv=server_mode, reuse_cached=True)
        token = str(data.get("access_token", "") or "")
        if not token:
            raise ApiError("호출에 필요한 접근토큰을 확보하지 못했습니다.", code="TOKEN_EMPTY", status_code=502, detail=data)
        return token

    def call(
        self,
        *,
        api_key: str,
        server_mode: str,
        access_token: str | None,
        query_params: dict[str, str],
        body_params: dict[str, str],
        save_db: bool,
        tr_id: str | None,
    ) -> ApiCallResponse:
        key, spec = self._get_spec(api_key)
        token = self._ensure_token(server_mode, access_token)
        query = dict(query_params)
        body = dict(body_params)

        try:
            if self.kind == "trading":
                effective_tr_id = _resolve_trading_tr_id(spec, server_mode, tr_id)
                result = self.caller(token, spec, effective_tr_id, query, body, server_mode)
                saved_rows = self.saver(spec, effective_tr_id, query, body, result) if save_db else 0
                response_tr_id = effective_tr_id
            else:
                result = self.caller(token, spec, query, server_mode)
                saved_rows = self.saver(spec, query, result) if save_db else 0
                response_tr_id = str(spec.get("tr_id", "") or "")
        except ApiError:
            raise
        except Exception as exc:
            raise ApiError(
                f"{self.kind} API 호출 실패",
                code="UPSTREAM_CALL_FAILED",
                status_code=502,
                detail={"reason": str(exc), "api_key": api_key},
            ) from exc

        return ApiCallResponse(
            key=key,
            name=str(spec.get("name", "") or ""),
            tr_id=response_tr_id,
            method=str(spec.get("method", "GET") or "GET"),
            url=str(spec.get("url", "") or ""),
            request={
                "server_mode": server_mode,
                "query_params": query,
                "body_params": body,
                "save_db": save_db,
            },
            saved_rows=saved_rows,
            response=result,
        )


def get_ranking_service() -> MarketApiService:
    return MarketApiService(
        marker="/ranking/",
        specs=RANKING_API_SPECS,
        caller=call_ranking_api,
        saver=save_ranking_result,
        kind="ranking",
    )


def get_quotations_service() -> MarketApiService:
    return MarketApiService(
        marker="/quotations/",
        specs=QUOTATIONS_API_SPECS,
        caller=call_quotations_api,
        saver=save_quotations_result,
        kind="quotations",
    )


def get_trading_service() -> MarketApiService:
    return MarketApiService(
        marker="/trading/",
        specs=TRADING_API_SPECS,
        caller=call_trading_api,
        saver=save_trading_result,
        kind="trading",
    )