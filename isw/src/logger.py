from __future__ import annotations

import logging
import os
from logging.handlers import TimedRotatingFileHandler

_LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "log")
_LOG_FILE = os.path.join(_LOG_DIR, "access.log")
_ERROR_LOG_FILE = os.path.join(_LOG_DIR, "error.log")
_DB_LOG_FILE = os.path.join(_LOG_DIR, "db.log")
_WEB_ERROR_LOG_FILE = os.path.join(_LOG_DIR, "webapp_error.log")

os.makedirs(_LOG_DIR, exist_ok=True)

_fmt = logging.Formatter(
    fmt="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)

_file_handler = TimedRotatingFileHandler(
    _LOG_FILE,
    when="midnight",
    backupCount=30,
    encoding="utf-8",
)
_file_handler.setFormatter(_fmt)

_console_handler = logging.StreamHandler()
_console_handler.setFormatter(_fmt)

_error_file_handler = TimedRotatingFileHandler(
    _ERROR_LOG_FILE,
    when="midnight",
    backupCount=30,
    encoding="utf-8",
)
_error_file_handler.setFormatter(_fmt)

_error_console_handler = logging.StreamHandler()
_error_console_handler.setFormatter(_fmt)

_db_file_handler = TimedRotatingFileHandler(
    _DB_LOG_FILE,
    when="midnight",
    backupCount=30,
    encoding="utf-8",
)
_db_file_handler.setFormatter(_fmt)

_db_console_handler = logging.StreamHandler()
_db_console_handler.setFormatter(_fmt)

_web_error_file_handler = TimedRotatingFileHandler(
    _WEB_ERROR_LOG_FILE,
    when="midnight",
    backupCount=30,
    encoding="utf-8",
)
_web_error_file_handler.setFormatter(_fmt)

_web_error_console_handler = logging.StreamHandler()
_web_error_console_handler.setFormatter(_fmt)

access_logger = logging.getLogger("isw.access")
access_logger.setLevel(logging.INFO)
access_logger.addHandler(_file_handler)
access_logger.addHandler(_console_handler)
access_logger.propagate = False

error_logger = logging.getLogger("isw.error")
error_logger.setLevel(logging.ERROR)
error_logger.addHandler(_error_file_handler)
error_logger.addHandler(_error_console_handler)
error_logger.propagate = False

db_logger = logging.getLogger("isw.db")
db_logger.setLevel(logging.INFO)
db_logger.addHandler(_db_file_handler)
db_logger.addHandler(_db_console_handler)
db_logger.propagate = False

web_error_logger = logging.getLogger("isw.web_error")
web_error_logger.setLevel(logging.ERROR)
web_error_logger.addHandler(_web_error_file_handler)
web_error_logger.addHandler(_web_error_console_handler)
web_error_logger.propagate = False
