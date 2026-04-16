"""
거래량 순위 관련 API (국내주식 > 순위정보)
URL: /api/dostk/rkinfo

포함 API:
  - 거래량급증요청  (ka10023)
  - 당일거래량상위  (ka10030)
  - 전일거래량상위  (ka10031)
  - 거래대금상위    (ka10032)
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

MRKT_TP_MAP = {
    '000': '전체',
    '001': '코스피',
    '101': '코스닥',
}


def _get_market_label(item: dict, selected_mrkt_tp: str = '000') -> str:
    market_code = item.get('mrkt_tp', '')
    if market_code in MRKT_TP_MAP and market_code != '000':
        return MRKT_TP_MAP[market_code]
    if selected_mrkt_tp in MRKT_TP_MAP and selected_mrkt_tp != '000':
        return MRKT_TP_MAP[selected_mrkt_tp]
    return ''


_RKINFO_URL = HOST + '/api/dostk/rkinfo'


def _post(token: str, api_id: str, body: dict) -> dict:
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': 'N',
        'next-key': '',
        'api-id': api_id,
    }
    resp = requests.post(_RKINFO_URL, headers=headers, json=body)
    resp.raise_for_status()
    return resp.json()


# ═══════════════════════════════════════════════════════
# ka10023 – 거래량급증요청
# ═══════════════════════════════════════════════════════
SORT_TP_MAP_10023 = {
    '1': '급증량',
    '2': '급증률',
    '3': '급감량',
    '4': '급감률',
}

TM_TP_MAP = {
    '1': '분',
    '2': '전일',
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


def get_volume_surge(token: str, mrkt_tp: str = '000', sort_tp: str = '1',
                     tm_tp: str = '2', trde_qty_tp: str = '5',
                     tm: str = '', stk_cnd: str = '0',
                     pric_tp: str = '0', stex_tp: str = '3') -> dict:
    """거래량급증요청 (ka10023)"""
    body = {
        'mrkt_tp': mrkt_tp,
        'sort_tp': sort_tp,
        'tm_tp': tm_tp,
        'trde_qty_tp': trde_qty_tp,
        'tm': tm,
        'stk_cnd': stk_cnd,
        'pric_tp': pric_tp,
        'stex_tp': stex_tp,
    }
    return _post(token, 'ka10023', body)


def print_volume_surge(token: str):
    """대화형 거래량급증 조회 (ka10023)"""
    print('\n[거래량급증요청 (ka10023)]')
    print('─' * 60)

    print('  시장구분: ', end='')
    for k, v in MRKT_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    mrkt_tp = input('\n  선택 (기본값 000·전체): ').strip() or '000'

    print('  정렬구분: ', end='')
    for k, v in SORT_TP_MAP_10023.items():
        print(f'{k}:{v}', end='  ')
    sort_tp = input('\n  선택 (기본값 1·급증량): ').strip() or '1'

    print('  시간구분: ', end='')
    for k, v in TM_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    tm_tp = input('\n  선택 (기본값 2·전일): ').strip() or '2'

    tm = ''
    if tm_tp == '1':
        tm = input('  분 입력 (예: 30): ').strip()

    print('  거래량구분: ', end='')
    for k, v in TRDE_QTY_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    trde_qty_tp = input('\n  선택 (기본값 5): ').strip() or '5'

    print(f'\n  → 조회 중...')
    result = get_volume_surge(token, mrkt_tp=mrkt_tp, sort_tp=sort_tp,
                              tm_tp=tm_tp, trde_qty_tp=trde_qty_tp, tm=tm)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('trde_qty_sdnin', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("순위", 4)}  {_rjust("종목코드", 12)}  {_ljust("시장", 6)}  {_ljust("종목명", 24)}  {_rjust("현재가", 10)}  '
          f'{_rjust("등락률", 8)}  {_rjust("이전거래량", 12)}  {_rjust("현재거래량", 12)}  {_rjust("급증량", 12)}  {_rjust("급증률", 8)}')
    print(f'  {"─"*4}  {"─"*12}  {"─"*6}  {"─"*24}  {"─"*10}  '
          f'{"─"*8}  {"─"*12}  {"─"*12}  {"─"*12}  {"─"*8}')
    for i, item in enumerate(items, 1):
        market = _get_market_label(item, mrkt_tp)
        print(f'  {_rjust(i, 4)}  {_rjust(item.get("stk_cd", ""), 12)}  {_ljust(market, 6)}  {_ljust(item.get("stk_nm", ""), 24)}  '
              f'{_rjust(item.get("cur_prc", ""), 10)}  {_rjust(item.get("flu_rt", ""), 8)}  '
              f'{_rjust(item.get("prev_trde_qty", ""), 12)}  {_rjust(item.get("now_trde_qty", ""), 12)}  '
              f'{_rjust(item.get("sdnin_qty", ""), 12)}  {_rjust(item.get("sdnin_rt", ""), 8)}')

    _ask_raw(result)


# ═══════════════════════════════════════════════════════
# ka10030 – 당일거래량상위요청
# ═══════════════════════════════════════════════════════
SORT_TP_MAP_10030 = {
    '1': '거래량',
    '2': '거래회전율',
    '3': '거래대금',
}

MRKT_OPEN_TP_MAP = {
    '0': '전체조회',
    '1': '장중',
    '2': '장전시간외',
    '3': '장후시간외',
}


def get_today_volume_rank(token: str, mrkt_tp: str = '000', sort_tp: str = '1',
                          mang_stk_incls: str = '0', crd_tp: str = '0',
                          trde_qty_tp: str = '0', pric_tp: str = '0',
                          trde_prica_tp: str = '0', mrkt_open_tp: str = '0',
                          stex_tp: str = '3') -> dict:
    """당일거래량상위요청 (ka10030)"""
    body = {
        'mrkt_tp': mrkt_tp,
        'sort_tp': sort_tp,
        'mang_stk_incls': mang_stk_incls,
        'crd_tp': crd_tp,
        'trde_qty_tp': trde_qty_tp,
        'pric_tp': pric_tp,
        'trde_prica_tp': trde_prica_tp,
        'mrkt_open_tp': mrkt_open_tp,
        'stex_tp': stex_tp,
    }
    return _post(token, 'ka10030', body)


def print_today_volume_rank(token: str):
    """대화형 당일거래량상위 조회 (ka10030)"""
    print('\n[당일거래량상위요청 (ka10030)]')
    print('─' * 60)

    print('  시장구분: ', end='')
    for k, v in MRKT_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    mrkt_tp = input('\n  선택 (기본값 000·전체): ').strip() or '000'

    print('  정렬구분: ', end='')
    for k, v in SORT_TP_MAP_10030.items():
        print(f'{k}:{v}', end='  ')
    sort_tp = input('\n  선택 (기본값 1·거래량): ').strip() or '1'

    print('  장운영구분: ', end='')
    for k, v in MRKT_OPEN_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    mrkt_open_tp = input('\n  선택 (기본값 0·전체): ').strip() or '0'

    print(f'\n  → 조회 중...')
    result = get_today_volume_rank(token, mrkt_tp=mrkt_tp, sort_tp=sort_tp,
                                   mrkt_open_tp=mrkt_open_tp)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('tdy_trde_qty_upper', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("순위", 4)}  {_rjust("종목코드", 12)}  {_ljust("시장", 6)}  {_ljust("종목명", 24)}  {_rjust("현재가", 10)}  '
          f'{_rjust("등락률", 8)}  {_rjust("거래량", 14)}  {_rjust("전일비", 8)}  {_rjust("거래금액(백만)", 14)}')
    print(f'  {"─"*4}  {"─"*12}  {"─"*6}  {"─"*24}  {"─"*10}  '
          f'{"─"*8}  {"─"*14}  {"─"*8}  {"─"*14}')
    for i, item in enumerate(items, 1):
        market = _get_market_label(item, mrkt_tp)
        print(f'  {_rjust(i, 4)}  {_rjust(item.get("stk_cd", ""), 12)}  {_ljust(market, 6)}  {_ljust(item.get("stk_nm", ""), 24)}  '
              f'{_rjust(item.get("cur_prc", ""), 10)}  {_rjust(item.get("flu_rt", ""), 8)}  '
              f'{_rjust(item.get("trde_qty", ""), 14)}  {_rjust(item.get("pred_rt", ""), 8)}  '
              f'{_rjust(item.get("trde_amt", ""), 14)}')

    _ask_raw(result)


# ═══════════════════════════════════════════════════════
# ka10031 – 전일거래량상위요청
# ═══════════════════════════════════════════════════════
QRY_TP_MAP = {
    '1': '전일거래량 상위100종목',
    '2': '전일거래대금 상위100종목',
}


def get_prev_volume_rank(token: str, mrkt_tp: str = '000', qry_tp: str = '1',
                         rank_strt: str = '0', rank_end: str = '20',
                         stex_tp: str = '3') -> dict:
    """전일거래량상위요청 (ka10031)"""
    body = {
        'mrkt_tp': mrkt_tp,
        'qry_tp': qry_tp,
        'rank_strt': rank_strt,
        'rank_end': rank_end,
        'stex_tp': stex_tp,
    }
    return _post(token, 'ka10031', body)


def print_prev_volume_rank(token: str):
    """대화형 전일거래량상위 조회 (ka10031)"""
    print('\n[전일거래량상위요청 (ka10031)]')
    print('─' * 60)

    print('  시장구분: ', end='')
    for k, v in MRKT_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    mrkt_tp = input('\n  선택 (기본값 000·전체): ').strip() or '000'

    print('  조회구분: ', end='')
    for k, v in QRY_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    qry_tp = input('\n  선택 (기본값 1·거래량): ').strip() or '1'

    rank_strt = input('  순위 시작 (0~100, 기본값 0): ').strip() or '0'
    rank_end  = input('  순위 끝   (0~100, 기본값 20): ').strip() or '20'

    print(f'\n  → 조회 중...')
    result = get_prev_volume_rank(token, mrkt_tp=mrkt_tp, qry_tp=qry_tp,
                                  rank_strt=rank_strt, rank_end=rank_end)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('pred_trde_qty_upper', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("순위", 4)}  {_rjust("종목코드", 12)}  {_ljust("시장", 6)}  {_ljust("종목명", 24)}  {_rjust("현재가", 10)}  '
          f'{_rjust("전일대비", 16)}  {_rjust("거래량", 14)}')
    print(f'  {"─"*4}  {"─"*12}  {"─"*6}  {"─"*24}  {"─"*10}  '
          f'{"─"*16}  {"─"*14}')
    for i, item in enumerate(items, 1):
        sig = PRE_SIG_MAP.get(item.get('pred_pre_sig', ''), '')
        market = _get_market_label(item, mrkt_tp)
        print(f'  {_rjust(i, 4)}  {_rjust(item.get("stk_cd", ""), 12)}  {_ljust(market, 6)}  {_ljust(item.get("stk_nm", ""), 24)}  '
              f'{_rjust(item.get("cur_prc", ""), 10)}  {_rjust(item.get("pred_pre", ""), 10)}({sig})  '
              f'{_rjust(item.get("trde_qty", ""), 14)}')

    _ask_raw(result)


# ═══════════════════════════════════════════════════════
# ka10032 – 거래대금상위요청
# ═══════════════════════════════════════════════════════
MANG_STK_MAP = {
    '0': '관리종목 미포함',
    '1': '관리종목 포함',
}


def get_trade_amount_rank(token: str, mrkt_tp: str = '001',
                          mang_stk_incls: str = '1',
                          stex_tp: str = '3') -> dict:
    """거래대금상위요청 (ka10032)"""
    body = {
        'mrkt_tp': mrkt_tp,
        'mang_stk_incls': mang_stk_incls,
        'stex_tp': stex_tp,
    }
    return _post(token, 'ka10032', body)


def print_trade_amount_rank(token: str):
    """대화형 거래대금상위 조회 (ka10032)"""
    print('\n[거래대금상위요청 (ka10032)]')
    print('─' * 60)

    print('  시장구분: ', end='')
    for k, v in MRKT_TP_MAP.items():
        print(f'{k}:{v}', end='  ')
    mrkt_tp = input('\n  선택 (기본값 001·코스피): ').strip() or '001'

    print('  관리종목포함: ', end='')
    for k, v in MANG_STK_MAP.items():
        print(f'{k}:{v}', end='  ')
    mang_stk_incls = input('\n  선택 (기본값 1·포함): ').strip() or '1'

    print(f'\n  → 조회 중...')
    result = get_trade_amount_rank(token, mrkt_tp=mrkt_tp,
                                   mang_stk_incls=mang_stk_incls)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    items = result.get('trde_prica_upper', [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    print()
    print(f'  {_rjust("현재순위", 8)}  {_rjust("전일순위", 8)}  {_rjust("종목코드", 12)}  {_ljust("시장", 6)}  {_ljust("종목명", 24)}  '
          f'{_rjust("현재가", 10)}  {_rjust("등락률", 8)}  {_rjust("현재거래량", 12)}  {_rjust("거래대금(백만)", 14)}')
    print(f'  {"─"*8}  {"─"*8}  {"─"*12}  {"─"*6}  {"─"*24}  '
          f'{"─"*10}  {"─"*8}  {"─"*12}  {"─"*14}')
    for item in items:
        market = _get_market_label(item, mrkt_tp)
        print(f'  {_rjust(item.get("now_rank", ""), 8)}  {_rjust(item.get("pred_rank", ""), 8)}  '
              f'{_rjust(item.get("stk_cd", ""), 12)}  {_ljust(market, 6)}  {_ljust(item.get("stk_nm", ""), 24)}  '
              f'{_rjust(item.get("cur_prc", ""), 10)}  {_rjust(item.get("flu_rt", ""), 8)}  '
              f'{_rjust(item.get("now_trde_qty", ""), 12)}  {_rjust(item.get("trde_prica", ""), 14)}')

    _ask_raw(result)


# ─────────────────────────────────────────────
def _ask_raw(result: dict):
    show_raw = input('\n  원시 JSON 출력? (y/N): ').strip().lower()
    if show_raw == 'y':
        print(json.dumps(result, indent=4, ensure_ascii=False))
