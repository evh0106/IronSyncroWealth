"""
키움증권 REST API 샘플 코드
- 토큰 발급 및 주식 매수 주문 예제
"""

import requests
import json
from oauth2 import HOST, get_access_token, load_api_keys, revoke_access_token

# ============================================================
# 2. 주식 매수 주문
# ============================================================
def buy_order(token: str, stock_code: str, order_qty: int, order_price: str = '', trade_type: str = '3'):
    """
    주식 매수 주문을 요청합니다.

    Parameters
    ----------
    token : str
        액세스 토큰
    stock_code : str
        종목 코드 (예: '039490' - 키움증권)
    order_qty : int
        주문 수량
    order_price : str
        주문 단가 (시장가 주문 시 빈 문자열)
    trade_type : str
        매매 구분
        - '1': 지정가
        - '3': 시장가 (기본값)
    """
    url = HOST + '/api/dostk/ordr'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': 'N',       # 연속조회 여부 (N: 최초 조회)
        'next-key': '',       # 연속조회 키 (최초 조회 시 빈 값)
        'api-id': 'kt10000',  # 현물 매수 주문 TR
    }

    data = {
        'dmst_stex_tp': 'KRX',       # 거래소 구분
        'stk_cd': stock_code,         # 종목 코드
        'ord_qty': str(order_qty),    # 주문 수량
        'ord_uv': order_price,        # 주문 단가 (시장가는 빈 값)
        'trde_tp': trade_type,        # 매매 구분
        'cond_uv': '',                # 조건 단가
    }

    print(f'\n[매수 주문 요청]')
    print(f'  종목코드: {stock_code}')
    print(f'  주문수량: {order_qty}')
    print(f'  매매구분: {"시장가" if trade_type == "3" else "지정가"}')

    response = requests.post(url, headers=headers, json=data)

    print(f'\n[응답 결과]')
    print(f'  Code  : {response.status_code}')
    print(f'  Header: {json.dumps(dict(response.headers), indent=4, ensure_ascii=False)}')
    print(f'  Body  : {json.dumps(response.json(), indent=4, ensure_ascii=False)}')

    return response


# ============================================================
# 3. 주식 매도 주문
# ============================================================
def sell_order(token: str, stock_code: str, order_qty: int, order_price: str = '', trade_type: str = '3'):
    """
    주식 매도 주문을 요청합니다.

    Parameters
    ----------
    token : str
        액세스 토큰
    stock_code : str
        종목 코드
    order_qty : int
        주문 수량
    order_price : str
        주문 단가 (시장가 주문 시 빈 문자열)
    trade_type : str
        매매 구분
        - '1': 지정가
        - '3': 시장가 (기본값)
    """
    url = HOST + '/api/dostk/ordr'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': 'N',
        'next-key': '',
        'api-id': 'kt10001',  # 현물 매도 주문 TR
    }

    data = {
        'dmst_stex_tp': 'KRX',
        'stk_cd': stock_code,
        'ord_qty': str(order_qty),
        'ord_uv': order_price,
        'trde_tp': trade_type,
        'cond_uv': '',
    }

    print(f'\n[매도 주문 요청]')
    print(f'  종목코드: {stock_code}')
    print(f'  주문수량: {order_qty}')
    print(f'  매매구분: {"시장가" if trade_type == "3" else "지정가"}')

    response = requests.post(url, headers=headers, json=data)

    print(f'\n[응답 결과]')
    print(f'  Code  : {response.status_code}')
    print(f'  Body  : {json.dumps(response.json(), indent=4, ensure_ascii=False)}')

    return response


# ============================================================
# 메인 실행
# ============================================================
if __name__ == '__main__':
    APP_KEY, APP_SECRET = load_api_keys()

    # 1. 토큰 발급
    token = get_access_token(APP_KEY, APP_SECRET)

    # 2. 키움증권(039490) 1주 시장가 매수
    buy_order(
        token=token,
        stock_code='039490',
        order_qty=1,
    )

    # 3. 토큰 폐기
    revoke_access_token(APP_KEY, APP_SECRET, token)
