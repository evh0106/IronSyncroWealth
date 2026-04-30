from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT_DIR / "kis_devlp.yaml"


def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def load_config(config_path: Path | None = None) -> dict[str, Any]:
    path = config_path or CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(
            f"설정 파일을 찾을 수 없습니다: {path}. kis_devlp.yaml.example을 복사해 생성하세요."
        )

    with path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    appkey_path = cfg.get("appkey_path")
    secretkey_path = cfg.get("secretkey_path")

    if appkey_path and not cfg.get("my_app"):
        cfg["my_app"] = _read_text_file(ROOT_DIR / appkey_path)
    if secretkey_path and not cfg.get("my_sec"):
        cfg["my_sec"] = _read_text_file(ROOT_DIR / secretkey_path)

    required_keys = ["my_app", "my_sec", "my_url", "my_url_vts", "env_dv"]
    missing = [k for k in required_keys if not cfg.get(k)]
    if missing:
        raise ValueError(f"필수 설정 누락: {', '.join(missing)}")

    return cfg
