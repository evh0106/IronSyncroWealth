"""
업종현재가요청 (ka20001)
국내주식 > 업종 > 업종현재가요청

업종코드별 현재가·전일대비·등락률 등을 조회합니다.
"""

import json
import requests
from oauth2 import HOST

# ─────────────────────────────────────────────
# 업종코드 참고표
# ─────────────────────────────────────────────
INDS_CODE_MAP = {
    '001': '종합(KOSPI)',
    '002': '대형주',
    '003': '중형주',
    '004': '소형주',
    '101': '종합(KOSDAQ)',
    '201': 'KOSPI200',
    '302': 'KOSTAR',
    '701': 'KRX100',
}

# 시장구분
MRKT_TP_MAP = {
    '0': '코스피',
    '1': '코스닥',
    '2': '코스피200',
}

# 전일대비기호
PRE_SIG_MAP = {
    '1': '상한',
    '2': '상승',
    '3': '보합',
    '4': '하한',
    '5': '하락',
}


def get_sector_current_price(token: str, mrkt_tp: str = '0', inds_cd: str = '001') -> dict:
    """
    업종현재가요청 (ka20001) 호출

    Parameters
    ----------
    token : str
        Bearer 액세스 토큰
    mrkt_tp : str
        시장구분  0:코스피  1:코스닥  2:코스피200
    inds_cd : str
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
        'inds_cd': inds_cd,
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
    inds_cd = input('  선택 (기본값 001·종합KOSPI): ').strip() or '001'
    if inds_cd not in INDS_CODE_MAP:
        print(f'  잘못된 업종코드: {inds_cd}')
        return

    print(f'\n  → {MRKT_TP_MAP[mrkt_tp]} / {INDS_CODE_MAP[inds_cd]} 조회 중...')

    result = get_sector_current_price(token, mrkt_tp=mrkt_tp, inds_cd=inds_cd)

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

    print()
    print(f'  ┌──────────────────────────────────────')
    print(f'  │  업종    : {INDS_CODE_MAP[inds_cd]} ({inds_cd})')
    print(f'  │  현재가  : {cur_prc}')
    print(f'  │  전일대비: {pred_pre}  ({sig_label})')
    print(f'  │  등락률  : {flu_rt} %')
    print(f'  │  거래량  : {trde_qty}')
    print(f'  │  시가    : {open_pric}')
    print(f'  │  고가    : {high_pric}')
    print(f'  │  저가    : {low_pric}')
    print(f'  └──────────────────────────────────────')

    # 원시 응답 확인이 필요할 경우
    show_raw = input('\n  원시 JSON 출력? (y/N): ').strip().lower()
    if show_raw == 'y':
        print(json.dumps(result, indent=4, ensure_ascii=False))
