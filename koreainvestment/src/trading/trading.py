"""국내주식 trading API 콘솔 메뉴."""

from __future__ import annotations

from datetime import datetime
import json
import re
from typing import Any

import requests

from kis_config import load_config
from logger import log_http_request, log_http_response
from ranking._fmt import _ljust, _rjust
from trading.specs_request import TRADING_API_SPECS


def _base_url(cfg: dict[str, Any]) -> str:
    return cfg["my_url_vts"] if cfg.get("env_dv") == "demo" else cfg["my_url"]


def _pick_account_number(cfg: dict[str, Any]) -> str:
    env_demo = cfg.get("env_dv") == "demo"
    candidates = []
    if env_demo:
        candidates = [cfg.get("my_paper_stock"), cfg.get("my_acct_stock"), cfg.get("my_prod")]
    else:
        candidates = [cfg.get("my_acct_stock"), cfg.get("my_prod"), cfg.get("my_paper_stock")]

    for raw in candidates:
        text = re.sub(r"\D", "", str(raw or ""))
        if len(text) >= 8:
            return text[:8]
    return ""


def _infer_default(element: str, description: str, cfg: dict[str, Any]) -> str:
    elem = (element or "").upper()
    desc = (description or "").strip()

    if elem == "CANO":
        return _pick_account_number(cfg)

    if elem == "ACNT_PRDT_CD":
        prod = str(cfg.get("my_prod", "") or "")
        if len(prod) == 2 and prod.isdigit():
            return prod
        return "01"

    if elem == "PDNO":
        return "005930"

    if elem in {"ORD_DVSN", "SLL_BUY_DVSN_CD"}:
        return "00"

    if elem in {"ORD_QTY", "ORD_UNPR", "PRIC", "QTY", "AMT"} or any(k in elem for k in ["ORD_QTY", "ORD_UNPR", "QTY", "AMT", "PRIC"]):
        return "0"

    if "INQR_STRT_DT" in elem or "STRT_DT" in elem or elem in {"F_DT", "INQR_FROM_DT"}:
        return datetime.now().strftime("%Y%m%d")

    if "INQR_END_DT" in elem or "END_DT" in elem or elem in {"T_DT", "INQR_TO_DT"}:
        return datetime.now().strftime("%Y%m%d")

    if "CTX_AREA_FK" in elem or "CTX_AREA_NK" in elem:
        return ""

    if "CMA_EVLU_AMT_ICLD_YN" in elem or "OVRS_ICLD_YN" in elem or elem.endswith("_YN"):
        return "N"

    if "TR_MKET_CODE" in elem:
        return "00"

    if "SORT" in elem or "DVSN" in elem or "CLS_CODE" in elem:
        return "0"

    if "입력값 없을때 전체" in desc or "공백" in desc:
        return ""

    m = re.search(r"([A-Za-z0-9_]+)\s*[:(]", desc)
    if m:
        return m.group(1)

    return ""


def _normalize_input(value: str, element: str) -> str:
    upper = (element or "").upper()
    digits = re.sub(r"\D", "", value or "")

    if "DT" in upper and len(digits) == 8:
        return digits

    if "TIME" in upper or "TMD" in upper or "HOUR" in upper:
        if len(digits) in {4, 6}:
            return digits

    return value


def _extract_missing_input_field(msg1: Any) -> str | None:
    text = str(msg1 or "")
    m = re.search(r"INPUT FIELD NOT FOUND\s*\[\s*([A-Za-z0-9_]+)\s*\]", text, re.IGNORECASE)
    return m.group(1) if m else None


def _build_headers(token: str, tr_id: str, cfg: dict[str, Any]) -> dict[str, str]:
    return {
        "content-type": "application/json; charset=utf-8",
        "authorization": f"Bearer {token}",
        "appkey": cfg["my_app"],
        "appsecret": cfg["my_sec"],
        "tr_id": tr_id,
        "custtype": "P",
    }


def _issue_hashkey(base_url: str, cfg: dict[str, Any], payload: dict[str, str]) -> str:
    res = requests.post(
        base_url + "/uapi/hashkey",
        headers={
            "content-type": "application/json; charset=utf-8",
            "appkey": cfg["my_app"],
            "appsecret": cfg["my_sec"],
        },
        data=json.dumps(payload, ensure_ascii=False),
        timeout=20,
    )
    res.raise_for_status()
    body = res.json()
    return str(body.get("HASH") or body.get("hash") or "")


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
        "odno",
        "ord_tmd",
        "pdno",
        "prdt_name",
        "ord_qty",
        "ord_unpr",
        "tot_ccld_qty",
        "tot_ccld_amt",
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


def _pick_tr_id(spec: dict[str, Any], cfg: dict[str, Any]) -> str:
    if cfg.get("env_dv") == "demo":
        return str(spec.get("tr_id_demo") or spec.get("tr_id") or "")
    return str(spec.get("tr_id") or "")


def _confirm_post_send(spec: dict[str, Any], tr_id: str, query_params: dict[str, str], body_params: dict[str, str]) -> bool:
    print("\n  [POST 전송 확인]")
    print(f"  API: {spec.get('name', '')}")
    print(f"  TR_ID: {tr_id}")
    print(f"  URL: {spec.get('url', '')}")
    if query_params:
        print(f"  Query: {json.dumps(query_params, ensure_ascii=False)}")
    if body_params:
        print(f"  Body: {json.dumps(body_params, ensure_ascii=False)}")

    confirm = input("  실제 전송하려면 'yes' 입력 (기본: 취소): ").strip().lower()
    return confirm == "yes"


def call_trading_api(
    token: str,
    spec: dict[str, Any],
    tr_id: str,
    query_params: dict[str, str],
    body_params: dict[str, str],
) -> dict[str, Any]:
    cfg = load_config()
    base = _base_url(cfg)
    url = base + spec["url"]
    method = str(spec.get("method", "GET")).upper()

    headers = _build_headers(token, tr_id, cfg)
    if method == "POST":
        payload = {k: v for k, v in body_params.items()}
        if payload:
            hashkey = _issue_hashkey(base, cfg, payload)
            if hashkey:
                headers["hashkey"] = hashkey

    session = requests.Session()
    request_kwargs: dict[str, Any] = {"headers": headers}
    if query_params:
        request_kwargs["params"] = query_params
    if method == "POST":
        request_kwargs["data"] = json.dumps(body_params, ensure_ascii=False)

    req = requests.Request(method, url, **request_kwargs)
    preq = session.prepare_request(req)

    _, req_id = log_http_request(
        api_id=tr_id,
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


def print_trading_api(token: str, spec: dict[str, Any]) -> None:
    cfg = load_config()
    tr_id = _pick_tr_id(spec, cfg)
    method = str(spec.get("method", "GET")).upper()

    print(f"\n[{spec['name']}]")
    print(f"TR_ID(default): {tr_id}")
    print(f"Method: {method}")
    print(f"URL: {spec['url']}")
    print("-" * 80)

    tr_id_input = input("  TR_ID override (엔터 시 기본값 사용): ").strip()
    if tr_id_input:
        tr_id = tr_id_input

    query_params: dict[str, str] = {}
    body_params: dict[str, str] = {}

    for field in spec.get("fields", []):
        element = str(field.get("element", ""))
        location = str(field.get("location", "query"))
        desc = str(field.get("description", ""))

        default = _infer_default(element, desc, cfg)
        hint = f" ({desc})" if desc else ""
        value = input(f"  [{location}] {element}{hint} [기본값: {default!r}]: ").strip()
        if not value:
            value = default
        value = _normalize_input(value, element)

        if location == "body":
            body_params[element] = value
        else:
            query_params[element] = value

    if method == "POST":
        if not _confirm_post_send(spec, tr_id, query_params, body_params):
            print("\n  [중단] POST 전송이 취소되었습니다.")
            return

    print("\n  → 조회 중...")

    max_retry = 10
    retry_count = 0
    while True:
        result = call_trading_api(token, spec, tr_id, query_params, body_params)
        missing_field = _extract_missing_input_field(result.get("msg1"))

        if not missing_field or retry_count >= max_retry:
            break

        missing_upper = missing_field.upper()
        target = None
        for f in spec.get("fields", []):
            if str(f.get("element", "")).upper() == missing_upper:
                target = f
                break

        if not target:
            break

        location = str(target.get("location", "query"))
        default = _infer_default(missing_field, str(target.get("description", "")), cfg)
        default = _normalize_input(default, missing_field)

        if location == "body":
            if body_params.get(missing_field):
                break
            body_params[missing_field] = default
        else:
            if query_params.get(missing_field):
                break
            query_params[missing_field] = default

        retry_count += 1
        print(f"  [안내] 누락 필드 감지: {missing_field} -> 기본값 보정 후 재조회 ({retry_count}/{max_retry})")

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


def run_trading_menu(token: str) -> None:
    specs = TRADING_API_SPECS

    while True:
        print("\n" + "=" * 84)
        print("[국내주식 Trading API 메뉴]")
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
            print_trading_api(token, spec)
        except requests.HTTPError as exc:
            print(f"\n[오류] HTTP 요청 실패: {exc}")
            if exc.response is not None:
                print(exc.response.text)
        except Exception as exc:
            print(f"\n[오류] trading 조회 실패: {exc}")
