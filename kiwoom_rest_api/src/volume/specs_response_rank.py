"""순위정보 API 응답 스펙 정의.

URL: /api/dostk/rkinfo
메뉴: 국내주식 > 순위정보
"""

RKINFO_RESPONSE_SPECS = {
    # ───────────────────────────────────────────────────────
    # ka10023 – 거래량급증요청
    # ───────────────────────────────────────────────────────
    'ka10023': [
        {'element': 'trde_qty_sdnin',  'label': '거래량급증',   'type': 'LIST',   'description': ''},
        {'element': '- stk_cd',        'label': '종목코드',     'type': 'String', 'description': ''},
        {'element': '- stk_nm',        'label': '종목명',       'type': 'String', 'description': ''},
        {'element': '- mrkt_tp',       'label': '시장구분',     'type': 'String', 'description': ''},
        {'element': '- cur_prc',       'label': '현재가',       'type': 'String', 'description': ''},
        {'element': '- flu_rt',        'label': '등락률',       'type': 'String', 'description': ''},
        {'element': '- prev_trde_qty', 'label': '이전거래량',   'type': 'String', 'description': ''},
        {'element': '- now_trde_qty',  'label': '현재거래량',   'type': 'String', 'description': ''},
        {'element': '- sdnin_qty',     'label': '급증량',       'type': 'String', 'description': ''},
        {'element': '- sdnin_rt',      'label': '급증률',       'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10030 – 당일거래량상위요청
    # ───────────────────────────────────────────────────────
    'ka10030': [
        {'element': 'tdy_trde_qty_upper', 'label': '당일거래량상위', 'type': 'LIST',   'description': ''},
        {'element': '- stk_cd',           'label': '종목코드',       'type': 'String', 'description': ''},
        {'element': '- stk_nm',           'label': '종목명',         'type': 'String', 'description': ''},
        {'element': '- mrkt_tp',          'label': '시장구분',       'type': 'String', 'description': ''},
        {'element': '- cur_prc',          'label': '현재가',         'type': 'String', 'description': ''},
        {'element': '- flu_rt',           'label': '등락률',         'type': 'String', 'description': ''},
        {'element': '- trde_qty',         'label': '거래량',         'type': 'String', 'description': ''},
        {'element': '- pred_rt',          'label': '전일비',         'type': 'String', 'description': ''},
        {'element': '- trde_amt',         'label': '거래금액(백만)', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10031 – 전일거래량상위요청
    # ───────────────────────────────────────────────────────
    'ka10031': [
        {'element': 'pred_trde_qty_upper', 'label': '전일거래량상위', 'type': 'LIST',   'description': ''},
        {'element': '- stk_cd',            'label': '종목코드',       'type': 'String', 'description': ''},
        {'element': '- stk_nm',            'label': '종목명',         'type': 'String', 'description': ''},
        {'element': '- mrkt_tp',           'label': '시장구분',       'type': 'String', 'description': ''},
        {'element': '- cur_prc',           'label': '현재가',         'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig',      'label': '전일대비기호',   'type': 'String', 'description': ''},
        {'element': '- pred_pre',          'label': '전일대비',       'type': 'String', 'description': ''},
        {'element': '- trde_qty',          'label': '거래량',         'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10032 – 거래대금상위요청
    # ───────────────────────────────────────────────────────
    'ka10032': [
        {'element': 'trde_prica_upper', 'label': '거래대금상위',  'type': 'LIST',   'description': ''},
        {'element': '- now_rank',       'label': '현재순위',      'type': 'String', 'description': ''},
        {'element': '- pred_rank',      'label': '전일순위',      'type': 'String', 'description': ''},
        {'element': '- stk_cd',         'label': '종목코드',      'type': 'String', 'description': ''},
        {'element': '- stk_nm',         'label': '종목명',        'type': 'String', 'description': ''},
        {'element': '- mrkt_tp',        'label': '시장구분',      'type': 'String', 'description': ''},
        {'element': '- cur_prc',        'label': '현재가',        'type': 'String', 'description': ''},
        {'element': '- flu_rt',         'label': '등락률',        'type': 'String', 'description': ''},
        {'element': '- now_trde_qty',   'label': '현재거래량',    'type': 'String', 'description': ''},
        {'element': '- trde_prica',     'label': '거래대금(백만)', 'type': 'String', 'description': ''},
    ],
}
