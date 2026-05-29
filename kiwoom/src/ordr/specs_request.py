"""정적 주문 API 요청 스펙 정의.

URL: /api/dostk/ordr
메뉴: 국내주식 > 주문
"""

ORDR_API_SPECS = [
    {
        'api_id': 'kt10000',
        'name': '주식 매수주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'required': True, 'description': 'KRX,NXT,SOR'},
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': ''},
            {'element': 'ord_qty', 'label': '주문수량', 'required': True, 'description': ''},
            {'element': 'ord_uv', 'label': '주문단가', 'required': False, 'description': ''},
            {'element': 'trde_tp', 'label': '매매구분', 'required': True, 'description': '0:보통, 3:시장가, 5:조건부지정가, 81:장마감후시간외, 61:장시작전시간외, 62:시간외단일가, 6:최유리지정가, 7:최우선지정가, 10:보통(IOC), 13:시장가(IOC), 16:최유리(IOC), 20:보통(FOK), 23:시장가(FOK), 26:최유리(FOK), 28:스톱지정가, 29:중간가, 30:중간가(IOC), 31:중간가(FOK)'},
            {'element': 'cond_uv', 'label': '조건단가', 'required': False, 'description': ''},
        ],
        'request_example': {
            'dmst_stex_tp': 'KRX',
            'stk_cd': '005930',
            'ord_qty': '1',
            'ord_uv': '',
            'trde_tp': '3',
            'cond_uv': '',
        },
    },
    {
        'api_id': 'kt10001',
        'name': '주식 매도주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'required': True, 'description': 'KRX,NXT,SOR'},
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': ''},
            {'element': 'ord_qty', 'label': '주문수량', 'required': True, 'description': ''},
            {'element': 'ord_uv', 'label': '주문단가', 'required': False, 'description': ''},
            {'element': 'trde_tp', 'label': '매매구분', 'required': True, 'description': '0:보통, 3:시장가, 5:조건부지정가, 81:장마감후시간외, 61:장시작전시간외, 62:시간외단일가, 6:최유리지정가, 7:최우선지정가, 10:보통(IOC), 13:시장가(IOC), 16:최유리(IOC), 20:보통(FOK), 23:시장가(FOK), 26:최유리(FOK), 28:스톱지정가, 29:중간가, 30:중간가(IOC), 31:중간가(FOK)'},
            {'element': 'cond_uv', 'label': '조건단가', 'required': False, 'description': ''},
        ],
        'request_example': {
            'dmst_stex_tp': 'KRX',
            'stk_cd': '005930',
            'ord_qty': '1',
            'ord_uv': '',
            'trde_tp': '3',
            'cond_uv': '',
        },
    },
    {
        'api_id': 'kt10002',
        'name': '주식 정정주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'required': True, 'description': 'KRX,NXT,SOR'},
            {'element': 'orig_ord_no', 'label': '원주문번호', 'required': True, 'description': ''},
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': ''},
            {'element': 'mdfy_qty', 'label': '정정수량', 'required': True, 'description': ''},
            {'element': 'mdfy_uv', 'label': '정정단가', 'required': True, 'description': ''},
            {'element': 'mdfy_cond_uv', 'label': '정정조건단가', 'required': False, 'description': ''},
        ],
        'request_example': {
            'dmst_stex_tp': 'KRX',
            'orig_ord_no': '',
            'stk_cd': '005930',
            'mdfy_qty': '1',
            'mdfy_uv': '70000',
            'mdfy_cond_uv': '',
        },
    },
    {
        'api_id': 'kt10003',
        'name': '주식 취소주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'dmst_stex_tp', 'label': '국내거래소구분', 'required': True, 'description': 'KRX,NXT,SOR'},
            {'element': 'orig_ord_no', 'label': '원주문번호', 'required': True, 'description': ''},
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': ''},
            {'element': 'cncl_qty', 'label': '취소수량', 'required': True, 'description': "'0' 입력시 잔량 전부 취소"},
        ],
        'request_example': {
            'dmst_stex_tp': 'KRX',
            'orig_ord_no': '',
            'stk_cd': '005930',
            'cncl_qty': '0',
        },
    },
    {
        'api_id': 'kt50000',
        'name': '금현물 매수주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': 'M04020000 금 99.99_1kg, M04020100 미니금 99.99_100g'},
            {'element': 'ord_qty', 'label': '주문수량', 'required': True, 'description': ''},
            {'element': 'ord_uv', 'label': '주문단가', 'required': False, 'description': ''},
            {'element': 'trde_tp', 'label': '매매구분', 'required': True, 'description': '00:보통, 10:보통(IOC), 20:보통(FOK)'},
        ],
        'request_example': {
            'stk_cd': 'M04020000',
            'ord_qty': '1',
            'ord_uv': '',
            'trde_tp': '00',
        },
    },
    {
        'api_id': 'kt50001',
        'name': '금현물 매도주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': 'M04020000 금 99.99_1kg, M04020100 미니금 99.99_100g'},
            {'element': 'ord_qty', 'label': '주문수량', 'required': True, 'description': ''},
            {'element': 'ord_uv', 'label': '주문단가', 'required': False, 'description': ''},
            {'element': 'trde_tp', 'label': '매매구분', 'required': True, 'description': '00:보통, 10:보통(IOC), 20:보통(FOK)'},
        ],
        'request_example': {
            'stk_cd': 'M04020000',
            'ord_qty': '1',
            'ord_uv': '',
            'trde_tp': '00',
        },
    },
    {
        'api_id': 'kt50002',
        'name': '금현물 정정주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': 'M04020000 금 99.99_1kg, M04020100 미니금 99.99_100g'},
            {'element': 'orig_ord_no', 'label': '원주문번호', 'required': True, 'description': ''},
            {'element': 'mdfy_qty', 'label': '정정수량', 'required': True, 'description': ''},
            {'element': 'mdfy_uv', 'label': '정정단가', 'required': True, 'description': ''},
        ],
        'request_example': {
            'stk_cd': 'M04020000',
            'orig_ord_no': '',
            'mdfy_qty': '1',
            'mdfy_uv': '130000',
        },
    },
    {
        'api_id': 'kt50003',
        'name': '금현물 취소주문',
        'overview': '',
        'url': '/api/dostk/ordr',
        'fields': [
            {'element': 'orig_ord_no', 'label': '원주문번호', 'required': True, 'description': ''},
            {'element': 'stk_cd', 'label': '종목코드', 'required': True, 'description': 'M04020000 금 99.99_1kg, M04020100 미니금 99.99_100g'},
            {'element': 'cncl_qty', 'label': '취소수량', 'required': True, 'description': "'0' 입력시 잔량 전부 취소"},
        ],
        'request_example': {
            'orig_ord_no': '',
            'stk_cd': 'M04020000',
            'cncl_qty': '0',
        },
    },
]
