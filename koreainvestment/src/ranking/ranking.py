"""국내주식 ranking API 콘솔 메뉴."""

from __future__ import annotations

from datetime import datetime, timedelta
import json
import re
from typing import Any

import requests

from db import get_connection
from kis_config import load_config
from logger import log_http_request, log_http_response
from ranking._fmt import _ljust, _rjust
from ranking.specs_request import RANKING_API_SPECS
from ranking.specs_response import RANKING_API_RESPONSE_SPECS_BY_TR_ID


def _base_url(cfg: dict[str, Any]) -> str:
    return cfg["my_url_vts"] if cfg.get("env_dv") == "demo" else cfg["my_url"]


def _norm_col(name: str) -> str:
    text = (name or "").strip().lower()
    text = re.sub(r"[^a-z0-9_]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    if not text:
        return "field"
    if text[0].isdigit():
        return f"f_{text}"
    return text


def _table_name_from_url(url: str) -> str:
    return _norm_col((url or "").rstrip("/").split("/")[-1])


TR_ID_TO_TABLE: dict[str, str] = {
    spec.get("tr_id", ""): _table_name_from_url(spec.get("url", ""))
    for spec in RANKING_API_SPECS
    if spec.get("tr_id")
}

_TABLE_COLUMNS_CACHE: dict[str, set[str]] = {}
_INSERT_SQL_CACHE: dict[str, tuple[str, list[str]]] = {}
_RESP_SKIP_FIELDS = {"rt_cd", "msg_cd", "msg1", "output", "output1", "output2"}


def _infer_default(element: str, description: str) -> str:
    desc = (description or "").strip()
    elem = element.upper()

    if elem == "F_DT":
        return (datetime.now() - timedelta(days=365)).strftime("%Y%m%d")

    if elem == "T_DT":
        return datetime.now().strftime("%Y%m%d")

    # 일부 ranking API는 기간 파라미터를 필수로 요구하므로 기본 기간을 보정합니다.
    if "INPUT_DATE_1" in elem:
        return (datetime.now() - timedelta(days=7)).strftime("%Y%m%d")

    if "INPUT_DATE_2" in elem:
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

    if "BLNG_CLS_CODE" in elem:
        return "0"

    if "MKOP_CLS_CODE" in elem:
        return "0"

    if "PBMN" in elem:
        return "0"

    if "APLY_RANG_PRC" in elem:
        return "0"

    if "INPUT_PRICE" in elem or "VOL" in elem:
        return "0"

    m = re.search(r"([A-Za-z0-9]+)\s*[:(]", desc)
    if m:
        return m.group(1)

    return ""


def _normalize_yyyymmdd(value: str) -> str:
    digits = re.sub(r"\D", "", value or "")
    return digits if len(digits) == 8 else value


def _extract_missing_input_field(msg1: Any) -> str | None:
    text = str(msg1 or "")
    m = re.search(r"INPUT FIELD NOT FOUND\s*\[\s*([A-Za-z0-9_]+)\s*\]", text, re.IGNORECASE)
    return m.group(1) if m else None


def _ensure_missing_field_param(params: dict[str, str], missing_field: str) -> bool:
    missing_upper = missing_field.upper()
    existing_key = next((k for k in params if k.upper() == missing_upper), None)

    target_key = existing_key or missing_field
    current_value = params.get(target_key, "")
    if current_value:
        return False

    value = _infer_default(target_key, "")
    if "DATE" in target_key.upper():
        value = _normalize_yyyymmdd(value)

    params[target_key] = value
    return existing_key is None or bool(value)


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


def _get_table_columns(cur: Any, table: str) -> set[str]:
    cached = _TABLE_COLUMNS_CACHE.get(table)
    if cached is not None:
        return cached

    cur.execute(f"SHOW COLUMNS FROM `{table}`")
    cols = {r["Field"] for r in cur.fetchall()}
    _TABLE_COLUMNS_CACHE[table] = cols
    return cols


def _prepare_insert_sql(table: str, insert_cols: list[str]) -> tuple[str, list[str]]:
    key = f"{table}|{'|'.join(insert_cols)}"
    cached = _INSERT_SQL_CACHE.get(key)
    if cached is not None:
        return cached

    col_sql = ", ".join([f"`{c}`" for c in insert_cols])
    placeholders = ", ".join([f"%({c})s" for c in insert_cols])
    sql = f"INSERT INTO `{table}` ({col_sql}) VALUES ({placeholders})"
    prepared = (sql, insert_cols)
    _INSERT_SQL_CACHE[key] = prepared
    return prepared


def _extract_top_rsp_values(result: dict[str, Any]) -> dict[str, str]:
    values: dict[str, str] = {}

    # Top-level scalar fields
    for key, value in result.items():
        if isinstance(value, (dict, list)):
            continue
        values[key] = "" if value is None else str(value)

    return values


def _extract_array_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for key in ("output", "output1", "output2"):
        value = result.get(key)
        if isinstance(value, dict):
            rows.append(value)
        elif isinstance(value, list):
            rows.extend([row for row in value if isinstance(row, dict)])

    return rows


def _collect_rsp_row_data(tr_id: str, top_values: dict[str, str], row_values: dict[str, Any] | None = None) -> dict[str, str]:
    spec = RANKING_API_RESPONSE_SPECS_BY_TR_ID.get(tr_id, {})

    row_scalar: dict[str, str] = {}
    if row_values:
        for k, v in row_values.items():
            if not isinstance(v, (dict, list)):
                row_scalar[k] = "" if v is None else str(v)

    row_data: dict[str, str] = {}
    seen_cols: set[str] = set()
    for field in spec.get("fields", []):
        element = str(field.get("element", "")).strip()
        if not element or element in _RESP_SKIP_FIELDS:
            continue

        col = f"rsp_{_norm_col(element)}"
        if col in seen_cols:
            continue
        seen_cols.add(col)
        row_data[col] = row_scalar.get(element, top_values.get(element, ""))

    return row_data


def save_ranking_result(spec: dict[str, Any], params: dict[str, str], result: dict[str, Any]) -> int:
    tr_id = spec.get("tr_id", "")
    table = TR_ID_TO_TABLE.get(tr_id)
    if not table:
        return 0

    base_row: dict[str, Any] = {
        "tr_id": tr_id,
        "req_url": spec.get("url", ""),
        "rt_cd": str(result.get("rt_cd", "") or ""),
        "msg_cd": str(result.get("msg_cd", "") or ""),
        "msg1": str(result.get("msg1", "") or ""),
        "response_json": json.dumps(result, ensure_ascii=False),
    }

    for key, value in params.items():
        base_row[f"req_{_norm_col(key)}"] = value

    top_rsp_values = _extract_top_rsp_values(result)
    rsp_rows = _extract_array_rows(result)
    if not rsp_rows:
        rsp_rows = [{}]

    payload_rows: list[dict[str, Any]] = []
    for rsp_row in rsp_rows:
        row_data = dict(base_row)
        row_data.update(_collect_rsp_row_data(tr_id, top_rsp_values, rsp_row))
        payload_rows.append(row_data)

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            available_cols = _get_table_columns(cur, table)

            insert_cols = [c for c in payload_rows[0] if c in available_cols and c != "id"]
            if not insert_cols:
                return 0

            sql, sql_cols = _prepare_insert_sql(table, insert_cols)
            payload = [{c: row.get(c, "") for c in sql_cols} for row in payload_rows]

            cur.executemany(sql, payload)

        conn.commit()
        print(f"  [DB 저장] {table}: {len(payload_rows)}행 저장됨")
        return len(payload_rows)
    except Exception as exc:
        conn.rollback()
        print(f"  [DB 오류] {type(exc).__name__}: {exc}")
        raise
    finally:
        conn.close()


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
        if "DATE" in element.upper():
            value = _normalize_yyyymmdd(value)
        params[element] = value

    print("\n  → 조회 중...")

    max_retry = 10
    retry_count = 0
    while True:
        result = call_ranking_api(token, spec, params)
        missing_field = _extract_missing_input_field(result.get("msg1"))

        if not missing_field or retry_count >= max_retry:
            break

        changed = _ensure_missing_field_param(params, missing_field)
        if not changed:
            break

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

    try:
        save_ranking_result(spec, params, result)
    except Exception:
        pass

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
