"""
키움증권 실시간 시세 WebSocket 등록/해제 헬퍼
URL: /api/dostk/websocket

실시간 항목 타입:
  00 – 주문체결      (item 불필요)
  04 – 잔고          (item 불필요)
  0A – 주식기세
  0B – 주식체결
  0C – 주식우선호가
  0D – 주식호가잔량
  0E – 주식시간외호가
  0F – 주식당일거래원
  0G – ETF NAV
  0H – 주식예상체결
  0I – 국제금환산가격
  0J – 업종지수
  0U – 업종등락
  0g – 주식종목정보
  0m – ELW 이론가
  0s – 장시작시간
  0u – ELW 지표
  0w – 종목프로그램매매
  1h – VI발동/해제
"""

from .client import WebSocketClient

# ─────────────────────────────────────────────
# 실시간 항목 타입 코드 상수
# ─────────────────────────────────────────────
TYPE_ORDER_EXECUTION   = '00'   # 주문체결
TYPE_BALANCE           = '04'   # 잔고
TYPE_STOCK_MOMENTUM    = '0A'   # 주식기세
TYPE_STOCK_EXECUTION   = '0B'   # 주식체결
TYPE_STOCK_BEST_QUOTE  = '0C'   # 주식우선호가
TYPE_STOCK_ORDERBOOK   = '0D'   # 주식호가잔량
TYPE_STOCK_AH_QUOTE    = '0E'   # 주식시간외호가
TYPE_STOCK_BROKER      = '0F'   # 주식당일거래원
TYPE_ETF_NAV           = '0G'   # ETF NAV
TYPE_STOCK_EXPECTED    = '0H'   # 주식예상체결
TYPE_GOLD_INTL         = '0I'   # 국제금환산가격
TYPE_SECTOR_INDEX      = '0J'   # 업종지수
TYPE_SECTOR_CHANGE     = '0U'   # 업종등락
TYPE_STOCK_INFO        = '0g'   # 주식종목정보
TYPE_ELW_THEORY        = '0m'   # ELW 이론가
TYPE_MARKET_OPEN       = '0s'   # 장시작시간
TYPE_ELW_INDICATOR     = '0u'   # ELW 지표
TYPE_STOCK_PROGRAM     = '0w'   # 종목프로그램매매
TYPE_VI_TRIGGER        = '1h'   # VI발동/해제


# ─────────────────────────────────────────────
# 공통 등록/해제 함수
# ─────────────────────────────────────────────
async def register(
    client: WebSocketClient,
    realtime_types: list[str],
    items: list[str] | None = None,
    group_no: str = '1',
    refresh: str = '1',
):
    """
    실시간 항목을 등록합니다. (trnm=REG)

    Parameters
    ----------
    client : WebSocketClient
        연결된 WebSocket 클라이언트
    realtime_types : list[str]
        실시간 항목 유형 목록 (예: ['0B', '0C'])
    items : list[str] | None
        종목 코드 목록. 계좌 기반 항목(00, 04)은 None으로 전달합니다.
        거래소별 종목코드 형식:
          KRX: '039490'  NXT: '039490_NX'  SOR: '039490_AL'
    group_no : str
        그룹 번호 (기본값 '1')
    refresh : str
        기존 등록 유지 여부 ('1': 유지, '0': 해제 후 재등록)
    """
    data_entry = {'type': realtime_types}
    if items is not None:
        data_entry['item'] = items

    await client.send_message({
        'trnm': 'REG',
        'grp_no': group_no,
        'refresh': refresh,
        'data': [data_entry],
    })


async def remove(
    client: WebSocketClient,
    realtime_types: list[str],
    items: list[str] | None = None,
    group_no: str = '1',
):
    """
    실시간 항목 등록을 해제합니다. (trnm=REMOVE)

    Parameters
    ----------
    client : WebSocketClient
        연결된 WebSocket 클라이언트
    realtime_types : list[str]
        해제할 실시간 항목 유형 목록
    items : list[str] | None
        해제할 종목 코드 목록. None이면 전체 해제.
    group_no : str
        그룹 번호
    """
    data_entry = {'type': realtime_types}
    if items is not None:
        data_entry['item'] = items

    await client.send_message({
        'trnm': 'REMOVE',
        'grp_no': group_no,
        'data': [data_entry],
    })


# ─────────────────────────────────────────────
# 타입별 편의 함수
# ─────────────────────────────────────────────

async def register_order_execution(client: WebSocketClient, group_no: str = '1', refresh: str = '1'):
    """주문체결(00) 실시간 등록 – 종목코드 불필요"""
    await register(client, [TYPE_ORDER_EXECUTION], items=None, group_no=group_no, refresh=refresh)


async def register_balance(client: WebSocketClient, group_no: str = '1', refresh: str = '1'):
    """잔고(04) 실시간 등록 – 종목코드 불필요"""
    await register(client, [TYPE_BALANCE], items=None, group_no=group_no, refresh=refresh)


async def register_stock_execution(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식체결(0B) 실시간 등록"""
    await register(client, [TYPE_STOCK_EXECUTION], items=items, group_no=group_no, refresh=refresh)


async def register_stock_best_quote(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식우선호가(0C) 실시간 등록"""
    await register(client, [TYPE_STOCK_BEST_QUOTE], items=items, group_no=group_no, refresh=refresh)


async def register_stock_orderbook(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식호가잔량(0D) 실시간 등록"""
    await register(client, [TYPE_STOCK_ORDERBOOK], items=items, group_no=group_no, refresh=refresh)


async def register_stock_momentum(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식기세(0A) 실시간 등록"""
    await register(client, [TYPE_STOCK_MOMENTUM], items=items, group_no=group_no, refresh=refresh)


async def register_stock_ah_quote(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식시간외호가(0E) 실시간 등록"""
    await register(client, [TYPE_STOCK_AH_QUOTE], items=items, group_no=group_no, refresh=refresh)


async def register_stock_broker(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식당일거래원(0F) 실시간 등록"""
    await register(client, [TYPE_STOCK_BROKER], items=items, group_no=group_no, refresh=refresh)


async def register_etf_nav(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """ETF NAV(0G) 실시간 등록"""
    await register(client, [TYPE_ETF_NAV], items=items, group_no=group_no, refresh=refresh)


async def register_stock_expected(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식예상체결(0H) 실시간 등록"""
    await register(client, [TYPE_STOCK_EXPECTED], items=items, group_no=group_no, refresh=refresh)


async def register_gold_intl(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """국제금환산가격(0I) 실시간 등록"""
    await register(client, [TYPE_GOLD_INTL], items=items, group_no=group_no, refresh=refresh)


async def register_sector_index(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """업종지수(0J) 실시간 등록"""
    await register(client, [TYPE_SECTOR_INDEX], items=items, group_no=group_no, refresh=refresh)


async def register_sector_change(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """업종등락(0U) 실시간 등록"""
    await register(client, [TYPE_SECTOR_CHANGE], items=items, group_no=group_no, refresh=refresh)


async def register_stock_info(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """주식종목정보(0g) 실시간 등록"""
    await register(client, [TYPE_STOCK_INFO], items=items, group_no=group_no, refresh=refresh)


async def register_elw_theory(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """ELW 이론가(0m) 실시간 등록"""
    await register(client, [TYPE_ELW_THEORY], items=items, group_no=group_no, refresh=refresh)


async def register_market_open(client: WebSocketClient, group_no: str = '1', refresh: str = '1'):
    """장시작시간(0s) 실시간 등록 – 종목코드 불필요"""
    await register(client, [TYPE_MARKET_OPEN], items=None, group_no=group_no, refresh=refresh)


async def register_elw_indicator(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """ELW 지표(0u) 실시간 등록"""
    await register(client, [TYPE_ELW_INDICATOR], items=items, group_no=group_no, refresh=refresh)


async def register_stock_program(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """종목프로그램매매(0w) 실시간 등록"""
    await register(client, [TYPE_STOCK_PROGRAM], items=items, group_no=group_no, refresh=refresh)


async def register_vi_trigger(client: WebSocketClient, items: list[str], group_no: str = '1', refresh: str = '1'):
    """VI발동/해제(1h) 실시간 등록"""
    await register(client, [TYPE_VI_TRIGGER], items=items, group_no=group_no, refresh=refresh)
