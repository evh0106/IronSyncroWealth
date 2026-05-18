"""
거래량 순위 관련 API (국내주식 > 순위정보)
URL: /api/dostk/rkinfo

포함 API:
  - 거래량급증요청  (ka10023)
  - 당일거래량상위  (ka10030)
  - 전일거래량상위  (ka10031)
  - 거래대금상위    (ka10032)

입력 파라미터 선택지와 한글 라벨은 specs_request_rank / specs_response_rank 에서 참조합니다.
"""

import requests
from datetime import datetime
from oauth2 import HOST
from logger import log_http_request, log_http_response
from ._fmt import _ljust, _rjust, _wcslen
from .specs_request_rank import RKINFO_API_SPECS
from .specs_response_rank import RKINFO_RESPONSE_SPECS
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

_RKINFO_URL = HOST + '/api/dostk/rkinfo'


# ─────────────────────────────────────────────
# specs 조회 헬퍼
# ─────────────────────────────────────────────

def _req_spec(api_id: str) -> dict:
    """api_id 에 해당하는 요청 스펙 반환"""
    for s in RKINFO_API_SPECS:
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
            choices[k.strip()] = v.strip()
    return choices


def _prompt_choice(api_id: str, element: str, default: str) -> str:
    """스펙에 정의된 선택지를 출력하고 사용자 입력을 받아 반환"""
    f = _field(api_id, element)
    label = f.get('label', element)
    choices = _parse_choices(f.get('description', ''))
    default_label = choices.get(default, default)
    print(f'  {label}: ', end='')
    for k, v in choices.items():
        print(f'{k}:{v}', end='  ')
    val = input(f'\n  선택 (기본값 {default}·{default_label}): ').strip() or default
    return val


def _resp_cols(api_id: str, skip: set = None) -> tuple:
    """응답 스펙에서 (list_key, [{key, label}, ...]) 반환.
    skip 에 포함된 element(접두 '- ' 제거 후)는 제외."""
    if skip is None:
        skip = set()
    rows = RKINFO_RESPONSE_SPECS.get(api_id, [])
    list_key = ''
    cols = []
    for row in rows:
        elem = row['element']
        if row['type'] == 'LIST':
            list_key = elem
        elif elem.startswith('- '):
            key = elem[2:]
            if key not in skip:
                cols.append({'key': key, 'label': row['label']})
    return list_key, cols


def _print_table(items: list, cols: list, widths: list, left_cols: set,
                 row_num: bool = False, row_fn=None):
    """specs 컬럼 목록으로 테이블 헤더·구분선·데이터를 출력.

    Args:
        items: 응답 리스트
        cols: [{'key': str, 'label': str}, ...]
        widths: 각 컬럼의 표시 너비 (cols 와 동일 순서)
        left_cols: 왼쪽 정렬할 key 집합
        row_num: True 이면 맨 앞에 순번 열 추가
        row_fn: item → dict 변환 함수 (가상 컬럼 생성 등)
    """
    def _cell(key, val):
        if key in left_cols:
            return _ljust(str(val), widths[col_idx[key]])
        return _rjust(str(val), widths[col_idx[key]])

    col_idx = {c['key']: i for i, c in enumerate(cols)}

    # 헤더
    hdr_parts = []
    sep_parts = []
    if row_num:
        hdr_parts.append(_rjust('순위', 4))
        sep_parts.append('─' * 4)
    for c, w in zip(cols, widths):
        if c['key'] in left_cols:
            hdr_parts.append(_ljust(c['label'], w))
        else:
            hdr_parts.append(_rjust(c['label'], w))
        sep_parts.append('─' * w)

    print()
    print('  ' + '  '.join(hdr_parts))
    print('  ' + '  '.join(sep_parts))

    for idx, item in enumerate(items, 1):
        row = row_fn(item) if row_fn else item
        parts = []
        if row_num:
            parts.append(_rjust(idx, 4))
        for c, w in zip(cols, widths):
            val = row.get(c['key'], '')
            if c['key'] in left_cols:
                parts.append(_ljust(str(val), w))
            else:
                parts.append(_rjust(str(val), w))
        print('  ' + '  '.join(parts))


# ─────────────────────────────────────────────
# 공통 HTTP 요청
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
    req = requests.Request('POST', _RKINFO_URL, headers=headers, json=body)
    preq = session.prepare_request(req)

    path, req_id = log_http_request(
        api_id=api_id,
        url=_RKINFO_URL,
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


# ─────────────────────────────────────────────
# 시장구분 디코드 헬퍼
# ─────────────────────────────────────────────
_MRKT_TP_CHOICES = _parse_choices(_field('ka10023', 'mrkt_tp').get('description', ''))


def _market_label(item: dict, selected_mrkt_tp: str = '000') -> str:
    code = item.get('mrkt_tp', '')
    if code in _MRKT_TP_CHOICES and code != '000':
        return _MRKT_TP_CHOICES[code]
    if selected_mrkt_tp in _MRKT_TP_CHOICES and selected_mrkt_tp != '000':
        return _MRKT_TP_CHOICES[selected_mrkt_tp]
    return ''


# ═══════════════════════════════════════════════════════
# ka10023 – 거래량급증요청
# ═══════════════════════════════════════════════════════

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
    api_id = 'ka10023'
    spec = _req_spec(api_id)
    print(f'\n[{spec["name"]} ({api_id})]')
    print('─' * 60)

    mrkt_tp    = _prompt_choice(api_id, 'mrkt_tp',    '000')
    sort_tp    = _prompt_choice(api_id, 'sort_tp',    '1')
    tm_tp      = _prompt_choice(api_id, 'tm_tp',      '2')

    tm = ''
    if tm_tp == '1':
        tm = input('  분 입력 (예: 30): ').strip()

    trde_qty_tp = _prompt_choice(api_id, 'trde_qty_tp', '5')

    print('\n  → 조회 중...')
    result = get_volume_surge(token, mrkt_tp=mrkt_tp, sort_tp=sort_tp,
                              tm_tp=tm_tp, trde_qty_tp=trde_qty_tp, tm=tm)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, cols = _resp_cols(api_id, skip={'mrkt_tp'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    # 시장 가상 컬럼 삽입 (stk_cd 뒤)
    cols_disp = []
    for c in cols:
        cols_disp.append(c)
        if c['key'] == 'stk_cd':
            cols_disp.append({'key': '_market', 'label': '시장'})

    widths   = [12, 6, 24, 10, 8, 12, 12, 12, 8]
    left_set = {'stk_nm', '_market'}

    def _row(item):
        r = dict(item)
        r['_market'] = _market_label(item, mrkt_tp)
        return r

    _print_table(items, cols_disp, widths, left_set, row_num=True, row_fn=_row)

    try:
        count = save_ka10023(items)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# ka10030 – 당일거래량상위요청
# ═══════════════════════════════════════════════════════

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
    api_id = 'ka10030'
    spec = _req_spec(api_id)
    print(f'\n[{spec["name"]} ({api_id})]')
    print('─' * 60)

    mrkt_tp     = _prompt_choice(api_id, 'mrkt_tp',     '000')
    sort_tp     = _prompt_choice(api_id, 'sort_tp',     '1')
    mrkt_open_tp = _prompt_choice(api_id, 'mrkt_open_tp', '0')

    today = datetime.now().strftime('%Y%m%d')
    
    request_params = {
        'req_dt': today,
        'mrkt_tp': mrkt_tp,
        'sort_tp': sort_tp,
        'mang_stk_incls': '0',
        'crd_tp': '0',
        'trde_qty_tp': '0',
        'pric_tp': '0',
        'trde_prica_tp': '0',
        'mrkt_open_tp': mrkt_open_tp,
        'stex_tp': '3',
    }

    api_params = {k: v for k, v in request_params.items() if k != 'req_dt'}
    print('\n  → 조회 중...')
    result = get_today_volume_rank(token, **api_params)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, cols = _resp_cols(api_id, skip={'mrkt_tp'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    cols_disp = []
    for c in cols:
        cols_disp.append(c)
        if c['key'] == 'stk_cd':
            cols_disp.append({'key': '_market', 'label': '시장'})

    widths   = [12, 6, 24, 10, 8, 14, 8, 14]
    left_set = {'stk_nm', '_market'}

    def _row(item):
        r = dict(item)
        r['_market'] = _market_label(item, mrkt_tp)
        return r

    _print_table(items, cols_disp, widths, left_set, row_num=True, row_fn=_row)

    try:
        count = save_ka10030(items, request_params)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# ka10031 – 전일거래량상위요청
# ═══════════════════════════════════════════════════════

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
    api_id = 'ka10031'
    spec = _req_spec(api_id)
    print(f'\n[{spec["name"]} ({api_id})]')
    print('─' * 60)

    mrkt_tp  = _prompt_choice(api_id, 'mrkt_tp', '000')
    qry_tp   = _prompt_choice(api_id, 'qry_tp',  '1')
    rank_strt = input('  순위 시작 (0~100, 기본값 0): ').strip() or '0'
    rank_end  = input('  순위 끝   (0~100, 기본값 20): ').strip() or '20'

    print('\n  → 조회 중...')
    result = get_prev_volume_rank(token, mrkt_tp=mrkt_tp, qry_tp=qry_tp,
                                  rank_strt=rank_strt, rank_end=rank_end)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, cols = _resp_cols(api_id, skip={'mrkt_tp', 'pred_pre_sig'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    # pred_pre → 전일대비기호 결합 표시
    cols_disp = []
    for c in cols:
        cols_disp.append(c)
        if c['key'] == 'stk_cd':
            cols_disp.append({'key': '_market', 'label': '시장'})
        if c['key'] == 'pred_pre':
            cols_disp[-1] = {'key': '_pred_pre_fmt', 'label': '전일대비'}

    widths   = [12, 6, 24, 10, 16, 14]
    left_set = {'stk_nm', '_market'}

    def _row(item):
        r = dict(item)
        r['_market'] = _market_label(item, mrkt_tp)
        sig = _PRE_SIG_MAP.get(item.get('pred_pre_sig', ''), '')
        r['_pred_pre_fmt'] = f'{item.get("pred_pre", "")}({sig})'
        return r

    _print_table(items, cols_disp, widths, left_set, row_num=True, row_fn=_row)

    try:
        count = save_ka10031(items)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# ka10032 – 거래대금상위요청
# ═══════════════════════════════════════════════════════

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
    api_id = 'ka10032'
    spec = _req_spec(api_id)
    print(f'\n[{spec["name"]} ({api_id})]')
    print('─' * 60)

    mrkt_tp      = _prompt_choice(api_id, 'mrkt_tp',      '001')
    mang_stk_incls = _prompt_choice(api_id, 'mang_stk_incls', '1')

    print('\n  → 조회 중...')
    result = get_trade_amount_rank(token, mrkt_tp=mrkt_tp,
                                   mang_stk_incls=mang_stk_incls)

    if result.get('return_code') != 0:
        print(f'  [오류] {result.get("return_msg")}')
        return

    list_key, cols = _resp_cols(api_id, skip={'mrkt_tp'})
    items = result.get(list_key, [])
    if not items:
        print('  조회 결과가 없습니다.')
        return

    cols_disp = []
    for c in cols:
        cols_disp.append(c)
        if c['key'] == 'stk_cd':
            cols_disp.append({'key': '_market', 'label': '시장'})

    widths   = [8, 8, 12, 6, 24, 10, 8, 12, 14]
    left_set = {'stk_nm', '_market'}

    def _row(item):
        r = dict(item)
        r['_market'] = _market_label(item, mrkt_tp)
        return r

    _print_table(items, cols_disp, widths, left_set, row_num=False, row_fn=_row)

    try:
        count = save_ka10032(items)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')


# ═══════════════════════════════════════════════════════
# DB 저장 – ka10030
# ═══════════════════════════════════════════════════════

_INSERT_KA10030 = """
    INSERT INTO ka10030_tdy_trde_qty_upper
        (req_dt, req_mrkt_tp, req_sort_tp, req_mang_stk_incls, req_crd_tp,
         req_trde_qty_tp, req_pric_tp, req_trde_prica_tp, req_mrkt_open_tp, req_stex_tp,
         rsp_rank, rsp_stk_cd, rsp_stk_nm, rsp_mrkt_tp, rsp_cur_prc, rsp_flu_rt, rsp_trde_qty, rsp_pred_rt, rsp_trde_amt)
    VALUES
        (%(req_dt)s, %(req_mrkt_tp)s, %(req_sort_tp)s, %(req_mang_stk_incls)s, %(req_crd_tp)s,
         %(req_trde_qty_tp)s, %(req_pric_tp)s, %(req_trde_prica_tp)s, %(req_mrkt_open_tp)s, %(req_stex_tp)s,
         %(rsp_rank)s, %(rsp_stk_cd)s, %(rsp_stk_nm)s, %(rsp_mrkt_tp)s, %(rsp_cur_prc)s,
         %(rsp_flu_rt)s, %(rsp_trde_qty)s, %(rsp_pred_rt)s, %(rsp_trde_amt)s)
    ON DUPLICATE KEY UPDATE
        rsp_stk_nm = VALUES(rsp_stk_nm),
        rsp_mrkt_tp = VALUES(rsp_mrkt_tp),
        rsp_cur_prc = VALUES(rsp_cur_prc),
        rsp_flu_rt = VALUES(rsp_flu_rt),
        rsp_trde_qty = VALUES(rsp_trde_qty),
        rsp_pred_rt = VALUES(rsp_pred_rt),
        rsp_trde_amt = VALUES(rsp_trde_amt),
        fetched_at = CURRENT_TIMESTAMP
"""


def save_ka10030(items: list, request_params: dict = None) -> int:
    """당일거래량상위 리스트를 ka10030_tdy_trde_qty_upper 테이블에 저장합니다.

    Args:
        items: API 응답의 tdy_trde_qty_upper 리스트
    Returns:
        삽입된 행 수
    """
    if not items:
        return 0

    request_params = request_params or {}

    rows = []
    for idx, item in enumerate(items, 1):
        rows.append({
            'req_dt': request_params.get('req_dt', ''),
            'req_mrkt_tp': request_params.get('mrkt_tp', ''),
            'req_sort_tp': request_params.get('sort_tp', ''),
            'req_mang_stk_incls': request_params.get('mang_stk_incls', ''),
            'req_crd_tp': request_params.get('crd_tp', ''),
            'req_trde_qty_tp': request_params.get('trde_qty_tp', ''),
            'req_pric_tp': request_params.get('pric_tp', ''),
            'req_trde_prica_tp': request_params.get('trde_prica_tp', ''),
            'req_mrkt_open_tp': request_params.get('mrkt_open_tp', ''),
            'req_stex_tp': request_params.get('stex_tp', ''),
            'rsp_rank': idx,
            'rsp_stk_cd':   item.get('stk_cd',   ''),
            'rsp_stk_nm':   item.get('stk_nm',   ''),
            'rsp_mrkt_tp':  item.get('mrkt_tp',  ''),
            'rsp_cur_prc':  item.get('cur_prc',  ''),
            'rsp_flu_rt':   item.get('flu_rt',   ''),
            'rsp_trde_qty': item.get('trde_qty', ''),
            'rsp_pred_rt':  item.get('pred_rt',  ''),
            'rsp_trde_amt': item.get('trde_amt', ''),
        })

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10030, rows)
        conn.commit()
        print(f'  [DB 저장] ka10030_tdy_trde_qty_upper: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()


# ═══════════════════════════════════════════════════════
# DB 저장 – ka10031
# ═══════════════════════════════════════════════════════

_INSERT_KA10031 = """
    INSERT INTO ka10031_pred_trde_qty_upper
        (header_id, stk_cd, stk_nm, mrkt_tp, cur_prc, pred_pre_sig, pred_pre, trde_qty)
    VALUES
        (%(header_id)s, %(stk_cd)s, %(stk_nm)s, %(mrkt_tp)s, %(cur_prc)s, %(pred_pre_sig)s, %(pred_pre)s, %(trde_qty)s)
"""


def save_ka10031(items: list) -> int:
    """전일거래량상위 리스트를 ka10031_pred_trde_qty_upper 테이블에 저장합니다."""
    if not items:
        return 0

    header_id = int(datetime.now().timestamp() * 1000)
    rows = []
    for item in items:
        rows.append({
            'header_id': header_id,
            'stk_cd': item.get('stk_cd', ''),
            'stk_nm': item.get('stk_nm', ''),
            'mrkt_tp': item.get('mrkt_tp', ''),
            'cur_prc': item.get('cur_prc', ''),
            'pred_pre_sig': item.get('pred_pre_sig', ''),
            'pred_pre': item.get('pred_pre', ''),
            'trde_qty': item.get('trde_qty', ''),
        })

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10031, rows)
        conn.commit()
        print(f'  [DB 저장] ka10031_pred_trde_qty_upper: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()


# ═══════════════════════════════════════════════════════
# DB 저장 – ka10023
# ═══════════════════════════════════════════════════════

_INSERT_KA10023 = """
    INSERT INTO ka10023_trde_qty_sdnin
        (header_id, stk_cd, stk_nm, mrkt_tp, cur_prc, flu_rt, prev_trde_qty, now_trde_qty, sdnin_qty, sdnin_rt)
    VALUES
        (%(header_id)s, %(stk_cd)s, %(stk_nm)s, %(mrkt_tp)s, %(cur_prc)s, %(flu_rt)s, %(prev_trde_qty)s, %(now_trde_qty)s, %(sdnin_qty)s, %(sdnin_rt)s)
"""


def save_ka10023(items: list) -> int:
    """거래량급증 리스트를 ka10023_trde_qty_sdnin 테이블에 저장합니다."""
    if not items:
        return 0

    header_id = int(datetime.now().timestamp() * 1000)
    rows = []
    for item in items:
        rows.append({
            'header_id': header_id,
            'stk_cd': item.get('stk_cd', ''),
            'stk_nm': item.get('stk_nm', ''),
            'mrkt_tp': item.get('mrkt_tp', ''),
            'cur_prc': item.get('cur_prc', ''),
            'flu_rt': item.get('flu_rt', ''),
            'prev_trde_qty': item.get('prev_trde_qty', ''),
            'now_trde_qty': item.get('now_trde_qty', ''),
            'sdnin_qty': item.get('sdnin_qty', ''),
            'sdnin_rt': item.get('sdnin_rt', ''),
        })

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10023, rows)
        conn.commit()
        print(f'  [DB 저장] ka10023_trde_qty_sdnin: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()


# ═══════════════════════════════════════════════════════
# DB 저장 – ka10032
# ═══════════════════════════════════════════════════════

_INSERT_KA10032 = """
    INSERT INTO ka10032_trde_prica_upper
        (header_id, now_rank, pred_rank, stk_cd, stk_nm, mrkt_tp, cur_prc, flu_rt, now_trde_qty, trde_prica)
    VALUES
        (%(header_id)s, %(now_rank)s, %(pred_rank)s, %(stk_cd)s, %(stk_nm)s, %(mrkt_tp)s, %(cur_prc)s, %(flu_rt)s, %(now_trde_qty)s, %(trde_prica)s)
"""


def save_ka10032(items: list) -> int:
    """거래대금상위 리스트를 ka10032_trde_prica_upper 테이블에 저장합니다."""
    if not items:
        return 0

    header_id = int(datetime.now().timestamp() * 1000)
    rows = []
    for item in items:
        rows.append({
            'header_id': header_id,
            'now_rank': item.get('now_rank', ''),
            'pred_rank': item.get('pred_rank', ''),
            'stk_cd': item.get('stk_cd', ''),
            'stk_nm': item.get('stk_nm', ''),
            'mrkt_tp': item.get('mrkt_tp', ''),
            'cur_prc': item.get('cur_prc', ''),
            'flu_rt': item.get('flu_rt', ''),
            'now_trde_qty': item.get('now_trde_qty', ''),
            'trde_prica': item.get('trde_prica', ''),
        })

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_INSERT_KA10032, rows)
        conn.commit()
        print(f'  [DB 저장] ka10032_trde_prica_upper: {len(rows)}행 저장됨')
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()
