"""순위정보 API 요청 스펙 정의.

URL: /api/dostk/rkinfo
메뉴: 국내주식 > 순위정보
"""

RKINFO_API_SPECS = [
    # ───────────────────────────────────────────────────────
    # ka10023 – 거래량급증요청
    # ───────────────────────────────────────────────────────
    {
        'api_id': 'ka10023',
        'name': '거래량급증요청',
        'url': '/api/dostk/rkinfo',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '000:전체, 001:코스피, 101:코스닥',
            },
            {
                'element': 'sort_tp',
                'label': '정렬구분',
                'required': True,
                'description': '1:급증량, 2:급증률, 3:급감량, 4:급감률',
            },
            {
                'element': 'tm_tp',
                'label': '시간구분',
                'required': True,
                'description': '1:분, 2:전일',
            },
            {
                'element': 'trde_qty_tp',
                'label': '거래량구분',
                'required': True,
                'description': '5:5천주 이상, 10:1만주 이상, 50:5만주 이상, 100:10만주 이상, 200:20만주 이상, 300:30만주 이상, 500:50만주 이상, 1000:100만주 이상',
            },
            {
                'element': 'tm',
                'label': '분',
                'required': False,
                'description': '',
            },
            {
                'element': 'stk_cnd',
                'label': '주가조건',
                'required': False,
                'description': '0:전체, 2:1천원 이상, 3:5천원 이상, 4:1만원 이상, 5:5만원 이상, 6:10만원 이상',
            },
            {
                'element': 'pric_tp',
                'label': '가격구분',
                'required': False,
                'description': '0:전체, 1:1만원 미만, 2:1만원 이상~2만원 미만, 3:2만원 이상~3만원 미만, 4:5만원 이상~10만원 미만, 5:10만원 이상',
            },
            {
                'element': 'stex_tp',
                'label': '거래소구분',
                'required': True,
                'description': '1:KRX, 2:NXT, 3:통합',
            },
        ],
        'request_example': {
            'mrkt_tp': '000', 'sort_tp': '1', 'tm_tp': '2',
            'trde_qty_tp': '5', 'tm': '', 'stk_cnd': '0',
            'pric_tp': '0', 'stex_tp': '3',
        },
    },
    # ───────────────────────────────────────────────────────
    # ka10030 – 당일거래량상위요청
    # ───────────────────────────────────────────────────────
    {
        'api_id': 'ka10030',
        'name': '당일거래량상위요청',
        'url': '/api/dostk/rkinfo',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '000:전체, 001:코스피, 101:코스닥',
            },
            {
                'element': 'sort_tp',
                'label': '정렬구분',
                'required': True,
                'description': '1:거래량, 2:거래회전율, 3:거래대금',
            },
            {
                'element': 'mang_stk_incls',
                'label': '관리종목포함',
                'required': False,
                'description': '0:미포함, 1:포함',
            },
            {
                'element': 'crd_tp',
                'label': '신용구분',
                'required': False,
                'description': '0:전체, 1:신용융자, 2:신용대주',
            },
            {
                'element': 'trde_qty_tp',
                'label': '거래량구분',
                'required': False,
                'description': '0:전체, 5:5천주 이상, 10:1만주 이상, 50:5만주 이상, 100:10만주 이상',
            },
            {
                'element': 'pric_tp',
                'label': '가격구분',
                'required': False,
                'description': '0:전체, 1:1만원 미만, 2:1만원 이상~2만원 미만, 3:2만원 이상~3만원 미만, 4:5만원 이상~10만원 미만, 5:10만원 이상',
            },
            {
                'element': 'trde_prica_tp',
                'label': '거래대금구분',
                'required': False,
                'description': '0:전체, 1:1억 미만, 2:1억 이상, 3:10억 이상, 4:100억 이상',
            },
            {
                'element': 'mrkt_open_tp',
                'label': '장운영구분',
                'required': False,
                'description': '0:전체조회, 1:장중, 2:장전시간외, 3:장후시간외',
            },
            {
                'element': 'stex_tp',
                'label': '거래소구분',
                'required': True,
                'description': '1:KRX, 2:NXT, 3:통합',
            },
        ],
        'request_example': {
            'mrkt_tp': '000', 'sort_tp': '1', 'mang_stk_incls': '0',
            'crd_tp': '0', 'trde_qty_tp': '0', 'pric_tp': '0',
            'trde_prica_tp': '0', 'mrkt_open_tp': '0', 'stex_tp': '3',
        },
    },
    # ───────────────────────────────────────────────────────
    # ka10031 – 전일거래량상위요청
    # ───────────────────────────────────────────────────────
    {
        'api_id': 'ka10031',
        'name': '전일거래량상위요청',
        'url': '/api/dostk/rkinfo',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '000:전체, 001:코스피, 101:코스닥',
            },
            {
                'element': 'qry_tp',
                'label': '조회구분',
                'required': True,
                'description': '1:전일거래량 상위100종목, 2:전일거래대금 상위100종목',
            },
            {
                'element': 'rank_strt',
                'label': '순위시작',
                'required': False,
                'description': '',
            },
            {
                'element': 'rank_end',
                'label': '순위끝',
                'required': False,
                'description': '',
            },
            {
                'element': 'stex_tp',
                'label': '거래소구분',
                'required': True,
                'description': '1:KRX, 2:NXT, 3:통합',
            },
        ],
        'request_example': {
            'mrkt_tp': '000', 'qry_tp': '1',
            'rank_strt': '0', 'rank_end': '20', 'stex_tp': '3',
        },
    },
    # ───────────────────────────────────────────────────────
    # ka10032 – 거래대금상위요청
    # ───────────────────────────────────────────────────────
    {
        'api_id': 'ka10032',
        'name': '거래대금상위요청',
        'url': '/api/dostk/rkinfo',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '000:전체, 001:코스피, 101:코스닥',
            },
            {
                'element': 'mang_stk_incls',
                'label': '관리종목포함',
                'required': False,
                'description': '0:미포함, 1:포함',
            },
            {
                'element': 'stex_tp',
                'label': '거래소구분',
                'required': True,
                'description': '1:KRX, 2:NXT, 3:통합',
            },
        ],
        'request_example': {
            'mrkt_tp': '001', 'mang_stk_incls': '1', 'stex_tp': '3',
        },
    },
]
