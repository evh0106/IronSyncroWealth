"""차트 API 응답 DB 저장 유틸.

db/dbschema_chart.sql 테이블 규칙을 기준으로, 차트 응답을 API ID별 테이블에 저장한다.
"""

from __future__ import annotations

from typing import Any

import db


_table_exists_cache: dict[str, bool] = {}
_table_columns_cache: dict[str, set[str]] = {}


def _table_exists(cur, table_name: str) -> bool:
    cached = _table_exists_cache.get(table_name)
    if cached is not None:
        return cached

    cur.execute(
        """
        SELECT 1
          FROM information_schema.TABLES
         WHERE TABLE_SCHEMA = DATABASE()
           AND TABLE_NAME = %s
         LIMIT 1
        """,
        (table_name,),
    )
    exists = cur.fetchone() is not None
    _table_exists_cache[table_name] = exists
    return exists


def _table_columns(cur, table_name: str) -> set[str]:
    cached = _table_columns_cache.get(table_name)
    if cached is not None:
        return cached

    cur.execute(
        """
        SELECT COLUMN_NAME
          FROM information_schema.COLUMNS
         WHERE TABLE_SCHEMA = DATABASE()
           AND TABLE_NAME = %s
        """,
        (table_name,),
    )
    cols = {row["COLUMN_NAME"] for row in cur.fetchall()}
    _table_columns_cache[table_name] = cols
    return cols


def _insert_row(cur, table_name: str, row: dict[str, Any]) -> int:
    cols = _table_columns(cur, table_name)
    payload = {k: v for k, v in row.items() if k in cols and v is not None}

    if payload:
        keys = list(payload.keys())
        cols_sql = ", ".join(keys)
        vals_sql = ", ".join(["%s"] * len(keys))
        sql = f"INSERT INTO {table_name} ({cols_sql}) VALUES ({vals_sql})"
        cur.execute(sql, tuple(payload[k] for k in keys))
    else:
        # fetched_at default만으로 1행 생성
        cur.execute(f"INSERT INTO {table_name} () VALUES ()")
    return cur.lastrowid


def _apply_request_fields(target: dict[str, Any], req_body: dict[str, Any], table_cols: set[str]) -> None:
    for k, v in req_body.items():
        req_key = f"req_{k}"
        if req_key in table_cols:
            target[req_key] = v
        elif k in table_cols:
            target[k] = v


def _find_primary_list_key(data: dict[str, Any]) -> str | None:
    for k, v in data.items():
        if isinstance(v, list):
            return k
    return None


def save_chart_api_response(api_id: str, req_body: dict[str, Any], data: dict[str, Any]) -> int:
    """차트 API 응답을 dbschema_chart.sql 대상 테이블에 저장한다.

    Returns
    -------
    int
        저장된 LIST 행 수
    """
    if not isinstance(data, dict):
        return 0
    if data.get("return_code") not in (None, 0):
        return 0

    list_key = _find_primary_list_key(data)
    if not list_key:
        return 0

    list_rows = data.get(list_key)
    if not isinstance(list_rows, list) or not list_rows:
        return 0

    list_table = f"{api_id}_{list_key}"
    header_table = f"{api_id}_header"

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            if not _table_exists(cur, list_table):
                return 0

            scalar_ctx: dict[str, Any] = {
                k: v
                for k, v in data.items()
                if k not in {"return_code", "return_msg", list_key} and not isinstance(v, list)
            }

            header_id: int | None = None
            if _table_exists(cur, header_table):
                header_cols = _table_columns(cur, header_table)
                header_row: dict[str, Any] = {}
                _apply_request_fields(header_row, req_body, header_cols)
                for k, v in scalar_ctx.items():
                    if k in header_cols:
                        header_row[k] = v
                header_id = _insert_row(cur, header_table, header_row)

            list_cols = _table_columns(cur, list_table)
            inserted = 0
            for item in list_rows:
                if not isinstance(item, dict):
                    continue

                row: dict[str, Any] = {}
                _apply_request_fields(row, req_body, list_cols)
                for k, v in scalar_ctx.items():
                    if k in list_cols:
                        row[k] = v

                if header_id is not None and "header_id" in list_cols:
                    row["header_id"] = header_id

                for k, v in item.items():
                    if k in list_cols:
                        row[k] = v

                _insert_row(cur, list_table, row)
                inserted += 1

        conn.commit()
        return inserted
    finally:
        conn.close()


def save_chart_api_response_with_meta(
    api_id: str,
    req_body: dict[str, Any],
    data: dict[str, Any],
) -> dict[str, Any]:
    """차트 API 응답 저장 후 메타 정보를 반환한다."""
    if not isinstance(data, dict) or data.get("return_code") not in (None, 0):
        return {"rows": 0, "list_table": "", "header_table": None}

    list_key = _find_primary_list_key(data)
    if not list_key:
        return {"rows": 0, "list_table": "", "header_table": None}

    list_table = f"{api_id}_{list_key}"
    header_table = f"{api_id}_header"
    rows = save_chart_api_response(api_id=api_id, req_body=req_body, data=data)
    return {
        "rows": rows,
        "list_table": list_table,
        "header_table": header_table,
    }
