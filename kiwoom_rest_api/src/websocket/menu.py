"""
키움증권 WebSocket 전용 메뉴
websocket.websocket 모듈이 독립 실행될 때 사용합니다.
"""

from volume._fmt import _ljust

REALTIME_TYPES = [
    ('0B', '주식체결'),
    ('0C', '주식우선호가'),
    ('0D', '주식호가잔량'),
    ('0A', '주식기세'),
    ('0E', '주식시간외호가'),
    ('0F', '주식당일거래원'),
    ('0G', 'ETF NAV'),
    ('0H', '주식예상체결'),
    ('0g', '주식종목정보'),
    ('0w', '종목프로그램매매'),
    ('1h', 'VI발동/해제'),
]

ACCOUNT_TYPES = [
    ('00', '주문체결  (계좌 기반)'),
    ('04', '잔고      (계좌 기반)'),
    ('0s', '장시작시간 (계좌 기반)'),
    ('0J', '업종지수'),
    ('0U', '업종등락'),
    ('0I', '국제금환산가격'),
    ('0m', 'ELW 이론가'),
    ('0u', 'ELW 지표'),
]

WEBSOCKET_MENU_ITEMS = [
    ('1', '종목 실시간 시세      (0A/0B/0C/...)', 'run_realtime_quote'),
    ('2', '계좌/기타 실시간      (00/04/0J/...)', 'run_account_realtime'),
    ('3', '조건검색              (ka10171~74)', 'run_condition_search'),
]


def print_websocket_menu() -> None:
    print()
    print('╔══════════════════════════════════════════════╗')
    print(f'║  {_ljust("키움 WebSocket 메뉴", 40)}║')
    print('╠══════════════════════════════════════════════╣')
    for key, label, _ in WEBSOCKET_MENU_ITEMS:
        print(f'║  [{key}] {_ljust(label, 40)}║')
    print(f'║  [0] {_ljust("종료", 40)}║')
    print('╚══════════════════════════════════════════════╝')


def run_websocket_menu(token: str) -> None:
    """토큰을 받아 WebSocket 전용 메뉴 루프를 실행합니다."""
    from .websocket import run_realtime_quote, run_account_realtime, run_condition_search

    handlers = {
        'run_realtime_quote': run_realtime_quote,
        'run_account_realtime': run_account_realtime,
        'run_condition_search': run_condition_search,
    }
    menu_map = {k: handlers[name] for k, _, name in WEBSOCKET_MENU_ITEMS}

    while True:
        print_websocket_menu()
        choice = input('메뉴 선택: ').strip()

        if choice == '0':
            print('\n웹소켓 프로그램을 종료합니다.')
            return

        fn = menu_map.get(choice)
        if fn is None:
            print(f'  알 수 없는 메뉴: {choice!r}  (0~{len(WEBSOCKET_MENU_ITEMS)} 사이 값을 입력하세요)')
            continue

        try:
            fn(token)
        except Exception as e:
            print(f'\n[오류] 기능 실행 중 문제가 발생했습니다: {e}')
