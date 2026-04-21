"""
MariaDB 연결 헬퍼

접속 정보:
  host     : 127.0.0.1
  port     : 3306
  user     : root
  password : my-secret-pw
  database : kiwoom
"""

import pymysql
import pymysql.cursors

_DB_CONFIG = {
    'host':     '127.0.0.1',
    'port':     3306,
    'user':     'root',
    'password': 'my-secret-pw',
    'database': 'kiwoom_db',
    'charset':  'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': False,
}


def get_connection() -> pymysql.connections.Connection:
    """새 DB 커넥션을 반환합니다."""
    return pymysql.connect(**_DB_CONFIG)
