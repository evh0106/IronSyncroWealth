"""문서 기반 업무 API 공통 런타임 유틸리티."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re

import requests

from logger import log_http_request, log_http_response
from oauth2 import HOST


_API_ID_PATTERN = re.compile(r"^[A-Za-z]{2}\d{5}$")


@dataclass(slots=True)
class ApiDocSpec:
    api_id: str
    name: str
    url: str


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

        specs.append(ApiDocSpec(api_id=api_id, name=name, url=url))

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


def _prompt_body() -> dict:
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

    while True:
        _print_api_list(title, specs)
        spec = _select_spec(specs)
        if spec is None:
            return

        print(f"\n[{spec.name} ({spec.api_id})]")
        print("-" * 60)
        body = _prompt_body()

        try:
            response = _post(token, spec.url or default_url_path, spec.api_id, body, log_name=log_name)
            payload = response.json()
            print("\n[응답]")
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        except requests.HTTPError as exc:
            print(f"\n[HTTP 오류] {exc}")
        except Exception as exc:
            print(f"\n[오류] {type(exc).__name__}: {exc}")

        input("\n엔터를 누르면 목록으로 돌아갑니다...")
