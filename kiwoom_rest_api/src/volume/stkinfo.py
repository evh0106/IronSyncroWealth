"""
거래량 종목정보 관련 API (국내주식 > 종목정보)
URL: /api/dostk/stkinfo

포함 API:
  - 거래량갱신요청        (ka10024)
  - 거래원순간거래량요청  (ka10052)
  - 당일전일체결량요청    (ka10055)
"""

import json
import requests
from oauth2 import HOST
from ._fmt import _ljust, _rjust

# ─────────────────────────────────────────────
# 공통 코드표
# ─────────────────────────────────────────────
PRE_SIG_MAP = {
    '1': '상한',
    '2': '상승',
    '3': '보합',
    '4': '하한',
    '5': '하락',
}

MRKT_TP_MAP_3 = {
    '000': '전체',
    '001': '코스피',
    '101': '코스닥',
}

_STKINFO_URL = HOST + '/api/dostk/stkinfo'


def _post(token: str, api_id: str, body: dict) -> dict:
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': 'N',
        'next-key': '',
        'api-id': api_id,
    }
    resp = requests.post(_STKINFO_URL, headers=headers, json=body)
    resp.raise_for_status()
    return resp.json()


# ═══════════════════════════════════════════════════════
# ka10024 – 거래량갱신요청
# ═══════════════════════════════════════════════════════
CYCLE_TP_MAP = {
    '5':   '5일',
    '10':  '10일',
    '20':  '20일',
    '60':  '60일',
    '250': '250일',
}

TRDE_QTY_TP_MAP = {
    '5':    '5천주 이상',
    '10':   '1만주 이상',
    '50':   '5만주 이상',
    '100':  '10만주 이상',
    '200':  '20만주 이상',
    '300':  '30만주 이상',
    '500':  '50만주 이상',
    '1000': '100만주 이상',
}


def get_volume_update(token: str, mrkt_tp: str = '000', cycle_tp: str = '5',
                      trde_qty_tp: str = '5', stex_tp: str = '3') -> dict:
    """거래량갱신요청 (ka10024): 지정 주기 내 거래량이 갱신된 종목 조회"""
    body = {
        'mrkt_tp': mrkt_tp,
        'cycle_tp': cycle_tp,
        'trde_qty_tp': trde_qty_tp,
        'stex_tp': stex_tp,
    }
    return _post(token, 'ka10024', body)


def print_volume_update(token: str):
    """대화형 거래량갱신 조회 (ka10024)"""
    print('\n[거래량갱신요청 (ka10024)]')
    print('─' * 60)

    print('  시장구분: ', end='')
    for k, v in MRKT_TP_MAP_3.items():
        print(f'{k}:{v}', end='  ')
    mrkt_tp = input('\n  선택 (기본값 000·전체): ').strip() or '000'

    print('  주기구분: ', end='')
    for k, v in CYCLE_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    cycle_tp = input('\n  선택 (기본값 5·5일): ').strip() or '5'

    print('  거래량구분: ', end='')
    for k, v in TRDE_QTY_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    trde_qty_tp = input('\n  선택 (기본값 5): ').strip() or '5'

    print(f'\n  → 조회 중...')
    result = get_volume_update(token, mrkt_tp=mrkt_tp, cycle_tp=cycle_tp,
                               trde_qty_tp=trde_qty_tp)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('trde_qty_updt', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("순위", 4)}  {_rjust("종목코드", 12)}  {_ljust("종목명", 24)}  {_rjust("현재가", 10)}  '
          f'{_rjust("등락률", 8)}  {_rjust("이전거래량", 12)}  {_rjust("현재거래량", 12)}  {_rjust("매도호가", 10)}  {_rjust("매수호가", 10)}')
    print(f'  {"─"*4}  {"─"*12}  {"─"*24}  {"─"*10}  '
          f'{"─"*8}  {"─"*12}  {"─"*12}  {"─"*10}  {"─"*10}')
    for i, item in enumerate(items, 1):
        print(f'  {_rjust(i, 4)}  {_rjust(item.get("stk_cd", ""), 12)}  {_ljust(item.get("stk_nm", ""), 24)}  '
              f'{_rjust(item.get("cur_prc", ""), 10)}  {_rjust(item.get("flu_rt", ""), 8)}  '
              f'{_rjust(item.get("prev_trde_qty", ""), 12)}  {_rjust(item.get("now_trde_qty", ""), 12)}  '
              f'{_rjust(item.get("sel_bid", ""), 10)}  {_rjust(item.get("buy_bid", ""), 10)}')

    _ask_raw(result)


# ═══════════════════════════════════════════════════════
# ka10052 – 거래원순간거래량요청
# ═══════════════════════════════════════════════════════
MRKT_TP_MAP_4 = {
    '0': '전체',
    '1': '코스피',
    '2': '코스닥',
    '3': '종목',
}

QTY_TP_MAP = {
    '0':   '전체',
    '1':   '1,000주',
    '2':   '2,000주',
    '10':  '10,000주',
    '30':  '30,000주',
    '50':  '50,000주',
    '100': '100,000주',
}

PRIC_TP_MAP = {
    '0': '전체',
    '1': '1천원 미만',
    '8': '1천원 이상',
    '2': '1천원~2천원',
    '3': '2천원~5천원',
    '4': '5천원~1만원',
    '5': '1만원 이상',
}


def get_broker_instant_volume(token: str, mmcm_cd: str, mrkt_tp: str = '0',
                               stk_cd: str = '', qty_tp: str = '0',
                               pric_tp: str = '0', stex_tp: str = '3') -> dict:
    """거래원순간거래량요청 (ka10052)"""
    body = {
        'mmcm_cd': mmcm_cd,
        'stk_cd': stk_cd,
        'mrkt_tp': mrkt_tp,
        'qty_tp': qty_tp,
        'pric_tp': pric_tp,
        'stex_tp': stex_tp,
    }
    return _post(token, 'ka10052', body)


def print_broker_instant_volume(token: str):
    """대화형 거래원순간거래량 조회 (ka10052)"""
    print('\n[거래원순간거래량요청 (ka10052)]')
    print('─' * 60)
    print('  ※ 회원사코드는 ka10102 API로 조회 가능합니다.')
    print('     주요 코드: 888(외국계합계), 001(키움증권)')

    mmcm_cd = input('  회원사코드 입력 (예: 888): ').strip()
    if not mmcm_cd:
        print('  회원사코드는 필수 입력입니다.')
        return

    print('  시장구분: ', end='')
    for k, v in MRKT_TP_MAP_4.items():
        print(f'{k}:{v}', end='  ')
    mrkt_tp = input('\n  선택 (기본값 0·전체): ').strip() or '0'

    stk_cd = ''
    if mrkt_tp == '3':
        stk_cd = input('  종목코드 입력 (예: 005930): ').strip()

    print('  수량구분: ', end='')
    for k, v in QTY_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    qty_tp = input('\n  선택 (기본값 0·전체): ').strip() or '0'

    print(f'\n  → 조회 중...')
    result = get_broker_instant_volume(token, mmcm_cd=mmcm_cd, mrkt_tp=mrkt_tp,
                                        stk_cd=stk_cd, qty_tp=qty_tp)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('trde_ori_mont_trde_qty', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("시간", 8)}  {_rjust("종목코드", 12)}  {_ljust("종목명", 24)}  {_ljust("거래원명", 14)}  '
          f'{_rjust("구분", 8)}  {_rjust("순간거래량", 12)}  {_rjust("누적순매수", 12)}  {_rjust("현재가", 10)}  {_rjust("등락율", 8)}')
    print(f'  {"─"*8}  {"─"*12}  {"─"*24}  {"─"*14}  '
          f'{"─"*8}  {"─"*12}  {"─"*12}  {"─"*10}  {"─"*8}')
    for item in items:
        print(f'  {_rjust(item.get("tm", ""), 8)}  {_rjust(item.get("stk_cd", ""), 12)}  '
              f'{_ljust(item.get("stk_nm", ""), 24)}  {_ljust(item.get("trde_ori_nm", ""), 14)}  '
              f'{_rjust(item.get("tp", ""), 8)}  {_rjust(item.get("mont_trde_qty", ""), 12)}  '
              f'{_rjust(item.get("acc_netprps", ""), 12)}  {_rjust(item.get("cur_prc", ""), 10)}  '
              f'{_rjust(item.get("flu_rt", ""), 8)}')

    _ask_raw(result)


# ═══════════════════════════════════════════════════════
# ka10055 – 당일전일체결량요청
# ═══════════════════════════════════════════════════════
TDY_PRED_MAP = {
    '1': '당일',
    '2': '전일',
}


def get_today_prev_contracts(token: str, stk_cd: str,
                              tdy_pred: str = '1') -> dict:
    """당일전일체결량요청 (ka10055): 종목별 시간대별 체결량 조회"""
    body = {
        'stk_cd': stk_cd,
        'tdy_pred': tdy_pred,
    }
    return _post(token, 'ka10055', body)


def print_today_prev_contracts(token: str):
    """대화형 당일전일체결량 조회 (ka10055)"""
    print('\n[당일전일체결량요청 (ka10055)]')
    print('─' * 60)

    stk_cd = input('  종목코드 입력 (예: 005930): ').strip()
    if not stk_cd:
        print('  종목코드는 필수 입력입니다.')
        return

    print('  당일전일: ', end='')
    for k, v in TDY_PRED_MAP.items():
        print(f'{k}:{v}', end='  ')
    tdy_pred = input('\n  선택 (기본값 1·당일): ').strip() or '1'

    print(f'\n  → {stk_cd} / {TDY_PRED_MAP.get(tdy_pred, tdy_pred)} 조회 중...')
    result = get_today_prev_contracts(token, stk_cd=stk_cd, tdy_pred=tdy_pred)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('tdy_pred_cntr_qty', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("체결시간", 8)}  {_rjust("체결가", 10)}  {_rjust("전일대비", 16)}  {_rjust("등락율", 8)}  '
          f'{_rjust("체결량", 12)}  {_rjust("누적거래량", 14)}  {_rjust("누적거래대금(백만)", 18)}')
    print(f'  {"─"*8}  {"─"*10}  {"─"*16}  {"─"*8}  '
          f'{"─"*12}  {"─"*14}  {"─"*18}')
    for item in items:
        sig = PRE_SIG_MAP.get(item.get('pred_pre_sig', ''), '')
        print(f'  {_rjust(item.get("cntr_tm", ""), 8)}  {_rjust(item.get("cntr_pric", ""), 10)}  '
              f'{_rjust(item.get("pred_pre", ""), 10)}({sig})  {_rjust(item.get("flu_rt", ""), 8)}  '
              f'{_rjust(item.get("cntr_qty", ""), 12)}  {_rjust(item.get("acc_trde_qty", ""), 14)}  '
              f'{_rjust(item.get("acc_trde_prica", ""), 18)}')

    _ask_raw(result)


# ─────────────────────────────────────────────
def _ask_raw(result: dict):
    show_raw = input('\n  원시 JSON 출력? (y/N): ').strip().lower()
    if show_raw == 'y':
        print(json.dumps(result, indent=4, ensure_ascii=False))
