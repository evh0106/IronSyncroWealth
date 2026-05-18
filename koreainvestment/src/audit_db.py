"""HTTP/WebSocket 요청-응답 원문을 공통 감사 테이블에 저장하는 유틸."""

from __future__ import annotations

import json
from typing import Any

from db import get_connection


_HTTP_TABLE = "http_exchange_log"
_WS_TABLE = "ws_message_log"
_HTTP_TABLE_READY = False
_WS_TABLE_READY = False


def _to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _headers_to_json(headers: Any) -> str:
    if headers is None:
        return ""
    try:
        if isinstance(headers, dict):
            return json.dumps({str(k): str(v) for k, v in headers.items()}, ensure_ascii=False)
        return json.dumps({str(k): str(v) for k, v in dict(headers).items()}, ensure_ascii=False)
    except Exception:
        return _to_text(headers)


def _ensure_http_table() -> None:
    global _HTTP_TABLE_READY
    if _HTTP_TABLE_READY:
        return

    sql = f"""
    CREATE TABLE IF NOT EXISTS `{_HTTP_TABLE}` (
        id BIGINT NOT NULL AUTO_INCREMENT,
        source VARCHAR(64) NOT NULL DEFAULT '',
        direction VARCHAR(16) NOT NULL DEFAULT 'outbound',
        api_id VARCHAR(64) NOT NULL DEFAULT '',
        method VARCHAR(16) NOT NULL DEFAULT '',
        req_url TEXT NULL,
        req_headers LONGTEXT NULL,
        req_body LONGTEXT NULL,
        rsp_status INT NULL,
        rsp_headers LONGTEXT NULL,
        rsp_body LONGTEXT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        INDEX idx_http_created_at (created_at),
        INDEX idx_http_source (source),
        INDEX idx_http_api_id (api_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
        _HTTP_TABLE_READY = True
    finally:
        conn.close()


def _ensure_ws_table() -> None:
    global _WS_TABLE_READY
    if _WS_TABLE_READY:
        return

    sql = f"""
    CREATE TABLE IF NOT EXISTS `{_WS_TABLE}` (
        id BIGINT NOT NULL AUTO_INCREMENT,
        source VARCHAR(64) NOT NULL DEFAULT '',
        direction VARCHAR(16) NOT NULL DEFAULT '',
        tr_id VARCHAR(64) NOT NULL DEFAULT '',
        tr_key VARCHAR(128) NOT NULL DEFAULT '',
        payload LONGTEXT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        INDEX idx_ws_created_at (created_at),
        INDEX idx_ws_direction (direction),
        INDEX idx_ws_tr_id (tr_id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
        _WS_TABLE_READY = True
    finally:
        conn.close()


def save_http_exchange(
    *,
    source: str,
    api_id: str,
    method: str,
    req_url: str,
    request_headers: Any,
    request_body: Any,
    response_status: int | None,
    response_headers: Any,
    response_body: Any,
    direction: str = "outbound",
) -> int:
    _ensure_http_table()

    row = {
        "source": str(source or ""),
        "direction": str(direction or "outbound"),
        "api_id": str(api_id or ""),
        "method": str(method or ""),
        "req_url": str(req_url or ""),
        "req_headers": _headers_to_json(request_headers),
        "req_body": _to_text(request_body),
        "rsp_status": response_status,
        "rsp_headers": _headers_to_json(response_headers),
        "rsp_body": _to_text(response_body),
    }

    sql = f"""
    INSERT INTO `{_HTTP_TABLE}`
    (source, direction, api_id, method, req_url, req_headers, req_body, rsp_status, rsp_headers, rsp_body)
    VALUES
    (%(source)s, %(direction)s, %(api_id)s, %(method)s, %(req_url)s, %(req_headers)s, %(req_body)s, %(rsp_status)s, %(rsp_headers)s, %(rsp_body)s)
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, row)
        conn.commit()
        return 1
    finally:
        conn.close()


def save_ws_message(*, source: str, direction: str, payload: Any, tr_id: str = "", tr_key: str = "") -> int:
    _ensure_ws_table()

    row = {
        "source": str(source or ""),
        "direction": str(direction or ""),
        "tr_id": str(tr_id or ""),
        "tr_key": str(tr_key or ""),
        "payload": _to_text(payload),
    }

    sql = f"""
    INSERT INTO `{_WS_TABLE}`
    (source, direction, tr_id, tr_key, payload)
    VALUES
    (%(source)s, %(direction)s, %(tr_id)s, %(tr_key)s, %(payload)s)
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, row)
        conn.commit()
        return 1
    finally:
        conn.close()
