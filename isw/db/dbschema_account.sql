-- =============================================================
-- ISW 계좌관리 스키마
-- 대상 화면: iswWeb /account-management
-- =============================================================

CREATE DATABASE IF NOT EXISTS isw_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_general_ci;

USE isw_db;

-- -------------------------------------------------------------
-- Drop existing table if it exists (for development/testing)
-- -------------------------------------------------------------
DROP TABLE IF EXISTS isw_acnt_account_register;

-- -------------------------------------------------------------
-- 등록계좌 테이블 (account-management 등록계좌 표)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_acnt_account_register (
    account_id                   BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '등록계좌 ID',
    broker                       VARCHAR(20)     NOT NULL DEFAULT 'kis' COMMENT '브로커 구분(kis/kiwoom/isw)',
    account_no                   VARCHAR(40)     NOT NULL DEFAULT '' COMMENT '계좌번호',
    account_name                 VARCHAR(120)    NOT NULL DEFAULT '' COMMENT '계좌명',
    connection_status            VARCHAR(20)     NOT NULL DEFAULT 'disconnected' COMMENT '연결상태(connected/disconnected/check-required)',
    is_default                   CHAR(1)         NOT NULL DEFAULT 'N' COMMENT '기본계좌 여부(Y/N)',

    api_key_ref                  VARCHAR(200)    NOT NULL DEFAULT '' COMMENT 'API 키 참조값(선택)',
    api_secret_ref               VARCHAR(200)    NOT NULL DEFAULT '' COMMENT 'API 시크릿 참조값(선택)',

    last_connected_at            DATETIME        NULL COMMENT '최근 연결시각',
    note                         VARCHAR(500)    NOT NULL DEFAULT '' COMMENT '비고',
    created_at                   DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '등록일시',
    updated_at                   DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',

    PRIMARY KEY (account_id),
    UNIQUE KEY uq_acnt_broker_account_no (broker, account_no),
    INDEX idx_acnt_status (connection_status),
    INDEX idx_acnt_default (is_default),

    CONSTRAINT chk_acnt_connection_status CHECK (connection_status IN ('connected', 'disconnected', 'check-required')),
    CONSTRAINT chk_acnt_is_default CHECK (is_default IN ('Y', 'N'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='계좌관리 등록계좌 저장';
