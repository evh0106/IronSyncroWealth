-- =============================================================
-- oauth2 (OAuth2 인증) 모듈 DB 스키마
-- source: src/oauth2/specs_request.py, src/oauth2/specs_response.py
-- =============================================================

-- 구현 URL
-- /oauth2/tokenP   -> tokenP (액세스 토큰 발급)
-- /oauth2/revokeP  -> revokeP (액세스 토큰 폐기)
-- /oauth2/Approval -> Approval (웹소켓 승인키 발급)

-- =============================================================
-- Drop existing tables if they exist
-- =============================================================
DROP TABLE IF EXISTS tokenP CASCADE;
DROP TABLE IF EXISTS revokeP CASCADE;
DROP TABLE IF EXISTS Approval CASCADE;

-- =============================================================
-- tokenP - 액세스 토큰 발급 (/oauth2/tokenP)
-- =============================================================
CREATE TABLE IF NOT EXISTS tokenP (
    id                          BIGINT        NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id                       VARCHAR(32)   NOT NULL DEFAULT 'ka10001' COMMENT 'API ID',
    req_url                     VARCHAR(200)  NOT NULL DEFAULT '/oauth2/tokenP' COMMENT '요청 URL',
    req_grant_type              VARCHAR(50)   NOT NULL DEFAULT '' COMMENT '요청 grant_type',
    req_appkey                  VARCHAR(100)  NOT NULL DEFAULT '' COMMENT '요청 appkey',
    req_appsecret               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '요청 appsecret',
    access_token                VARCHAR(1200) NOT NULL DEFAULT '' COMMENT '응답 access_token',
    token_type                  VARCHAR(50)   NOT NULL DEFAULT '' COMMENT '응답 token_type',
    access_token_token_expired  VARCHAR(64)   NOT NULL DEFAULT '' COMMENT '응답 access_token_token_expired',
    fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='oauth2/tokenP';

-- =============================================================
-- revokeP - 액세스 토큰 폐기 (/oauth2/revokeP)
-- =============================================================
CREATE TABLE IF NOT EXISTS revokeP (
    id              BIGINT        NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id           VARCHAR(32)   NOT NULL DEFAULT 'ka10002' COMMENT 'API ID',
    req_url         VARCHAR(200)  NOT NULL DEFAULT '/oauth2/revokeP' COMMENT '요청 URL',
    req_appkey      VARCHAR(100)  NOT NULL DEFAULT '' COMMENT '요청 appkey',
    req_appsecret   VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '요청 appsecret',
    req_token       VARCHAR(1200) NOT NULL DEFAULT '' COMMENT '요청 token',
    code            VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '응답 code',
    message         VARCHAR(255)  NOT NULL DEFAULT '' COMMENT '응답 message',
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id),
    INDEX idx_code (code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='oauth2/revokeP';

-- =============================================================
-- Approval - 웹소켓 승인키 발급 (/oauth2/Approval)
-- =============================================================
CREATE TABLE IF NOT EXISTS Approval (
    id              BIGINT        NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tr_id           VARCHAR(32)   NOT NULL DEFAULT 'ka10003' COMMENT 'API ID',
    req_url         VARCHAR(200)  NOT NULL DEFAULT '/oauth2/Approval' COMMENT '요청 URL',
    req_grant_type  VARCHAR(50)   NOT NULL DEFAULT '' COMMENT '요청 grant_type',
    req_appkey      VARCHAR(100)  NOT NULL DEFAULT '' COMMENT '요청 appkey',
    req_secretkey   VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '요청 secretkey',
    approval_key    VARCHAR(300)  NOT NULL DEFAULT '' COMMENT '응답 approval_key',
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_tr_id (tr_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='oauth2/Approval';

-- =============================================================
-- 인덱스 설명
-- =============================================================
-- idx_req_dt: 시간 범위 조회
-- idx_tr_id: API ID 조건 조회
-- idx_code: revoke 결과 코드 조회
