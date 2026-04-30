"""국내주식 ranking API 요청 스펙 로더."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


_SPECS_PATH = Path(__file__).with_name("ranking_specs.json")


def load_ranking_api_specs() -> list[dict[str, Any]]:
    if not _SPECS_PATH.exists():
        raise FileNotFoundError(f"ranking spec json not found: {_SPECS_PATH}")
    specs: list[dict[str, Any]] = json.loads(_SPECS_PATH.read_text(encoding="utf-8"))

    # 문서상 HHKDB13470100(배당률 상위)에는 CTS_AREA가 필수인데,
    # 원본 추출 JSON 누락 가능성이 있어 로더 단계에서 보정합니다.
    for spec in specs:
        if spec.get("tr_id") != "HHKDB13470100":
            continue
        fields = spec.setdefault("fields", [])
        exists = any(str(f.get("element", "")).upper() == "CTS_AREA" for f in fields)
        if not exists:
            fields.insert(
                0,
                {
                    "element": "CTS_AREA",
                    "required": "Y",
                    "description": "공백",
                },
            )

    return specs


RANKING_API_SPECS = load_ranking_api_specs()
