"""국내주식 ranking API 콘솔 메뉴."""

from __future__ import annotations

from datetime import datetime, timedelta
import re
from typing import Any

import requests

from kis_config import load_config
from logger import log_http_request, log_http_response
from ranking._fmt import _ljust, _rjust
from ranking.specs_request import RANKING_API_SPECS


def _base_url(cfg: dict[str, Any]) -> str:
    return cfg["my_url_vts"] if cfg.get("env_dv") == "demo" else cfg["my_url"]


def _infer_default(element: str, description: str) -> str:
    desc = (description or "").strip()
    elem = element.upper()

    if elem == "F_DT":
        return (datetime.now() - timedelta(days=365)).strftime("%Y%m%d")

    if elem == "T_DT":
        return datetime.now().strftime("%Y%m%d")

    if "UNIQUE KEY(" in desc.upper():
        m = re.search(r"\(([^)]+)\)", desc)
        if m:
            return m.group(1).strip()

    if "공백" in desc:
        return ""

    if "INPUT_ISCD" in elem:
        return "0000"

    if "COND_MRKT_DIV_CODE" in elem:
        return "J"

    m = re.search(r"([A-Za-z0-9]+)\s*[:(]", desc)
    if m:
        return m.group(1)

    return ""


def _build_headers(token: str, tr_id: str, cfg: dict[str, Any]) -> dict[str, str]:
    return {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {token}",
        "appkey": cfg["my_app"],
        "appsecret": cfg["my_sec"],
        "tr_id": tr_id,
        "custtype": "P",
    }


def _pick_output_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    for key in ("output", "output1", "output2"):
        value = result.get(key)
        if isinstance(value, list) and value:
            return [v for v in value if isinstance(v, dict)]
        if isinstance(value, dict):
            return [value]

    for value in result.values():
        if isinstance(value, list) and value and isinstance(value[0], dict):
            return value
    return []


def _select_columns(rows: list[dict[str, Any]]) -> list[str]:
    if not rows:
        return []

    preferred = [
        "data_rank",
        "mksc_shrn_iscd",
        "stck_shrn_iscd",
        "hts_kor_isnm",
        "stck_prpr",
        "prdy_ctrt",
        "acml_vol",
        "bstp_kor_isnm",
        "ovtm_untp_antc_cnqn",
    ]

    keys = list(rows[0].keys())
    columns = [k for k in preferred if k in keys]
    for key in keys:
        if key not in columns:
            columns.append(key)
    return columns[:8]


def _print_rows(rows: list[dict[str, Any]]) -> None:
    cols = _select_columns(rows)
    if not cols:
        print("  출력 테이블 데이터가 없습니다.")
        return

    sample_size = min(20, len(rows))
    widths: list[int] = []
    for col in cols:
        max_len = len(col)
        for row in rows[:sample_size]:
            max_len = max(max_len, len(str(row.get(col, ""))))
        widths.append(min(max_len + 2, 28))

    print()
    head = "  " + "  ".join(_ljust(c, w) for c, w in zip(cols, widths))
    sep = "  " + "  ".join("-" * w for w in widths)
    print(head)
    print(sep)

    for idx, row in enumerate(rows[:sample_size], 1):
        cells = []
        for col, width in zip(cols, widths):
            val = str(row.get(col, ""))
            if val.replace(".", "", 1).replace("-", "", 1).isdigit():
                cells.append(_rjust(val, width))
            else:
                cells.append(_ljust(val, width))
        print(f"  {_rjust(idx, 3)} " + "  ".join(cells))

    if len(rows) > sample_size:
        print(f"\n  ... 총 {len(rows)}건 중 {sample_size}건 표시")


def call_ranking_api(token: str, spec: dict[str, Any], params: dict[str, str]) -> dict[str, Any]:
    cfg = load_config()
    url = _base_url(cfg) + spec["url"]
    headers = _build_headers(token, spec["tr_id"], cfg)

    session = requests.Session()
    req = requests.Request("GET", url, headers=headers, params=params)
    preq = session.prepare_request(req)
    _, req_id = log_http_request(
        api_id=spec["tr_id"],
        url=preq.url or url,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name="koreainvestment",
    )

    response = session.send(preq, timeout=20)
    log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name="koreainvestment",
    )
    response.raise_for_status()
    return response.json()


def print_ranking_api(token: str, spec: dict[str, Any]) -> None:
    print(f"\n[{spec['name']}]")
    print(f"TR_ID: {spec['tr_id']}")
    print(f"URL: {spec['url']}")
    print("-" * 80)

    params: dict[str, str] = {}
    for field in spec.get("fields", []):
        element = field.get("element", "")
        desc = field.get("description", "")
        default = _infer_default(element, desc)
        hint = f" ({desc})" if desc else ""
        value = input(f"  {element}{hint} [기본값: {default!r}]: ").strip()
        if not value:
            value = default
        params[element] = value

    print("\n  → 조회 중...")
    result = call_ranking_api(token, spec, params)

    rt_cd = result.get("rt_cd")
    msg1 = result.get("msg1")
    msg_cd = result.get("msg_cd")
    if rt_cd is not None:
        print(f"  rt_cd: {rt_cd}")
    if msg_cd:
        print(f"  msg_cd: {msg_cd}")
    if msg1:
        print(f"  msg1: {msg1}")

    rows = _pick_output_rows(result)
    if not rows:
        print("\n  output 데이터가 비어 있습니다.")
        return

    _print_rows(rows)


def run_ranking_menu(token: str) -> None:
    specs = RANKING_API_SPECS

    while True:
        print("\n" + "=" * 84)
        print("[국내주식 Ranking API 메뉴]")
        print("=" * 84)
        for idx, spec in enumerate(specs, 1):
            print(f"  [{idx:02}] {spec['name']} ({spec['tr_id']})")
        print("  [00] 뒤로")

        choice = input("메뉴 선택: ").strip()
        if choice in {"0", "00"}:
            return

        if not choice.isdigit():
            print("  숫자를 입력하세요.")
            continue

        sel = int(choice)
        if sel < 1 or sel > len(specs):
            print("  유효하지 않은 번호입니다.")
            continue

        spec = specs[sel - 1]
        try:
            print_ranking_api(token, spec)
        except requests.HTTPError as exc:
            print(f"\n[오류] HTTP 요청 실패: {exc}")
            if exc.response is not None:
                print(exc.response.text)
        except Exception as exc:
            print(f"\n[오류] ranking 조회 실패: {exc}")
