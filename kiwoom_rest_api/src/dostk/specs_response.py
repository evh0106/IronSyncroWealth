"""정적 종목정보 API 응답 스펙 정의.

URL: /api/dostk/stkinfo
메뉴: 국내주식 > 종목정보
"""

STKINFO_RESPONSE_SPECS = {
    # ───────────────────────────────────────────────────────
    # ka00198 – 실시간종목조회순위
    # ───────────────────────────────────────────────────────
    'ka00198': [
        {'element': 'item_inq_rank', 'label': '실시간종목조회순위', 'type': 'LIST', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- bigd_rank', 'label': '빅데이터 순위', 'type': 'String', 'description': ''},
        {'element': '- rank_chg', 'label': '순위 등락', 'type': 'String', 'description': ''},
        {'element': '- rank_chg_sign', 'label': '순위 등락 부호', 'type': 'String', 'description': ''},
        {'element': '- past_curr_prc', 'label': '과거 현재가', 'type': 'String', 'description': ''},
        {'element': '- base_comp_sign', 'label': '기준가 대비 부호', 'type': 'String', 'description': ''},
        {'element': '- base_comp_chgr', 'label': '기준가 대비 등락율', 'type': 'String', 'description': ''},
        {'element': '- prev_base_sign', 'label': '직전 기준 대비 부호', 'type': 'String', 'description': ''},
        {'element': '- prev_base_chgr', 'label': '직전 기준 대비 등락율', 'type': 'String', 'description': ''},
        {'element': '- dt', 'label': '일자', 'type': 'String', 'description': ''},
        {'element': '- tm', 'label': '시간', 'type': 'String', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10001 – 주식기본정보요청
    # ───────────────────────────────────────────────────────
    'ka10001': [
        {'element': 'stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': 'stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': 'setl_mm', 'label': '결산월', 'type': 'String', 'description': ''},
        {'element': 'fav', 'label': '액면가', 'type': 'String', 'description': ''},
        {'element': 'cap', 'label': '자본금', 'type': 'String', 'description': ''},
        {'element': 'flo_stk', 'label': '상장주식', 'type': 'String', 'description': ''},
        {'element': 'crd_rt', 'label': '신용비율', 'type': 'String', 'description': ''},
        {'element': 'oyr_hgst', 'label': '연중최고', 'type': 'String', 'description': ''},
        {'element': 'oyr_lwst', 'label': '연중최저', 'type': 'String', 'description': ''},
        {'element': 'mac', 'label': '시가총액', 'type': 'String', 'description': ''},
        {'element': 'mac_wght', 'label': '시가총액비중', 'type': 'String', 'description': ''},
        {'element': 'for_exh_rt', 'label': '외인소진률', 'type': 'String', 'description': ''},
        {'element': 'repl_pric', 'label': '대용가', 'type': 'String', 'description': ''},
        {'element': 'per', 'label': 'PER', 'type': 'String', 'description': '[ 주의 ] PER, ROE 값들은 외부벤더사에서 제공되는 데이터이며 일주일에 한번 또는 실적발표 시즌에 업데이트 됨'},
        {'element': 'eps', 'label': 'EPS', 'type': 'String', 'description': ''},
        {'element': 'roe', 'label': 'ROE', 'type': 'String', 'description': '[ 주의 ]  PER, ROE 값들은 외부벤더사에서 제공되는 데이터이며 일주일에 한번 또는 실적발표 시즌에 업데이트 됨'},
        {'element': 'pbr', 'label': 'PBR', 'type': 'String', 'description': ''},
        {'element': 'ev', 'label': 'EV', 'type': 'String', 'description': ''},
        {'element': 'bps', 'label': 'BPS', 'type': 'String', 'description': ''},
        {'element': 'sale_amt', 'label': '매출액', 'type': 'String', 'description': ''},
        {'element': 'bus_pro', 'label': '영업이익', 'type': 'String', 'description': ''},
        {'element': 'cup_nga', 'label': '당기순이익', 'type': 'String', 'description': ''},
        {'element': '250hgst', 'label': '250최고', 'type': 'String', 'description': ''},
        {'element': '250lwst', 'label': '250최저', 'type': 'String', 'description': ''},
        {'element': 'open_pric', 'label': '시가', 'type': 'String', 'description': ''},
        {'element': 'high_pric', 'label': '고가', 'type': 'String', 'description': ''},
        {'element': 'low_pric', 'label': '저가', 'type': 'String', 'description': ''},
        {'element': 'upl_pric', 'label': '상한가', 'type': 'String', 'description': ''},
        {'element': 'lst_pric', 'label': '하한가', 'type': 'String', 'description': ''},
        {'element': 'base_pric', 'label': '기준가', 'type': 'String', 'description': ''},
        {'element': 'exp_cntr_pric', 'label': '예상체결가', 'type': 'String', 'description': ''},
        {'element': 'exp_cntr_qty', 'label': '예상체결수량', 'type': 'String', 'description': ''},
        {'element': '250hgst_pric_dt', 'label': '250최고가일', 'type': 'String', 'description': ''},
        {'element': '250hgst_pric_pre_rt', 'label': '250최고가대비율', 'type': 'String', 'description': ''},
        {'element': '250lwst_pric_dt', 'label': '250최저가일', 'type': 'String', 'description': ''},
        {'element': '250lwst_pric_pre_rt', 'label': '250최저가대비율', 'type': 'String', 'description': ''},
        {'element': 'cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': 'pre_sig', 'label': '대비기호', 'type': 'String', 'description': ''},
        {'element': 'pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': 'flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
        {'element': 'trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': 'trde_pre', 'label': '거래대비', 'type': 'String', 'description': ''},
        {'element': 'fav_unit', 'label': '액면가단위', 'type': 'String', 'description': ''},
        {'element': 'dstr_stk', 'label': '유통주식', 'type': 'String', 'description': ''},
        {'element': 'dstr_rt', 'label': '유통비율', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10002 – 주식거래원요청
    # ───────────────────────────────────────────────────────
    'ka10002': [
        {'element': 'stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': 'stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': 'cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': 'flu_smbol', 'label': '등락부호', 'type': 'String', 'description': ''},
        {'element': 'base_pric', 'label': '기준가', 'type': 'String', 'description': ''},
        {'element': 'pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': 'flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_nm_1', 'label': '매도거래원명1', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_1', 'label': '매도거래원1', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_qty_1', 'label': '매도거래량1', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_nm_1', 'label': '매수거래원명1', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_1', 'label': '매수거래원1', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_qty_1', 'label': '매수거래량1', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_nm_2', 'label': '매도거래원명2', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_2', 'label': '매도거래원2', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_qty_2', 'label': '매도거래량2', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_nm_2', 'label': '매수거래원명2', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_2', 'label': '매수거래원2', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_qty_2', 'label': '매수거래량2', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_nm_3', 'label': '매도거래원명3', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_3', 'label': '매도거래원3', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_qty_3', 'label': '매도거래량3', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_nm_3', 'label': '매수거래원명3', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_3', 'label': '매수거래원3', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_qty_3', 'label': '매수거래량3', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_nm_4', 'label': '매도거래원명4', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_4', 'label': '매도거래원4', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_qty_4', 'label': '매도거래량4', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_nm_4', 'label': '매수거래원명4', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_4', 'label': '매수거래원4', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_qty_4', 'label': '매수거래량4', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_nm_5', 'label': '매도거래원명5', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_ori_5', 'label': '매도거래원5', 'type': 'String', 'description': ''},
        {'element': 'sel_trde_qty_5', 'label': '매도거래량5', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_nm_5', 'label': '매수거래원명5', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_ori_5', 'label': '매수거래원5', 'type': 'String', 'description': ''},
        {'element': 'buy_trde_qty_5', 'label': '매수거래량5', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10003 – 체결정보요청
    # ───────────────────────────────────────────────────────
    'ka10003': [
        {'element': 'cntr_infr', 'label': '체결정보', 'type': 'LIST', 'description': ''},
        {'element': '- tm', 'label': '시간', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- pre_rt', 'label': '대비율', 'type': 'String', 'description': ''},
        {'element': '- pri_sel_bid_unit', 'label': '우선매도호가단위', 'type': 'String', 'description': ''},
        {'element': '- pri_buy_bid_unit', 'label': '우선매수호가단위', 'type': 'String', 'description': ''},
        {'element': '- cntr_trde_qty', 'label': '체결거래량', 'type': 'String', 'description': ''},
        {'element': '- sign', 'label': 'sign', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty', 'label': '누적거래량', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_prica', 'label': '누적거래대금', 'type': 'String', 'description': ''},
        {'element': '- cntr_str', 'label': '체결강도', 'type': 'String', 'description': ''},
        {'element': '- stex_tp', 'label': '거래소구분', 'type': 'String', 'description': 'KRX , NXT , 통합'},
    ],

    # ───────────────────────────────────────────────────────
    # ka10013 – 신용매매동향요청
    # ───────────────────────────────────────────────────────
    'ka10013': [
        {'element': 'crd_trde_trend', 'label': '신용매매동향', 'type': 'LIST', 'description': ''},
        {'element': '- dt', 'label': '일자', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- new', 'label': '신규', 'type': 'String', 'description': ''},
        {'element': '- rpya', 'label': '상환', 'type': 'String', 'description': ''},
        {'element': '- remn', 'label': '잔고', 'type': 'String', 'description': ''},
        {'element': '- amt', 'label': '금액', 'type': 'String', 'description': ''},
        {'element': '- pre', 'label': '대비', 'type': 'String', 'description': ''},
        {'element': '- shr_rt', 'label': '공여율', 'type': 'String', 'description': ''},
        {'element': '- remn_rt', 'label': '잔고율', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10015 – 일별거래상세요청
    # ───────────────────────────────────────────────────────
    'ka10015': [
        {'element': 'daly_trde_dtl', 'label': '일별거래상세', 'type': 'LIST', 'description': ''},
        {'element': '- dt', 'label': '일자', 'type': 'String', 'description': ''},
        {'element': '- close_pric', 'label': '종가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- trde_prica', 'label': '거래대금', 'type': 'String', 'description': ''},
        {'element': '- bf_mkrt_trde_qty', 'label': '장전거래량', 'type': 'String', 'description': ''},
        {'element': '- bf_mkrt_trde_wght', 'label': '장전거래비중', 'type': 'String', 'description': ''},
        {'element': '- opmr_trde_qty', 'label': '장중거래량', 'type': 'String', 'description': ''},
        {'element': '- opmr_trde_wght', 'label': '장중거래비중', 'type': 'String', 'description': ''},
        {'element': '- af_mkrt_trde_qty', 'label': '장후거래량', 'type': 'String', 'description': ''},
        {'element': '- af_mkrt_trde_wght', 'label': '장후거래비중', 'type': 'String', 'description': ''},
        {'element': '- tot_3', 'label': '합계3', 'type': 'String', 'description': ''},
        {'element': '- prid_trde_qty', 'label': '기간중거래량', 'type': 'String', 'description': ''},
        {'element': '- cntr_str', 'label': '체결강도', 'type': 'String', 'description': ''},
        {'element': '- for_poss', 'label': '외인보유', 'type': 'String', 'description': ''},
        {'element': '- for_wght', 'label': '외인비중', 'type': 'String', 'description': ''},
        {'element': '- for_netprps', 'label': '외인순매수', 'type': 'String', 'description': ''},
        {'element': '- orgn_netprps', 'label': '기관순매수', 'type': 'String', 'description': ''},
        {'element': '- ind_netprps', 'label': '개인순매수', 'type': 'String', 'description': ''},
        {'element': '- frgn', 'label': '외국계', 'type': 'String', 'description': ''},
        {'element': '- crd_remn_rt', 'label': '신용잔고율', 'type': 'String', 'description': ''},
        {'element': '- prm', 'label': '프로그램', 'type': 'String', 'description': ''},
        {'element': '- bf_mkrt_trde_prica', 'label': '장전거래대금', 'type': 'String', 'description': ''},
        {'element': '- bf_mkrt_trde_prica_wght', 'label': '장전거래대금비중', 'type': 'String', 'description': ''},
        {'element': '- opmr_trde_prica', 'label': '장중거래대금', 'type': 'String', 'description': ''},
        {'element': '- opmr_trde_prica_wght', 'label': '장중거래대금비중', 'type': 'String', 'description': ''},
        {'element': '- af_mkrt_trde_prica', 'label': '장후거래대금', 'type': 'String', 'description': ''},
        {'element': '- af_mkrt_trde_prica_wght', 'label': '장후거래대금비중', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10016 – 신고저가요청
    # ───────────────────────────────────────────────────────
    'ka10016': [
        {'element': 'ntl_pric', 'label': '신고저가', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- pred_trde_qty_pre_rt', 'label': '전일거래량대비율', 'type': 'String', 'description': ''},
        {'element': '- sel_bid', 'label': '매도호가', 'type': 'String', 'description': ''},
        {'element': '- buy_bid', 'label': '매수호가', 'type': 'String', 'description': ''},
        {'element': '- high_pric', 'label': '고가', 'type': 'String', 'description': ''},
        {'element': '- low_pric', 'label': '저가', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10017 – 상하한가요청
    # ───────────────────────────────────────────────────────
    'ka10017': [
        {'element': 'updown_pric', 'label': '상하한가', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_infr', 'label': '종목정보', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- pred_trde_qty', 'label': '전일거래량', 'type': 'String', 'description': ''},
        {'element': '- sel_req', 'label': '매도잔량', 'type': 'String', 'description': ''},
        {'element': '- sel_bid', 'label': '매도호가', 'type': 'String', 'description': ''},
        {'element': '- buy_bid', 'label': '매수호가', 'type': 'String', 'description': ''},
        {'element': '- buy_req', 'label': '매수잔량', 'type': 'String', 'description': ''},
        {'element': '- cnt', 'label': '횟수', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10018 – 고저가근접요청
    # ───────────────────────────────────────────────────────
    'ka10018': [
        {'element': 'high_low_pric_alacc', 'label': '고저가근접', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- sel_bid', 'label': '매도호가', 'type': 'String', 'description': ''},
        {'element': '- buy_bid', 'label': '매수호가', 'type': 'String', 'description': ''},
        {'element': '- tdy_high_pric', 'label': '당일고가', 'type': 'String', 'description': ''},
        {'element': '- tdy_low_pric', 'label': '당일저가', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10019 – 가격급등락요청
    # ───────────────────────────────────────────────────────
    'ka10019': [
        {'element': 'pric_jmpflu', 'label': '가격급등락', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_cls', 'label': '종목분류', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- base_pric', 'label': '기준가', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- base_pre', 'label': '기준대비', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- jmp_rt', 'label': '급등률', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10024 – 거래량갱신요청
    # ───────────────────────────────────────────────────────
    'ka10024': [
        {'element': 'trde_qty_updt', 'label': '거래량갱신', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- prev_trde_qty', 'label': '이전거래량', 'type': 'String', 'description': ''},
        {'element': '- now_trde_qty', 'label': '현재거래량', 'type': 'String', 'description': ''},
        {'element': '- sel_bid', 'label': '매도호가', 'type': 'String', 'description': ''},
        {'element': '- buy_bid', 'label': '매수호가', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10025 – 매물대집중요청
    # ───────────────────────────────────────────────────────
    'ka10025': [
        {'element': 'prps_cnctr', 'label': '매물대집중', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- now_trde_qty', 'label': '현재거래량', 'type': 'String', 'description': ''},
        {'element': '- pric_strt', 'label': '가격대시작', 'type': 'String', 'description': ''},
        {'element': '- pric_end', 'label': '가격대끝', 'type': 'String', 'description': ''},
        {'element': '- prps_qty', 'label': '매물량', 'type': 'String', 'description': ''},
        {'element': '- prps_rt', 'label': '매물비', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10026 – 고저PER요청
    # ───────────────────────────────────────────────────────
    'ka10026': [
        {'element': 'high_low_per', 'label': '고저PER', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- per', 'label': 'PER', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- now_trde_qty', 'label': '현재거래량', 'type': 'String', 'description': ''},
        {'element': '- sel_bid', 'label': '매도호가', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10028 – 시가대비등락률요청
    # ───────────────────────────────────────────────────────
    'ka10028': [
        {'element': 'open_pric_pre_flu_rt', 'label': '시가대비등락률', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락률', 'type': 'String', 'description': ''},
        {'element': '- open_pric', 'label': '시가', 'type': 'String', 'description': ''},
        {'element': '- high_pric', 'label': '고가', 'type': 'String', 'description': ''},
        {'element': '- low_pric', 'label': '저가', 'type': 'String', 'description': ''},
        {'element': '- open_pric_pre', 'label': '시가대비', 'type': 'String', 'description': ''},
        {'element': '- now_trde_qty', 'label': '현재거래량', 'type': 'String', 'description': ''},
        {'element': '- cntr_str', 'label': '체결강도', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10043 – 거래원매물대분석요청
    # ───────────────────────────────────────────────────────
    'ka10043': [
        {'element': 'trde_ori_prps_anly', 'label': '거래원매물대분석', 'type': 'LIST', 'description': ''},
        {'element': '- dt', 'label': '일자', 'type': 'String', 'description': ''},
        {'element': '- close_pric', 'label': '종가', 'type': 'String', 'description': ''},
        {'element': '- pre_sig', 'label': '대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- sel_qty', 'label': '매도량', 'type': 'String', 'description': ''},
        {'element': '- buy_qty', 'label': '매수량', 'type': 'String', 'description': ''},
        {'element': '- netprps_qty', 'label': '순매수수량', 'type': 'String', 'description': ''},
        {'element': '- trde_qty_sum', 'label': '거래량합', 'type': 'String', 'description': ''},
        {'element': '- trde_wght', 'label': '거래비중', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10052 – 거래원순간거래량요청
    # ───────────────────────────────────────────────────────
    'ka10052': [
        {'element': 'trde_ori_mont_trde_qty', 'label': '거래원순간거래량', 'type': 'LIST', 'description': ''},
        {'element': '- tm', 'label': '시간', 'type': 'String', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- trde_ori_nm', 'label': '거래원명', 'type': 'String', 'description': ''},
        {'element': '- tp', 'label': '구분', 'type': 'String', 'description': ''},
        {'element': '- mont_trde_qty', 'label': '순간거래량', 'type': 'String', 'description': ''},
        {'element': '- acc_netprps', 'label': '누적순매수', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10054 – 변동성완화장치발동종목요청
    # ───────────────────────────────────────────────────────
    'ka10054': [
        {'element': 'motn_stk', 'label': '발동종목', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty', 'label': '누적거래량', 'type': 'String', 'description': ''},
        {'element': '- motn_pric', 'label': '발동가격', 'type': 'String', 'description': ''},
        {'element': '- dynm_dispty_rt', 'label': '동적괴리율', 'type': 'String', 'description': ''},
        {'element': '- trde_cntr_proc_time', 'label': '매매체결처리시각', 'type': 'String', 'description': ''},
        {'element': '- virelis_time', 'label': 'VI해제시각', 'type': 'String', 'description': ''},
        {'element': '- viaplc_tp', 'label': 'VI적용구분', 'type': 'String', 'description': ''},
        {'element': '- dynm_stdpc', 'label': '동적기준가격', 'type': 'String', 'description': ''},
        {'element': '- static_stdpc', 'label': '정적기준가격', 'type': 'String', 'description': ''},
        {'element': '- static_dispty_rt', 'label': '정적괴리율', 'type': 'String', 'description': ''},
        {'element': '- open_pric_pre_flu_rt', 'label': '시가대비등락률', 'type': 'String', 'description': ''},
        {'element': '- vimotn_cnt', 'label': 'VI발동횟수', 'type': 'String', 'description': ''},
        {'element': '- stex_tp', 'label': '거래소구분', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10055 – 당일전일체결량요청
    # ───────────────────────────────────────────────────────
    'ka10055': [
        {'element': 'tdy_pred_cntr_qty', 'label': '당일전일체결량', 'type': 'LIST', 'description': ''},
        {'element': '- cntr_tm', 'label': '체결시간', 'type': 'String', 'description': ''},
        {'element': '- cntr_pric', 'label': '체결가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
        {'element': '- cntr_qty', 'label': '체결량', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty', 'label': '누적거래량', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_prica', 'label': '누적거래대금', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10058 – 투자자별일별매매종목요청
    # ───────────────────────────────────────────────────────
    'ka10058': [
        {'element': 'invsr_daly_trde_stk', 'label': '투자자별일별매매종목', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- netslmt_qty', 'label': '순매도수량', 'type': 'String', 'description': ''},
        {'element': '- netslmt_amt', 'label': '순매도금액', 'type': 'String', 'description': ''},
        {'element': '- prsm_avg_pric', 'label': '추정평균가', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pre_sig', 'label': '대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- avg_pric_pre', 'label': '평균가대비', 'type': 'String', 'description': ''},
        {'element': '- pre_rt', 'label': '대비율', 'type': 'String', 'description': ''},
        {'element': '- dt_trde_qty', 'label': '기간거래량', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10059 – 종목별투자자기관별요청
    # ───────────────────────────────────────────────────────
    'ka10059': [
        {'element': 'stk_invsr_orgn', 'label': '종목별투자자기관별', 'type': 'LIST', 'description': ''},
        {'element': '- dt', 'label': '일자', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pre_sig', 'label': '대비기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락율', 'type': 'String', 'description': '우측 2자리 소수점자리수'},
        {'element': '- acc_trde_qty', 'label': '누적거래량', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_prica', 'label': '누적거래대금', 'type': 'String', 'description': ''},
        {'element': '- ind_invsr', 'label': '개인투자자', 'type': 'String', 'description': ''},
        {'element': '- frgnr_invsr', 'label': '외국인투자자', 'type': 'String', 'description': ''},
        {'element': '- orgn', 'label': '기관계', 'type': 'String', 'description': ''},
        {'element': '- fnnc_invt', 'label': '금융투자', 'type': 'String', 'description': ''},
        {'element': '- insrnc', 'label': '보험', 'type': 'String', 'description': ''},
        {'element': '- invtrt', 'label': '투신', 'type': 'String', 'description': ''},
        {'element': '- etc_fnnc', 'label': '기타금융', 'type': 'String', 'description': ''},
        {'element': '- bank', 'label': '은행', 'type': 'String', 'description': ''},
        {'element': '- penfnd_etc', 'label': '연기금등', 'type': 'String', 'description': ''},
        {'element': '- samo_fund', 'label': '사모펀드', 'type': 'String', 'description': ''},
        {'element': '- natn', 'label': '국가', 'type': 'String', 'description': ''},
        {'element': '- etc_corp', 'label': '기타법인', 'type': 'String', 'description': ''},
        {'element': '- natfor', 'label': '내외국인', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10061 – 종목별투자자기관별합계요청
    # ───────────────────────────────────────────────────────
    'ka10061': [
        {'element': 'stk_invsr_orgn_tot', 'label': '종목별투자자기관별합계', 'type': 'LIST', 'description': ''},
        {'element': '- ind_invsr', 'label': '개인투자자', 'type': 'String', 'description': ''},
        {'element': '- frgnr_invsr', 'label': '외국인투자자', 'type': 'String', 'description': ''},
        {'element': '- orgn', 'label': '기관계', 'type': 'String', 'description': ''},
        {'element': '- fnnc_invt', 'label': '금융투자', 'type': 'String', 'description': ''},
        {'element': '- insrnc', 'label': '보험', 'type': 'String', 'description': ''},
        {'element': '- invtrt', 'label': '투신', 'type': 'String', 'description': ''},
        {'element': '- etc_fnnc', 'label': '기타금융', 'type': 'String', 'description': ''},
        {'element': '- bank', 'label': '은행', 'type': 'String', 'description': ''},
        {'element': '- penfnd_etc', 'label': '연기금등', 'type': 'String', 'description': ''},
        {'element': '- samo_fund', 'label': '사모펀드', 'type': 'String', 'description': ''},
        {'element': '- natn', 'label': '국가', 'type': 'String', 'description': ''},
        {'element': '- etc_corp', 'label': '기타법인', 'type': 'String', 'description': ''},
        {'element': '- natfor', 'label': '내외국인', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10084 – 당일전일체결요청
    # ───────────────────────────────────────────────────────
    'ka10084': [
        {'element': 'tdy_pred_cntr', 'label': '당일전일체결', 'type': 'LIST', 'description': ''},
        {'element': '- tm', 'label': '시간', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- pre_rt', 'label': '대비율', 'type': 'String', 'description': ''},
        {'element': '- pri_sel_bid_unit', 'label': '우선매도호가단위', 'type': 'String', 'description': ''},
        {'element': '- pri_buy_bid_unit', 'label': '우선매수호가단위', 'type': 'String', 'description': ''},
        {'element': '- cntr_trde_qty', 'label': '체결거래량', 'type': 'String', 'description': ''},
        {'element': '- sign', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty', 'label': '누적거래량', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_prica', 'label': '누적거래대금', 'type': 'String', 'description': ''},
        {'element': '- cntr_str', 'label': '체결강도', 'type': 'String', 'description': ''},
        {'element': '- stex_tp', 'label': '거래소구분', 'type': 'String', 'description': 'KRX , NXT , 통합'},
    ],

    # ───────────────────────────────────────────────────────
    # ka10095 – 관심종목정보요청
    # ───────────────────────────────────────────────────────
    'ka10095': [
        {'element': 'atn_stk_infr', 'label': '관심종목정보', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- base_pric', 'label': '기준가', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- pred_pre_sig', 'label': '전일대비기호', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
        {'element': '- trde_qty', 'label': '거래량', 'type': 'String', 'description': ''},
        {'element': '- trde_prica', 'label': '거래대금', 'type': 'String', 'description': ''},
        {'element': '- cntr_qty', 'label': '체결량', 'type': 'String', 'description': ''},
        {'element': '- cntr_str', 'label': '체결강도', 'type': 'String', 'description': ''},
        {'element': '- pred_trde_qty_pre', 'label': '전일거래량대비', 'type': 'String', 'description': ''},
        {'element': '- sel_bid', 'label': '매도호가', 'type': 'String', 'description': ''},
        {'element': '- buy_bid', 'label': '매수호가', 'type': 'String', 'description': ''},
        {'element': '- sel_1th_bid', 'label': '매도1차호가', 'type': 'String', 'description': ''},
        {'element': '- sel_2th_bid', 'label': '매도2차호가', 'type': 'String', 'description': ''},
        {'element': '- sel_3th_bid', 'label': '매도3차호가', 'type': 'String', 'description': ''},
        {'element': '- sel_4th_bid', 'label': '매도4차호가', 'type': 'String', 'description': ''},
        {'element': '- sel_5th_bid', 'label': '매도5차호가', 'type': 'String', 'description': ''},
        {'element': '- buy_1th_bid', 'label': '매수1차호가', 'type': 'String', 'description': ''},
        {'element': '- buy_2th_bid', 'label': '매수2차호가', 'type': 'String', 'description': ''},
        {'element': '- buy_3th_bid', 'label': '매수3차호가', 'type': 'String', 'description': ''},
        {'element': '- buy_4th_bid', 'label': '매수4차호가', 'type': 'String', 'description': ''},
        {'element': '- buy_5th_bid', 'label': '매수5차호가', 'type': 'String', 'description': ''},
        {'element': '- upl_pric', 'label': '상한가', 'type': 'String', 'description': ''},
        {'element': '- lst_pric', 'label': '하한가', 'type': 'String', 'description': ''},
        {'element': '- open_pric', 'label': '시가', 'type': 'String', 'description': ''},
        {'element': '- high_pric', 'label': '고가', 'type': 'String', 'description': ''},
        {'element': '- low_pric', 'label': '저가', 'type': 'String', 'description': ''},
        {'element': '- close_pric', 'label': '종가', 'type': 'String', 'description': ''},
        {'element': '- cntr_tm', 'label': '체결시간', 'type': 'String', 'description': ''},
        {'element': '- exp_cntr_pric', 'label': '예상체결가', 'type': 'String', 'description': ''},
        {'element': '- exp_cntr_qty', 'label': '예상체결량', 'type': 'String', 'description': ''},
        {'element': '- cap', 'label': '자본금', 'type': 'String', 'description': ''},
        {'element': '- fav', 'label': '액면가', 'type': 'String', 'description': ''},
        {'element': '- mac', 'label': '시가총액', 'type': 'String', 'description': ''},
        {'element': '- stkcnt', 'label': '주식수', 'type': 'String', 'description': ''},
        {'element': '- bid_tm', 'label': '호가시간', 'type': 'String', 'description': ''},
        {'element': '- dt', 'label': '일자', 'type': 'String', 'description': ''},
        {'element': '- pri_sel_req', 'label': '우선매도잔량', 'type': 'String', 'description': ''},
        {'element': '- pri_buy_req', 'label': '우선매수잔량', 'type': 'String', 'description': ''},
        {'element': '- pri_sel_cnt', 'label': '우선매도건수', 'type': 'String', 'description': ''},
        {'element': '- pri_buy_cnt', 'label': '우선매수건수', 'type': 'String', 'description': ''},
        {'element': '- tot_sel_req', 'label': '총매도잔량', 'type': 'String', 'description': ''},
        {'element': '- tot_buy_req', 'label': '총매수잔량', 'type': 'String', 'description': ''},
        {'element': '- tot_sel_cnt', 'label': '총매도건수', 'type': 'String', 'description': ''},
        {'element': '- tot_buy_cnt', 'label': '총매수건수', 'type': 'String', 'description': ''},
        {'element': '- prty', 'label': '패리티', 'type': 'String', 'description': ''},
        {'element': '- gear', 'label': '기어링', 'type': 'String', 'description': ''},
        {'element': '- pl_qutr', 'label': '손익분기', 'type': 'String', 'description': ''},
        {'element': '- cap_support', 'label': '자본지지', 'type': 'String', 'description': ''},
        {'element': '- elwexec_pric', 'label': 'ELW행사가', 'type': 'String', 'description': ''},
        {'element': '- cnvt_rt', 'label': '전환비율', 'type': 'String', 'description': ''},
        {'element': '- elwexpr_dt', 'label': 'ELW만기일', 'type': 'String', 'description': ''},
        {'element': '- cntr_engg', 'label': '미결제약정', 'type': 'String', 'description': ''},
        {'element': '- cntr_pred_pre', 'label': '미결제전일대비', 'type': 'String', 'description': ''},
        {'element': '- theory_pric', 'label': '이론가', 'type': 'String', 'description': ''},
        {'element': '- innr_vltl', 'label': '내재변동성', 'type': 'String', 'description': ''},
        {'element': '- delta', 'label': '델타', 'type': 'String', 'description': ''},
        {'element': '- gam', 'label': '감마', 'type': 'String', 'description': ''},
        {'element': '- theta', 'label': '쎄타', 'type': 'String', 'description': ''},
        {'element': '- vega', 'label': '베가', 'type': 'String', 'description': ''},
        {'element': '- law', 'label': '로', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10099 – 종목정보 리스트
    # ───────────────────────────────────────────────────────
    'ka10099': [
        {'element': 'list', 'label': '종목리스트', 'type': 'LIST', 'description': ''},
        {'element': '- code', 'label': '종목코드', 'type': 'String', 'description': '단축코드'},
        {'element': '- name', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- listCount', 'label': '상장주식수', 'type': 'String', 'description': ''},
        {'element': '- auditInfo', 'label': '감리구분', 'type': 'String', 'description': ''},
        {'element': '- regDay', 'label': '상장일', 'type': 'String', 'description': ''},
        {'element': '- lastPrice', 'label': '전일종가', 'type': 'String', 'description': ''},
        {'element': '- state', 'label': '종목상태', 'type': 'String', 'description': ''},
        {'element': '- marketCode', 'label': '시장구분코드', 'type': 'String', 'description': ''},
        {'element': '- marketName', 'label': '시장명', 'type': 'String', 'description': ''},
        {'element': '- upName', 'label': '업종명', 'type': 'String', 'description': ''},
        {'element': '- upSizeName', 'label': '회사크기분류', 'type': 'String', 'description': ''},
        {'element': '- orderWarning', 'label': '투자유의종목여부', 'type': 'String', 'description': '0: 해당없음, 2: 정리매매, 3: 단기과열, 4: 투자위험, 5: 투자경과, 1: ETF투자주의요망(ETF인 경우만 전달'},
        {'element': '- companyClassName', 'label': '회사분류', 'type': 'String', 'description': '코스닥만 존재함'},
        {'element': '- nxtEnable', 'label': 'NXT가능여부', 'type': 'String', 'description': 'Y: 가능'},
    ],

    # ───────────────────────────────────────────────────────
    # ka10100 – 종목정보 조회
    # ───────────────────────────────────────────────────────
    'ka10100': [
        {'element': 'code', 'label': '종목코드', 'type': 'String', 'description': '단축코드'},
        {'element': 'name', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': 'listCount', 'label': '상장주식수', 'type': 'String', 'description': ''},
        {'element': 'auditInfo', 'label': '감리구분', 'type': 'String', 'description': ''},
        {'element': 'regDay', 'label': '상장일', 'type': 'String', 'description': ''},
        {'element': 'lastPrice', 'label': '전일종가', 'type': 'String', 'description': ''},
        {'element': 'state', 'label': '종목상태', 'type': 'String', 'description': ''},
        {'element': 'marketCode', 'label': '시장구분코드', 'type': 'String', 'description': ''},
        {'element': 'marketName', 'label': '시장명', 'type': 'String', 'description': ''},
        {'element': 'upName', 'label': '업종명', 'type': 'String', 'description': ''},
        {'element': 'upSizeName', 'label': '회사크기분류', 'type': 'String', 'description': ''},
        {'element': 'companyClassName', 'label': '회사분류', 'type': 'String', 'description': '코스닥만 존재함'},
        {'element': 'orderWarning', 'label': '투자유의종목여부', 'type': 'String', 'description': '0: 해당없음, 2: 정리매매, 3: 단기과열, 4: 투자위험, 5: 투자경과, 1: ETF투자주의요망(ETF인 경우만 전달'},
        {'element': 'nxtEnable', 'label': 'NXT가능여부', 'type': 'String', 'description': 'Y: 가능'},
    ],

    # ───────────────────────────────────────────────────────
    # ka10101 – 업종코드 리스트
    # ───────────────────────────────────────────────────────
    'ka10101': [
        {'element': 'list', 'label': '업종코드리스트', 'type': 'LIST', 'description': ''},
        {'element': '- marketCode', 'label': '시장구분코드', 'type': 'LIST', 'description': ''},
        {'element': '- code', 'label': '코드', 'type': 'String', 'description': ''},
        {'element': '- name', 'label': '업종명', 'type': 'String', 'description': ''},
        {'element': '- group', 'label': '그룹', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka10102 – 회원사 리스트
    # ───────────────────────────────────────────────────────
    'ka10102': [
        {'element': 'list', 'label': '회원사코드리스트', 'type': 'LIST', 'description': ''},
        {'element': '- code', 'label': '코드', 'type': 'String', 'description': ''},
        {'element': '- name', 'label': '업종명', 'type': 'String', 'description': ''},
        {'element': '- gb', 'label': '구분', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka90003 – 프로그램순매수상위50요청
    # ───────────────────────────────────────────────────────
    'ka90003': [
        {'element': 'prm_netprps_upper_50', 'label': '프로그램순매수상위50', 'type': 'LIST', 'description': ''},
        {'element': '- rank', 'label': '순위', 'type': 'String', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- flu_sig', 'label': '등락기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- flu_rt', 'label': '등락율', 'type': 'String', 'description': ''},
        {'element': '- acc_trde_qty', 'label': '누적거래량', 'type': 'String', 'description': ''},
        {'element': '- prm_sell_amt', 'label': '프로그램매도금액', 'type': 'String', 'description': ''},
        {'element': '- prm_buy_amt', 'label': '프로그램매수금액', 'type': 'String', 'description': ''},
        {'element': '- prm_netprps_amt', 'label': '프로그램순매수금액', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # ka90004 – 종목별프로그램매매현황요청
    # ───────────────────────────────────────────────────────
    'ka90004': [
        {'element': 'tot_1', 'label': '매수체결수량합계', 'type': 'String', 'description': ''},
        {'element': 'tot_2', 'label': '매수체결금액합계', 'type': 'String', 'description': ''},
        {'element': 'tot_3', 'label': '매도체결수량합계', 'type': 'String', 'description': ''},
        {'element': 'tot_4', 'label': '매도체결금액합계', 'type': 'String', 'description': ''},
        {'element': 'tot_5', 'label': '순매수대금합계', 'type': 'String', 'description': ''},
        {'element': 'tot_6', 'label': '합계6', 'type': 'String', 'description': ''},
        {'element': 'stk_prm_trde_prst', 'label': '종목별프로그램매매현황', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- cur_prc', 'label': '현재가', 'type': 'String', 'description': ''},
        {'element': '- flu_sig', 'label': '등락기호', 'type': 'String', 'description': ''},
        {'element': '- pred_pre', 'label': '전일대비', 'type': 'String', 'description': ''},
        {'element': '- buy_cntr_qty', 'label': '매수체결수량', 'type': 'String', 'description': ''},
        {'element': '- buy_cntr_amt', 'label': '매수체결금액', 'type': 'String', 'description': ''},
        {'element': '- sel_cntr_qty', 'label': '매도체결수량', 'type': 'String', 'description': ''},
        {'element': '- sel_cntr_amt', 'label': '매도체결금액', 'type': 'String', 'description': ''},
        {'element': '- netprps_prica', 'label': '순매수대금', 'type': 'String', 'description': ''},
        {'element': '- all_trde_rt', 'label': '전체거래비율', 'type': 'String', 'description': ''},
    ],

    # ───────────────────────────────────────────────────────
    # kt20016 – 신용융자 가능종목요청
    # ───────────────────────────────────────────────────────
    'kt20016': [
        {'element': 'crd_loan_able', 'label': '신용융자가능여부', 'type': 'String', 'description': ''},
        {'element': 'crd_loan_pos_stk', 'label': '신용융자가능종목', 'type': 'LIST', 'description': ''},
        {'element': '- stk_cd', 'label': '종목코드', 'type': 'String', 'description': ''},
        {'element': '- stk_nm', 'label': '종목명', 'type': 'String', 'description': ''},
        {'element': '- crd_assr_rt', 'label': '신용보증금율', 'type': 'String', 'description': ''},
        {'element': '- repl_pric', 'label': '대용가', 'type': 'String', 'description': ''},
        {'element': '- pred_close_pric', 'label': '전일종가', 'type': 'String', 'description': ''},
        {'element': '- crd_limit_over_yn', 'label': '신용한도초과여부', 'type': 'String', 'description': ''},
        {'element': '- crd_limit_over_txt', 'label': '신용한도초과', 'type': 'String', 'description': 'N:공란,Y:회사한도 초과'},
    ],

    # ───────────────────────────────────────────────────────
    # kt20017 – 신용융자 가능문의
    # ───────────────────────────────────────────────────────
    'kt20017': [
        {'element': 'crd_alow_yn', 'label': '신용가능여부', 'type': 'String', 'description': ''},
    ],

}
