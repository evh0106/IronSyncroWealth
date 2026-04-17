"""
업종현재가요청 (ka20001)
국내주식 > 업종 > 업종현재가요청

업종코드별 현재가·전일대비·등락률 등을 조회합니다.
"""

import json
import requests
from oauth2 import HOST
from sect.specs_request import SECT_API_SPECS
from sect.specs_response import SECT_RESPONSE_SPECS


def _parse_code_map(description: str) -> dict:
    """'key:value, key:value' 형식의 description 문자열을 dict로 변환합니다."""
    result = {}
    for part in description.split(','):
        part = part.strip()
        if ':' in part:
            k, v = part.split(':', 1)
            result[k.strip()] = v.strip()
    return result


# ka20001 요청 스펙에서 필드 정보 추출
_KA20001_SPEC = next(s for s in SECT_API_SPECS if s['api_id'] == 'ka20001')
_REQ_FIELDS   = {f['element']: f for f in _KA20001_SPEC['fields']}

# ka20001 응답 스펙에서 필드 정보 추출
_RESP_FIELDS  = {f['element']: f for f in SECT_RESPONSE_SPECS['ka20001']}

# 코드 → 라벨 맵 (specs에서 동적 생성)
MRKT_TP_MAP  = _parse_code_map(_REQ_FIELDS['mrkt_tp']['description'])
INDS_CODE_MAP = _parse_code_map(_REQ_FIELDS['sect_cd']['description'])
PRE_SIG_MAP  = _parse_code_map(_RESP_FIELDS['pred_pre_sig']['description'])


def get_sector_current_price(token: str, mrkt_tp: str = '0', sect_cd: str = '001') -> dict:
    """
    업종현재가요청 (ka20001) 호출

    Parameters
    ----------
    token : str
        Bearer 액세스 토큰
    mrkt_tp : str
        시장구분  0:코스피  1:코스닥  2:코스피200
    sect_cd : str
        업종코드  001:종합(KOSPI)  101:종합(KOSDAQ)  201:KOSPI200 ...

    Returns
    -------
    dict
        API 응답 JSON
    """
    url = HOST + '/api/dostk/sect'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': 'N',
        'next-key': '',
        'api-id': 'ka20001',
    }

    body = {
        'mrkt_tp': mrkt_tp,
        'inds_cd': sect_cd,
    }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()


def print_sector_price(token: str):
    """대화형으로 업종을 선택하고 현재가 정보를 출력합니다."""

    print('\n[업종현재가요청 (ka20001)]')
    print('─' * 40)
    mrkt_tp = '0'

    print('  업종코드:')
    for k, v in INDS_CODE_MAP.items():
        print(f'    {k}: {v}')
    sect_cd = input('  선택 (기본값 001·종합KOSPI): ').strip() or '001'
    if sect_cd not in INDS_CODE_MAP:
        print(f'  잘못된 업종코드: {sect_cd}')
        return

    print(f'\n  → {MRKT_TP_MAP[mrkt_tp]} / {INDS_CODE_MAP[sect_cd]} 조회 중...')

    result = get_sector_current_price(token, mrkt_tp=mrkt_tp, sect_cd=sect_cd)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    cur_prc    = result.get('cur_prc', 'N/A')
    pred_pre   = result.get('pred_pre', 'N/A')
    flu_rt     = result.get('flu_rt', 'N/A')
    sig_code   = result.get('pred_pre_sig', '')
    sig_label  = PRE_SIG_MAP.get(sig_code, '')
    trde_qty   = result.get('trde_qty', 'N/A')
    open_pric  = result.get('open_pric', 'N/A')
    high_pric  = result.get('high_pric', 'N/A')
    low_pric   = result.get('low_pric', 'N/A')

    def lbl(element: str) -> str:
        return _RESP_FIELDS.get(element, {}).get('label', element)

    print()
    print(f'  ┌──────────────────────────────────────')
    print(f'  │  업종    : {INDS_CODE_MAP[sect_cd]} ({sect_cd})')
    print(f'  │  {lbl("cur_prc"):6}: {cur_prc}')
    print(f'  │  {lbl("pred_pre"):6}: {pred_pre}  ({sig_label})')
    print(f'  │  {lbl("flu_rt"):6}: {flu_rt} %')
    print(f'  │  {lbl("trde_qty"):6}: {trde_qty}')
    print(f'  │  {lbl("open_pric"):6}: {open_pric}')
    print(f'  │  {lbl("high_pric"):6}: {high_pric}')
    print(f'  │  {lbl("low_pric"):6}: {low_pric}')
    print(f'  └──────────────────────────────────────')

    # 원시 응답 확인이 필요할 경우
    show_raw = input('\n  원시 JSON 출력? (y/N): ').strip().lower()
    if show_raw == 'y':
        print(json.dumps(result, indent=4, ensure_ascii=False))
