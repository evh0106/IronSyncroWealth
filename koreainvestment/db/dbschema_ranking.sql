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
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_input_vol_1        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_VOL_1',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
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
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
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
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_option             VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_OPTION',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_MRKT_DIV_CODE',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
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
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_RANK_SORT_CLS_CODE',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_VOL_CNT',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
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
    id            BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id         VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url       VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_cts_area  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 CTS_AREA',
    req_gb1       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB1',
    req_upjong    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 UPJONG',
    req_gb2       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB2',
    req_gb3       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB3',
    req_f_dt      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 F_DT',
    req_t_dt      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 T_DT',
    req_gb4       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 GB4',
    rt_cd         VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd        VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1          VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
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
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    req_fid_aply_rang_prc_1    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_APLY_RANG_PRC_1',
    req_fid_aply_rang_prc_2    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_APLY_RANG_PRC_2',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    req_fid_input_iscd_2       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd_2',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    req_fid_aply_rang_vol      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_vol',
    req_fid_aply_rang_prc_2    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_2',
    req_fid_aply_rang_prc_1    VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_aply_rang_prc_1',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_cond_mrkt_div_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_mrkt_div_code',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_cond_scr_div_code',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_iscd',
    req_fid_rank_sort_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rank_sort_cls_code',
    req_fid_input_cnt_1        VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_cnt_1',
    req_fid_prc_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_prc_cls_code',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_input_price_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_vol_cnt',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_cls_code',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_trgt_exls_cls_code',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_div_cls_code',
    req_fid_rsfl_rate1         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 fid_rsfl_rate1',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
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
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
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
    id                         BIGINT NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                      VARCHAR(32) NOT NULL DEFAULT '' COMMENT 'TR ID',
    req_url                    VARCHAR(200) NOT NULL DEFAULT '' COMMENT '요청 URL',
    req_fid_mrkt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_MRKT_CLS_CODE',
    req_fid_cond_scr_div_code  VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_COND_SCR_DIV_CODE',
    req_fid_input_iscd         VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_ISCD',
    req_fid_div_cls_code       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_DIV_CLS_CODE',
    req_fid_input_price_1      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_1',
    req_fid_input_price_2      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_INPUT_PRICE_2',
    req_fid_vol_cnt            VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_VOL_CNT',
    req_fid_trgt_cls_code      VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_CLS_CODE',
    req_fid_trgt_exls_cls_code VARCHAR(255) NOT NULL DEFAULT '' COMMENT '요청 FID_TRGT_EXLS_CLS_CODE',
    rt_cd                      VARCHAR(10) NOT NULL DEFAULT '' COMMENT '응답 rt_cd',
    msg_cd                     VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 msg_cd',
    msg1                       VARCHAR(255) NOT NULL DEFAULT '' COMMENT '응답 msg1',
    response_json              LONGTEXT NULL COMMENT '응답 원문 JSON',
    fetched_at                 DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
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
