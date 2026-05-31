-- =============================================================
-- ISW 매매등록(주문 입력) 저장 스키마
-- 대상 화면: iswWeb /trade/register
-- =============================================================

CREATE DATABASE IF NOT EXISTS isw_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_general_ci;

USE isw_db;

-- -------------------------------------------------------------
-- Drop existing table if it exists (for development/testing)
-- -------------------------------------------------------------
DROP TABLE IF EXISTS isw_trd_order_register;

-- -------------------------------------------------------------
-- 매매등록 주문 저장 테이블
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_trd_order_register (
    trade_id                    BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '매매등록 ID',
    broker                      VARCHAR(20)     NOT NULL DEFAULT 'kis' COMMENT '브로커 구분(kis/kiwoom/isw)',
    account_no                  VARCHAR(40)     NOT NULL DEFAULT '' COMMENT '계좌번호',
    market_code                 VARCHAR(40)     NOT NULL DEFAULT '' COMMENT '시장 구분 코드(kospi/kosdaq/... )',
    market_name                 VARCHAR(100)    NOT NULL DEFAULT '' COMMENT '시장 구분명',
    symbol_code                 VARCHAR(40)     NOT NULL DEFAULT '' COMMENT '종목코드',
    order_datetime              DATETIME        NOT NULL COMMENT '주문일시',
    side                        VARCHAR(8)      NOT NULL DEFAULT 'buy' COMMENT '매매구분(buy/sell)',
    order_type                  VARCHAR(16)     NOT NULL DEFAULT 'limit' COMMENT '주문유형(limit/market)',
    quantity                    INT UNSIGNED    NOT NULL DEFAULT 0 COMMENT '주문수량',
    price                       DECIMAL(18,4)   NOT NULL DEFAULT 0 COMMENT '주문가격(시장가인 경우 0 가능)',
    memo                        VARCHAR(500)    NOT NULL DEFAULT '' COMMENT '사용자 메모',
    order_status                VARCHAR(20)     NOT NULL DEFAULT 'registered' COMMENT '주문상태(registered/requested/filled/canceled/rejected)',
    created_at                  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '등록일시',
    updated_at                  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',

    PRIMARY KEY (trade_id),
    INDEX idx_trd_account_datetime (account_no, order_datetime),
    INDEX idx_trd_market_symbol_datetime (market_code, symbol_code, order_datetime),
    INDEX idx_trd_status_created (order_status, created_at),

    CONSTRAINT chk_trd_side CHECK (side IN ('buy', 'sell')),
    CONSTRAINT chk_trd_order_type CHECK (order_type IN ('limit', 'market')),
    CONSTRAINT chk_trd_quantity CHECK (quantity > 0),
    CONSTRAINT chk_trd_price CHECK (price >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='매매등록 주문 저장';
