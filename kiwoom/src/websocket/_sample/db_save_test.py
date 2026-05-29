"""
WebSocket DB 저장 기능 테스트 코드

웹소켓으로부터 수신한 실시간 데이터를 DB에 저장하는 기능을 테스트합니다.
"""

import sys
import json
from datetime import datetime
from pathlib import Path
import importlib.util

# 부모 디렉토리를 파이썬 경로에 추가
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# 직접 모듈 import (websocket 패키지 전체 import 회피)
import importlib.util
spec = importlib.util.spec_from_file_location("ws_db", 
    Path(__file__).parent.parent / "db.py")
ws_db = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ws_db)

save_websocket_data = ws_db.save_websocket_data
save_websocket_realtime = ws_db.save_websocket_realtime
_parse_response_data = ws_db._parse_response_data


# ─────────────────────────────────────────────────────────────
# 테스트 데이터 (실제 WebSocket 응답 포맷)
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
                    {'name': '12', 'value': '0.71'},    # 등락율
                    {'name': '27', 'value': '70100'},   # 매도호가
                    {'name': '28', 'value': '70000'},   # 매수호가
                    {'name': '15', 'value': '10000'},   # 거래량
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
                'item': '11111111',  # 계좌번호
                'values': [
                    {'name': '9201', 'value': '11111111'},  # 계좌번호
                    {'name': '9001', 'value': '005930'},    # 종목코드
                    {'name': '302', 'value': '삼성전자'},    # 종목명
                    {'name': '10', 'value': '70000'},       # 현재가
                    {'name': '930', 'value': '100'},        # 보유수량
                    {'name': '931', 'value': '65000'},      # 매입단가
                ]
            }
        ]
    }
}


# ─────────────────────────────────────────────────────────────
# 테스트 함수
# ─────────────────────────────────────────────────────────────
def test_save_websocket_data():
    """각 API 타입별로 DB 저장 기능을 테스트합니다."""
    print('=' * 60)
    print('WebSocket DB 저장 기능 테스트')
    print('=' * 60)
    
    for api_type, response in TEST_RESPONSES.items():
        print(f'\n[테스트] API 타입: {api_type}')
        print(f'  응답: {json.dumps(response, ensure_ascii=False, indent=2)[:100]}...')
        
        try:
            saved_count = save_websocket_data(api_type, response)
            print(f'  결과: {saved_count} 행 저장됨')
        except Exception as exc:
            print(f'  오류: {exc}')


def test_save_websocket_realtime():
    """save_websocket_realtime 함수를 테스트합니다."""
    print('\n' + '=' * 60)
    print('WebSocket 실시간 저장 함수 테스트')
    print('=' * 60)
    
    for api_type, response in TEST_RESPONSES.items():
        print(f'\n[테스트] trnm: {api_type}')
        
        try:
            saved_count = save_websocket_realtime(response)
            print(f'  결과: {saved_count} 행 저장됨')
        except Exception as exc:
            print(f'  오류: {exc}')


def test_parse_response():
    """응답 데이터 파싱을 테스트합니다."""
    print('\n' + '=' * 60)
    print('응답 데이터 파싱 테스트')
    print('=' * 60)
    
    for api_type, response in TEST_RESPONSES.items():
        print(f'\n[테스트] API 타입: {api_type}')
        
        try:
            rows = _parse_response_data(api_type, response)
            print(f'  파싱된 행 수: {len(rows)}')
            
            for i, row in enumerate(rows):
                print(f'  행 {i+1}:')
                for key, value in sorted(row.items()):
                    if key.startswith('rsp_f'):
                        print(f'    {key}: {value}')
        except Exception as exc:
            print(f'  오류: {exc}')


# ─────────────────────────────────────────────────────────────
# 메인
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    try:
        test_parse_response()
        test_save_websocket_data()
        test_save_websocket_realtime()
        
        print('\n' + '=' * 60)
        print('테스트 완료')
        print('=' * 60)
    except Exception as exc:
        print(f'\n테스트 실패: {exc}')
        sys.exit(1)
