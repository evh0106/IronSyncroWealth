-- =============================================================
-- ISW 시장별 종목 마스터 DB 스키마
-- 참고: isw/docs/stocks_info/*code.py
-- =============================================================

-- -------------------------------------------------------------
-- Drop existing tables if they exist (for development/testing purposes)
-- -------------------------------------------------------------
DROP TABLE IF EXISTS isw_mst_kospi CASCADE;
DROP TABLE IF EXISTS isw_mst_kosdaq CASCADE;
DROP TABLE IF EXISTS isw_mst_konex CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_elw CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_index_future CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_stock_future CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_cme_future CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_commodity_future CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_eurex_option CASCADE;
DROP TABLE IF EXISTS isw_mst_domestic_bond CASCADE;
DROP TABLE IF EXISTS isw_mst_overseas_stock CASCADE;
DROP TABLE IF EXISTS isw_mst_overseas_index CASCADE;
DROP TABLE IF EXISTS isw_mst_overseas_future CASCADE;

-- -------------------------------------------------------------
-- KOSPI 종목 마스터 (kis_kospi_code_mst.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_kospi (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글명',
	group_code                  VARCHAR(2)    NOT NULL DEFAULT '' COMMENT '그룹코드',
	market_cap_size_code        VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '시가총액규모',
	index_sector_large          VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '지수업종대분류',
	index_sector_mid            VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '지수업종중분류',
	index_sector_small          VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '지수업종소분류',
	base_price                  DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '기준가',
	regular_lot_size            INT           NOT NULL DEFAULT 0 COMMENT '매매수량단위',
	offhour_lot_size            INT           NOT NULL DEFAULT 0 COMMENT '시간외수량단위',
	trade_halt_yn               CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '거래정지',
	managed_issue_yn            CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '관리종목',
	market_warning_code         VARCHAR(2)    NOT NULL DEFAULT '' COMMENT '시장경고',
	margin_rate                 DECIMAL(7,4)  NOT NULL DEFAULT 0 COMMENT '증거금비율',
	prev_volume                 BIGINT        NOT NULL DEFAULT 0 COMMENT '전일거래량',
	par_value                   DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '액면가',
	listing_date                VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '상장일자',
	listed_shares_thousand      BIGINT        NOT NULL DEFAULT 0 COMMENT '상장주수(천)',
	roe                         DECIMAL(9,4)  NOT NULL DEFAULT 0 COMMENT 'ROE',
	base_yyyymm                 VARCHAR(6)    NOT NULL DEFAULT '' COMMENT '기준년월',
	prev_market_cap_100m        BIGINT        NOT NULL DEFAULT 0 COMMENT '전일기준 시가총액(억)',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_kospi_short_code (short_code),
	UNIQUE KEY uq_kospi_standard_code (standard_code),
	INDEX idx_kospi_name (stock_name_kr),
	INDEX idx_kospi_listing_date (listing_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='KOSPI 종목 마스터';

-- -------------------------------------------------------------
-- KOSDAQ 종목 마스터 (kis_kosdaq_code_mst.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_kosdaq (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	security_group_code         VARCHAR(2)    NOT NULL DEFAULT '' COMMENT '증권그룹구분코드',
	market_cap_size_code        VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '시가총액 규모 구분 코드 유가',
	index_sector_large          VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '지수업종 대분류 코드',
	index_sector_mid            VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '지수 업종 중분류 코드',
	index_sector_small          VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '지수업종 소분류 코드',
	venture_yn                  CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '벤처기업 여부',
	kosdaq150_yn                CHAR(1)       NOT NULL DEFAULT 'N' COMMENT 'KOSDAQ150지수여부',
	base_price                  DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '주식 기준가',
	regular_lot_size            INT           NOT NULL DEFAULT 0 COMMENT '정규 시장 매매 수량 단위',
	offhour_lot_size            INT           NOT NULL DEFAULT 0 COMMENT '시간외 시장 매매 수량 단위',
	trade_halt_yn               CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '거래정지 여부',
	managed_issue_yn            CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '관리 종목 여부',
	market_warning_code         VARCHAR(2)    NOT NULL DEFAULT '' COMMENT '시장 경고 구분 코드',
	margin_rate                 DECIMAL(7,4)  NOT NULL DEFAULT 0 COMMENT '증거금 비율',
	listing_date                VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '주식 상장 일자',
	listed_shares_thousand      BIGINT        NOT NULL DEFAULT 0 COMMENT '상장 주수(천)',
	roe                         DECIMAL(9,4)  NOT NULL DEFAULT 0 COMMENT 'ROE(자기자본이익률)',
	base_yyyymm                 VARCHAR(6)    NOT NULL DEFAULT '' COMMENT '기준년월',
	prev_market_cap_100m        BIGINT        NOT NULL DEFAULT 0 COMMENT '전일기준 시가총액 (억)',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_kosdaq_short_code (short_code),
	UNIQUE KEY uq_kosdaq_standard_code (standard_code),
	INDEX idx_kosdaq_name (stock_name_kr),
	INDEX idx_kosdaq_listing_date (listing_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='KOSDAQ 종목 마스터';

-- -------------------------------------------------------------
-- KONEX 종목 마스터 (kis_konex_code_mst.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_konex (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '종목명',
	security_group_code         VARCHAR(2)    NOT NULL DEFAULT '' COMMENT '증권그룹구분코드',
	base_price                  DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '주식 기준가',
	regular_lot_size            INT           NOT NULL DEFAULT 0 COMMENT '정규 시장 매매 수량 단위',
	offhour_lot_size            INT           NOT NULL DEFAULT 0 COMMENT '시간외 시장 매매 수량 단위',
	trade_halt_yn               CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '거래정지 여부',
	managed_issue_yn            CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '관리 종목 여부',
	market_warning_code         VARCHAR(2)    NOT NULL DEFAULT '' COMMENT '시장 경고 구분 코드',
	margin_rate                 DECIMAL(7,4)  NOT NULL DEFAULT 0 COMMENT '증거금 비율',
	listing_date                VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '주식 상장 일자',
	listed_shares_thousand      BIGINT        NOT NULL DEFAULT 0 COMMENT '상장 주수(천)',
	roe                         DECIMAL(9,4)  NOT NULL DEFAULT 0 COMMENT 'ROE',
	base_yyyymm                 VARCHAR(6)    NOT NULL DEFAULT '' COMMENT '기준년월',
	prev_market_cap_100m        BIGINT        NOT NULL DEFAULT 0 COMMENT '전일기준 시가총액(억)',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_konex_short_code (short_code),
	UNIQUE KEY uq_konex_standard_code (standard_code),
	INDEX idx_konex_name (stock_name_kr),
	INDEX idx_konex_listing_date (listing_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='KONEX 종목 마스터';

-- -------------------------------------------------------------
-- 국내 ELW 종목 마스터 (domestic_elw_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_elw (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	elw_right_type              VARCHAR(1)    NOT NULL DEFAULT '' COMMENT 'ELW권리형태',
	knockout_barrier_price      DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT 'ELW조기종료발생기준가격',
	basket_yn                   CHAR(1)       NOT NULL DEFAULT 'N' COMMENT '바스켓 여부',
	underlying_code1            VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산코드1',
	underlying_code2            VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산코드2',
	underlying_code3            VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산코드3',
	underlying_code4            VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산코드4',
	underlying_code5            VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산코드5',
	issuer_name_kr              VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '발행사 한글 종목명',
	issuer_code                 VARCHAR(5)    NOT NULL DEFAULT '' COMMENT '발행사코드',
	strike_price                DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '행사가',
	last_trading_date           VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '최종거래일',
	remain_days                 INT           NOT NULL DEFAULT 0 COMMENT '잔존 일수',
	right_type_code             VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '권리 유형 구분 코드',
	payment_date                VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '지급일',
	prev_market_cap_100m        BIGINT        NOT NULL DEFAULT 0 COMMENT '전일시가총액(억)',
	listed_shares_thousand      BIGINT        NOT NULL DEFAULT 0 COMMENT '상장주수(천)',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_elw_short_code (short_code),
	UNIQUE KEY uq_domestic_elw_standard_code (standard_code),
	INDEX idx_domestic_elw_name (stock_name_kr),
	INDEX idx_domestic_elw_last_trading_date (last_trading_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국내 ELW 종목 마스터';

-- -------------------------------------------------------------
-- 국내 지수선물옵션 종목 마스터 (domestic_index_future_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_index_future (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	product_type                VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '상품종류',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	atm_flag                    VARCHAR(1)    NOT NULL DEFAULT '' COMMENT 'ATM구분',
	strike_price                DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '행사가',
	month_code                  VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '월물구분코드',
	underlying_short_code       VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산 단축코드',
	underlying_name             VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '기초자산 명',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_index_future_short_code (short_code),
	UNIQUE KEY uq_domestic_index_future_standard_code (standard_code),
	INDEX idx_domestic_index_future_name (stock_name_kr),
	INDEX idx_domestic_index_future_underlying (underlying_short_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국내 지수선물옵션 종목 마스터';

-- -------------------------------------------------------------
-- 국내 주식선물옵션 종목 마스터 (domestic_stock_future_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_stock_future (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	product_type                VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '상품종류',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	atm_flag                    VARCHAR(1)    NOT NULL DEFAULT '' COMMENT 'ATM구분',
	strike_price                DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '행사가',
	month_code                  VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '월물구분코드',
	underlying_short_code       VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산 단축코드',
	underlying_name             VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '기초자산 명',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_stock_future_short_code (short_code),
	UNIQUE KEY uq_domestic_stock_future_standard_code (standard_code),
	INDEX idx_domestic_stock_future_name (stock_name_kr),
	INDEX idx_domestic_stock_future_underlying (underlying_short_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국내 주식선물옵션 종목 마스터';

-- -------------------------------------------------------------
-- 국내 CME 연계 야간선물 종목 마스터 (domestic_cme_future_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_cme_future (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	product_type                VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '상품종류',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	strike_price                DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '행사가',
	underlying_short_code       VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '기초자산 단축코드',
	underlying_name             VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '기초자산 명',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_cme_future_short_code (short_code),
	UNIQUE KEY uq_domestic_cme_future_standard_code (standard_code),
	INDEX idx_domestic_cme_future_name (stock_name_kr),
	INDEX idx_domestic_cme_future_underlying (underlying_short_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국내 CME 연계 야간선물 종목 마스터';

-- -------------------------------------------------------------
-- 국내 상품선물옵션 종목 마스터 (domestic_commodity_future_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_commodity_future (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	product_group               VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '상품구분',
	product_type                VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '상품종류',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	month_code                  VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '월물구분코드',
	underlying_short_code       VARCHAR(3)    NOT NULL DEFAULT '' COMMENT '기초자산 단축코드',
	underlying_name             VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '기초자산 명',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_commodity_future_short_code (short_code),
	UNIQUE KEY uq_domestic_commodity_future_standard_code (standard_code),
	INDEX idx_domestic_commodity_future_name (stock_name_kr)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국내 상품선물옵션 종목 마스터';

-- -------------------------------------------------------------
-- 국내 EUREX 연계 야간옵션 종목 마스터 (domestic_eurex_option_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_eurex_option (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	product_type                VARCHAR(1)    NOT NULL DEFAULT '' COMMENT '상품종류',
	short_code                  VARCHAR(9)    NOT NULL DEFAULT '' COMMENT '단축코드',
	standard_code               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '표준코드',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '한글종목명',
	atm_flag                    VARCHAR(1)    NOT NULL DEFAULT '' COMMENT 'ATM구분',
	strike_price                DECIMAL(18,4) NOT NULL DEFAULT 0 COMMENT '행사가',
	underlying_short_code       VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기초자산 단축코드',
	underlying_name             VARCHAR(200)  NOT NULL DEFAULT '' COMMENT '기초자산 명',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_eurex_option_short_code (short_code),
	UNIQUE KEY uq_domestic_eurex_option_standard_code (standard_code),
	INDEX idx_domestic_eurex_option_name (stock_name_kr)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='국내 EUREX 연계 야간옵션 종목 마스터';

-- -------------------------------------------------------------
-- 장내채권 종목 마스터 (domestic_bond_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_domestic_bond (
	base_date                   VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '단축코드',
	bond_type                   VARCHAR(2)   NOT NULL DEFAULT '' COMMENT '유형',
	bond_class_code             VARCHAR(2)   NOT NULL DEFAULT '' COMMENT '채권분류코드',
	standard_code               VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '표준코드',
	bond_name                   VARCHAR(200) NOT NULL DEFAULT '' COMMENT '종목명',
	bond_interest_class_code    VARCHAR(2)   NOT NULL DEFAULT '' COMMENT '채권이자분류코드',
	listing_date                VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '상장일',
	issue_date                  VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '발행일',
	redemption_date             VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '상환일',
	fetched_at                  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_domestic_bond_standard_code (standard_code),
	INDEX idx_domestic_bond_name (bond_name),
	INDEX idx_domestic_bond_redemption_date (redemption_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='장내채권 종목 마스터';

-- -------------------------------------------------------------
-- 해외주식 종목 마스터 (overseas_stock_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_overseas_stock (
	base_date                   VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(32)   NOT NULL DEFAULT '' COMMENT '단축코드',
	national_code               VARCHAR(8)    NOT NULL DEFAULT '' COMMENT 'National code',
	exchange_id                 VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'Exchange id',
	exchange_code               VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'Exchange code',
	exchange_name               VARCHAR(100)  NOT NULL DEFAULT '' COMMENT 'Exchange name',
	symbol                      VARCHAR(32)   NOT NULL DEFAULT '' COMMENT 'Symbol',
	realtime_symbol             VARCHAR(32)   NOT NULL DEFAULT '' COMMENT 'realtime symbol',
	stock_name_kr               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT 'Korea name',
	stock_name_en               VARCHAR(200)  NOT NULL DEFAULT '' COMMENT 'English name',
	security_type               VARCHAR(4)    NOT NULL DEFAULT '' COMMENT 'Security type',
	currency                    VARCHAR(12)   NOT NULL DEFAULT '' COMMENT 'currency',
	base_price                  DECIMAL(18,6) NOT NULL DEFAULT 0 COMMENT 'base price',
	bid_order_size              DECIMAL(20,6) NOT NULL DEFAULT 0 COMMENT 'Bid order size',
	ask_order_size              DECIMAL(20,6) NOT NULL DEFAULT 0 COMMENT 'Ask order size',
	market_start_hhmm           VARCHAR(4)    NOT NULL DEFAULT '' COMMENT 'market start time(HHMM)',
	market_end_hhmm             VARCHAR(4)    NOT NULL DEFAULT '' COMMENT 'market end time(HHMM)',
	dr_yn                       CHAR(1)       NOT NULL DEFAULT 'N' COMMENT 'DR 여부(Y/N)',
	dr_national_code            VARCHAR(8)    NOT NULL DEFAULT '' COMMENT 'DR 국가코드',
	industry_code               VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '업종분류코드',
	index_component_yn          CHAR(1)       NOT NULL DEFAULT '0' COMMENT '지수구성종목 존재 여부',
	tick_size_type              VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'Tick size Type',
	etp_category_code           VARCHAR(3)    NOT NULL DEFAULT '' COMMENT '구분코드',
	fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_overseas_stock_symbol (exchange_code, symbol),
	INDEX idx_overseas_stock_name_kr (stock_name_kr),
	INDEX idx_overseas_stock_name_en (stock_name_en),
	INDEX idx_overseas_stock_national_code (national_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='해외주식 종목 마스터';

-- -------------------------------------------------------------
-- 해외주식지수 종목 마스터 (overseas_index_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_overseas_index (
	base_date                   VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '단축코드',
	category_code               VARCHAR(1)   NOT NULL DEFAULT '' COMMENT '구분코드',
	symbol                      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '심볼',
	stock_name_en               VARCHAR(200) NOT NULL DEFAULT '' COMMENT '영문명',
	stock_name_kr               VARCHAR(200) NOT NULL DEFAULT '' COMMENT '한글명',
	issue_industry_code         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '종목업종코드',
	dow30_component_yn          CHAR(1)      NOT NULL DEFAULT '0' COMMENT '다우30 편입종목여부',
	nasdaq100_component_yn      CHAR(1)      NOT NULL DEFAULT '0' COMMENT '나스닥100 편입종목여부',
	sp500_component_yn          CHAR(1)      NOT NULL DEFAULT '0' COMMENT 'S&P 500 편입종목여부',
	exchange_code               VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '거래소코드',
	national_code               VARCHAR(3)   NOT NULL DEFAULT '' COMMENT '국가구분코드',
	fetched_at                  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_overseas_index_symbol (symbol),
	INDEX idx_overseas_index_name_kr (stock_name_kr),
	INDEX idx_overseas_index_exchange (exchange_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='해외주식지수 종목 마스터';

-- -------------------------------------------------------------
-- 해외선물옵션 종목 마스터 (overseas_future_code.py)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS isw_mst_overseas_future (
	base_date                   VARCHAR(8)     NOT NULL DEFAULT '' COMMENT '기준일자(YYYYMMDD)',
	short_code                  VARCHAR(32)    NOT NULL DEFAULT '' COMMENT '단축코드',
	instrument_code             VARCHAR(32)    NOT NULL DEFAULT '' COMMENT '종목코드',
	auto_orderable_yn           CHAR(1)        NOT NULL DEFAULT 'N' COMMENT '서버자동주문 가능 종목 여부',
	auto_twap_orderable_yn      CHAR(1)        NOT NULL DEFAULT 'N' COMMENT '서버자동주문 TWAP 가능 종목 여부',
	auto_macro_orderable_yn     CHAR(1)        NOT NULL DEFAULT 'N' COMMENT '서버자동 경제지표 주문 가능 종목 여부',
	instrument_name_kr          VARCHAR(200)   NOT NULL DEFAULT '' COMMENT '종목한글명',
	exchange_code               VARCHAR(10)    NOT NULL DEFAULT '' COMMENT '거래소코드',
	item_code                   VARCHAR(10)    NOT NULL DEFAULT '' COMMENT '품목코드',
	item_type                   VARCHAR(3)     NOT NULL DEFAULT '' COMMENT '품목종류',
	output_decimals             INT            NOT NULL DEFAULT 0 COMMENT '출력 소수점',
	calc_decimals               INT            NOT NULL DEFAULT 0 COMMENT '계산 소수점',
	tick_size                   DECIMAL(20,8)  NOT NULL DEFAULT 0 COMMENT '틱사이즈',
	tick_value                  DECIMAL(20,8)  NOT NULL DEFAULT 0 COMMENT '틱가치',
	contract_size               DECIMAL(20,8)  NOT NULL DEFAULT 0 COMMENT '계약크기',
	price_radix                 VARCHAR(4)     NOT NULL DEFAULT '' COMMENT '가격표시진법',
	conversion_multiplier       DECIMAL(20,8)  NOT NULL DEFAULT 0 COMMENT '환산승수',
	front_month_yn              CHAR(1)        NOT NULL DEFAULT '0' COMMENT '최다월물여부',
	near_month_yn               CHAR(1)        NOT NULL DEFAULT '0' COMMENT '최근월물여부',
	spread_yn                   CHAR(1)        NOT NULL DEFAULT 'N' COMMENT '스프레드여부',
	spread_leg1_yn              CHAR(1)        NOT NULL DEFAULT 'N' COMMENT '스프레드기준종목 LEG1 여부',
	sub_exchange_code           VARCHAR(3)     NOT NULL DEFAULT '' COMMENT '서브 거래소 코드',
	fetched_at                  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
	PRIMARY KEY (base_date, short_code),
	UNIQUE KEY uq_overseas_future_instrument_code (instrument_code),
	INDEX idx_overseas_future_name_kr (instrument_name_kr),
	INDEX idx_overseas_future_exchange_item (exchange_code, item_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='해외선물옵션 종목 마스터';
