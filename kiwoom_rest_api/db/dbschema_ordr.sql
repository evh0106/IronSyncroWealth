-- ============================================================
-- Kiwoom REST API 주문(ordr) 응답 저장 스키마
-- URL: /api/dostk/ordr
-- specs_request.py  : ORDR_API_SPECS
-- specs_response.py : ORDR_RESPONSE_SPECS
-- ============================================================

-- 공통 패턴:
--   req_dt       VARCHAR(8)   요청 일시 (YYYYMMDD, 호출 시 자동 생성)
--   req_*        요청 파라미터 컬럼
--   rsp_*        응답 컬럼
--   rsp_ord_no   VARCHAR(20)  주문번호 (PK 핵심 구성 요소)
--   fetched_at   DATETIME     수신일시

-- ------------------------------------------------------------
-- Drop existing tables if they exist (for development/testing purposes)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS kt10000_stk_buy_ord CASCADE;
DROP TABLE IF EXISTS kt10001_stk_sll_ord CASCADE;
DROP TABLE IF EXISTS kt10002_stk_mdfy_ord CASCADE;
DROP TABLE IF EXISTS kt10003_stk_cncl_ord CASCADE;
DROP TABLE IF EXISTS kt50000_gold_buy_ord CASCADE;
DROP TABLE IF EXISTS kt50001_gold_sll_ord CASCADE;
DROP TABLE IF EXISTS kt50002_gold_mdfy_ord CASCADE;
DROP TABLE IF EXISTS kt50003_gold_cncl_ord CASCADE;

-- ------------------------------------------------------------
-- kt10000 : 주식 매수주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt10000_stk_buy_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 국내거래소구분 (KRX/NXT/SOR)',
    req_stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_ord_qty         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문수량',
    req_ord_uv          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문단가',
    req_trde_tp         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 매매구분',
    req_cond_uv         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 조건단가',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    rsp_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '응답 국내거래소구분',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt10000 주식 매수주문';

-- ------------------------------------------------------------
-- kt10001 : 주식 매도주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt10001_stk_sll_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 국내거래소구분 (KRX/NXT/SOR)',
    req_stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_ord_qty         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문수량',
    req_ord_uv          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문단가',
    req_trde_tp         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 매매구분',
    req_cond_uv         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 조건단가',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    rsp_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '응답 국내거래소구분',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt10001 주식 매도주문';

-- ------------------------------------------------------------
-- kt10002 : 주식 정정주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt10002_stk_mdfy_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 국내거래소구분 (KRX/NXT/SOR)',
    req_orig_ord_no     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 원주문번호',
    req_stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_mdfy_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 정정수량',
    req_mdfy_uv         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 정정단가',
    req_mdfy_cond_uv    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 정정조건단가',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    rsp_base_orig_ord_no VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 모주문번호',
    rsp_mdfy_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 정정수량',
    rsp_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '응답 국내거래소구분',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at),
    INDEX idx_orig_ord (req_orig_ord_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt10002 주식 정정주문';

-- ------------------------------------------------------------
-- kt10003 : 주식 취소주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt10003_stk_cncl_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_dmst_stex_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 국내거래소구분 (KRX/NXT/SOR)',
    req_orig_ord_no     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 원주문번호',
    req_stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_cncl_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 취소수량',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    rsp_base_orig_ord_no VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 모주문번호',
    rsp_cncl_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 취소수량',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at),
    INDEX idx_orig_ord (req_orig_ord_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt10003 주식 취소주문';

-- ------------------------------------------------------------
-- kt50000 : 금현물 매수주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50000_gold_buy_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_stk_cd          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_ord_qty         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문수량',
    req_ord_uv          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문단가',
    req_trde_tp         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 매매구분',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt50000 금현물 매수주문';

-- ------------------------------------------------------------
-- kt50001 : 금현물 매도주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50001_gold_sll_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_stk_cd          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_ord_qty         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문수량',
    req_ord_uv          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 주문단가',
    req_trde_tp         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '요청 매매구분',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt50001 금현물 매도주문';

-- ------------------------------------------------------------
-- kt50002 : 금현물 정정주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50002_gold_mdfy_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_stk_cd          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_orig_ord_no     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 원주문번호',
    req_mdfy_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 정정수량',
    req_mdfy_uv         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 정정단가',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    rsp_base_orig_ord_no VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 모주문번호',
    rsp_mdfy_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 정정수량',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at),
    INDEX idx_orig_ord (req_orig_ord_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt50002 금현물 정정주문';

-- ------------------------------------------------------------
-- kt50003 : 금현물 취소주문
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50003_gold_cncl_ord (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자 (YYYYMMDD)',
    req_orig_ord_no     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 원주문번호',
    req_stk_cd          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 종목코드',
    req_cncl_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '요청 취소수량',
    rsp_ord_no          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 주문번호',
    rsp_base_orig_ord_no VARCHAR(20) NOT NULL DEFAULT '' COMMENT '응답 모주문번호',
    rsp_cncl_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 취소수량',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (req_stk_cd, fetched_at),
    INDEX idx_orig_ord (req_orig_ord_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='kt50003 금현물 취소주문';