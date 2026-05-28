-- =============================================================
-- quotations (/uapi/domestic-stock/v1/quotations/) 모듈 DB 스키마
-- source: src/quotations/specs_request.py, src/quotations/specs_response.py
-- =============================================================

-- 테이블명 규칙: URL 마지막 경로를 snake_case 로 변환
-- 예: /uapi/domestic-stock/v1/quotations/inquire-price -> inquire_price

DROP TABLE IF EXISTS inquire_daily_price CASCADE;
DROP TABLE IF EXISTS inquire_price CASCADE;
DROP TABLE IF EXISTS inquire_overtime_price CASCADE;
DROP TABLE IF EXISTS inquire_time_overtimeconclusion CASCADE;
DROP TABLE IF EXISTS inquire_daily_overtimeprice CASCADE;
DROP TABLE IF EXISTS inquire_overtime_asking_price CASCADE;
DROP TABLE IF EXISTS inquire_time_itemconclusion CASCADE;
DROP TABLE IF EXISTS inquire_price_2 CASCADE;
DROP TABLE IF EXISTS inquire_time_dailychartprice CASCADE;
DROP TABLE IF EXISTS inquire_daily_itemchartprice CASCADE;
DROP TABLE IF EXISTS inquire_asking_price_exp_ccn CASCADE;
DROP TABLE IF EXISTS inquire_ccnl CASCADE;
DROP TABLE IF EXISTS inquire_member CASCADE;
DROP TABLE IF EXISTS inquire_investor CASCADE;
DROP TABLE IF EXISTS exp_closing_price CASCADE;
DROP TABLE IF EXISTS inquire_time_itemchartprice CASCADE;
DROP TABLE IF EXISTS inquire_elw_price CASCADE;
DROP TABLE IF EXISTS exp_index_trend CASCADE;
DROP TABLE IF EXISTS inquire_daily_indexchartprice CASCADE;
DROP TABLE IF EXISTS inquire_index_timeprice CASCADE;
DROP TABLE IF EXISTS inquire_index_category_price CASCADE;
DROP TABLE IF EXISTS inquire_time_indexchartprice CASCADE;
DROP TABLE IF EXISTS chk_holiday CASCADE;
DROP TABLE IF EXISTS exp_total_index CASCADE;
DROP TABLE IF EXISTS inquire_index_price CASCADE;
DROP TABLE IF EXISTS market_time CASCADE;
DROP TABLE IF EXISTS inquire_index_tickprice CASCADE;
DROP TABLE IF EXISTS inquire_index_daily_price CASCADE;
DROP TABLE IF EXISTS comp_interest CASCADE;
DROP TABLE IF EXISTS inquire_vi_status CASCADE;
DROP TABLE IF EXISTS news_title CASCADE;
DROP TABLE IF EXISTS search_info CASCADE;
DROP TABLE IF EXISTS invest_opbysec CASCADE;
DROP TABLE IF EXISTS credit_by_company CASCADE;
DROP TABLE IF EXISTS invest_opinion CASCADE;
DROP TABLE IF EXISTS lendable_by_company CASCADE;
DROP TABLE IF EXISTS search_stock_info CASCADE;
DROP TABLE IF EXISTS estimate_perform CASCADE;
DROP TABLE IF EXISTS comp_program_trade_today CASCADE;
DROP TABLE IF EXISTS daily_credit_balance CASCADE;
DROP TABLE IF EXISTS inquire_investor_daily_by_market CASCADE;
DROP TABLE IF EXISTS daily_short_sale CASCADE;
DROP TABLE IF EXISTS investor_trade_by_stock_daily CASCADE;
DROP TABLE IF EXISTS psearch_title CASCADE;
DROP TABLE IF EXISTS capture_uplowprice CASCADE;
DROP TABLE IF EXISTS comp_program_trade_daily CASCADE;
DROP TABLE IF EXISTS daily_loan_trans CASCADE;
DROP TABLE IF EXISTS psearch_result CASCADE;
DROP TABLE IF EXISTS pbar_tratio CASCADE;
DROP TABLE IF EXISTS foreign_institution_total CASCADE;
DROP TABLE IF EXISTS intstock_stocklist_by_group CASCADE;
DROP TABLE IF EXISTS inquire_member_daily CASCADE;
DROP TABLE IF EXISTS program_trade_by_stock_daily CASCADE;
DROP TABLE IF EXISTS intstock_grouplist CASCADE;
DROP TABLE IF EXISTS investor_trend_estimate CASCADE;
DROP TABLE IF EXISTS inquire_daily_trade_volume CASCADE;
DROP TABLE IF EXISTS tradprt_byamt CASCADE;
DROP TABLE IF EXISTS investor_program_trade_today CASCADE;
DROP TABLE IF EXISTS mktfunds CASCADE;
DROP TABLE IF EXISTS exp_price_trend CASCADE;
DROP TABLE IF EXISTS frgnmem_trade_trend CASCADE;
DROP TABLE IF EXISTS inquire_investor_time_by_market CASCADE;
DROP TABLE IF EXISTS program_trade_by_stock CASCADE;
DROP TABLE IF EXISTS frgnmem_trade_estimate CASCADE;
DROP TABLE IF EXISTS frgnmem_pchs_trend CASCADE;
DROP TABLE IF EXISTS intstock_multprice CASCADE;
DROP TABLE IF EXISTS volume_rank CASCADE;

-- =============================================================
-- inquire_daily_price - 주식현재가 일자별 (FHKST01010400)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-daily-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_daily_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_period_div_code TEXT NULL COMMENT '요청 기간 분류 코드',
    req_fid_org_adj_prc TEXT NULL COMMENT '요청 수정주가 원주가 가격',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '전일 대비 거래량 비율',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_hts_frgn_ehrt TEXT NULL COMMENT 'HTS 외국인 소진율',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_flng_cls_code TEXT NULL COMMENT '락 구분 코드',
    rsp_acml_prtt_rate TEXT NULL COMMENT '누적 분할 비율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-daily-price';

-- =============================================================
-- inquire_price - 주식현재가 시세 (FHKST01010100)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_iscd_stat_cls_code TEXT NULL COMMENT '종목 상태 구분 코드',
    rsp_marg_rate TEXT NULL COMMENT '증거금 비율',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표 시장 한글 명',
    rsp_new_hgpr_lwpr_cls_code TEXT NULL COMMENT '신 고가 저가 구분 코드',
    rsp_bstp_kor_isnm TEXT NULL COMMENT '업종 한글 종목명',
    rsp_temp_stop_yn TEXT NULL COMMENT '임시 정지 여부',
    rsp_oprc_rang_cont_yn TEXT NULL COMMENT '시가 범위 연장 여부',
    rsp_clpr_rang_cont_yn TEXT NULL COMMENT '종가 범위 연장 여부',
    rsp_crdt_able_yn TEXT NULL COMMENT '신용 가능 여부',
    rsp_grmn_rate_cls_code TEXT NULL COMMENT '보증금 비율 구분 코드',
    rsp_elw_pblc_yn TEXT NULL COMMENT 'ELW 발행 여부',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '전일 대비 거래량 비율',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_stck_mxpr TEXT NULL COMMENT '주식 상한가',
    rsp_stck_llam TEXT NULL COMMENT '주식 하한가',
    rsp_stck_sdpr TEXT NULL COMMENT '주식 기준가',
    rsp_wghn_avrg_stck_prc TEXT NULL COMMENT '가중 평균 주식 가격',
    rsp_hts_frgn_ehrt TEXT NULL COMMENT 'HTS 외국인 소진율',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_pgtr_ntby_qty TEXT NULL COMMENT '프로그램매매 순매수 수량',
    rsp_pvt_scnd_dmrs_prc TEXT NULL COMMENT '피벗 2차 디저항 가격',
    rsp_pvt_frst_dmrs_prc TEXT NULL COMMENT '피벗 1차 디저항 가격',
    rsp_pvt_pont_val TEXT NULL COMMENT '피벗 포인트 값',
    rsp_pvt_frst_dmsp_prc TEXT NULL COMMENT '피벗 1차 디지지 가격',
    rsp_pvt_scnd_dmsp_prc TEXT NULL COMMENT '피벗 2차 디지지 가격',
    rsp_dmrs_val TEXT NULL COMMENT '디저항 값',
    rsp_dmsp_val TEXT NULL COMMENT '디지지 값',
    rsp_cpfn TEXT NULL COMMENT '자본금',
    rsp_rstc_wdth_prc TEXT NULL COMMENT '제한 폭 가격',
    rsp_stck_fcam TEXT NULL COMMENT '주식 액면가',
    rsp_stck_sspr TEXT NULL COMMENT '주식 대용가',
    rsp_aspr_unit TEXT NULL COMMENT '호가단위',
    rsp_hts_deal_qty_unit_val TEXT NULL COMMENT 'HTS 매매 수량 단위 값',
    rsp_lstn_stcn TEXT NULL COMMENT '상장 주수',
    rsp_hts_avls TEXT NULL COMMENT 'HTS 시가총액',
    rsp_per TEXT NULL COMMENT 'PER',
    rsp_pbr TEXT NULL COMMENT 'PBR',
    rsp_stac_month TEXT NULL COMMENT '결산 월',
    rsp_vol_tnrt TEXT NULL COMMENT '거래량 회전율',
    rsp_eps TEXT NULL COMMENT 'EPS',
    rsp_bps TEXT NULL COMMENT 'BPS',
    rsp_d250_hgpr TEXT NULL COMMENT '250일 최고가',
    rsp_d250_hgpr_date TEXT NULL COMMENT '250일 최고가 일자',
    rsp_d250_hgpr_vrss_prpr_rate TEXT NULL COMMENT '250일 최고가 대비 현재가 비율',
    rsp_d250_lwpr TEXT NULL COMMENT '250일 최저가',
    rsp_d250_lwpr_date TEXT NULL COMMENT '250일 최저가 일자',
    rsp_d250_lwpr_vrss_prpr_rate TEXT NULL COMMENT '250일 최저가 대비 현재가 비율',
    rsp_stck_dryy_hgpr TEXT NULL COMMENT '주식 연중 최고가',
    rsp_dryy_hgpr_vrss_prpr_rate TEXT NULL COMMENT '연중 최고가 대비 현재가 비율',
    rsp_dryy_hgpr_date TEXT NULL COMMENT '연중 최고가 일자',
    rsp_stck_dryy_lwpr TEXT NULL COMMENT '주식 연중 최저가',
    rsp_dryy_lwpr_vrss_prpr_rate TEXT NULL COMMENT '연중 최저가 대비 현재가 비율',
    rsp_dryy_lwpr_date TEXT NULL COMMENT '연중 최저가 일자',
    rsp_w52_hgpr TEXT NULL COMMENT '52주일 최고가',
    rsp_w52_hgpr_vrss_prpr_ctrt TEXT NULL COMMENT '52주일 최고가 대비 현재가 대비',
    rsp_w52_hgpr_date TEXT NULL COMMENT '52주일 최고가 일자',
    rsp_w52_lwpr TEXT NULL COMMENT '52주일 최저가',
    rsp_w52_lwpr_vrss_prpr_ctrt TEXT NULL COMMENT '52주일 최저가 대비 현재가 대비',
    rsp_w52_lwpr_date TEXT NULL COMMENT '52주일 최저가 일자',
    rsp_whol_loan_rmnd_rate TEXT NULL COMMENT '전체 융자 잔고 비율',
    rsp_ssts_yn TEXT NULL COMMENT '공매도가능여부',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식 단축 종목코드',
    rsp_fcam_cnnm TEXT NULL COMMENT '액면가 통화명',
    rsp_cpfn_cnnm TEXT NULL COMMENT '자본금 통화명',
    rsp_apprch_rate TEXT NULL COMMENT '접근도',
    rsp_frgn_hldn_qty TEXT NULL COMMENT '외국인 보유 수량',
    rsp_vi_cls_code TEXT NULL COMMENT 'VI적용구분코드',
    rsp_ovtm_vi_cls_code TEXT NULL COMMENT '시간외단일가VI적용구분코드',
    rsp_last_ssts_cntg_qty TEXT NULL COMMENT '최종 공매도 체결 수량',
    rsp_invt_caful_yn TEXT NULL COMMENT '투자유의여부',
    rsp_mrkt_warn_cls_code TEXT NULL COMMENT '시장경고코드',
    rsp_short_over_yn TEXT NULL COMMENT '단기과열여부',
    rsp_sltr_yn TEXT NULL COMMENT '정리매매여부',
    rsp_mang_issu_cls_code TEXT NULL COMMENT '관리종목여부',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-price';

-- =============================================================
-- inquire_overtime_price - 국내주식 시간외현재가 (FHPST02300000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-overtime-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_overtime_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bstp_kor_isnm TEXT NULL COMMENT '업종 한글 종목명',
    rsp_mang_issu_cls_name TEXT NULL COMMENT '관리 종목 구분 명',
    rsp_ovtm_untp_prpr TEXT NULL COMMENT '시간외 단일가 현재가',
    rsp_ovtm_untp_prdy_vrss TEXT NULL COMMENT '시간외 단일가 전일 대비',
    rsp_ovtm_untp_prdy_vrss_sign TEXT NULL COMMENT '시간외 단일가 전일 대비 부호',
    rsp_ovtm_untp_prdy_ctrt TEXT NULL COMMENT '시간외 단일가 전일 대비율',
    rsp_ovtm_untp_vol TEXT NULL COMMENT '시간외 단일가 거래량',
    rsp_ovtm_untp_tr_pbmn TEXT NULL COMMENT '시간외 단일가 거래 대금',
    rsp_ovtm_untp_mxpr TEXT NULL COMMENT '시간외 단일가 상한가',
    rsp_ovtm_untp_llam TEXT NULL COMMENT '시간외 단일가 하한가',
    rsp_ovtm_untp_oprc TEXT NULL COMMENT '시간외 단일가 시가2',
    rsp_ovtm_untp_hgpr TEXT NULL COMMENT '시간외 단일가 최고가',
    rsp_ovtm_untp_lwpr TEXT NULL COMMENT '시간외 단일가 최저가',
    rsp_marg_rate TEXT NULL COMMENT '증거금 비율',
    rsp_ovtm_untp_antc_cnpr TEXT NULL COMMENT '시간외 단일가 예상 체결가',
    rsp_ovtm_untp_antc_cntg_vrss TEXT NULL COMMENT '시간외 단일가 예상 체결 대비',
    rsp_ovtm_untp_antc_cntg_vrss_sign TEXT NULL COMMENT '시간외 단일가 예상 체결 대비',
    rsp_ovtm_untp_antc_cntg_ctrt TEXT NULL COMMENT '시간외 단일가 예상 체결 대비율',
    rsp_ovtm_untp_antc_cnqn TEXT NULL COMMENT '시간외 단일가 예상 체결량',
    rsp_crdt_able_yn TEXT NULL COMMENT '신용 가능 여부',
    rsp_new_lstn_cls_name TEXT NULL COMMENT '신규 상장 구분 명',
    rsp_sltr_yn TEXT NULL COMMENT '정리매매 여부',
    rsp_mang_issu_yn TEXT NULL COMMENT '관리 종목 여부',
    rsp_mrkt_warn_cls_code TEXT NULL COMMENT '시장 경고 구분 코드',
    rsp_trht_yn TEXT NULL COMMENT '거래정지 여부',
    rsp_vlnt_deal_cls_name TEXT NULL COMMENT '임의 매매 구분 명',
    rsp_ovtm_untp_sdpr TEXT NULL COMMENT '시간외 단일가 기준가',
    rsp_mrkt_warn_cls_name TEXT NULL COMMENT '시장 경구 구분 명',
    rsp_revl_issu_reas_name TEXT NULL COMMENT '재평가 종목 사유 명',
    rsp_insn_pbnt_yn TEXT NULL COMMENT '불성실 공시 여부',
    rsp_flng_cls_name TEXT NULL COMMENT '락 구분 이름',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표 시장 한글 명',
    rsp_ovtm_vi_cls_code TEXT NULL COMMENT '시간외단일가VI적용구분코드',
    rsp_bidp TEXT NULL COMMENT '매수호가',
    rsp_askp TEXT NULL COMMENT '매도호가',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-overtime-price';

-- =============================================================
-- inquire_time_overtimeconclusion - 주식현재가 시간외시간별체결 (FHPST02310000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-time-overtimeconclusion
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_time_overtimeconclusion (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_hour_cls_code TEXT NULL COMMENT '요청 시간 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_ovtm_untp_prpr TEXT NULL COMMENT '시간외 단일가 현재가',
    rsp_ovtm_untp_prdy_vrss TEXT NULL COMMENT '시간외 단일가 전일 대비',
    rsp_ovtm_untp_prdy_vrss_sign TEXT NULL COMMENT '시간외 단일가 전일 대비 부호',
    rsp_ovtm_untp_prdy_ctrt TEXT NULL COMMENT '시간외 단일가 전일 대비율',
    rsp_ovtm_untp_vol TEXT NULL COMMENT '시간외 단일가 거래량',
    rsp_ovtm_untp_tr_pbmn TEXT NULL COMMENT '시간외 단일가 거래 대금',
    rsp_ovtm_untp_mxpr TEXT NULL COMMENT '시간외 단일가 상한가',
    rsp_ovtm_untp_llam TEXT NULL COMMENT '시간외 단일가 하한가',
    rsp_ovtm_untp_oprc TEXT NULL COMMENT '시간외 단일가 시가2',
    rsp_ovtm_untp_hgpr TEXT NULL COMMENT '시간외 단일가 최고가',
    rsp_ovtm_untp_lwpr TEXT NULL COMMENT '시간외 단일가 최저가',
    rsp_ovtm_untp_antc_cnpr TEXT NULL COMMENT '시간외 단일가 예상 체결가',
    rsp_ovtm_untp_antc_cntg_vrss TEXT NULL COMMENT '시간외 단일가 예상 체결 대비',
    rsp_ovtm_untp_antc_cntg_vrss_sign TEXT NULL COMMENT '시간외 단일가 예상 체결 대비',
    rsp_ovtm_untp_antc_cntg_ctrt TEXT NULL COMMENT '시간외 단일가 예상 체결 대비율',
    rsp_ovtm_untp_antc_vol TEXT NULL COMMENT '시간외 단일가 예상 거래량',
    rsp_uplm_sign TEXT NULL COMMENT '상한 부호',
    rsp_lslm_sign TEXT NULL COMMENT '하한 부호',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_askp TEXT NULL COMMENT '매도호가',
    rsp_bidp TEXT NULL COMMENT '매수호가',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-time-overtimeconclusion';

-- =============================================================
-- inquire_daily_overtimeprice - 주식현재가 시간외일자별주가 (FHPST02320000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-daily-overtimeprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_daily_overtimeprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_ovtm_untp_prpr TEXT NULL COMMENT '시간외 단일가 현재가',
    rsp_ovtm_untp_prdy_vrss TEXT NULL COMMENT '시간외 단일가 전일 대비',
    rsp_ovtm_untp_prdy_vrss_sign TEXT NULL COMMENT '시간외 단일가 전일 대비 부호',
    rsp_ovtm_untp_prdy_ctrt TEXT NULL COMMENT '시간외 단일가 전일 대비율',
    rsp_ovtm_untp_vol TEXT NULL COMMENT '시간외 단일가 거래량',
    rsp_ovtm_untp_tr_pbmn TEXT NULL COMMENT '시간외 단일가 거래대금',
    rsp_ovtm_untp_mxpr TEXT NULL COMMENT '시간외 단일가 상한가',
    rsp_ovtm_untp_llam TEXT NULL COMMENT '시간외 단일가 하한가',
    rsp_ovtm_untp_oprc TEXT NULL COMMENT '시간외 단일가 시가2',
    rsp_ovtm_untp_hgpr TEXT NULL COMMENT '시간외 단일가 최고가',
    rsp_ovtm_untp_lwpr TEXT NULL COMMENT '시간외 단일가 최저가',
    rsp_ovtm_untp_antc_cnpr TEXT NULL COMMENT '시간외 단일가 예상 체결가',
    rsp_ovtm_untp_antc_cntg_vrss TEXT NULL COMMENT '시간외 단일가 예상 체결 대비',
    rsp_ovtm_untp_antc_cntg_vrss_sign TEXT NULL COMMENT '시간외 단일가 예상 체결 대비',
    rsp_ovtm_untp_antc_cntg_ctrt TEXT NULL COMMENT '시간외 단일가 예상 체결 대비율',
    rsp_ovtm_untp_antc_vol TEXT NULL COMMENT '시간외 단일가 예상 거래량',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-daily-overtimeprice';

-- =============================================================
-- inquire_overtime_asking_price - 국내주식 시간외호가 (FHPST02300400)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-overtime-asking-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_overtime_asking_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_ovtm_untp_last_hour TEXT NULL COMMENT '시간외 단일가 최종 시간',
    rsp_ovtm_untp_askp1 TEXT NULL COMMENT '시간외 단일가 매도호가1',
    rsp_ovtm_untp_askp2 TEXT NULL COMMENT '시간외 단일가 매도호가2',
    rsp_ovtm_untp_askp3 TEXT NULL COMMENT '시간외 단일가 매도호가3',
    rsp_ovtm_untp_askp4 TEXT NULL COMMENT '시간외 단일가 매도호가4',
    rsp_ovtm_untp_askp5 TEXT NULL COMMENT '시간외 단일가 매도호가5',
    rsp_ovtm_untp_askp6 TEXT NULL COMMENT '시간외 단일가 매도호가6',
    rsp_ovtm_untp_askp7 TEXT NULL COMMENT '시간외 단일가 매도호가7',
    rsp_ovtm_untp_askp8 TEXT NULL COMMENT '시간외 단일가 매도호가8',
    rsp_ovtm_untp_askp9 TEXT NULL COMMENT '시간외 단일가 매도호가9',
    rsp_ovtm_untp_askp10 TEXT NULL COMMENT '시간외 단일가 매도호가10',
    rsp_ovtm_untp_bidp1 TEXT NULL COMMENT '시간외 단일가 매수호가1',
    rsp_ovtm_untp_bidp2 TEXT NULL COMMENT '시간외 단일가 매수호가2',
    rsp_ovtm_untp_bidp3 TEXT NULL COMMENT '시간외 단일가 매수호가3',
    rsp_ovtm_untp_bidp4 TEXT NULL COMMENT '시간외 단일가 매수호가4',
    rsp_ovtm_untp_bidp5 TEXT NULL COMMENT '시간외 단일가 매수호가5',
    rsp_ovtm_untp_bidp6 TEXT NULL COMMENT '시간외 단일가 매수호가6',
    rsp_ovtm_untp_bidp7 TEXT NULL COMMENT '시간외 단일가 매수호가7',
    rsp_ovtm_untp_bidp8 TEXT NULL COMMENT '시간외 단일가 매수호가8',
    rsp_ovtm_untp_bidp9 TEXT NULL COMMENT '시간외 단일가 매수호가9',
    rsp_ovtm_untp_bidp10 TEXT NULL COMMENT '시간외 단일가 매수호가10',
    rsp_ovtm_untp_askp_icdc1 TEXT NULL COMMENT '시간외 단일가 매도호가 증감1',
    rsp_ovtm_untp_askp_icdc2 TEXT NULL COMMENT '시간외 단일가 매도호가 증감2',
    rsp_ovtm_untp_askp_icdc3 TEXT NULL COMMENT '시간외 단일가 매도호가 증감3',
    rsp_ovtm_untp_askp_icdc4 TEXT NULL COMMENT '시간외 단일가 매도호가 증감4',
    rsp_ovtm_untp_askp_icdc5 TEXT NULL COMMENT '시간외 단일가 매도호가 증감5',
    rsp_ovtm_untp_askp_icdc6 TEXT NULL COMMENT '시간외 단일가 매도호가 증감6',
    rsp_ovtm_untp_askp_icdc7 TEXT NULL COMMENT '시간외 단일가 매도호가 증감7',
    rsp_ovtm_untp_askp_icdc8 TEXT NULL COMMENT '시간외 단일가 매도호가 증감8',
    rsp_ovtm_untp_askp_icdc9 TEXT NULL COMMENT '시간외 단일가 매도호가 증감9',
    rsp_ovtm_untp_askp_icdc10 TEXT NULL COMMENT '시간외 단일가 매도호가 증감10',
    rsp_ovtm_untp_bidp_icdc1 TEXT NULL COMMENT '시간외 단일가 매수호가 증감1',
    rsp_ovtm_untp_bidp_icdc2 TEXT NULL COMMENT '시간외 단일가 매수호가 증감2',
    rsp_ovtm_untp_bidp_icdc3 TEXT NULL COMMENT '시간외 단일가 매수호가 증감3',
    rsp_ovtm_untp_bidp_icdc4 TEXT NULL COMMENT '시간외 단일가 매수호가 증감4',
    rsp_ovtm_untp_bidp_icdc5 TEXT NULL COMMENT '시간외 단일가 매수호가 증감5',
    rsp_ovtm_untp_bidp_icdc6 TEXT NULL COMMENT '시간외 단일가 매수호가 증감6',
    rsp_ovtm_untp_bidp_icdc7 TEXT NULL COMMENT '시간외 단일가 매수호가 증감7',
    rsp_ovtm_untp_bidp_icdc8 TEXT NULL COMMENT '시간외 단일가 매수호가 증감8',
    rsp_ovtm_untp_bidp_icdc9 TEXT NULL COMMENT '시간외 단일가 매수호가 증감9',
    rsp_ovtm_untp_bidp_icdc10 TEXT NULL COMMENT '시간외 단일가 매수호가 증감10',
    rsp_ovtm_untp_askp_rsqn1 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량1',
    rsp_ovtm_untp_askp_rsqn2 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량2',
    rsp_ovtm_untp_askp_rsqn3 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량3',
    rsp_ovtm_untp_askp_rsqn4 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량4',
    rsp_ovtm_untp_askp_rsqn5 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량5',
    rsp_ovtm_untp_askp_rsqn6 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량6',
    rsp_ovtm_untp_askp_rsqn7 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량7',
    rsp_ovtm_untp_askp_rsqn8 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량8',
    rsp_ovtm_untp_askp_rsqn9 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량9',
    rsp_ovtm_untp_askp_rsqn10 TEXT NULL COMMENT '시간외 단일가 매도호가 잔량10',
    rsp_ovtm_untp_bidp_rsqn1 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량1',
    rsp_ovtm_untp_bidp_rsqn2 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량2',
    rsp_ovtm_untp_bidp_rsqn3 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량3',
    rsp_ovtm_untp_bidp_rsqn4 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량4',
    rsp_ovtm_untp_bidp_rsqn5 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량5',
    rsp_ovtm_untp_bidp_rsqn6 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량6',
    rsp_ovtm_untp_bidp_rsqn7 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량7',
    rsp_ovtm_untp_bidp_rsqn8 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량8',
    rsp_ovtm_untp_bidp_rsqn9 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량9',
    rsp_ovtm_untp_bidp_rsqn10 TEXT NULL COMMENT '시간외 단일가 매수호가 잔량10',
    rsp_ovtm_untp_total_askp_rsqn TEXT NULL COMMENT '시간외 단일가 총 매도호가 잔량',
    rsp_ovtm_untp_total_bidp_rsqn TEXT NULL COMMENT '시간외 단일가 총 매수호가 잔량',
    rsp_ovtm_untp_total_askp_rsqn_icdc TEXT NULL COMMENT '시간외 단일가 총 매도호가 잔량',
    rsp_ovtm_untp_total_bidp_rsqn_icdc TEXT NULL COMMENT '시간외 단일가 총 매수호가 잔량',
    rsp_ovtm_untp_ntby_bidp_rsqn TEXT NULL COMMENT '시간외 단일가 순매수 호가 잔량',
    rsp_total_askp_rsqn TEXT NULL COMMENT '총 매도호가 잔량',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '총 매수호가 잔량',
    rsp_total_askp_rsqn_icdc TEXT NULL COMMENT '총 매도호가 잔량 증감',
    rsp_total_bidp_rsqn_icdc TEXT NULL COMMENT '총 매수호가 잔량 증감',
    rsp_ovtm_total_askp_rsqn TEXT NULL COMMENT '시간외 총 매도호가 잔량',
    rsp_ovtm_total_bidp_rsqn TEXT NULL COMMENT '시간외 총 매수호가 잔량',
    rsp_ovtm_total_askp_icdc TEXT NULL COMMENT '시간외 총 매도호가 증감',
    rsp_ovtm_total_bidp_icdc TEXT NULL COMMENT '시간외 총 매수호가 증감',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-overtime-asking-price';

-- =============================================================
-- inquire_time_itemconclusion - 주식현재가 당일시간대별체결 (FHPST01060000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-time-itemconclusion
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_time_itemconclusion (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력 시간1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표 시장 한글 명',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_stck_pbpr TEXT NULL COMMENT '주식 현재가',
    rsp_askp TEXT NULL COMMENT '매도호가',
    rsp_bidp TEXT NULL COMMENT '매수호가',
    rsp_tday_rltv TEXT NULL COMMENT '당일 체결강도',
    rsp_cnqn TEXT NULL COMMENT '체결량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-time-itemconclusion';

-- =============================================================
-- inquire_price_2 - 주식현재가 시세2 (FHPST01010000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-price-2
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_price_2 (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표 시장 한글 명',
    rsp_new_hgpr_lwpr_cls_code TEXT NULL COMMENT '신 고가 저가 구분 코드',
    rsp_mxpr_llam_cls_code TEXT NULL COMMENT '상하한가 구분 코드',
    rsp_crdt_able_yn TEXT NULL COMMENT '신용 가능 여부',
    rsp_stck_mxpr TEXT NULL COMMENT '주식 상한가',
    rsp_elw_pblc_yn TEXT NULL COMMENT 'ELW 발행 여부',
    rsp_prdy_clpr_vrss_oprc_rate TEXT NULL COMMENT '전일 종가 대비 시가2 비율',
    rsp_crdt_rate TEXT NULL COMMENT '신용 비율',
    rsp_marg_rate TEXT NULL COMMENT '증거금 비율',
    rsp_lwpr_vrss_prpr TEXT NULL COMMENT '최저가 대비 현재가',
    rsp_lwpr_vrss_prpr_sign TEXT NULL COMMENT '최저가 대비 현재가 부호',
    rsp_prdy_clpr_vrss_lwpr_rate TEXT NULL COMMENT '전일 종가 대비 최저가 비율',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_hgpr_vrss_prpr TEXT NULL COMMENT '최고가 대비 현재가',
    rsp_hgpr_vrss_prpr_sign TEXT NULL COMMENT '최고가 대비 현재가 부호',
    rsp_prdy_clpr_vrss_hgpr_rate TEXT NULL COMMENT '전일 종가 대비 최고가 비율',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_oprc_vrss_prpr TEXT NULL COMMENT '시가2 대비 현재가',
    rsp_oprc_vrss_prpr_sign TEXT NULL COMMENT '시가2 대비 현재가 부호',
    rsp_mang_issu_yn TEXT NULL COMMENT '관리 종목 여부',
    rsp_divi_app_cls_code TEXT NULL COMMENT '동시호가배분처리코드',
    rsp_short_over_yn TEXT NULL COMMENT '단기과열여부',
    rsp_mrkt_warn_cls_code TEXT NULL COMMENT '시장경고코드',
    rsp_invt_caful_yn TEXT NULL COMMENT '투자유의여부',
    rsp_stange_runup_yn TEXT NULL COMMENT '이상급등여부',
    rsp_ssts_hot_yn TEXT NULL COMMENT '공매도과열 여부',
    rsp_low_current_yn TEXT NULL COMMENT '저유동성 종목 여부',
    rsp_vi_cls_code TEXT NULL COMMENT 'VI적용구분코드',
    rsp_short_over_cls_code TEXT NULL COMMENT '단기과열구분코드',
    rsp_stck_llam TEXT NULL COMMENT '주식 하한가',
    rsp_new_lstn_cls_name TEXT NULL COMMENT '신규 상장 구분 명',
    rsp_vlnt_deal_cls_name TEXT NULL COMMENT '임의 매매 구분 명',
    rsp_flng_cls_name TEXT NULL COMMENT '락 구분 이름',
    rsp_revl_issu_reas_name TEXT NULL COMMENT '재평가 종목 사유 명',
    rsp_mrkt_warn_cls_name TEXT NULL COMMENT '시장 경고 구분 명',
    rsp_stck_sdpr TEXT NULL COMMENT '주식 기준가',
    rsp_bstp_cls_code TEXT NULL COMMENT '업종 구분 코드',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식 전일 종가',
    rsp_insn_pbnt_yn TEXT NULL COMMENT '불성실 공시 여부',
    rsp_fcam_mod_cls_name TEXT NULL COMMENT '액면가 변경 구분 명',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '전일 대비 거래량 비율',
    rsp_bstp_kor_isnm TEXT NULL COMMENT '업종 한글 종목명',
    rsp_sltr_yn TEXT NULL COMMENT '정리매매 여부',
    rsp_trht_yn TEXT NULL COMMENT '거래정지 여부',
    rsp_oprc_rang_cont_yn TEXT NULL COMMENT '시가 범위 연장 여부',
    rsp_vlnt_fin_cls_code TEXT NULL COMMENT '임의 종료 구분 코드',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-price-2';

-- =============================================================
-- inquire_time_dailychartprice - 주식일별분봉조회 (FHKST03010230)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-time-dailychartprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_time_dailychartprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력 시간1',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜1',
    req_fid_pw_data_incu_yn TEXT NULL COMMENT '요청 과거 데이터 포함 여부',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식 전일 종가',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-time-dailychartprice';

-- =============================================================
-- inquire_daily_itemchartprice - 국내주식기간별시세(일_주_월_년) (FHKST03010100)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_daily_itemchartprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜 1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 입력 날짜 2',
    req_fid_period_div_code TEXT NULL COMMENT '요청 기간분류코드',
    req_fid_org_adj_prc TEXT NULL COMMENT '요청 수정주가 원주가 가격 여부',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식 전일 종가',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식 단축 종목코드',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_stck_mxpr TEXT NULL COMMENT '주식 상한가',
    rsp_stck_llam TEXT NULL COMMENT '주식 하한가',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_stck_prdy_oprc TEXT NULL COMMENT '주식 전일 시가',
    rsp_stck_prdy_hgpr TEXT NULL COMMENT '주식 전일 최고가',
    rsp_stck_prdy_lwpr TEXT NULL COMMENT '주식 전일 최저가',
    rsp_askp TEXT NULL COMMENT '매도호가',
    rsp_bidp TEXT NULL COMMENT '매수호가',
    rsp_prdy_vrss_vol TEXT NULL COMMENT '전일 대비 거래량',
    rsp_vol_tnrt TEXT NULL COMMENT '거래량 회전율',
    rsp_stck_fcam TEXT NULL COMMENT '주식 액면가',
    rsp_lstn_stcn TEXT NULL COMMENT '상장 주수',
    rsp_cpfn TEXT NULL COMMENT '자본금',
    rsp_hts_avls TEXT NULL COMMENT 'HTS 시가총액',
    rsp_per TEXT NULL COMMENT 'PER',
    rsp_eps TEXT NULL COMMENT 'EPS',
    rsp_pbr TEXT NULL COMMENT 'PBR',
    rsp_itewhol_loan_rmnd_ratem TEXT NULL COMMENT '전체 융자 잔고 비율',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_flng_cls_code TEXT NULL COMMENT '락 구분 코드',
    rsp_prtt_rate TEXT NULL COMMENT '분할 비율',
    rsp_mod_yn TEXT NULL COMMENT '변경 여부',
    rsp_revl_issu_reas TEXT NULL COMMENT '재평가사유코드',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-daily-itemchartprice';

-- =============================================================
-- inquire_asking_price_exp_ccn - 주식현재가 호가_예상체결 (FHKST01010200)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_asking_price_exp_ccn (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_aspr_acpt_hour TEXT NULL COMMENT '호가 접수 시간',
    rsp_askp1 TEXT NULL COMMENT '매도호가1',
    rsp_askp2 TEXT NULL COMMENT '매도호가2',
    rsp_askp3 TEXT NULL COMMENT '매도호가3',
    rsp_askp4 TEXT NULL COMMENT '매도호가4',
    rsp_askp5 TEXT NULL COMMENT '매도호가5',
    rsp_askp6 TEXT NULL COMMENT '매도호가6',
    rsp_askp7 TEXT NULL COMMENT '매도호가7',
    rsp_askp8 TEXT NULL COMMENT '매도호가8',
    rsp_askp9 TEXT NULL COMMENT '매도호가9',
    rsp_askp10 TEXT NULL COMMENT '매도호가10',
    rsp_bidp1 TEXT NULL COMMENT '매수호가1',
    rsp_bidp2 TEXT NULL COMMENT '매수호가2',
    rsp_bidp3 TEXT NULL COMMENT '매수호가3',
    rsp_bidp4 TEXT NULL COMMENT '매수호가4',
    rsp_bidp5 TEXT NULL COMMENT '매수호가5',
    rsp_bidp6 TEXT NULL COMMENT '매수호가6',
    rsp_bidp7 TEXT NULL COMMENT '매수호가7',
    rsp_bidp8 TEXT NULL COMMENT '매수호가8',
    rsp_bidp9 TEXT NULL COMMENT '매수호가9',
    rsp_bidp10 TEXT NULL COMMENT '매수호가10',
    rsp_askp_rsqn1 TEXT NULL COMMENT '매도호가 잔량1',
    rsp_askp_rsqn2 TEXT NULL COMMENT '매도호가 잔량2',
    rsp_askp_rsqn3 TEXT NULL COMMENT '매도호가 잔량3',
    rsp_askp_rsqn4 TEXT NULL COMMENT '매도호가 잔량4',
    rsp_askp_rsqn5 TEXT NULL COMMENT '매도호가 잔량5',
    rsp_askp_rsqn6 TEXT NULL COMMENT '매도호가 잔량6',
    rsp_askp_rsqn7 TEXT NULL COMMENT '매도호가 잔량7',
    rsp_askp_rsqn8 TEXT NULL COMMENT '매도호가 잔량8',
    rsp_askp_rsqn9 TEXT NULL COMMENT '매도호가 잔량9',
    rsp_askp_rsqn10 TEXT NULL COMMENT '매도호가 잔량10',
    rsp_bidp_rsqn1 TEXT NULL COMMENT '매수호가 잔량1',
    rsp_bidp_rsqn2 TEXT NULL COMMENT '매수호가 잔량2',
    rsp_bidp_rsqn3 TEXT NULL COMMENT '매수호가 잔량3',
    rsp_bidp_rsqn4 TEXT NULL COMMENT '매수호가 잔량4',
    rsp_bidp_rsqn5 TEXT NULL COMMENT '매수호가 잔량5',
    rsp_bidp_rsqn6 TEXT NULL COMMENT '매수호가 잔량6',
    rsp_bidp_rsqn7 TEXT NULL COMMENT '매수호가 잔량7',
    rsp_bidp_rsqn8 TEXT NULL COMMENT '매수호가 잔량8',
    rsp_bidp_rsqn9 TEXT NULL COMMENT '매수호가 잔량9',
    rsp_bidp_rsqn10 TEXT NULL COMMENT '매수호가 잔량10',
    rsp_askp_rsqn_icdc1 TEXT NULL COMMENT '매도호가 잔량 증감1',
    rsp_askp_rsqn_icdc2 TEXT NULL COMMENT '매도호가 잔량 증감2',
    rsp_askp_rsqn_icdc3 TEXT NULL COMMENT '매도호가 잔량 증감3',
    rsp_askp_rsqn_icdc4 TEXT NULL COMMENT '매도호가 잔량 증감4',
    rsp_askp_rsqn_icdc5 TEXT NULL COMMENT '매도호가 잔량 증감5',
    rsp_askp_rsqn_icdc6 TEXT NULL COMMENT '매도호가 잔량 증감6',
    rsp_askp_rsqn_icdc7 TEXT NULL COMMENT '매도호가 잔량 증감7',
    rsp_askp_rsqn_icdc8 TEXT NULL COMMENT '매도호가 잔량 증감8',
    rsp_askp_rsqn_icdc9 TEXT NULL COMMENT '매도호가 잔량 증감9',
    rsp_askp_rsqn_icdc10 TEXT NULL COMMENT '매도호가 잔량 증감10',
    rsp_bidp_rsqn_icdc1 TEXT NULL COMMENT '매수호가 잔량 증감1',
    rsp_bidp_rsqn_icdc2 TEXT NULL COMMENT '매수호가 잔량 증감2',
    rsp_bidp_rsqn_icdc3 TEXT NULL COMMENT '매수호가 잔량 증감3',
    rsp_bidp_rsqn_icdc4 TEXT NULL COMMENT '매수호가 잔량 증감4',
    rsp_bidp_rsqn_icdc5 TEXT NULL COMMENT '매수호가 잔량 증감5',
    rsp_bidp_rsqn_icdc6 TEXT NULL COMMENT '매수호가 잔량 증감6',
    rsp_bidp_rsqn_icdc7 TEXT NULL COMMENT '매수호가 잔량 증감7',
    rsp_bidp_rsqn_icdc8 TEXT NULL COMMENT '매수호가 잔량 증감8',
    rsp_bidp_rsqn_icdc9 TEXT NULL COMMENT '매수호가 잔량 증감9',
    rsp_bidp_rsqn_icdc10 TEXT NULL COMMENT '매수호가 잔량 증감10',
    rsp_total_askp_rsqn TEXT NULL COMMENT '총 매도호가 잔량',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '총 매수호가 잔량',
    rsp_total_askp_rsqn_icdc TEXT NULL COMMENT '총 매도호가 잔량 증감',
    rsp_total_bidp_rsqn_icdc TEXT NULL COMMENT '총 매수호가 잔량 증감',
    rsp_ovtm_total_askp_icdc TEXT NULL COMMENT '시간외 총 매도호가 증감',
    rsp_ovtm_total_bidp_icdc TEXT NULL COMMENT '시간외 총 매수호가 증감',
    rsp_ovtm_total_askp_rsqn TEXT NULL COMMENT '시간외 총 매도호가 잔량',
    rsp_ovtm_total_bidp_rsqn TEXT NULL COMMENT '시간외 총 매수호가 잔량',
    rsp_ntby_aspr_rsqn TEXT NULL COMMENT '순매수 호가 잔량',
    rsp_new_mkop_cls_code TEXT NULL COMMENT '신 장운영 구분 코드',
    rsp_antc_mkop_cls_code TEXT NULL COMMENT '예상 장운영 구분 코드',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_stck_sdpr TEXT NULL COMMENT '주식 기준가',
    rsp_antc_cnpr TEXT NULL COMMENT '예상 체결가',
    rsp_antc_cntg_vrss_sign TEXT NULL COMMENT '예상 체결 대비 부호',
    rsp_antc_cntg_vrss TEXT NULL COMMENT '예상 체결 대비',
    rsp_antc_cntg_prdy_ctrt TEXT NULL COMMENT '예상 체결 전일 대비율',
    rsp_antc_vol TEXT NULL COMMENT '예상 거래량',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식 단축 종목코드',
    rsp_vi_cls_code TEXT NULL COMMENT 'VI적용구분코드',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-asking-price-exp-ccn';

-- =============================================================
-- inquire_ccnl - 주식현재가 체결 (FHKST01010300)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-ccnl
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_ccnl (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    rsp_tday_rltv TEXT NULL COMMENT '당일 체결강도',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-ccnl';

-- =============================================================
-- inquire_member - 주식현재가 회원사 (FHKST01010600)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-member
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_member (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_seln_mbcr_no1 TEXT NULL COMMENT '매도 회원사 번호1',
    rsp_seln_mbcr_no2 TEXT NULL COMMENT '매도 회원사 번호2',
    rsp_seln_mbcr_no3 TEXT NULL COMMENT '매도 회원사 번호3',
    rsp_seln_mbcr_no4 TEXT NULL COMMENT '매도 회원사 번호4',
    rsp_seln_mbcr_no5 TEXT NULL COMMENT '매도 회원사 번호5',
    rsp_seln_mbcr_name1 TEXT NULL COMMENT '매도 회원사 명1',
    rsp_seln_mbcr_name2 TEXT NULL COMMENT '매도 회원사 명2',
    rsp_seln_mbcr_name3 TEXT NULL COMMENT '매도 회원사 명3',
    rsp_seln_mbcr_name4 TEXT NULL COMMENT '매도 회원사 명4',
    rsp_seln_mbcr_name5 TEXT NULL COMMENT '매도 회원사 명5',
    rsp_total_seln_qty1 TEXT NULL COMMENT '총 매도 수량1',
    rsp_total_seln_qty2 TEXT NULL COMMENT '총 매도 수량2',
    rsp_total_seln_qty3 TEXT NULL COMMENT '총 매도 수량3',
    rsp_total_seln_qty4 TEXT NULL COMMENT '총 매도 수량4',
    rsp_total_seln_qty5 TEXT NULL COMMENT '총 매도 수량5',
    rsp_seln_mbcr_rlim1 TEXT NULL COMMENT '매도 회원사 비중1',
    rsp_seln_mbcr_rlim2 TEXT NULL COMMENT '매도 회원사 비중2',
    rsp_seln_mbcr_rlim3 TEXT NULL COMMENT '매도 회원사 비중3',
    rsp_seln_mbcr_rlim4 TEXT NULL COMMENT '매도 회원사 비중4',
    rsp_seln_mbcr_rlim5 TEXT NULL COMMENT '매도 회원사 비중5',
    rsp_seln_qty_icdc1 TEXT NULL COMMENT '매도 수량 증감1',
    rsp_seln_qty_icdc2 TEXT NULL COMMENT '매도 수량 증감2',
    rsp_seln_qty_icdc3 TEXT NULL COMMENT '매도 수량 증감3',
    rsp_seln_qty_icdc4 TEXT NULL COMMENT '매도 수량 증감4',
    rsp_seln_qty_icdc5 TEXT NULL COMMENT '매도 수량 증감5',
    rsp_shnu_mbcr_no1 TEXT NULL COMMENT '매수2 회원사 번호1',
    rsp_shnu_mbcr_no2 TEXT NULL COMMENT '매수2 회원사 번호2',
    rsp_shnu_mbcr_no3 TEXT NULL COMMENT '매수2 회원사 번호3',
    rsp_shnu_mbcr_no4 TEXT NULL COMMENT '매수2 회원사 번호4',
    rsp_shnu_mbcr_no5 TEXT NULL COMMENT '매수2 회원사 번호5',
    rsp_shnu_mbcr_name1 TEXT NULL COMMENT '매수2 회원사 명1',
    rsp_shnu_mbcr_name2 TEXT NULL COMMENT '매수2 회원사 명2',
    rsp_shnu_mbcr_name3 TEXT NULL COMMENT '매수2 회원사 명3',
    rsp_shnu_mbcr_name4 TEXT NULL COMMENT '매수2 회원사 명4',
    rsp_shnu_mbcr_name5 TEXT NULL COMMENT '매수2 회원사 명5',
    rsp_total_shnu_qty1 TEXT NULL COMMENT '총 매수2 수량1',
    rsp_total_shnu_qty2 TEXT NULL COMMENT '총 매수2 수량2',
    rsp_total_shnu_qty3 TEXT NULL COMMENT '총 매수2 수량3',
    rsp_total_shnu_qty4 TEXT NULL COMMENT '총 매수2 수량4',
    rsp_total_shnu_qty5 TEXT NULL COMMENT '총 매수2 수량5',
    rsp_shnu_mbcr_rlim1 TEXT NULL COMMENT '매수2 회원사 비중1',
    rsp_shnu_mbcr_rlim2 TEXT NULL COMMENT '매수2 회원사 비중2',
    rsp_shnu_mbcr_rlim3 TEXT NULL COMMENT '매수2 회원사 비중3',
    rsp_shnu_mbcr_rlim4 TEXT NULL COMMENT '매수2 회원사 비중4',
    rsp_shnu_mbcr_rlim5 TEXT NULL COMMENT '매수2 회원사 비중5',
    rsp_shnu_qty_icdc1 TEXT NULL COMMENT '매수2 수량 증감1',
    rsp_shnu_qty_icdc2 TEXT NULL COMMENT '매수2 수량 증감2',
    rsp_shnu_qty_icdc3 TEXT NULL COMMENT '매수2 수량 증감3',
    rsp_shnu_qty_icdc4 TEXT NULL COMMENT '매수2 수량 증감4',
    rsp_shnu_qty_icdc5 TEXT NULL COMMENT '매수2 수량 증감5',
    rsp_glob_total_seln_qty TEXT NULL COMMENT '외국계 총 매도 수량',
    rsp_glob_seln_rlim TEXT NULL COMMENT '외국계 매도 비중',
    rsp_glob_ntby_qty TEXT NULL COMMENT '외국계 순매수 수량',
    rsp_glob_total_shnu_qty TEXT NULL COMMENT '외국계 총 매수2 수량',
    rsp_glob_shnu_rlim TEXT NULL COMMENT '외국계 매수2 비중',
    rsp_seln_mbcr_glob_yn_1 TEXT NULL COMMENT '매도 회원사 외국계 여부1',
    rsp_seln_mbcr_glob_yn_2 TEXT NULL COMMENT '매도 회원사 외국계 여부2',
    rsp_seln_mbcr_glob_yn_3 TEXT NULL COMMENT '매도 회원사 외국계 여부3',
    rsp_seln_mbcr_glob_yn_4 TEXT NULL COMMENT '매도 회원사 외국계 여부4',
    rsp_seln_mbcr_glob_yn_5 TEXT NULL COMMENT '매도 회원사 외국계 여부5',
    rsp_shnu_mbcr_glob_yn_1 TEXT NULL COMMENT '매수2 회원사 외국계 여부1',
    rsp_shnu_mbcr_glob_yn_2 TEXT NULL COMMENT '매수2 회원사 외국계 여부2',
    rsp_shnu_mbcr_glob_yn_3 TEXT NULL COMMENT '매수2 회원사 외국계 여부3',
    rsp_shnu_mbcr_glob_yn_4 TEXT NULL COMMENT '매수2 회원사 외국계 여부4',
    rsp_shnu_mbcr_glob_yn_5 TEXT NULL COMMENT '매수2 회원사 외국계 여부5',
    rsp_glob_total_seln_qty_icdc TEXT NULL COMMENT '외국계 총 매도 수량 증감',
    rsp_glob_total_shnu_qty_icdc TEXT NULL COMMENT '외국계 총 매수2 수량 증감',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-member';

-- =============================================================
-- inquire_investor - 주식현재가 투자자 (FHKST01010900)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-investor
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_investor (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '개인 순매수 수량',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '기관계 순매수 수량',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '개인 순매수 거래 대금',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '외국인 순매수 거래 대금',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '기관계 순매수 거래 대금',
    rsp_prsn_shnu_vol TEXT NULL COMMENT '개인 매수2 거래량',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '외국인 매수2 거래량',
    rsp_orgn_shnu_vol TEXT NULL COMMENT '기관계 매수2 거래량',
    rsp_prsn_shnu_tr_pbmn TEXT NULL COMMENT '개인 매수2 거래 대금',
    rsp_frgn_shnu_tr_pbmn TEXT NULL COMMENT '외국인 매수2 거래 대금',
    rsp_orgn_shnu_tr_pbmn TEXT NULL COMMENT '기관계 매수2 거래 대금',
    rsp_prsn_seln_vol TEXT NULL COMMENT '개인 매도 거래량',
    rsp_frgn_seln_vol TEXT NULL COMMENT '외국인 매도 거래량',
    rsp_orgn_seln_vol TEXT NULL COMMENT '기관계 매도 거래량',
    rsp_prsn_seln_tr_pbmn TEXT NULL COMMENT '개인 매도 거래 대금',
    rsp_frgn_seln_tr_pbmn TEXT NULL COMMENT '외국인 매도 거래 대금',
    rsp_orgn_seln_tr_pbmn TEXT NULL COMMENT '기관계 매도 거래 대금',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-investor';

-- =============================================================
-- exp_closing_price - 국내주식 장마감 예상체결가 (FHKST117300C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/exp-closing-price
-- =============================================================
CREATE TABLE IF NOT EXISTS exp_closing_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 순위 정렬 구분 코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건 화면 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_blng_cls_code TEXT NULL COMMENT '요청 소속 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식 단축 종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_sdpr_vrss_prpr TEXT NULL COMMENT '기준가 대비 현재가',
    rsp_sdpr_vrss_prpr_rate TEXT NULL COMMENT '기준가 대비 현재가 비율',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/exp-closing-price';

-- =============================================================
-- inquire_time_itemchartprice - 주식당일분봉조회 (FHKST03010200)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_time_itemchartprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력 시간1',
    req_fid_pw_data_incu_yn TEXT NULL COMMENT '요청 과거 데이터 포함 여부',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 기타 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '전일대비 종가',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래대금',
    rsp_hts_kor_isnm TEXT NULL COMMENT '한글 종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업일자',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결시간',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-time-itemchartprice';

-- =============================================================
-- inquire_elw_price - ELW 현재가 시세 (FHKEW15010000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-elw-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_elw_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_elw_shrn_iscd TEXT NULL COMMENT 'ELW 단축 종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_elw_prpr TEXT NULL COMMENT 'ELW 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '전일 대비 거래량 비율',
    rsp_unas_shrn_iscd TEXT NULL COMMENT '기초자산 단축 종목코드',
    rsp_unas_isnm TEXT NULL COMMENT '기초자산 종목명',
    rsp_unas_prpr TEXT NULL COMMENT '기초자산 현재가',
    rsp_unas_prdy_vrss TEXT NULL COMMENT '기초자산 전일 대비',
    rsp_unas_prdy_vrss_sign TEXT NULL COMMENT '기초자산 전일 대비 부호',
    rsp_unas_prdy_ctrt TEXT NULL COMMENT '기초자산 전일 대비율',
    rsp_bidp TEXT NULL COMMENT '매수호가',
    rsp_askp TEXT NULL COMMENT '매도호가',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_vol_tnrt TEXT NULL COMMENT '거래량 회전율',
    rsp_elw_oprc TEXT NULL COMMENT 'ELW 시가2',
    rsp_elw_hgpr TEXT NULL COMMENT 'ELW 최고가',
    rsp_elw_lwpr TEXT NULL COMMENT 'ELW 최저가',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식 전일 종가',
    rsp_hts_thpr TEXT NULL COMMENT 'HTS 이론가',
    rsp_dprt TEXT NULL COMMENT '괴리율',
    rsp_atm_cls_name TEXT NULL COMMENT 'ATM 구분 명',
    rsp_hts_ints_vltl TEXT NULL COMMENT 'HTS 내재 변동성',
    rsp_acpr TEXT NULL COMMENT '행사가',
    rsp_pvt_scnd_dmrs_prc TEXT NULL COMMENT '피벗 2차 디저항 가격',
    rsp_pvt_frst_dmrs_prc TEXT NULL COMMENT '피벗 1차 디저항 가격',
    rsp_pvt_pont_val TEXT NULL COMMENT '피벗 포인트 값',
    rsp_pvt_frst_dmsp_prc TEXT NULL COMMENT '피벗 1차 디지지 가격',
    rsp_pvt_scnd_dmsp_prc TEXT NULL COMMENT '피벗 2차 디지지 가격',
    rsp_dmsp_val TEXT NULL COMMENT '디지지 값',
    rsp_dmrs_val TEXT NULL COMMENT '디저항 값',
    rsp_elw_sdpr TEXT NULL COMMENT 'ELW 기준가',
    rsp_apprch_rate TEXT NULL COMMENT '접근도',
    rsp_tick_conv_prc TEXT NULL COMMENT '틱환산가',
    rsp_invt_epmd_cntt TEXT NULL COMMENT '투자 유의 내용',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-elw-price';

-- =============================================================
-- exp_index_trend - 국내주식 예상체결지수 추이 (FHPST01840000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/exp-index-trend
-- =============================================================
CREATE TABLE IF NOT EXISTS exp_index_trend (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_mkop_cls_code TEXT NULL COMMENT '요청 장운영 구분 코드',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력 시간1',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 단축 종목코드',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '주식 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비 부호',
    rsp_acml_vol TEXT NULL COMMENT '전일 대비율',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '기준가 대비 현재가',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/exp-index-trend';

-- =============================================================
-- inquire_daily_indexchartprice - 국내주식업종기간별시세(일_주_월_년) (FHKUP03500100)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_daily_indexchartprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 업종 상세코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 조회 시작일자',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 조회 종료일자',
    req_fid_period_div_code TEXT NULL COMMENT '요청 기간분류코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_prdy_nmix TEXT NULL COMMENT '전일 지수',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_cls_code TEXT NULL COMMENT '업종 구분 코드',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '업종 지수 시가2',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '업종 지수 최고가',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '업종 지수 최저가',
    rsp_futs_prdy_oprc TEXT NULL COMMENT '선물 전일 시가',
    rsp_futs_prdy_hgpr TEXT NULL COMMENT '선물 전일 최고가',
    rsp_futs_prdy_lwpr TEXT NULL COMMENT '선물 전일 최저가',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_mod_yn TEXT NULL COMMENT '변경 여부',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-daily-indexchartprice';

-- =============================================================
-- inquire_index_timeprice - 국내업종 시간별지수(분) (FHPUP02110200)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-index-timeprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_index_timeprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 ?입력 시간1',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_hour TEXT NULL COMMENT '영업 시간',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-index-timeprice';

-- =============================================================
-- inquire_index_category_price - 국내업종 구분별전체시세 (FHPUP02140000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-index-category-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_index_category_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID 조건 화면 분류 코드',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID 시장 구분 코드',
    req_fid_blng_cls_code TEXT NULL COMMENT '요청 FID 소속 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '업종 지수 시가2',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '업종 지수 최고가',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '업종 지수 최저가',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '상승 종목 수',
    rsp_down_issu_cnt TEXT NULL COMMENT '하락 종목 수',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '보합 종목 수',
    rsp_uplm_issu_cnt TEXT NULL COMMENT '상한 종목 수',
    rsp_lslm_issu_cnt TEXT NULL COMMENT '하한 종목 수',
    rsp_prdy_tr_pbmn TEXT NULL COMMENT '전일 거래 대금',
    rsp_dryy_bstp_nmix_hgpr_date TEXT NULL COMMENT '연중업종지수최고가일자',
    rsp_dryy_bstp_nmix_hgpr TEXT NULL COMMENT '연중업종지수최고가',
    rsp_dryy_bstp_nmix_lwpr TEXT NULL COMMENT '연중업종지수최저가',
    rsp_dryy_bstp_nmix_lwpr_date TEXT NULL COMMENT '연중업종지수최저가일자',
    rsp_bstp_cls_code TEXT NULL COMMENT '업종 구분 코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_acml_vol_rlim TEXT NULL COMMENT '누적 거래량 비중',
    rsp_acml_tr_pbmn_rlim TEXT NULL COMMENT '누적 거래 대금 비중',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-index-category-price';

-- =============================================================
-- inquire_time_indexchartprice - 업종 분봉조회 (FHKUP03500200)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-time-indexchartprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_time_indexchartprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID 기타 구분 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID 입력 시간1',
    req_fid_pw_data_incu_yn TEXT NULL COMMENT '요청 FID 과거 데이터 포함 여부',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_output1 TEXT NULL COMMENT '응답상세',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_prdy_nmix TEXT NULL COMMENT '전일 지수',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_cls_code TEXT NULL COMMENT '업종 구분 코드',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '업종 지수 시가2',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '업종 지수 최고가',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '업종 지수 최저가',
    rsp_futs_prdy_oprc TEXT NULL COMMENT '선물 전일 시가',
    rsp_futs_prdy_hgpr TEXT NULL COMMENT '선물 전일 최고가',
    rsp_futs_prdy_lwpr TEXT NULL COMMENT '선물 전일 최저가',
    rsp_output2 TEXT NULL COMMENT '응답상세2',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-time-indexchartprice';

-- =============================================================
-- chk_holiday - 국내휴장일조회 (CTCA0903R)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/chk-holiday
-- =============================================================
CREATE TABLE IF NOT EXISTS chk_holiday (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_bass_dt TEXT NULL COMMENT '요청 기준일자',
    req_ctx_area_nk TEXT NULL COMMENT '요청 연속조회키',
    req_ctx_area_fk TEXT NULL COMMENT '요청 연속조회검색조건',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bass_dt TEXT NULL COMMENT '기준일자',
    rsp_wday_dvsn_cd TEXT NULL COMMENT '요일구분코드',
    rsp_bzdy_yn TEXT NULL COMMENT '영업일여부',
    rsp_tr_day_yn TEXT NULL COMMENT '거래일여부',
    rsp_opnd_yn TEXT NULL COMMENT '개장일여부',
    rsp_sttl_day_yn TEXT NULL COMMENT '결제일여부',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/chk-holiday';

-- =============================================================
-- exp_total_index - 국내주식 예상체결 전체지수 (FHKUP11750000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/exp-total-index
-- =============================================================
CREATE TABLE IF NOT EXISTS exp_total_index (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 시장 구분 코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건 화면 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_mkop_cls_code TEXT NULL COMMENT '요청 장운영 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '상승 종목 수',
    rsp_down_issu_cnt TEXT NULL COMMENT '하락 종목 수',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '보합 종목 수',
    rsp_bstp_cls_code TEXT NULL COMMENT '업종 구분 코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_nmix_sdpr TEXT NULL COMMENT '지수 기준가',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/exp-total-index';

-- =============================================================
-- inquire_index_price - 국내업종 현재지수 (FHPUP02100000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-index-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_index_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_prdy_tr_pbmn TEXT NULL COMMENT '전일 거래 대금',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '업종 지수 시가2',
    rsp_prdy_nmix_vrss_nmix_oprc TEXT NULL COMMENT '전일 지수 대비 지수 시가2',
    rsp_oprc_vrss_prpr_sign TEXT NULL COMMENT '시가2 대비 현재가 부호',
    rsp_bstp_nmix_oprc_prdy_ctrt TEXT NULL COMMENT '업종 지수 시가2 전일 대비율',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '업종 지수 최고가',
    rsp_prdy_nmix_vrss_nmix_hgpr TEXT NULL COMMENT '전일 지수 대비 지수 최고가',
    rsp_hgpr_vrss_prpr_sign TEXT NULL COMMENT '최고가 대비 현재가 부호',
    rsp_bstp_nmix_hgpr_prdy_ctrt TEXT NULL COMMENT '업종 지수 최고가 전일 대비율',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '업종 지수 최저가',
    rsp_prdy_clpr_vrss_lwpr TEXT NULL COMMENT '전일 종가 대비 최저가',
    rsp_lwpr_vrss_prpr_sign TEXT NULL COMMENT '최저가 대비 현재가 부호',
    rsp_prdy_clpr_vrss_lwpr_rate TEXT NULL COMMENT '전일 종가 대비 최저가 비율',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '상승 종목 수',
    rsp_uplm_issu_cnt TEXT NULL COMMENT '상한 종목 수',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '보합 종목 수',
    rsp_down_issu_cnt TEXT NULL COMMENT '하락 종목 수',
    rsp_lslm_issu_cnt TEXT NULL COMMENT '하한 종목 수',
    rsp_dryy_bstp_nmix_hgpr TEXT NULL COMMENT '연중업종지수최고가',
    rsp_dryy_hgpr_vrss_prpr_rate TEXT NULL COMMENT '연중 최고가 대비 현재가 비율',
    rsp_dryy_bstp_nmix_hgpr_date TEXT NULL COMMENT '연중업종지수최고가일자',
    rsp_dryy_bstp_nmix_lwpr TEXT NULL COMMENT '연중업종지수최저가',
    rsp_dryy_lwpr_vrss_prpr_rate TEXT NULL COMMENT '연중 최저가 대비 현재가 비율',
    rsp_dryy_bstp_nmix_lwpr_date TEXT NULL COMMENT '연중업종지수최저가일자',
    rsp_total_askp_rsqn TEXT NULL COMMENT '총 매도호가 잔량',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '총 매수호가 잔량',
    rsp_seln_rsqn_rate TEXT NULL COMMENT '매도 잔량 비율',
    rsp_shnu_rsqn_rate TEXT NULL COMMENT '매수2 잔량 비율',
    rsp_ntby_rsqn TEXT NULL COMMENT '순매수 잔량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-index-price';

-- =============================================================
-- market_time - 국내선물 영업일조회 (HHMCM000002C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/market-time
-- =============================================================
CREATE TABLE IF NOT EXISTS market_time (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_date1 TEXT NULL COMMENT '영업일1',
    rsp_date2 TEXT NULL COMMENT '영업일2',
    rsp_date3 TEXT NULL COMMENT '영업일3',
    rsp_date4 TEXT NULL COMMENT '영업일4',
    rsp_date5 TEXT NULL COMMENT '영업일5',
    rsp_today TEXT NULL COMMENT '오늘일자',
    rsp_time TEXT NULL COMMENT '현재시간',
    rsp_s_time TEXT NULL COMMENT '장시작시간',
    rsp_e_time TEXT NULL COMMENT '장마감시간',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/market-time';

-- =============================================================
-- inquire_index_tickprice - 국내업종 시간별지수(초) (FHPUP02110100)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-index-tickprice
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_index_tickprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 시장 분류 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_cntg_vol TEXT NULL COMMENT '체결 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-index-tickprice';

-- =============================================================
-- inquire_index_daily_price - 국내업종 일자별지수 (FHPUP02120000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-index-daily-price
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_index_daily_price (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID 기간 분류 코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID 입력 날짜1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '업종 지수 시가2',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '업종 지수 최고가',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '업종 지수 최저가',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '상승 종목 수',
    rsp_down_issu_cnt TEXT NULL COMMENT '하락 종목 수',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '보합 종목 수',
    rsp_uplm_issu_cnt TEXT NULL COMMENT '상한 종목 수',
    rsp_lslm_issu_cnt TEXT NULL COMMENT '하한 종목 수',
    rsp_prdy_tr_pbmn TEXT NULL COMMENT '전일 거래 대금',
    rsp_dryy_bstp_nmix_hgpr_date TEXT NULL COMMENT '연중업종지수최고가일자',
    rsp_dryy_bstp_nmix_hgpr TEXT NULL COMMENT '연중업종지수최고가',
    rsp_dryy_bstp_nmix_lwpr TEXT NULL COMMENT '연중업종지수최저가',
    rsp_dryy_bstp_nmix_lwpr_date TEXT NULL COMMENT '연중업종지수최저가일자',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_acml_vol_rlim TEXT NULL COMMENT '누적 거래량 비중',
    rsp_invt_new_psdg TEXT NULL COMMENT '투자 신 심리도',
    rsp_d20_dsrt TEXT NULL COMMENT '20일 이격도',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-index-daily-price';

-- =============================================================
-- comp_interest - 금리 종합(국내채권_금리) (FHPST07020000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/comp-interest
-- =============================================================
CREATE TABLE IF NOT EXISTS comp_interest (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 분류구분코드',
    req_fid_div_cls_code1 TEXT NULL COMMENT '요청 분류구분코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bcdt_code TEXT NULL COMMENT '자료코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_bond_mnrt_prpr TEXT NULL COMMENT '채권금리현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_bond_mnrt_prdy_vrss TEXT NULL COMMENT '채권금리전일대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식영업일자',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종지수전일대비율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/comp-interest';

-- =============================================================
-- inquire_vi_status - 변동성완화장치(VI) 현황 (FHPST01390000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-vi-status
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_vi_status (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID 분류 구분 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID 조건 화면 분류 코드',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID 시장 구분 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 FID 순위 정렬 구분 코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID 입력 날짜1',
    req_fid_trgt_cls_code TEXT NULL COMMENT '요청 FID 대상 구분 코드',
    req_fid_trgt_exls_cls_code TEXT NULL COMMENT '요청 FID 대상 제외 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '유가증권 단축 종목코드',
    rsp_vi_cls_code TEXT NULL COMMENT 'VI발동상태',
    rsp_bsop_date TEXT NULL COMMENT '영업 일자',
    rsp_cntg_vi_hour TEXT NULL COMMENT 'VI발동시간',
    rsp_vi_cncl_hour TEXT NULL COMMENT 'VI해제시간',
    rsp_vi_kind_code TEXT NULL COMMENT 'VI종류코드',
    rsp_vi_prc TEXT NULL COMMENT 'VI발동가격',
    rsp_vi_stnd_prc TEXT NULL COMMENT '정적VI발동기준가격',
    rsp_vi_dprt TEXT NULL COMMENT '정적VI발동괴리율',
    rsp_vi_dmc_stnd_prc TEXT NULL COMMENT '동적VI발동기준가격',
    rsp_vi_dmc_dprt TEXT NULL COMMENT '동적VI발동괴리율',
    rsp_vi_count TEXT NULL COMMENT 'VI발동횟수',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-vi-status';

-- =============================================================
-- news_title - 종합 시황_공시(제목) (FHKST01011800)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/news-title
-- =============================================================
CREATE TABLE IF NOT EXISTS news_title (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_news_ofer_entp_code TEXT NULL COMMENT '요청 뉴스 제공 업체 코드',
    req_fid_cond_mrkt_cls_code TEXT NULL COMMENT '요청 조건 시장 구분 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_titl_cntt TEXT NULL COMMENT '요청 제목 내용',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력 시간',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 순위 정렬 구분 코드',
    req_fid_input_srno TEXT NULL COMMENT '요청 입력 일련번호',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_cntt_usiq_srno TEXT NULL COMMENT '내용 조회용 일련번호',
    rsp_news_ofer_entp_code TEXT NULL COMMENT '뉴스 제공 업체 코드',
    rsp_data_dt TEXT NULL COMMENT '작성일자',
    rsp_data_tm TEXT NULL COMMENT '작성시간',
    rsp_hts_pbnt_titl_cntt TEXT NULL COMMENT 'HTS 공시 제목 내용',
    rsp_news_lrdv_code TEXT NULL COMMENT '뉴스 대구분',
    rsp_dorg TEXT NULL COMMENT '자료원',
    rsp_iscd1 TEXT NULL COMMENT '종목 코드1',
    rsp_iscd2 TEXT NULL COMMENT '종목 코드2',
    rsp_iscd3 TEXT NULL COMMENT '종목 코드3',
    rsp_iscd4 TEXT NULL COMMENT '종목 코드4',
    rsp_iscd5 TEXT NULL COMMENT '종목 코드5',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/news-title';

-- =============================================================
-- search_info - 상품기본조회 (CTPF1604R)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/search-info
-- =============================================================
CREATE TABLE IF NOT EXISTS search_info (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_pdno TEXT NULL COMMENT '요청 상품번호',
    req_prdt_type_cd TEXT NULL COMMENT '요청 상품유형코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_pdno TEXT NULL COMMENT '상품번호',
    rsp_prdt_type_cd TEXT NULL COMMENT '상품유형코드',
    rsp_prdt_name TEXT NULL COMMENT '상품명',
    rsp_prdt_name120 TEXT NULL COMMENT '상품명120',
    rsp_prdt_abrv_name TEXT NULL COMMENT '상품약어명',
    rsp_prdt_eng_name TEXT NULL COMMENT '상품영문명',
    rsp_prdt_eng_name120 TEXT NULL COMMENT '상품영문명120',
    rsp_prdt_eng_abrv_name TEXT NULL COMMENT '상품영문약어명',
    rsp_std_pdno TEXT NULL COMMENT '표준상품번호',
    rsp_shtn_pdno TEXT NULL COMMENT '단축상품번호',
    rsp_prdt_sale_stat_cd TEXT NULL COMMENT '상품판매상태코드',
    rsp_prdt_risk_grad_cd TEXT NULL COMMENT '상품위험등급코드',
    rsp_prdt_clsf_cd TEXT NULL COMMENT '상품분류코드',
    rsp_prdt_clsf_name TEXT NULL COMMENT '상품분류명',
    rsp_sale_strt_dt TEXT NULL COMMENT '판매시작일자',
    rsp_sale_end_dt TEXT NULL COMMENT '판매종료일자',
    rsp_wrap_asst_type_cd TEXT NULL COMMENT '랩어카운트자산유형코드',
    rsp_ivst_prdt_type_cd TEXT NULL COMMENT '투자상품유형코드',
    rsp_ivst_prdt_type_cd_name TEXT NULL COMMENT '투자상품유형코드명',
    rsp_frst_erlm_dt TEXT NULL COMMENT '최초등록일자',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/search-info';

-- =============================================================
-- invest_opbysec - 국내주식 증권사별 투자의견 (FHKST663400C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/invest-opbysec
-- =============================================================
CREATE TABLE IF NOT EXISTS invest_opbysec (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 분류구분코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력날짜1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 입력날짜2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식영업일자',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식단축종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_invt_opnn TEXT NULL COMMENT '투자의견',
    rsp_invt_opnn_cls_code TEXT NULL COMMENT '투자의견구분코드',
    rsp_rgbf_invt_opnn TEXT NULL COMMENT '직전투자의견',
    rsp_rgbf_invt_opnn_cls_code TEXT NULL COMMENT '직전투자의견구분코드',
    rsp_mbcr_name TEXT NULL COMMENT '회원사명',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_hts_goal_prc TEXT NULL COMMENT 'HTS목표가격',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식전일종가',
    rsp_stft_esdg TEXT NULL COMMENT '주식선물괴리도',
    rsp_dprt TEXT NULL COMMENT '괴리율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/invest-opbysec';

-- =============================================================
-- credit_by_company - 국내주식 당사 신용가능종목 (FHPST04770000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/credit-by-company
-- =============================================================
CREATE TABLE IF NOT EXISTS credit_by_company (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 순위 정렬 구분 코드',
    req_fid_slct_yn TEXT NULL COMMENT '요청 선택 여부',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건 화면 분류 코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식 단축 종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_crdt_rate TEXT NULL COMMENT '신용 비율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/credit-by-company';

-- =============================================================
-- invest_opinion - 국내주식 종목투자의견 (FHKST663300C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/invest-opinion
-- =============================================================
CREATE TABLE IF NOT EXISTS invest_opinion (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력날짜1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 입력날짜2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식영업일자',
    rsp_invt_opnn TEXT NULL COMMENT '투자의견',
    rsp_invt_opnn_cls_code TEXT NULL COMMENT '투자의견구분코드',
    rsp_rgbf_invt_opnn TEXT NULL COMMENT '직전투자의견',
    rsp_rgbf_invt_opnn_cls_code TEXT NULL COMMENT '직전투자의견구분코드',
    rsp_mbcr_name TEXT NULL COMMENT '회원사명',
    rsp_hts_goal_prc TEXT NULL COMMENT 'HTS목표가격',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식전일종가',
    rsp_stck_nday_esdg TEXT NULL COMMENT '주식N일괴리도',
    rsp_nday_dprt TEXT NULL COMMENT 'N일괴리율',
    rsp_stft_esdg TEXT NULL COMMENT '주식선물괴리도',
    rsp_dprt TEXT NULL COMMENT '괴리율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/invest-opinion';

-- =============================================================
-- lendable_by_company - 당사 대주가능 종목 (CTSC2702R)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/lendable-by-company
-- =============================================================
CREATE TABLE IF NOT EXISTS lendable_by_company (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_excg_dvsn_cd TEXT NULL COMMENT '요청 거래소구분코드',
    req_pdno TEXT NULL COMMENT '요청 상품번호',
    req_thco_stln_psbl_yn TEXT NULL COMMENT '요청 당사대주가능여부',
    req_inqr_dvsn_1 TEXT NULL COMMENT '요청 조회구분1',
    req_ctx_area_fk200 TEXT NULL COMMENT '요청 연속조회검색조건200',
    req_ctx_area_nk100 TEXT NULL COMMENT '요청 연속조회키100',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_pdno TEXT NULL COMMENT '상품번호',
    rsp_prdt_name TEXT NULL COMMENT '상품명',
    rsp_papr TEXT NULL COMMENT '액면가',
    rsp_bfdy_clpr TEXT NULL COMMENT '전일종가',
    rsp_sbst_prvs TEXT NULL COMMENT '대용가',
    rsp_tr_stop_dvsn_name TEXT NULL COMMENT '거래정지구분명',
    rsp_psbl_yn_name TEXT NULL COMMENT '가능여부명',
    rsp_lmt_qty1 TEXT NULL COMMENT '한도수량1',
    rsp_use_qty1 TEXT NULL COMMENT '사용수량1',
    rsp_trad_psbl_qty2 TEXT NULL COMMENT '매매가능수량2',
    rsp_rght_type_cd TEXT NULL COMMENT '권리유형코드',
    rsp_bass_dt TEXT NULL COMMENT '기준일자',
    rsp_psbl_yn TEXT NULL COMMENT '가능여부',
    rsp_tot_stup_lmt_qty TEXT NULL COMMENT '총설정한도수량',
    rsp_brch_lmt_qty TEXT NULL COMMENT '지점한도수량',
    rsp_rqst_psbl_qty TEXT NULL COMMENT '신청가능수량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/lendable-by-company';

-- =============================================================
-- search_stock_info - 주식기본조회 (CTPF1002R)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/search-stock-info
-- =============================================================
CREATE TABLE IF NOT EXISTS search_stock_info (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_prdt_type_cd TEXT NULL COMMENT '요청 상품유형코드',
    req_pdno TEXT NULL COMMENT '요청 상품번호',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_pdno TEXT NULL COMMENT '상품번호',
    rsp_prdt_type_cd TEXT NULL COMMENT '상품유형코드',
    rsp_mket_id_cd TEXT NULL COMMENT '시장ID코드',
    rsp_scty_grp_id_cd TEXT NULL COMMENT '증권그룹ID코드',
    rsp_excg_dvsn_cd TEXT NULL COMMENT '거래소구분코드',
    rsp_setl_mmdd TEXT NULL COMMENT '결산월일',
    rsp_lstg_stqt TEXT NULL COMMENT '상장주수',
    rsp_lstg_cptl_amt TEXT NULL COMMENT '상장자본금액',
    rsp_cpta TEXT NULL COMMENT '자본금',
    rsp_papr TEXT NULL COMMENT '액면가',
    rsp_issu_pric TEXT NULL COMMENT '발행가격',
    rsp_kospi200_item_yn TEXT NULL COMMENT '코스피200종목여부',
    rsp_scts_mket_lstg_dt TEXT NULL COMMENT '유가증권시장상장일자',
    rsp_scts_mket_lstg_abol_dt TEXT NULL COMMENT '유가증권시장상장폐지일자',
    rsp_kosdaq_mket_lstg_dt TEXT NULL COMMENT '코스닥시장상장일자',
    rsp_kosdaq_mket_lstg_abol_dt TEXT NULL COMMENT '코스닥시장상장폐지일자',
    rsp_frbd_mket_lstg_dt TEXT NULL COMMENT '프리보드시장상장일자',
    rsp_frbd_mket_lstg_abol_dt TEXT NULL COMMENT '프리보드시장상장폐지일자',
    rsp_reits_kind_cd TEXT NULL COMMENT '리츠종류코드',
    rsp_etf_dvsn_cd TEXT NULL COMMENT 'ETF구분코드',
    rsp_oilf_fund_yn TEXT NULL COMMENT '유전펀드여부',
    rsp_idx_bztp_lcls_cd TEXT NULL COMMENT '지수업종대분류코드',
    rsp_idx_bztp_mcls_cd TEXT NULL COMMENT '지수업종중분류코드',
    rsp_idx_bztp_scls_cd TEXT NULL COMMENT '지수업종소분류코드',
    rsp_stck_kind_cd TEXT NULL COMMENT '주식종류코드',
    rsp_mfnd_opng_dt TEXT NULL COMMENT '뮤추얼펀드개시일자',
    rsp_mfnd_end_dt TEXT NULL COMMENT '뮤추얼펀드종료일자',
    rsp_dpsi_erlm_cncl_dt TEXT NULL COMMENT '예탁등록취소일자',
    rsp_etf_cu_qty TEXT NULL COMMENT 'ETFCU수량',
    rsp_prdt_name TEXT NULL COMMENT '상품명',
    rsp_prdt_name120 TEXT NULL COMMENT '상품명120',
    rsp_prdt_abrv_name TEXT NULL COMMENT '상품약어명',
    rsp_std_pdno TEXT NULL COMMENT '표준상품번호',
    rsp_prdt_eng_name TEXT NULL COMMENT '상품영문명',
    rsp_prdt_eng_name120 TEXT NULL COMMENT '상품영문명120',
    rsp_prdt_eng_abrv_name TEXT NULL COMMENT '상품영문약어명',
    rsp_dpsi_aptm_erlm_yn TEXT NULL COMMENT '예탁지정등록여부',
    rsp_etf_txtn_type_cd TEXT NULL COMMENT 'ETF과세유형코드',
    rsp_etf_type_cd TEXT NULL COMMENT 'ETF유형코드',
    rsp_lstg_abol_dt TEXT NULL COMMENT '상장폐지일자',
    rsp_nwst_odst_dvsn_cd TEXT NULL COMMENT '신주구주구분코드',
    rsp_sbst_pric TEXT NULL COMMENT '대용가격',
    rsp_thco_sbst_pric TEXT NULL COMMENT '당사대용가격',
    rsp_thco_sbst_pric_chng_dt TEXT NULL COMMENT '당사대용가격변경일자',
    rsp_tr_stop_yn TEXT NULL COMMENT '거래정지여부',
    rsp_admn_item_yn TEXT NULL COMMENT '관리종목여부',
    rsp_thdt_clpr TEXT NULL COMMENT '당일종가',
    rsp_bfdy_clpr TEXT NULL COMMENT '전일종가',
    rsp_clpr_chng_dt TEXT NULL COMMENT '종가변경일자',
    rsp_std_idst_clsf_cd TEXT NULL COMMENT '표준산업분류코드',
    rsp_std_idst_clsf_cd_name TEXT NULL COMMENT '표준산업분류코드명',
    rsp_idx_bztp_lcls_cd_name TEXT NULL COMMENT '지수업종대분류코드명',
    rsp_idx_bztp_mcls_cd_name TEXT NULL COMMENT '지수업종중분류코드명',
    rsp_idx_bztp_scls_cd_name TEXT NULL COMMENT '지수업종소분류코드명',
    rsp_ocr_no TEXT NULL COMMENT 'OCR번호',
    rsp_crfd_item_yn TEXT NULL COMMENT '크라우드펀딩종목여부',
    rsp_elec_scty_yn TEXT NULL COMMENT '전자증권여부',
    rsp_issu_istt_cd TEXT NULL COMMENT '발행기관코드',
    rsp_etf_chas_erng_rt_dbnb TEXT NULL COMMENT 'ETF추적수익율배수',
    rsp_etf_etn_ivst_heed_item_yn TEXT NULL COMMENT 'ETFETN투자유의종목여부',
    rsp_stln_int_rt_dvsn_cd TEXT NULL COMMENT '대주이자율구분코드',
    rsp_frnr_psnl_lmt_rt TEXT NULL COMMENT '외국인개인한도비율',
    rsp_lstg_rqsr_issu_istt_cd TEXT NULL COMMENT '상장신청인발행기관코드',
    rsp_lstg_rqsr_item_cd TEXT NULL COMMENT '상장신청인종목코드',
    rsp_trst_istt_issu_istt_cd TEXT NULL COMMENT '신탁기관발행기관코드',
    rsp_cptt_trad_tr_psbl_yn TEXT NULL COMMENT 'NXT 거래종목여부',
    rsp_nxt_tr_stop_yn TEXT NULL COMMENT 'NXT 거래정지여부',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/search-stock-info';

-- =============================================================
-- estimate_perform - 국내주식 종목추정실적 (HHKST668300C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/estimate-perform
-- =============================================================
CREATE TABLE IF NOT EXISTS estimate_perform (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_sht_cd TEXT NULL COMMENT '요청 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_sht_cd TEXT NULL COMMENT 'ELW단축종목코드',
    rsp_item_kor_nm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_name1 TEXT NULL COMMENT 'ELW현재가',
    rsp_name2 TEXT NULL COMMENT '전일대비',
    rsp_estdate TEXT NULL COMMENT '전일대비부호',
    rsp_rcmd_name TEXT NULL COMMENT '전일대비율',
    rsp_capital TEXT NULL COMMENT '누적거래량',
    rsp_forn_item_lmtrt TEXT NULL COMMENT '행사가',
    rsp_data1 TEXT NULL COMMENT 'DATA1',
    rsp_data2 TEXT NULL COMMENT 'DATA2',
    rsp_data3 TEXT NULL COMMENT 'DATA3',
    rsp_data4 TEXT NULL COMMENT 'DATA4',
    rsp_data5 TEXT NULL COMMENT 'DATA5',
    rsp_output3 TEXT NULL COMMENT '응답상세',
    rsp_output4 TEXT NULL COMMENT '응답상세',
    rsp_dt TEXT NULL COMMENT '결산년월',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/estimate-perform';

-- =============================================================
-- comp_program_trade_today - 프로그램매매 종합현황(시간) (FHPPG04600101)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/comp-program-trade-today
-- =============================================================
CREATE TABLE IF NOT EXISTS comp_program_trade_today (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 시장 분류 코드',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 시장 구분 코드',
    req_fid_sctn_cls_code TEXT NULL COMMENT '요청 구간 구분 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_cond_mrkt_div_code1 TEXT NULL COMMENT '요청 시장 분류코드1',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력 시간1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_hour TEXT NULL COMMENT '영업 시간',
    rsp_arbt_smtn_seln_tr_pbmn TEXT NULL COMMENT '차익 합계 매도 거래 대금',
    rsp_arbt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '차익 합계 매도 거래대금 비율',
    rsp_arbt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '차익 합계 매수2 거래 대금',
    rsp_arbt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '차익합계매수거래대금비율',
    rsp_nabt_smtn_seln_tr_pbmn TEXT NULL COMMENT '비차익 합계 매도 거래 대금',
    rsp_nabt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '비차익 합계 매도 거래대금 비율',
    rsp_nabt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '비차익 합계 매수2 거래 대금',
    rsp_nabt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '비차익합계매수거래대금비율',
    rsp_arbt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '차익 합계 순매수 거래 대금',
    rsp_arbt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '차익 합계 순매수 거래대금 비율',
    rsp_nabt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '비차익 합계 순매수 거래 대금',
    rsp_nabt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '비차익 합계 순매수 거래대금 비',
    rsp_whol_smtn_ntby_tr_pbmn TEXT NULL COMMENT '전체 합계 순매수 거래 대금',
    rsp_whol_ntby_tr_pbmn_rate TEXT NULL COMMENT '전체 순매수 거래대금 비율',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/comp-program-trade-today';

-- =============================================================
-- daily_credit_balance - 국내주식 신용잔고 일별추이 (FHPST04760000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/daily-credit-balance
-- =============================================================
CREATE TABLE IF NOT EXISTS daily_credit_balance (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 시장 분류 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 화면 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 결제일자',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_deal_date TEXT NULL COMMENT '매매 일자',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_stlm_date TEXT NULL COMMENT '결제 일자',
    rsp_whol_loan_new_stcn TEXT NULL COMMENT '전체 융자 신규 주수',
    rsp_whol_loan_rdmp_stcn TEXT NULL COMMENT '전체 융자 상환 주수',
    rsp_whol_loan_rmnd_stcn TEXT NULL COMMENT '전체 융자 잔고 주수',
    rsp_whol_loan_new_amt TEXT NULL COMMENT '전체 융자 신규 금액',
    rsp_whol_loan_rdmp_amt TEXT NULL COMMENT '전체 융자 상환 금액',
    rsp_whol_loan_rmnd_amt TEXT NULL COMMENT '전체 융자 잔고 금액',
    rsp_whol_loan_rmnd_rate TEXT NULL COMMENT '전체 융자 잔고 비율',
    rsp_whol_loan_gvrt TEXT NULL COMMENT '전체 융자 공여율',
    rsp_whol_stln_new_stcn TEXT NULL COMMENT '전체 대주 신규 주수',
    rsp_whol_stln_rdmp_stcn TEXT NULL COMMENT '전체 대주 상환 주수',
    rsp_whol_stln_rmnd_stcn TEXT NULL COMMENT '전체 대주 잔고 주수',
    rsp_whol_stln_new_amt TEXT NULL COMMENT '전체 대주 신규 금액',
    rsp_whol_stln_rdmp_amt TEXT NULL COMMENT '전체 대주 상환 금액',
    rsp_whol_stln_rmnd_amt TEXT NULL COMMENT '전체 대주 잔고 금액',
    rsp_whol_stln_rmnd_rate TEXT NULL COMMENT '전체 대주 잔고 비율',
    rsp_whol_stln_gvrt TEXT NULL COMMENT '전체 대주 공여율',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/daily-credit-balance';

-- =============================================================
-- inquire_investor_daily_by_market - 시장별 투자자매매동향(일별) (FHPTJ04040000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-investor-daily-by-market
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_investor_daily_by_market (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜1',
    req_fid_input_iscd_1 TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 입력 날짜2',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 하위 분류코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종 지수 현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종 지수 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '업종 지수 전일 대비율',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '업종 지수 시가2',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '업종 지수 최고가',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '업종 지수 최저가',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '주식 전일 종가',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_frgn_reg_ntby_qty TEXT NULL COMMENT '외국인 등록 순매수 수량',
    rsp_frgn_nreg_ntby_qty TEXT NULL COMMENT '외국인 비등록 순매수 수량',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '개인 순매수 수량',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '기관계 순매수 수량',
    rsp_scrt_ntby_qty TEXT NULL COMMENT '증권 순매수 수량',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '투자신탁 순매수 수량',
    rsp_pe_fund_ntby_vol TEXT NULL COMMENT '사모 펀드 순매수 거래량',
    rsp_bank_ntby_qty TEXT NULL COMMENT '은행 순매수 수량',
    rsp_insu_ntby_qty TEXT NULL COMMENT '보험 순매수 수량',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '종금 순매수 수량',
    rsp_fund_ntby_qty TEXT NULL COMMENT '기금 순매수 수량',
    rsp_etc_ntby_qty TEXT NULL COMMENT '기타 순매수 수량',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '기타 단체 순매수 거래량',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '기타 법인 순매수 거래량',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '외국인 순매수 거래 대금',
    rsp_frgn_reg_ntby_pbmn TEXT NULL COMMENT '외국인 등록 순매수 대금',
    rsp_frgn_nreg_ntby_pbmn TEXT NULL COMMENT '외국인 비등록 순매수 대금',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '개인 순매수 거래 대금',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '기관계 순매수 거래 대금',
    rsp_scrt_ntby_tr_pbmn TEXT NULL COMMENT '증권 순매수 거래 대금',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '투자신탁 순매수 거래 대금',
    rsp_pe_fund_ntby_tr_pbmn TEXT NULL COMMENT '사모 펀드 순매수 거래 대금',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '은행 순매수 거래 대금',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '보험 순매수 거래 대금',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '종금 순매수 거래 대금',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '기금 순매수 거래 대금',
    rsp_etc_ntby_tr_pbmn TEXT NULL COMMENT '기타 순매수 거래 대금',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '기타 단체 순매수 거래 대금',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '기타 법인 순매수 거래 대금',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-investor-daily-by-market';

-- =============================================================
-- daily_short_sale - 국내주식 공매도 일별추이 (FHPST04830000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/daily-short-sale
-- =============================================================
CREATE TABLE IF NOT EXISTS daily_short_sale (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 입력 날짜2',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_stnd_vol_smtn TEXT NULL COMMENT '기준 거래량 합계',
    rsp_ssts_cntg_qty TEXT NULL COMMENT '공매도 체결 수량',
    rsp_ssts_vol_rlim TEXT NULL COMMENT '공매도 거래량 비중',
    rsp_acml_ssts_cntg_qty TEXT NULL COMMENT '누적 공매도 체결 수량',
    rsp_acml_ssts_cntg_qty_rlim TEXT NULL COMMENT '누적 공매도 체결 수량 비중',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_stnd_tr_pbmn_smtn TEXT NULL COMMENT '기준 거래대금 합계',
    rsp_ssts_tr_pbmn TEXT NULL COMMENT '공매도 거래 대금',
    rsp_ssts_tr_pbmn_rlim TEXT NULL COMMENT '공매도 거래대금 비중',
    rsp_acml_ssts_tr_pbmn TEXT NULL COMMENT '누적 공매도 거래 대금',
    rsp_acml_ssts_tr_pbmn_rlim TEXT NULL COMMENT '누적 공매도 거래 대금 비중',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_avrg_prc TEXT NULL COMMENT '평균가격',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/daily-short-sale';

-- =============================================================
-- investor_trade_by_stock_daily - 종목별 투자자매매동향(일별) (FHPTJ04160001)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/investor-trade-by-stock-daily
-- =============================================================
CREATE TABLE IF NOT EXISTS investor_trade_by_stock_daily (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜1',
    req_fid_org_adj_prc TEXT NULL COMMENT '요청 수정주가 원주가 가격',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 기타 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표 시장 한글 명',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_stck_oprc TEXT NULL COMMENT '주식 시가2',
    rsp_stck_hgpr TEXT NULL COMMENT '주식 최고가',
    rsp_stck_lwpr TEXT NULL COMMENT '주식 최저가',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_frgn_reg_ntby_qty TEXT NULL COMMENT '외국인 등록 순매수 수량',
    rsp_frgn_nreg_ntby_qty TEXT NULL COMMENT '외국인 비등록 순매수 수량',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '개인 순매수 수량',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '기관계 순매수 수량',
    rsp_scrt_ntby_qty TEXT NULL COMMENT '증권 순매수 수량',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '투자신탁 순매수 수량',
    rsp_pe_fund_ntby_vol TEXT NULL COMMENT '사모 펀드 순매수 거래량',
    rsp_bank_ntby_qty TEXT NULL COMMENT '은행 순매수 수량',
    rsp_insu_ntby_qty TEXT NULL COMMENT '보험 순매수 수량',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '종금 순매수 수량',
    rsp_fund_ntby_qty TEXT NULL COMMENT '기금 순매수 수량',
    rsp_etc_ntby_qty TEXT NULL COMMENT '기타 순매수 수량',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '기타 법인 순매수 거래량',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '기타 단체 순매수 거래량',
    rsp_frgn_reg_ntby_pbmn TEXT NULL COMMENT '외국인 등록 순매수 대금',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '외국인 순매수 거래 대금',
    rsp_frgn_nreg_ntby_pbmn TEXT NULL COMMENT '외국인 비등록 순매수 대금',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '개인 순매수 거래 대금',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '기관계 순매수 거래 대금',
    rsp_scrt_ntby_tr_pbmn TEXT NULL COMMENT '증권 순매수 거래 대금',
    rsp_pe_fund_ntby_tr_pbmn TEXT NULL COMMENT '사모 펀드 순매수 거래 대금',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '투자신탁 순매수 거래 대금',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '은행 순매수 거래 대금',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '보험 순매수 거래 대금',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '종금 순매수 거래 대금',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '기금 순매수 거래 대금',
    rsp_etc_ntby_tr_pbmn TEXT NULL COMMENT '기타 순매수 거래 대금',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '기타 법인 순매수 거래 대금',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '기타 단체 순매수 거래 대금',
    rsp_frgn_seln_vol TEXT NULL COMMENT '외국인 매도 거래량',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '외국인 매수2 거래량',
    rsp_frgn_seln_tr_pbmn TEXT NULL COMMENT '외국인 매도 거래 대금',
    rsp_frgn_shnu_tr_pbmn TEXT NULL COMMENT '외국인 매수2 거래 대금',
    rsp_frgn_reg_askp_qty TEXT NULL COMMENT '외국인 등록 매도 수량',
    rsp_frgn_reg_bidp_qty TEXT NULL COMMENT '외국인 등록 매수 수량',
    rsp_frgn_reg_askp_pbmn TEXT NULL COMMENT '외국인 등록 매도 대금',
    rsp_frgn_reg_bidp_pbmn TEXT NULL COMMENT '외국인 등록 매수 대금',
    rsp_frgn_nreg_askp_qty TEXT NULL COMMENT '외국인 비등록 매도 수량',
    rsp_frgn_nreg_bidp_qty TEXT NULL COMMENT '외국인 비등록 매수 수량',
    rsp_frgn_nreg_askp_pbmn TEXT NULL COMMENT '외국인 비등록 매도 대금',
    rsp_frgn_nreg_bidp_pbmn TEXT NULL COMMENT '외국인 비등록 매수 대금',
    rsp_prsn_seln_vol TEXT NULL COMMENT '개인 매도 거래량',
    rsp_prsn_shnu_vol TEXT NULL COMMENT '개인 매수2 거래량',
    rsp_prsn_seln_tr_pbmn TEXT NULL COMMENT '개인 매도 거래 대금',
    rsp_prsn_shnu_tr_pbmn TEXT NULL COMMENT '개인 매수2 거래 대금',
    rsp_orgn_seln_vol TEXT NULL COMMENT '기관계 매도 거래량',
    rsp_orgn_shnu_vol TEXT NULL COMMENT '기관계 매수2 거래량',
    rsp_orgn_seln_tr_pbmn TEXT NULL COMMENT '기관계 매도 거래 대금',
    rsp_orgn_shnu_tr_pbmn TEXT NULL COMMENT '기관계 매수2 거래 대금',
    rsp_scrt_seln_vol TEXT NULL COMMENT '증권 매도 거래량',
    rsp_scrt_shnu_vol TEXT NULL COMMENT '증권 매수2 거래량',
    rsp_scrt_seln_tr_pbmn TEXT NULL COMMENT '증권 매도 거래 대금',
    rsp_scrt_shnu_tr_pbmn TEXT NULL COMMENT '증권 매수2 거래 대금',
    rsp_ivtr_seln_vol TEXT NULL COMMENT '투자신탁 매도 거래량',
    rsp_ivtr_shnu_vol TEXT NULL COMMENT '투자신탁 매수2 거래량',
    rsp_ivtr_seln_tr_pbmn TEXT NULL COMMENT '투자신탁 매도 거래 대금',
    rsp_ivtr_shnu_tr_pbmn TEXT NULL COMMENT '투자신탁 매수2 거래 대금',
    rsp_pe_fund_seln_tr_pbmn TEXT NULL COMMENT '사모 펀드 매도 거래 대금',
    rsp_pe_fund_seln_vol TEXT NULL COMMENT '사모 펀드 매도 거래량',
    rsp_pe_fund_shnu_tr_pbmn TEXT NULL COMMENT '사모 펀드 매수2 거래 대금',
    rsp_pe_fund_shnu_vol TEXT NULL COMMENT '사모 펀드 매수2 거래량',
    rsp_bank_seln_vol TEXT NULL COMMENT '은행 매도 거래량',
    rsp_bank_shnu_vol TEXT NULL COMMENT '은행 매수2 거래량',
    rsp_bank_seln_tr_pbmn TEXT NULL COMMENT '은행 매도 거래 대금',
    rsp_bank_shnu_tr_pbmn TEXT NULL COMMENT '은행 매수2 거래 대금',
    rsp_insu_seln_vol TEXT NULL COMMENT '보험 매도 거래량',
    rsp_insu_shnu_vol TEXT NULL COMMENT '보험 매수2 거래량',
    rsp_insu_seln_tr_pbmn TEXT NULL COMMENT '보험 매도 거래 대금',
    rsp_insu_shnu_tr_pbmn TEXT NULL COMMENT '보험 매수2 거래 대금',
    rsp_mrbn_seln_vol TEXT NULL COMMENT '종금 매도 거래량',
    rsp_mrbn_shnu_vol TEXT NULL COMMENT '종금 매수2 거래량',
    rsp_mrbn_seln_tr_pbmn TEXT NULL COMMENT '종금 매도 거래 대금',
    rsp_mrbn_shnu_tr_pbmn TEXT NULL COMMENT '종금 매수2 거래 대금',
    rsp_fund_seln_vol TEXT NULL COMMENT '기금 매도 거래량',
    rsp_fund_shnu_vol TEXT NULL COMMENT '기금 매수2 거래량',
    rsp_fund_seln_tr_pbmn TEXT NULL COMMENT '기금 매도 거래 대금',
    rsp_fund_shnu_tr_pbmn TEXT NULL COMMENT '기금 매수2 거래 대금',
    rsp_etc_seln_vol TEXT NULL COMMENT '기타 매도 거래량',
    rsp_etc_shnu_vol TEXT NULL COMMENT '기타 매수2 거래량',
    rsp_etc_seln_tr_pbmn TEXT NULL COMMENT '기타 매도 거래 대금',
    rsp_etc_shnu_tr_pbmn TEXT NULL COMMENT '기타 매수2 거래 대금',
    rsp_etc_orgt_seln_vol TEXT NULL COMMENT '기타 단체 매도 거래량',
    rsp_etc_orgt_shnu_vol TEXT NULL COMMENT '기타 단체 매수2 거래량',
    rsp_etc_orgt_seln_tr_pbmn TEXT NULL COMMENT '기타 단체 매도 거래 대금',
    rsp_etc_orgt_shnu_tr_pbmn TEXT NULL COMMENT '기타 단체 매수2 거래 대금',
    rsp_etc_corp_seln_vol TEXT NULL COMMENT '기타 법인 매도 거래량',
    rsp_etc_corp_shnu_vol TEXT NULL COMMENT '기타 법인 매수2 거래량',
    rsp_etc_corp_seln_tr_pbmn TEXT NULL COMMENT '기타 법인 매도 거래 대금',
    rsp_etc_corp_shnu_tr_pbmn TEXT NULL COMMENT '기타 법인 매수2 거래 대금',
    rsp_bold_yn TEXT NULL COMMENT 'BOLD 여부',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/investor-trade-by-stock-daily';

-- =============================================================
-- psearch_title - 종목조건검색 목록조회 (HHKST03900300)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/psearch-title
-- =============================================================
CREATE TABLE IF NOT EXISTS psearch_title (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_user_id TEXT NULL COMMENT '요청 사용자 HTS ID',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_user_id TEXT NULL COMMENT 'HTS ID',
    rsp_seq TEXT NULL COMMENT '조건키값',
    rsp_grp_nm TEXT NULL COMMENT '그룹명',
    rsp_condition_nm TEXT NULL COMMENT '조건명',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/psearch-title';

-- =============================================================
-- capture_uplowprice - 국내주식 상하한가 포착 (FHKST130000C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/capture-uplowprice
-- =============================================================
CREATE TABLE IF NOT EXISTS capture_uplowprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_prc_cls_code TEXT NULL COMMENT '요청 상하한가 구분코드',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 분류구분코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    req_fid_trgt_cls_code TEXT NULL COMMENT '요청 대상구분코드',
    req_fid_trgt_exls_cls_code TEXT NULL COMMENT '요청 대상제외구분코드',
    req_fid_input_price_1 TEXT NULL COMMENT '요청 입력가격1',
    req_fid_input_price_2 TEXT NULL COMMENT '요청 입력가격2',
    req_fid_vol_cnt TEXT NULL COMMENT '요청 거래량수',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '유가증권단축종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적거래량',
    rsp_total_askp_rsqn TEXT NULL COMMENT '총매도호가잔량',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '총매수호가잔량',
    rsp_askp_rsqn1 TEXT NULL COMMENT '매도호가잔량1',
    rsp_bidp_rsqn1 TEXT NULL COMMENT '매수호가잔량1',
    rsp_prdy_vol TEXT NULL COMMENT '전일거래량',
    rsp_seln_cnqn TEXT NULL COMMENT '매도체결량',
    rsp_shnu_cnqn TEXT NULL COMMENT '매수2체결량',
    rsp_stck_llam TEXT NULL COMMENT '주식하한가',
    rsp_stck_mxpr TEXT NULL COMMENT '주식상한가',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '전일대비거래량비율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/capture-uplowprice';

-- =============================================================
-- comp_program_trade_daily - 프로그램매매 종합현황(일별) (FHPPG04600001)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/comp-program-trade-daily
-- =============================================================
CREATE TABLE IF NOT EXISTS comp_program_trade_daily (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 시장 분류 코드',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 시장 구분 코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 검색시작일',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 검색종료일',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_nabt_entm_seln_tr_pbmn TEXT NULL COMMENT '비차익 위탁 매도 거래 대금',
    rsp_nabt_onsl_seln_vol TEXT NULL COMMENT '비차익 자기 매도 거래량',
    rsp_whol_onsl_seln_tr_pbmn TEXT NULL COMMENT '전체 자기 매도 거래 대금',
    rsp_arbt_smtn_shnu_vol TEXT NULL COMMENT '차익 합계 매수2 거래량',
    rsp_nabt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '비차익 합계 매수2 거래 대금',
    rsp_arbt_entm_ntby_qty TEXT NULL COMMENT '차익 위탁 순매수 수량',
    rsp_nabt_entm_ntby_tr_pbmn TEXT NULL COMMENT '비차익 위탁 순매수 거래 대금',
    rsp_arbt_entm_seln_vol TEXT NULL COMMENT '차익 위탁 매도 거래량',
    rsp_nabt_entm_seln_vol_rate TEXT NULL COMMENT '비차익 위탁 매도 거래량 비율',
    rsp_nabt_onsl_seln_vol_rate TEXT NULL COMMENT '비차익 자기 매도 거래량 비율',
    rsp_whol_onsl_seln_tr_pbmn_rate TEXT NULL COMMENT '전체 자기 매도 거래 대금 비율',
    rsp_arbt_smtm_shun_vol_rate TEXT NULL COMMENT '차익 합계 매수 거래량 비율',
    rsp_nabt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '비차익 합계 매수 거래대금 비율',
    rsp_arbt_entm_ntby_qty_rate TEXT NULL COMMENT '차익 위탁 순매수 수량 비율',
    rsp_nabt_entm_ntby_tr_pbmn_rate TEXT NULL COMMENT '비차익 위탁 순매수 거래 대금',
    rsp_arbt_entm_seln_vol_rate TEXT NULL COMMENT '차익 위탁 매도 거래량 비율',
    rsp_nabt_entm_seln_tr_pbmn_rate TEXT NULL COMMENT '비차익 위탁 매도 거래 대금 비',
    rsp_nabt_onsl_seln_tr_pbmn TEXT NULL COMMENT '비차익 자기 매도 거래 대금',
    rsp_whol_smtn_seln_vol TEXT NULL COMMENT '전체 합계 매도 거래량',
    rsp_arbt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '차익 합계 매수2 거래 대금',
    rsp_whol_entm_shnu_vol TEXT NULL COMMENT '전체 위탁 매수2 거래량',
    rsp_arbt_entm_ntby_tr_pbmn TEXT NULL COMMENT '차익 위탁 순매수 거래 대금',
    rsp_nabt_onsl_ntby_qty TEXT NULL COMMENT '비차익 자기 순매수 수량',
    rsp_arbt_entm_seln_tr_pbmn TEXT NULL COMMENT '차익 위탁 매도 거래 대금',
    rsp_nabt_onsl_seln_tr_pbmn_rate TEXT NULL COMMENT '비차익 자기 매도 거래 대금 비',
    rsp_whol_seln_vol_rate TEXT NULL COMMENT '전체 매도 거래량 비율',
    rsp_arbt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '차익 합계 매수 거래대금 비율',
    rsp_whol_entm_shnu_vol_rate TEXT NULL COMMENT '전체 위탁 매수 거래량 비율',
    rsp_arbt_entm_ntby_tr_pbmn_rate TEXT NULL COMMENT '차익 위탁 순매수 거래 대금 비',
    rsp_nabt_onsl_ntby_qty_rate TEXT NULL COMMENT '비차익 자기 순매수 수량 비율',
    rsp_arbt_entm_seln_tr_pbmn_rate TEXT NULL COMMENT '차익 위탁 매도 거래 대금 비율',
    rsp_nabt_smtn_seln_vol TEXT NULL COMMENT '비차익 합계 매도 거래량',
    rsp_whol_smtn_seln_tr_pbmn TEXT NULL COMMENT '전체 합계 매도 거래 대금',
    rsp_nabt_entm_shnu_vol TEXT NULL COMMENT '비차익 위탁 매수2 거래량',
    rsp_whol_entm_shnu_tr_pbmn TEXT NULL COMMENT '전체 위탁 매수2 거래 대금',
    rsp_arbt_onsl_ntby_qty TEXT NULL COMMENT '차익 자기 순매수 수량',
    rsp_nabt_onsl_ntby_tr_pbmn TEXT NULL COMMENT '비차익 자기 순매수 거래 대금',
    rsp_arbt_onsl_seln_tr_pbmn TEXT NULL COMMENT '차익 자기 매도 거래 대금',
    rsp_nabt_smtm_seln_vol_rate TEXT NULL COMMENT '비차익 합계 매도 거래량 비율',
    rsp_whol_seln_tr_pbmn_rate TEXT NULL COMMENT '전체 매도 거래대금 비율',
    rsp_nabt_entm_shnu_vol_rate TEXT NULL COMMENT '비차익 위탁 매수 거래량 비율',
    rsp_whol_entm_shnu_tr_pbmn_rate TEXT NULL COMMENT '전체 위탁 매수 거래 대금 비율',
    rsp_arbt_onsl_ntby_qty_rate TEXT NULL COMMENT '차익 자기 순매수 수량 비율',
    rsp_nabt_onsl_ntby_tr_pbmn_rate TEXT NULL COMMENT '비차익 자기 순매수 거래 대금',
    rsp_arbt_onsl_seln_tr_pbmn_rate TEXT NULL COMMENT '차익 자기 매도 거래 대금 비율',
    rsp_nabt_smtn_seln_tr_pbmn TEXT NULL COMMENT '비차익 합계 매도 거래 대금',
    rsp_arbt_entm_shnu_vol TEXT NULL COMMENT '차익 위탁 매수2 거래량',
    rsp_nabt_entm_shnu_tr_pbmn TEXT NULL COMMENT '비차익 위탁 매수2 거래 대금',
    rsp_whol_onsl_shnu_vol TEXT NULL COMMENT '전체 자기 매수2 거래량',
    rsp_arbt_onsl_ntby_tr_pbmn TEXT NULL COMMENT '차익 자기 순매수 거래 대금',
    rsp_nabt_smtn_ntby_qty TEXT NULL COMMENT '비차익 합계 순매수 수량',
    rsp_arbt_onsl_seln_vol TEXT NULL COMMENT '차익 자기 매도 거래량',
    rsp_nabt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '비차익 합계 매도 거래대금 비율',
    rsp_arbt_entm_shnu_vol_rate TEXT NULL COMMENT '차익 위탁 매수 거래량 비율',
    rsp_nabt_entm_shnu_tr_pbmn_rate TEXT NULL COMMENT '비차익 위탁 매수 거래 대금 비',
    rsp_whol_onsl_shnu_tr_pbmn TEXT NULL COMMENT '전체 자기 매수2 거래 대금',
    rsp_arbt_onsl_ntby_tr_pbmn_rate TEXT NULL COMMENT '차익 자기 순매수 거래 대금 비',
    rsp_nabt_smtm_ntby_qty_rate TEXT NULL COMMENT '비차익 합계 순매수 수량 비율',
    rsp_arbt_onsl_seln_vol_rate TEXT NULL COMMENT '차익 자기 매도 거래량 비율',
    rsp_whol_entm_seln_vol TEXT NULL COMMENT '전체 위탁 매도 거래량',
    rsp_arbt_entm_shnu_tr_pbmn TEXT NULL COMMENT '차익 위탁 매수2 거래 대금',
    rsp_nabt_onsl_shnu_vol TEXT NULL COMMENT '비차익 자기 매수2 거래량',
    rsp_whol_onsl_shnu_tr_pbmn_rate TEXT NULL COMMENT '전체 자기 매수 거래 대금 비율',
    rsp_arbt_smtn_ntby_qty TEXT NULL COMMENT '차익 합계 순매수 수량',
    rsp_nabt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '비차익 합계 순매수 거래 대금',
    rsp_arbt_smtn_seln_vol TEXT NULL COMMENT '차익 합계 매도 거래량',
    rsp_whol_entm_seln_tr_pbmn TEXT NULL COMMENT '전체 위탁 매도 거래 대금',
    rsp_arbt_entm_shnu_tr_pbmn_rate TEXT NULL COMMENT '차익 위탁 매수 거래 대금 비율',
    rsp_nabt_onsl_shnu_vol_rate TEXT NULL COMMENT '비차익 자기 매수 거래량 비율',
    rsp_whol_onsl_shnu_vol_rate TEXT NULL COMMENT '전체 자기 매수 거래량 비율',
    rsp_arbt_smtm_ntby_qty_rate TEXT NULL COMMENT '차익 합계 순매수 수량 비율',
    rsp_nabt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '비차익 합계 순매수 거래대금 비',
    rsp_arbt_smtm_seln_vol_rate TEXT NULL COMMENT '차익 합계 매도 거래량 비율',
    rsp_whol_entm_seln_vol_rate TEXT NULL COMMENT '전체 위탁 매도 거래량 비율',
    rsp_arbt_onsl_shnu_vol TEXT NULL COMMENT '차익 자기 매수2 거래량',
    rsp_nabt_onsl_shnu_tr_pbmn TEXT NULL COMMENT '비차익 자기 매수2 거래 대금',
    rsp_whol_smtn_shnu_vol TEXT NULL COMMENT '전체 합계 매수2 거래량',
    rsp_arbt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '차익 합계 순매수 거래 대금',
    rsp_whol_entm_ntby_qty TEXT NULL COMMENT '전체 위탁 순매수 수량',
    rsp_arbt_smtn_seln_tr_pbmn TEXT NULL COMMENT '차익 합계 매도 거래 대금',
    rsp_whol_entm_seln_tr_pbmn_rate TEXT NULL COMMENT '전체 위탁 매도 거래 대금 비율',
    rsp_arbt_onsl_shnu_vol_rate TEXT NULL COMMENT '차익 자기 매수 거래량 비율',
    rsp_nabt_onsl_shnu_tr_pbmn_rate TEXT NULL COMMENT '비차익 자기 매수 거래 대금 비',
    rsp_whol_shun_vol_rate TEXT NULL COMMENT '전체 매수 거래량 비율',
    rsp_arbt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '차익 합계 순매수 거래대금 비율',
    rsp_whol_entm_ntby_qty_rate TEXT NULL COMMENT '전체 위탁 순매수 수량 비율',
    rsp_arbt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '차익 합계 매도 거래대금 비율',
    rsp_whol_onsl_seln_vol TEXT NULL COMMENT '전체 자기 매도 거래량',
    rsp_arbt_onsl_shnu_tr_pbmn TEXT NULL COMMENT '차익 자기 매수2 거래 대금',
    rsp_nabt_smtn_shnu_vol TEXT NULL COMMENT '비차익 합계 매수2 거래량',
    rsp_whol_smtn_shnu_tr_pbmn TEXT NULL COMMENT '전체 합계 매수2 거래 대금',
    rsp_nabt_entm_ntby_qty TEXT NULL COMMENT '비차익 위탁 순매수 수량',
    rsp_whol_entm_ntby_tr_pbmn TEXT NULL COMMENT '전체 위탁 순매수 거래 대금',
    rsp_nabt_entm_seln_vol TEXT NULL COMMENT '비차익 위탁 매도 거래량',
    rsp_whol_onsl_seln_vol_rate TEXT NULL COMMENT '전체 자기 매도 거래량 비율',
    rsp_arbt_onsl_shnu_tr_pbmn_rate TEXT NULL COMMENT '차익 자기 매수 거래 대금 비율',
    rsp_nabt_smtm_shun_vol_rate TEXT NULL COMMENT '비차익 합계 매수 거래량 비율',
    rsp_whol_shun_tr_pbmn_rate TEXT NULL COMMENT '전체 매수 거래대금 비율',
    rsp_nabt_entm_ntby_qty_rate TEXT NULL COMMENT '비차익 위탁 순매수 수량 비율',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/comp-program-trade-daily';

-- =============================================================
-- daily_loan_trans - 종목별 일별 대차거래추이 (HHPST074500C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/daily-loan-trans
-- =============================================================
CREATE TABLE IF NOT EXISTS daily_loan_trans (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_mrkt_div_cls_code TEXT NULL COMMENT '요청 조회구분',
    req_mksc_shrn_iscd TEXT NULL COMMENT '요청 종목코드',
    req_start_date TEXT NULL COMMENT '요청 조회시작일시',
    req_end_date TEXT NULL COMMENT '요청 조회종료일시',
    req_cts TEXT NULL COMMENT '요청 이전조회KEY',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_date TEXT NULL COMMENT '일자',
    rsp_stck_prpr TEXT NULL COMMENT '주식 종가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_new_stcn TEXT NULL COMMENT '당일 증가 주수 (체결)',
    rsp_rdmp_stcn TEXT NULL COMMENT '당일 감소 주수 (상환)',
    rsp_prdy_rmnd_vrss TEXT NULL COMMENT '대차거래 증감',
    rsp_rmnd_stcn TEXT NULL COMMENT '당일 잔고 주수',
    rsp_rmnd_amt TEXT NULL COMMENT '당일 잔고 금액',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/daily-loan-trans';

-- =============================================================
-- psearch_result - 종목조건검색조회 (HHKST03900400)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/psearch-result
-- =============================================================
CREATE TABLE IF NOT EXISTS psearch_result (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_user_id TEXT NULL COMMENT '요청 사용자 HTS ID',
    req_seq TEXT NULL COMMENT '요청 사용자조건 키값',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_code TEXT NULL COMMENT '종목코드',
    rsp_name TEXT NULL COMMENT '종목명',
    rsp_daebi TEXT NULL COMMENT '전일대비부호',
    rsp_price TEXT NULL COMMENT '현재가',
    rsp_chgrate TEXT NULL COMMENT '등락율',
    rsp_acml_vol TEXT NULL COMMENT '거래량',
    rsp_trade_amt TEXT NULL COMMENT '거래대금',
    rsp_change TEXT NULL COMMENT '전일대비',
    rsp_cttr TEXT NULL COMMENT '체결강도',
    rsp_open TEXT NULL COMMENT '시가',
    rsp_high TEXT NULL COMMENT '고가',
    rsp_low TEXT NULL COMMENT '저가',
    rsp_high52 TEXT NULL COMMENT '52주최고가',
    rsp_low52 TEXT NULL COMMENT '52주최저가',
    rsp_expprice TEXT NULL COMMENT '예상체결가',
    rsp_expchange TEXT NULL COMMENT '예상대비',
    rsp_expchggrate TEXT NULL COMMENT '예상등락률',
    rsp_expcvol TEXT NULL COMMENT '예상체결수량',
    rsp_chgrate2 TEXT NULL COMMENT '전일거래량대비율',
    rsp_expdaebi TEXT NULL COMMENT '예상대비부호',
    rsp_recprice TEXT NULL COMMENT '기준가',
    rsp_uplmtprice TEXT NULL COMMENT '상한가',
    rsp_dnlmtprice TEXT NULL COMMENT '하한가',
    rsp_stotprice TEXT NULL COMMENT '시가총액',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/psearch-result';

-- =============================================================
-- pbar_tratio - 국내주식 매물대_거래비중 (FHPST01130000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/pbar-tratio
-- =============================================================
CREATE TABLE IF NOT EXISTS pbar_tratio (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 입력시간1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표시장한글명',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식단축종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적거래량',
    rsp_prdy_vol TEXT NULL COMMENT '전일거래량',
    rsp_wghn_avrg_stck_prc TEXT NULL COMMENT '가중평균주식가격',
    rsp_lstn_stcn TEXT NULL COMMENT '상장주수',
    rsp_data_rank TEXT NULL COMMENT '데이터순위',
    rsp_cntg_vol TEXT NULL COMMENT '체결거래량',
    rsp_acml_vol_rlim TEXT NULL COMMENT '누적거래량비중',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/pbar-tratio';

-- =============================================================
-- foreign_institution_total - 국내기관_외국인 매매종목가집계 (FHPTJ04400000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/foreign-institution-total
-- =============================================================
CREATE TABLE IF NOT EXISTS foreign_institution_total (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 시장 분류 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건 화면 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 분류 구분 코드',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 순위 정렬 구분 코드',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 기타 구분  정렬',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_output TEXT NULL COMMENT '응답상세1',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '유가증권 단축 종목코드',
    rsp_ntby_qty TEXT NULL COMMENT '순매수 수량',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '기관계 순매수 수량',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '투자신탁 순매수 수량',
    rsp_bank_ntby_qty TEXT NULL COMMENT '은행 순매수 수량',
    rsp_insu_ntby_qty TEXT NULL COMMENT '보험 순매수 수량',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '종금 순매수 수량',
    rsp_fund_ntby_qty TEXT NULL COMMENT '기금 순매수 수량',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '기타 단체 순매수 거래량',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '기타 법인 순매수 거래량',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '외국인 순매수 거래 대금',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '기관계 순매수 거래 대금',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '투자신탁 순매수 거래 대금',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '은행 순매수 거래 대금',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '보험 순매수 거래 대금',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '종금 순매수 거래 대금',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '기금 순매수 거래 대금',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '기타 단체 순매수 거래 대금',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '기타 법인 순매수 거래 대금',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/foreign-institution-total';

-- =============================================================
-- intstock_stocklist_by_group - 관심종목 그룹별 종목조회 (HHKCM113004C6)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/intstock-stocklist-by-group
-- =============================================================
CREATE TABLE IF NOT EXISTS intstock_stocklist_by_group (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_type TEXT NULL COMMENT '요청 관심종목구분코드',
    req_user_id TEXT NULL COMMENT '요청 사용자 ID',
    req_data_rank TEXT NULL COMMENT '요청 데이터 순위',
    req_inter_grp_code TEXT NULL COMMENT '요청 관심 그룹 코드',
    req_inter_grp_name TEXT NULL COMMENT '요청 관심 그룹 명',
    req_hts_kor_isnm TEXT NULL COMMENT '요청 HTS 한글 종목명',
    req_cntg_cls_code TEXT NULL COMMENT '요청 체결 구분 코드',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 기타 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_data_rank TEXT NULL COMMENT '데이터 순위',
    rsp_inter_grp_name TEXT NULL COMMENT '관심 그룹 명',
    rsp_fid_mrkt_cls_code TEXT NULL COMMENT 'FID 시장 구분 코드',
    rsp_exch_code TEXT NULL COMMENT '거래소코드',
    rsp_jong_code TEXT NULL COMMENT '종목코드',
    rsp_color_code TEXT NULL COMMENT '생상 코드',
    rsp_memo TEXT NULL COMMENT '메모',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_fxdt_ntby_qty TEXT NULL COMMENT '기준일 순매수 수량',
    rsp_cntg_unpr TEXT NULL COMMENT '체결단가',
    rsp_cntg_cls_code TEXT NULL COMMENT '체결 구분 코드',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/intstock-stocklist-by-group';

-- =============================================================
-- inquire_member_daily - 주식현재가 회원사 종목매매동향 (FHPST04540000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-member-daily
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_member_daily (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 회원사코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력날짜1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 입력날짜2',
    req_fid_sctn_cls_code TEXT NULL COMMENT '요청 구간구분코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식영업일자',
    rsp_total_seln_qty TEXT NULL COMMENT '총매도수량',
    rsp_total_shnu_qty TEXT NULL COMMENT '총매수2수량',
    rsp_ntby_qty TEXT NULL COMMENT '순매수수량',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-member-daily';

-- =============================================================
-- program_trade_by_stock_daily - 종목별 프로그램매매추이(일별) (FHPPG04650201)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/program-trade-by-stock-daily
-- =============================================================
CREATE TABLE IF NOT EXISTS program_trade_by_stock_daily (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력 날짜1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_clpr TEXT NULL COMMENT '주식 종가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_whol_smtn_seln_vol TEXT NULL COMMENT '전체 합계 매도 거래량',
    rsp_whol_smtn_shnu_vol TEXT NULL COMMENT '전체 합계 매수2 거래량',
    rsp_whol_smtn_ntby_qty TEXT NULL COMMENT '전체 합계 순매수 수량',
    rsp_whol_smtn_seln_tr_pbmn TEXT NULL COMMENT '전체 합계 매도 거래 대금',
    rsp_whol_smtn_shnu_tr_pbmn TEXT NULL COMMENT '전체 합계 매수2 거래 대금',
    rsp_whol_smtn_ntby_tr_pbmn TEXT NULL COMMENT '전체 합계 순매수 거래 대금',
    rsp_whol_ntby_vol_icdc TEXT NULL COMMENT '전체 순매수 거래량 증감',
    rsp_whol_ntby_tr_pbmn_icdc2 TEXT NULL COMMENT '전체 순매수 거래 대금 증감2',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/program-trade-by-stock-daily';

-- =============================================================
-- intstock_grouplist - 관심종목 그룹조회 (HHKCM113004C7)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/intstock-grouplist
-- =============================================================
CREATE TABLE IF NOT EXISTS intstock_grouplist (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_type TEXT NULL COMMENT '요청 관심종목구분코드',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID 기타 구분 코드',
    req_user_id TEXT NULL COMMENT '요청 사용자 ID',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_date TEXT NULL COMMENT '일자',
    rsp_trnm_hour TEXT NULL COMMENT '전송 시간',
    rsp_data_rank TEXT NULL COMMENT '데이터 순위',
    rsp_inter_grp_code TEXT NULL COMMENT '관심 그룹 코드',
    rsp_inter_grp_name TEXT NULL COMMENT '관심 그룹 명',
    rsp_ask_cnt TEXT NULL COMMENT '요청 개수',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/intstock-grouplist';

-- =============================================================
-- investor_trend_estimate - 종목별 외인기관 추정가집계 (HHPTJ04160200)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/investor-trend-estimate
-- =============================================================
CREATE TABLE IF NOT EXISTS investor_trend_estimate (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_mksc_shrn_iscd TEXT NULL COMMENT '요청 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_hour_gb TEXT NULL COMMENT '입력구분',
    rsp_frgn_fake_ntby_qty TEXT NULL COMMENT '외국인수량(가집계)',
    rsp_orgn_fake_ntby_qty TEXT NULL COMMENT '기관수량(가집계)',
    rsp_sum_fake_ntby_qty TEXT NULL COMMENT '합산수량(가집계)',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/investor-trend-estimate';

-- =============================================================
-- inquire_daily_trade_volume - 종목별일별매수매도체결량 (FHKST03010800)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-daily-trade-volume
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_daily_trade_volume (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID 입력 종목코드',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID 입력 날짜1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID 입력 날짜2',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID 기간 분류 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_shnu_cnqn_smtn TEXT NULL COMMENT '매수 체결량 합계',
    rsp_seln_cnqn_smtn TEXT NULL COMMENT '매도 체결량 합계',
    rsp_stck_bsop_date TEXT NULL COMMENT '거래상태정보',
    rsp_total_seln_qty TEXT NULL COMMENT '총 매도 수량',
    rsp_total_shnu_qty TEXT NULL COMMENT '총 매수 수량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-daily-trade-volume';

-- =============================================================
-- tradprt_byamt - 국내주식 체결금액별 매매비중 (FHKST111900C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/tradprt-byamt
-- =============================================================
CREATE TABLE IF NOT EXISTS tradprt_byamt (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_prpr_name TEXT NULL COMMENT '가격명',
    rsp_smtn_avrg_prpr TEXT NULL COMMENT '합계 평균가격',
    rsp_acml_vol TEXT NULL COMMENT '합계 거래량',
    rsp_whol_ntby_qty_rate TEXT NULL COMMENT '합계 순매수비율',
    rsp_ntby_cntg_csnu TEXT NULL COMMENT '합계 순매수건수',
    rsp_seln_cnqn_smtn TEXT NULL COMMENT '매도 거래량',
    rsp_whol_seln_vol_rate TEXT NULL COMMENT '매도 거래량비율',
    rsp_seln_cntg_csnu TEXT NULL COMMENT '매도 건수',
    rsp_shnu_cnqn_smtn TEXT NULL COMMENT '매수 거래량',
    rsp_whol_shun_vol_rate TEXT NULL COMMENT '매수 거래량비율',
    rsp_shnu_cntg_csnu TEXT NULL COMMENT '매수 건수',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/tradprt-byamt';

-- =============================================================
-- investor_program_trade_today - 프로그램매매 투자자매매동향(당일) (HHPPG046600C1)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/investor-program-trade-today
-- =============================================================
CREATE TABLE IF NOT EXISTS investor_program_trade_today (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_exch_div_cls_code TEXT NULL COMMENT '요청 거래소 구분 코드',
    req_mrkt_div_cls_code TEXT NULL COMMENT '요청 시장 구분 코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_invr_cls_code TEXT NULL COMMENT '투자자코드',
    rsp_all_seln_qty TEXT NULL COMMENT '전체매도수량',
    rsp_all_seln_amt TEXT NULL COMMENT '전체매도대금',
    rsp_invr_cls_name TEXT NULL COMMENT '투자자 구분 명',
    rsp_all_shnu_qty TEXT NULL COMMENT '전체매수수량',
    rsp_all_shnu_amt TEXT NULL COMMENT '전체매수대금',
    rsp_all_ntby_amt TEXT NULL COMMENT '전체순매수대금',
    rsp_arbt_seln_qty TEXT NULL COMMENT '차익매도수량',
    rsp_all_ntby_qty TEXT NULL COMMENT '전체순매수수량',
    rsp_arbt_shnu_qty TEXT NULL COMMENT '차익매수수량',
    rsp_arbt_ntby_qty TEXT NULL COMMENT '차익순매수수량',
    rsp_arbt_seln_amt TEXT NULL COMMENT '차익매도대금',
    rsp_arbt_shnu_amt TEXT NULL COMMENT '차익매수대금',
    rsp_arbt_ntby_amt TEXT NULL COMMENT '차익순매수대금',
    rsp_nabt_seln_qty TEXT NULL COMMENT '비차익매도수량',
    rsp_nabt_shnu_qty TEXT NULL COMMENT '비차익매수수량',
    rsp_nabt_ntby_qty TEXT NULL COMMENT '비차익순매수수량',
    rsp_nabt_seln_amt TEXT NULL COMMENT '비차익매도대금',
    rsp_nabt_shnu_amt TEXT NULL COMMENT '비차익매수대금',
    rsp_nabt_ntby_amt TEXT NULL COMMENT '비차익순매수대금',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/investor-program-trade-today';

-- =============================================================
-- mktfunds - 국내 증시자금 종합 (FHKST649100C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/mktfunds
-- =============================================================
CREATE TABLE IF NOT EXISTS mktfunds (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 입력날짜1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_date TEXT NULL COMMENT '영업일자',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '업종지수현재가',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '업종지수전일대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_hts_avls TEXT NULL COMMENT 'HTS시가총액',
    rsp_cust_dpmn_amt TEXT NULL COMMENT '고객예탁금금액',
    rsp_cust_dpmn_amt_prdy_vrss TEXT NULL COMMENT '고객예탁금금액전일대비',
    rsp_amt_tnrt TEXT NULL COMMENT '금액회전율',
    rsp_uncl_amt TEXT NULL COMMENT '미수금액',
    rsp_crdt_loan_rmnd TEXT NULL COMMENT '신용융자잔고',
    rsp_futs_tfam_amt TEXT NULL COMMENT '선물예수금금액',
    rsp_sttp_amt TEXT NULL COMMENT '주식형금액',
    rsp_mxtp_amt TEXT NULL COMMENT '혼합형금액',
    rsp_bntp_amt TEXT NULL COMMENT '채권형금액',
    rsp_mmf_amt TEXT NULL COMMENT 'MMF금액',
    rsp_secu_lend_amt TEXT NULL COMMENT '담보대출잔고금액',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/mktfunds';

-- =============================================================
-- exp_price_trend - 국내주식 예상체결가 추이 (FHPST01810000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/exp-price-trend
-- =============================================================
CREATE TABLE IF NOT EXISTS exp_price_trend (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_mkop_cls_code TEXT NULL COMMENT '요청 장운영 구분 코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '대표 시장 한글 명',
    rsp_antc_cnpr TEXT NULL COMMENT '예상 체결가',
    rsp_antc_cntg_vrss_sign TEXT NULL COMMENT '예상 체결 대비 부호',
    rsp_antc_cntg_vrss TEXT NULL COMMENT '예상 체결 대비',
    rsp_antc_cntg_prdy_ctrt TEXT NULL COMMENT '예상 체결 전일 대비율',
    rsp_antc_vol TEXT NULL COMMENT '예상 거래량',
    rsp_antc_tr_pbmn TEXT NULL COMMENT '예상 거래대금',
    rsp_stck_bsop_date TEXT NULL COMMENT '주식 영업 일자',
    rsp_stck_cntg_hour TEXT NULL COMMENT '주식 체결 시간',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/exp-price-trend';

-- =============================================================
-- frgnmem_trade_trend - 회원사 실시간 매매동향(틱) (FHPST04320000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/frgnmem-trade-trend
-- =============================================================
CREATE TABLE IF NOT EXISTS frgnmem_trade_trend (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID 조건 시장 분류 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 화면분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 종목코드',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 회원사코드',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 시장구분코드',
    req_fid_vol_cnt TEXT NULL COMMENT '요청 거래량',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_total_seln_qty TEXT NULL COMMENT '총매도수량',
    rsp_total_shnu_qty TEXT NULL COMMENT '총매수2수량',
    rsp_bsop_hour TEXT NULL COMMENT '영업시간',
    rsp_mbcr_name TEXT NULL COMMENT '회원사명',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_cntg_vol TEXT NULL COMMENT '체결거래량',
    rsp_acml_ntby_qty TEXT NULL COMMENT '누적순매수수량',
    rsp_glob_ntby_qty TEXT NULL COMMENT '외국계순매수수량',
    rsp_frgn_ntby_qty_icdc TEXT NULL COMMENT '외국인순매수수량증감',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/frgnmem-trade-trend';

-- =============================================================
-- inquire_investor_time_by_market - 시장별 투자자매매동향(시세) (FHPTJ04030000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market
-- =============================================================
CREATE TABLE IF NOT EXISTS inquire_investor_time_by_market (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_iscd TEXT NULL COMMENT '요청 시장구분',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 업종구분',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_frgn_seln_vol TEXT NULL COMMENT '외국인 매도 거래량',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '외국인 매수2 거래량',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '외국인 순매수 수량',
    rsp_frgn_seln_tr_pbmn TEXT NULL COMMENT '외국인 매도 거래 대금',
    rsp_frgn_shnu_tr_pbmn TEXT NULL COMMENT '외국인 매수2 거래 대금',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '외국인 순매수 거래 대금',
    rsp_prsn_seln_vol TEXT NULL COMMENT '개인 매도 거래량',
    rsp_prsn_shnu_vol TEXT NULL COMMENT '개인 매수2 거래량',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '개인 순매수 수량',
    rsp_prsn_seln_tr_pbmn TEXT NULL COMMENT '개인 매도 거래 대금',
    rsp_prsn_shnu_tr_pbmn TEXT NULL COMMENT '개인 매수2 거래 대금',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '개인 순매수 거래 대금',
    rsp_orgn_seln_vol TEXT NULL COMMENT '기관계 매도 거래량',
    rsp_orgn_shnu_vol TEXT NULL COMMENT '기관계 매수2 거래량',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '기관계 순매수 수량',
    rsp_orgn_seln_tr_pbmn TEXT NULL COMMENT '기관계 매도 거래 대금',
    rsp_orgn_shnu_tr_pbmn TEXT NULL COMMENT '기관계 매수2 거래 대금',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '기관계 순매수 거래 대금',
    rsp_scrt_seln_vol TEXT NULL COMMENT '증권 매도 거래량',
    rsp_scrt_shnu_vol TEXT NULL COMMENT '증권 매수2 거래량',
    rsp_scrt_ntby_qty TEXT NULL COMMENT '증권 순매수 수량',
    rsp_scrt_seln_tr_pbmn TEXT NULL COMMENT '증권 매도 거래 대금',
    rsp_scrt_shnu_tr_pbmn TEXT NULL COMMENT '증권 매수2 거래 대금',
    rsp_scrt_ntby_tr_pbmn TEXT NULL COMMENT '증권 순매수 거래 대금',
    rsp_ivtr_seln_vol TEXT NULL COMMENT '투자신탁 매도 거래량',
    rsp_ivtr_shnu_vol TEXT NULL COMMENT '투자신탁 매수2 거래량',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '투자신탁 순매수 수량',
    rsp_ivtr_seln_tr_pbmn TEXT NULL COMMENT '투자신탁 매도 거래 대금',
    rsp_ivtr_shnu_tr_pbmn TEXT NULL COMMENT '투자신탁 매수2 거래 대금',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '투자신탁 순매수 거래 대금',
    rsp_pe_fund_seln_tr_pbmn TEXT NULL COMMENT '사모 펀드 매도 거래 대금',
    rsp_pe_fund_seln_vol TEXT NULL COMMENT '사모 펀드 매도 거래량',
    rsp_pe_fund_ntby_vol TEXT NULL COMMENT '사모 펀드 순매수 거래량',
    rsp_pe_fund_shnu_tr_pbmn TEXT NULL COMMENT '사모 펀드 매수2 거래 대금',
    rsp_pe_fund_shnu_vol TEXT NULL COMMENT '사모 펀드 매수2 거래량',
    rsp_pe_fund_ntby_tr_pbmn TEXT NULL COMMENT '사모 펀드 순매수 거래 대금',
    rsp_bank_seln_vol TEXT NULL COMMENT '은행 매도 거래량',
    rsp_bank_shnu_vol TEXT NULL COMMENT '은행 매수2 거래량',
    rsp_bank_ntby_qty TEXT NULL COMMENT '은행 순매수 수량',
    rsp_bank_seln_tr_pbmn TEXT NULL COMMENT '은행 매도 거래 대금',
    rsp_bank_shnu_tr_pbmn TEXT NULL COMMENT '은행 매수2 거래 대금',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '은행 순매수 거래 대금',
    rsp_insu_seln_vol TEXT NULL COMMENT '보험 매도 거래량',
    rsp_insu_shnu_vol TEXT NULL COMMENT '보험 매수2 거래량',
    rsp_insu_ntby_qty TEXT NULL COMMENT '보험 순매수 수량',
    rsp_insu_seln_tr_pbmn TEXT NULL COMMENT '보험 매도 거래 대금',
    rsp_insu_shnu_tr_pbmn TEXT NULL COMMENT '보험 매수2 거래 대금',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '보험 순매수 거래 대금',
    rsp_mrbn_seln_vol TEXT NULL COMMENT '종금 매도 거래량',
    rsp_mrbn_shnu_vol TEXT NULL COMMENT '종금 매수2 거래량',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '종금 순매수 수량',
    rsp_mrbn_seln_tr_pbmn TEXT NULL COMMENT '종금 매도 거래 대금',
    rsp_mrbn_shnu_tr_pbmn TEXT NULL COMMENT '종금 매수2 거래 대금',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '종금 순매수 거래 대금',
    rsp_fund_seln_vol TEXT NULL COMMENT '기금 매도 거래량',
    rsp_fund_shnu_vol TEXT NULL COMMENT '기금 매수2 거래량',
    rsp_fund_ntby_qty TEXT NULL COMMENT '기금 순매수 수량',
    rsp_fund_seln_tr_pbmn TEXT NULL COMMENT '기금 매도 거래 대금',
    rsp_fund_shnu_tr_pbmn TEXT NULL COMMENT '기금 매수2 거래 대금',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '기금 순매수 거래 대금',
    rsp_etc_orgt_seln_vol TEXT NULL COMMENT '기타 단체 매도 거래량',
    rsp_etc_orgt_shnu_vol TEXT NULL COMMENT '기타 단체 매수2 거래량',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '기타 단체 순매수 거래량',
    rsp_etc_orgt_seln_tr_pbmn TEXT NULL COMMENT '기타 단체 매도 거래 대금',
    rsp_etc_orgt_shnu_tr_pbmn TEXT NULL COMMENT '기타 단체 매수2 거래 대금',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '기타 단체 순매수 거래 대금',
    rsp_etc_corp_seln_vol TEXT NULL COMMENT '기타 법인 매도 거래량',
    rsp_etc_corp_shnu_vol TEXT NULL COMMENT '기타 법인 매수2 거래량',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '기타 법인 순매수 거래량',
    rsp_etc_corp_seln_tr_pbmn TEXT NULL COMMENT '기타 법인 매도 거래 대금',
    rsp_etc_corp_shnu_tr_pbmn TEXT NULL COMMENT '기타 법인 매수2 거래 대금',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '기타 법인 순매수 거래 대금',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/inquire-investor-time-by-market';

-- =============================================================
-- program_trade_by_stock - 종목별 프로그램매매추이(체결) (FHPPG04650101)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/program-trade-by-stock
-- =============================================================
CREATE TABLE IF NOT EXISTS program_trade_by_stock (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_hour TEXT NULL COMMENT '영업 시간',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_whol_smtn_seln_vol TEXT NULL COMMENT '전체 합계 매도 거래량',
    rsp_whol_smtn_shnu_vol TEXT NULL COMMENT '전체 합계 매수2 거래량',
    rsp_whol_smtn_ntby_qty TEXT NULL COMMENT '전체 합계 순매수 수량',
    rsp_whol_smtn_seln_tr_pbmn TEXT NULL COMMENT '전체 합계 매도 거래 대금',
    rsp_whol_smtn_shnu_tr_pbmn TEXT NULL COMMENT '전체 합계 매수2 거래 대금',
    rsp_whol_smtn_ntby_tr_pbmn TEXT NULL COMMENT '전체 합계 순매수 거래 대금',
    rsp_whol_ntby_vol_icdc TEXT NULL COMMENT '전체 순매수 거래량 증감',
    rsp_whol_ntby_tr_pbmn_icdc TEXT NULL COMMENT '전체 순매수 거래 대금 증감',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/program-trade-by-stock';

-- =============================================================
-- frgnmem_trade_estimate - 외국계 매매종목 가집계 (FHKST644100C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/frgnmem-trade-estimate
-- =============================================================
CREATE TABLE IF NOT EXISTS frgnmem_trade_estimate (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력종목코드',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 순위정렬구분코드',
    req_fid_rank_sort_cls_code_2 TEXT NULL COMMENT '요청 순위정렬구분코드2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '주식단축종목코드',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS한글종목명',
    rsp_glob_ntsl_qty TEXT NULL COMMENT '외국계순매도수량',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적거래량',
    rsp_glob_total_seln_qty TEXT NULL COMMENT '외국계총매도수량',
    rsp_glob_total_shnu_qty TEXT NULL COMMENT '외국계총매수2수량',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/frgnmem-trade-estimate';

-- =============================================================
-- frgnmem_pchs_trend - 종목별 외국계 순매수추이 (FHKST644400C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/frgnmem-pchs-trend
-- =============================================================
CREATE TABLE IF NOT EXISTS frgnmem_pchs_trend (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_input_iscd TEXT NULL COMMENT '요청 조건시장분류코드',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 조건화면분류코드',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 시장구분코드',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_bsop_hour TEXT NULL COMMENT '영업시간',
    rsp_stck_prpr TEXT NULL COMMENT '주식현재가',
    rsp_prdy_vrss TEXT NULL COMMENT '전일대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일대비부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적거래량',
    rsp_frgn_seln_vol TEXT NULL COMMENT '외국인매도거래량',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '외국인매수2거래량',
    rsp_glob_ntby_qty TEXT NULL COMMENT '외국계순매수수량',
    rsp_frgn_ntby_qty_icdc TEXT NULL COMMENT '외국인순매수수량증감',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/frgnmem-pchs-trend';

-- =============================================================
-- intstock_multprice - 관심종목(멀티종목) 시세조회 (FHKST11300006)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/intstock-multprice
-- =============================================================
CREATE TABLE IF NOT EXISTS intstock_multprice (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code_1 TEXT NULL COMMENT '요청 조건 시장 분류 코드1',
    req_fid_input_iscd_1 TEXT NULL COMMENT '요청 입력 종목코드1',
    req_fid_cond_mrkt_div_code_2 TEXT NULL COMMENT '요청 조건 시장 분류 코드2',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 입력 종목코드2',
    req_fid_cond_mrkt_div_code_3 TEXT NULL COMMENT '요청 조건 시장 분류 코드3',
    req_fid_input_iscd_3 TEXT NULL COMMENT '요청 입력 종목코드3',
    req_fid_cond_mrkt_div_code_4 TEXT NULL COMMENT '요청 조건 시장 분류 코드4',
    req_fid_input_iscd_4 TEXT NULL COMMENT '요청 입력 종목코드4',
    req_fid_cond_mrkt_div_code_5 TEXT NULL COMMENT '요청 조건 시장 분류 코드5',
    req_fid_input_iscd_5 TEXT NULL COMMENT '요청 입력 종목코드5',
    req_fid_cond_mrkt_div_code_6 TEXT NULL COMMENT '요청 조건 시장 분류 코드6',
    req_fid_input_iscd_6 TEXT NULL COMMENT '요청 입력 종목코드6',
    req_fid_cond_mrkt_div_code_7 TEXT NULL COMMENT '요청 조건 시장 분류 코드7',
    req_fid_input_iscd_7 TEXT NULL COMMENT '요청 입력 종목코드7',
    req_fid_cond_mrkt_div_code_8 TEXT NULL COMMENT '요청 조건 시장 분류 코드8',
    req_fid_input_iscd_8 TEXT NULL COMMENT '요청 입력 종목코드8',
    req_fid_cond_mrkt_div_code_9 TEXT NULL COMMENT '요청 조건 시장 분류 코드9',
    req_fid_input_iscd_9 TEXT NULL COMMENT '요청 입력 종목코드9',
    req_fid_cond_mrkt_div_code_10 TEXT NULL COMMENT '요청 조건 시장 분류 코드10',
    req_fid_input_iscd_10 TEXT NULL COMMENT '요청 입력 종목코드10',
    req_fid_cond_mrkt_div_code_11 TEXT NULL COMMENT '요청 조건 시장 분류 코드11',
    req_fid_input_iscd_11 TEXT NULL COMMENT '요청 입력 종목코드11',
    req_fid_cond_mrkt_div_code_12 TEXT NULL COMMENT '요청 조건 시장 분류 코드12',
    req_fid_input_iscd_12 TEXT NULL COMMENT '요청 입력 종목코드12',
    req_fid_cond_mrkt_div_code_13 TEXT NULL COMMENT '요청 조건 시장 분류 코드13',
    req_fid_input_iscd_13 TEXT NULL COMMENT '요청 입력 종목코드13',
    req_fid_cond_mrkt_div_code_14 TEXT NULL COMMENT '요청 조건 시장 분류 코드14',
    req_fid_input_iscd_14 TEXT NULL COMMENT '요청 입력 종목코드14',
    req_fid_cond_mrkt_div_code_15 TEXT NULL COMMENT '요청 조건 시장 분류 코드15',
    req_fid_input_iscd_15 TEXT NULL COMMENT '요청 입력 종목코드15',
    req_fid_cond_mrkt_div_code_16 TEXT NULL COMMENT '요청 조건 시장 분류 코드16',
    req_fid_input_iscd_16 TEXT NULL COMMENT '요청 입력 종목코드16',
    req_fid_cond_mrkt_div_code_17 TEXT NULL COMMENT '요청 조건 시장 분류 코드17',
    req_fid_input_iscd_17 TEXT NULL COMMENT '요청 입력 종목코드17',
    req_fid_cond_mrkt_div_code_18 TEXT NULL COMMENT '요청 조건 시장 분류 코드18',
    req_fid_input_iscd_18 TEXT NULL COMMENT '요청 입력 종목코드18',
    req_fid_cond_mrkt_div_code_19 TEXT NULL COMMENT '요청 조건 시장 분류 코드19',
    req_fid_input_iscd_19 TEXT NULL COMMENT '요청 입력 종목코드19',
    req_fid_cond_mrkt_div_code_20 TEXT NULL COMMENT '요청 조건 시장 분류 코드20',
    req_fid_input_iscd_20 TEXT NULL COMMENT '요청 입력 종목코드20',
    req_fid_cond_mrkt_div_code_21 TEXT NULL COMMENT '요청 조건 시장 분류 코드21',
    req_fid_input_iscd_21 TEXT NULL COMMENT '요청 입력 종목코드21',
    req_fid_cond_mrkt_div_code_22 TEXT NULL COMMENT '요청 조건 시장 분류 코드22',
    req_fid_input_iscd_22 TEXT NULL COMMENT '요청 입력 종목코드22',
    req_fid_cond_mrkt_div_code_23 TEXT NULL COMMENT '요청 조건 시장 분류 코드23',
    req_fid_input_iscd_23 TEXT NULL COMMENT '요청 입력 종목코드23',
    req_fid_cond_mrkt_div_code_24 TEXT NULL COMMENT '요청 조건 시장 분류 코드24',
    req_fid_input_iscd_24 TEXT NULL COMMENT '요청 입력 종목코드24',
    req_fid_cond_mrkt_div_code_25 TEXT NULL COMMENT '요청 조건 시장 분류 코드25',
    req_fid_input_iscd_25 TEXT NULL COMMENT '요청 입력 종목코드25',
    req_fid_cond_mrkt_div_code_26 TEXT NULL COMMENT '요청 조건 시장 분류 코드26',
    req_fid_input_iscd_26 TEXT NULL COMMENT '요청 입력 종목코드26',
    req_fid_cond_mrkt_div_code_27 TEXT NULL COMMENT '요청 조건 시장 분류 코드27',
    req_fid_input_iscd_27 TEXT NULL COMMENT '요청 입력 종목코드27',
    req_fid_cond_mrkt_div_code_28 TEXT NULL COMMENT '요청 조건 시장 분류 코드28',
    req_fid_input_iscd_28 TEXT NULL COMMENT '요청 입력 종목코드28',
    req_fid_cond_mrkt_div_code_29 TEXT NULL COMMENT '요청 조건 시장 분류 코드29',
    req_fid_input_iscd_29 TEXT NULL COMMENT '요청 입력 종목코드29',
    req_fid_cond_mrkt_div_code_30 TEXT NULL COMMENT '요청 조건 시장 분류 코드30',
    req_fid_input_iscd_30 TEXT NULL COMMENT '요청 입력 종목코드30',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_kospi_kosdaq_cls_name TEXT NULL COMMENT '코스피 코스닥 구분 명',
    rsp_mrkt_trtm_cls_name TEXT NULL COMMENT '시장 조치 구분 명',
    rsp_hour_cls_code TEXT NULL COMMENT '시간 구분 코드',
    rsp_inter_shrn_iscd TEXT NULL COMMENT '관심 단축 종목코드',
    rsp_inter_kor_isnm TEXT NULL COMMENT '관심 한글 종목명',
    rsp_inter2_prpr TEXT NULL COMMENT '관심2 현재가',
    rsp_inter2_prdy_vrss TEXT NULL COMMENT '관심2 전일 대비',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_inter2_oprc TEXT NULL COMMENT '관심2 시가',
    rsp_inter2_hgpr TEXT NULL COMMENT '관심2 고가',
    rsp_inter2_lwpr TEXT NULL COMMENT '관심2 저가',
    rsp_inter2_llam TEXT NULL COMMENT '관심2 하한가',
    rsp_inter2_mxpr TEXT NULL COMMENT '관심2 상한가',
    rsp_inter2_askp TEXT NULL COMMENT '관심2 매도호가',
    rsp_inter2_bidp TEXT NULL COMMENT '관심2 매수호가',
    rsp_seln_rsqn TEXT NULL COMMENT '매도 잔량',
    rsp_shnu_rsqn TEXT NULL COMMENT '매수2 잔량',
    rsp_total_askp_rsqn TEXT NULL COMMENT '총 매도호가 잔량',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '총 매수호가 잔량',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    rsp_inter2_prdy_clpr TEXT NULL COMMENT '관심2 전일 종가',
    rsp_oprc_vrss_hgpr_rate TEXT NULL COMMENT '시가 대비 최고가 비율',
    rsp_intr_antc_cntg_vrss TEXT NULL COMMENT '관심 예상 체결 대비',
    rsp_intr_antc_cntg_vrss_sign TEXT NULL COMMENT '관심 예상 체결 대비 부호',
    rsp_intr_antc_cntg_prdy_ctrt TEXT NULL COMMENT '관심 예상 체결 전일 대비율',
    rsp_intr_antc_vol TEXT NULL COMMENT '관심 예상 거래량',
    rsp_inter2_sdpr TEXT NULL COMMENT '관심2 기준가',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/intstock-multprice';

-- =============================================================
-- volume_rank - 거래량순위 (FHPST01710000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/quotations/volume-rank
-- =============================================================
CREATE TABLE IF NOT EXISTS volume_rank (
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    gt_uid VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'Global UID',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 조건 시장 분류 코드',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 조건 화면 분류 코드',
    req_fid_input_iscd TEXT NULL COMMENT '요청 입력 종목코드',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 분류 구분 코드',
    req_fid_blng_cls_code TEXT NULL COMMENT '요청 소속 구분 코드',
    req_fid_trgt_cls_code TEXT NULL COMMENT '요청 대상 구분 코드',
    req_fid_trgt_exls_cls_code TEXT NULL COMMENT '요청 대상 제외 구분 코드',
    req_fid_input_price_1 TEXT NULL COMMENT '요청 입력 가격1',
    req_fid_input_price_2 TEXT NULL COMMENT '요청 입력 가격2',
    req_fid_vol_cnt TEXT NULL COMMENT '요청 거래량 수',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '성공 실패 여부',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답코드',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답메세지',
    rsp_output TEXT NULL COMMENT '응답상세',
    rsp_hts_kor_isnm TEXT NULL COMMENT 'HTS 한글 종목명',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '유가증권 단축 종목코드',
    rsp_data_rank TEXT NULL COMMENT '데이터 순위',
    rsp_stck_prpr TEXT NULL COMMENT '주식 현재가',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '전일 대비 부호',
    rsp_prdy_vrss TEXT NULL COMMENT '전일 대비',
    rsp_prdy_ctrt TEXT NULL COMMENT '전일 대비율',
    rsp_acml_vol TEXT NULL COMMENT '누적 거래량',
    rsp_prdy_vol TEXT NULL COMMENT '전일 거래량',
    rsp_lstn_stcn TEXT NULL COMMENT '상장 주수',
    rsp_avrg_vol TEXT NULL COMMENT '평균 거래량',
    rsp_n_befr_clpr_vrss_prpr_rate TEXT NULL COMMENT 'N일전종가대비현재가대비율',
    rsp_vol_inrt TEXT NULL COMMENT '거래량증가율',
    rsp_vol_tnrt TEXT NULL COMMENT '거래량 회전율',
    rsp_nday_vol_tnrt TEXT NULL COMMENT 'N일 거래량 회전율',
    rsp_avrg_tr_pbmn TEXT NULL COMMENT '평균 거래 대금',
    rsp_tr_pbmn_tnrt TEXT NULL COMMENT '거래대금회전율',
    rsp_nday_tr_pbmn_tnrt TEXT NULL COMMENT 'N일 거래대금 회전율',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '누적 거래 대금',
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='quotations/volume-rank';

-- =============================================================
-- 인덱스 설명
-- =============================================================
-- idx_req_dt: 시간 범위 조회
-- idx_tr_id: TR_ID 조건 조회
-- idx_rt_cd: 성공/실패 구분 조회 (rt_cd = 0 성공)

