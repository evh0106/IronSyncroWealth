-- ============================================================
-- Kiwoom REST API 업종(sect) 응답 저장 스키마
-- URL: /api/dostk/sect
-- ============================================================

-- 공통 메타 컬럼: sect_cd (업종코드), fetched_at (수신일시)

-- ------------------------------------------------------------
-- Drop existing tables if they exist (for development/testing purposes)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS ka20001_inds_cur_prc;
DROP TABLE IF EXISTS ka20001_header;
DROP TABLE IF EXISTS ka20002;
DROP TABLE IF EXISTS ka20003;
DROP TABLE IF EXISTS ka20009_header;
DROP TABLE IF EXISTS ka20009_inds_cur_prc_daly;

-- ------------------------------------------------------------
-- ka20001 : 업종현재가
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20001_inds_cur_prc (
    req_dt                  VARCHAR(8)     NOT NULL DEFAULT '' COMMENT '요청 일자',
    req_mrkt_tp             VARCHAR(10)    NOT NULL DEFAULT '' COMMENT '요청 시장구분',
    req_sect_cd             VARCHAR(20)    NOT NULL DEFAULT '' COMMENT '요청 업종코드',
    rsp_tm_n                VARCHAR(6)     NOT NULL DEFAULT '' COMMENT '응답 시간',
    rsp_cur_prc             DECIMAL(20,2)              COMMENT '응답 현재가',
    rsp_pred_pre_sig        CHAR(1)                    COMMENT '응답 전일대비기호(1:상한,2:상승,3:보합,4:하한,5:하락)',
    rsp_pred_pre            DECIMAL(20,2)              COMMENT '응답 전일대비',
    rsp_flu_rt              DECIMAL(10,4)              COMMENT '응답 등락률',
    rsp_trde_qty            BIGINT                     COMMENT '응답 거래량',
    rsp_trde_prica          DECIMAL(20,2)              COMMENT '응답 거래대금',
    rsp_trde_frmatn_stk_num INT                        COMMENT '응답 거래형성종목수',
    rsp_trde_frmatn_rt      DECIMAL(10,4)              COMMENT '응답 거래형성비율',
    rsp_open_pric           DECIMAL(20,2)              COMMENT '응답 시가',
    rsp_high_pric           DECIMAL(20,2)              COMMENT '응답 고가',
    rsp_low_pric            DECIMAL(20,2)              COMMENT '응답 저가',
    rsp_upl                 INT                        COMMENT '응답 상한',
    rsp_rising              INT                        COMMENT '응답 상승',
    rsp_stdns               INT                        COMMENT '응답 보합',
    rsp_fall                INT                        COMMENT '응답 하락',
    rsp_lst                 INT                        COMMENT '응답 하한',
    rsp_w52_hgst_pric       DECIMAL(20,2)              COMMENT '응답 52주최고가',
    rsp_w52_hgst_pric_dt    VARCHAR(8)                 COMMENT '응답 52주최고가일',
    rsp_w52_hgst_pric_pre_rt DECIMAL(10,4)             COMMENT '응답 52주최고가대비율',
    rsp_w52_lwst_pric       DECIMAL(20,2)              COMMENT '응답 52주최저가',
    rsp_w52_lwst_pric_dt    VARCHAR(8)                 COMMENT '응답 52주최저가일',
    rsp_w52_lwst_pric_pre_rt DECIMAL(10,4)             COMMENT '응답 52주최저가대비율',
    rsp_cur_prc_n           DECIMAL(20,2)              COMMENT '응답 시간별 현재가',
    rsp_pred_pre_sig_n      CHAR(1)                    COMMENT '응답 시간별 전일대비기호',
    rsp_pred_pre_n          DECIMAL(20,2)              COMMENT '응답 시간별 전일대비',
    rsp_flu_rt_n            DECIMAL(10,4)              COMMENT '응답 시간별 등락률',
    rsp_trde_qty_n          BIGINT                     COMMENT '응답 시간별 거래량',
    rsp_acc_trde_qty_n      BIGINT                     COMMENT '응답 시간별 누적거래량',
    fetched_at              DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (req_dt, req_mrkt_tp, req_sect_cd, rsp_tm_n),
    INDEX idx_sect_fetched (req_sect_cd, fetched_at),
    INDEX idx_dt_tm (req_dt, rsp_tm_n)
) COMMENT='ka20001 업종현재가';

-- ------------------------------------------------------------
-- ka20002 : 업종별주가요청 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20002 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    sect_cd         VARCHAR(20)   NOT NULL COMMENT '요청 업종코드',
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cur_prc         DECIMAL(20,2)          COMMENT '현재가',
    pred_pre_sig    CHAR(1)                COMMENT '전일대비기호',
    pred_pre        DECIMAL(20,2)          COMMENT '전일대비',
    flu_rt          DECIMAL(10,4)          COMMENT '등락률',
    now_trde_qty    BIGINT                 COMMENT '현재거래량',
    sel_bid         DECIMAL(20,2)          COMMENT '매도호가',
    buy_bid         DECIMAL(20,2)          COMMENT '매수호가',
    open_pric       DECIMAL(20,2)          COMMENT '시가',
    high_pric       DECIMAL(20,2)          COMMENT '고가',
    low_pric        DECIMAL(20,2)          COMMENT '저가',
    PRIMARY KEY (id),
    INDEX idx_sect_fetched (sect_cd, fetched_at),
    INDEX idx_stk_cd (stk_cd)
) COMMENT='ka20002 업종별주가';

-- ------------------------------------------------------------
-- ka20003 : 전업종지수요청 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20003 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stk_cd          VARCHAR(20)            COMMENT '업종코드',
    stk_nm          VARCHAR(100)           COMMENT '업종명',
    cur_prc         DECIMAL(20,2)          COMMENT '현재가',
    pre_sig         CHAR(1)                COMMENT '전일대비기호',
    pred_pre        DECIMAL(20,2)          COMMENT '전일대비',
    flu_rt          DECIMAL(10,4)          COMMENT '등락률',
    trde_qty        BIGINT                 COMMENT '거래량',
    wght            DECIMAL(10,4)          COMMENT '비중',
    trde_prica      DECIMAL(20,2)          COMMENT '거래대금',
    upl             INT                    COMMENT '상한',
    rising          INT                    COMMENT '상승',
    stdns           INT                    COMMENT '보합',
    fall            INT                    COMMENT '하락',
    lst             INT                    COMMENT '하한',
    flo_stk_num     INT                    COMMENT '상장종목수',
    PRIMARY KEY (id),
    INDEX idx_fetched (fetched_at),
    INDEX idx_stk_cd (stk_cd)
) COMMENT='ka20003 전업종지수';

-- ------------------------------------------------------------
-- ka20009 : 업종현재가일별요청 (헤더 + 일별 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka20009_header (
    id                      BIGINT        NOT NULL AUTO_INCREMENT,
    sect_cd                 VARCHAR(20)   NOT NULL COMMENT '요청 업종코드',
    fetched_at              DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cur_prc                 DECIMAL(20,2)          COMMENT '현재가',
    pred_pre_sig            CHAR(1)                COMMENT '전일대비기호',
    pred_pre                DECIMAL(20,2)          COMMENT '전일대비',
    flu_rt                  DECIMAL(10,4)          COMMENT '등락률',
    trde_qty                BIGINT                 COMMENT '거래량',
    trde_prica              DECIMAL(20,2)          COMMENT '거래대금',
    trde_frmatn_stk_num     INT                    COMMENT '거래형성종목수',
    trde_frmatn_rt          DECIMAL(10,4)          COMMENT '거래형성비율',
    open_pric               DECIMAL(20,2)          COMMENT '시가',
    high_pric               DECIMAL(20,2)          COMMENT '고가',
    low_pric                DECIMAL(20,2)          COMMENT '저가',
    upl                     INT                    COMMENT '상한',
    rising                  INT                    COMMENT '상승',
    stdns                   INT                    COMMENT '보합',
    fall                    INT                    COMMENT '하락',
    lst                     INT                    COMMENT '하한',
    w52_hgst_pric           DECIMAL(20,2)          COMMENT '52주최고가',
    w52_hgst_pric_dt        VARCHAR(8)             COMMENT '52주최고가일',
    w52_hgst_pric_pre_rt    DECIMAL(10,4)          COMMENT '52주최고가대비율',
    w52_lwst_pric           DECIMAL(20,2)          COMMENT '52주최저가',
    w52_lwst_pric_dt        VARCHAR(8)             COMMENT '52주최저가일',
    w52_lwst_pric_pre_rt    DECIMAL(10,4)          COMMENT '52주최저가대비율',
    PRIMARY KEY (id),
    INDEX idx_sect_fetched (sect_cd, fetched_at)
) COMMENT='ka20009 업종현재가일별 헤더';

CREATE TABLE IF NOT EXISTS ka20009_inds_cur_prc_daly (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL COMMENT 'ka20009_header.id',
    dt_n            VARCHAR(8)             COMMENT '일자',
    cur_prc_n       DECIMAL(20,2)          COMMENT '현재가',
    pred_pre_sig_n  CHAR(1)                COMMENT '전일대비기호',
    pred_pre_n      DECIMAL(20,2)          COMMENT '전일대비',
    flu_rt_n        DECIMAL(10,4)          COMMENT '등락률',
    acc_trde_qty_n  BIGINT                 COMMENT '누적거래량',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='ka20009 업종현재가 일별 리스트';
