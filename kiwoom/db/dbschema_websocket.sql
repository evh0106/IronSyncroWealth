-- ============================================================
-- Kiwoom WebSocket API 실시간 데이터 저장 스키마
-- wss://openapi.koreainvestment.com:9443/websocket
-- specs_request.py  : WEBSOCKET_API_SPECS
-- specs_response.py : WEBSOCKET_RESPONSE_SPECS
-- ============================================================

-- 공통 패턴:
--   req_dt           VARCHAR(14)  수신 일시 (YYYYMMDDHHmmss)
--   req_type         VARCHAR(8)   실시간 항목 코드 (0A, 0B ...)
--   req_item         VARCHAR(40)  실시간 등록 종목코드
--   rsp_return_code  VARCHAR(10)  결과코드
--   rsp_return_msg   VARCHAR(200) 결과메시지
--   rsp_f{FID}       VARCHAR(40)  FID 값 컬럼
--   fetched_at       DATETIME     수신일시

-- ------------------------------------------------------------
-- Drop existing tables
-- ------------------------------------------------------------
DROP TABLE IF EXISTS ws_00_ord_ccls CASCADE;
DROP TABLE IF EXISTS ws_04_balance CASCADE;
DROP TABLE IF EXISTS ws_0a_stk_kse CASCADE;
DROP TABLE IF EXISTS ws_0b_stk_ccls CASCADE;
DROP TABLE IF EXISTS ws_0c_stk_prio_hga CASCADE;
DROP TABLE IF EXISTS ws_0d_stk_hga_qty CASCADE;
DROP TABLE IF EXISTS ws_0e_stk_ah_hga CASCADE;
DROP TABLE IF EXISTS ws_0f_stk_dly_trd CASCADE;
DROP TABLE IF EXISTS ws_0g_etf_nav CASCADE;
DROP TABLE IF EXISTS ws_0h_stk_exp_ccls CASCADE;
DROP TABLE IF EXISTS ws_0i_intl_gold_prc CASCADE;
DROP TABLE IF EXISTS ws_0j_sect_idx CASCADE;
DROP TABLE IF EXISTS ws_0u_sect_flct CASCADE;
DROP TABLE IF EXISTS ws_0g_stk_nfo CASCADE;
DROP TABLE IF EXISTS ws_0m_elw_thr CASCADE;
DROP TABLE IF EXISTS ws_0s_mkt_tm CASCADE;
DROP TABLE IF EXISTS ws_0u_elw_idx CASCADE;
DROP TABLE IF EXISTS ws_0w_stk_prg_trd CASCADE;
DROP TABLE IF EXISTS ws_ka10171_cndsr_lst CASCADE;
DROP TABLE IF EXISTS ws_ka10172_cndsr_req CASCADE;
DROP TABLE IF EXISTS ws_ka10173_cndsr_rt CASCADE;
DROP TABLE IF EXISTS ws_ka10174_cndsr_clr CASCADE;

-- ------------------------------------------------------------
-- ws_00_ord_ccls : 주문체결 (api_id: 00)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_00_ord_ccls (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (00)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f9201           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '계좌번호',
    rsp_f9203           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '주문번호',
    rsp_f9205           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '관리자사번',
    rsp_f9001           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드,업종코드',
    rsp_f912            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '주문업무분류',
    rsp_f913            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '주문상태',
    rsp_f302            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '종목명',
    rsp_f900            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '주문수량',
    rsp_f901            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '주문가격',
    rsp_f902            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '미체결수량',
    rsp_f903            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결누계금액',
    rsp_f904            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '원주문번호',
    rsp_f905            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '주문구분',
    rsp_f906            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매매구분',
    rsp_f907            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '매도수구분',
    rsp_f908            VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '주문/체결시간',
    rsp_f909            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결번호',
    rsp_f910            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결가',
    rsp_f911            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결량',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f27             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매도호가',
    rsp_f28             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매수호가',
    rsp_f914            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '단위체결가',
    rsp_f915            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '단위체결량',
    rsp_f938            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일매매수수료',
    rsp_f939            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일매매세금',
    rsp_f919            VARCHAR(100) NOT NULL DEFAULT '' COMMENT '거부사유',
    rsp_f920            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '화면번호',
    rsp_f921            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '터미널번호',
    rsp_f922            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '신용구분',
    rsp_f923            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '대출일',
    rsp_f10010          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시간외단일가_현재가',
    rsp_f2134           VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '거래소구분',
    rsp_f2135           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래소구분명',
    rsp_f2136           VARCHAR(4)   NOT NULL DEFAULT '' COMMENT 'SOR여부',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt),
    INDEX idx_acnt (rsp_f9201),
    INDEX idx_ord_no (rsp_f9203)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_00 주문체결 실시간';

-- ------------------------------------------------------------
-- ws_04_balance : 잔고 (api_id: 04)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_04_balance (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (04)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f9201           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '계좌번호',
    rsp_f9001           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드,업종코드',
    rsp_f917            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '신용구분',
    rsp_f916            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '대출일',
    rsp_f302            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '종목명',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f930            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '보유수량',
    rsp_f931            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매입단가',
    rsp_f932            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '총매입가(당일누적)',
    rsp_f933            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '주문가능수량',
    rsp_f945            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일순매수량',
    rsp_f946            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도/매수구분',
    rsp_f950            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일총매도손익',
    rsp_f951            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'Extra Item',
    rsp_f27             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매도호가',
    rsp_f28             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매수호가',
    rsp_f307            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기준가',
    rsp_f8019           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '손익률(실현손익)',
    rsp_f957            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '신용금액',
    rsp_f958            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '신용이자',
    rsp_f918            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '만기일',
    rsp_f990            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일실현손익(유가)',
    rsp_f991            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일실현손익율(유가)',
    rsp_f992            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일실현손익(신용)',
    rsp_f993            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일실현손익율(신용)',
    rsp_f959            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '담보대출수량',
    rsp_f924            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'Extra Item',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt),
    INDEX idx_acnt (rsp_f9201)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_04 잔고 실시간';

-- ------------------------------------------------------------
-- ws_0a_stk_kse : 주식기세 (api_id: 0A)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0a_stk_kse (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0A)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f27             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매도호가',
    rsp_f28             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매수호가',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f14             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    rsp_f16             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    rsp_f17             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    rsp_f18             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f26             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비(계약,주)',
    rsp_f29             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래대금증감',
    rsp_f30             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비(비율)',
    rsp_f31             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래회전율',
    rsp_f32             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래비용',
    rsp_f311            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가총액(억)',
    rsp_f567            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '상한가발생시간',
    rsp_f568            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '하한가발생시간',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0A 주식기세 실시간';

-- ------------------------------------------------------------
-- ws_0b_stk_ccls : 주식체결 (api_id: 0B)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0b_stk_ccls (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0B)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f27             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매도호가',
    rsp_f28             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매수호가',
    rsp_f15             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래량',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f14             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    rsp_f16             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    rsp_f17             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    rsp_f18             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f26             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비(계약,주)',
    rsp_f29             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래대금증감',
    rsp_f30             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비(비율)',
    rsp_f31             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래회전율',
    rsp_f32             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래비용',
    rsp_f228            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결강도',
    rsp_f311            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가총액(억)',
    rsp_f290            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '장구분',
    rsp_f691            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'K.O 접근도',
    rsp_f567            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '상한가발생시간',
    rsp_f568            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '하한가발생시간',
    rsp_f851            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일 동시간 거래량 비율',
    rsp_f1890           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시가시간',
    rsp_f1891           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '고가시간',
    rsp_f1892           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '저가시간',
    rsp_f1030           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도체결량',
    rsp_f1031           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수체결량',
    rsp_f1032           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수비율',
    rsp_f1071           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도체결건수',
    rsp_f1072           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수체결건수',
    rsp_f1313           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순간거래대금',
    rsp_f1315           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도체결량_단건',
    rsp_f1316           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수체결량_단건',
    rsp_f1314           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수체결량',
    rsp_f1497           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'CFD증거금',
    rsp_f1498           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '유지증거금',
    rsp_f620            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일거래평균가',
    rsp_f732            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'CFD거래비용',
    rsp_f852            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '대주거래비용',
    rsp_f9081           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래소구분',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt),
    INDEX idx_dt (req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0B 주식체결 실시간';

-- ------------------------------------------------------------
-- ws_0c_stk_prio_hga : 주식우선호가 (api_id: 0C)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0c_stk_prio_hga (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0C)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f27             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매도호가',
    rsp_f28             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '(최우선)매수호가',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0C 주식우선호가 실시간';

-- ------------------------------------------------------------
-- ws_0d_stk_hga_qty : 주식호가잔량 (api_id: 0D)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0d_stk_hga_qty (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0D)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f21             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '호가시간',
    rsp_f41             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가1',
    rsp_f61             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량1',
    rsp_f81             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비1',
    rsp_f51             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가1',
    rsp_f71             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량1',
    rsp_f91             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비1',
    rsp_f42             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가2',
    rsp_f62             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량2',
    rsp_f82             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비2',
    rsp_f52             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가2',
    rsp_f72             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량2',
    rsp_f92             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비2',
    rsp_f43             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가3',
    rsp_f63             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량3',
    rsp_f83             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비3',
    rsp_f53             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가3',
    rsp_f73             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량3',
    rsp_f93             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비3',
    rsp_f44             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가4',
    rsp_f64             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량4',
    rsp_f84             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비4',
    rsp_f54             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가4',
    rsp_f74             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량4',
    rsp_f94             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비4',
    rsp_f45             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가5',
    rsp_f65             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량5',
    rsp_f85             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비5',
    rsp_f55             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가5',
    rsp_f75             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량5',
    rsp_f95             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비5',
    rsp_f46             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가6',
    rsp_f66             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량6',
    rsp_f86             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비6',
    rsp_f56             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가6',
    rsp_f76             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량6',
    rsp_f96             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비6',
    rsp_f47             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가7',
    rsp_f67             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량7',
    rsp_f87             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비7',
    rsp_f57             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가7',
    rsp_f77             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량7',
    rsp_f97             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비7',
    rsp_f48             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가8',
    rsp_f68             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량8',
    rsp_f88             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비8',
    rsp_f58             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가8',
    rsp_f78             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량8',
    rsp_f98             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비8',
    rsp_f49             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가9',
    rsp_f69             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량9',
    rsp_f89             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비9',
    rsp_f59             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가9',
    rsp_f79             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량9',
    rsp_f99             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비9',
    rsp_f50             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가10',
    rsp_f70             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가수량10',
    rsp_f90             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가직전대비10',
    rsp_f60             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가10',
    rsp_f80             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가수량10',
    rsp_f100            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가직전대비10',
    rsp_f121            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가총잔량',
    rsp_f122            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가총잔량직전대비',
    rsp_f125            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가총잔량',
    rsp_f126            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가총잔량직전대비',
    rsp_f23             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가',
    rsp_f24             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결수량',
    rsp_f128            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수잔량',
    rsp_f129            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수비율',
    rsp_f138            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매도잔량',
    rsp_f139            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도비율',
    rsp_f200            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가전일종가대비',
    rsp_f201            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가전일종가대비등락율',
    rsp_f238            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '예상체결가전일종가대비기호',
    rsp_f291            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가2',
    rsp_f292            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결량',
    rsp_f293            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '예상체결가전일대비기호',
    rsp_f294            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가전일대비',
    rsp_f295            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가전일대비등락율',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f299            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비예상체결율',
    rsp_f215            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '장운영구분',
    rsp_f216            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '투자자별ticker',
    rsp_f621            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량1',
    rsp_f631            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량1',
    rsp_f622            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량2',
    rsp_f632            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량2',
    rsp_f623            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량3',
    rsp_f633            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량3',
    rsp_f624            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량4',
    rsp_f634            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량4',
    rsp_f625            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량5',
    rsp_f635            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량5',
    rsp_f626            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량6',
    rsp_f636            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량6',
    rsp_f627            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량7',
    rsp_f637            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량7',
    rsp_f628            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량8',
    rsp_f638            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량8',
    rsp_f629            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량9',
    rsp_f639            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량9',
    rsp_f630            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매도호가수량10',
    rsp_f640            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP매수호가수량10',
    rsp_f6044           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량1',
    rsp_f6045           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량2',
    rsp_f6046           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량3',
    rsp_f6047           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량4',
    rsp_f6048           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량5',
    rsp_f6049           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량6',
    rsp_f6050           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량7',
    rsp_f6051           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량8',
    rsp_f6052           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량9',
    rsp_f6053           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가잔량10',
    rsp_f6054           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량1',
    rsp_f6055           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량2',
    rsp_f6056           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량3',
    rsp_f6057           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량4',
    rsp_f6058           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량5',
    rsp_f6059           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량6',
    rsp_f6060           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량7',
    rsp_f6061           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량8',
    rsp_f6062           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량9',
    rsp_f6063           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가잔량10',
    rsp_f6064           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매도호가총잔량',
    rsp_f6065           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 매수호가총잔량',
    rsp_f6066           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량1',
    rsp_f6067           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량2',
    rsp_f6068           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량3',
    rsp_f6069           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량4',
    rsp_f6070           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량5',
    rsp_f6071           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량6',
    rsp_f6072           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량7',
    rsp_f6073           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량8',
    rsp_f6074           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량9',
    rsp_f6075           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가잔량10',
    rsp_f6076           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량1',
    rsp_f6077           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량2',
    rsp_f6078           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량3',
    rsp_f6079           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량4',
    rsp_f6080           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량5',
    rsp_f6081           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량6',
    rsp_f6082           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량7',
    rsp_f6083           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량8',
    rsp_f6084           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량9',
    rsp_f6085           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가잔량10',
    rsp_f6086           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매도호가총잔량',
    rsp_f6087           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT 매수호가총잔량',
    rsp_f6100           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 중간가 매도 총잔량 증감',
    rsp_f6101           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 중간가 매도 총잔량',
    rsp_f6102           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 중간가',
    rsp_f6103           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 중간가 매수 총잔량',
    rsp_f6104           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX 중간가 매수 총잔량 증감',
    rsp_f6105           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가 매도 총잔량 증감',
    rsp_f6106           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가 매도 총잔량',
    rsp_f6107           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가',
    rsp_f6108           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가 매수 총잔량',
    rsp_f6109           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가 매수 총잔량 증감',
    rsp_f6110           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX중간가대비',
    rsp_f6111           VARCHAR(4)   NOT NULL DEFAULT '' COMMENT 'KRX중간가대비 기호',
    rsp_f6112           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'KRX중간가대비등락율',
    rsp_f6113           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가대비',
    rsp_f6114           VARCHAR(4)   NOT NULL DEFAULT '' COMMENT 'NXT중간가대비 기호',
    rsp_f6115           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NXT중간가대비등락율',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0D 주식호가잔량 실시간';

-- ------------------------------------------------------------
-- ws_0e_stk_ah_hga : 주식시간외호가 (api_id: 0E)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0e_stk_ah_hga (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0E)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f21             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '호가시간',
    rsp_f131            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시간외매도호가총잔량',
    rsp_f132            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시간외매도호가총잔량직전대비',
    rsp_f135            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시간외매수호가총잔량',
    rsp_f136            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시간외매수호가총잔량직전대비',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0E 주식시간외호가 실시간';

-- ------------------------------------------------------------
-- ws_0f_stk_dly_trd : 주식당일거래원 (api_id: 0F)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0f_stk_dly_trd (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0F)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f141            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매도거래원1',
    rsp_f161            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원수량1',
    rsp_f166            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원별증감1',
    rsp_f146            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원코드1',
    rsp_f271            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원색깔1',
    rsp_f151            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매수거래원1',
    rsp_f171            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원수량1',
    rsp_f176            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원별증감1',
    rsp_f156            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원코드1',
    rsp_f281            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원색깔1',
    rsp_f142            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매도거래원2',
    rsp_f162            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원수량2',
    rsp_f167            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원별증감2',
    rsp_f147            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원코드2',
    rsp_f272            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원색깔2',
    rsp_f152            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매수거래원2',
    rsp_f172            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원수량2',
    rsp_f177            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원별증감2',
    rsp_f157            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원코드2',
    rsp_f282            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원색깔2',
    rsp_f143            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매도거래원3',
    rsp_f163            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원수량3',
    rsp_f168            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원별증감3',
    rsp_f148            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원코드3',
    rsp_f273            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원색깔3',
    rsp_f153            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매수거래원3',
    rsp_f173            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원수량3',
    rsp_f178            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원별증감3',
    rsp_f158            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원코드3',
    rsp_f283            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원색깔3',
    rsp_f144            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매도거래원4',
    rsp_f164            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원수량4',
    rsp_f169            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원별증감4',
    rsp_f149            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원코드4',
    rsp_f274            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원색깔4',
    rsp_f154            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매수거래원4',
    rsp_f174            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원수량4',
    rsp_f179            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원별증감4',
    rsp_f159            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원코드4',
    rsp_f284            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원색깔4',
    rsp_f145            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매도거래원5',
    rsp_f165            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원수량5',
    rsp_f170            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래원별증감5',
    rsp_f150            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원코드5',
    rsp_f275            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원색깔5',
    rsp_f155            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '매수거래원5',
    rsp_f175            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원수량5',
    rsp_f180            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래원별증감5',
    rsp_f160            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원코드5',
    rsp_f285            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원색깔5',
    rsp_f261            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계매도추정합',
    rsp_f262            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계매도추정합변동',
    rsp_f263            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계매수추정합',
    rsp_f264            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계매수추정합변동',
    rsp_f267            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계순매수추정합',
    rsp_f268            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계순매수변동',
    rsp_f337            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래소구분',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0F 주식당일거래원 실시간';

-- ------------------------------------------------------------
-- ws_0g_etf_nav : ETF NAV (api_id: 0G)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0g_etf_nav (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0G)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f36             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NAV',
    rsp_f37             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NAV전일대비',
    rsp_f38             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NAV등락율',
    rsp_f39             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '추적오차율',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f667            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW기어링비율',
    rsp_f668            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW손익분기율',
    rsp_f669            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW자본지지점',
    rsp_f265            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NAV/지수괴리율',
    rsp_f266            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'NAV/ETF괴리율',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0G ETF NAV 실시간';

-- ------------------------------------------------------------
-- ws_0h_stk_exp_ccls : 주식예상체결 (api_id: 0H)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0h_stk_exp_ccls (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0H)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f15             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래량',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0H 주식예상체결 실시간';

-- ------------------------------------------------------------
-- ws_0i_intl_gold_prc : 국제금환산가격 (api_id: 0I)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0i_intl_gold_prc (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0I)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 코드 (MGD/MGU)',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0I 국제금환산가격 실시간';

-- ------------------------------------------------------------
-- ws_0j_sect_idx : 업종지수 (api_id: 0J)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0j_sect_idx (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0J)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 업종코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f15             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래량',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f14             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    rsp_f16             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    rsp_f17             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    rsp_f18             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f26             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0J 업종지수 실시간';

-- ------------------------------------------------------------
-- ws_0u_sect_flct : 업종등락 (api_id: 0U)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0u_sect_flct (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0U)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 업종코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f252            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '상승종목수',
    rsp_f251            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '상한종목수',
    rsp_f253            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '보합종목수',
    rsp_f255            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '하락종목수',
    rsp_f254            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '하한종목수',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f14             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f256            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래형성종목수',
    rsp_f257            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래형성비율',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0U 업종등락 실시간';

-- ------------------------------------------------------------
-- ws_0g_stk_nfo : 주식종목정보 (api_id: 0g)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0g_stk_nfo (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0g)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f297            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '임의연장',
    rsp_f592            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '장전임의연장',
    rsp_f593            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '장후임의연장',
    rsp_f305            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '상한가',
    rsp_f306            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '하한가',
    rsp_f307            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기준가',
    rsp_f689            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '조기종료ELW발생',
    rsp_f594            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '통화단위',
    rsp_f382            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '증거금율표시',
    rsp_f370            VARCHAR(200) NOT NULL DEFAULT '' COMMENT '종목정보',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0g 주식종목정보 실시간';

-- ------------------------------------------------------------
-- ws_0m_elw_thr : ELW 이론가 (api_id: 0m)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0m_elw_thr (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0m)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f670            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW이론가',
    rsp_f671            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW내재변동성',
    rsp_f672            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW델타',
    rsp_f673            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW감마',
    rsp_f674            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW쎄타',
    rsp_f675            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW베가',
    rsp_f676            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW로',
    rsp_f706            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'LP호가내재변동성',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0m ELW 이론가 실시간';

-- ------------------------------------------------------------
-- ws_0s_mkt_tm : 장시작시간 (api_id: 0s)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0s_mkt_tm (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0s)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 요소',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f215            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '장운영구분',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f214            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장시작예상잔여시간',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_dt (req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0s 장시작시간 실시간';

-- ------------------------------------------------------------
-- ws_0u_elw_idx : ELW 지표 (api_id: 0u)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0u_elw_idx (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0u)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f666            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW패리티',
    rsp_f1211           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW프리미엄',
    rsp_f667            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW기어링비율',
    rsp_f668            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW손익분기율',
    rsp_f669            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW자본지지점',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0u ELW 지표 실시간';

-- ------------------------------------------------------------
-- ws_0w_stk_prg_trd : 종목프로그램매매 (api_id: 0w)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_0w_stk_prg_trd (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    req_type            VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '실시간 항목 코드 (0w)',
    req_item            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '실시간 등록 종목코드',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f202            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도수량',
    rsp_f204            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도금액',
    rsp_f206            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수수량',
    rsp_f208            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수금액',
    rsp_f210            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수수량',
    rsp_f211            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수수량증감',
    rsp_f212            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수금액',
    rsp_f213            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수금액증감',
    rsp_f214            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장시작예상잔여시간',
    rsp_f215            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '장운영구분',
    rsp_f216            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '투자자별ticker',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_item_dt (req_item, req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_0w 종목프로그램매매 실시간';

-- ------------------------------------------------------------
-- ws_ka10171_cndsr_lst : 조건검색 목록조회 (api_id: ka10171)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_ka10171_cndsr_lst (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_seq             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '조건검색식 일련번호',
    rsp_name            VARCHAR(100) NOT NULL DEFAULT '' COMMENT '조건검색식 명',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_dt (req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_ka10171 조건검색 목록조회';

-- ------------------------------------------------------------
-- ws_ka10172_cndsr_req : 조건검색 요청 일반 (api_id: ka10172)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_ka10172_cndsr_req (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_seq             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '조건검색식 일련번호',
    rsp_f9001           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    rsp_f302            VARCHAR(40)  NOT NULL DEFAULT '' COMMENT '종목명',
    rsp_f10             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    rsp_f25             VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    rsp_f11             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    rsp_f12             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    rsp_f13             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    rsp_f16             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    rsp_f17             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    rsp_f18             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_dt (req_dt),
    INDEX idx_seq (rsp_seq)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_ka10172 조건검색 요청 일반';

-- ------------------------------------------------------------
-- ws_ka10173_cndsr_rt : 조건검색 요청 실시간 (api_id: ka10173)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_ka10173_cndsr_rt (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_seq             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '조건검색식 일련번호',
    rsp_jmcode          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    rsp_f841            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '일련번호',
    rsp_f9001           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목코드',
    rsp_f843            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '삽입삭제 구분 (I/D)',
    rsp_f20             VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '체결시간',
    rsp_f907            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '매도/수 구분',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_dt (req_dt),
    INDEX idx_seq_jm (rsp_seq, rsp_jmcode)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_ka10173 조건검색 요청 실시간';

-- ------------------------------------------------------------
-- ws_ka10174_cndsr_clr : 조건검색 실시간 해제 (api_id: ka10174)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ws_ka10174_cndsr_clr (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    req_dt              VARCHAR(14)  NOT NULL DEFAULT '' COMMENT '수신 일시 (YYYYMMDDHHmmss)',
    rsp_return_code     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '결과코드',
    rsp_return_msg      VARCHAR(200) NOT NULL DEFAULT '' COMMENT '결과메시지',
    rsp_seq             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '조건검색식 일련번호',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    PRIMARY KEY (id),
    INDEX idx_dt (req_dt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='ws_ka10174 조건검색 실시간 해제';