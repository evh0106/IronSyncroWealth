"""DB 연결 헬퍼 (PyMySQL)."""

import os

import pymysql
import pymysql.cursors


_DB_CONFIG: dict = {
    "host": os.environ.get("ISW_DB_HOST", "127.0.0.1"),
    "port": int(os.environ.get("ISW_DB_PORT", "3310")),
    "user": os.environ.get("ISW_DB_USER", "root"),
    "password": os.environ.get("ISW_DB_PASSWORD", "my-secret-pw"),
    "database": os.environ.get("ISW_DB_NAME", "isw_db"),
    "charset": "utf8mb4",
    "autocommit": False,
    "cursorclass": pymysql.cursors.Cursor,
}


def get_conn() -> pymysql.connections.Connection:
    """새 DB 커넥션을 반환한다."""
    return pymysql.connect(**_DB_CONFIG)
