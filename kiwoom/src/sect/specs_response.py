"""정적 업종 API 응답 스펙 정의.

URL: /api/dostk/sect
메뉴: 국내주식 > 업종
"""

SECT_RESPONSE_SPECS = {
    # ─────────────────────────────────────────────────────────
    # ka20001 – 업종현재가요청
    # ─────────────────────────────────────────────────────────
    'ka20001': [
        {'element': 'cur_prc',               'label': '현재가',           'type': 'String', 'description': ''},
        {'element': 'pred_pre_sig',           'label': '전일대비기호',     'type': 'String', 'description': '1:상한, 2:상승, 3:보합, 4:하한, 5:하락'},
        {'element': 'pred_pre',              'label': '전일대비',         'type': 'String', 'description': ''},
        {'element': 'flu_rt',                'label': '등락률',           'type': 'String', 'description': ''},
        {'element': 'trde_qty',              'label': '거래량',           'type': 'String', 'description': ''},
        {'element': 'trde_prica',            'label': '거래대금',         'type': 'String', 'description': ''},
        {'element': 'trde_frmatn_stk_num',   'label': '거래형성종목수',   'type': 'String', 'description': ''},
        {'element': 'trde_frmatn_rt',        'label': '거래형성비율',     'type': 'String', 'description': ''},
        {'element': 'open_pric',             'label': '시가',             'type': 'String', 'description': ''},
        {'element': 'high_pric',             'label': '고가',             'type': 'String', 'description': ''},
        {'element': 'low_pric',              'label': '저가',             'type': 'String', 'description': ''},
        {'element': 'upl',                   'label': '상한',             'type': 'String', 'description': ''},
        {'element': 'rising',                'label': '상승',             'type': 'String', 'description': ''},
        {'element': 'stdns',                 'label': '보합',             'type': 'String', 'description': ''},
        {'element': 'fall',                  'label': '하락',             'type': 'String', 'description': ''},
        {'element': 'lst',                   'label': '하한',             'type': 'String', 'description': ''},
        {'element': '52wk_hgst_pric',        'label': '52주최고가',       'type': 'String', 'description': ''},
        {'element': '52wk_hgst_pric_dt',     'label': '52주최고가일',     'type': 'String', 'description': ''},
        {'element': '52wk_hgst_pric_pre_rt', 'label': '52주최고가대비율', 'type': 'String', 'description': ''},
        {'element': '52wk_lwst_pric',        'label': '52주최저가',       'type': 'String', 'description': ''},
        {'element': '52wk_lwst_pric_dt',     'label': '52주최저가일',     'type': 'String', 'description': ''},
        {'element': '52wk_lwst_pric_pre_rt', 'label': '52주최저가대비율', 'type': 'String', 'description': ''},
        {'element': 'inds_cur_prc_tm',       'label': '업종현재가_시간별', 'type': 'LIST',   'description': ''},
        {'element': '- tm_n',                'label': '시간n',            'type': 'String', 'description': ''},
        {'element': '- cur_prc_n',           'label': '현재가n',          'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig_n',      'label': '전일대비기호n',    'type': 'String', 'description': ''},
        {'element': '- pred_pre_n',          'label': '전일대비n',        'type': 'String', 'description': ''},
        {'element': '- flu_rt_n',            'label': '등락률n',          'type': 'String', 'description': ''},
        {'element': '- trde_qty_n',          'label': '거래량n',          'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty_n',      'label': '누적거래량n',      'type': 'String', 'description': ''},
    ],

    # ─────────────────────────────────────────────────────────
    # ka20002 – 업종별주가요청
    # ─────────────────────────────────────────────────────────
    'ka20002': [
        {'element': 'inds_stkpc',       'label': '업종별주가',   'type': 'LIST',   'description': ''},
        {'element': '- stk_cd',         'label': '종목코드',     'type': 'String', 'description': ''},
        {'element': '- stk_nm',         'label': '종목명',       'type': 'String', 'description': ''},
        {'element': '- cur_prc',        'label': '현재가',       'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig',   'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre',       'label': '전일대비',     'type': 'String', 'description': ''},
        {'element': '- flu_rt',         'label': '등락률',       'type': 'String', 'description': ''},
        {'element': '- now_trde_qty',   'label': '현재거래량',   'type': 'String', 'description': ''},
        {'element': '- sel_bid',        'label': '매도호가',     'type': 'String', 'description': ''},
        {'element': '- buy_bid',        'label': '매수호가',     'type': 'String', 'description': ''},
        {'element': '- open_pric',      'label': '시가',         'type': 'String', 'description': ''},
        {'element': '- high_pric',      'label': '고가',         'type': 'String', 'description': ''},
        {'element': '- low_pric',       'label': '저가',         'type': 'String', 'description': ''},
    ],

    # ─────────────────────────────────────────────────────────
    # ka20003 – 전업종지수요청
    # ─────────────────────────────────────────────────────────
    'ka20003': [
        {'element': 'all_inds_idex',  'label': '전업종지수',   'type': 'LIST',   'description': ''},
        {'element': '- stk_cd',       'label': '업종코드',     'type': 'String', 'description': ''},
        {'element': '- stk_nm',       'label': '업종명',       'type': 'String', 'description': ''},
        {'element': '- cur_prc',      'label': '현재가',       'type': 'String', 'description': ''},
        {'element': '- pre_sig',      'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre',     'label': '전일대비',     'type': 'String', 'description': ''},
        {'element': '- flu_rt',       'label': '등락률',       'type': 'String', 'description': ''},
        {'element': '- trde_qty',     'label': '거래량',       'type': 'String', 'description': ''},
        {'element': '- wght',         'label': '비중',         'type': 'String', 'description': ''},
        {'element': '- trde_prica',   'label': '거래대금',     'type': 'String', 'description': ''},
        {'element': '- upl',          'label': '상한',         'type': 'String', 'description': ''},
        {'element': '- rising',       'label': '상승',         'type': 'String', 'description': ''},
        {'element': '- stdns',        'label': '보합',         'type': 'String', 'description': ''},
        {'element': '- fall',         'label': '하락',         'type': 'String', 'description': ''},
        {'element': '- lst',          'label': '하한',         'type': 'String', 'description': ''},
        {'element': '- flo_stk_num',  'label': '상장종목수',   'type': 'String', 'description': ''},
    ],

    # ─────────────────────────────────────────────────────────
    # ka20009 – 업종현재가일별요청
    # ─────────────────────────────────────────────────────────
    'ka20009': [
        {'element': 'cur_prc',               'label': '현재가',           'type': 'String', 'description': ''},
        {'element': 'pred_pre_sig',          'label': '전일대비기호',     'type': 'String', 'description': ''},
        {'element': 'pred_pre',              'label': '전일대비',         'type': 'String', 'description': ''},
        {'element': 'flu_rt',               'label': '등락률',           'type': 'String', 'description': ''},
        {'element': 'trde_qty',             'label': '거래량',           'type': 'String', 'description': ''},
        {'element': 'trde_prica',           'label': '거래대금',         'type': 'String', 'description': ''},
        {'element': 'trde_frmatn_stk_num',  'label': '거래형성종목수',   'type': 'String', 'description': ''},
        {'element': 'trde_frmatn_rt',       'label': '거래형성비율',     'type': 'String', 'description': ''},
        {'element': 'open_pric',            'label': '시가',             'type': 'String', 'description': ''},
        {'element': 'high_pric',            'label': '고가',             'type': 'String', 'description': ''},
        {'element': 'low_pric',             'label': '저가',             'type': 'String', 'description': ''},
        {'element': 'upl',                  'label': '상한',             'type': 'String', 'description': ''},
        {'element': 'rising',               'label': '상승',             'type': 'String', 'description': ''},
        {'element': 'stdns',                'label': '보합',             'type': 'String', 'description': ''},
        {'element': 'fall',                 'label': '하락',             'type': 'String', 'description': ''},
        {'element': 'lst',                  'label': '하한',             'type': 'String', 'description': ''},
        {'element': '52wk_hgst_pric',       'label': '52주최고가',       'type': 'String', 'description': ''},
        {'element': '52wk_hgst_pric_dt',    'label': '52주최고가일',     'type': 'String', 'description': ''},
        {'element': '52wk_hgst_pric_pre_rt','label': '52주최고가대비율', 'type': 'String', 'description': ''},
        {'element': '52wk_lwst_pric',       'label': '52주최저가',       'type': 'String', 'description': ''},
        {'element': '52wk_lwst_pric_dt',    'label': '52주최저가일',     'type': 'String', 'description': ''},
        {'element': '52wk_lwst_pric_pre_rt','label': '52주최저가대비율', 'type': 'String', 'description': ''},
        {'element': 'inds_cur_prc_daly_rept', 'label': '업종현재가일별', 'type': 'LIST',   'description': ''},
        {'element': '- dt_n',              'label': '일자n',            'type': 'String', 'description': ''},
        {'element': '- cur_prc_n',         'label': '현재가n',          'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig_n',    'label': '전일대비기호n',    'type': 'String', 'description': ''},
        {'element': '- pred_pre_n',        'label': '전일대비n',        'type': 'String', 'description': ''},
        {'element': '- flu_rt_n',          'label': '등락률n',          'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty_n',    'label': '누적거래량n',      'type': 'String', 'description': ''},
    ],
}
