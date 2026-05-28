-- =============================================================
-- chart (차트) 모듈 DB 스키마
-- docs/키움 REST API 문서/chart/*.md 기반
-- =============================================================

-- -------------------------------------------------------------
-- Drop existing tables if they exist (for development/testing purposes)
-- -------------------------------------------------------------
DROP TABLE IF EXISTS ka10060_stk_invsr_orgn_chart CASCADE;
DROP TABLE IF EXISTS ka10064_opmr_invsr_trde_chart CASCADE;
DROP TABLE IF EXISTS ka10079_stk_tic_chart_qry CASCADE;
DROP TABLE IF EXISTS ka10079_header CASCADE;
DROP TABLE IF EXISTS ka10080_stk_min_pole_chart_qry CASCADE;
DROP TABLE IF EXISTS ka10080_header CASCADE;
DROP TABLE IF EXISTS ka10081_stk_dt_pole_chart_qry CASCADE;
DROP TABLE IF EXISTS ka10081_header CASCADE;
DROP TABLE IF EXISTS ka10082_stk_stk_pole_chart_qry CASCADE;
DROP TABLE IF EXISTS ka10082_header CASCADE;
DROP TABLE IF EXISTS ka10083_stk_mth_pole_chart_qry CASCADE;
DROP TABLE IF EXISTS ka10083_header CASCADE;
DROP TABLE IF EXISTS ka10094_stk_yr_pole_chart_qry CASCADE;
DROP TABLE IF EXISTS ka10094_header CASCADE;
DROP TABLE IF EXISTS ka20004_inds_tic_chart_qry CASCADE;
DROP TABLE IF EXISTS ka20004_header CASCADE;
DROP TABLE IF EXISTS ka20005_inds_min_pole_qry CASCADE;
DROP TABLE IF EXISTS ka20005_header CASCADE;
DROP TABLE IF EXISTS ka20006_inds_dt_pole_qry CASCADE;
DROP TABLE IF EXISTS ka20006_header CASCADE;
DROP TABLE IF EXISTS ka20007_inds_stk_pole_qry CASCADE;
DROP TABLE IF EXISTS ka20007_header CASCADE;
DROP TABLE IF EXISTS ka20008_inds_mth_pole_qry CASCADE;
DROP TABLE IF EXISTS ka20008_header CASCADE;
DROP TABLE IF EXISTS ka20019_inds_yr_pole_qry CASCADE;
DROP TABLE IF EXISTS ka20019_header CASCADE;
DROP TABLE IF EXISTS ka50079_gds_tic_chart_qry CASCADE;
DROP TABLE IF EXISTS ka50080_gds_min_chart_qry CASCADE;
DROP TABLE IF EXISTS ka50081_gds_day_chart_qry CASCADE;
DROP TABLE IF EXISTS ka50082_gds_week_chart_qry CASCADE;
DROP TABLE IF EXISTS ka50083_gds_month_chart_qry CASCADE;
DROP TABLE IF EXISTS ka50091_gds_tic_chart_qry CASCADE;
DROP TABLE IF EXISTS ka50092_gds_min_chart_qry CASCADE;

-- -------------------------------------------------------------
-- ka10060 – 종목별투자자기관별차트요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10060_stk_invsr_orgn_chart (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt           VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자',
    req_stk_cd       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_amt_qty_tp   VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 금액수량구분',
    req_trde_tp      VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 매매구분',
    req_unit_tp      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 단위구분',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    acc_trde_prica   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    ind_invsr        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '개인투자자',
    frgnr_invsr      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국인투자자',
    orgn             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기관계',
    fnnc_invt        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '금융투자',
    insrnc           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '보험',
    invtrt           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '투신',
    etc_fnnc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타금융',
    bank             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '은행',
    penfnd_etc       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '연기금등',
    samo_fund        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '사모펀드',
    natn             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '국가',
    etc_corp         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타법인',
    natfor           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '내외국인',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_stk_fetched (req_stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목별투자자기관별차트';

-- -------------------------------------------------------------
-- ka10064 – 장중투자자별매매차트요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10064_opmr_invsr_trde_chart (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_mrkt_tp      VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 시장구분',
    req_amt_qty_tp   VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 금액수량구분',
    req_trde_tp      VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 매매구분',
    req_stk_cd       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    tm               VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '시간',
    frgnr_invsr      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국인투자자',
    orgn             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기관계',
    invtrt           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '투신',
    insrnc           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '보험',
    bank             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '은행',
    penfnd_etc       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '연기금등',
    etc_corp         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타법인',
    natn             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '국가',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_stk_fetched (req_stk_cd, fetched_at),
    INDEX idx_tm (tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='장중투자자별매매차트';

-- -------------------------------------------------------------
-- ka10079 – 주식틱차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10079_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청/응답 종목코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    last_tic_cnt     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '마지막틱갯수',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식틱차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka10079_stk_tic_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식틱차트조회';

-- -------------------------------------------------------------
-- ka10080 – 주식분봉차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10080_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청/응답 종목코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식분봉차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka10080_stk_min_pole_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식분봉차트조회';

-- -------------------------------------------------------------
-- ka10081 – 주식일봉차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10081_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청/응답 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식일봉차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka10081_stk_dt_pole_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    trde_tern_rt     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래회전율',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식일봉차트조회';

-- -------------------------------------------------------------
-- ka10082 – 주식주봉차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10082_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청/응답 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식주봉차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka10082_stk_stk_pole_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    trde_tern_rt     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래회전율',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식주봉차트조회';

-- -------------------------------------------------------------
-- ka10083 – 주식월봉차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10083_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청/응답 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식월봉차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka10083_stk_mth_pole_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    trde_tern_rt     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래회전율',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식월봉차트조회';

-- -------------------------------------------------------------
-- ka10094 – 주식년봉차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10094_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청/응답 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식년봉차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka10094_stk_yr_pole_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식년봉차트조회';

-- -------------------------------------------------------------
-- ka20004 – 업종틱차트조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20004_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청/응답 업종코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_inds_fetched (inds_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종틱차트조회 헤더';

CREATE TABLE IF NOT EXISTS ka20004_inds_tic_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '업종코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_inds_fetched (inds_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종틱차트조회';

-- -------------------------------------------------------------
-- ka20005 – 업종분봉조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20005_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청/응답 업종코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_inds_fetched (inds_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종분봉조회 헤더';

CREATE TABLE IF NOT EXISTS ka20005_inds_min_pole_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '업종코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_inds_fetched (inds_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종분봉조회';

-- -------------------------------------------------------------
-- ka20006 – 업종일봉조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20006_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청/응답 업종코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_inds_fetched (inds_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종일봉조회 헤더';

CREATE TABLE IF NOT EXISTS ka20006_inds_dt_pole_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '업종코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_inds_fetched (inds_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종일봉조회';

-- -------------------------------------------------------------
-- ka20007 – 업종주봉조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20007_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청/응답 업종코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_inds_fetched (inds_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종주봉조회 헤더';

CREATE TABLE IF NOT EXISTS ka20007_inds_stk_pole_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '업종코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_inds_fetched (inds_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종주봉조회';

-- -------------------------------------------------------------
-- ka20008 – 업종월봉조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20008_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청/응답 업종코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_inds_fetched (inds_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종월봉조회 헤더';

CREATE TABLE IF NOT EXISTS ka20008_inds_mth_pole_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '업종코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_inds_fetched (inds_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종월봉조회';

-- -------------------------------------------------------------
-- ka20019 – 업종년봉조회요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20019_header (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청/응답 업종코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_inds_fetched (inds_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종년봉조회 헤더';

CREATE TABLE IF NOT EXISTS ka20019_inds_yr_pole_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    inds_cd          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '업종코드',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    trde_prica       VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_inds_fetched (inds_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종년봉조회';

-- -------------------------------------------------------------
-- ka50079 – 금현물틱차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50079_gds_tic_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    dt               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '일자',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물틱차트조회';

-- -------------------------------------------------------------
-- ka50080 – 금현물분봉차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50080_gds_min_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    dt               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '일자',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물분봉차트조회';

-- -------------------------------------------------------------
-- ka50081 – 금현물일봉차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50081_gds_day_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물일봉차트조회';

-- -------------------------------------------------------------
-- ka50082 – 금현물주봉차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50082_gds_week_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물주봉차트조회';

-- -------------------------------------------------------------
-- ka50083 – 금현물월봉차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50083_gds_month_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    base_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 기준일자',
    upd_stkpc_tp     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 수정주가구분',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    dt               VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_dt (dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물월봉차트조회';

-- -------------------------------------------------------------
-- ka50091 – 금현물당일틱차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50091_gds_tic_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    cntr_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    dt               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '일자',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물당일틱차트조회';

-- -------------------------------------------------------------
-- ka50092 – 금현물당일분봉차트조회요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka50092_gds_min_chart_qry (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    tic_scope        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 틱범위',
    cntr_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결가',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    trde_qty         VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    open_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    cntr_tm          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결시간',
    dt               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '일자',
    pred_pre_sig     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at),
    INDEX idx_cntr_tm (cntr_tm)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='금현물당일분봉차트조회';