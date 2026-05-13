"""국내주식 websocket URL 기능 실행 메뉴."""

from __future__ import annotations

import asyncio
import json
import re
from typing import Any

import requests
import websockets

from audit_db import save_ws_message
from db import get_connection
from kis_auth import issue_access_token, issue_ws_approval_key
from kis_config import load_config
from logger import log_http_request, log_http_response, log_websocket_message
from ranking._fmt import _ljust, _rjust
from websocket.specs_request import WEBSOCKET_REQUEST_SPECS, WEBSOCKET_REQUEST_SPECS_BY_URL
from websocket.specs_response import WEBSOCKET_RESPONSE_SPECS_BY_URL

_REST_URL = "/uapi/domestic-stock/v1/quotations/frgnmem-trade-trend"
_TABLE_COLUMNS_CACHE: dict[str, set[str]] = {}
_INSERT_SQL_CACHE: dict[str, tuple[str, list[str]]] = {}
_RESP_SKIP_FIELDS = {"rt_cd", "msg_cd", "msg1", "output", "output1", "output2"}


def _base_url(cfg: dict[str, Any]) -> str:
    return cfg["my_url_vts"] if cfg.get("env_dv") == "demo" else cfg["my_url"]


def _base_ws_url(cfg: dict[str, Any]) -> str:
    return cfg["my_url_ws_vts"] if cfg.get("env_dv") == "demo" else cfg["my_url_ws"]


def _norm_col(name: str) -> str:
    text = (name or "").strip().lower()
    text = re.sub(r"[^a-z0-9_]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    if not text:
        return "field"
    if text[0].isdigit():
        return f"f_{text}"
    return text


def _table_from_url(url: str) -> str:
    u = str(url or "")
    if u.startswith("/tryitout/"):
        return "tryitout_" + _norm_col(u.split("/tryitout/", 1)[1])

    marker = "/uapi/domestic-stock/v1/"
    if marker in u:
        u = u.split(marker, 1)[1]
    else:
        u = u.strip("/")
    return _norm_col(u.replace("/", "_"))


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


def _collect_rsp_row_data(url: str, top_values: dict[str, str], row_values: dict[str, Any] | None = None) -> dict[str, str]:
    spec = WEBSOCKET_RESPONSE_SPECS_BY_URL.get(url, {})

    row_scalar: dict[str, str] = {}
    if row_values:
        for k, v in row_values.items():
            if not isinstance(v, (dict, list)):
                row_scalar[k] = "" if v is None else str(v)

    row_data: dict[str, str] = {}
    seen_cols: set[str] = set()
    for field in spec.get("fields", []):
        element = str(field.get("element", "")).strip()
        if not element or element.lower() in _RESP_SKIP_FIELDS:
            continue

        col = f"rsp_{_norm_col(element)}"
        if col in seen_cols:
            continue
        seen_cols.add(col)
        row_data[col] = row_scalar.get(element, row_scalar.get(element.lower(), top_values.get(element, top_values.get(element.lower(), ""))))

    return row_data


def save_websocket_result(spec: dict[str, Any], tr_id: str, request_payload: dict[str, Any], response_payload: dict[str, Any]) -> int:
    table = _table_from_url(str(spec.get("url", "")))
    if not table:
        return 0

    result = response_payload if isinstance(response_payload, dict) else {"raw": str(response_payload)}
    base_row: dict[str, Any] = {
        "tr_id": tr_id,
        "req_url": spec.get("url", ""),
        "rt_cd": str(result.get("rt_cd", "") or ""),
        "msg_cd": str(result.get("msg_cd", "") or ""),
        "msg1": str(result.get("msg1", "") or ""),
    }

    for key, value in request_payload.items():
        if isinstance(value, (dict, list)):
            continue
        base_row[f"req_{_norm_col(key)}"] = "" if value is None else str(value)

    top_rsp_values = _extract_top_rsp_values(result)
    rsp_rows = _extract_array_rows(result)
    if not rsp_rows:
        rsp_rows = [{}]

    payload_rows: list[dict[str, Any]] = []
    for rsp_row in rsp_rows:
        row_data = dict(base_row)
        row_data.update(_collect_rsp_row_data(str(spec.get("url", "")), top_rsp_values, rsp_row))
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


def _resolve_tr_id(spec: dict[str, Any], cfg: dict[str, Any]) -> str:
    env_demo = cfg.get("env_dv") == "demo"
    tr_demo = str(spec.get("tr_id_demo", "") or "").strip()
    tr_real = str(spec.get("tr_id", "") or "").strip()

    if env_demo and tr_demo and "미지원" not in tr_demo:
        return tr_demo
    return tr_real


def _infer_default(element: str, description: str) -> str:
    elem = (element or "").strip().upper()
    desc = (description or "").strip()

    if elem == "FID_COND_MRKT_DIV_CODE":
        return "J"
    if elem == "FID_COND_SCR_DIV_CODE":
        m = re.search(r"(\d{5})", desc)
        return m.group(1) if m else "20432"
    if elem == "FID_INPUT_ISCD":
        return "005930"
    if elem == "FID_INPUT_ISCD_2":
        return "99999"
    if elem == "FID_MRKT_CLS_CODE":
        return "A"
    if elem == "FID_VOL_CNT":
        return "0"

    if elem == "TR_ID":
        return ""
    if elem == "TR_KEY":
        upper_desc = desc.upper()
        if "HTS ID" in upper_desc:
            return ""
        if "R+" in upper_desc or "DNAS" in upper_desc or "AAPL" in upper_desc:
            return "DNASAAPL"
        if "업종" in desc:
            return "0001"
        return "005930"

    m = re.search(r"([A-Za-z0-9_]+)\s*[:(]", desc)
    if m:
        return m.group(1)

    if "공란" in desc or "공백" in desc:
        return ""

    return ""


def _build_rest_headers(token: str, tr_id: str, cfg: dict[str, Any]) -> dict[str, str]:
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
        "bsop_hour",
        "mbcr_name",
        "hts_kor_isnm",
        "stck_prpr",
        "prdy_vrss",
        "cntg_vol",
        "acml_ntby_qty",
        "glob_ntby_qty",
    ]
    keys = list(rows[0].keys())
    cols = [k for k in preferred if k in keys]
    for k in keys:
        if k not in cols:
            cols.append(k)
    return cols[:8]


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
    print("  " + "  ".join(_ljust(c, w) for c, w in zip(cols, widths)))
    print("  " + "  ".join("-" * w for w in widths))

    for idx, row in enumerate(rows[:sample_size], 1):
        cells: list[str] = []
        for col, width in zip(cols, widths):
            val = str(row.get(col, ""))
            if val.replace(".", "", 1).replace("-", "", 1).isdigit():
                cells.append(_rjust(val, width))
            else:
                cells.append(_ljust(val, width))
        print(f"  {_rjust(idx, 3)} " + "  ".join(cells))


def _call_frgnmem_trade_trend(token: str) -> dict[str, Any]:
    cfg = load_config()
    spec = WEBSOCKET_REQUEST_SPECS_BY_URL[_REST_URL]
    tr_id = _resolve_tr_id(spec, cfg)
    url = _base_url(cfg) + _REST_URL
    headers = _build_rest_headers(token, tr_id, cfg)

    params: dict[str, str] = {}
    for field in spec.get("fields", []):
        if str(field.get("location", "query")) != "query":
            continue
        element = str(field.get("element", ""))
        desc = str(field.get("description", ""))
        default = _infer_default(element, desc)
        value = input(f"  {element} ({desc}) [기본값: {default!r}]: ").strip() or default
        params[element] = value

    session = requests.Session()
    req = requests.Request("GET", url, headers=headers, params=params)
    preq = session.prepare_request(req)
    _, req_id = log_http_request(
        api_id=tr_id,
        url=preq.url or url,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name="websocket",
    )

    response = session.send(preq, timeout=20)
    log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name="websocket",
    )
    response.raise_for_status()
    result = response.json()

    try:
        save_websocket_result(spec, tr_id, params, result)
    except Exception:
        pass

    return result


def _build_ws_subscribe_payload(approval_key: str, tr_id: str, tr_key: str) -> dict[str, Any]:
    return {
        "header": {
            "approval_key": approval_key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8",
        },
        "body": {
            "input": {
                "tr_id": tr_id,
                "tr_key": tr_key,
            }
        },
    }


def _extract_tr_id_from_message(obj: dict[str, Any], raw_text: str) -> str:
    if "|" in (raw_text or ""):
        parts = [p.strip() for p in raw_text.split("|")]
        if len(parts) >= 2 and re.fullmatch(r"[A-Z0-9]{8}", parts[1]):
            return parts[1]

    for key in ("tr_id", "trid", "TR_ID", "TRID"):
        if key in obj and obj.get(key):
            return str(obj.get(key))

    for key in ("header", "body", "output", "data"):
        value = obj.get(key)
        if isinstance(value, dict):
            nested = _extract_tr_id_from_message(value, raw_text)
            if nested:
                return nested

    m = re.search(r"\b([A-Z0-9]{8})\b", raw_text or "")
    return m.group(1) if m else ""


def _response_field_names(spec: dict[str, Any]) -> list[str]:
    url = str(spec.get("url", ""))
    rsp_spec = WEBSOCKET_RESPONSE_SPECS_BY_URL.get(url, {})
    names: list[str] = []
    for f in rsp_spec.get("fields", []):
        element = str(f.get("element", "")).strip()
        if not element:
            continue
        names.append(element)
    return names


def _decode_pipe_caret_message(spec: dict[str, Any], tr_id: str, raw_text: str) -> dict[str, Any]:
    text = str(raw_text or "")
    parts = text.split("|")
    field_names = _response_field_names(spec)

    if len(parts) < 4 or not field_names:
        return {
            "tr_id": tr_id,
            "message": text,
            "output": [],
        }

    ws_rt_cd = parts[0].strip()
    payload_count = parts[2].strip()
    payload = "|".join(parts[3:])
    values = payload.split("^") if payload else []

    chunk = len(field_names)
    if chunk <= 0:
        return {
            "tr_id": tr_id,
            "message": text,
            "output": [],
        }

    if len(values) < chunk and values:
        values = values + ([""] * (chunk - len(values)))
    elif len(values) % chunk != 0:
        use_len = (len(values) // chunk) * chunk
        values = values[:use_len] if use_len > 0 else []

    rows: list[dict[str, str]] = []
    for i in range(0, len(values), chunk):
        row_values = values[i : i + chunk]
        if len(row_values) < chunk:
            row_values = row_values + ([""] * (chunk - len(row_values)))
        row: dict[str, str] = {}
        for j, name in enumerate(field_names):
            row[name] = row_values[j] if j < len(row_values) else ""
        rows.append(row)

    return {
        "tr_id": tr_id,
        "rt_cd": ws_rt_cd,
        "msg_cd": "",
        "msg1": "",
        "ws_count": payload_count,
        "output": rows,
        "raw_message": text,
    }


def _parse_multi_choice(choice: str, max_len: int) -> list[int]:
    idxs: list[int] = []
    for token in (choice or "").split(","):
        t = token.strip()
        if not t.isdigit():
            continue
        v = int(t)
        if 1 <= v <= max_len and v not in idxs:
            idxs.append(v)
    return idxs


async def _run_ws_stream(subscriptions: list[tuple[dict[str, Any], str, str]], approval_key: str, ws_url: str) -> None:
    if not subscriptions:
        print("\n  [오류] 구독할 항목이 없습니다.")
        return

    sub_map: dict[str, tuple[dict[str, Any], dict[str, str]]] = {}
    for spec, tr_id, tr_key in subscriptions:
        sub_map[tr_id] = (spec, {"tr_id": tr_id, "tr_key": tr_key})

    print(f"\n  연결 URL: {ws_url}")
    print(f"  구독 건수: {len(subscriptions)}")
    for i, (_, tr_id, tr_key) in enumerate(subscriptions, 1):
        print(f"  [{i}] {tr_id} / {tr_key}")

    async with websockets.connect(ws_url) as ws:
        for spec, tr_id, tr_key in subscriptions:
            payload = _build_ws_subscribe_payload(approval_key, tr_id, tr_key)
            payload_text = json.dumps(payload, ensure_ascii=False)
            await ws.send(payload_text)

            try:
                log_websocket_message(payload, direction="send")
            except Exception:
                pass

            try:
                save_ws_message(
                    source="websocket_stream",
                    direction="send",
                    payload=payload,
                    tr_id=tr_id,
                    tr_key=tr_key,
                )
            except Exception:
                pass
            await asyncio.sleep(0.05)

        print("\n  실시간 수신 시작. Enter를 누르면 종료합니다.")

        stop_task = asyncio.create_task(asyncio.to_thread(input, ""))
        recv_task = asyncio.create_task(ws.recv())

        try:
            while True:
                done, _ = await asyncio.wait({stop_task, recv_task}, return_when=asyncio.FIRST_COMPLETED)

                if stop_task in done:
                    print("\n  [중단] 사용자 요청으로 종료합니다.")
                    break

                if recv_task in done:
                    raw = recv_task.result()
                    text = str(raw)

                    msg_tr_id = _extract_tr_id_from_message({}, text)
                    spec_req = sub_map.get(msg_tr_id)
                    if not spec_req and subscriptions:
                        first_spec, first_tr_id, first_tr_key = subscriptions[0]
                        spec_req = (first_spec, {"tr_id": first_tr_id, "tr_key": first_tr_key})

                    try:
                        obj = json.loads(text)
                        mapped = obj

                        msg_tr_id_json = _extract_tr_id_from_message(obj, text)
                        if msg_tr_id_json:
                            msg_tr_id = msg_tr_id_json
                            spec_req = sub_map.get(msg_tr_id) or spec_req

                        if spec_req:
                            spec, _ = spec_req
                            mapped = _decode_pipe_caret_message(spec, msg_tr_id, text)

                        print(json.dumps(mapped, ensure_ascii=False, indent=2))
                        rows = _pick_output_rows(mapped) if isinstance(mapped, dict) else []
                        if rows:
                            _print_rows(rows)

                        log_websocket_message(mapped, direction="recv")

                        if spec_req:
                            spec, req_payload_for_db = spec_req
                            try:
                                save_websocket_result(
                                    spec,
                                    req_payload_for_db.get("tr_id", ""),
                                    req_payload_for_db,
                                    mapped if isinstance(mapped, dict) else {"message": str(mapped)},
                                )
                            except Exception:
                                pass
                    except Exception:
                        if spec_req:
                            spec, req_payload_for_db = spec_req
                            mapped = _decode_pipe_caret_message(spec, req_payload_for_db.get("tr_id", msg_tr_id), text)
                        else:
                            mapped = {"message": text}

                        print(json.dumps(mapped, ensure_ascii=False, indent=2))
                        rows = _pick_output_rows(mapped) if isinstance(mapped, dict) else []
                        if rows:
                            _print_rows(rows)

                        log_websocket_message(mapped, direction="recv")

                        if spec_req:
                            spec, req_payload_for_db = spec_req
                            try:
                                save_websocket_result(
                                    spec,
                                    req_payload_for_db.get("tr_id", ""),
                                    req_payload_for_db,
                                    mapped if isinstance(mapped, dict) else {"message": str(mapped)},
                                )
                            except Exception:
                                pass
                    recv_task = asyncio.create_task(ws.recv())
        finally:
            if not stop_task.done():
                stop_task.cancel()
            if not recv_task.done():
                recv_task.cancel()


def _list_ws_specs() -> list[dict[str, Any]]:
    return [s for s in WEBSOCKET_REQUEST_SPECS if str(s.get("url", "")).startswith("/tryitout/")]


def _run_rest_menu(current_token: str) -> str:
    token = current_token
    if not token:
        access = issue_access_token()
        token = str(access.get("access_token") or "")

    if not token:
        print("\n[오류] access token을 확보하지 못했습니다.")
        return current_token

    print("\n[회원사 실시간 매매동향(틱)]")
    try:
        result = _call_frgnmem_trade_trend(token)
    except requests.HTTPError as exc:
        print(f"\n[오류] HTTP 요청 실패: {exc}")
        if exc.response is not None:
            print(exc.response.text)
        return token
    except Exception as exc:
        print(f"\n[오류] 조회 실패: {exc}")
        return token

    print(f"  rt_cd: {result.get('rt_cd')}")
    print(f"  msg_cd: {result.get('msg_cd')}")
    print(f"  msg1: {result.get('msg1')}")

    rows = _pick_output_rows(result)
    if rows:
        _print_rows(rows)
    else:
        print("\n  output 데이터가 비어 있습니다.")

    return token


def _run_ws_menu() -> None:
    specs = _list_ws_specs()
    cfg = load_config()

    while True:
        print("\n" + "=" * 84)
        print("[국내주식 WebSocket tryitout 메뉴]")
        print("=" * 84)
        for idx, spec in enumerate(specs, 1):
            print(f"  [{idx:02}] {spec['name']} ({spec.get('tr_id','')})")
        print("  [00] 뒤로")

        choice = input("메뉴 선택 (예: 1 또는 1,3,5): ").strip()
        if choice in {"0", "00"}:
            return
        indexes = _parse_multi_choice(choice, len(specs))
        if not indexes:
            print("  숫자를 입력하세요. 여러 개는 쉼표로 구분합니다.")
            continue

        subscriptions: list[tuple[dict[str, Any], str, str]] = []
        for sel in indexes:
            spec = specs[sel - 1]
            tr_id = _resolve_tr_id(spec, cfg)

            tr_key_desc = ""
            for f in spec.get("fields", []):
                if str(f.get("element", "")).lower() == "tr_key":
                    tr_key_desc = str(f.get("description", ""))
                    break
            tr_key_default = _infer_default("tr_key", tr_key_desc)
            tr_key = input(f"  [{spec.get('name')}] tr_key [기본값: {tr_key_default!r}]: ").strip() or tr_key_default
            if not tr_key:
                print("  tr_key 값이 필요합니다.")
                subscriptions = []
                break
            subscriptions.append((spec, tr_id, tr_key))

        if not subscriptions:
            continue

        try:
            approval = issue_ws_approval_key()
            approval_key = str(approval.get("approval_key") or "")
            if not approval_key:
                print("\n[오류] approval_key를 확보하지 못했습니다.")
                continue

            ws_url = _base_ws_url(cfg)
            asyncio.run(_run_ws_stream(subscriptions, approval_key, ws_url))
        except Exception as exc:
            print(f"\n[오류] websocket 실행 실패: {exc}")


def run_websocket_menu(current_access_token: str = "") -> str:
    token = current_access_token

    while True:
        print("\n" + "=" * 84)
        print("[국내주식 WebSocket 기능 메뉴]")
        print("=" * 84)
        print("  [1] 회원사 실시간 매매동향(틱) REST 조회")
        print("  [2] tryitout 실시간 WebSocket 구독")
        print("  [0] 뒤로")

        choice = input("메뉴 선택: ").strip()
        if choice == "0":
            return token
        if choice == "1":
            token = _run_rest_menu(token)
            continue
        if choice == "2":
            _run_ws_menu()
            continue

        print("  유효하지 않은 번호입니다.")
