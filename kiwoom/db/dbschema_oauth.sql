-- =============================================================
-- oauth2 (OAuth2 인증) 모듈 DB 스키마
-- specs_response.py : OAUTH2_RESPONSE_SPECS
-- =============================================================

-- au10001: 액세스 토큰 발급 (au10001)
-- au10002: 액세스 토큰 폐기 (au10002)

-- =============================================================
-- Drop existing tables if they exist (for development/testing)
-- =============================================================
DROP TABLE IF EXISTS au10001 CASCADE;
DROP TABLE IF EXISTS au10002 CASCADE;

-- =============================================================
-- au10001 – 액세스 토큰 발급 (scalar)
-- =============================================================
-- API 요청 시점의 요청 파라미터, 응답 결과를 저장합니다.
-- 각 발급 시점에 1행씩 저장됩니다.
CREATE TABLE IF NOT EXISTS au10001 (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    grant_type      VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '요청 grant_type',
    req_appkey      VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '요청 appkey',
    expires_dt      VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '토큰 만료일 (응답)',
    token_type      VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '토큰 타입 (응답)',
    token           VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '액세스 토큰 (응답)',
    return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과 코드 (응답)',
    return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과 메시지 (응답)',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_return_code (return_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='액세스 토큰 발급';

-- =============================================================
-- au10002 – 액세스 토큰 폐기 (scalar)
-- =============================================================
-- API 요청 시점의 응답 결과를 저장합니다.
-- 각 폐기 시점에 1행씩 저장됩니다.
CREATE TABLE IF NOT EXISTS au10002 (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_appkey      VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '요청 appkey',
    req_token       VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '요청 token',
    return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과 코드 (응답)',
    return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과 메시지 (응답)',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_req_dt (fetched_at),
    INDEX idx_return_code (return_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='액세스 토큰 폐기';

-- =============================================================
-- 인덱스 설명
-- =============================================================
-- idx_req_dt: 시간 범위 조회 (예: 오늘 발급된 토큰 조회)
-- idx_return_code: 성공/실패 구분 (return_code = '0' 성공)
