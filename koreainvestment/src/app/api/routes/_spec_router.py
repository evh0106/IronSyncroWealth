"""Utility: dynamically register per-spec POST routes for Swagger UI discoverability."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from fastapi import APIRouter, Depends

from app.schemas.common import ApiCallRequest, ApiCallResponse
from app.services.market_service import MarketApiService


def _spec_key(url: str, marker: str) -> str:
    if marker in url:
        return url.split(marker, 1)[1].strip("/")
    return (url or "").rstrip("/").split("/")[-1]


def _build_description(spec: dict[str, Any]) -> str:
    api_id = spec.get("api_id", "")
    tr_id = spec.get("tr_id", "")
    tr_id_demo = spec.get("tr_id_demo", "")
    url = spec.get("url", "")
    method = spec.get("method", "GET")
    fields: list[dict[str, Any]] = spec.get("fields", []) or []

    lines: list[str] = []
    if api_id:
        lines.append(f"**API_ID**: `{api_id}`")
    if tr_id:
        lines.append(f"**TR_ID**: `{tr_id}`")
    if tr_id_demo:
        lines.append(f"**TR_ID (모의)**: `{tr_id_demo}`")
    lines += [
        f"**Method**: `{method}`",
        f"**KIS URL**: `{url}`",
    ]

    if fields:
        lines.append("")
        lines.append("**파라미터**:")
        for f in fields:
            req = "✅ 필수" if f.get("required") == "Y" else "선택"
            desc = (f.get("description") or "").replace("\r\n", " ").replace("\n", " ").strip()
            elem = f.get("element", "")
            entry = f"- `{elem}` ({req})"
            if desc:
                entry += f": {desc}"
            lines.append(entry)

    return "\n".join(lines)


def _make_handler(api_key: str, service_dep: Callable[[], MarketApiService]) -> Callable:
    """Return a route handler closed over *api_key*, avoiding loop-variable capture."""

    def handler(
        request: ApiCallRequest,
        service: MarketApiService = Depends(service_dep),
    ) -> ApiCallResponse:
        return service.call(
            api_key=api_key,
            server_mode=request.server_mode,
            access_token=request.access_token,
            query_params=request.query_params,
            body_params=request.body_params,
            save_db=request.save_db,
            tr_id=request.tr_id,
        )

    # FastAPI uses __name__ for operation ID deduplication
    handler.__name__ = "call_" + api_key.replace("-", "_").replace("/", "_")
    return handler


def register_spec_routes(
    router: APIRouter,
    specs: list[dict[str, Any]],
    marker: str,
    service_dep: Callable[[], MarketApiService],
    tags: list[str],
) -> None:
    """Iterate *specs* and attach one POST endpoint per spec to *router*."""
    for spec in specs:
        url = str(spec.get("url", "") or "")
        key = _spec_key(url, marker)
        if not key:
            continue
        name = str(spec.get("name", "") or key)
        desc = _build_description(spec)
        api_id = str(spec.get("api_id", "") or "")
        tr_id = str(spec.get("tr_id", "") or "")
        identifier = api_id or tr_id
        summary = f"{name} [{identifier}]" if identifier else name

        router.add_api_route(
            f"/{key}",
            _make_handler(key, service_dep),
            methods=["POST"],
            response_model=ApiCallResponse,
            summary=summary,
            description=desc,
            operation_id=f"call_{key.replace('-', '_').replace('/', '_')}_{tags[0]}",
            tags=tags,
            responses={
                200: {"description": "KIS API 응답"},
                404: {"description": "등록되지 않은 API"},
                502: {"description": "KIS 서버 오류"},
            },
            openapi_extra={
                "x-api-id": api_id,
                "x-tr-id": tr_id,
                "x-kis-url": url,
            },
        )
