"""정적 주문 API 응답 스펙 정의.

URL: /api/dostk/ordr
메뉴: 국내주식 > 주문
"""

ORDR_RESPONSE_SPECS = {
    'kt10000': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
        {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'type': 'String', 'description': ''},
    ],
    'kt10001': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
        {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'type': 'String', 'description': ''},
    ],
    'kt10002': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
        {'element': 'base_orig_ord_no', 'label': '모주문번호', 'type': 'String', 'description': ''},
        {'element': 'mdfy_qty', 'label': '정정수량', 'type': 'String', 'description': ''},
        {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'type': 'String', 'description': ''},
    ],
    'kt10003': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
        {'element': 'base_orig_ord_no', 'label': '모주문번호', 'type': 'String', 'description': ''},
        {'element': 'cncl_qty', 'label': '취소수량', 'type': 'String', 'description': ''},
    ],
    'kt50000': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
    ],
    'kt50001': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
    ],
    'kt50002': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
        {'element': 'base_orig_ord_no', 'label': '모주문번호', 'type': 'String', 'description': ''},
        {'element': 'mdfy_qty', 'label': '정정수량', 'type': 'String', 'description': ''},
    ],
    'kt50003': [
        {'element': 'ord_no', 'label': '주문번호', 'type': 'String', 'description': ''},
        {'element': 'base_orig_ord_no', 'label': '모주문번호', 'type': 'String', 'description': ''},
        {'element': 'cncl_qty', 'label': '취소수량', 'type': 'String', 'description': ''},
    ],
}
