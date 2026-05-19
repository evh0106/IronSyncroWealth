"""Utility: dynamically register per-spec POST routes for Swagger UI discoverability."""

from __future__ import annotations

from collections.abc import Callable
import inspect
from functools import lru_cache
from pathlib import Path
import re
from typing import Any

from fastapi import APIRouter, Depends, Query

from app.schemas.common import ApiCallRequest, ApiCallResponse, ServerMode
from app.services.market_service import MarketApiService


_FIELD_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_]+$")
_TR_ID_TOKEN_PATTERN = re.compile(r"\b[A-Z]{2,}[A-Z0-9]+\b")


@lru_cache(maxsize=1)
def _load_md_spec_overrides() -> dict[str, dict[str, str]]:
    """Load method/name/TR_ID overrides from markdown specs under docs/한국투자증권_오픈API."""
    project_root = Path(__file__).resolve().parents[4]
    docs_root = project_root / "docs" / "한국투자증권_오픈API"
    if not docs_root.exists():
        return {}

    overrides: dict[str, dict[str, str]] = {}
    url_re = re.compile(r"(?m)^-\s*URL\s*명\s*:\s*(/uapi/\S+)")
    method_re = re.compile(r"(?m)^-\s*HTTP\s*Method\s*:\s*([A-Z]+)")
    name_re = re.compile(r"(?m)^-\s*API\s*명\s*:\s*([^\r\n]+)")
    tr_re = re.compile(r"(?m)^-\s*실전\s*TR_ID\s*:\s*([^\r\n]+)")
    tr_demo_re = re.compile(r"(?m)^-\s*모의\s*TR_ID\s*:\s*([^\r\n]+)")

    for md in docs_root.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue

        url_m = url_re.search(text)
        if not url_m:
            continue
        url = url_m.group(1).strip()
        if url in overrides:
            continue

        method_m = method_re.search(text)
        name_m = name_re.search(text)
        tr_m = tr_re.search(text)
        tr_demo_m = tr_demo_re.search(text)

        tr_id = ""
        if tr_m:
            token_m = _TR_ID_TOKEN_PATTERN.search(tr_m.group(1))
            tr_id = token_m.group(0) if token_m else tr_m.group(1).strip()

        tr_id_demo = ""
        if tr_demo_m:
            token_m = _TR_ID_TOKEN_PATTERN.search(tr_demo_m.group(1))
            tr_id_demo = token_m.group(0) if token_m else tr_demo_m.group(1).strip()

        overrides[url] = {
            "method": method_m.group(1).strip().upper() if method_m else "",
            "name": name_m.group(1).strip() if name_m else "",
            "tr_id": tr_id,
            "tr_id_demo": tr_id_demo,
        }

    return overrides


def _extract_readable_fields(fields: list[dict[str, Any]]) -> list[dict[str, Any]]:
    readable: list[dict[str, Any]] = []
    for field in fields:
        element = str(field.get("element", "") or "").strip()
        if not element:
            continue
        # Skip embedded request/response JSON examples accidentally captured as field rows.
        if "\n" in element or "\r" in element:
            continue
        if not _FIELD_NAME_PATTERN.match(element):
            continue
        readable.append(field)
    return readable


def _spec_key(url: str, marker: str) -> str:
    if marker in url:
        return url.split(marker, 1)[1].strip("/")
    return (url or "").rstrip("/").split("/")[-1]


def _build_description(spec: dict[str, Any], response_spec: dict[str, Any] | None = None) -> str:
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

    if response_spec:
        response_fields = _extract_readable_fields(response_spec.get("fields", []) or [])
        if response_fields:
            lines.append("")
            lines.append("**응답 필드**:")
            max_fields = 80
            for idx, f in enumerate(response_fields):
                if idx >= max_fields:
                    lines.append(f"- ... (총 {len(response_fields)}개 중 {max_fields}개 표시)")
                    break
                elem = str(f.get("element", "") or "")
                field_type = str(f.get("type", "") or "")
                req = "✅ 필수" if f.get("required") == "Y" else "선택"
                desc = str(f.get("description", "") or "").replace("\r\n", " ").replace("\n", " ").strip()

                entry = f"- `{elem}`"
                meta_parts: list[str] = [req]
                if field_type:
                    meta_parts.append(field_type)
                entry += f" ({', '.join(meta_parts)})"
                if desc:
                    entry += f": {desc}"
                lines.append(entry)

    return "\n".join(lines)


def _make_body_handler(api_key: str, service_dep: Callable[[], MarketApiService]) -> Callable:
    """Return a body-based route handler closed over *api_key*."""

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


def _make_query_handler(
    api_key: str,
    service_dep: Callable[[], MarketApiService],
    fields: list[dict[str, Any]],
) -> Callable:
    """Return a query-based handler with dynamic signature for Swagger input fields."""

    query_fields: list[dict[str, Any]] = []
    seen: set[str] = set()
    for f in fields:
        name = str(f.get("element", "") or "").strip()
        if not name or name in seen:
            continue
        # Swagger query parameter names must be valid Python identifiers for signature injection.
        if not name.isidentifier():
            continue
        query_fields.append(f)
        seen.add(name)

    query_field_names = [str(f.get("element", "") or "") for f in query_fields]

    def handler(**kwargs: Any) -> ApiCallResponse:
        service: MarketApiService = kwargs.pop("service")
        server_mode: ServerMode = kwargs.pop("server_mode")
        access_token: str | None = kwargs.pop("access_token")
        save_db: bool = kwargs.pop("save_db")
        tr_id: str | None = kwargs.pop("tr_id")

        query_params = {
            name: kwargs[name]
            for name in query_field_names
            if name in kwargs and kwargs[name] is not None
        }

        return service.call(
            api_key=api_key,
            server_mode=server_mode,
            access_token=access_token,
            query_params=query_params,
            body_params={},
            save_db=save_db,
            tr_id=tr_id,
        )

    params: list[inspect.Parameter] = []
    for f in query_fields:
        name = str(f.get("element", "") or "")
        required = f.get("required") == "Y"
        desc = str(f.get("description", "") or "").replace("\r\n", " ").replace("\n", " ").strip()
        default = Query(... if required else None, description=desc or None)
        annotation: Any = str if required else (str | None)
        params.append(
            inspect.Parameter(
                name=name,
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=default,
                annotation=annotation,
            )
        )

    params.extend(
        [
            inspect.Parameter(
                name="server_mode",
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=Query("real", description="KIS server mode"),
                annotation=ServerMode,
            ),
            inspect.Parameter(
                name="access_token",
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=Query(None, description="Optional access token override"),
                annotation=str | None,
            ),
            inspect.Parameter(
                name="save_db",
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=Query(True, description="Persist result to DB when saver exists"),
                annotation=bool,
            ),
            inspect.Parameter(
                name="tr_id",
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=Query(None, description="Optional TR_ID override for trading APIs"),
                annotation=str | None,
            ),
            inspect.Parameter(
                name="service",
                kind=inspect.Parameter.KEYWORD_ONLY,
                default=Depends(service_dep),
                annotation=MarketApiService,
            ),
        ]
    )

    handler.__signature__ = inspect.Signature(parameters=params, return_annotation=ApiCallResponse)
    handler.__name__ = "call_" + api_key.replace("-", "_").replace("/", "_") + "_get"
    return handler


def register_spec_routes(
    router: APIRouter,
    specs: list[dict[str, Any]],
    marker: str,
    service_dep: Callable[[], MarketApiService],
    tags: list[str],
    response_specs_by_tr_id: dict[str, dict[str, Any]] | None = None,
) -> None:
    """Iterate *specs* and attach one endpoint per spec to *router* using spec method."""
    md_overrides_by_url = _load_md_spec_overrides()

    for spec in specs:
        url = str(spec.get("url", "") or "")
        key = _spec_key(url, marker)
        if not key:
            continue
        spec_for_route = dict(spec)
        md_override = md_overrides_by_url.get(url)
        if md_override:
            if md_override.get("name"):
                spec_for_route["name"] = md_override["name"]
            if md_override.get("method"):
                spec_for_route["method"] = md_override["method"]
            if md_override.get("tr_id"):
                spec_for_route["tr_id"] = md_override["tr_id"]
            if md_override.get("tr_id_demo"):
                spec_for_route["tr_id_demo"] = md_override["tr_id_demo"]

        name = str(spec_for_route.get("name", "") or key)
        tr_id = str(spec_for_route.get("tr_id", "") or "")
        response_spec = response_specs_by_tr_id.get(tr_id) if response_specs_by_tr_id else None
        desc = _build_description(spec_for_route, response_spec)
        api_id = str(spec_for_route.get("api_id", "") or "")
        method = str(spec_for_route.get("method", "POST") or "POST").upper()
        if method not in {"GET", "POST", "PUT", "DELETE", "PATCH"}:
            method = "POST"
        identifier = api_id or tr_id
        summary = f"{name} [{identifier}]" if identifier else name

        handler = _make_query_handler(key, service_dep, spec_for_route.get("fields", []) or []) if method == "GET" else _make_body_handler(key, service_dep)

        router.add_api_route(
            f"/{key}",
            handler,
            methods=[method],
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
