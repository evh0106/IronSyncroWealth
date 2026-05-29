"""문서 기반 업무 API 공통 런타임 유틸리티."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
import json
from pathlib import Path
import re
from typing import Any

import requests
from chart.db import save_chart_api_response_with_meta

from logger import log_http_request, log_http_response
from oauth2 import HOST, get_access_token, load_api_keys


_API_ID_PATTERN = re.compile(r"^[A-Za-z]{2}\d{5}$")


@dataclass(slots=True)
class ApiDocSpec:
    api_id: str
    name: str
    url: str
    request_fields: list["ApiRequestField"]


@dataclass(slots=True)
class ApiRequestField:
    name: str
    required: bool
    kind: str
    description: str


def _extract_request_fields(text: str) -> list[ApiRequestField]:
    start = text.find("## Request")
    if start < 0:
        return []
    end = text.find("## Response", start)
    request_block = text[start:end] if end > start else text[start:]

    fields: list[ApiRequestField] = []
    seen: set[str] = set()
    in_body_section = False

    for raw in request_block.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if line.startswith("|:---") or line.startswith("|---"):
            continue

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

        fields.append(ApiRequestField(name=elem, required=required, kind=kind, description=merged_desc))

    return fields


def _infer_default(field: ApiRequestField) -> Any:
    if field.kind == "list":
        return []

    name = field.name.lower()
    desc = (field.description or "").lower()
    today = datetime.now().strftime("%Y%m%d")
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y%m%d")

    if name in {"stk_cd", "isu_cd", "item_cd", "jongmok_code"} or "종목코드" in desc:
        return "005930"

    if name in {"base_dt", "end_dt", "to_dt", "qry_dt"}:
        return today
    if name in {"start_dt", "from_dt", "fr_dt"}:
        return week_ago
    if name.endswith("_dt") or "yyyymmdd" in desc:
        return today

    if name == "upd_stkpc_tp":
        return "1"

    if "0 or 1" in desc or "0/1" in desc:
        return "1"

    m = re.search(r"예\)\s*([0-9A-Za-z_\-]+)", field.description or "")
    if m:
        return m.group(1)

    return ""


def load_specs_from_doc_dir(doc_dir: Path, default_url_path: str) -> list[ApiDocSpec]:
    """문서 디렉터리의 md 파일을 읽어 API 목록을 구성한다."""
    specs: list[ApiDocSpec] = []

    if not doc_dir.exists():
        return specs

    for md_path in sorted(doc_dir.glob("*.md")):
        api_id = md_path.stem
        if not _API_ID_PATTERN.match(api_id):
            continue

        name = api_id
        url = default_url_path

        try:
            text = md_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = md_path.read_text(encoding="cp949", errors="ignore")

        for line in text.splitlines():
            line = line.strip()
            if line.startswith("- API 명:"):
                value = line.split(":", 1)[1].strip()
                if value:
                    name = value
            elif line.startswith("- URL:"):
                value = line.split(":", 1)[1].strip()
                if value:
                    url = value

        specs.append(
            ApiDocSpec(
                api_id=api_id,
                name=name,
                url=url,
                request_fields=_extract_request_fields(text),
            )
        )

    return specs


def _print_api_list(title: str, specs: list[ApiDocSpec]):
    print(f"\n[{title} API 목록]")
    print("-" * 72)
    for idx, spec in enumerate(specs, 1):
        print(f"  [{idx:02}] {spec.api_id:<8} {spec.name}")
    print("  [0] 뒤로")


def _select_spec(specs: list[ApiDocSpec]) -> ApiDocSpec | None:
    while True:
        choice = input("실행할 API 번호 또는 api-id 입력: ").strip()
        if choice == "0":
            return None

        for idx, spec in enumerate(specs, 1):
            if choice == str(idx) or choice.lower() == spec.api_id.lower():
                return spec

        print(f"  알 수 없는 선택: {choice!r}")


def _prompt_body(spec: ApiDocSpec) -> dict:
    if not spec.request_fields:
        print("  요청 Body JSON 입력 (엔터: {}):")
        raw = input("  > ").strip()
        if not raw:
            return {}

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            print(f"  [입력 오류] JSON 파싱 실패: {exc}")
            return {}

        if not isinstance(parsed, dict):
            print("  [입력 오류] JSON 객체(dict)만 허용됩니다.")
            return {}

        return parsed

    print("  요청 파라미터를 입력하세요. (엔터 시 기본값 적용)")
    body: dict[str, Any] = {}
    for field in spec.request_fields:
        default_value = _infer_default(field)
        required_text = "필수" if field.required else "선택"
        desc = field.description or "-"

        if field.kind == "list":
            prompt = (
                f"  - {field.name} ({required_text}, list) [{desc}] "
                f"[기본값: {json.dumps(default_value, ensure_ascii=False)}]: "
            )
            while True:
                raw = input(prompt).strip()
                if not raw:
                    value = default_value
                    break
                try:
                    value = json.loads(raw)
                except json.JSONDecodeError as exc:
                    print(f"    [입력 오류] JSON 파싱 실패: {exc}")
                    continue
                if not isinstance(value, list):
                    print("    [입력 오류] list 타입(JSON 배열)만 허용됩니다.")
                    continue
                break
        else:
            prompt = f"  - {field.name} ({required_text}) [{desc}] [기본값: {default_value}]: "
            value = input(prompt).strip() or str(default_value)

        if field.required and ((field.kind == "list" and not value) or (field.kind != "list" and not str(value).strip())):
            print(f"    [입력 오류] 필수 항목입니다: {field.name}")
            if field.kind == "list":
                value = default_value
            else:
                value = str(default_value)

        body[field.name] = value

    return body


def _post(token: str, url_path: str, api_id: str, body: dict, log_name: str):
    url = HOST + url_path
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "authorization": f"Bearer {token}",
        "cont-yn": "N",
        "next-key": "",
        "api-id": api_id,
    }

    session = requests.Session()
    req = requests.Request("POST", url, headers=headers, json=body)
    preq = session.prepare_request(req)

    path, req_id = log_http_request(
        api_id=api_id,
        url=url,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name=log_name,
    )
    print(f"  -> 요청 로그 저장: {path}")

    resp = session.send(preq)
    path = log_http_response(
        req_id=req_id,
        response_status=resp.status_code,
        response_headers=resp.headers,
        response_body=resp.text,
        log_name=log_name,
    )
    print(f"  -> 응답 로그 저장: {path}")

    resp.raise_for_status()
    return resp


def _is_invalid_token_payload(payload: Any) -> bool:
    if not isinstance(payload, dict):
        return False

    code = str(payload.get("return_code", "")).strip()
    if code != "3":
        return False

    msg = str(payload.get("return_msg", "") or "")
    return ("8005" in msg) or ("token" in msg.lower() and "유효" in msg)


def run_document_api_menu(
    token: str,
    title: str,
    doc_dir: Path,
    default_url_path: str,
    log_name: str,
):
    """문서에서 API 목록을 동적으로 읽어 공통 메뉴를 실행한다."""
    specs = load_specs_from_doc_dir(doc_dir, default_url_path)

    if not specs:
        print(f"\n[{title}] 문서 기반 API 목록이 없습니다: {doc_dir}")
        return

    current_token = token

    while True:
        _print_api_list(title, specs)
        spec = _select_spec(specs)
        if spec is None:
            return

        print(f"\n[{spec.name} ({spec.api_id})]")
        print("-" * 60)
        body = _prompt_body(spec)

        try:
            response = _post(current_token, spec.url or default_url_path, spec.api_id, body, log_name=log_name)
            payload = response.json()

            if _is_invalid_token_payload(payload):
                print("\n[안내] 토큰이 유효하지 않아 재발급 후 1회 재시도합니다.")
                app_key, app_secret = load_api_keys(host=HOST)
                current_token = get_access_token(app_key, app_secret, host=HOST)
                response = _post(current_token, spec.url or default_url_path, spec.api_id, body, log_name=log_name)
                payload = response.json()

            if log_name == "chart":
                print("\n[응답 요약]")
                print(f"  return_code: {payload.get('return_code')}")
                print(f"  return_msg : {payload.get('return_msg')}")

                save_meta = save_chart_api_response_with_meta(spec.api_id, body, payload)
                rows = int(save_meta.get("rows", 0) or 0)
                list_table = str(save_meta.get("list_table", "") or "")
                header_table = save_meta.get("header_table")
                if rows > 0:
                    if header_table:
                        print(f"  [DB 저장] header_table={header_table}, list_table={list_table}, rows={rows}")
                    else:
                        print(f"  [DB 저장] list_table={list_table}, rows={rows}")
                else:
                    print("  [DB 저장] 저장된 행이 없습니다.")
            else:
                print("\n[응답]")
                print(json.dumps(payload, ensure_ascii=False, indent=2))
        except requests.HTTPError as exc:
            print(f"\n[HTTP 오류] {exc}")
        except Exception as exc:
            print(f"\n[오류] {type(exc).__name__}: {exc}")

        input("\n엔터를 누르면 목록으로 돌아갑니다...")
