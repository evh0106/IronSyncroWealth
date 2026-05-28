from __future__ import annotations

import asyncio
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.core.exceptions import ApiError
from app.services.kiwoom_client import kiwoom_post
from chart.db import save_chart_api_response_with_meta
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL
from oauth2.oauth import get_current_unrevoked_token

_SERVER_HOSTS: dict[str, str] = {
    "real": HOST_REAL,
    "mock": HOST_MOC,
}


@dataclass(frozen=True)
class KiwoomRawApiSpec:
    api_id: str
    name: str
    url_path: str
    doc_rel_path: str
    request_fields: list["KiwoomRawRequestField"]


@dataclass(frozen=True)
class KiwoomRawRequestField:
    name: str
    required: bool
    kind: str
    description: str


def _project_root() -> Path:
    # .../kiwoom_rest_api/src/app/services/kiwoom_raw_service.py -> .../kiwoom_rest_api
    return Path(__file__).resolve().parents[3]


def _load_missing_ids(report_path: Path) -> set[str]:
    if not report_path.exists():
        return set()
    with report_path.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    missing = payload.get("missing_in_swagger", [])
    return {str(x).strip() for x in missing if str(x).strip()}


def _parse_doc_link(cell: str) -> str:
    m = re.search(r"\(([^)]+)\)", cell)
    if not m:
        return ""
    return m.group(1).strip()


def _extract_request_fields(doc_path: Path) -> list[KiwoomRawRequestField]:
    if not doc_path.exists():
        return []

    text = doc_path.read_text(encoding="utf-8", errors="ignore")
    start = text.find("## Request")
    if start < 0:
        return []
    end = text.find("## Response", start)
    request_block = text[start:end] if end > start else text[start:]

    fields: list[KiwoomRawRequestField] = []
    seen: set[str] = set()
    in_body_section = False

    for raw in request_block.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if line.startswith("|:---") or line.startswith("|---"):
            continue

        # Preserve leading empty cells (e.g. "||base_dt|...") so section
        # continuation rows remain detectable.
        row = line[1:-1] if line.endswith("|") else line[1:]
        cols = [c.strip() for c in row.split("|")]
        if len(cols) < 6:
            continue
        if cols[0] == "구분" and cols[1] == "Element":
            continue

        section_col = cols[0]
        if section_col == "Body":
            in_body_section = True
        elif section_col and section_col != "Body":
            in_body_section = False

        if not in_body_section:
            continue

        elem = cols[1].lstrip("-").strip()
        if not elem:
            continue

        # Keep only valid JSON key-like names for body input fields.
        elem = re.sub(r"\s+", "_", elem)
        elem = re.sub(r"[^0-9A-Za-z_]", "_", elem)
        if not elem:
            continue
        if elem[0].isdigit():
            elem = f"f_{elem}"

        if elem in seen:
            continue
        seen.add(elem)

        label = cols[2]
        typ = cols[3].upper()
        required = cols[4].upper() == "Y"
        desc = cols[6] if len(cols) > 6 else ""
        merged_desc = " / ".join(x for x in [label, desc] if x)
        kind = "list" if typ == "LIST" else "string"

        fields.append(
            KiwoomRawRequestField(
                name=elem,
                required=required,
                kind=kind,
                description=merged_desc,
            )
        )

    return fields


def _load_catalog(doc_list_path: Path, missing_ids: set[str]) -> list[KiwoomRawApiSpec]:
    if not doc_list_path.exists():
        return []

    specs: list[KiwoomRawApiSpec] = []
    docs_root = doc_list_path.parent
    with doc_list_path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line.startswith("|"):
                continue
            if line.startswith("|No.") or line.startswith("|---"):
                continue

            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) < 7:
                continue

            api_id = parts[1]
            name = parts[2]
            url_path = parts[5]
            doc_rel = _parse_doc_link(parts[6])
            if not api_id or api_id == "공통":
                continue
            if missing_ids and api_id not in missing_ids:
                continue
            if not url_path.startswith("/"):
                continue

            specs.append(
                KiwoomRawApiSpec(
                    api_id=api_id,
                    name=name,
                    url_path=url_path,
                    doc_rel_path=doc_rel,
                    request_fields=_extract_request_fields(docs_root / doc_rel),
                )
            )

    return specs


class KiwoomRawService:
    def __init__(self) -> None:
        root = _project_root()
        report_path = root / "compare_docs_swagger_report.json"
        doc_list_path = root / "docs" / "키움 REST API 문서" / "kiwoom_api_list.md"
        missing_ids = _load_missing_ids(report_path)
        catalog = _load_catalog(doc_list_path, missing_ids)

        self._specs: list[KiwoomRawApiSpec] = catalog
        self._index: dict[str, KiwoomRawApiSpec] = {s.api_id: s for s in catalog}

    def list_specs(self) -> list[KiwoomRawApiSpec]:
        return self._specs

    def _resolve_token(self) -> tuple[str, str, str]:
        token_ctx = get_current_unrevoked_token()
        if not token_ctx:
            raise ApiError(
                message="No valid access token found. Issue a token first via POST /api/v1/auth/token",
                code="TOKEN_NOT_FOUND",
                status_code=401,
            )
        server_mode, token = token_ctx
        host = _SERVER_HOSTS.get(server_mode)
        if host is None:
            raise ApiError(
                message=f"Unsupported server_mode: {server_mode}",
                code="INVALID_SERVER_MODE",
                status_code=400,
            )
        return server_mode, host, token

    async def call(self, api_id: str, body: dict[str, Any]) -> dict[str, Any]:
        spec = self._index.get(api_id)
        if spec is None:
            raise ApiError(
                message=f"Unknown or not-missing api_id: {api_id}",
                code="UNKNOWN_API_ID",
                status_code=400,
            )

        server_mode, host, token = self._resolve_token()
        data = await kiwoom_post(
            host=host,
            url_path=spec.url_path,
            api_id=spec.api_id,
            token=token,
            body=body,
        )

        if spec.doc_rel_path.startswith("chart/"):
            try:
                save_meta = await asyncio.to_thread(
                    save_chart_api_response_with_meta,
                    spec.api_id,
                    body,
                    data,
                )
                if save_meta.get("rows", 0) > 0:
                    list_table = save_meta.get("list_table", "")
                    header_table = save_meta.get("header_table")
                    if header_table:
                        print(
                            f"[CHART DB 저장] api_id={spec.api_id} "
                            f"header_table={header_table}, list_table={list_table}, rows={save_meta['rows']}"
                        )
                    else:
                        print(
                            f"[CHART DB 저장] api_id={spec.api_id} "
                            f"list_table={list_table}, rows={save_meta['rows']}"
                        )
            except Exception:
                # 저장 실패가 API 응답 자체를 막지 않도록 무시
                pass

        return {
            "server_mode": server_mode,
            "api_id": spec.api_id,
            "url_path": spec.url_path,
            "data": data,
        }


_SERVICE = KiwoomRawService()


def get_kiwoom_raw_service() -> KiwoomRawService:
    return _SERVICE
