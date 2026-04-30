-- =============================================================
-- ranking (/uapi/domestic-stock/v1/ranking/) 모듈 DB 스키마
-- source: 한국투자증권_오픈API_전체문서_20260430_030000.xlsx
-- =============================================================

-- 테이블명 규칙: URL 마지막 경로를 snake_case 로 변환
-- 예: /uapi/domestic-stock/v1/ranking/market-cap -> market_cap

DROP TABLE IF EXISTS overtime_exp_trans_fluct;
DROP TABLE IF EXISTS exp_trans_updown;
DROP TABLE IF EXISTS quote_balance;
DROP TABLE IF EXISTS credit_balance;
DROP TABLE IF EXISTS overtime_volume;
DROP TABLE IF EXISTS dividend_rate;
DROP TABLE IF EXISTS after_hour_balance;
DROP TABLE IF EXISTS short_sale;
DROP TABLE IF EXISTS disparity;
DROP TABLE IF EXISTS hts_top_view;
DROP TABLE IF EXISTS profit_asset_index;
DROP TABLE IF EXISTS near_new_highlow;
DROP TABLE IF EXISTS prefer_disparate_ratio;
DROP TABLE IF EXISTS bulk_trans_num;
DROP TABLE IF EXISTS finance_ratio;
DROP TABLE IF EXISTS market_cap;
DROP TABLE IF EXISTS traded_by_company;
DROP TABLE IF EXISTS fluctuation;
DROP TABLE IF EXISTS market_value;
DROP TABLE IF EXISTS top_interest_stock;
DROP TABLE IF EXISTS volume_power;
DROP TABLE IF EXISTS overtime_fluctuation;

-- =============================================================
-- overtime_exp_trans_fluct - 국내주식 시간외예상체결등락률 (FHKST11860000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/overtime-exp-trans-fluct
-- =============================================================
CREATE TABLE IF NOT EXISTS overtime_exp_trans_fluct (
    id                               BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                            VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                          VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_rank_sort_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_div_cls_code             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_input_price_1            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_input_vol_1              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_VOL_1',
    rt_cd                            VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                           VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_data_rank                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_iscd_stat_cls_code           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 iscd_stat_cls_code',
    rsp_stck_shrn_iscd               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_ovtm_untp_antc_cnpr          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_antc_cnpr',
    rsp_ovtm_untp_antc_cntg_vrss     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_antc_cntg_vrss',
    rsp_ovtm_untp_antc_cntg_vrsssign VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_antc_cntg_vrsssign',
    rsp_ovtm_untp_antc_cntg_ctrt     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_antc_cntg_ctrt',
    rsp_ovtm_untp_askp_rsqn1         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_askp_rsqn1',
    rsp_ovtm_untp_bidp_rsqn1         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_bidp_rsqn1',
    rsp_ovtm_untp_antc_cnqn          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_antc_cnqn',
    rsp_itmt_vol                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 itmt_vol',
    rsp_stck_prpr                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    response_json                    LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/overtime-exp-trans-fluct';

-- =============================================================
-- exp_trans_updown - 국내주식 예상체결 상승/하락상위 (FHPST01820000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/exp-trans-updown
-- =============================================================
CREATE TABLE IF NOT EXISTS exp_trans_updown (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_aply_rang_prc_1    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_1',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_pbmn               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_pbmn',
    req_fid_blng_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_blng_cls_code',
    req_fid_mkop_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_mkop_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/exp-trans-updown';

-- =============================================================
-- quote_balance - 국내주식 호가잔량 순위 (FHPST01720000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/quote-balance
-- =============================================================
CREATE TABLE IF NOT EXISTS quote_balance (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_total_askp_rsqn        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 total_askp_rsqn',
    rsp_total_bidp_rsqn        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 total_bidp_rsqn',
    rsp_total_ntsl_bidp_rsqn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 total_ntsl_bidp_rsqn',
    rsp_shnu_rsqn_rate         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 shnu_rsqn_rate',
    rsp_seln_rsqn_rate         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 seln_rsqn_rate',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/quote-balance';

-- =============================================================
-- credit_balance - 국내주식 신용잔고 상위 (FHKST17010000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/credit-balance
-- =============================================================
CREATE TABLE IF NOT EXISTS credit_balance (
    id                           BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                        VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_scr_div_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_option               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_OPTION',
    req_fid_cond_mrkt_div_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_rank_sort_cls_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    rt_cd                        VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                       VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_bstp_cls_code            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bstp_cls_code',
    rsp_hts_kor_isnm             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stnd_date1               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stnd_date1',
    rsp_stnd_date2               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stnd_date2',
    rsp_mksc_shrn_iscd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_stck_prpr                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_whol_loan_rmnd_stcn      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 whol_loan_rmnd_stcn',
    rsp_whol_loan_rmnd_amt       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 whol_loan_rmnd_amt',
    rsp_whol_loan_rmnd_rate      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 whol_loan_rmnd_rate',
    rsp_whol_stln_rmnd_stcn      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 whol_stln_rmnd_stcn',
    rsp_whol_stln_rmnd_amt       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 whol_stln_rmnd_amt',
    rsp_whol_stln_rmnd_rate      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 whol_stln_rmnd_rate',
    rsp_nday_vrss_loan_rmnd_inrt VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 nday_vrss_loan_rmnd_inrt',
    rsp_nday_vrss_stln_rmnd_inrt VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 nday_vrss_stln_rmnd_inrt',
    response_json                LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/credit-balance';

-- =============================================================
-- overtime_volume - 국내주식 시간외거래량순위 (FHPST02350000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/overtime-volume
-- =============================================================
CREATE TABLE IF NOT EXISTS overtime_volume (
    id                           BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                        VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_rank_sort_cls_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_input_price_1        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_vol_cnt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_VOL_CNT',
    req_fid_trgt_cls_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    rt_cd                        VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                       VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_ovtm_untp_exch_vol       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_exch_vol',
    rsp_ovtm_untp_exch_tr_pbmn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_exch_tr_pbmn',
    rsp_ovtm_untp_kosdaq_vol     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_kosdaq_vol',
    rsp_ovtm_untp_kosdaq_tr_pbmn VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_kosdaq_tr_pbmn',
    rsp_stck_shrn_iscd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_shrn_iscd',
    rsp_hts_kor_isnm             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_ovtm_untp_prpr           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prpr',
    rsp_ovtm_untp_prdy_vrss      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prdy_vrss',
    rsp_ovtm_untp_prdy_vrss_sign VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prdy_vrss_sign',
    rsp_ovtm_untp_prdy_ctrt      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prdy_ctrt',
    rsp_ovtm_untp_seln_rsqn      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_seln_rsqn',
    rsp_ovtm_untp_shnu_rsqn      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_shnu_rsqn',
    rsp_ovtm_untp_vol            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_vol',
    rsp_ovtm_vrss_acml_vol_rlim  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_vrss_acml_vol_rlim',
    rsp_stck_prpr                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_acml_vol                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_bidp                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bidp',
    rsp_askp                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 askp',
    response_json                LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/overtime-volume';

-- =============================================================
-- dividend_rate - 국내주식 배당률 상위 (HHKDB13470100)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/dividend-rate
-- =============================================================
CREATE TABLE IF NOT EXISTS dividend_rate (
    id                   BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url              VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_cts_area         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 CTS_AREA',
    req_gb1              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB1',
    req_upjong           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 UPJONG',
    req_gb2              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB2',
    req_gb3              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB3',
    req_f_dt             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 F_DT',
    req_t_dt             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 T_DT',
    req_gb4              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB4',
    rt_cd                VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd               VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_rank             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 rank',
    rsp_sht_cd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 sht_cd',
    rsp_isin_name        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 isin_name',
    rsp_record_date      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 record_date',
    rsp_per_sto_divi_amt VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 per_sto_divi_amt',
    rsp_divi_rate        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 divi_rate',
    rsp_divi_kind        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 divi_kind',
    response_json        LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/dividend-rate';

-- =============================================================
-- after_hour_balance - 국내주식 시간외잔량 순위 (FHPST01760000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/after-hour-balance
-- =============================================================
CREATE TABLE IF NOT EXISTS after_hour_balance (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_shrn_iscd',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_ovtm_total_askp_rsqn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_total_askp_rsqn',
    rsp_ovtm_total_bidp_rsqn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_total_bidp_rsqn',
    rsp_mkob_otcp_vol          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mkob_otcp_vol',
    rsp_mkfa_otcp_vol          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mkfa_otcp_vol',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/after-hour-balance';

-- =============================================================
-- short_sale - 국내주식 공매도 상위종목 (FHPST04820000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/short-sale
-- =============================================================
CREATE TABLE IF NOT EXISTS short_sale (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_period_div_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_PERIOD_DIV_CODE',
    req_fid_input_cnt_1        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_CNT_1',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_aply_rang_vol      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_APLY_RANG_VOL',
    req_fid_aply_rang_prc_1    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_APLY_RANG_PRC_1',
    req_fid_aply_rang_prc_2    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_APLY_RANG_PRC_2',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_tr_pbmn',
    rsp_ssts_cntg_qty          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ssts_cntg_qty',
    rsp_ssts_vol_rlim          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ssts_vol_rlim',
    rsp_ssts_tr_pbmn           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ssts_tr_pbmn',
    rsp_ssts_tr_pbmn_rlim      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ssts_tr_pbmn_rlim',
    rsp_stnd_date1             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stnd_date1',
    rsp_stnd_date2             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stnd_date2',
    rsp_avrg_prc               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 avrg_prc',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/short-sale';

-- =============================================================
-- disparity - 국내주식 이격도 순위 (FHPST01780000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/disparity
-- =============================================================
CREATE TABLE IF NOT EXISTS disparity (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_hour_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_hour_cls_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_d5_dsrt                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 d5_dsrt',
    rsp_d10_dsrt               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 d10_dsrt',
    rsp_d20_dsrt               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 d20_dsrt',
    rsp_d60_dsrt               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 d60_dsrt',
    rsp_d120_dsrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 d120_dsrt',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/disparity';

-- =============================================================
-- hts_top_view - HTS조회상위20종목 (HHMCM000100C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/hts-top-view
-- =============================================================
CREATE TABLE IF NOT EXISTS hts_top_view (
    id                    BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                 VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url               VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    rt_cd                 VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mrkt_div_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mrkt_div_cls_code',
    rsp_mksc_shrn_iscd    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    response_json         LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at            DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/hts-top-view';

-- =============================================================
-- profit_asset_index - 국내주식 수익자산지표 순위 (FHPST01730000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/profit-asset-index
-- =============================================================
CREATE TABLE IF NOT EXISTS profit_asset_index (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_input_option_1     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_option_1',
    req_fid_input_option_2     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_option_2',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_blng_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_blng_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_sale_totl_prfi         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 sale_totl_prfi',
    rsp_bsop_prti              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bsop_prti',
    rsp_op_prfi                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 op_prfi',
    rsp_thtr_ntin              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 thtr_ntin',
    rsp_total_aset             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 total_aset',
    rsp_total_lblt             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 total_lblt',
    rsp_total_cptl             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 total_cptl',
    rsp_stac_month             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stac_month',
    rsp_stac_month_cls_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stac_month_cls_code',
    rsp_iqry_csnu              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 iqry_csnu',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/profit-asset-index';

-- =============================================================
-- near_new_highlow - 국내주식 신고/신저근접종목 상위 (FHPST01870000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/near-new-highlow
-- =============================================================
CREATE TABLE IF NOT EXISTS near_new_highlow (
    id            BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id         VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url       VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    rt_cd         VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd        VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/near-new-highlow';

-- =============================================================
-- prefer_disparate_ratio - 국내주식 우선주/괴리율 상위 (FHPST01770000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/prefer-disparate-ratio
-- =============================================================
CREATE TABLE IF NOT EXISTS prefer_disparate_ratio (
    id            BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id         VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url       VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    rt_cd         VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd        VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/prefer-disparate-ratio';

-- =============================================================
-- bulk_trans_num - 국내주식 대량체결건수 상위 (FHKST190900C0)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/bulk-trans-num
-- =============================================================
CREATE TABLE IF NOT EXISTS bulk_trans_num (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_aply_rang_prc_1    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_1',
    req_fid_aply_rang_prc_2    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_2',
    req_fid_input_iscd_2       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd_2',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_shnu_cntg_csnu         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 shnu_cntg_csnu',
    rsp_seln_cntg_csnu         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 seln_cntg_csnu',
    rsp_ntby_cnqn              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ntby_cnqn',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/bulk-trans-num';

-- =============================================================
-- finance_ratio - 국내주식 재무비율 순위 (FHPST01750000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/finance-ratio
-- =============================================================
CREATE TABLE IF NOT EXISTS finance_ratio (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_input_option_1     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_option_1',
    req_fid_input_option_2     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_option_2',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_blng_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_blng_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_cptl_op_prfi           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 cptl_op_prfi',
    rsp_cptl_ntin_rate         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 cptl_ntin_rate',
    rsp_sale_totl_rate         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 sale_totl_rate',
    rsp_sale_ntin_rate         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 sale_ntin_rate',
    rsp_bis                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bis',
    rsp_lblt_rate              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 lblt_rate',
    rsp_bram_depn              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bram_depn',
    rsp_rsrv_rate              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 rsrv_rate',
    rsp_grs                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 grs',
    rsp_op_prfi_inrt           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 op_prfi_inrt',
    rsp_bsop_prfi_inrt         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bsop_prfi_inrt',
    rsp_ntin_inrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ntin_inrt',
    rsp_equt_inrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 equt_inrt',
    rsp_cptl_tnrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 cptl_tnrt',
    rsp_sale_bond_tnrt         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 sale_bond_tnrt',
    rsp_totl_aset_inrt         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 totl_aset_inrt',
    rsp_stac_month             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stac_month',
    rsp_stac_month_cls_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stac_month_cls_code',
    rsp_iqry_csnu              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 iqry_csnu',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/finance-ratio';

-- =============================================================
-- market_cap - 국내주식 시가총액 상위 (FHPST01740000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/market-cap
-- =============================================================
CREATE TABLE IF NOT EXISTS market_cap (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_lstn_stcn              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 lstn_stcn',
    rsp_stck_avls              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_avls',
    rsp_mrkt_whol_avls_rlim    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mrkt_whol_avls_rlim',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/market-cap';

-- =============================================================
-- traded_by_company - 국내주식 당사매매종목 상위 (FHPST01860000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/traded-by-company
-- =============================================================
CREATE TABLE IF NOT EXISTS traded_by_company (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_input_date_1       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_date_1',
    req_fid_input_date_2       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_date_2',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_aply_rang_vol      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_vol',
    req_fid_aply_rang_prc_2    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_2',
    req_fid_aply_rang_prc_1    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_1',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_tr_pbmn',
    rsp_seln_cnqn_smtn         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 seln_cnqn_smtn',
    rsp_shnu_cnqn_smtn         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 shnu_cnqn_smtn',
    rsp_ntby_cnqn              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ntby_cnqn',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/traded-by-company';

-- =============================================================
-- fluctuation - 국내주식 등락률 순위 (FHPST01700000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/fluctuation
-- =============================================================
CREATE TABLE IF NOT EXISTS fluctuation (
    id                                BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                             VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                           VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_rank_sort_cls_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_input_cnt_1               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_cnt_1',
    req_fid_prc_cls_code              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_prc_cls_code',
    req_fid_input_price_1             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt                   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_trgt_cls_code             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_div_cls_code              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_rsfl_rate1                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rsfl_rate1',
    req_fid_rsfl_rate2                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rsfl_rate2',
    rt_cd                             VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                            VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_shrn_iscd                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_shrn_iscd',
    rsp_data_rank                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm                  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol                      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_stck_hgpr                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_hgpr',
    rsp_hgpr_hour                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hgpr_hour',
    rsp_acml_hgpr_date                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_hgpr_date',
    rsp_stck_lwpr                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_lwpr',
    rsp_lwpr_hour                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 lwpr_hour',
    rsp_acml_lwpr_date                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_lwpr_date',
    rsp_lwpr_vrss_prpr_rate           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 lwpr_vrss_prpr_rate',
    rsp_dsgt_date_clpr_vrss_prpr_rate VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 dsgt_date_clpr_vrss_prpr_rate',
    rsp_cnnt_ascn_dynu                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 cnnt_ascn_dynu',
    rsp_hgpr_vrss_prpr_rate           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hgpr_vrss_prpr_rate',
    rsp_cnnt_down_dynu                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 cnnt_down_dynu',
    rsp_oprc_vrss_prpr_sign           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 oprc_vrss_prpr_sign',
    rsp_oprc_vrss_prpr                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 oprc_vrss_prpr',
    rsp_oprc_vrss_prpr_rate           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 oprc_vrss_prpr_rate',
    rsp_prd_rsfl                      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prd_rsfl',
    rsp_prd_rsfl_rate                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prd_rsfl_rate',
    response_json                     LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/fluctuation';

-- =============================================================
-- market_value - 국내주식 시장가치 순위 (FHPST01790000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/market-value
-- =============================================================
CREATE TABLE IF NOT EXISTS market_value (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_input_option_1     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_option_1',
    req_fid_input_option_2     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_option_2',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_blng_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_blng_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_per                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 per',
    rsp_pbr                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 pbr',
    rsp_pcr                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 pcr',
    rsp_psr                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 psr',
    rsp_eps                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 eps',
    rsp_eva                    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 eva',
    rsp_ebitda                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ebitda',
    rsp_pv_div_ebitda          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 pv_div_ebitda',
    rsp_ebitda_div_fnnc_expn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ebitda_div_fnnc_expn',
    rsp_stac_month             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stac_month',
    rsp_stac_month_cls_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stac_month_cls_code',
    rsp_iqry_csnu              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 iqry_csnu',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/market-value';

-- =============================================================
-- top_interest_stock - 국내주식 관심종목등록 상위 (FHPST01800000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/top-interest-stock
-- =============================================================
CREATE TABLE IF NOT EXISTS top_interest_stock (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_input_iscd_2       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd_2',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_cnt_1        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_cnt_1',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_mrkt_div_cls_name      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mrkt_div_cls_name',
    rsp_mksc_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_acml_tr_pbmn           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_tr_pbmn',
    rsp_askp                   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 askp',
    rsp_bidp                   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bidp',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_inter_issu_reg_csnu    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 inter_issu_reg_csnu',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/top-interest-stock';

-- =============================================================
-- volume_power - 국내주식 체결강도 상위 (FHPST01680000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/volume-power
-- =============================================================
CREATE TABLE IF NOT EXISTS volume_power (
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_stck_shrn_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_shrn_iscd',
    rsp_data_rank              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 data_rank',
    rsp_hts_kor_isnm           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_stck_prpr              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_prdy_vrss              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss',
    rsp_prdy_vrss_sign         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_vrss_sign',
    rsp_prdy_ctrt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 prdy_ctrt',
    rsp_acml_vol               VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_tday_rltv              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 tday_rltv',
    rsp_seln_cnqn_smtn         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 seln_cnqn_smtn',
    rsp_shnu_cnqn_smtn         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 shnu_cnqn_smtn',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/volume-power';

-- =============================================================
-- overtime_fluctuation - 국내주식 시간외등락율순위 (FHPST02340000)
-- METHOD: GET
-- URL: /uapi/domestic-stock/v1/ranking/overtime-fluctuation
-- =============================================================
CREATE TABLE IF NOT EXISTS overtime_fluctuation (
    id                           BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                        VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_mrkt_cls_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_cond_scr_div_code    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_div_cls_code         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_input_price_1        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_vol_cnt              VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_VOL_CNT',
    req_fid_trgt_cls_code        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    rt_cd                        VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                       VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    rsp_ovtm_untp_uplm_issu_cnt  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_uplm_issu_cnt',
    rsp_ovtm_untp_ascn_issu_cnt  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_ascn_issu_cnt',
    rsp_ovtm_untp_stnr_issu_cnt  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_stnr_issu_cnt',
    rsp_ovtm_untp_lslm_issu_cnt  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_lslm_issu_cnt',
    rsp_ovtm_untp_down_issu_cnt  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_down_issu_cnt',
    rsp_ovtm_untp_acml_vol       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_acml_vol',
    rsp_ovtm_untp_acml_tr_pbmn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_acml_tr_pbmn',
    rsp_ovtm_untp_exch_vol       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_exch_vol',
    rsp_ovtm_untp_exch_tr_pbmn   VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_exch_tr_pbmn',
    rsp_ovtm_untp_kosdaq_vol     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_kosdaq_vol',
    rsp_ovtm_untp_kosdaq_tr_pbmn VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_kosdaq_tr_pbmn',
    rsp_mksc_shrn_iscd           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 mksc_shrn_iscd',
    rsp_hts_kor_isnm             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 hts_kor_isnm',
    rsp_ovtm_untp_prpr           VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prpr',
    rsp_ovtm_untp_prdy_vrss      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prdy_vrss',
    rsp_ovtm_untp_prdy_vrss_sign VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prdy_vrss_sign',
    rsp_ovtm_untp_prdy_ctrt      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_prdy_ctrt',
    rsp_ovtm_untp_askp1          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_askp1',
    rsp_ovtm_untp_seln_rsqn      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_seln_rsqn',
    rsp_ovtm_untp_bidp1          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_bidp1',
    rsp_ovtm_untp_shnu_rsqn      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_shnu_rsqn',
    rsp_ovtm_untp_vol            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_untp_vol',
    rsp_ovtm_vrss_acml_vol_rlim  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 ovtm_vrss_acml_vol_rlim',
    rsp_stck_prpr                VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 stck_prpr',
    rsp_acml_vol                 VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 acml_vol',
    rsp_bidp                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 bidp',
    rsp_askp                     VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 askp',
    response_json                LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_rt_cd (rt_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ranking/overtime-fluctuation';

-- =============================================================
-- 인덱스 설명
-- =============================================================
-- idx_req_dt: 시간 범위 조회
-- idx_tr_id: TR_ID 조건 조회
-- idx_rt_cd: 성공/실패 구분 조회 (rt_cd = 0 성공)
