"""
키움증권 조건검색 WebSocket API
URL: /api/dostk/websocket

포함 API:
  ka10171 – 조건검색 목록조회   (trnm=CNSRLST)
  ka10172 – 조건검색 요청 일반  (trnm=CNSRREQ, search_type='0')
  ka10173 – 조건검색 요청 실시간 (trnm=CNSRREQ, search_type='1')
  ka10174 – 조건검색 실시간 해제 (trnm=CNSRCLR)

주의:
  조건검색 목록조회(CNSRLST)를 먼저 호출한 뒤 실시간 조회를 사용해야 합니다.
  조건검색식은 영웅문4에서 생성할 수 있습니다.
"""

from .client import WebSocketClient


async def get_condition_list(client: WebSocketClient):
    """
    조건검색식 목록을 조회합니다. (ka10171, trnm=CNSRLST)

    서버 응답 예시::

        {
            'trnm': 'CNSRLST',
            'return_code': 0,
            'data': [['0', '조건1'], ['1', '조건2'], ...]
        }
    """
    await client.send_message({'trnm': 'CNSRLST'})


async def request_condition(
    client: WebSocketClient,
    seq: str,
    stex_tp: str = 'K',
    cont_yn: str = 'N',
    next_key: str = '',
):
    """
    조건검색 일반 요청 (ka10172, trnm=CNSRREQ, search_type='0')

    Parameters
    ----------
    client : WebSocketClient
        연결된 WebSocket 클라이언트
    seq : str
        조건검색식 일련번호 (CNSRLST 응답의 seq 값)
    stex_tp : str
        거래소 구분 ('K': KRX)
    cont_yn : str
        연속조회여부 ('Y': 연속, 'N': 최초)
    next_key : str
        연속조회키 (연속조회 시 이전 응답의 next_key 값)

    서버 응답 예시::

        {
            'trnm': 'CNSRREQ',
            'seq': '4',
            'return_code': 0,
            'data': [{'9001': 'A005930', '302': '삼성전자', '10': '000075000', ...}, ...]
        }

    Response Body 필드:
        - 9001: 종목코드
        - 302:  종목명
        - 10:   현재가
        - 25:   전일대비기호
        - 11:   전일대비
        - 12:   등락율
        - 13:   누적거래량
        - 16:   시가
        - 17:   고가
        - 18:   저가
    """
    await client.send_message({
        'trnm': 'CNSRREQ',
        'seq': seq,
        'search_type': '0',
        'stex_tp': stex_tp,
        'cont_yn': cont_yn,
        'next_key': next_key,
    })


async def request_condition_realtime(
    client: WebSocketClient,
    seq: str,
    stex_tp: str = 'K',
):
    """
    조건검색 실시간 요청 (ka10173, trnm=CNSRREQ, search_type='1')

    조건검색 목록조회(get_condition_list)를 먼저 호출한 뒤 사용해야 합니다.

    Parameters
    ----------
    client : WebSocketClient
        연결된 WebSocket 클라이언트
    seq : str
        조건검색식 일련번호
    stex_tp : str
        거래소 구분 ('K': KRX)

    서버 응답 (실시간 데이터)::

        {
            'trnm': 'REAL',
            'data': [{
                'type': '02',
                'name': '조건검색',
                'item': '005930',
                'values': {
                    '841': '4',         # 일련번호
                    '9001': '005930',   # 종목코드
                    '843': 'I',         # 삽입(I)/삭제(D) 구분
                    '20': '152028',     # 체결시간
                    '907': '2'          # 매도/수 구분
                }
            }]
        }
    """
    await client.send_message({
        'trnm': 'CNSRREQ',
        'seq': seq,
        'search_type': '1',
        'stex_tp': stex_tp,
    })


async def remove_condition_realtime(client: WebSocketClient, seq: str):
    """
    조건검색 실시간 해제 (ka10174, trnm=CNSRCLR)

    Parameters
    ----------
    client : WebSocketClient
        연결된 WebSocket 클라이언트
    seq : str
        해제할 조건검색식 일련번호

    서버 응답 예시::

        {
            'trnm': 'CNSRCLR',
            'seq': '1',
            'return_code': 0,
            'return_msg': ''
        }
    """
    await client.send_message({'trnm': 'CNSRCLR', 'seq': seq})
