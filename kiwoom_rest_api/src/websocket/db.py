"""
WebSocket 실시간 데이터 DB 저장 모듈

웹소켓으로부터 수신한 실시간 데이터를 데이터타입별 테이블에 저장합니다.
각 API 타입(0A, 0B, 0D 등)별로 INSERT 쿼리를 정의하고 실행합니다.
"""

from datetime import datetime
import sys
from pathlib import Path

# 부모 디렉토리의 db 모듈 import
sys.path.insert(0, str(Path(__file__).parent.parent))
import db


# ─────────────────────────────────────────────────────────────
# 테이블명 매핑: API타입 → 테이블명
# ─────────────────────────────────────────────────────────────
_TABLE_MAPPING = {
    '00': 'ws_00_ord_ccls',         # 주문체결
    '04': 'ws_04_balance',          # 잔고
    '0A': 'ws_0a_stk_kse',          # 주식기세
    '0B': 'ws_0b_stk_ccls',         # 주식체결
    '0C': 'ws_0c_stk_prio_hga',     # 주식우선호가
    '0D': 'ws_0d_stk_hga_qty',      # 주식호가잔량
    '0E': 'ws_0e_stk_ah_hga',       # 주식시간외호가
    '0F': 'ws_0f_stk_dly_trd',      # 주식당일거래원
    '0G': 'ws_0g_etf_nav',          # ETF NAV
    '0H': 'ws_0h_stk_exp_ccls',     # 주식예상체결
    '0I': 'ws_0i_intl_gold_prc',    # 국제금환산가격
    '0J': 'ws_0j_sect_idx',         # 업종지수
    '0U': 'ws_0u_sect_flct',        # 업종등락
    '0g': 'ws_0g_stk_nfo',          # 주식종목정보
    '0m': 'ws_0m_elw_thr',          # ELW 이론가
    '0s': 'ws_0s_mkt_tm',           # 장시작시간
    '0u': 'ws_0u_elw_idx',          # ELW 지표
    '0w': 'ws_0w_stk_prg_trd',      # 종목프로그램매매
    'ka10171': 'ws_ka10171_cndsr_lst',  # 조건검색 목록
    'ka10172': 'ws_ka10172_cndsr_req',  # 조건검색 요청 일반
    'ka10173': 'ws_ka10173_cndsr_rt',   # 조건검색 요청 실시간
    'ka10174': 'ws_ka10174_cndsr_clr',  # 조건검색 해제
}


# ─────────────────────────────────────────────────────────────
# 동적 INSERT SQL 생성
# ─────────────────────────────────────────────────────────────
def _build_insert_sql(table_name: str, columns: dict) -> tuple[str, dict]:
    """
    테이블명과 컬럼 딕셔너리로부터 INSERT SQL을 동적으로 생성합니다.
    
    Parameters
    ----------
    table_name : str
        테이블명
    columns : dict
        {컬럼명: 값} 형식의 딕셔너리
        
    Returns
    -------
    tuple[str, dict]
        (SQL 쿼리, 파라미터 딕셔너리)
    """
    col_names = list(columns.keys())
    col_placeholders = [f'%({name})s' for name in col_names]
    
    cols_str = ', '.join(col_names)
    vals_str = ', '.join(col_placeholders)
    
    sql = f'INSERT INTO {table_name} ({cols_str}) VALUES ({vals_str})'
    return sql, columns


# ─────────────────────────────────────────────────────────────
# 데이터 파싱: 응답 JSON → 컬럼 딕셔너리
# ─────────────────────────────────────────────────────────────
def _parse_response_data(api_type: str, response: dict, data_item: dict = None) -> list[dict]:
    """
    WebSocket 응답을 파싱하여 컬럼 딕셔너리 리스트로 변환합니다.
    
    실제 수신 구조 (trnm=REAL):
    {
      "trnm": "REAL",
      "data": [
        {
          "type": "00",
          "name": "주문체결",
          "item": "051980",
          "values": {
            "9201": "6512000310",
            "9203": "0808200",
            ...
          }
        }
      ]
    }
    """
    result_list = []
    
    # 기본 컬럼: 공통필드
    req_dt = datetime.now().strftime('%Y%m%d%H%M%S')
    base_row = {
        'req_dt': req_dt,
        'req_type': api_type,
        'rsp_return_code': response.get('return_code', ''),
        'rsp_return_msg': response.get('return_msg', ''),
    }
    
    # data_item이 지정된 경우 해당 항목만, 아닌 경우 data 배열 전체 처리
    if data_item is not None:
        items = [data_item]
    else:
        items = response.get('data', [])
        if not isinstance(items, list):
            items = [items]
    
    for item in items:
        row = base_row.copy()
        row['req_item'] = item.get('item', '')
        
        values = item.get('values', {})
        
        if isinstance(values, dict):
            # 실제 수신 형식: {"FID번호": "값", ...}
            for fid, value in values.items():
                row[f'rsp_f{fid}'] = value
        elif isinstance(values, list):
            # 스펙상 형식: [{"name": "FID번호", "value": "값"}, ...]
            for val_item in values:
                if isinstance(val_item, dict):
                    fid = val_item.get('name', '')
                    if fid:
                        row[f'rsp_f{fid}'] = val_item.get('value', '')
        
        result_list.append(row)
    
    return result_list


# ─────────────────────────────────────────────────────────────
# DB 저장
# ─────────────────────────────────────────────────────────────
def save_websocket_data(api_type: str, response: dict) -> int:
    """
    WebSocket 응답 데이터를 DB에 저장합니다.
    
    Parameters
    ----------
    api_type : str
        API 타입 (예: '00', '0A', 'ka10171')
    response : dict
        WebSocket 응답 JSON
        
    Returns
    -------
    int
        저장된 행 수 (실패 시 0)
    """
    # 테이블명 조회
    table_name = _TABLE_MAPPING.get(api_type)
    if not table_name:
        print(f'  [저장 오류] 알 수 없는 API 타입: {api_type}')
        return 0
    
    # 데이터 파싱
    try:
        rows = _parse_response_data(api_type, response)
    except Exception as exc:
        print(f'  [파싱 오류] {api_type}: {exc}')
        return 0
    
    if not rows:
        return 0
    
    # DB 저장
    conn = db.get_connection()
    saved_count = 0
    
    try:
        with conn.cursor() as cur:
            for row in rows:
                try:
                    sql, params = _build_insert_sql(table_name, row)
                    cur.execute(sql, params)
                    saved_count += 1
                except Exception as exc:
                    print(f'  [INSERT 오류] {table_name}: {exc}')
                    continue
        
        conn.commit()
        return saved_count
    
    except Exception as exc:
        conn.rollback()
        print(f'  [DB 커밋 오류] {exc}')
        return 0
    
    finally:
        conn.close()


def _insert_rows(table_name: str, rows: list) -> int:
    """rows를 table_name에 INSERT합니다. save_websocket_data와 동일한 DB 로직."""
    conn = db.get_connection()
    saved_count = 0
    try:
        with conn.cursor() as cur:
            for row in rows:
                try:
                    sql, params = _build_insert_sql(table_name, row)
                    cur.execute(sql, params)
                    saved_count += 1
                except Exception as exc:
                    print(f'  [INSERT 오류] {table_name}: {exc}')
                    continue
        conn.commit()
        return saved_count
    except Exception as exc:
        conn.rollback()
        print(f'  [DB 커밋 오류] {exc}')
        return 0
    finally:
        conn.close()


def save_websocket_realtime(response: dict) -> int:
    """
    WebSocket 실시간 데이터를 DB에 저장합니다.
    
    trnm == 'REAL' 인 경우 data[].type 기준으로 항목별로 저장합니다.
    그 외에는 trnm을 직접 API 타입으로 사용합니다.
    """
    trnm = response.get('trnm', '')
    
    # 제어 메시지 제외
    if trnm in ('LOGIN', 'PING', 'REG', 'SYSTEM', 'CNSRLST', 'CNSRREQ', 'CNSRCLR'):
        return 0
    
    # trnm=REAL: data 배열의 각 항목 type 기준으로 저장
    if trnm == 'REAL':
        total = 0
        for data_item in response.get('data', []):
            api_type = data_item.get('type', '')
            if not api_type:
                continue
            table_name = _TABLE_MAPPING.get(api_type)
            if not table_name:
                print(f'  [저장 오류] 알 수 없는 API 타입: {api_type}')
                continue
            try:
                rows = _parse_response_data(api_type, response, data_item)
            except Exception as exc:
                print(f'  [파싱 오류] {api_type}: {exc}')
                continue
            if rows:
                total += _insert_rows(table_name, rows)
        return total
    
    return save_websocket_data(trnm, response)
