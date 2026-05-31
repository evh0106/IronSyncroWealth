from __future__ import annotations

import logging
import os
from logging.handlers import TimedRotatingFileHandler

_LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "log")
_LOG_FILE = os.path.join(_LOG_DIR, "access.log")

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

access_logger = logging.getLogger("isw.access")
access_logger.setLevel(logging.INFO)
access_logger.addHandler(_file_handler)
access_logger.addHandler(_console_handler)
access_logger.propagate = False
