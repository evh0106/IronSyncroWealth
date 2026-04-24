"""
WebSocket 데이터 파싱 로직 단위 테스트 (DB 연결 없음)

응답 데이터 파싱 로직의 정확성을 검증합니다.
"""

import json
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# 파싱 함수 (websocket/db.py에서 복사)
# ─────────────────────────────────────────────────────────────
def parse_response_data(api_type: str, response: dict) -> list[dict]:
    """
    WebSocket 응답을 파싱하여 컬럼 딕셔너리 리스트로 변환합니다.
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
    
    # data 배열 처리
    data_list = response.get('data', [])
    if not isinstance(data_list, list):
        data_list = [data_list]
    
    for data_item in data_list:
        row = base_row.copy()
        
        # 종목코드/등록요소
        req_item = data_item.get('item', '')
        row['req_item'] = req_item
        
        # values 파싱 (FID → rsp_f{FID})
        values_list = data_item.get('values', [])
        if not isinstance(values_list, list):
            values_list = [values_list]
        
        for val_item in values_list:
            if isinstance(val_item, dict):
                # {"name": "FID번호", "value": "값"} 형식
                fid = val_item.get('name', '')
                value = val_item.get('value', '')
                
                if fid:
                    col_name = f'rsp_f{fid}'
                    row[col_name] = value
            elif isinstance(val_item, str):
                # 간단한 문자열 형식 (거의 안 쓰임)
                pass
        
        result_list.append(row)
    
    return result_list


# ─────────────────────────────────────────────────────────────
# 테스트 데이터
# ─────────────────────────────────────────────────────────────
TEST_RESPONSES = {
    '0A': {
        'trnm': '0A',
        'return_code': '0',
        'return_msg': 'success',
        'data': [
            {
                'type': '0A',
                'name': '주식기세',
                'item': '005930',  # 삼성전자
                'values': [
                    {'name': '10', 'value': '70000'},
                    {'name': '11', 'value': '500'},
                    {'name': '12', 'value': '0.71'},
                    {'name': '27', 'value': '70100'},
                    {'name': '28', 'value': '70000'},
                    {'name': '13', 'value': '12345678'},
                    {'name': '14', 'value': '864000000000'},
                ]
            }
        ]
    },
    '0B': {
        'trnm': '0B',
        'return_code': '0',
        'return_msg': 'success',
        'data': [
            {
                'type': '0B',
                'name': '주식체결',
                'item': '005930',
                'values': [
                    {'name': '20', 'value': '150000'},  # 체결시간
                    {'name': '10', 'value': '70000'},   # 현재가
                    {'name': '11', 'value': '500'},     # 전일대비
                ]
            }
        ]
    },
    '04': {
        'trnm': '04',
        'return_code': '0',
        'return_msg': 'success',
        'data': [
            {
                'type': '04',
                'name': '잔고',
                'item': '11111111',
                'values': [
                    {'name': '9201', 'value': '11111111'},
                    {'name': '9001', 'value': '005930'},
                    {'name': '302', 'value': '삼성전자'},
                ]
            }
        ]
    }
}


# ─────────────────────────────────────────────────────────────
# 테스트 함수
# ─────────────────────────────────────────────────────────────
def test_parsing():
    """응답 데이터 파싱을 테스트합니다."""
    print('=' * 80)
    print('WebSocket 응답 데이터 파싱 테스트')
    print('=' * 80)
    
    all_passed = True
    
    for api_type, response in TEST_RESPONSES.items():
        print(f'\n[테스트] API 타입: {api_type}')
        
        try:
            rows = parse_response_data(api_type, response)
            print(f'✓ 파싱 성공: {len(rows)} 행')
            
            # 각 행 검증
            for i, row in enumerate(rows):
                print(f'\n  행 {i+1}:')
                
                # 공통 컬럼 확인
                print(f'    ├─ req_type: {row.get("req_type")}')
                print(f'    ├─ req_item: {row.get("req_item")}')
                print(f'    ├─ rsp_return_code: {row.get("rsp_return_code")}')
                print(f'    ├─ rsp_return_msg: {row.get("rsp_return_msg")}')
                
                # FID 컬럼들
                fid_cols = {k: v for k, v in row.items() if k.startswith('rsp_f')}
                print(f'    └─ FID 데이터: {len(fid_cols)} 개')
                
                for fid_col, value in sorted(fid_cols.items()):
                    fid_num = fid_col.replace('rsp_f', '')
                    print(f'       {fid_num}: {value}')
                
                # 전체 컬럼 목록
                all_cols = sorted(row.keys())
                print(f'\n    전체 컬럼 ({len(all_cols)}개): {", ".join(all_cols)}')
        
        except Exception as exc:
            print(f'✗ 파싱 실패: {exc}')
            all_passed = False
    
    print('\n' + '=' * 80)
    if all_passed:
        print('✓ 모든 테스트 통과!')
    else:
        print('✗ 일부 테스트 실패')
    print('=' * 80)
    
    return all_passed


if __name__ == '__main__':
    success = test_parsing()
    exit(0 if success else 1)
