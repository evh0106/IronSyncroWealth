"""
업종현재가요청 (ka20001)
국내주식 > 업종 > 업종현재가요청

업종코드별 현재가·전일대비·등락률 등을 조회합니다.
"""

import requests
from datetime import datetime
import db
from logger import log_http_request, log_http_response
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
_SECT_URL = HOST + '/api/dostk/sect'

_UPSERT_KA20001 = """
    INSERT INTO ka20001_inds_cur_prc (
        req_dt, req_mrkt_tp, req_sect_cd,
        rsp_tm_n, rsp_cur_prc, rsp_pred_pre_sig, rsp_pred_pre, rsp_flu_rt,
        rsp_trde_qty, rsp_trde_prica, rsp_trde_frmatn_stk_num, rsp_trde_frmatn_rt,
        rsp_open_pric, rsp_high_pric, rsp_low_pric, rsp_upl, rsp_rising,
        rsp_stdns, rsp_fall, rsp_lst, rsp_w52_hgst_pric, rsp_w52_hgst_pric_dt,
        rsp_w52_hgst_pric_pre_rt, rsp_w52_lwst_pric, rsp_w52_lwst_pric_dt,
        rsp_w52_lwst_pric_pre_rt, rsp_cur_prc_n, rsp_pred_pre_sig_n,
        rsp_pred_pre_n, rsp_flu_rt_n, rsp_trde_qty_n, rsp_acc_trde_qty_n
    )
    VALUES (
        %(req_dt)s, %(req_mrkt_tp)s, %(req_sect_cd)s,
        %(rsp_tm_n)s, %(rsp_cur_prc)s, %(rsp_pred_pre_sig)s, %(rsp_pred_pre)s, %(rsp_flu_rt)s,
        %(rsp_trde_qty)s, %(rsp_trde_prica)s, %(rsp_trde_frmatn_stk_num)s, %(rsp_trde_frmatn_rt)s,
        %(rsp_open_pric)s, %(rsp_high_pric)s, %(rsp_low_pric)s, %(rsp_upl)s, %(rsp_rising)s,
        %(rsp_stdns)s, %(rsp_fall)s, %(rsp_lst)s, %(rsp_w52_hgst_pric)s, %(rsp_w52_hgst_pric_dt)s,
        %(rsp_w52_hgst_pric_pre_rt)s, %(rsp_w52_lwst_pric)s, %(rsp_w52_lwst_pric_dt)s,
        %(rsp_w52_lwst_pric_pre_rt)s, %(rsp_cur_prc_n)s, %(rsp_pred_pre_sig_n)s,
        %(rsp_pred_pre_n)s, %(rsp_flu_rt_n)s, %(rsp_trde_qty_n)s, %(rsp_acc_trde_qty_n)s
    )
    ON DUPLICATE KEY UPDATE
        rsp_cur_prc = VALUES(rsp_cur_prc),
        rsp_pred_pre_sig = VALUES(rsp_pred_pre_sig),
        rsp_pred_pre = VALUES(rsp_pred_pre),
        rsp_flu_rt = VALUES(rsp_flu_rt),
        rsp_trde_qty = VALUES(rsp_trde_qty),
        rsp_trde_prica = VALUES(rsp_trde_prica),
        rsp_trde_frmatn_stk_num = VALUES(rsp_trde_frmatn_stk_num),
        rsp_trde_frmatn_rt = VALUES(rsp_trde_frmatn_rt),
        rsp_open_pric = VALUES(rsp_open_pric),
        rsp_high_pric = VALUES(rsp_high_pric),
        rsp_low_pric = VALUES(rsp_low_pric),
        rsp_upl = VALUES(rsp_upl),
        rsp_rising = VALUES(rsp_rising),
        rsp_stdns = VALUES(rsp_stdns),
        rsp_fall = VALUES(rsp_fall),
        rsp_lst = VALUES(rsp_lst),
        rsp_w52_hgst_pric = VALUES(rsp_w52_hgst_pric),
        rsp_w52_hgst_pric_dt = VALUES(rsp_w52_hgst_pric_dt),
        rsp_w52_hgst_pric_pre_rt = VALUES(rsp_w52_hgst_pric_pre_rt),
        rsp_w52_lwst_pric = VALUES(rsp_w52_lwst_pric),
        rsp_w52_lwst_pric_dt = VALUES(rsp_w52_lwst_pric_dt),
        rsp_w52_lwst_pric_pre_rt = VALUES(rsp_w52_lwst_pric_pre_rt),
        rsp_cur_prc_n = VALUES(rsp_cur_prc_n),
        rsp_pred_pre_sig_n = VALUES(rsp_pred_pre_sig_n),
        rsp_pred_pre_n = VALUES(rsp_pred_pre_n),
        rsp_flu_rt_n = VALUES(rsp_flu_rt_n),
        rsp_trde_qty_n = VALUES(rsp_trde_qty_n),
        rsp_acc_trde_qty_n = VALUES(rsp_acc_trde_qty_n),
        fetched_at = CURRENT_TIMESTAMP
"""


def save_ka20001(result: dict, request_params: dict) -> int:
    """업종현재가요청 응답을 ka20001_inds_cur_prc 테이블에 저장합니다."""
    items = result.get('inds_cur_prc_tm', [])
    if not items:
        return 0

    rows = []
    for item in items:
        rows.append({
            'req_dt': request_params.get('req_dt', ''),
            'req_mrkt_tp': request_params.get('mrkt_tp', ''),
            'req_sect_cd': request_params.get('sect_cd', ''),
            'rsp_tm_n': item.get('tm_n', ''),
            'rsp_cur_prc': result.get('cur_prc'),
            'rsp_pred_pre_sig': result.get('pred_pre_sig'),
            'rsp_pred_pre': result.get('pred_pre'),
            'rsp_flu_rt': result.get('flu_rt'),
            'rsp_trde_qty': result.get('trde_qty'),
            'rsp_trde_prica': result.get('trde_prica'),
            'rsp_trde_frmatn_stk_num': result.get('trde_frmatn_stk_num'),
            'rsp_trde_frmatn_rt': result.get('trde_frmatn_rt'),
            'rsp_open_pric': result.get('open_pric'),
            'rsp_high_pric': result.get('high_pric'),
            'rsp_low_pric': result.get('low_pric'),
            'rsp_upl': result.get('upl'),
            'rsp_rising': result.get('rising'),
            'rsp_stdns': result.get('stdns'),
            'rsp_fall': result.get('fall'),
            'rsp_lst': result.get('lst'),
            'rsp_w52_hgst_pric': result.get('52wk_hgst_pric'),
            'rsp_w52_hgst_pric_dt': result.get('52wk_hgst_pric_dt'),
            'rsp_w52_hgst_pric_pre_rt': result.get('52wk_hgst_pric_pre_rt'),
            'rsp_w52_lwst_pric': result.get('52wk_lwst_pric'),
            'rsp_w52_lwst_pric_dt': result.get('52wk_lwst_pric_dt'),
            'rsp_w52_lwst_pric_pre_rt': result.get('52wk_lwst_pric_pre_rt'),
            'rsp_cur_prc_n': item.get('cur_prc_n'),
            'rsp_pred_pre_sig_n': item.get('pred_pre_sig_n'),
            'rsp_pred_pre_n': item.get('pred_pre_n'),
            'rsp_flu_rt_n': item.get('flu_rt_n'),
            'rsp_trde_qty_n': item.get('trde_qty_n'),
            'rsp_acc_trde_qty_n': item.get('acc_trde_qty_n'),
        })

    print(f'\n  [SQL] {_UPSERT_KA20001.strip()}')
    print(f'  [파라미터 예시] {rows[0] if rows else {}}')

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(_UPSERT_KA20001, rows)
        conn.commit()
        return len(rows)
    except Exception as e:
        conn.rollback()
        print(f'  [DB 오류] {type(e).__name__}: {e}')
        raise
    finally:
        conn.close()


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

    session = requests.Session()
    req = requests.Request('POST', _SECT_URL, headers=headers, json=body)
    preq = session.prepare_request(req)

    path, req_id = log_http_request(
        api_id='ka20001',
        url=_SECT_URL,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name='sect',
    )
    print(f'  → 요청 로그 저장: {path}')

    response = session.send(preq)
    path = log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name='sect',
    )
    print(f'  → 응답 로그 저장: {path}')
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

    request_params = {
        'req_dt': datetime.now().strftime('%Y%m%d'),
        'mrkt_tp': mrkt_tp,
        'sect_cd': sect_cd,
    }

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

    try:
        count = save_ka20001(result, request_params)
        print(f'  → {count}건 저장 완료.')
    except Exception as e:
        print(f'  [DB 오류] {e}')

