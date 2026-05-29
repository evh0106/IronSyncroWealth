"""
거래량 종목정보 관련 API (국내주식 > 종목정보)
URL: /api/dostk/stkinfo

포함 API:
  - 거래량갱신요청        (ka10024)
  - 거래원순간거래량요청  (ka10052)
  - 당일전일체결량요청    (ka10055)

입력 파라미터 선택지와 한글 라벨은 specs_request / specs_response 에서 참조합니다.
"""

import requests
from datetime import datetime
from oauth2 import HOST
from logger import log_http_request, log_http_response
from ._fmt import _ljust, _rjust, _wcslen
from .specs_request import STKINFO_API_SPECS
from .specs_response import STKINFO_RESPONSE_SPECS
import db

# ─────────────────────────────────────────────
# 전일대비기호 표시용 (응답 스펙에는 없는 표현)
# ─────────────────────────────────────────────
_PRE_SIG_MAP = {
    '1': '상한',
    '2': '상승',
    '3': '보합',
    '4': '하한',
    '5': '하락',
}

_STKINFO_URL = HOST + '/api/dostk/stkinfo'


# ─────────────────────────────────────────────
# specs 조회 헬퍼
# ─────────────────────────────────────────────

def _req_spec(api_id: str) -> dict:
    """api_id 에 해당하는 요청 스펙 반환"""
    for s in STKINFO_API_SPECS:
        if s['api_id'] == api_id:
            return s
    return {}


def _field(api_id: str, element: str) -> dict:
    """요청 스펙에서 특정 element 의 필드 정보 반환"""
    for f in _req_spec(api_id).get('fields', []):
        if f['element'] == element:
            return f
    return {}


def _parse_choices(description: str) -> dict:
    """'k1:v1, k2:v2' 형식 description 을 {key: label} 딕셔너리로 파싱"""
    choices = {}
    for part in description.split(','):
        part = part.strip()
        if ':' in part:
            k, v = part.split(':', 1)
            k = k.strip()
            if k:
                choices[k] = v.strip()
    return choices


def _prompt_choice(api_id: str, element: str, default: str) -> str:
    """스펙의 description 을 파싱해 선택지를 출력하고 입력 받음"""
    f = _field(api_id, element)
    label = f.get('label', element)
    choices = _parse_choices(f.get('description', ''))

    if choices:
        print(f'  {label}: ', end='')
        for k, v in choices.items():
            print(f'{k}:{v}', end='  ')
        default_label = choices.get(default, default)
        val = input(f'\n  선택 (기본값 {default}·{default_label}): ').strip() or default
    else:
        val = input(f'  {label} 입력 (기본값 {default}): ').strip() or default
    return val


def _resp_cols(api_id: str, skip: set | None = None) -> tuple[str, list[dict]]:
    """
    응답 스펙에서 리스트 키와 컬럼 목록({key, label}) 반환.
    skip 에 포함된 element 는 제외합니다.
    """
    skip = skip or set()
    specs = STKINFO_RESPONSE_SPECS.get(api_id, [])
    list_key = ''
    cols = []
    for s in specs:
        if s['type'] == 'LIST':
            list_key = s['element']
        elif s['element'].startswith('- '):
            key = s['element'][2:]
            if key not in skip:
                cols.append({'key': key, 'label': s['label']})
    return list_key, cols


def _print_table(items: list[dict], cols: list[dict],
                 widths: dict[str, int], left_cols: set | None = None):
    """
    cols 순서로 items 를 표 형식으로 출력.
    widths: {key: int}  left_cols: 왼쪽 정렬할 key 집합
    """
    left_cols = left_cols or set()

    def _fmt(key, val, w):
        return _ljust(val, w) if key in left_cols else _rjust(val, w)

    # 헤더
    header = '  ' + '  '.join(_fmt(c['key'], c['label'], widths[c['key']]) for c in cols)
    sep    = '  ' + '  '.join('─' * widths[c['key']] for c in cols)
    print(header)
    print(sep)

    for item in items:
        row = '  ' + '  '.join(_fmt(c['key'], str(item.get(c['key'], '')), widths[c['key']]) for c in cols)
        print(row)


# ─────────────────────────────────────────────
# 공통 내부 함수
# ─────────────────────────────────────────────

def _post(token: str, api_id: str, body: dict) -> dict:
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': 'N',
        'next-key': '',
        'api-id': api_id,
    }
    session = requests.Session()
    req = requests.Request('POST', _STKINFO_URL, headers=headers, json=body)
    preq = session.prepare_request(req)

    path, req_id = log_http_request(
        api_id=api_id,
        url=_STKINFO_URL,
        request_headers=preq.headers,
        request_body=preq.body,
    )
    print(f'  → 요청 로그 저장: {path}')

    resp = session.send(preq)
    path = log_http_response(
        req_id=req_id,
        response_status=resp.status_code,
        response_headers=resp.headers,
        response_body=resp.text,
    )
    print(f'  → 응답 로그 저장: {path}')
    resp.raise_for_status()
    return resp.json()



# ═══════════════════════════════════════════════════════
# ka10024 – 거래량갱신요청
# ═══════════════════════════════════════════════════════

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
    API_ID = 'ka10024'
    spec = _req_spec(API_ID)
    print(f'\n[{spec.get("name", API_ID)} ({API_ID})]')
    print('─' * 60)

    mrkt_tp    = _prompt_choice(API_ID, 'mrkt_tp',    '000')
    cycle_tp   = _prompt_choice(API_ID, 'cycle_tp',   '5')
    trde_qty_tp = _prompt_choice(API_ID, 'trde_qty_tp', '5')

    print(f'\n  → 조회 중...')
    result = get_volume_update(token, mrkt_tp=mrkt_tp, cycle_tp=cycle_tp,
                               trde_qty_tp=trde_qty_tp)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, all_cols = _resp_cols(API_ID, skip={'pred_pre_sig', 'pred_pre'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    # 컬럼별 표시 너비 지정
    widths = {
        'stk_cd':        12,
        'stk_nm':        24,
        'cur_prc':       10,
        'flu_rt':         8,
        'prev_trde_qty': 14,
        'now_trde_qty':  14,
        'sel_bid':       10,
        'buy_bid':       10,
    }
    # 순위 컬럼을 앞에 추가
    rank_col = {'key': '_rank', 'label': '순위'}
    widths['_rank'] = 4
    display_cols = [rank_col] + all_cols

    print()
    _print_table(
        [{**item, '_rank': i} for i, item in enumerate(items, 1)],
        display_cols,
        widths,
        left_cols={'stk_nm'},
    )

    try:
        count = save_ka10024(items)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# ka10052 – 거래원순간거래량요청
# ═══════════════════════════════════════════════════════

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
    API_ID = 'ka10052'
    spec = _req_spec(API_ID)
    print(f'\n[{spec.get("name", API_ID)} ({API_ID})]')
    print('─' * 60)

    mmcm_field = _field(API_ID, 'mmcm_cd')
    print(f'  ※ {mmcm_field.get("description", "회원사 코드는 ka10102 조회")}')
    print('     주요 코드: 888(외국계합계), 001(키움증권)')
    mmcm_cd = input(f'  {mmcm_field.get("label", "회원사코드")} 입력 (예: 888): ').strip()
    if not mmcm_cd:
        print(f'  {mmcm_field.get("label", "회원사코드")}는 필수 입력입니다.')
        return

    mrkt_tp = _prompt_choice(API_ID, 'mrkt_tp', '0')

    stk_cd = ''
    if mrkt_tp == '3':
        stk_cd_field = _field(API_ID, 'stk_cd')
        stk_cd = input(f'  {stk_cd_field.get("label", "종목코드")} 입력 (예: 005930): ').strip()

    qty_tp  = _prompt_choice(API_ID, 'qty_tp',  '0')
    pric_tp = _prompt_choice(API_ID, 'pric_tp', '0')

    print(f'\n  → 조회 중...')
    result = get_broker_instant_volume(token, mmcm_cd=mmcm_cd, mrkt_tp=mrkt_tp,
                                        stk_cd=stk_cd, qty_tp=qty_tp, pric_tp=pric_tp)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, all_cols = _resp_cols(API_ID, skip={'pred_pre_sig', 'pred_pre'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    widths = {
        'tm':            8,
        'stk_cd':        12,
        'stk_nm':        24,
        'trde_ori_nm':   14,
        'tp':             8,
        'mont_trde_qty': 14,
        'acc_netprps':   14,
        'cur_prc':       10,
        'flu_rt':         8,
    }

    print()
    _print_table(items, all_cols, widths, left_cols={'stk_nm', 'trde_ori_nm'})

    try:
        count = save_ka10052(items)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# ka10055 – 당일전일체결량요청
# ═══════════════════════════════════════════════════════

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
    API_ID = 'ka10055'
    spec = _req_spec(API_ID)
    print(f'\n[{spec.get("name", API_ID)} ({API_ID})]')
    print('─' * 60)

    stk_cd_field = _field(API_ID, 'stk_cd')
    stk_cd = input(f'  {stk_cd_field.get("label", "종목코드")} 입력 (예: 005930): ').strip()
    if not stk_cd:
        print(f'  {stk_cd_field.get("label", "종목코드")}는 필수 입력입니다.')
        return

    tdy_pred = _prompt_choice(API_ID, 'tdy_pred', '1')
    tdy_pred_label = _parse_choices(
        _field(API_ID, 'tdy_pred').get('description', '')
    ).get(tdy_pred, tdy_pred)

    print(f'\n  → {stk_cd} / {tdy_pred_label} 조회 중...')
    result = get_today_prev_contracts(token, stk_cd=stk_cd, tdy_pred=tdy_pred)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, all_cols = _resp_cols(API_ID, skip={'pred_pre_sig'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    # pred_pre 는 전일대비기호(sig)와 합쳐서 표시하기 위해 컬럼에서 제거 후 별도 처리
    display_cols = [c for c in all_cols if c['key'] != 'pred_pre']
    # pred_pre 라벨은 스펙에서 가져와 헤더에 사용
    pred_pre_label = next(
        (c['label'] for c in all_cols if c['key'] == 'pred_pre'), '전일대비'
    )
    # pred_pre 컬럼을 cntr_pric 다음에 삽입 (기호 포함 포맷)
    insert_idx = next(
        (i + 1 for i, c in enumerate(display_cols) if c['key'] == 'cntr_pric'), 1
    )
    display_cols.insert(insert_idx, {'key': '_pred_pre_fmt', 'label': pred_pre_label})

    widths = {
        'cntr_tm':         8,
        'cntr_pric':      10,
        '_pred_pre_fmt':  14,
        'flu_rt':          8,
        'cntr_qty':       12,
        'acc_trde_qty':   14,
        'acc_trde_prica': 18,
    }

    # 전일대비기호를 결합한 포맷 필드 추가
    def _fmt_pre(item):
        sig = _PRE_SIG_MAP.get(item.get('pred_pre_sig', ''), '')
        pre = item.get('pred_pre', '')
        return f'{pre}({sig})' if sig else pre

    enriched = [{**item, '_pred_pre_fmt': _fmt_pre(item)} for item in items]

    print()
    _print_table(enriched, display_cols, widths)

    try:
        count = save_ka10055(items, stk_cd)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# DB 저장 함수
# ═══════════════════════════════════════════════════════

_INSERT_KA10024 = """
    INSERT INTO ka10024_trde_qty_updt
        (header_id, stk_cd, stk_nm, cur_prc, pred_pre_sig, pred_pre, flu_rt, prev_trde_qty, now_trde_qty, sel_bid, buy_bid)
    VALUES
        (%(header_id)s, %(stk_cd)s, %(stk_nm)s, %(cur_prc)s, %(pred_pre_sig)s, %(pred_pre)s, %(flu_rt)s, %(prev_trde_qty)s, %(now_trde_qty)s, %(sel_bid)s, %(buy_bid)s)
"""

_INSERT_KA10052 = """
    INSERT INTO ka10052_trde_ori_mont_trde_qty
        (header_id, stk_cd, tm, stk_nm, trde_ori_nm, tp, mont_trde_qty, acc_netprps, cur_prc, pred_pre_sig, pred_pre, flu_rt)
    VALUES
        (%(header_id)s, %(stk_cd)s, %(tm)s, %(stk_nm)s, %(trde_ori_nm)s, %(tp)s, %(mont_trde_qty)s, %(acc_netprps)s, %(cur_prc)s, %(pred_pre_sig)s, %(pred_pre)s, %(flu_rt)s)
"""

_INSERT_KA10055 = """
    INSERT INTO ka10055_tdy_pred_cntr_qty
        (header_id, stk_cd, cntr_tm, cntr_pric, pred_pre_sig, pred_pre, flu_rt, cntr_qty, acc_trde_qty, acc_trde_prica)
    VALUES
        (%(header_id)s, %(stk_cd)s, %(cntr_tm)s, %(cntr_pric)s, %(pred_pre_sig)s, %(pred_pre)s, %(flu_rt)s, %(cntr_qty)s, %(acc_trde_qty)s, %(acc_trde_prica)s)
"""


def save_ka10024(items: list) -> int:
    if not items:
        return 0
    header_id = int(datetime.now().timestamp() * 1000)
    rows = []
    for item in items:
        rows.append({
            'header_id': header_id,
            'stk_cd': item.get('stk_cd', ''),
            'stk_nm': item.get('stk_nm', ''),
            'cur_prc': item.get('cur_prc', ''),
            'pred_pre_sig': item.get('pred_pre_sig', ''),
            'pred_pre': item.get('pred_pre', ''),
            'flu_rt': item.get('flu_rt', ''),
            'prev_trde_qty': item.get('prev_trde_qty', ''),
            'now_trde_qty': item.get('now_trde_qty', ''),
            'sel_bid': item.get('sel_bid', ''),
            'buy_bid': item.get('buy_bid', ''),
        })
    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10024, rows)
        conn.commit()
        print(f'  [DB 저장] ka10024_trde_qty_updt: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()


def save_ka10052(items: list) -> int:
    if not items:
        return 0
    header_id = int(datetime.now().timestamp() * 1000)
    rows = []
    for item in items:
        rows.append({
            'header_id': header_id,
            'stk_cd': item.get('stk_cd', ''),
            'tm': item.get('tm', ''),
            'stk_nm': item.get('stk_nm', ''),
            'trde_ori_nm': item.get('trde_ori_nm', ''),
            'tp': item.get('tp', ''),
            'mont_trde_qty': item.get('mont_trde_qty', ''),
            'acc_netprps': item.get('acc_netprps', ''),
            'cur_prc': item.get('cur_prc', ''),
            'pred_pre_sig': item.get('pred_pre_sig', ''),
            'pred_pre': item.get('pred_pre', ''),
            'flu_rt': item.get('flu_rt', ''),
        })
    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10052, rows)
        conn.commit()
        print(f'  [DB 저장] ka10052_trde_ori_mont_trde_qty: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()


def save_ka10055(items: list, stk_cd: str) -> int:
    if not items:
        return 0
    header_id = int(datetime.now().timestamp() * 1000)
    rows = []
    for item in items:
        rows.append({
            'header_id': header_id,
            'stk_cd': stk_cd,
            'cntr_tm': item.get('cntr_tm', ''),
            'cntr_pric': item.get('cntr_pric', ''),
            'pred_pre_sig': item.get('pred_pre_sig', ''),
            'pred_pre': item.get('pred_pre', ''),
            'flu_rt': item.get('flu_rt', ''),
            'cntr_qty': item.get('cntr_qty', ''),
            'acc_trde_qty': item.get('acc_trde_qty', ''),
            'acc_trde_prica': item.get('acc_trde_prica', ''),
        })
    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10055, rows)
        conn.commit()
        print(f'  [DB 저장] ka10055_tdy_pred_cntr_qty: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()

    
