"""
websocket 패키지 – 키움증권 WebSocket API
URL: wss://api.kiwoom.com:10000/api/dostk/websocket

client (client.py):
    WebSocketClient         – 연결/로그인/송수신/종료

realtime (realtime.py):
    register                – 실시간 항목 일괄 등록
    remove                  – 실시간 항목 일괄 해제

    register_order_execution    – 주문체결(00)
    register_balance            – 잔고(04)
    register_stock_momentum     – 주식기세(0A)
    register_stock_execution    – 주식체결(0B)
    register_stock_best_quote   – 주식우선호가(0C)
    register_stock_orderbook    – 주식호가잔량(0D)
    register_stock_ah_quote     – 주식시간외호가(0E)
    register_stock_broker       – 주식당일거래원(0F)
    register_etf_nav            – ETF NAV(0G)
    register_stock_expected     – 주식예상체결(0H)
    register_gold_intl          – 국제금환산가격(0I)
    register_sector_index       – 업종지수(0J)
    register_sector_change      – 업종등락(0U)
    register_stock_info         – 주식종목정보(0g)
    register_elw_theory         – ELW 이론가(0m)
    register_market_open        – 장시작시간(0s)
    register_elw_indicator      – ELW 지표(0u)
    register_stock_program      – 종목프로그램매매(0w)
    register_vi_trigger         – VI발동/해제(1h)

condition (condition.py):
    get_condition_list          – 조건검색 목록조회  (ka10171)
    request_condition           – 조건검색 요청 일반 (ka10172)
    request_condition_realtime  – 조건검색 요청 실시간 (ka10173)
    remove_condition_realtime   – 조건검색 실시간 해제 (ka10174)
"""

from .client import WebSocketClient, SOCKET_URL, SOCKET_URL_PROD, SOCKET_URL_MOCK

from .realtime import (
    register,
    remove,
    register_order_execution,
    register_balance,
    register_stock_momentum,
    register_stock_execution,
    register_stock_best_quote,
    register_stock_orderbook,
    register_stock_ah_quote,
    register_stock_broker,
    register_etf_nav,
    register_stock_expected,
    register_gold_intl,
    register_sector_index,
    register_sector_change,
    register_stock_info,
    register_elw_theory,
    register_market_open,
    register_elw_indicator,
    register_stock_program,
    register_vi_trigger,
    TYPE_ORDER_EXECUTION,
    TYPE_BALANCE,
    TYPE_STOCK_MOMENTUM,
    TYPE_STOCK_EXECUTION,
    TYPE_STOCK_BEST_QUOTE,
    TYPE_STOCK_ORDERBOOK,
    TYPE_STOCK_AH_QUOTE,
    TYPE_STOCK_BROKER,
    TYPE_ETF_NAV,
    TYPE_STOCK_EXPECTED,
    TYPE_GOLD_INTL,
    TYPE_SECTOR_INDEX,
    TYPE_SECTOR_CHANGE,
    TYPE_STOCK_INFO,
    TYPE_ELW_THEORY,
    TYPE_MARKET_OPEN,
    TYPE_ELW_INDICATOR,
    TYPE_STOCK_PROGRAM,
    TYPE_VI_TRIGGER,
)

from .condition import (
    get_condition_list,
    request_condition,
    request_condition_realtime,
    remove_condition_realtime,
)

from .menu import run_websocket_menu


def run_realtime_quote(token: str):
    from .websocket import run_realtime_quote as _run_realtime_quote

    return _run_realtime_quote(token)


def run_account_realtime(token: str):
    from .websocket import run_account_realtime as _run_account_realtime

    return _run_account_realtime(token)


def run_condition_search(token: str):
    from .websocket import run_condition_search as _run_condition_search

    return _run_condition_search(token)

__all__ = [
    # client
    'WebSocketClient',
    'SOCKET_URL',
    'SOCKET_URL_PROD',
    'SOCKET_URL_MOCK',
    # realtime – 공통
    'register',
    'remove',
    # realtime – 타입별 등록
    'register_order_execution',
    'register_balance',
    'register_stock_momentum',
    'register_stock_execution',
    'register_stock_best_quote',
    'register_stock_orderbook',
    'register_stock_ah_quote',
    'register_stock_broker',
    'register_etf_nav',
    'register_stock_expected',
    'register_gold_intl',
    'register_sector_index',
    'register_sector_change',
    'register_stock_info',
    'register_elw_theory',
    'register_market_open',
    'register_elw_indicator',
    'register_stock_program',
    'register_vi_trigger',
    # realtime – 타입 상수
    'TYPE_ORDER_EXECUTION',
    'TYPE_BALANCE',
    'TYPE_STOCK_MOMENTUM',
    'TYPE_STOCK_EXECUTION',
    'TYPE_STOCK_BEST_QUOTE',
    'TYPE_STOCK_ORDERBOOK',
    'TYPE_STOCK_AH_QUOTE',
    'TYPE_STOCK_BROKER',
    'TYPE_ETF_NAV',
    'TYPE_STOCK_EXPECTED',
    'TYPE_GOLD_INTL',
    'TYPE_SECTOR_INDEX',
    'TYPE_SECTOR_CHANGE',
    'TYPE_STOCK_INFO',
    'TYPE_ELW_THEORY',
    'TYPE_MARKET_OPEN',
    'TYPE_ELW_INDICATOR',
    'TYPE_STOCK_PROGRAM',
    'TYPE_VI_TRIGGER',
    # condition
    'get_condition_list',
    'request_condition',
    'request_condition_realtime',
    'remove_condition_realtime',
    # menu (동기 진입점)
    'run_realtime_quote',
    'run_account_realtime',
    'run_condition_search',
    'run_websocket_menu',
]
