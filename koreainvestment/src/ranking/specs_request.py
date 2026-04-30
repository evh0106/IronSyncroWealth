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

    # 문서상 FHKST11860000(시간외예상체결등락률)는 FID_COND_MRKT_DIV_CODE가 필요하나,
    # 추출 JSON 누락 가능성이 있어 로더 단계에서 보정합니다.
    for spec in specs:
        if spec.get("tr_id") != "FHKST11860000":
            continue

        fields = spec.setdefault("fields", [])
        exists = any(str(f.get("element", "")).upper() == "FID_COND_MRKT_DIV_CODE" for f in fields)
        if exists:
            continue

        fields.insert(
            0,
            {
                "element": "FID_COND_MRKT_DIV_CODE",
                "required": "Y",
                "description": "시장구분코드 (주식 J)",
            },
        )

    # 문서상 FHKST190900C0(대량체결건수 상위)는 fid_aply_rang_prc_2가 필요하나,
    # 추출 JSON 누락 가능성이 있어 로더 단계에서 보정합니다.
    for spec in specs:
        if spec.get("tr_id") != "FHKST190900C0":
            continue

        fields = spec.setdefault("fields", [])
        exists = any(str(f.get("element", "")).lower() == "fid_aply_rang_prc_2" for f in fields)
        if exists:
            continue

        insert_idx = len(fields)
        for idx, field in enumerate(fields):
            if str(field.get("element", "")).lower() == "fid_aply_rang_prc_1":
                insert_idx = idx + 1
                break

        fields.insert(
            insert_idx,
            {
                "element": "fid_aply_rang_prc_2",
                "required": "Y",
                "description": "~ 가격",
            },
        )

    # 문서상 FHPST01820000(예상체결 상승/하락상위)는 조회 파라미터가 필요하나,
    # 추출 JSON에서 fields가 비어 있을 수 있어 로더 단계에서 보정합니다.
    for spec in specs:
        if spec.get("tr_id") != "FHPST01820000":
            continue

        fields = spec.setdefault("fields", [])
        if fields:
            continue

        spec["sheet_found"] = True
        fields.extend(
            [
                {
                    "element": "fid_cond_mrkt_div_code",
                    "required": "Y",
                    "description": "시장구분코드 (J:KRX, NX:NXT)",
                },
                {
                    "element": "fid_cond_scr_div_code",
                    "required": "Y",
                    "description": "Unique key(20182)",
                },
                {
                    "element": "fid_input_iscd",
                    "required": "Y",
                    "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200",
                },
                {
                    "element": "fid_rank_sort_cls_code",
                    "required": "Y",
                    "description": "0:상승률순, 1:하락률순",
                },
                {
                    "element": "fid_div_cls_code",
                    "required": "Y",
                    "description": "0:전체",
                },
                {
                    "element": "fid_input_price_1",
                    "required": "Y",
                    "description": "가격 ~",
                },
                {
                    "element": "fid_input_price_2",
                    "required": "Y",
                    "description": "~ 가격",
                },
                {
                    "element": "fid_vol_cnt",
                    "required": "Y",
                    "description": "거래량 ~",
                },
                {
                    "element": "fid_trgt_cls_code",
                    "required": "Y",
                    "description": "0:전체",
                },
                {
                    "element": "fid_trgt_exls_cls_code",
                    "required": "Y",
                    "description": "0:전체",
                },
            ]
        )

    return specs


RANKING_API_SPECS = load_ranking_api_specs()
