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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID_PERIOD_DIV_CODE',
    req_fid_org_adj_prc TEXT NULL COMMENT '요청 FID_ORG_ADJ_PRC',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '응답 prdy_vrss_vol_rate',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_hts_frgn_ehrt TEXT NULL COMMENT '응답 hts_frgn_ehrt',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_flng_cls_code TEXT NULL COMMENT '응답 flng_cls_code',
    rsp_acml_prtt_rate TEXT NULL COMMENT '응답 acml_prtt_rate',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_iscd_stat_cls_code TEXT NULL COMMENT '응답 iscd_stat_cls_code',
    rsp_marg_rate TEXT NULL COMMENT '응답 marg_rate',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_new_hgpr_lwpr_cls_code TEXT NULL COMMENT '응답 new_hgpr_lwpr_cls_code',
    rsp_bstp_kor_isnm TEXT NULL COMMENT '응답 bstp_kor_isnm',
    rsp_temp_stop_yn TEXT NULL COMMENT '응답 temp_stop_yn',
    rsp_oprc_rang_cont_yn TEXT NULL COMMENT '응답 oprc_rang_cont_yn',
    rsp_clpr_rang_cont_yn TEXT NULL COMMENT '응답 clpr_rang_cont_yn',
    rsp_crdt_able_yn TEXT NULL COMMENT '응답 crdt_able_yn',
    rsp_grmn_rate_cls_code TEXT NULL COMMENT '응답 grmn_rate_cls_code',
    rsp_elw_pblc_yn TEXT NULL COMMENT '응답 elw_pblc_yn',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '응답 prdy_vrss_vol_rate',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_stck_mxpr TEXT NULL COMMENT '응답 stck_mxpr',
    rsp_stck_llam TEXT NULL COMMENT '응답 stck_llam',
    rsp_stck_sdpr TEXT NULL COMMENT '응답 stck_sdpr',
    rsp_wghn_avrg_stck_prc TEXT NULL COMMENT '응답 wghn_avrg_stck_prc',
    rsp_hts_frgn_ehrt TEXT NULL COMMENT '응답 hts_frgn_ehrt',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_pgtr_ntby_qty TEXT NULL COMMENT '응답 pgtr_ntby_qty',
    rsp_pvt_scnd_dmrs_prc TEXT NULL COMMENT '응답 pvt_scnd_dmrs_prc',
    rsp_pvt_frst_dmrs_prc TEXT NULL COMMENT '응답 pvt_frst_dmrs_prc',
    rsp_pvt_pont_val TEXT NULL COMMENT '응답 pvt_pont_val',
    rsp_pvt_frst_dmsp_prc TEXT NULL COMMENT '응답 pvt_frst_dmsp_prc',
    rsp_pvt_scnd_dmsp_prc TEXT NULL COMMENT '응답 pvt_scnd_dmsp_prc',
    rsp_dmrs_val TEXT NULL COMMENT '응답 dmrs_val',
    rsp_dmsp_val TEXT NULL COMMENT '응답 dmsp_val',
    rsp_cpfn TEXT NULL COMMENT '응답 cpfn',
    rsp_rstc_wdth_prc TEXT NULL COMMENT '응답 rstc_wdth_prc',
    rsp_stck_fcam TEXT NULL COMMENT '응답 stck_fcam',
    rsp_stck_sspr TEXT NULL COMMENT '응답 stck_sspr',
    rsp_aspr_unit TEXT NULL COMMENT '응답 aspr_unit',
    rsp_hts_deal_qty_unit_val TEXT NULL COMMENT '응답 hts_deal_qty_unit_val',
    rsp_lstn_stcn TEXT NULL COMMENT '응답 lstn_stcn',
    rsp_hts_avls TEXT NULL COMMENT '응답 hts_avls',
    rsp_per TEXT NULL COMMENT '응답 per',
    rsp_pbr TEXT NULL COMMENT '응답 pbr',
    rsp_stac_month TEXT NULL COMMENT '응답 stac_month',
    rsp_vol_tnrt TEXT NULL COMMENT '응답 vol_tnrt',
    rsp_eps TEXT NULL COMMENT '응답 eps',
    rsp_bps TEXT NULL COMMENT '응답 bps',
    rsp_d250_hgpr TEXT NULL COMMENT '응답 d250_hgpr',
    rsp_d250_hgpr_date TEXT NULL COMMENT '응답 d250_hgpr_date',
    rsp_d250_hgpr_vrss_prpr_rate TEXT NULL COMMENT '응답 d250_hgpr_vrss_prpr_rate',
    rsp_d250_lwpr TEXT NULL COMMENT '응답 d250_lwpr',
    rsp_d250_lwpr_date TEXT NULL COMMENT '응답 d250_lwpr_date',
    rsp_d250_lwpr_vrss_prpr_rate TEXT NULL COMMENT '응답 d250_lwpr_vrss_prpr_rate',
    rsp_stck_dryy_hgpr TEXT NULL COMMENT '응답 stck_dryy_hgpr',
    rsp_dryy_hgpr_vrss_prpr_rate TEXT NULL COMMENT '응답 dryy_hgpr_vrss_prpr_rate',
    rsp_dryy_hgpr_date TEXT NULL COMMENT '응답 dryy_hgpr_date',
    rsp_stck_dryy_lwpr TEXT NULL COMMENT '응답 stck_dryy_lwpr',
    rsp_dryy_lwpr_vrss_prpr_rate TEXT NULL COMMENT '응답 dryy_lwpr_vrss_prpr_rate',
    rsp_dryy_lwpr_date TEXT NULL COMMENT '응답 dryy_lwpr_date',
    rsp_w52_hgpr TEXT NULL COMMENT '응답 w52_hgpr',
    rsp_w52_hgpr_vrss_prpr_ctrt TEXT NULL COMMENT '응답 w52_hgpr_vrss_prpr_ctrt',
    rsp_w52_hgpr_date TEXT NULL COMMENT '응답 w52_hgpr_date',
    rsp_w52_lwpr TEXT NULL COMMENT '응답 w52_lwpr',
    rsp_w52_lwpr_vrss_prpr_ctrt TEXT NULL COMMENT '응답 w52_lwpr_vrss_prpr_ctrt',
    rsp_w52_lwpr_date TEXT NULL COMMENT '응답 w52_lwpr_date',
    rsp_whol_loan_rmnd_rate TEXT NULL COMMENT '응답 whol_loan_rmnd_rate',
    rsp_ssts_yn TEXT NULL COMMENT '응답 ssts_yn',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_fcam_cnnm TEXT NULL COMMENT '응답 fcam_cnnm',
    rsp_cpfn_cnnm TEXT NULL COMMENT '응답 cpfn_cnnm',
    rsp_apprch_rate TEXT NULL COMMENT '응답 apprch_rate',
    rsp_frgn_hldn_qty TEXT NULL COMMENT '응답 frgn_hldn_qty',
    rsp_vi_cls_code TEXT NULL COMMENT '응답 vi_cls_code',
    rsp_ovtm_vi_cls_code TEXT NULL COMMENT '응답 ovtm_vi_cls_code',
    rsp_last_ssts_cntg_qty TEXT NULL COMMENT '응답 last_ssts_cntg_qty',
    rsp_invt_caful_yn TEXT NULL COMMENT '응답 invt_caful_yn',
    rsp_mrkt_warn_cls_code TEXT NULL COMMENT '응답 mrkt_warn_cls_code',
    rsp_short_over_yn TEXT NULL COMMENT '응답 short_over_yn',
    rsp_sltr_yn TEXT NULL COMMENT '응답 sltr_yn',
    rsp_mang_issu_cls_code TEXT NULL COMMENT '응답 mang_issu_cls_code',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bstp_kor_isnm TEXT NULL COMMENT '응답 bstp_kor_isnm',
    rsp_mang_issu_cls_name TEXT NULL COMMENT '응답 mang_issu_cls_name',
    rsp_ovtm_untp_prpr TEXT NULL COMMENT '응답 ovtm_untp_prpr',
    rsp_ovtm_untp_prdy_vrss TEXT NULL COMMENT '응답 ovtm_untp_prdy_vrss',
    rsp_ovtm_untp_prdy_vrss_sign TEXT NULL COMMENT '응답 ovtm_untp_prdy_vrss_sign',
    rsp_ovtm_untp_prdy_ctrt TEXT NULL COMMENT '응답 ovtm_untp_prdy_ctrt',
    rsp_ovtm_untp_vol TEXT NULL COMMENT '응답 ovtm_untp_vol',
    rsp_ovtm_untp_tr_pbmn TEXT NULL COMMENT '응답 ovtm_untp_tr_pbmn',
    rsp_ovtm_untp_mxpr TEXT NULL COMMENT '응답 ovtm_untp_mxpr',
    rsp_ovtm_untp_llam TEXT NULL COMMENT '응답 ovtm_untp_llam',
    rsp_ovtm_untp_oprc TEXT NULL COMMENT '응답 ovtm_untp_oprc',
    rsp_ovtm_untp_hgpr TEXT NULL COMMENT '응답 ovtm_untp_hgpr',
    rsp_ovtm_untp_lwpr TEXT NULL COMMENT '응답 ovtm_untp_lwpr',
    rsp_marg_rate TEXT NULL COMMENT '응답 marg_rate',
    rsp_ovtm_untp_antc_cnpr TEXT NULL COMMENT '응답 ovtm_untp_antc_cnpr',
    rsp_ovtm_untp_antc_cntg_vrss TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_vrss',
    rsp_ovtm_untp_antc_cntg_vrss_sign TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_vrss_sign',
    rsp_ovtm_untp_antc_cntg_ctrt TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_ctrt',
    rsp_ovtm_untp_antc_cnqn TEXT NULL COMMENT '응답 ovtm_untp_antc_cnqn',
    rsp_crdt_able_yn TEXT NULL COMMENT '응답 crdt_able_yn',
    rsp_new_lstn_cls_name TEXT NULL COMMENT '응답 new_lstn_cls_name',
    rsp_sltr_yn TEXT NULL COMMENT '응답 sltr_yn',
    rsp_mang_issu_yn TEXT NULL COMMENT '응답 mang_issu_yn',
    rsp_mrkt_warn_cls_code TEXT NULL COMMENT '응답 mrkt_warn_cls_code',
    rsp_trht_yn TEXT NULL COMMENT '응답 trht_yn',
    rsp_vlnt_deal_cls_name TEXT NULL COMMENT '응답 vlnt_deal_cls_name',
    rsp_ovtm_untp_sdpr TEXT NULL COMMENT '응답 ovtm_untp_sdpr',
    rsp_mrkt_warn_cls_name TEXT NULL COMMENT '응답 mrkt_warn_cls_name',
    rsp_revl_issu_reas_name TEXT NULL COMMENT '응답 revl_issu_reas_name',
    rsp_insn_pbnt_yn TEXT NULL COMMENT '응답 insn_pbnt_yn',
    rsp_flng_cls_name TEXT NULL COMMENT '응답 flng_cls_name',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_ovtm_vi_cls_code TEXT NULL COMMENT '응답 ovtm_vi_cls_code',
    rsp_bidp TEXT NULL COMMENT '응답 bidp',
    rsp_askp TEXT NULL COMMENT '응답 askp',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_hour_cls_code TEXT NULL COMMENT '요청 FID_HOUR_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_ovtm_untp_prpr TEXT NULL COMMENT '응답 ovtm_untp_prpr',
    rsp_ovtm_untp_prdy_vrss TEXT NULL COMMENT '응답 ovtm_untp_prdy_vrss',
    rsp_ovtm_untp_prdy_vrss_sign TEXT NULL COMMENT '응답 ovtm_untp_prdy_vrss_sign',
    rsp_ovtm_untp_prdy_ctrt TEXT NULL COMMENT '응답 ovtm_untp_prdy_ctrt',
    rsp_ovtm_untp_vol TEXT NULL COMMENT '응답 ovtm_untp_vol',
    rsp_ovtm_untp_tr_pbmn TEXT NULL COMMENT '응답 ovtm_untp_tr_pbmn',
    rsp_ovtm_untp_mxpr TEXT NULL COMMENT '응답 ovtm_untp_mxpr',
    rsp_ovtm_untp_llam TEXT NULL COMMENT '응답 ovtm_untp_llam',
    rsp_ovtm_untp_oprc TEXT NULL COMMENT '응답 ovtm_untp_oprc',
    rsp_ovtm_untp_hgpr TEXT NULL COMMENT '응답 ovtm_untp_hgpr',
    rsp_ovtm_untp_lwpr TEXT NULL COMMENT '응답 ovtm_untp_lwpr',
    rsp_ovtm_untp_antc_cnpr TEXT NULL COMMENT '응답 ovtm_untp_antc_cnpr',
    rsp_ovtm_untp_antc_cntg_vrss TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_vrss',
    rsp_ovtm_untp_antc_cntg_vrss_sign TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_vrss_sign',
    rsp_ovtm_untp_antc_cntg_ctrt TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_ctrt',
    rsp_ovtm_untp_antc_vol TEXT NULL COMMENT '응답 ovtm_untp_antc_vol',
    rsp_uplm_sign TEXT NULL COMMENT '응답 uplm_sign',
    rsp_lslm_sign TEXT NULL COMMENT '응답 lslm_sign',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_askp TEXT NULL COMMENT '응답 askp',
    rsp_bidp TEXT NULL COMMENT '응답 bidp',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_ovtm_untp_prpr TEXT NULL COMMENT '응답 ovtm_untp_prpr',
    rsp_ovtm_untp_prdy_vrss TEXT NULL COMMENT '응답 ovtm_untp_prdy_vrss',
    rsp_ovtm_untp_prdy_vrss_sign TEXT NULL COMMENT '응답 ovtm_untp_prdy_vrss_sign',
    rsp_ovtm_untp_prdy_ctrt TEXT NULL COMMENT '응답 ovtm_untp_prdy_ctrt',
    rsp_ovtm_untp_vol TEXT NULL COMMENT '응답 ovtm_untp_vol',
    rsp_ovtm_untp_tr_pbmn TEXT NULL COMMENT '응답 ovtm_untp_tr_pbmn',
    rsp_ovtm_untp_mxpr TEXT NULL COMMENT '응답 ovtm_untp_mxpr',
    rsp_ovtm_untp_llam TEXT NULL COMMENT '응답 ovtm_untp_llam',
    rsp_ovtm_untp_oprc TEXT NULL COMMENT '응답 ovtm_untp_oprc',
    rsp_ovtm_untp_hgpr TEXT NULL COMMENT '응답 ovtm_untp_hgpr',
    rsp_ovtm_untp_lwpr TEXT NULL COMMENT '응답 ovtm_untp_lwpr',
    rsp_ovtm_untp_antc_cnpr TEXT NULL COMMENT '응답 ovtm_untp_antc_cnpr',
    rsp_ovtm_untp_antc_cntg_vrss TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_vrss',
    rsp_ovtm_untp_antc_cntg_vrss_sign TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_vrss_sign',
    rsp_ovtm_untp_antc_cntg_ctrt TEXT NULL COMMENT '응답 ovtm_untp_antc_cntg_ctrt',
    rsp_ovtm_untp_antc_vol TEXT NULL COMMENT '응답 ovtm_untp_antc_vol',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_ovtm_untp_last_hour TEXT NULL COMMENT '응답 ovtm_untp_last_hour',
    rsp_ovtm_untp_askp1 TEXT NULL COMMENT '응답 ovtm_untp_askp1',
    rsp_ovtm_untp_askp2 TEXT NULL COMMENT '응답 ovtm_untp_askp2',
    rsp_ovtm_untp_askp3 TEXT NULL COMMENT '응답 ovtm_untp_askp3',
    rsp_ovtm_untp_askp4 TEXT NULL COMMENT '응답 ovtm_untp_askp4',
    rsp_ovtm_untp_askp5 TEXT NULL COMMENT '응답 ovtm_untp_askp5',
    rsp_ovtm_untp_askp6 TEXT NULL COMMENT '응답 ovtm_untp_askp6',
    rsp_ovtm_untp_askp7 TEXT NULL COMMENT '응답 ovtm_untp_askp7',
    rsp_ovtm_untp_askp8 TEXT NULL COMMENT '응답 ovtm_untp_askp8',
    rsp_ovtm_untp_askp9 TEXT NULL COMMENT '응답 ovtm_untp_askp9',
    rsp_ovtm_untp_askp10 TEXT NULL COMMENT '응답 ovtm_untp_askp10',
    rsp_ovtm_untp_bidp1 TEXT NULL COMMENT '응답 ovtm_untp_bidp1',
    rsp_ovtm_untp_bidp2 TEXT NULL COMMENT '응답 ovtm_untp_bidp2',
    rsp_ovtm_untp_bidp3 TEXT NULL COMMENT '응답 ovtm_untp_bidp3',
    rsp_ovtm_untp_bidp4 TEXT NULL COMMENT '응답 ovtm_untp_bidp4',
    rsp_ovtm_untp_bidp5 TEXT NULL COMMENT '응답 ovtm_untp_bidp5',
    rsp_ovtm_untp_bidp6 TEXT NULL COMMENT '응답 ovtm_untp_bidp6',
    rsp_ovtm_untp_bidp7 TEXT NULL COMMENT '응답 ovtm_untp_bidp7',
    rsp_ovtm_untp_bidp8 TEXT NULL COMMENT '응답 ovtm_untp_bidp8',
    rsp_ovtm_untp_bidp9 TEXT NULL COMMENT '응답 ovtm_untp_bidp9',
    rsp_ovtm_untp_bidp10 TEXT NULL COMMENT '응답 ovtm_untp_bidp10',
    rsp_ovtm_untp_askp_icdc1 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc1',
    rsp_ovtm_untp_askp_icdc2 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc2',
    rsp_ovtm_untp_askp_icdc3 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc3',
    rsp_ovtm_untp_askp_icdc4 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc4',
    rsp_ovtm_untp_askp_icdc5 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc5',
    rsp_ovtm_untp_askp_icdc6 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc6',
    rsp_ovtm_untp_askp_icdc7 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc7',
    rsp_ovtm_untp_askp_icdc8 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc8',
    rsp_ovtm_untp_askp_icdc9 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc9',
    rsp_ovtm_untp_askp_icdc10 TEXT NULL COMMENT '응답 ovtm_untp_askp_icdc10',
    rsp_ovtm_untp_bidp_icdc1 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc1',
    rsp_ovtm_untp_bidp_icdc2 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc2',
    rsp_ovtm_untp_bidp_icdc3 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc3',
    rsp_ovtm_untp_bidp_icdc4 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc4',
    rsp_ovtm_untp_bidp_icdc5 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc5',
    rsp_ovtm_untp_bidp_icdc6 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc6',
    rsp_ovtm_untp_bidp_icdc7 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc7',
    rsp_ovtm_untp_bidp_icdc8 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc8',
    rsp_ovtm_untp_bidp_icdc9 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc9',
    rsp_ovtm_untp_bidp_icdc10 TEXT NULL COMMENT '응답 ovtm_untp_bidp_icdc10',
    rsp_ovtm_untp_askp_rsqn1 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn1',
    rsp_ovtm_untp_askp_rsqn2 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn2',
    rsp_ovtm_untp_askp_rsqn3 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn3',
    rsp_ovtm_untp_askp_rsqn4 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn4',
    rsp_ovtm_untp_askp_rsqn5 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn5',
    rsp_ovtm_untp_askp_rsqn6 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn6',
    rsp_ovtm_untp_askp_rsqn7 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn7',
    rsp_ovtm_untp_askp_rsqn8 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn8',
    rsp_ovtm_untp_askp_rsqn9 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn9',
    rsp_ovtm_untp_askp_rsqn10 TEXT NULL COMMENT '응답 ovtm_untp_askp_rsqn10',
    rsp_ovtm_untp_bidp_rsqn1 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn1',
    rsp_ovtm_untp_bidp_rsqn2 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn2',
    rsp_ovtm_untp_bidp_rsqn3 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn3',
    rsp_ovtm_untp_bidp_rsqn4 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn4',
    rsp_ovtm_untp_bidp_rsqn5 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn5',
    rsp_ovtm_untp_bidp_rsqn6 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn6',
    rsp_ovtm_untp_bidp_rsqn7 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn7',
    rsp_ovtm_untp_bidp_rsqn8 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn8',
    rsp_ovtm_untp_bidp_rsqn9 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn9',
    rsp_ovtm_untp_bidp_rsqn10 TEXT NULL COMMENT '응답 ovtm_untp_bidp_rsqn10',
    rsp_ovtm_untp_total_askp_rsqn TEXT NULL COMMENT '응답 ovtm_untp_total_askp_rsqn',
    rsp_ovtm_untp_total_bidp_rsqn TEXT NULL COMMENT '응답 ovtm_untp_total_bidp_rsqn',
    rsp_ovtm_untp_total_askp_rsqn_icdc TEXT NULL COMMENT '응답 ovtm_untp_total_askp_rsqn_icdc',
    rsp_ovtm_untp_total_bidp_rsqn_icdc TEXT NULL COMMENT '응답 ovtm_untp_total_bidp_rsqn_icdc',
    rsp_ovtm_untp_ntby_bidp_rsqn TEXT NULL COMMENT '응답 ovtm_untp_ntby_bidp_rsqn',
    rsp_total_askp_rsqn TEXT NULL COMMENT '응답 total_askp_rsqn',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '응답 total_bidp_rsqn',
    rsp_total_askp_rsqn_icdc TEXT NULL COMMENT '응답 total_askp_rsqn_icdc',
    rsp_total_bidp_rsqn_icdc TEXT NULL COMMENT '응답 total_bidp_rsqn_icdc',
    rsp_ovtm_total_askp_rsqn TEXT NULL COMMENT '응답 ovtm_total_askp_rsqn',
    rsp_ovtm_total_bidp_rsqn TEXT NULL COMMENT '응답 ovtm_total_bidp_rsqn',
    rsp_ovtm_total_askp_icdc TEXT NULL COMMENT '응답 ovtm_total_askp_icdc',
    rsp_ovtm_total_bidp_icdc TEXT NULL COMMENT '응답 ovtm_total_bidp_icdc',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_stck_pbpr TEXT NULL COMMENT '응답 stck_pbpr',
    rsp_askp TEXT NULL COMMENT '응답 askp',
    rsp_bidp TEXT NULL COMMENT '응답 bidp',
    rsp_tday_rltv TEXT NULL COMMENT '응답 tday_rltv',
    rsp_cnqn TEXT NULL COMMENT '응답 cnqn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_new_hgpr_lwpr_cls_code TEXT NULL COMMENT '응답 new_hgpr_lwpr_cls_code',
    rsp_mxpr_llam_cls_code TEXT NULL COMMENT '응답 mxpr_llam_cls_code',
    rsp_crdt_able_yn TEXT NULL COMMENT '응답 crdt_able_yn',
    rsp_stck_mxpr TEXT NULL COMMENT '응답 stck_mxpr',
    rsp_elw_pblc_yn TEXT NULL COMMENT '응답 elw_pblc_yn',
    rsp_prdy_clpr_vrss_oprc_rate TEXT NULL COMMENT '응답 prdy_clpr_vrss_oprc_rate',
    rsp_crdt_rate TEXT NULL COMMENT '응답 crdt_rate',
    rsp_marg_rate TEXT NULL COMMENT '응답 marg_rate',
    rsp_lwpr_vrss_prpr TEXT NULL COMMENT '응답 lwpr_vrss_prpr',
    rsp_lwpr_vrss_prpr_sign TEXT NULL COMMENT '응답 lwpr_vrss_prpr_sign',
    rsp_prdy_clpr_vrss_lwpr_rate TEXT NULL COMMENT '응답 prdy_clpr_vrss_lwpr_rate',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_hgpr_vrss_prpr TEXT NULL COMMENT '응답 hgpr_vrss_prpr',
    rsp_hgpr_vrss_prpr_sign TEXT NULL COMMENT '응답 hgpr_vrss_prpr_sign',
    rsp_prdy_clpr_vrss_hgpr_rate TEXT NULL COMMENT '응답 prdy_clpr_vrss_hgpr_rate',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_oprc_vrss_prpr TEXT NULL COMMENT '응답 oprc_vrss_prpr',
    rsp_oprc_vrss_prpr_sign TEXT NULL COMMENT '응답 oprc_vrss_prpr_sign',
    rsp_mang_issu_yn TEXT NULL COMMENT '응답 mang_issu_yn',
    rsp_divi_app_cls_code TEXT NULL COMMENT '응답 divi_app_cls_code',
    rsp_short_over_yn TEXT NULL COMMENT '응답 short_over_yn',
    rsp_mrkt_warn_cls_code TEXT NULL COMMENT '응답 mrkt_warn_cls_code',
    rsp_invt_caful_yn TEXT NULL COMMENT '응답 invt_caful_yn',
    rsp_stange_runup_yn TEXT NULL COMMENT '응답 stange_runup_yn',
    rsp_ssts_hot_yn TEXT NULL COMMENT '응답 ssts_hot_yn',
    rsp_low_current_yn TEXT NULL COMMENT '응답 low_current_yn',
    rsp_vi_cls_code TEXT NULL COMMENT '응답 vi_cls_code',
    rsp_short_over_cls_code TEXT NULL COMMENT '응답 short_over_cls_code',
    rsp_stck_llam TEXT NULL COMMENT '응답 stck_llam',
    rsp_new_lstn_cls_name TEXT NULL COMMENT '응답 new_lstn_cls_name',
    rsp_vlnt_deal_cls_name TEXT NULL COMMENT '응답 vlnt_deal_cls_name',
    rsp_flng_cls_name TEXT NULL COMMENT '응답 flng_cls_name',
    rsp_revl_issu_reas_name TEXT NULL COMMENT '응답 revl_issu_reas_name',
    rsp_mrkt_warn_cls_name TEXT NULL COMMENT '응답 mrkt_warn_cls_name',
    rsp_stck_sdpr TEXT NULL COMMENT '응답 stck_sdpr',
    rsp_bstp_cls_code TEXT NULL COMMENT '응답 bstp_cls_code',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_insn_pbnt_yn TEXT NULL COMMENT '응답 insn_pbnt_yn',
    rsp_fcam_mod_cls_name TEXT NULL COMMENT '응답 fcam_mod_cls_name',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '응답 prdy_vrss_vol_rate',
    rsp_bstp_kor_isnm TEXT NULL COMMENT '응답 bstp_kor_isnm',
    rsp_sltr_yn TEXT NULL COMMENT '응답 sltr_yn',
    rsp_trht_yn TEXT NULL COMMENT '응답 trht_yn',
    rsp_oprc_rang_cont_yn TEXT NULL COMMENT '응답 oprc_rang_cont_yn',
    rsp_vlnt_fin_cls_code TEXT NULL COMMENT '응답 vlnt_fin_cls_code',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_pw_data_incu_yn TEXT NULL COMMENT '요청 FID_PW_DATA_INCU_YN',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID_PERIOD_DIV_CODE',
    req_fid_org_adj_prc TEXT NULL COMMENT '요청 FID_ORG_ADJ_PRC',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_stck_mxpr TEXT NULL COMMENT '응답 stck_mxpr',
    rsp_stck_llam TEXT NULL COMMENT '응답 stck_llam',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_stck_prdy_oprc TEXT NULL COMMENT '응답 stck_prdy_oprc',
    rsp_stck_prdy_hgpr TEXT NULL COMMENT '응답 stck_prdy_hgpr',
    rsp_stck_prdy_lwpr TEXT NULL COMMENT '응답 stck_prdy_lwpr',
    rsp_askp TEXT NULL COMMENT '응답 askp',
    rsp_bidp TEXT NULL COMMENT '응답 bidp',
    rsp_prdy_vrss_vol TEXT NULL COMMENT '응답 prdy_vrss_vol',
    rsp_vol_tnrt TEXT NULL COMMENT '응답 vol_tnrt',
    rsp_stck_fcam TEXT NULL COMMENT '응답 stck_fcam',
    rsp_lstn_stcn TEXT NULL COMMENT '응답 lstn_stcn',
    rsp_cpfn TEXT NULL COMMENT '응답 cpfn',
    rsp_hts_avls TEXT NULL COMMENT '응답 hts_avls',
    rsp_per TEXT NULL COMMENT '응답 per',
    rsp_eps TEXT NULL COMMENT '응답 eps',
    rsp_pbr TEXT NULL COMMENT '응답 pbr',
    rsp_itewhol_loan_rmnd_ratem TEXT NULL COMMENT '응답 itewhol_loan_rmnd_ratem',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_flng_cls_code TEXT NULL COMMENT '응답 flng_cls_code',
    rsp_prtt_rate TEXT NULL COMMENT '응답 prtt_rate',
    rsp_mod_yn TEXT NULL COMMENT '응답 mod_yn',
    rsp_revl_issu_reas TEXT NULL COMMENT '응답 revl_issu_reas',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_aspr_acpt_hour TEXT NULL COMMENT '응답 aspr_acpt_hour',
    rsp_askp1 TEXT NULL COMMENT '응답 askp1',
    rsp_askp2 TEXT NULL COMMENT '응답 askp2',
    rsp_askp3 TEXT NULL COMMENT '응답 askp3',
    rsp_askp4 TEXT NULL COMMENT '응답 askp4',
    rsp_askp5 TEXT NULL COMMENT '응답 askp5',
    rsp_askp6 TEXT NULL COMMENT '응답 askp6',
    rsp_askp7 TEXT NULL COMMENT '응답 askp7',
    rsp_askp8 TEXT NULL COMMENT '응답 askp8',
    rsp_askp9 TEXT NULL COMMENT '응답 askp9',
    rsp_askp10 TEXT NULL COMMENT '응답 askp10',
    rsp_bidp1 TEXT NULL COMMENT '응답 bidp1',
    rsp_bidp2 TEXT NULL COMMENT '응답 bidp2',
    rsp_bidp3 TEXT NULL COMMENT '응답 bidp3',
    rsp_bidp4 TEXT NULL COMMENT '응답 bidp4',
    rsp_bidp5 TEXT NULL COMMENT '응답 bidp5',
    rsp_bidp6 TEXT NULL COMMENT '응답 bidp6',
    rsp_bidp7 TEXT NULL COMMENT '응답 bidp7',
    rsp_bidp8 TEXT NULL COMMENT '응답 bidp8',
    rsp_bidp9 TEXT NULL COMMENT '응답 bidp9',
    rsp_bidp10 TEXT NULL COMMENT '응답 bidp10',
    rsp_askp_rsqn1 TEXT NULL COMMENT '응답 askp_rsqn1',
    rsp_askp_rsqn2 TEXT NULL COMMENT '응답 askp_rsqn2',
    rsp_askp_rsqn3 TEXT NULL COMMENT '응답 askp_rsqn3',
    rsp_askp_rsqn4 TEXT NULL COMMENT '응답 askp_rsqn4',
    rsp_askp_rsqn5 TEXT NULL COMMENT '응답 askp_rsqn5',
    rsp_askp_rsqn6 TEXT NULL COMMENT '응답 askp_rsqn6',
    rsp_askp_rsqn7 TEXT NULL COMMENT '응답 askp_rsqn7',
    rsp_askp_rsqn8 TEXT NULL COMMENT '응답 askp_rsqn8',
    rsp_askp_rsqn9 TEXT NULL COMMENT '응답 askp_rsqn9',
    rsp_askp_rsqn10 TEXT NULL COMMENT '응답 askp_rsqn10',
    rsp_bidp_rsqn1 TEXT NULL COMMENT '응답 bidp_rsqn1',
    rsp_bidp_rsqn2 TEXT NULL COMMENT '응답 bidp_rsqn2',
    rsp_bidp_rsqn3 TEXT NULL COMMENT '응답 bidp_rsqn3',
    rsp_bidp_rsqn4 TEXT NULL COMMENT '응답 bidp_rsqn4',
    rsp_bidp_rsqn5 TEXT NULL COMMENT '응답 bidp_rsqn5',
    rsp_bidp_rsqn6 TEXT NULL COMMENT '응답 bidp_rsqn6',
    rsp_bidp_rsqn7 TEXT NULL COMMENT '응답 bidp_rsqn7',
    rsp_bidp_rsqn8 TEXT NULL COMMENT '응답 bidp_rsqn8',
    rsp_bidp_rsqn9 TEXT NULL COMMENT '응답 bidp_rsqn9',
    rsp_bidp_rsqn10 TEXT NULL COMMENT '응답 bidp_rsqn10',
    rsp_askp_rsqn_icdc1 TEXT NULL COMMENT '응답 askp_rsqn_icdc1',
    rsp_askp_rsqn_icdc2 TEXT NULL COMMENT '응답 askp_rsqn_icdc2',
    rsp_askp_rsqn_icdc3 TEXT NULL COMMENT '응답 askp_rsqn_icdc3',
    rsp_askp_rsqn_icdc4 TEXT NULL COMMENT '응답 askp_rsqn_icdc4',
    rsp_askp_rsqn_icdc5 TEXT NULL COMMENT '응답 askp_rsqn_icdc5',
    rsp_askp_rsqn_icdc6 TEXT NULL COMMENT '응답 askp_rsqn_icdc6',
    rsp_askp_rsqn_icdc7 TEXT NULL COMMENT '응답 askp_rsqn_icdc7',
    rsp_askp_rsqn_icdc8 TEXT NULL COMMENT '응답 askp_rsqn_icdc8',
    rsp_askp_rsqn_icdc9 TEXT NULL COMMENT '응답 askp_rsqn_icdc9',
    rsp_askp_rsqn_icdc10 TEXT NULL COMMENT '응답 askp_rsqn_icdc10',
    rsp_bidp_rsqn_icdc1 TEXT NULL COMMENT '응답 bidp_rsqn_icdc1',
    rsp_bidp_rsqn_icdc2 TEXT NULL COMMENT '응답 bidp_rsqn_icdc2',
    rsp_bidp_rsqn_icdc3 TEXT NULL COMMENT '응답 bidp_rsqn_icdc3',
    rsp_bidp_rsqn_icdc4 TEXT NULL COMMENT '응답 bidp_rsqn_icdc4',
    rsp_bidp_rsqn_icdc5 TEXT NULL COMMENT '응답 bidp_rsqn_icdc5',
    rsp_bidp_rsqn_icdc6 TEXT NULL COMMENT '응답 bidp_rsqn_icdc6',
    rsp_bidp_rsqn_icdc7 TEXT NULL COMMENT '응답 bidp_rsqn_icdc7',
    rsp_bidp_rsqn_icdc8 TEXT NULL COMMENT '응답 bidp_rsqn_icdc8',
    rsp_bidp_rsqn_icdc9 TEXT NULL COMMENT '응답 bidp_rsqn_icdc9',
    rsp_bidp_rsqn_icdc10 TEXT NULL COMMENT '응답 bidp_rsqn_icdc10',
    rsp_total_askp_rsqn TEXT NULL COMMENT '응답 total_askp_rsqn',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '응답 total_bidp_rsqn',
    rsp_total_askp_rsqn_icdc TEXT NULL COMMENT '응답 total_askp_rsqn_icdc',
    rsp_total_bidp_rsqn_icdc TEXT NULL COMMENT '응답 total_bidp_rsqn_icdc',
    rsp_ovtm_total_askp_icdc TEXT NULL COMMENT '응답 ovtm_total_askp_icdc',
    rsp_ovtm_total_bidp_icdc TEXT NULL COMMENT '응답 ovtm_total_bidp_icdc',
    rsp_ovtm_total_askp_rsqn TEXT NULL COMMENT '응답 ovtm_total_askp_rsqn',
    rsp_ovtm_total_bidp_rsqn TEXT NULL COMMENT '응답 ovtm_total_bidp_rsqn',
    rsp_ntby_aspr_rsqn TEXT NULL COMMENT '응답 ntby_aspr_rsqn',
    rsp_new_mkop_cls_code TEXT NULL COMMENT '응답 new_mkop_cls_code',
    rsp_antc_mkop_cls_code TEXT NULL COMMENT '응답 antc_mkop_cls_code',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_stck_sdpr TEXT NULL COMMENT '응답 stck_sdpr',
    rsp_antc_cnpr TEXT NULL COMMENT '응답 antc_cnpr',
    rsp_antc_cntg_vrss_sign TEXT NULL COMMENT '응답 antc_cntg_vrss_sign',
    rsp_antc_cntg_vrss TEXT NULL COMMENT '응답 antc_cntg_vrss',
    rsp_antc_cntg_prdy_ctrt TEXT NULL COMMENT '응답 antc_cntg_prdy_ctrt',
    rsp_antc_vol TEXT NULL COMMENT '응답 antc_vol',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_vi_cls_code TEXT NULL COMMENT '응답 vi_cls_code',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
    rsp_tday_rltv TEXT NULL COMMENT '응답 tday_rltv',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_seln_mbcr_no1 TEXT NULL COMMENT '응답 seln_mbcr_no1',
    rsp_seln_mbcr_no2 TEXT NULL COMMENT '응답 seln_mbcr_no2',
    rsp_seln_mbcr_no3 TEXT NULL COMMENT '응답 seln_mbcr_no3',
    rsp_seln_mbcr_no4 TEXT NULL COMMENT '응답 seln_mbcr_no4',
    rsp_seln_mbcr_no5 TEXT NULL COMMENT '응답 seln_mbcr_no5',
    rsp_seln_mbcr_name1 TEXT NULL COMMENT '응답 seln_mbcr_name1',
    rsp_seln_mbcr_name2 TEXT NULL COMMENT '응답 seln_mbcr_name2',
    rsp_seln_mbcr_name3 TEXT NULL COMMENT '응답 seln_mbcr_name3',
    rsp_seln_mbcr_name4 TEXT NULL COMMENT '응답 seln_mbcr_name4',
    rsp_seln_mbcr_name5 TEXT NULL COMMENT '응답 seln_mbcr_name5',
    rsp_total_seln_qty1 TEXT NULL COMMENT '응답 total_seln_qty1',
    rsp_total_seln_qty2 TEXT NULL COMMENT '응답 total_seln_qty2',
    rsp_total_seln_qty3 TEXT NULL COMMENT '응답 total_seln_qty3',
    rsp_total_seln_qty4 TEXT NULL COMMENT '응답 total_seln_qty4',
    rsp_total_seln_qty5 TEXT NULL COMMENT '응답 total_seln_qty5',
    rsp_seln_mbcr_rlim1 TEXT NULL COMMENT '응답 seln_mbcr_rlim1',
    rsp_seln_mbcr_rlim2 TEXT NULL COMMENT '응답 seln_mbcr_rlim2',
    rsp_seln_mbcr_rlim3 TEXT NULL COMMENT '응답 seln_mbcr_rlim3',
    rsp_seln_mbcr_rlim4 TEXT NULL COMMENT '응답 seln_mbcr_rlim4',
    rsp_seln_mbcr_rlim5 TEXT NULL COMMENT '응답 seln_mbcr_rlim5',
    rsp_seln_qty_icdc1 TEXT NULL COMMENT '응답 seln_qty_icdc1',
    rsp_seln_qty_icdc2 TEXT NULL COMMENT '응답 seln_qty_icdc2',
    rsp_seln_qty_icdc3 TEXT NULL COMMENT '응답 seln_qty_icdc3',
    rsp_seln_qty_icdc4 TEXT NULL COMMENT '응답 seln_qty_icdc4',
    rsp_seln_qty_icdc5 TEXT NULL COMMENT '응답 seln_qty_icdc5',
    rsp_shnu_mbcr_no1 TEXT NULL COMMENT '응답 shnu_mbcr_no1',
    rsp_shnu_mbcr_no2 TEXT NULL COMMENT '응답 shnu_mbcr_no2',
    rsp_shnu_mbcr_no3 TEXT NULL COMMENT '응답 shnu_mbcr_no3',
    rsp_shnu_mbcr_no4 TEXT NULL COMMENT '응답 shnu_mbcr_no4',
    rsp_shnu_mbcr_no5 TEXT NULL COMMENT '응답 shnu_mbcr_no5',
    rsp_shnu_mbcr_name1 TEXT NULL COMMENT '응답 shnu_mbcr_name1',
    rsp_shnu_mbcr_name2 TEXT NULL COMMENT '응답 shnu_mbcr_name2',
    rsp_shnu_mbcr_name3 TEXT NULL COMMENT '응답 shnu_mbcr_name3',
    rsp_shnu_mbcr_name4 TEXT NULL COMMENT '응답 shnu_mbcr_name4',
    rsp_shnu_mbcr_name5 TEXT NULL COMMENT '응답 shnu_mbcr_name5',
    rsp_total_shnu_qty1 TEXT NULL COMMENT '응답 total_shnu_qty1',
    rsp_total_shnu_qty2 TEXT NULL COMMENT '응답 total_shnu_qty2',
    rsp_total_shnu_qty3 TEXT NULL COMMENT '응답 total_shnu_qty3',
    rsp_total_shnu_qty4 TEXT NULL COMMENT '응답 total_shnu_qty4',
    rsp_total_shnu_qty5 TEXT NULL COMMENT '응답 total_shnu_qty5',
    rsp_shnu_mbcr_rlim1 TEXT NULL COMMENT '응답 shnu_mbcr_rlim1',
    rsp_shnu_mbcr_rlim2 TEXT NULL COMMENT '응답 shnu_mbcr_rlim2',
    rsp_shnu_mbcr_rlim3 TEXT NULL COMMENT '응답 shnu_mbcr_rlim3',
    rsp_shnu_mbcr_rlim4 TEXT NULL COMMENT '응답 shnu_mbcr_rlim4',
    rsp_shnu_mbcr_rlim5 TEXT NULL COMMENT '응답 shnu_mbcr_rlim5',
    rsp_shnu_qty_icdc1 TEXT NULL COMMENT '응답 shnu_qty_icdc1',
    rsp_shnu_qty_icdc2 TEXT NULL COMMENT '응답 shnu_qty_icdc2',
    rsp_shnu_qty_icdc3 TEXT NULL COMMENT '응답 shnu_qty_icdc3',
    rsp_shnu_qty_icdc4 TEXT NULL COMMENT '응답 shnu_qty_icdc4',
    rsp_shnu_qty_icdc5 TEXT NULL COMMENT '응답 shnu_qty_icdc5',
    rsp_glob_total_seln_qty TEXT NULL COMMENT '응답 glob_total_seln_qty',
    rsp_glob_seln_rlim TEXT NULL COMMENT '응답 glob_seln_rlim',
    rsp_glob_ntby_qty TEXT NULL COMMENT '응답 glob_ntby_qty',
    rsp_glob_total_shnu_qty TEXT NULL COMMENT '응답 glob_total_shnu_qty',
    rsp_glob_shnu_rlim TEXT NULL COMMENT '응답 glob_shnu_rlim',
    rsp_seln_mbcr_glob_yn_1 TEXT NULL COMMENT '응답 seln_mbcr_glob_yn_1',
    rsp_seln_mbcr_glob_yn_2 TEXT NULL COMMENT '응답 seln_mbcr_glob_yn_2',
    rsp_seln_mbcr_glob_yn_3 TEXT NULL COMMENT '응답 seln_mbcr_glob_yn_3',
    rsp_seln_mbcr_glob_yn_4 TEXT NULL COMMENT '응답 seln_mbcr_glob_yn_4',
    rsp_seln_mbcr_glob_yn_5 TEXT NULL COMMENT '응답 seln_mbcr_glob_yn_5',
    rsp_shnu_mbcr_glob_yn_1 TEXT NULL COMMENT '응답 shnu_mbcr_glob_yn_1',
    rsp_shnu_mbcr_glob_yn_2 TEXT NULL COMMENT '응답 shnu_mbcr_glob_yn_2',
    rsp_shnu_mbcr_glob_yn_3 TEXT NULL COMMENT '응답 shnu_mbcr_glob_yn_3',
    rsp_shnu_mbcr_glob_yn_4 TEXT NULL COMMENT '응답 shnu_mbcr_glob_yn_4',
    rsp_shnu_mbcr_glob_yn_5 TEXT NULL COMMENT '응답 shnu_mbcr_glob_yn_5',
    rsp_glob_total_seln_qty_icdc TEXT NULL COMMENT '응답 glob_total_seln_qty_icdc',
    rsp_glob_total_shnu_qty_icdc TEXT NULL COMMENT '응답 glob_total_shnu_qty_icdc',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '응답 prsn_ntby_qty',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '응답 orgn_ntby_qty',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '응답 prsn_ntby_tr_pbmn',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 frgn_ntby_tr_pbmn',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 orgn_ntby_tr_pbmn',
    rsp_prsn_shnu_vol TEXT NULL COMMENT '응답 prsn_shnu_vol',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '응답 frgn_shnu_vol',
    rsp_orgn_shnu_vol TEXT NULL COMMENT '응답 orgn_shnu_vol',
    rsp_prsn_shnu_tr_pbmn TEXT NULL COMMENT '응답 prsn_shnu_tr_pbmn',
    rsp_frgn_shnu_tr_pbmn TEXT NULL COMMENT '응답 frgn_shnu_tr_pbmn',
    rsp_orgn_shnu_tr_pbmn TEXT NULL COMMENT '응답 orgn_shnu_tr_pbmn',
    rsp_prsn_seln_vol TEXT NULL COMMENT '응답 prsn_seln_vol',
    rsp_frgn_seln_vol TEXT NULL COMMENT '응답 frgn_seln_vol',
    rsp_orgn_seln_vol TEXT NULL COMMENT '응답 orgn_seln_vol',
    rsp_prsn_seln_tr_pbmn TEXT NULL COMMENT '응답 prsn_seln_tr_pbmn',
    rsp_frgn_seln_tr_pbmn TEXT NULL COMMENT '응답 frgn_seln_tr_pbmn',
    rsp_orgn_seln_tr_pbmn TEXT NULL COMMENT '응답 orgn_seln_tr_pbmn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_blng_cls_code TEXT NULL COMMENT '요청 FID_BLNG_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_sdpr_vrss_prpr TEXT NULL COMMENT '응답 sdpr_vrss_prpr',
    rsp_sdpr_vrss_prpr_rate TEXT NULL COMMENT '응답 sdpr_vrss_prpr_rate',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    req_fid_pw_data_incu_yn TEXT NULL COMMENT '요청 FID_PW_DATA_INCU_YN',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID_ETC_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_elw_shrn_iscd TEXT NULL COMMENT '응답 elw_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_elw_prpr TEXT NULL COMMENT '응답 elw_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '응답 prdy_vrss_vol_rate',
    rsp_unas_shrn_iscd TEXT NULL COMMENT '응답 unas_shrn_iscd',
    rsp_unas_isnm TEXT NULL COMMENT '응답 unas_isnm',
    rsp_unas_prpr TEXT NULL COMMENT '응답 unas_prpr',
    rsp_unas_prdy_vrss TEXT NULL COMMENT '응답 unas_prdy_vrss',
    rsp_unas_prdy_vrss_sign TEXT NULL COMMENT '응답 unas_prdy_vrss_sign',
    rsp_unas_prdy_ctrt TEXT NULL COMMENT '응답 unas_prdy_ctrt',
    rsp_bidp TEXT NULL COMMENT '응답 bidp',
    rsp_askp TEXT NULL COMMENT '응답 askp',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_vol_tnrt TEXT NULL COMMENT '응답 vol_tnrt',
    rsp_elw_oprc TEXT NULL COMMENT '응답 elw_oprc',
    rsp_elw_hgpr TEXT NULL COMMENT '응답 elw_hgpr',
    rsp_elw_lwpr TEXT NULL COMMENT '응답 elw_lwpr',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_hts_thpr TEXT NULL COMMENT '응답 hts_thpr',
    rsp_dprt TEXT NULL COMMENT '응답 dprt',
    rsp_atm_cls_name TEXT NULL COMMENT '응답 atm_cls_name',
    rsp_hts_ints_vltl TEXT NULL COMMENT '응답 hts_ints_vltl',
    rsp_acpr TEXT NULL COMMENT '응답 acpr',
    rsp_pvt_scnd_dmrs_prc TEXT NULL COMMENT '응답 pvt_scnd_dmrs_prc',
    rsp_pvt_frst_dmrs_prc TEXT NULL COMMENT '응답 pvt_frst_dmrs_prc',
    rsp_pvt_pont_val TEXT NULL COMMENT '응답 pvt_pont_val',
    rsp_pvt_frst_dmsp_prc TEXT NULL COMMENT '응답 pvt_frst_dmsp_prc',
    rsp_pvt_scnd_dmsp_prc TEXT NULL COMMENT '응답 pvt_scnd_dmsp_prc',
    rsp_dmsp_val TEXT NULL COMMENT '응답 dmsp_val',
    rsp_dmrs_val TEXT NULL COMMENT '응답 dmrs_val',
    rsp_elw_sdpr TEXT NULL COMMENT '응답 elw_sdpr',
    rsp_apprch_rate TEXT NULL COMMENT '응답 apprch_rate',
    rsp_tick_conv_prc TEXT NULL COMMENT '응답 tick_conv_prc',
    rsp_invt_epmd_cntt TEXT NULL COMMENT '응답 invt_epmd_cntt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_mkop_cls_code TEXT NULL COMMENT '요청 FID_MKOP_CLS_CODE',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID_PERIOD_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_prdy_nmix TEXT NULL COMMENT '응답 prdy_nmix',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_cls_code TEXT NULL COMMENT '응답 bstp_cls_code',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '응답 bstp_nmix_oprc',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '응답 bstp_nmix_hgpr',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '응답 bstp_nmix_lwpr',
    rsp_futs_prdy_oprc TEXT NULL COMMENT '응답 futs_prdy_oprc',
    rsp_futs_prdy_hgpr TEXT NULL COMMENT '응답 futs_prdy_hgpr',
    rsp_futs_prdy_lwpr TEXT NULL COMMENT '응답 futs_prdy_lwpr',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_mod_yn TEXT NULL COMMENT '응답 mod_yn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_hour TEXT NULL COMMENT '응답 bsop_hour',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_blng_cls_code TEXT NULL COMMENT '요청 FID_BLNG_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '응답 bstp_nmix_oprc',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '응답 bstp_nmix_hgpr',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '응답 bstp_nmix_lwpr',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '응답 ascn_issu_cnt',
    rsp_down_issu_cnt TEXT NULL COMMENT '응답 down_issu_cnt',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '응답 stnr_issu_cnt',
    rsp_uplm_issu_cnt TEXT NULL COMMENT '응답 uplm_issu_cnt',
    rsp_lslm_issu_cnt TEXT NULL COMMENT '응답 lslm_issu_cnt',
    rsp_prdy_tr_pbmn TEXT NULL COMMENT '응답 prdy_tr_pbmn',
    rsp_dryy_bstp_nmix_hgpr_date TEXT NULL COMMENT '응답 dryy_bstp_nmix_hgpr_date',
    rsp_dryy_bstp_nmix_hgpr TEXT NULL COMMENT '응답 dryy_bstp_nmix_hgpr',
    rsp_dryy_bstp_nmix_lwpr TEXT NULL COMMENT '응답 dryy_bstp_nmix_lwpr',
    rsp_dryy_bstp_nmix_lwpr_date TEXT NULL COMMENT '응답 dryy_bstp_nmix_lwpr_date',
    rsp_bstp_cls_code TEXT NULL COMMENT '응답 bstp_cls_code',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_acml_vol_rlim TEXT NULL COMMENT '응답 acml_vol_rlim',
    rsp_acml_tr_pbmn_rlim TEXT NULL COMMENT '응답 acml_tr_pbmn_rlim',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID_ETC_CLS_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    req_fid_pw_data_incu_yn TEXT NULL COMMENT '요청 FID_PW_DATA_INCU_YN',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_output1 TEXT NULL COMMENT '응답 Output1',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_prdy_nmix TEXT NULL COMMENT '응답 prdy_nmix',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_cls_code TEXT NULL COMMENT '응답 bstp_cls_code',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '응답 bstp_nmix_oprc',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '응답 bstp_nmix_hgpr',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '응답 bstp_nmix_lwpr',
    rsp_futs_prdy_oprc TEXT NULL COMMENT '응답 futs_prdy_oprc',
    rsp_futs_prdy_hgpr TEXT NULL COMMENT '응답 futs_prdy_hgpr',
    rsp_futs_prdy_lwpr TEXT NULL COMMENT '응답 futs_prdy_lwpr',
    rsp_output2 TEXT NULL COMMENT '응답 Output2',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_bass_dt TEXT NULL COMMENT '요청 BASS_DT',
    req_ctx_area_nk TEXT NULL COMMENT '요청 CTX_AREA_NK',
    req_ctx_area_fk TEXT NULL COMMENT '요청 CTX_AREA_FK',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bass_dt TEXT NULL COMMENT '응답 bass_dt',
    rsp_wday_dvsn_cd TEXT NULL COMMENT '응답 wday_dvsn_cd',
    rsp_bzdy_yn TEXT NULL COMMENT '응답 bzdy_yn',
    rsp_tr_day_yn TEXT NULL COMMENT '응답 tr_day_yn',
    rsp_opnd_yn TEXT NULL COMMENT '응답 opnd_yn',
    rsp_sttl_day_yn TEXT NULL COMMENT '응답 sttl_day_yn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 fid_mrkt_cls_code',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd TEXT NULL COMMENT '요청 fid_input_iscd',
    req_fid_mkop_cls_code TEXT NULL COMMENT '요청 fid_mkop_cls_code',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '응답 ascn_issu_cnt',
    rsp_down_issu_cnt TEXT NULL COMMENT '응답 down_issu_cnt',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '응답 stnr_issu_cnt',
    rsp_bstp_cls_code TEXT NULL COMMENT '응답 bstp_cls_code',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_nmix_sdpr TEXT NULL COMMENT '응답 nmix_sdpr',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_prdy_tr_pbmn TEXT NULL COMMENT '응답 prdy_tr_pbmn',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '응답 bstp_nmix_oprc',
    rsp_prdy_nmix_vrss_nmix_oprc TEXT NULL COMMENT '응답 prdy_nmix_vrss_nmix_oprc',
    rsp_oprc_vrss_prpr_sign TEXT NULL COMMENT '응답 oprc_vrss_prpr_sign',
    rsp_bstp_nmix_oprc_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_oprc_prdy_ctrt',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '응답 bstp_nmix_hgpr',
    rsp_prdy_nmix_vrss_nmix_hgpr TEXT NULL COMMENT '응답 prdy_nmix_vrss_nmix_hgpr',
    rsp_hgpr_vrss_prpr_sign TEXT NULL COMMENT '응답 hgpr_vrss_prpr_sign',
    rsp_bstp_nmix_hgpr_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_hgpr_prdy_ctrt',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '응답 bstp_nmix_lwpr',
    rsp_prdy_clpr_vrss_lwpr TEXT NULL COMMENT '응답 prdy_clpr_vrss_lwpr',
    rsp_lwpr_vrss_prpr_sign TEXT NULL COMMENT '응답 lwpr_vrss_prpr_sign',
    rsp_prdy_clpr_vrss_lwpr_rate TEXT NULL COMMENT '응답 prdy_clpr_vrss_lwpr_rate',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '응답 ascn_issu_cnt',
    rsp_uplm_issu_cnt TEXT NULL COMMENT '응답 uplm_issu_cnt',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '응답 stnr_issu_cnt',
    rsp_down_issu_cnt TEXT NULL COMMENT '응답 down_issu_cnt',
    rsp_lslm_issu_cnt TEXT NULL COMMENT '응답 lslm_issu_cnt',
    rsp_dryy_bstp_nmix_hgpr TEXT NULL COMMENT '응답 dryy_bstp_nmix_hgpr',
    rsp_dryy_hgpr_vrss_prpr_rate TEXT NULL COMMENT '응답 dryy_hgpr_vrss_prpr_rate',
    rsp_dryy_bstp_nmix_hgpr_date TEXT NULL COMMENT '응답 dryy_bstp_nmix_hgpr_date',
    rsp_dryy_bstp_nmix_lwpr TEXT NULL COMMENT '응답 dryy_bstp_nmix_lwpr',
    rsp_dryy_lwpr_vrss_prpr_rate TEXT NULL COMMENT '응답 dryy_lwpr_vrss_prpr_rate',
    rsp_dryy_bstp_nmix_lwpr_date TEXT NULL COMMENT '응답 dryy_bstp_nmix_lwpr_date',
    rsp_total_askp_rsqn TEXT NULL COMMENT '응답 total_askp_rsqn',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '응답 total_bidp_rsqn',
    rsp_seln_rsqn_rate TEXT NULL COMMENT '응답 seln_rsqn_rate',
    rsp_shnu_rsqn_rate TEXT NULL COMMENT '응답 shnu_rsqn_rate',
    rsp_ntby_rsqn TEXT NULL COMMENT '응답 ntby_rsqn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_date1 TEXT NULL COMMENT '응답 date1',
    rsp_date2 TEXT NULL COMMENT '응답 date2',
    rsp_date3 TEXT NULL COMMENT '응답 date3',
    rsp_date4 TEXT NULL COMMENT '응답 date4',
    rsp_date5 TEXT NULL COMMENT '응답 date5',
    rsp_today TEXT NULL COMMENT '응답 today',
    rsp_time TEXT NULL COMMENT '응답 time',
    rsp_s_time TEXT NULL COMMENT '응답 s_time',
    rsp_e_time TEXT NULL COMMENT '응답 e_time',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID_PERIOD_DIV_CODE',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '응답 bstp_nmix_oprc',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '응답 bstp_nmix_hgpr',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '응답 bstp_nmix_lwpr',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_ascn_issu_cnt TEXT NULL COMMENT '응답 ascn_issu_cnt',
    rsp_down_issu_cnt TEXT NULL COMMENT '응답 down_issu_cnt',
    rsp_stnr_issu_cnt TEXT NULL COMMENT '응답 stnr_issu_cnt',
    rsp_uplm_issu_cnt TEXT NULL COMMENT '응답 uplm_issu_cnt',
    rsp_lslm_issu_cnt TEXT NULL COMMENT '응답 lslm_issu_cnt',
    rsp_prdy_tr_pbmn TEXT NULL COMMENT '응답 prdy_tr_pbmn',
    rsp_dryy_bstp_nmix_hgpr_date TEXT NULL COMMENT '응답 dryy_bstp_nmix_hgpr_date',
    rsp_dryy_bstp_nmix_hgpr TEXT NULL COMMENT '응답 dryy_bstp_nmix_hgpr',
    rsp_dryy_bstp_nmix_lwpr TEXT NULL COMMENT '응답 dryy_bstp_nmix_lwpr',
    rsp_dryy_bstp_nmix_lwpr_date TEXT NULL COMMENT '응답 dryy_bstp_nmix_lwpr_date',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_acml_vol_rlim TEXT NULL COMMENT '응답 acml_vol_rlim',
    rsp_invt_new_psdg TEXT NULL COMMENT '응답 invt_new_psdg',
    rsp_d20_dsrt TEXT NULL COMMENT '응답 d20_dsrt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_div_cls_code1 TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bcdt_code TEXT NULL COMMENT '응답 bcdt_code',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_bond_mnrt_prpr TEXT NULL COMMENT '응답 bond_mnrt_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bond_mnrt_prdy_vrss TEXT NULL COMMENT '응답 bond_mnrt_prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_trgt_cls_code TEXT NULL COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code TEXT NULL COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '응답 mksc_shrn_iscd',
    rsp_vi_cls_code TEXT NULL COMMENT '응답 vi_cls_code',
    rsp_bsop_date TEXT NULL COMMENT '응답 bsop_date',
    rsp_cntg_vi_hour TEXT NULL COMMENT '응답 cntg_vi_hour',
    rsp_vi_cncl_hour TEXT NULL COMMENT '응답 vi_cncl_hour',
    rsp_vi_kind_code TEXT NULL COMMENT '응답 vi_kind_code',
    rsp_vi_prc TEXT NULL COMMENT '응답 vi_prc',
    rsp_vi_stnd_prc TEXT NULL COMMENT '응답 vi_stnd_prc',
    rsp_vi_dprt TEXT NULL COMMENT '응답 vi_dprt',
    rsp_vi_dmc_stnd_prc TEXT NULL COMMENT '응답 vi_dmc_stnd_prc',
    rsp_vi_dmc_dprt TEXT NULL COMMENT '응답 vi_dmc_dprt',
    rsp_vi_count TEXT NULL COMMENT '응답 vi_count',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_news_ofer_entp_code TEXT NULL COMMENT '요청 FID_NEWS_OFER_ENTP_CODE',
    req_fid_cond_mrkt_cls_code TEXT NULL COMMENT '요청 FID_COND_MRKT_CLS_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_titl_cntt TEXT NULL COMMENT '요청 FID_TITL_CNTT',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_input_srno TEXT NULL COMMENT '요청 FID_INPUT_SRNO',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_cntt_usiq_srno TEXT NULL COMMENT '응답 cntt_usiq_srno',
    rsp_news_ofer_entp_code TEXT NULL COMMENT '응답 news_ofer_entp_code',
    rsp_data_dt TEXT NULL COMMENT '응답 data_dt',
    rsp_data_tm TEXT NULL COMMENT '응답 data_tm',
    rsp_hts_pbnt_titl_cntt TEXT NULL COMMENT '응답 hts_pbnt_titl_cntt',
    rsp_news_lrdv_code TEXT NULL COMMENT '응답 news_lrdv_code',
    rsp_dorg TEXT NULL COMMENT '응답 dorg',
    rsp_iscd1 TEXT NULL COMMENT '응답 iscd1',
    rsp_iscd2 TEXT NULL COMMENT '응답 iscd2',
    rsp_iscd3 TEXT NULL COMMENT '응답 iscd3',
    rsp_iscd4 TEXT NULL COMMENT '응답 iscd4',
    rsp_iscd5 TEXT NULL COMMENT '응답 iscd5',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_pdno TEXT NULL COMMENT '요청 PDNO',
    req_prdt_type_cd TEXT NULL COMMENT '요청 PRDT_TYPE_CD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_pdno TEXT NULL COMMENT '응답 pdno',
    rsp_prdt_type_cd TEXT NULL COMMENT '응답 prdt_type_cd',
    rsp_prdt_name TEXT NULL COMMENT '응답 prdt_name',
    rsp_prdt_name120 TEXT NULL COMMENT '응답 prdt_name120',
    rsp_prdt_abrv_name TEXT NULL COMMENT '응답 prdt_abrv_name',
    rsp_prdt_eng_name TEXT NULL COMMENT '응답 prdt_eng_name',
    rsp_prdt_eng_name120 TEXT NULL COMMENT '응답 prdt_eng_name120',
    rsp_prdt_eng_abrv_name TEXT NULL COMMENT '응답 prdt_eng_abrv_name',
    rsp_std_pdno TEXT NULL COMMENT '응답 std_pdno',
    rsp_shtn_pdno TEXT NULL COMMENT '응답 shtn_pdno',
    rsp_prdt_sale_stat_cd TEXT NULL COMMENT '응답 prdt_sale_stat_cd',
    rsp_prdt_risk_grad_cd TEXT NULL COMMENT '응답 prdt_risk_grad_cd',
    rsp_prdt_clsf_cd TEXT NULL COMMENT '응답 prdt_clsf_cd',
    rsp_prdt_clsf_name TEXT NULL COMMENT '응답 prdt_clsf_name',
    rsp_sale_strt_dt TEXT NULL COMMENT '응답 sale_strt_dt',
    rsp_sale_end_dt TEXT NULL COMMENT '응답 sale_end_dt',
    rsp_wrap_asst_type_cd TEXT NULL COMMENT '응답 wrap_asst_type_cd',
    rsp_ivst_prdt_type_cd TEXT NULL COMMENT '응답 ivst_prdt_type_cd',
    rsp_ivst_prdt_type_cd_name TEXT NULL COMMENT '응답 ivst_prdt_type_cd_name',
    rsp_frst_erlm_dt TEXT NULL COMMENT '응답 frst_erlm_dt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_invt_opnn TEXT NULL COMMENT '응답 invt_opnn',
    rsp_invt_opnn_cls_code TEXT NULL COMMENT '응답 invt_opnn_cls_code',
    rsp_rgbf_invt_opnn TEXT NULL COMMENT '응답 rgbf_invt_opnn',
    rsp_rgbf_invt_opnn_cls_code TEXT NULL COMMENT '응답 rgbf_invt_opnn_cls_code',
    rsp_mbcr_name TEXT NULL COMMENT '응답 mbcr_name',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_hts_goal_prc TEXT NULL COMMENT '응답 hts_goal_prc',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_stft_esdg TEXT NULL COMMENT '응답 stft_esdg',
    rsp_dprt TEXT NULL COMMENT '응답 dprt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_slct_yn TEXT NULL COMMENT '요청 fid_slct_yn',
    req_fid_input_iscd TEXT NULL COMMENT '요청 fid_input_iscd',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 fid_cond_scr_div_code',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 fid_cond_mrkt_div_code',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_crdt_rate TEXT NULL COMMENT '응답 crdt_rate',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_invt_opnn TEXT NULL COMMENT '응답 invt_opnn',
    rsp_invt_opnn_cls_code TEXT NULL COMMENT '응답 invt_opnn_cls_code',
    rsp_rgbf_invt_opnn TEXT NULL COMMENT '응답 rgbf_invt_opnn',
    rsp_rgbf_invt_opnn_cls_code TEXT NULL COMMENT '응답 rgbf_invt_opnn_cls_code',
    rsp_mbcr_name TEXT NULL COMMENT '응답 mbcr_name',
    rsp_hts_goal_prc TEXT NULL COMMENT '응답 hts_goal_prc',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_stck_nday_esdg TEXT NULL COMMENT '응답 stck_nday_esdg',
    rsp_nday_dprt TEXT NULL COMMENT '응답 nday_dprt',
    rsp_stft_esdg TEXT NULL COMMENT '응답 stft_esdg',
    rsp_dprt TEXT NULL COMMENT '응답 dprt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_excg_dvsn_cd TEXT NULL COMMENT '요청 EXCG_DVSN_CD',
    req_pdno TEXT NULL COMMENT '요청 PDNO',
    req_thco_stln_psbl_yn TEXT NULL COMMENT '요청 THCO_STLN_PSBL_YN',
    req_inqr_dvsn_1 TEXT NULL COMMENT '요청 INQR_DVSN_1',
    req_ctx_area_fk200 TEXT NULL COMMENT '요청 CTX_AREA_FK200',
    req_ctx_area_nk100 TEXT NULL COMMENT '요청 CTX_AREA_NK100',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_pdno TEXT NULL COMMENT '응답 pdno',
    rsp_prdt_name TEXT NULL COMMENT '응답 prdt_name',
    rsp_papr TEXT NULL COMMENT '응답 papr',
    rsp_bfdy_clpr TEXT NULL COMMENT '응답 bfdy_clpr',
    rsp_sbst_prvs TEXT NULL COMMENT '응답 sbst_prvs',
    rsp_tr_stop_dvsn_name TEXT NULL COMMENT '응답 tr_stop_dvsn_name',
    rsp_psbl_yn_name TEXT NULL COMMENT '응답 psbl_yn_name',
    rsp_lmt_qty1 TEXT NULL COMMENT '응답 lmt_qty1',
    rsp_use_qty1 TEXT NULL COMMENT '응답 use_qty1',
    rsp_trad_psbl_qty2 TEXT NULL COMMENT '응답 trad_psbl_qty2',
    rsp_rght_type_cd TEXT NULL COMMENT '응답 rght_type_cd',
    rsp_bass_dt TEXT NULL COMMENT '응답 bass_dt',
    rsp_psbl_yn TEXT NULL COMMENT '응답 psbl_yn',
    rsp_tot_stup_lmt_qty TEXT NULL COMMENT '응답 tot_stup_lmt_qty',
    rsp_brch_lmt_qty TEXT NULL COMMENT '응답 brch_lmt_qty',
    rsp_rqst_psbl_qty TEXT NULL COMMENT '응답 rqst_psbl_qty',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_prdt_type_cd TEXT NULL COMMENT '요청 PRDT_TYPE_CD',
    req_pdno TEXT NULL COMMENT '요청 PDNO',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_pdno TEXT NULL COMMENT '응답 pdno',
    rsp_prdt_type_cd TEXT NULL COMMENT '응답 prdt_type_cd',
    rsp_mket_id_cd TEXT NULL COMMENT '응답 mket_id_cd',
    rsp_scty_grp_id_cd TEXT NULL COMMENT '응답 scty_grp_id_cd',
    rsp_excg_dvsn_cd TEXT NULL COMMENT '응답 excg_dvsn_cd',
    rsp_setl_mmdd TEXT NULL COMMENT '응답 setl_mmdd',
    rsp_lstg_stqt TEXT NULL COMMENT '응답 lstg_stqt',
    rsp_lstg_cptl_amt TEXT NULL COMMENT '응답 lstg_cptl_amt',
    rsp_cpta TEXT NULL COMMENT '응답 cpta',
    rsp_papr TEXT NULL COMMENT '응답 papr',
    rsp_issu_pric TEXT NULL COMMENT '응답 issu_pric',
    rsp_kospi200_item_yn TEXT NULL COMMENT '응답 kospi200_item_yn',
    rsp_scts_mket_lstg_dt TEXT NULL COMMENT '응답 scts_mket_lstg_dt',
    rsp_scts_mket_lstg_abol_dt TEXT NULL COMMENT '응답 scts_mket_lstg_abol_dt',
    rsp_kosdaq_mket_lstg_dt TEXT NULL COMMENT '응답 kosdaq_mket_lstg_dt',
    rsp_kosdaq_mket_lstg_abol_dt TEXT NULL COMMENT '응답 kosdaq_mket_lstg_abol_dt',
    rsp_frbd_mket_lstg_dt TEXT NULL COMMENT '응답 frbd_mket_lstg_dt',
    rsp_frbd_mket_lstg_abol_dt TEXT NULL COMMENT '응답 frbd_mket_lstg_abol_dt',
    rsp_reits_kind_cd TEXT NULL COMMENT '응답 reits_kind_cd',
    rsp_etf_dvsn_cd TEXT NULL COMMENT '응답 etf_dvsn_cd',
    rsp_oilf_fund_yn TEXT NULL COMMENT '응답 oilf_fund_yn',
    rsp_idx_bztp_lcls_cd TEXT NULL COMMENT '응답 idx_bztp_lcls_cd',
    rsp_idx_bztp_mcls_cd TEXT NULL COMMENT '응답 idx_bztp_mcls_cd',
    rsp_idx_bztp_scls_cd TEXT NULL COMMENT '응답 idx_bztp_scls_cd',
    rsp_stck_kind_cd TEXT NULL COMMENT '응답 stck_kind_cd',
    rsp_mfnd_opng_dt TEXT NULL COMMENT '응답 mfnd_opng_dt',
    rsp_mfnd_end_dt TEXT NULL COMMENT '응답 mfnd_end_dt',
    rsp_dpsi_erlm_cncl_dt TEXT NULL COMMENT '응답 dpsi_erlm_cncl_dt',
    rsp_etf_cu_qty TEXT NULL COMMENT '응답 etf_cu_qty',
    rsp_prdt_name TEXT NULL COMMENT '응답 prdt_name',
    rsp_prdt_name120 TEXT NULL COMMENT '응답 prdt_name120',
    rsp_prdt_abrv_name TEXT NULL COMMENT '응답 prdt_abrv_name',
    rsp_std_pdno TEXT NULL COMMENT '응답 std_pdno',
    rsp_prdt_eng_name TEXT NULL COMMENT '응답 prdt_eng_name',
    rsp_prdt_eng_name120 TEXT NULL COMMENT '응답 prdt_eng_name120',
    rsp_prdt_eng_abrv_name TEXT NULL COMMENT '응답 prdt_eng_abrv_name',
    rsp_dpsi_aptm_erlm_yn TEXT NULL COMMENT '응답 dpsi_aptm_erlm_yn',
    rsp_etf_txtn_type_cd TEXT NULL COMMENT '응답 etf_txtn_type_cd',
    rsp_etf_type_cd TEXT NULL COMMENT '응답 etf_type_cd',
    rsp_lstg_abol_dt TEXT NULL COMMENT '응답 lstg_abol_dt',
    rsp_nwst_odst_dvsn_cd TEXT NULL COMMENT '응답 nwst_odst_dvsn_cd',
    rsp_sbst_pric TEXT NULL COMMENT '응답 sbst_pric',
    rsp_thco_sbst_pric TEXT NULL COMMENT '응답 thco_sbst_pric',
    rsp_thco_sbst_pric_chng_dt TEXT NULL COMMENT '응답 thco_sbst_pric_chng_dt',
    rsp_tr_stop_yn TEXT NULL COMMENT '응답 tr_stop_yn',
    rsp_admn_item_yn TEXT NULL COMMENT '응답 admn_item_yn',
    rsp_thdt_clpr TEXT NULL COMMENT '응답 thdt_clpr',
    rsp_bfdy_clpr TEXT NULL COMMENT '응답 bfdy_clpr',
    rsp_clpr_chng_dt TEXT NULL COMMENT '응답 clpr_chng_dt',
    rsp_std_idst_clsf_cd TEXT NULL COMMENT '응답 std_idst_clsf_cd',
    rsp_std_idst_clsf_cd_name TEXT NULL COMMENT '응답 std_idst_clsf_cd_name',
    rsp_idx_bztp_lcls_cd_name TEXT NULL COMMENT '응답 idx_bztp_lcls_cd_name',
    rsp_idx_bztp_mcls_cd_name TEXT NULL COMMENT '응답 idx_bztp_mcls_cd_name',
    rsp_idx_bztp_scls_cd_name TEXT NULL COMMENT '응답 idx_bztp_scls_cd_name',
    rsp_ocr_no TEXT NULL COMMENT '응답 ocr_no',
    rsp_crfd_item_yn TEXT NULL COMMENT '응답 crfd_item_yn',
    rsp_elec_scty_yn TEXT NULL COMMENT '응답 elec_scty_yn',
    rsp_issu_istt_cd TEXT NULL COMMENT '응답 issu_istt_cd',
    rsp_etf_chas_erng_rt_dbnb TEXT NULL COMMENT '응답 etf_chas_erng_rt_dbnb',
    rsp_etf_etn_ivst_heed_item_yn TEXT NULL COMMENT '응답 etf_etn_ivst_heed_item_yn',
    rsp_stln_int_rt_dvsn_cd TEXT NULL COMMENT '응답 stln_int_rt_dvsn_cd',
    rsp_frnr_psnl_lmt_rt TEXT NULL COMMENT '응답 frnr_psnl_lmt_rt',
    rsp_lstg_rqsr_issu_istt_cd TEXT NULL COMMENT '응답 lstg_rqsr_issu_istt_cd',
    rsp_lstg_rqsr_item_cd TEXT NULL COMMENT '응답 lstg_rqsr_item_cd',
    rsp_trst_istt_issu_istt_cd TEXT NULL COMMENT '응답 trst_istt_issu_istt_cd',
    rsp_cptt_trad_tr_psbl_yn TEXT NULL COMMENT '응답 cptt_trad_tr_psbl_yn',
    rsp_nxt_tr_stop_yn TEXT NULL COMMENT '응답 nxt_tr_stop_yn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_sht_cd TEXT NULL COMMENT '요청 SHT_CD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_sht_cd TEXT NULL COMMENT '응답 sht_cd',
    rsp_item_kor_nm TEXT NULL COMMENT '응답 item_kor_nm',
    rsp_name1 TEXT NULL COMMENT '응답 name1',
    rsp_name2 TEXT NULL COMMENT '응답 name2',
    rsp_estdate TEXT NULL COMMENT '응답 estdate',
    rsp_rcmd_name TEXT NULL COMMENT '응답 rcmd_name',
    rsp_capital TEXT NULL COMMENT '응답 capital',
    rsp_forn_item_lmtrt TEXT NULL COMMENT '응답 forn_item_lmtrt',
    rsp_data1 TEXT NULL COMMENT '응답 data1',
    rsp_data2 TEXT NULL COMMENT '응답 data2',
    rsp_data3 TEXT NULL COMMENT '응답 data3',
    rsp_data4 TEXT NULL COMMENT '응답 data4',
    rsp_data5 TEXT NULL COMMENT '응답 data5',
    rsp_output3 TEXT NULL COMMENT '응답 output3',
    rsp_output4 TEXT NULL COMMENT '응답 output4',
    rsp_dt TEXT NULL COMMENT '응답 dt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_sctn_cls_code TEXT NULL COMMENT '요청 FID_SCTN_CLS_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_mrkt_div_code1 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE1',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_hour TEXT NULL COMMENT '응답 bsop_hour',
    rsp_arbt_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 arbt_smtn_seln_tr_pbmn',
    rsp_arbt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_smtm_seln_tr_pbmn_rate',
    rsp_arbt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 arbt_smtn_shnu_tr_pbmn',
    rsp_arbt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_smtm_shun_tr_pbmn_rate',
    rsp_nabt_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 nabt_smtn_seln_tr_pbmn',
    rsp_nabt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_smtm_seln_tr_pbmn_rate',
    rsp_nabt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 nabt_smtn_shnu_tr_pbmn',
    rsp_nabt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_smtm_shun_tr_pbmn_rate',
    rsp_arbt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 arbt_smtn_ntby_tr_pbmn',
    rsp_arbt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_smtm_ntby_tr_pbmn_rate',
    rsp_nabt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 nabt_smtn_ntby_tr_pbmn',
    rsp_nabt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_smtm_ntby_tr_pbmn_rate',
    rsp_whol_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_ntby_tr_pbmn',
    rsp_whol_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_ntby_tr_pbmn_rate',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd TEXT NULL COMMENT '요청 fid_input_iscd',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 fid_input_date_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_deal_date TEXT NULL COMMENT '응답 deal_date',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_stlm_date TEXT NULL COMMENT '응답 stlm_date',
    rsp_whol_loan_new_stcn TEXT NULL COMMENT '응답 whol_loan_new_stcn',
    rsp_whol_loan_rdmp_stcn TEXT NULL COMMENT '응답 whol_loan_rdmp_stcn',
    rsp_whol_loan_rmnd_stcn TEXT NULL COMMENT '응답 whol_loan_rmnd_stcn',
    rsp_whol_loan_new_amt TEXT NULL COMMENT '응답 whol_loan_new_amt',
    rsp_whol_loan_rdmp_amt TEXT NULL COMMENT '응답 whol_loan_rdmp_amt',
    rsp_whol_loan_rmnd_amt TEXT NULL COMMENT '응답 whol_loan_rmnd_amt',
    rsp_whol_loan_rmnd_rate TEXT NULL COMMENT '응답 whol_loan_rmnd_rate',
    rsp_whol_loan_gvrt TEXT NULL COMMENT '응답 whol_loan_gvrt',
    rsp_whol_stln_new_stcn TEXT NULL COMMENT '응답 whol_stln_new_stcn',
    rsp_whol_stln_rdmp_stcn TEXT NULL COMMENT '응답 whol_stln_rdmp_stcn',
    rsp_whol_stln_rmnd_stcn TEXT NULL COMMENT '응답 whol_stln_rmnd_stcn',
    rsp_whol_stln_new_amt TEXT NULL COMMENT '응답 whol_stln_new_amt',
    rsp_whol_stln_rdmp_amt TEXT NULL COMMENT '응답 whol_stln_rdmp_amt',
    rsp_whol_stln_rmnd_amt TEXT NULL COMMENT '응답 whol_stln_rmnd_amt',
    rsp_whol_stln_rmnd_rate TEXT NULL COMMENT '응답 whol_stln_rmnd_rate',
    rsp_whol_stln_gvrt TEXT NULL COMMENT '응답 whol_stln_gvrt',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_iscd_1 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_bstp_nmix_prdy_ctrt TEXT NULL COMMENT '응답 bstp_nmix_prdy_ctrt',
    rsp_bstp_nmix_oprc TEXT NULL COMMENT '응답 bstp_nmix_oprc',
    rsp_bstp_nmix_hgpr TEXT NULL COMMENT '응답 bstp_nmix_hgpr',
    rsp_bstp_nmix_lwpr TEXT NULL COMMENT '응답 bstp_nmix_lwpr',
    rsp_stck_prdy_clpr TEXT NULL COMMENT '응답 stck_prdy_clpr',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_frgn_reg_ntby_qty TEXT NULL COMMENT '응답 frgn_reg_ntby_qty',
    rsp_frgn_nreg_ntby_qty TEXT NULL COMMENT '응답 frgn_nreg_ntby_qty',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '응답 prsn_ntby_qty',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '응답 orgn_ntby_qty',
    rsp_scrt_ntby_qty TEXT NULL COMMENT '응답 scrt_ntby_qty',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '응답 ivtr_ntby_qty',
    rsp_pe_fund_ntby_vol TEXT NULL COMMENT '응답 pe_fund_ntby_vol',
    rsp_bank_ntby_qty TEXT NULL COMMENT '응답 bank_ntby_qty',
    rsp_insu_ntby_qty TEXT NULL COMMENT '응답 insu_ntby_qty',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '응답 mrbn_ntby_qty',
    rsp_fund_ntby_qty TEXT NULL COMMENT '응답 fund_ntby_qty',
    rsp_etc_ntby_qty TEXT NULL COMMENT '응답 etc_ntby_qty',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '응답 etc_orgt_ntby_vol',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '응답 etc_corp_ntby_vol',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 frgn_ntby_tr_pbmn',
    rsp_frgn_reg_ntby_pbmn TEXT NULL COMMENT '응답 frgn_reg_ntby_pbmn',
    rsp_frgn_nreg_ntby_pbmn TEXT NULL COMMENT '응답 frgn_nreg_ntby_pbmn',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '응답 prsn_ntby_tr_pbmn',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 orgn_ntby_tr_pbmn',
    rsp_scrt_ntby_tr_pbmn TEXT NULL COMMENT '응답 scrt_ntby_tr_pbmn',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '응답 ivtr_ntby_tr_pbmn',
    rsp_pe_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_ntby_tr_pbmn',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '응답 bank_ntby_tr_pbmn',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '응답 insu_ntby_tr_pbmn',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '응답 mrbn_ntby_tr_pbmn',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 fund_ntby_tr_pbmn',
    rsp_etc_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_ntby_tr_pbmn',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_ntby_tr_pbmn',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_ntby_tr_pbmn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_stnd_vol_smtn TEXT NULL COMMENT '응답 stnd_vol_smtn',
    rsp_ssts_cntg_qty TEXT NULL COMMENT '응답 ssts_cntg_qty',
    rsp_ssts_vol_rlim TEXT NULL COMMENT '응답 ssts_vol_rlim',
    rsp_acml_ssts_cntg_qty TEXT NULL COMMENT '응답 acml_ssts_cntg_qty',
    rsp_acml_ssts_cntg_qty_rlim TEXT NULL COMMENT '응답 acml_ssts_cntg_qty_rlim',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_stnd_tr_pbmn_smtn TEXT NULL COMMENT '응답 stnd_tr_pbmn_smtn',
    rsp_ssts_tr_pbmn TEXT NULL COMMENT '응답 ssts_tr_pbmn',
    rsp_ssts_tr_pbmn_rlim TEXT NULL COMMENT '응답 ssts_tr_pbmn_rlim',
    rsp_acml_ssts_tr_pbmn TEXT NULL COMMENT '응답 acml_ssts_tr_pbmn',
    rsp_acml_ssts_tr_pbmn_rlim TEXT NULL COMMENT '응답 acml_ssts_tr_pbmn_rlim',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_avrg_prc TEXT NULL COMMENT '응답 avrg_prc',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_org_adj_prc TEXT NULL COMMENT '요청 FID_ORG_ADJ_PRC',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID_ETC_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_stck_oprc TEXT NULL COMMENT '응답 stck_oprc',
    rsp_stck_hgpr TEXT NULL COMMENT '응답 stck_hgpr',
    rsp_stck_lwpr TEXT NULL COMMENT '응답 stck_lwpr',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_frgn_reg_ntby_qty TEXT NULL COMMENT '응답 frgn_reg_ntby_qty',
    rsp_frgn_nreg_ntby_qty TEXT NULL COMMENT '응답 frgn_nreg_ntby_qty',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '응답 prsn_ntby_qty',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '응답 orgn_ntby_qty',
    rsp_scrt_ntby_qty TEXT NULL COMMENT '응답 scrt_ntby_qty',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '응답 ivtr_ntby_qty',
    rsp_pe_fund_ntby_vol TEXT NULL COMMENT '응답 pe_fund_ntby_vol',
    rsp_bank_ntby_qty TEXT NULL COMMENT '응답 bank_ntby_qty',
    rsp_insu_ntby_qty TEXT NULL COMMENT '응답 insu_ntby_qty',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '응답 mrbn_ntby_qty',
    rsp_fund_ntby_qty TEXT NULL COMMENT '응답 fund_ntby_qty',
    rsp_etc_ntby_qty TEXT NULL COMMENT '응답 etc_ntby_qty',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '응답 etc_corp_ntby_vol',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '응답 etc_orgt_ntby_vol',
    rsp_frgn_reg_ntby_pbmn TEXT NULL COMMENT '응답 frgn_reg_ntby_pbmn',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 frgn_ntby_tr_pbmn',
    rsp_frgn_nreg_ntby_pbmn TEXT NULL COMMENT '응답 frgn_nreg_ntby_pbmn',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '응답 prsn_ntby_tr_pbmn',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 orgn_ntby_tr_pbmn',
    rsp_scrt_ntby_tr_pbmn TEXT NULL COMMENT '응답 scrt_ntby_tr_pbmn',
    rsp_pe_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_ntby_tr_pbmn',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '응답 ivtr_ntby_tr_pbmn',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '응답 bank_ntby_tr_pbmn',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '응답 insu_ntby_tr_pbmn',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '응답 mrbn_ntby_tr_pbmn',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 fund_ntby_tr_pbmn',
    rsp_etc_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_ntby_tr_pbmn',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_ntby_tr_pbmn',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_ntby_tr_pbmn',
    rsp_frgn_seln_vol TEXT NULL COMMENT '응답 frgn_seln_vol',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '응답 frgn_shnu_vol',
    rsp_frgn_seln_tr_pbmn TEXT NULL COMMENT '응답 frgn_seln_tr_pbmn',
    rsp_frgn_shnu_tr_pbmn TEXT NULL COMMENT '응답 frgn_shnu_tr_pbmn',
    rsp_frgn_reg_askp_qty TEXT NULL COMMENT '응답 frgn_reg_askp_qty',
    rsp_frgn_reg_bidp_qty TEXT NULL COMMENT '응답 frgn_reg_bidp_qty',
    rsp_frgn_reg_askp_pbmn TEXT NULL COMMENT '응답 frgn_reg_askp_pbmn',
    rsp_frgn_reg_bidp_pbmn TEXT NULL COMMENT '응답 frgn_reg_bidp_pbmn',
    rsp_frgn_nreg_askp_qty TEXT NULL COMMENT '응답 frgn_nreg_askp_qty',
    rsp_frgn_nreg_bidp_qty TEXT NULL COMMENT '응답 frgn_nreg_bidp_qty',
    rsp_frgn_nreg_askp_pbmn TEXT NULL COMMENT '응답 frgn_nreg_askp_pbmn',
    rsp_frgn_nreg_bidp_pbmn TEXT NULL COMMENT '응답 frgn_nreg_bidp_pbmn',
    rsp_prsn_seln_vol TEXT NULL COMMENT '응답 prsn_seln_vol',
    rsp_prsn_shnu_vol TEXT NULL COMMENT '응답 prsn_shnu_vol',
    rsp_prsn_seln_tr_pbmn TEXT NULL COMMENT '응답 prsn_seln_tr_pbmn',
    rsp_prsn_shnu_tr_pbmn TEXT NULL COMMENT '응답 prsn_shnu_tr_pbmn',
    rsp_orgn_seln_vol TEXT NULL COMMENT '응답 orgn_seln_vol',
    rsp_orgn_shnu_vol TEXT NULL COMMENT '응답 orgn_shnu_vol',
    rsp_orgn_seln_tr_pbmn TEXT NULL COMMENT '응답 orgn_seln_tr_pbmn',
    rsp_orgn_shnu_tr_pbmn TEXT NULL COMMENT '응답 orgn_shnu_tr_pbmn',
    rsp_scrt_seln_vol TEXT NULL COMMENT '응답 scrt_seln_vol',
    rsp_scrt_shnu_vol TEXT NULL COMMENT '응답 scrt_shnu_vol',
    rsp_scrt_seln_tr_pbmn TEXT NULL COMMENT '응답 scrt_seln_tr_pbmn',
    rsp_scrt_shnu_tr_pbmn TEXT NULL COMMENT '응답 scrt_shnu_tr_pbmn',
    rsp_ivtr_seln_vol TEXT NULL COMMENT '응답 ivtr_seln_vol',
    rsp_ivtr_shnu_vol TEXT NULL COMMENT '응답 ivtr_shnu_vol',
    rsp_ivtr_seln_tr_pbmn TEXT NULL COMMENT '응답 ivtr_seln_tr_pbmn',
    rsp_ivtr_shnu_tr_pbmn TEXT NULL COMMENT '응답 ivtr_shnu_tr_pbmn',
    rsp_pe_fund_seln_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_seln_tr_pbmn',
    rsp_pe_fund_seln_vol TEXT NULL COMMENT '응답 pe_fund_seln_vol',
    rsp_pe_fund_shnu_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_shnu_tr_pbmn',
    rsp_pe_fund_shnu_vol TEXT NULL COMMENT '응답 pe_fund_shnu_vol',
    rsp_bank_seln_vol TEXT NULL COMMENT '응답 bank_seln_vol',
    rsp_bank_shnu_vol TEXT NULL COMMENT '응답 bank_shnu_vol',
    rsp_bank_seln_tr_pbmn TEXT NULL COMMENT '응답 bank_seln_tr_pbmn',
    rsp_bank_shnu_tr_pbmn TEXT NULL COMMENT '응답 bank_shnu_tr_pbmn',
    rsp_insu_seln_vol TEXT NULL COMMENT '응답 insu_seln_vol',
    rsp_insu_shnu_vol TEXT NULL COMMENT '응답 insu_shnu_vol',
    rsp_insu_seln_tr_pbmn TEXT NULL COMMENT '응답 insu_seln_tr_pbmn',
    rsp_insu_shnu_tr_pbmn TEXT NULL COMMENT '응답 insu_shnu_tr_pbmn',
    rsp_mrbn_seln_vol TEXT NULL COMMENT '응답 mrbn_seln_vol',
    rsp_mrbn_shnu_vol TEXT NULL COMMENT '응답 mrbn_shnu_vol',
    rsp_mrbn_seln_tr_pbmn TEXT NULL COMMENT '응답 mrbn_seln_tr_pbmn',
    rsp_mrbn_shnu_tr_pbmn TEXT NULL COMMENT '응답 mrbn_shnu_tr_pbmn',
    rsp_fund_seln_vol TEXT NULL COMMENT '응답 fund_seln_vol',
    rsp_fund_shnu_vol TEXT NULL COMMENT '응답 fund_shnu_vol',
    rsp_fund_seln_tr_pbmn TEXT NULL COMMENT '응답 fund_seln_tr_pbmn',
    rsp_fund_shnu_tr_pbmn TEXT NULL COMMENT '응답 fund_shnu_tr_pbmn',
    rsp_etc_seln_vol TEXT NULL COMMENT '응답 etc_seln_vol',
    rsp_etc_shnu_vol TEXT NULL COMMENT '응답 etc_shnu_vol',
    rsp_etc_seln_tr_pbmn TEXT NULL COMMENT '응답 etc_seln_tr_pbmn',
    rsp_etc_shnu_tr_pbmn TEXT NULL COMMENT '응답 etc_shnu_tr_pbmn',
    rsp_etc_orgt_seln_vol TEXT NULL COMMENT '응답 etc_orgt_seln_vol',
    rsp_etc_orgt_shnu_vol TEXT NULL COMMENT '응답 etc_orgt_shnu_vol',
    rsp_etc_orgt_seln_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_seln_tr_pbmn',
    rsp_etc_orgt_shnu_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_shnu_tr_pbmn',
    rsp_etc_corp_seln_vol TEXT NULL COMMENT '응답 etc_corp_seln_vol',
    rsp_etc_corp_shnu_vol TEXT NULL COMMENT '응답 etc_corp_shnu_vol',
    rsp_etc_corp_seln_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_seln_tr_pbmn',
    rsp_etc_corp_shnu_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_shnu_tr_pbmn',
    rsp_bold_yn TEXT NULL COMMENT '응답 bold_yn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_user_id TEXT NULL COMMENT '요청 user_id',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_user_id TEXT NULL COMMENT '응답 user_id',
    rsp_seq TEXT NULL COMMENT '응답 seq',
    rsp_grp_nm TEXT NULL COMMENT '응답 grp_nm',
    rsp_condition_nm TEXT NULL COMMENT '응답 condition_nm',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_prc_cls_code TEXT NULL COMMENT '요청 FID_PRC_CLS_CODE',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_trgt_cls_code TEXT NULL COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code TEXT NULL COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    req_fid_input_price_1 TEXT NULL COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2 TEXT NULL COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_vol_cnt TEXT NULL COMMENT '요청 FID_VOL_CNT',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '응답 mksc_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_total_askp_rsqn TEXT NULL COMMENT '응답 total_askp_rsqn',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '응답 total_bidp_rsqn',
    rsp_askp_rsqn1 TEXT NULL COMMENT '응답 askp_rsqn1',
    rsp_bidp_rsqn1 TEXT NULL COMMENT '응답 bidp_rsqn1',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_seln_cnqn TEXT NULL COMMENT '응답 seln_cnqn',
    rsp_shnu_cnqn TEXT NULL COMMENT '응답 shnu_cnqn',
    rsp_stck_llam TEXT NULL COMMENT '응답 stck_llam',
    rsp_stck_mxpr TEXT NULL COMMENT '응답 stck_mxpr',
    rsp_prdy_vrss_vol_rate TEXT NULL COMMENT '응답 prdy_vrss_vol_rate',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_nabt_entm_seln_tr_pbmn TEXT NULL COMMENT '응답 nabt_entm_seln_tr_pbmn',
    rsp_nabt_onsl_seln_vol TEXT NULL COMMENT '응답 nabt_onsl_seln_vol',
    rsp_whol_onsl_seln_tr_pbmn TEXT NULL COMMENT '응답 whol_onsl_seln_tr_pbmn',
    rsp_arbt_smtn_shnu_vol TEXT NULL COMMENT '응답 arbt_smtn_shnu_vol',
    rsp_nabt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 nabt_smtn_shnu_tr_pbmn',
    rsp_arbt_entm_ntby_qty TEXT NULL COMMENT '응답 arbt_entm_ntby_qty',
    rsp_nabt_entm_ntby_tr_pbmn TEXT NULL COMMENT '응답 nabt_entm_ntby_tr_pbmn',
    rsp_arbt_entm_seln_vol TEXT NULL COMMENT '응답 arbt_entm_seln_vol',
    rsp_nabt_entm_seln_vol_rate TEXT NULL COMMENT '응답 nabt_entm_seln_vol_rate',
    rsp_nabt_onsl_seln_vol_rate TEXT NULL COMMENT '응답 nabt_onsl_seln_vol_rate',
    rsp_whol_onsl_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_onsl_seln_tr_pbmn_rate',
    rsp_arbt_smtm_shun_vol_rate TEXT NULL COMMENT '응답 arbt_smtm_shun_vol_rate',
    rsp_nabt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_smtm_shun_tr_pbmn_rate',
    rsp_arbt_entm_ntby_qty_rate TEXT NULL COMMENT '응답 arbt_entm_ntby_qty_rate',
    rsp_nabt_entm_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_entm_ntby_tr_pbmn_rate',
    rsp_arbt_entm_seln_vol_rate TEXT NULL COMMENT '응답 arbt_entm_seln_vol_rate',
    rsp_nabt_entm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_entm_seln_tr_pbmn_rate',
    rsp_nabt_onsl_seln_tr_pbmn TEXT NULL COMMENT '응답 nabt_onsl_seln_tr_pbmn',
    rsp_whol_smtn_seln_vol TEXT NULL COMMENT '응답 whol_smtn_seln_vol',
    rsp_arbt_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 arbt_smtn_shnu_tr_pbmn',
    rsp_whol_entm_shnu_vol TEXT NULL COMMENT '응답 whol_entm_shnu_vol',
    rsp_arbt_entm_ntby_tr_pbmn TEXT NULL COMMENT '응답 arbt_entm_ntby_tr_pbmn',
    rsp_nabt_onsl_ntby_qty TEXT NULL COMMENT '응답 nabt_onsl_ntby_qty',
    rsp_arbt_entm_seln_tr_pbmn TEXT NULL COMMENT '응답 arbt_entm_seln_tr_pbmn',
    rsp_nabt_onsl_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_onsl_seln_tr_pbmn_rate',
    rsp_whol_seln_vol_rate TEXT NULL COMMENT '응답 whol_seln_vol_rate',
    rsp_arbt_smtm_shun_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_smtm_shun_tr_pbmn_rate',
    rsp_whol_entm_shnu_vol_rate TEXT NULL COMMENT '응답 whol_entm_shnu_vol_rate',
    rsp_arbt_entm_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_entm_ntby_tr_pbmn_rate',
    rsp_nabt_onsl_ntby_qty_rate TEXT NULL COMMENT '응답 nabt_onsl_ntby_qty_rate',
    rsp_arbt_entm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_entm_seln_tr_pbmn_rate',
    rsp_nabt_smtn_seln_vol TEXT NULL COMMENT '응답 nabt_smtn_seln_vol',
    rsp_whol_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_seln_tr_pbmn',
    rsp_nabt_entm_shnu_vol TEXT NULL COMMENT '응답 nabt_entm_shnu_vol',
    rsp_whol_entm_shnu_tr_pbmn TEXT NULL COMMENT '응답 whol_entm_shnu_tr_pbmn',
    rsp_arbt_onsl_ntby_qty TEXT NULL COMMENT '응답 arbt_onsl_ntby_qty',
    rsp_nabt_onsl_ntby_tr_pbmn TEXT NULL COMMENT '응답 nabt_onsl_ntby_tr_pbmn',
    rsp_arbt_onsl_seln_tr_pbmn TEXT NULL COMMENT '응답 arbt_onsl_seln_tr_pbmn',
    rsp_nabt_smtm_seln_vol_rate TEXT NULL COMMENT '응답 nabt_smtm_seln_vol_rate',
    rsp_whol_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_seln_tr_pbmn_rate',
    rsp_nabt_entm_shnu_vol_rate TEXT NULL COMMENT '응답 nabt_entm_shnu_vol_rate',
    rsp_whol_entm_shnu_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_entm_shnu_tr_pbmn_rate',
    rsp_arbt_onsl_ntby_qty_rate TEXT NULL COMMENT '응답 arbt_onsl_ntby_qty_rate',
    rsp_nabt_onsl_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_onsl_ntby_tr_pbmn_rate',
    rsp_arbt_onsl_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_onsl_seln_tr_pbmn_rate',
    rsp_nabt_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 nabt_smtn_seln_tr_pbmn',
    rsp_arbt_entm_shnu_vol TEXT NULL COMMENT '응답 arbt_entm_shnu_vol',
    rsp_nabt_entm_shnu_tr_pbmn TEXT NULL COMMENT '응답 nabt_entm_shnu_tr_pbmn',
    rsp_whol_onsl_shnu_vol TEXT NULL COMMENT '응답 whol_onsl_shnu_vol',
    rsp_arbt_onsl_ntby_tr_pbmn TEXT NULL COMMENT '응답 arbt_onsl_ntby_tr_pbmn',
    rsp_nabt_smtn_ntby_qty TEXT NULL COMMENT '응답 nabt_smtn_ntby_qty',
    rsp_arbt_onsl_seln_vol TEXT NULL COMMENT '응답 arbt_onsl_seln_vol',
    rsp_nabt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_smtm_seln_tr_pbmn_rate',
    rsp_arbt_entm_shnu_vol_rate TEXT NULL COMMENT '응답 arbt_entm_shnu_vol_rate',
    rsp_nabt_entm_shnu_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_entm_shnu_tr_pbmn_rate',
    rsp_whol_onsl_shnu_tr_pbmn TEXT NULL COMMENT '응답 whol_onsl_shnu_tr_pbmn',
    rsp_arbt_onsl_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_onsl_ntby_tr_pbmn_rate',
    rsp_nabt_smtm_ntby_qty_rate TEXT NULL COMMENT '응답 nabt_smtm_ntby_qty_rate',
    rsp_arbt_onsl_seln_vol_rate TEXT NULL COMMENT '응답 arbt_onsl_seln_vol_rate',
    rsp_whol_entm_seln_vol TEXT NULL COMMENT '응답 whol_entm_seln_vol',
    rsp_arbt_entm_shnu_tr_pbmn TEXT NULL COMMENT '응답 arbt_entm_shnu_tr_pbmn',
    rsp_nabt_onsl_shnu_vol TEXT NULL COMMENT '응답 nabt_onsl_shnu_vol',
    rsp_whol_onsl_shnu_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_onsl_shnu_tr_pbmn_rate',
    rsp_arbt_smtn_ntby_qty TEXT NULL COMMENT '응답 arbt_smtn_ntby_qty',
    rsp_nabt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 nabt_smtn_ntby_tr_pbmn',
    rsp_arbt_smtn_seln_vol TEXT NULL COMMENT '응답 arbt_smtn_seln_vol',
    rsp_whol_entm_seln_tr_pbmn TEXT NULL COMMENT '응답 whol_entm_seln_tr_pbmn',
    rsp_arbt_entm_shnu_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_entm_shnu_tr_pbmn_rate',
    rsp_nabt_onsl_shnu_vol_rate TEXT NULL COMMENT '응답 nabt_onsl_shnu_vol_rate',
    rsp_whol_onsl_shnu_vol_rate TEXT NULL COMMENT '응답 whol_onsl_shnu_vol_rate',
    rsp_arbt_smtm_ntby_qty_rate TEXT NULL COMMENT '응답 arbt_smtm_ntby_qty_rate',
    rsp_nabt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_smtm_ntby_tr_pbmn_rate',
    rsp_arbt_smtm_seln_vol_rate TEXT NULL COMMENT '응답 arbt_smtm_seln_vol_rate',
    rsp_whol_entm_seln_vol_rate TEXT NULL COMMENT '응답 whol_entm_seln_vol_rate',
    rsp_arbt_onsl_shnu_vol TEXT NULL COMMENT '응답 arbt_onsl_shnu_vol',
    rsp_nabt_onsl_shnu_tr_pbmn TEXT NULL COMMENT '응답 nabt_onsl_shnu_tr_pbmn',
    rsp_whol_smtn_shnu_vol TEXT NULL COMMENT '응답 whol_smtn_shnu_vol',
    rsp_arbt_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 arbt_smtn_ntby_tr_pbmn',
    rsp_whol_entm_ntby_qty TEXT NULL COMMENT '응답 whol_entm_ntby_qty',
    rsp_arbt_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 arbt_smtn_seln_tr_pbmn',
    rsp_whol_entm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_entm_seln_tr_pbmn_rate',
    rsp_arbt_onsl_shnu_vol_rate TEXT NULL COMMENT '응답 arbt_onsl_shnu_vol_rate',
    rsp_nabt_onsl_shnu_tr_pbmn_rate TEXT NULL COMMENT '응답 nabt_onsl_shnu_tr_pbmn_rate',
    rsp_whol_shun_vol_rate TEXT NULL COMMENT '응답 whol_shun_vol_rate',
    rsp_arbt_smtm_ntby_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_smtm_ntby_tr_pbmn_rate',
    rsp_whol_entm_ntby_qty_rate TEXT NULL COMMENT '응답 whol_entm_ntby_qty_rate',
    rsp_arbt_smtm_seln_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_smtm_seln_tr_pbmn_rate',
    rsp_whol_onsl_seln_vol TEXT NULL COMMENT '응답 whol_onsl_seln_vol',
    rsp_arbt_onsl_shnu_tr_pbmn TEXT NULL COMMENT '응답 arbt_onsl_shnu_tr_pbmn',
    rsp_nabt_smtn_shnu_vol TEXT NULL COMMENT '응답 nabt_smtn_shnu_vol',
    rsp_whol_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_shnu_tr_pbmn',
    rsp_nabt_entm_ntby_qty TEXT NULL COMMENT '응답 nabt_entm_ntby_qty',
    rsp_whol_entm_ntby_tr_pbmn TEXT NULL COMMENT '응답 whol_entm_ntby_tr_pbmn',
    rsp_nabt_entm_seln_vol TEXT NULL COMMENT '응답 nabt_entm_seln_vol',
    rsp_whol_onsl_seln_vol_rate TEXT NULL COMMENT '응답 whol_onsl_seln_vol_rate',
    rsp_arbt_onsl_shnu_tr_pbmn_rate TEXT NULL COMMENT '응답 arbt_onsl_shnu_tr_pbmn_rate',
    rsp_nabt_smtm_shun_vol_rate TEXT NULL COMMENT '응답 nabt_smtm_shun_vol_rate',
    rsp_whol_shun_tr_pbmn_rate TEXT NULL COMMENT '응답 whol_shun_tr_pbmn_rate',
    rsp_nabt_entm_ntby_qty_rate TEXT NULL COMMENT '응답 nabt_entm_ntby_qty_rate',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_mrkt_div_cls_code TEXT NULL COMMENT '요청 MRKT_DIV_CLS_CODE',
    req_mksc_shrn_iscd TEXT NULL COMMENT '요청 MKSC_SHRN_ISCD',
    req_start_date TEXT NULL COMMENT '요청 START_DATE',
    req_end_date TEXT NULL COMMENT '요청 END_DATE',
    req_cts TEXT NULL COMMENT '요청 CTS',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_date TEXT NULL COMMENT '응답 bsop_date',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_new_stcn TEXT NULL COMMENT '응답 new_stcn',
    rsp_rdmp_stcn TEXT NULL COMMENT '응답 rdmp_stcn',
    rsp_prdy_rmnd_vrss TEXT NULL COMMENT '응답 prdy_rmnd_vrss',
    rsp_rmnd_stcn TEXT NULL COMMENT '응답 rmnd_stcn',
    rsp_rmnd_amt TEXT NULL COMMENT '응답 rmnd_amt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_user_id TEXT NULL COMMENT '요청 user_id',
    req_seq TEXT NULL COMMENT '요청 seq',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_code TEXT NULL COMMENT '응답 code',
    rsp_name TEXT NULL COMMENT '응답 name',
    rsp_daebi TEXT NULL COMMENT '응답 daebi',
    rsp_price TEXT NULL COMMENT '응답 price',
    rsp_chgrate TEXT NULL COMMENT '응답 chgrate',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_trade_amt TEXT NULL COMMENT '응답 trade_amt',
    rsp_change TEXT NULL COMMENT '응답 change',
    rsp_cttr TEXT NULL COMMENT '응답 cttr',
    rsp_open TEXT NULL COMMENT '응답 open',
    rsp_high TEXT NULL COMMENT '응답 high',
    rsp_low TEXT NULL COMMENT '응답 low',
    rsp_high52 TEXT NULL COMMENT '응답 high52',
    rsp_low52 TEXT NULL COMMENT '응답 low52',
    rsp_expprice TEXT NULL COMMENT '응답 expprice',
    rsp_expchange TEXT NULL COMMENT '응답 expchange',
    rsp_expchggrate TEXT NULL COMMENT '응답 expchggrate',
    rsp_expcvol TEXT NULL COMMENT '응답 expcvol',
    rsp_chgrate2 TEXT NULL COMMENT '응답 chgrate2',
    rsp_expdaebi TEXT NULL COMMENT '응답 expdaebi',
    rsp_recprice TEXT NULL COMMENT '응답 recprice',
    rsp_uplmtprice TEXT NULL COMMENT '응답 uplmtprice',
    rsp_dnlmtprice TEXT NULL COMMENT '응답 dnlmtprice',
    rsp_stotprice TEXT NULL COMMENT '응답 stotprice',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_hour_1 TEXT NULL COMMENT '요청 FID_INPUT_HOUR_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_wghn_avrg_stck_prc TEXT NULL COMMENT '응답 wghn_avrg_stck_prc',
    rsp_lstn_stcn TEXT NULL COMMENT '응답 lstn_stcn',
    rsp_data_rank TEXT NULL COMMENT '응답 data_rank',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
    rsp_acml_vol_rlim TEXT NULL COMMENT '응답 acml_vol_rlim',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID_ETC_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_output TEXT NULL COMMENT '응답 Output',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '응답 mksc_shrn_iscd',
    rsp_ntby_qty TEXT NULL COMMENT '응답 ntby_qty',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '응답 orgn_ntby_qty',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '응답 ivtr_ntby_qty',
    rsp_bank_ntby_qty TEXT NULL COMMENT '응답 bank_ntby_qty',
    rsp_insu_ntby_qty TEXT NULL COMMENT '응답 insu_ntby_qty',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '응답 mrbn_ntby_qty',
    rsp_fund_ntby_qty TEXT NULL COMMENT '응답 fund_ntby_qty',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '응답 etc_orgt_ntby_vol',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '응답 etc_corp_ntby_vol',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 frgn_ntby_tr_pbmn',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 orgn_ntby_tr_pbmn',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '응답 ivtr_ntby_tr_pbmn',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '응답 bank_ntby_tr_pbmn',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '응답 insu_ntby_tr_pbmn',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '응답 mrbn_ntby_tr_pbmn',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 fund_ntby_tr_pbmn',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_ntby_tr_pbmn',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_ntby_tr_pbmn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_type TEXT NULL COMMENT '요청 TYPE',
    req_user_id TEXT NULL COMMENT '요청 USER_ID',
    req_data_rank TEXT NULL COMMENT '요청 DATA_RANK',
    req_inter_grp_code TEXT NULL COMMENT '요청 INTER_GRP_CODE',
    req_inter_grp_name TEXT NULL COMMENT '요청 INTER_GRP_NAME',
    req_hts_kor_isnm TEXT NULL COMMENT '요청 HTS_KOR_ISNM',
    req_cntg_cls_code TEXT NULL COMMENT '요청 CNTG_CLS_CODE',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID_ETC_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_data_rank TEXT NULL COMMENT '응답 data_rank',
    rsp_inter_grp_name TEXT NULL COMMENT '응답 inter_grp_name',
    rsp_fid_mrkt_cls_code TEXT NULL COMMENT '응답 fid_mrkt_cls_code',
    rsp_exch_code TEXT NULL COMMENT '응답 exch_code',
    rsp_jong_code TEXT NULL COMMENT '응답 jong_code',
    rsp_color_code TEXT NULL COMMENT '응답 color_code',
    rsp_memo TEXT NULL COMMENT '응답 memo',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_fxdt_ntby_qty TEXT NULL COMMENT '응답 fxdt_ntby_qty',
    rsp_cntg_unpr TEXT NULL COMMENT '응답 cntg_unpr',
    rsp_cntg_cls_code TEXT NULL COMMENT '응답 cntg_cls_code',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_2',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    req_fid_sctn_cls_code TEXT NULL COMMENT '요청 FID_SCTN_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_total_seln_qty TEXT NULL COMMENT '응답 total_seln_qty',
    rsp_total_shnu_qty TEXT NULL COMMENT '응답 total_shnu_qty',
    rsp_ntby_qty TEXT NULL COMMENT '응답 ntby_qty',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_clpr TEXT NULL COMMENT '응답 stck_clpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_whol_smtn_seln_vol TEXT NULL COMMENT '응답 whol_smtn_seln_vol',
    rsp_whol_smtn_shnu_vol TEXT NULL COMMENT '응답 whol_smtn_shnu_vol',
    rsp_whol_smtn_ntby_qty TEXT NULL COMMENT '응답 whol_smtn_ntby_qty',
    rsp_whol_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_seln_tr_pbmn',
    rsp_whol_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_shnu_tr_pbmn',
    rsp_whol_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_ntby_tr_pbmn',
    rsp_whol_ntby_vol_icdc TEXT NULL COMMENT '응답 whol_ntby_vol_icdc',
    rsp_whol_ntby_tr_pbmn_icdc2 TEXT NULL COMMENT '응답 whol_ntby_tr_pbmn_icdc2',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_type TEXT NULL COMMENT '요청 TYPE',
    req_fid_etc_cls_code TEXT NULL COMMENT '요청 FID_ETC_CLS_CODE',
    req_user_id TEXT NULL COMMENT '요청 USER_ID',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_date TEXT NULL COMMENT '응답 date',
    rsp_trnm_hour TEXT NULL COMMENT '응답 trnm_hour',
    rsp_data_rank TEXT NULL COMMENT '응답 data_rank',
    rsp_inter_grp_code TEXT NULL COMMENT '응답 inter_grp_code',
    rsp_inter_grp_name TEXT NULL COMMENT '응답 inter_grp_name',
    rsp_ask_cnt TEXT NULL COMMENT '응답 ask_cnt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_mksc_shrn_iscd TEXT NULL COMMENT '요청 MKSC_SHRN_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_hour_gb TEXT NULL COMMENT '응답 bsop_hour_gb',
    rsp_frgn_fake_ntby_qty TEXT NULL COMMENT '응답 frgn_fake_ntby_qty',
    rsp_orgn_fake_ntby_qty TEXT NULL COMMENT '응답 orgn_fake_ntby_qty',
    rsp_sum_fake_ntby_qty TEXT NULL COMMENT '응답 sum_fake_ntby_qty',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    req_fid_input_date_2 TEXT NULL COMMENT '요청 FID_INPUT_DATE_2',
    req_fid_period_div_code TEXT NULL COMMENT '요청 FID_PERIOD_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_shnu_cnqn_smtn TEXT NULL COMMENT '응답 shnu_cnqn_smtn',
    rsp_seln_cnqn_smtn TEXT NULL COMMENT '응답 seln_cnqn_smtn',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_total_seln_qty TEXT NULL COMMENT '응답 total_seln_qty',
    rsp_total_shnu_qty TEXT NULL COMMENT '응답 total_shnu_qty',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_prpr_name TEXT NULL COMMENT '응답 prpr_name',
    rsp_smtn_avrg_prpr TEXT NULL COMMENT '응답 smtn_avrg_prpr',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_whol_ntby_qty_rate TEXT NULL COMMENT '응답 whol_ntby_qty_rate',
    rsp_ntby_cntg_csnu TEXT NULL COMMENT '응답 ntby_cntg_csnu',
    rsp_seln_cnqn_smtn TEXT NULL COMMENT '응답 seln_cnqn_smtn',
    rsp_whol_seln_vol_rate TEXT NULL COMMENT '응답 whol_seln_vol_rate',
    rsp_seln_cntg_csnu TEXT NULL COMMENT '응답 seln_cntg_csnu',
    rsp_shnu_cnqn_smtn TEXT NULL COMMENT '응답 shnu_cnqn_smtn',
    rsp_whol_shun_vol_rate TEXT NULL COMMENT '응답 whol_shun_vol_rate',
    rsp_shnu_cntg_csnu TEXT NULL COMMENT '응답 shnu_cntg_csnu',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_exch_div_cls_code TEXT NULL COMMENT '요청 EXCH_DIV_CLS_CODE',
    req_mrkt_div_cls_code TEXT NULL COMMENT '요청 MRKT_DIV_CLS_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_invr_cls_code TEXT NULL COMMENT '응답 invr_cls_code',
    rsp_all_seln_qty TEXT NULL COMMENT '응답 all_seln_qty',
    rsp_all_seln_amt TEXT NULL COMMENT '응답 all_seln_amt',
    rsp_invr_cls_name TEXT NULL COMMENT '응답 invr_cls_name',
    rsp_all_shnu_qty TEXT NULL COMMENT '응답 all_shnu_qty',
    rsp_all_shnu_amt TEXT NULL COMMENT '응답 all_shnu_amt',
    rsp_all_ntby_amt TEXT NULL COMMENT '응답 all_ntby_amt',
    rsp_arbt_seln_qty TEXT NULL COMMENT '응답 arbt_seln_qty',
    rsp_all_ntby_qty TEXT NULL COMMENT '응답 all_ntby_qty',
    rsp_arbt_shnu_qty TEXT NULL COMMENT '응답 arbt_shnu_qty',
    rsp_arbt_ntby_qty TEXT NULL COMMENT '응답 arbt_ntby_qty',
    rsp_arbt_seln_amt TEXT NULL COMMENT '응답 arbt_seln_amt',
    rsp_arbt_shnu_amt TEXT NULL COMMENT '응답 arbt_shnu_amt',
    rsp_arbt_ntby_amt TEXT NULL COMMENT '응답 arbt_ntby_amt',
    rsp_nabt_seln_qty TEXT NULL COMMENT '응답 nabt_seln_qty',
    rsp_nabt_shnu_qty TEXT NULL COMMENT '응답 nabt_shnu_qty',
    rsp_nabt_ntby_qty TEXT NULL COMMENT '응답 nabt_ntby_qty',
    rsp_nabt_seln_amt TEXT NULL COMMENT '응답 nabt_seln_amt',
    rsp_nabt_shnu_amt TEXT NULL COMMENT '응답 nabt_shnu_amt',
    rsp_nabt_ntby_amt TEXT NULL COMMENT '응답 nabt_ntby_amt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_date_1 TEXT NULL COMMENT '요청 FID_INPUT_DATE_1',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_date TEXT NULL COMMENT '응답 bsop_date',
    rsp_bstp_nmix_prpr TEXT NULL COMMENT '응답 bstp_nmix_prpr',
    rsp_bstp_nmix_prdy_vrss TEXT NULL COMMENT '응답 bstp_nmix_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_hts_avls TEXT NULL COMMENT '응답 hts_avls',
    rsp_cust_dpmn_amt TEXT NULL COMMENT '응답 cust_dpmn_amt',
    rsp_cust_dpmn_amt_prdy_vrss TEXT NULL COMMENT '응답 cust_dpmn_amt_prdy_vrss',
    rsp_amt_tnrt TEXT NULL COMMENT '응답 amt_tnrt',
    rsp_uncl_amt TEXT NULL COMMENT '응답 uncl_amt',
    rsp_crdt_loan_rmnd TEXT NULL COMMENT '응답 crdt_loan_rmnd',
    rsp_futs_tfam_amt TEXT NULL COMMENT '응답 futs_tfam_amt',
    rsp_sttp_amt TEXT NULL COMMENT '응답 sttp_amt',
    rsp_mxtp_amt TEXT NULL COMMENT '응답 mxtp_amt',
    rsp_bntp_amt TEXT NULL COMMENT '응답 bntp_amt',
    rsp_mmf_amt TEXT NULL COMMENT '응답 mmf_amt',
    rsp_secu_lend_amt TEXT NULL COMMENT '응답 secu_lend_amt',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_mkop_cls_code TEXT NULL COMMENT '요청 fid_mkop_cls_code',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_input_iscd TEXT NULL COMMENT '요청 fid_input_iscd',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_rprs_mrkt_kor_name TEXT NULL COMMENT '응답 rprs_mrkt_kor_name',
    rsp_antc_cnpr TEXT NULL COMMENT '응답 antc_cnpr',
    rsp_antc_cntg_vrss_sign TEXT NULL COMMENT '응답 antc_cntg_vrss_sign',
    rsp_antc_cntg_vrss TEXT NULL COMMENT '응답 antc_cntg_vrss',
    rsp_antc_cntg_prdy_ctrt TEXT NULL COMMENT '응답 antc_cntg_prdy_ctrt',
    rsp_antc_vol TEXT NULL COMMENT '응답 antc_vol',
    rsp_antc_tr_pbmn TEXT NULL COMMENT '응답 antc_tr_pbmn',
    rsp_stck_bsop_date TEXT NULL COMMENT '응답 stck_bsop_date',
    rsp_stck_cntg_hour TEXT NULL COMMENT '응답 stck_cntg_hour',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_2',
    req_fid_mrkt_cls_code TEXT NULL COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_vol_cnt TEXT NULL COMMENT '요청 FID_VOL_CNT',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_total_seln_qty TEXT NULL COMMENT '응답 total_seln_qty',
    rsp_total_shnu_qty TEXT NULL COMMENT '응답 total_shnu_qty',
    rsp_bsop_hour TEXT NULL COMMENT '응답 bsop_hour',
    rsp_mbcr_name TEXT NULL COMMENT '응답 mbcr_name',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_cntg_vol TEXT NULL COMMENT '응답 cntg_vol',
    rsp_acml_ntby_qty TEXT NULL COMMENT '응답 acml_ntby_qty',
    rsp_glob_ntby_qty TEXT NULL COMMENT '응답 glob_ntby_qty',
    rsp_frgn_ntby_qty_icdc TEXT NULL COMMENT '응답 frgn_ntby_qty_icdc',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_iscd TEXT NULL COMMENT '요청 fid_input_iscd',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 fid_input_iscd_2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_frgn_seln_vol TEXT NULL COMMENT '응답 frgn_seln_vol',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '응답 frgn_shnu_vol',
    rsp_frgn_ntby_qty TEXT NULL COMMENT '응답 frgn_ntby_qty',
    rsp_frgn_seln_tr_pbmn TEXT NULL COMMENT '응답 frgn_seln_tr_pbmn',
    rsp_frgn_shnu_tr_pbmn TEXT NULL COMMENT '응답 frgn_shnu_tr_pbmn',
    rsp_frgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 frgn_ntby_tr_pbmn',
    rsp_prsn_seln_vol TEXT NULL COMMENT '응답 prsn_seln_vol',
    rsp_prsn_shnu_vol TEXT NULL COMMENT '응답 prsn_shnu_vol',
    rsp_prsn_ntby_qty TEXT NULL COMMENT '응답 prsn_ntby_qty',
    rsp_prsn_seln_tr_pbmn TEXT NULL COMMENT '응답 prsn_seln_tr_pbmn',
    rsp_prsn_shnu_tr_pbmn TEXT NULL COMMENT '응답 prsn_shnu_tr_pbmn',
    rsp_prsn_ntby_tr_pbmn TEXT NULL COMMENT '응답 prsn_ntby_tr_pbmn',
    rsp_orgn_seln_vol TEXT NULL COMMENT '응답 orgn_seln_vol',
    rsp_orgn_shnu_vol TEXT NULL COMMENT '응답 orgn_shnu_vol',
    rsp_orgn_ntby_qty TEXT NULL COMMENT '응답 orgn_ntby_qty',
    rsp_orgn_seln_tr_pbmn TEXT NULL COMMENT '응답 orgn_seln_tr_pbmn',
    rsp_orgn_shnu_tr_pbmn TEXT NULL COMMENT '응답 orgn_shnu_tr_pbmn',
    rsp_orgn_ntby_tr_pbmn TEXT NULL COMMENT '응답 orgn_ntby_tr_pbmn',
    rsp_scrt_seln_vol TEXT NULL COMMENT '응답 scrt_seln_vol',
    rsp_scrt_shnu_vol TEXT NULL COMMENT '응답 scrt_shnu_vol',
    rsp_scrt_ntby_qty TEXT NULL COMMENT '응답 scrt_ntby_qty',
    rsp_scrt_seln_tr_pbmn TEXT NULL COMMENT '응답 scrt_seln_tr_pbmn',
    rsp_scrt_shnu_tr_pbmn TEXT NULL COMMENT '응답 scrt_shnu_tr_pbmn',
    rsp_scrt_ntby_tr_pbmn TEXT NULL COMMENT '응답 scrt_ntby_tr_pbmn',
    rsp_ivtr_seln_vol TEXT NULL COMMENT '응답 ivtr_seln_vol',
    rsp_ivtr_shnu_vol TEXT NULL COMMENT '응답 ivtr_shnu_vol',
    rsp_ivtr_ntby_qty TEXT NULL COMMENT '응답 ivtr_ntby_qty',
    rsp_ivtr_seln_tr_pbmn TEXT NULL COMMENT '응답 ivtr_seln_tr_pbmn',
    rsp_ivtr_shnu_tr_pbmn TEXT NULL COMMENT '응답 ivtr_shnu_tr_pbmn',
    rsp_ivtr_ntby_tr_pbmn TEXT NULL COMMENT '응답 ivtr_ntby_tr_pbmn',
    rsp_pe_fund_seln_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_seln_tr_pbmn',
    rsp_pe_fund_seln_vol TEXT NULL COMMENT '응답 pe_fund_seln_vol',
    rsp_pe_fund_ntby_vol TEXT NULL COMMENT '응답 pe_fund_ntby_vol',
    rsp_pe_fund_shnu_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_shnu_tr_pbmn',
    rsp_pe_fund_shnu_vol TEXT NULL COMMENT '응답 pe_fund_shnu_vol',
    rsp_pe_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 pe_fund_ntby_tr_pbmn',
    rsp_bank_seln_vol TEXT NULL COMMENT '응답 bank_seln_vol',
    rsp_bank_shnu_vol TEXT NULL COMMENT '응답 bank_shnu_vol',
    rsp_bank_ntby_qty TEXT NULL COMMENT '응답 bank_ntby_qty',
    rsp_bank_seln_tr_pbmn TEXT NULL COMMENT '응답 bank_seln_tr_pbmn',
    rsp_bank_shnu_tr_pbmn TEXT NULL COMMENT '응답 bank_shnu_tr_pbmn',
    rsp_bank_ntby_tr_pbmn TEXT NULL COMMENT '응답 bank_ntby_tr_pbmn',
    rsp_insu_seln_vol TEXT NULL COMMENT '응답 insu_seln_vol',
    rsp_insu_shnu_vol TEXT NULL COMMENT '응답 insu_shnu_vol',
    rsp_insu_ntby_qty TEXT NULL COMMENT '응답 insu_ntby_qty',
    rsp_insu_seln_tr_pbmn TEXT NULL COMMENT '응답 insu_seln_tr_pbmn',
    rsp_insu_shnu_tr_pbmn TEXT NULL COMMENT '응답 insu_shnu_tr_pbmn',
    rsp_insu_ntby_tr_pbmn TEXT NULL COMMENT '응답 insu_ntby_tr_pbmn',
    rsp_mrbn_seln_vol TEXT NULL COMMENT '응답 mrbn_seln_vol',
    rsp_mrbn_shnu_vol TEXT NULL COMMENT '응답 mrbn_shnu_vol',
    rsp_mrbn_ntby_qty TEXT NULL COMMENT '응답 mrbn_ntby_qty',
    rsp_mrbn_seln_tr_pbmn TEXT NULL COMMENT '응답 mrbn_seln_tr_pbmn',
    rsp_mrbn_shnu_tr_pbmn TEXT NULL COMMENT '응답 mrbn_shnu_tr_pbmn',
    rsp_mrbn_ntby_tr_pbmn TEXT NULL COMMENT '응답 mrbn_ntby_tr_pbmn',
    rsp_fund_seln_vol TEXT NULL COMMENT '응답 fund_seln_vol',
    rsp_fund_shnu_vol TEXT NULL COMMENT '응답 fund_shnu_vol',
    rsp_fund_ntby_qty TEXT NULL COMMENT '응답 fund_ntby_qty',
    rsp_fund_seln_tr_pbmn TEXT NULL COMMENT '응답 fund_seln_tr_pbmn',
    rsp_fund_shnu_tr_pbmn TEXT NULL COMMENT '응답 fund_shnu_tr_pbmn',
    rsp_fund_ntby_tr_pbmn TEXT NULL COMMENT '응답 fund_ntby_tr_pbmn',
    rsp_etc_orgt_seln_vol TEXT NULL COMMENT '응답 etc_orgt_seln_vol',
    rsp_etc_orgt_shnu_vol TEXT NULL COMMENT '응답 etc_orgt_shnu_vol',
    rsp_etc_orgt_ntby_vol TEXT NULL COMMENT '응답 etc_orgt_ntby_vol',
    rsp_etc_orgt_seln_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_seln_tr_pbmn',
    rsp_etc_orgt_shnu_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_shnu_tr_pbmn',
    rsp_etc_orgt_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_orgt_ntby_tr_pbmn',
    rsp_etc_corp_seln_vol TEXT NULL COMMENT '응답 etc_corp_seln_vol',
    rsp_etc_corp_shnu_vol TEXT NULL COMMENT '응답 etc_corp_shnu_vol',
    rsp_etc_corp_ntby_vol TEXT NULL COMMENT '응답 etc_corp_ntby_vol',
    rsp_etc_corp_seln_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_seln_tr_pbmn',
    rsp_etc_corp_shnu_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_shnu_tr_pbmn',
    rsp_etc_corp_ntby_tr_pbmn TEXT NULL COMMENT '응답 etc_corp_ntby_tr_pbmn',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_hour TEXT NULL COMMENT '응답 bsop_hour',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_whol_smtn_seln_vol TEXT NULL COMMENT '응답 whol_smtn_seln_vol',
    rsp_whol_smtn_shnu_vol TEXT NULL COMMENT '응답 whol_smtn_shnu_vol',
    rsp_whol_smtn_ntby_qty TEXT NULL COMMENT '응답 whol_smtn_ntby_qty',
    rsp_whol_smtn_seln_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_seln_tr_pbmn',
    rsp_whol_smtn_shnu_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_shnu_tr_pbmn',
    rsp_whol_smtn_ntby_tr_pbmn TEXT NULL COMMENT '응답 whol_smtn_ntby_tr_pbmn',
    rsp_whol_ntby_vol_icdc TEXT NULL COMMENT '응답 whol_ntby_vol_icdc',
    rsp_whol_ntby_tr_pbmn_icdc TEXT NULL COMMENT '응답 whol_ntby_tr_pbmn_icdc',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_rank_sort_cls_code TEXT NULL COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_rank_sort_cls_code_2 TEXT NULL COMMENT '요청 FID_RANK_SORT_CLS_CODE_2',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_shrn_iscd TEXT NULL COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_glob_ntsl_qty TEXT NULL COMMENT '응답 glob_ntsl_qty',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_glob_total_seln_qty TEXT NULL COMMENT '응답 glob_total_seln_qty',
    rsp_glob_total_shnu_qty TEXT NULL COMMENT '응답 glob_total_shnu_qty',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_2',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bsop_hour TEXT NULL COMMENT '응답 bsop_hour',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_frgn_seln_vol TEXT NULL COMMENT '응답 frgn_seln_vol',
    rsp_frgn_shnu_vol TEXT NULL COMMENT '응답 frgn_shnu_vol',
    rsp_glob_ntby_qty TEXT NULL COMMENT '응답 glob_ntby_qty',
    rsp_frgn_ntby_qty_icdc TEXT NULL COMMENT '응답 frgn_ntby_qty_icdc',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code_1 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_1',
    req_fid_input_iscd_1 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_1',
    req_fid_cond_mrkt_div_code_2 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_2',
    req_fid_input_iscd_2 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_2',
    req_fid_cond_mrkt_div_code_3 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_3',
    req_fid_input_iscd_3 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_3',
    req_fid_cond_mrkt_div_code_4 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_4',
    req_fid_input_iscd_4 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_4',
    req_fid_cond_mrkt_div_code_5 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_5',
    req_fid_input_iscd_5 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_5',
    req_fid_cond_mrkt_div_code_6 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_6',
    req_fid_input_iscd_6 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_6',
    req_fid_cond_mrkt_div_code_7 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_7',
    req_fid_input_iscd_7 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_7',
    req_fid_cond_mrkt_div_code_8 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_8',
    req_fid_input_iscd_8 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_8',
    req_fid_cond_mrkt_div_code_9 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_9',
    req_fid_input_iscd_9 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_9',
    req_fid_cond_mrkt_div_code_10 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_10',
    req_fid_input_iscd_10 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_10',
    req_fid_cond_mrkt_div_code_11 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_11',
    req_fid_input_iscd_11 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_11',
    req_fid_cond_mrkt_div_code_12 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_12',
    req_fid_input_iscd_12 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_12',
    req_fid_cond_mrkt_div_code_13 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_13',
    req_fid_input_iscd_13 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_13',
    req_fid_cond_mrkt_div_code_14 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_14',
    req_fid_input_iscd_14 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_14',
    req_fid_cond_mrkt_div_code_15 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_15',
    req_fid_input_iscd_15 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_15',
    req_fid_cond_mrkt_div_code_16 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_16',
    req_fid_input_iscd_16 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_16',
    req_fid_cond_mrkt_div_code_17 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_17',
    req_fid_input_iscd_17 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_17',
    req_fid_cond_mrkt_div_code_18 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_18',
    req_fid_input_iscd_18 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_18',
    req_fid_cond_mrkt_div_code_19 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_19',
    req_fid_input_iscd_19 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_19',
    req_fid_cond_mrkt_div_code_20 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_20',
    req_fid_input_iscd_20 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_20',
    req_fid_cond_mrkt_div_code_21 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_21',
    req_fid_input_iscd_21 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_21',
    req_fid_cond_mrkt_div_code_22 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_22',
    req_fid_input_iscd_22 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_22',
    req_fid_cond_mrkt_div_code_23 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_23',
    req_fid_input_iscd_23 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_23',
    req_fid_cond_mrkt_div_code_24 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_24',
    req_fid_input_iscd_24 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_24',
    req_fid_cond_mrkt_div_code_25 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_25',
    req_fid_input_iscd_25 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_25',
    req_fid_cond_mrkt_div_code_26 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_26',
    req_fid_input_iscd_26 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_26',
    req_fid_cond_mrkt_div_code_27 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_27',
    req_fid_input_iscd_27 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_27',
    req_fid_cond_mrkt_div_code_28 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_28',
    req_fid_input_iscd_28 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_28',
    req_fid_cond_mrkt_div_code_29 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_29',
    req_fid_input_iscd_29 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_29',
    req_fid_cond_mrkt_div_code_30 TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE_30',
    req_fid_input_iscd_30 TEXT NULL COMMENT '요청 FID_INPUT_ISCD_30',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_kospi_kosdaq_cls_name TEXT NULL COMMENT '응답 kospi_kosdaq_cls_name',
    rsp_mrkt_trtm_cls_name TEXT NULL COMMENT '응답 mrkt_trtm_cls_name',
    rsp_hour_cls_code TEXT NULL COMMENT '응답 hour_cls_code',
    rsp_inter_shrn_iscd TEXT NULL COMMENT '응답 inter_shrn_iscd',
    rsp_inter_kor_isnm TEXT NULL COMMENT '응답 inter_kor_isnm',
    rsp_inter2_prpr TEXT NULL COMMENT '응답 inter2_prpr',
    rsp_inter2_prdy_vrss TEXT NULL COMMENT '응답 inter2_prdy_vrss',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_inter2_oprc TEXT NULL COMMENT '응답 inter2_oprc',
    rsp_inter2_hgpr TEXT NULL COMMENT '응답 inter2_hgpr',
    rsp_inter2_lwpr TEXT NULL COMMENT '응답 inter2_lwpr',
    rsp_inter2_llam TEXT NULL COMMENT '응답 inter2_llam',
    rsp_inter2_mxpr TEXT NULL COMMENT '응답 inter2_mxpr',
    rsp_inter2_askp TEXT NULL COMMENT '응답 inter2_askp',
    rsp_inter2_bidp TEXT NULL COMMENT '응답 inter2_bidp',
    rsp_seln_rsqn TEXT NULL COMMENT '응답 seln_rsqn',
    rsp_shnu_rsqn TEXT NULL COMMENT '응답 shnu_rsqn',
    rsp_total_askp_rsqn TEXT NULL COMMENT '응답 total_askp_rsqn',
    rsp_total_bidp_rsqn TEXT NULL COMMENT '응답 total_bidp_rsqn',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
    rsp_inter2_prdy_clpr TEXT NULL COMMENT '응답 inter2_prdy_clpr',
    rsp_oprc_vrss_hgpr_rate TEXT NULL COMMENT '응답 oprc_vrss_hgpr_rate',
    rsp_intr_antc_cntg_vrss TEXT NULL COMMENT '응답 intr_antc_cntg_vrss',
    rsp_intr_antc_cntg_vrss_sign TEXT NULL COMMENT '응답 intr_antc_cntg_vrss_sign',
    rsp_intr_antc_cntg_prdy_ctrt TEXT NULL COMMENT '응답 intr_antc_cntg_prdy_ctrt',
    rsp_intr_antc_vol TEXT NULL COMMENT '응답 intr_antc_vol',
    rsp_inter2_sdpr TEXT NULL COMMENT '응답 inter2_sdpr',
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
    req_url VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code TEXT NULL COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code TEXT NULL COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd TEXT NULL COMMENT '요청 FID_INPUT_ISCD',
    req_fid_div_cls_code TEXT NULL COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_blng_cls_code TEXT NULL COMMENT '요청 FID_BLNG_CLS_CODE',
    req_fid_trgt_cls_code TEXT NULL COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code TEXT NULL COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    req_fid_input_price_1 TEXT NULL COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2 TEXT NULL COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_vol_cnt TEXT NULL COMMENT '요청 FID_VOL_CNT',
    rt_cd VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_output TEXT NULL COMMENT '응답 Output',
    rsp_hts_kor_isnm TEXT NULL COMMENT '응답 hts_kor_isnm',
    rsp_mksc_shrn_iscd TEXT NULL COMMENT '응답 mksc_shrn_iscd',
    rsp_data_rank TEXT NULL COMMENT '응답 data_rank',
    rsp_stck_prpr TEXT NULL COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign TEXT NULL COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss TEXT NULL COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt TEXT NULL COMMENT '응답 prdy_ctrt',
    rsp_acml_vol TEXT NULL COMMENT '응답 acml_vol',
    rsp_prdy_vol TEXT NULL COMMENT '응답 prdy_vol',
    rsp_lstn_stcn TEXT NULL COMMENT '응답 lstn_stcn',
    rsp_avrg_vol TEXT NULL COMMENT '응답 avrg_vol',
    rsp_n_befr_clpr_vrss_prpr_rate TEXT NULL COMMENT '응답 n_befr_clpr_vrss_prpr_rate',
    rsp_vol_inrt TEXT NULL COMMENT '응답 vol_inrt',
    rsp_vol_tnrt TEXT NULL COMMENT '응답 vol_tnrt',
    rsp_nday_vol_tnrt TEXT NULL COMMENT '응답 nday_vol_tnrt',
    rsp_avrg_tr_pbmn TEXT NULL COMMENT '응답 avrg_tr_pbmn',
    rsp_tr_pbmn_tnrt TEXT NULL COMMENT '응답 tr_pbmn_tnrt',
    rsp_nday_tr_pbmn_tnrt TEXT NULL COMMENT '응답 nday_tr_pbmn_tnrt',
    rsp_acml_tr_pbmn TEXT NULL COMMENT '응답 acml_tr_pbmn',
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

