-- =============================================================
-- volume (종목정보/순위정보) 모듈 DB 스키마
-- specs_response.py  : STKINFO_RESPONSE_SPECS
-- specs_response_rank.py : RKINFO_RESPONSE_SPECS
-- =============================================================

-- -------------------------------------------------------------
-- Drop existing tables if they exist (for development/testing purposes)
-- -------------------------------------------------------------
DROP TABLE IF EXISTS ka00198_item_inq_rank CASCADE;
DROP TABLE IF EXISTS ka10001 CASCADE;
DROP TABLE IF EXISTS ka10002 CASCADE;
DROP TABLE IF EXISTS ka10003_cntr_infr CASCADE;
DROP TABLE IF EXISTS ka10013_crd_trde_trend CASCADE;
DROP TABLE IF EXISTS ka10015_daly_trde_dtl CASCADE;
DROP TABLE IF EXISTS ka10016_ntl_pric CASCADE;
DROP TABLE IF EXISTS ka10017_updown_pric CASCADE;
DROP TABLE IF EXISTS ka10018_high_low_pric_alacc CASCADE;
DROP TABLE IF EXISTS ka10019_pric_jmpflu CASCADE;
DROP TABLE IF EXISTS ka10024_trde_qty_updt CASCADE;
DROP TABLE IF EXISTS ka10025_prps_cnctr CASCADE;
DROP TABLE IF EXISTS ka10026_high_low_per CASCADE;
DROP TABLE IF EXISTS ka10028_open_pric_pre_flu_rt CASCADE;
DROP TABLE IF EXISTS ka10043_trde_ori_prps_anly CASCADE;
DROP TABLE IF EXISTS ka10052_trde_ori_mont_trde_qty CASCADE;
DROP TABLE IF EXISTS ka10054_motn_stk CASCADE;
DROP TABLE IF EXISTS ka10055_tdy_pred_cntr_qty CASCADE;
DROP TABLE IF EXISTS ka10058_invsr_daly_trde_stk CASCADE;
DROP TABLE IF EXISTS ka10059_stk_invsr_orgn CASCADE;
DROP TABLE IF EXISTS ka10061_stk_invsr_orgn_tot CASCADE;
DROP TABLE IF EXISTS ka10084_tdy_pred_cntr CASCADE;
DROP TABLE IF EXISTS ka10095_atn_stk_infr CASCADE;
DROP TABLE IF EXISTS ka10099_list CASCADE;
DROP TABLE IF EXISTS ka10100 CASCADE;
DROP TABLE IF EXISTS ka10101_list CASCADE;
DROP TABLE IF EXISTS ka10102_list CASCADE;
DROP TABLE IF EXISTS ka90003_prm_netprps_upper_50 CASCADE;
DROP TABLE IF EXISTS ka90004_header CASCADE;
DROP TABLE IF EXISTS ka90004_stk_prm_trde_prst CASCADE;
DROP TABLE IF EXISTS kt20016_header CASCADE;
DROP TABLE IF EXISTS kt20016_crd_loan_pos_stk CASCADE;
DROP TABLE IF EXISTS kt20017 CASCADE;
DROP TABLE IF EXISTS ka10023_trde_qty_sdnin CASCADE;
DROP TABLE IF EXISTS ka10030_tdy_trde_qty_upper CASCADE;
DROP TABLE IF EXISTS ka10031_pred_trde_qty_upper CASCADE;
DROP TABLE IF EXISTS ka10032_trde_prica_upper CASCADE;

-- -------------------------------------------------------------
-- ka00198 – 실시간종목조회순위 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka00198_item_inq_rank (
    id           BIGINT        NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_nm       VARCHAR(100)  NOT NULL DEFAULT '' COMMENT '종목명',
    bigd_rank    VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '빅데이터 순위',
    rank_chg     VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '순위 등락',
    rank_chg_sign VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '순위 등락 부호',
    past_curr_prc VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '과거 현재가',
    base_comp_sign VARCHAR(4)  NOT NULL DEFAULT '' COMMENT '기준가 대비 부호',
    base_comp_chgr VARCHAR(20) NOT NULL DEFAULT '' COMMENT '기준가 대비 등락율',
    prev_base_sign VARCHAR(4)  NOT NULL DEFAULT '' COMMENT '직전 기준 대비 부호',
    prev_base_chgr VARCHAR(20) NOT NULL DEFAULT '' COMMENT '직전 기준 대비 등락율',
    dt           VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '일자',
    tm           VARCHAR(6)    NOT NULL DEFAULT '' COMMENT '시간',
    stk_cd       VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '종목코드',
    fetched_at   DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='실시간종목조회순위';

-- -------------------------------------------------------------
-- ka10001 – 주식기본정보요청 (scalar)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10001 (
    id                   BIGINT        NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd               VARCHAR(12)   NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm               VARCHAR(100)  NOT NULL DEFAULT '' COMMENT '종목명',
    setl_mm              VARCHAR(6)    NOT NULL DEFAULT '' COMMENT '결산월',
    fav                  VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '액면가',
    cap                  VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '자본금',
    flo_stk              VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '상장주식',
    crd_rt               VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '신용비율',
    oyr_hgst             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '연중최고',
    oyr_lwst             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '연중최저',
    mac                  VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '시가총액',
    mac_wght             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '시가총액비중',
    for_exh_rt           VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '외인소진률',
    repl_pric            VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '대용가',
    per                  VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'PER',
    eps                  VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'EPS',
    roe                  VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'ROE',
    pbr                  VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'PBR',
    ev                   VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'EV',
    bps                  VARCHAR(20)   NOT NULL DEFAULT '' COMMENT 'BPS',
    sale_amt             VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '매출액',
    bus_pro              VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '영업이익',
    cup_nga              VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '당기순이익',
    p250hgst             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '250최고',
    p250lwst             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '250최저',
    open_pric            VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '시가',
    high_pric            VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '고가',
    low_pric             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '저가',
    upl_pric             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '상한가',
    lst_pric             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '하한가',
    base_pric            VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '기준가',
    exp_cntr_pric        VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '예상체결가',
    exp_cntr_qty         VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '예상체결수량',
    p250hgst_pric_dt     VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '250최고가일',
    p250hgst_pric_pre_rt VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '250최고가대비율',
    p250lwst_pric_dt     VARCHAR(8)    NOT NULL DEFAULT '' COMMENT '250최저가일',
    p250lwst_pric_pre_rt VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '250최저가대비율',
    cur_prc              VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '현재가',
    pre_sig              VARCHAR(4)    NOT NULL DEFAULT '' COMMENT '대비기호',
    pred_pre             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt               VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '등락율',
    trde_qty             VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '거래량',
    trde_pre             VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '거래대비',
    fav_unit             VARCHAR(10)   NOT NULL DEFAULT '' COMMENT '액면가단위',
    dstr_stk             VARCHAR(30)   NOT NULL DEFAULT '' COMMENT '유통주식',
    dstr_rt              VARCHAR(20)   NOT NULL DEFAULT '' COMMENT '유통비율',
    fetched_at           DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식기본정보';

-- -------------------------------------------------------------
-- ka10002 – 주식거래원요청 (scalar)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10002 (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd              VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm              VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    flu_smbol           VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '등락부호',
    base_pric           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기준가',
    pred_pre            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt              VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    sel_trde_ori_nm_1   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매도거래원명1',
    sel_trde_ori_1      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원1',
    sel_trde_qty_1      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래량1',
    buy_trde_ori_nm_1   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매수거래원명1',
    buy_trde_ori_1      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원1',
    buy_trde_qty_1      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래량1',
    sel_trde_ori_nm_2   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매도거래원명2',
    sel_trde_ori_2      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원2',
    sel_trde_qty_2      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래량2',
    buy_trde_ori_nm_2   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매수거래원명2',
    buy_trde_ori_2      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원2',
    buy_trde_qty_2      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래량2',
    sel_trde_ori_nm_3   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매도거래원명3',
    sel_trde_ori_3      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원3',
    sel_trde_qty_3      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래량3',
    buy_trde_ori_nm_3   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매수거래원명3',
    buy_trde_ori_3      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원3',
    buy_trde_qty_3      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래량3',
    sel_trde_ori_nm_4   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매도거래원명4',
    sel_trde_ori_4      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원4',
    sel_trde_qty_4      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래량4',
    buy_trde_ori_nm_4   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매수거래원명4',
    buy_trde_ori_4      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원4',
    buy_trde_qty_4      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래량4',
    sel_trde_ori_nm_5   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매도거래원명5',
    sel_trde_ori_5      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매도거래원5',
    sel_trde_qty_5      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도거래량5',
    buy_trde_ori_nm_5   VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '매수거래원명5',
    buy_trde_ori_5      VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매수거래원5',
    buy_trde_qty_5      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수거래량5',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='주식거래원';

-- -------------------------------------------------------------
-- ka10003 – 체결정보요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10003_cntr_infr (
    id                BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id         BIGINT       NOT NULL COMMENT '헤더 참조ID (stk_cd+fetched_at 그룹)',
    stk_cd            VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    tm                VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '시간',
    cur_prc           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pre_rt            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '대비율',
    pri_sel_bid_unit  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '우선매도호가단위',
    pri_buy_bid_unit  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '우선매수호가단위',
    cntr_trde_qty     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결거래량',
    sign              VARCHAR(4)   NOT NULL DEFAULT '' COMMENT 'sign',
    acc_trde_qty      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    cntr_str          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결강도',
    stex_tp           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래소구분',
    fetched_at        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='체결정보';

-- -------------------------------------------------------------
-- ka10013 – 신용매매동향요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10013_crd_trde_trend (
    id           BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id    BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd       VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    dt           VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    cur_prc      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    new          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '신규',
    rpya         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '상환',
    remn         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '잔고',
    amt          VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '금액',
    pre          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '대비',
    shr_rt       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '공여율',
    remn_rt      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '잔고율',
    fetched_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신용매매동향';

-- -------------------------------------------------------------
-- ka10015 – 일별거래상세요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10015_daly_trde_dtl (
    id                      BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id               BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd                  VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    dt                      VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    close_pric              VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종가',
    pred_pre_sig            VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt                  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    trde_qty                VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    trde_prica              VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    bf_mkrt_trde_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장전거래량',
    bf_mkrt_trde_wght       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장전거래비중',
    opmr_trde_qty           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장중거래량',
    opmr_trde_wght          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장중거래비중',
    af_mkrt_trde_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장후거래량',
    af_mkrt_trde_wght       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장후거래비중',
    tot_3                   VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '합계3',
    prid_trde_qty           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기간중거래량',
    cntr_str                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결강도',
    for_poss                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외인보유',
    for_wght                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외인비중',
    for_netprps             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외인순매수',
    orgn_netprps            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기관순매수',
    ind_netprps             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '개인순매수',
    frgn                    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국계',
    crd_remn_rt             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '신용잔고율',
    prm                     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '프로그램',
    bf_mkrt_trde_prica      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장전거래대금',
    bf_mkrt_trde_prica_wght VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장전거래대금비중',
    opmr_trde_prica         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장중거래대금',
    opmr_trde_prica_wght    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장중거래대금비중',
    af_mkrt_trde_prica      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장후거래대금',
    af_mkrt_trde_prica_wght VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '장후거래대금비중',
    fetched_at              DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='일별거래상세';

-- -------------------------------------------------------------
-- ka10016 – 신고저가요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10016_ntl_pric (
    id                    BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id             BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd                VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm                VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig          VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre              VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    trde_qty              VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    pred_trde_qty_pre_rt  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비율',
    sel_bid               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가',
    buy_bid               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가',
    high_pric             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric              VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    fetched_at            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신고저가';

-- -------------------------------------------------------------
-- ka10017 – 상하한가요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10017_updown_pric (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_infr        VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '종목정보',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    trde_qty        VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    pred_trde_qty   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '전일거래량',
    sel_req         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도잔량',
    sel_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가',
    buy_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가',
    buy_req         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수잔량',
    cnt             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '횟수',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='상하한가';

-- -------------------------------------------------------------
-- ka10018 – 고저가근접요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10018_high_low_pric_alacc (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    trde_qty        VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    sel_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가',
    buy_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가',
    tdy_high_pric   VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일고가',
    tdy_low_pric    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '당일저가',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='고저가근접';

-- -------------------------------------------------------------
-- ka10019 – 가격급등락요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10019_pric_jmpflu (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_cls         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목분류',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    base_pric       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기준가',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    base_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기준대비',
    trde_qty        VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    jmp_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '급등률',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='가격급등락';

-- -------------------------------------------------------------
-- ka10024 – 거래량갱신요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10024_trde_qty_updt (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    prev_trde_qty   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '이전거래량',
    now_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '현재거래량',
    sel_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가',
    buy_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='거래량갱신';

-- -------------------------------------------------------------
-- ka10025 – 매물대집중요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10025_prps_cnctr (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    now_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '현재거래량',
    pric_strt       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '가격대시작',
    pric_end        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '가격대끝',
    prps_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매물량',
    prps_rt         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매물비',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='매물대집중';

-- -------------------------------------------------------------
-- ka10026 – 고저PER요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10026_high_low_per (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    per             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'PER',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    now_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '현재거래량',
    sel_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='고저PER';

-- -------------------------------------------------------------
-- ka10028 – 시가대비등락률요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10028_open_pric_pre_flu_rt (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    open_pric       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    open_pric_pre   VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가대비',
    now_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '현재거래량',
    cntr_str        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결강도',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='시가대비등락률';

-- -------------------------------------------------------------
-- ka10043 – 거래원매물대분석요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10043_trde_ori_prps_anly (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    close_pric      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종가',
    pre_sig         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    sel_qty         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도량',
    buy_qty         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수량',
    netprps_qty     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매수수량',
    trde_qty_sum    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래량합',
    trde_wght       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '거래비중',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='거래원매물대분석';

-- -------------------------------------------------------------
-- ka10052 – 거래원순간거래량요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10052_trde_ori_mont_trde_qty (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    tm              VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '시간',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    trde_ori_nm     VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '거래원명',
    tp              VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '구분',
    mont_trde_qty   VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순간거래량',
    acc_netprps     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '누적순매수',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='거래원순간거래량';

-- -------------------------------------------------------------
-- ka10054 – 변동성완화장치발동종목요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10054_motn_stk (
    id                    BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id             BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd                VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm                VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    acc_trde_qty          VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    motn_pric             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '발동가격',
    dynm_dispty_rt        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '동적괴리율',
    trde_cntr_proc_time   VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '매매체결처리시각',
    virelis_time          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT 'VI해제시각',
    viaplc_tp             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT 'VI적용구분',
    dynm_stdpc            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '동적기준가격',
    static_stdpc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '정적기준가격',
    static_dispty_rt      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '정적괴리율',
    open_pric_pre_flu_rt  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가대비등락률',
    vimotn_cnt            VARCHAR(10)  NOT NULL DEFAULT '' COMMENT 'VI발동횟수',
    stex_tp               VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래소구분',
    fetched_at            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='변동성완화장치발동종목';

-- -------------------------------------------------------------
-- ka10055 – 당일전일체결량요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10055_tdy_pred_cntr_qty (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    cntr_tm         VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '체결시간',
    cntr_pric       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    cntr_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결량',
    acc_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica  VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='당일전일체결량';

-- -------------------------------------------------------------
-- ka10058 – 투자자별일별매매종목요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10058_invsr_daly_trde_stk (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    netslmt_qty     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '순매도수량',
    netslmt_amt     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '순매도금액',
    prsm_avg_pric   VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '추정평균가',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pre_sig         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    avg_pric_pre    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '평균가대비',
    pre_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '대비율',
    dt_trde_qty     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기간거래량',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='투자자별일별매매종목';

-- -------------------------------------------------------------
-- ka10059 – 종목별투자자기관별요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10059_stk_invsr_orgn (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pre_sig         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    acc_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica  VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    ind_invsr       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '개인투자자',
    frgnr_invsr     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국인투자자',
    orgn            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기관계',
    fnnc_invt       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '금융투자',
    insrnc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '보험',
    invtrt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '투신',
    etc_fnnc        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타금융',
    bank            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '은행',
    penfnd_etc      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '연기금등',
    samo_fund       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '사모펀드',
    natn            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '국가',
    etc_corp        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타법인',
    natfor          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '내외국인',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목별투자자기관별';

-- -------------------------------------------------------------
-- ka10061 – 종목별투자자기관별합계요청 (LIST only, no stk_cd key)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10061_stk_invsr_orgn_tot (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    ind_invsr       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '개인투자자',
    frgnr_invsr     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '외국인투자자',
    orgn            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기관계',
    fnnc_invt       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '금융투자',
    insrnc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '보험',
    invtrt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '투신',
    etc_fnnc        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타금융',
    bank            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '은행',
    penfnd_etc      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '연기금등',
    samo_fund       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '사모펀드',
    natn            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '국가',
    etc_corp        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기타법인',
    natfor          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '내외국인',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_fetched (fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목별투자자기관별합계';

-- -------------------------------------------------------------
-- ka10084 – 당일전일체결요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10084_tdy_pred_cntr (
    id                BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id         BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd            VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    tm                VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '시간',
    cur_prc           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pre_rt            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '대비율',
    pri_sel_bid_unit  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '우선매도호가단위',
    pri_buy_bid_unit  VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '우선매수호가단위',
    cntr_trde_qty     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결거래량',
    sign              VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    acc_trde_qty      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    acc_trde_prica    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래대금',
    cntr_str          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결강도',
    stex_tp           VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '거래소구분',
    fetched_at        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='당일전일체결';

-- -------------------------------------------------------------
-- ka10095 – 관심종목정보요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10095_atn_stk_infr (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id           BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd              VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm              VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    base_pric           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기준가',
    pred_pre            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    pred_pre_sig        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    flu_rt              VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    trde_qty            VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    trde_prica          VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금',
    cntr_qty            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결량',
    cntr_str            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '체결강도',
    pred_trde_qty_pre   VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일거래량대비',
    sel_bid             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도호가',
    buy_bid             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수호가',
    sel_1th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도1차호가',
    sel_2th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도2차호가',
    sel_3th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도3차호가',
    sel_4th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도4차호가',
    sel_5th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도5차호가',
    buy_1th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수1차호가',
    buy_2th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수2차호가',
    buy_3th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수3차호가',
    buy_4th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수4차호가',
    buy_5th_bid         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수5차호가',
    upl_pric            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '상한가',
    lst_pric            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '하한가',
    open_pric           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '시가',
    high_pric           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '고가',
    low_pric            VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '저가',
    close_pric          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종가',
    cntr_tm             VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '체결시간',
    exp_cntr_pric       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결가',
    exp_cntr_qty        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '예상체결량',
    cap                 VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '자본금',
    fav                 VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '액면가',
    mac                 VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '시가총액',
    stkcnt              VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '주식수',
    bid_tm              VARCHAR(6)   NOT NULL DEFAULT '' COMMENT '호가시간',
    dt                  VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '일자',
    pri_sel_req         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '우선매도잔량',
    pri_buy_req         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '우선매수잔량',
    pri_sel_cnt         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '우선매도건수',
    pri_buy_cnt         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '우선매수건수',
    tot_sel_req         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '총매도잔량',
    tot_buy_req         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '총매수잔량',
    tot_sel_cnt         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '총매도건수',
    tot_buy_cnt         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '총매수건수',
    prty                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '패리티',
    gear                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '기어링',
    pl_qutr             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '손익분기',
    cap_support         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '자본지지',
    elwexec_pric        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT 'ELW행사가',
    cnvt_rt             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전환비율',
    elwexpr_dt          VARCHAR(8)   NOT NULL DEFAULT '' COMMENT 'ELW만기일',
    cntr_engg           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '미결제약정',
    cntr_pred_pre       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '미결제전일대비',
    theory_pric         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '이론가',
    innr_vltl           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '내재변동성',
    delta               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '델타',
    gam                 VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '감마',
    theta               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '쎄타',
    vega                VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '베가',
    law                 VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '로',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='관심종목정보';

-- -------------------------------------------------------------
-- ka10099 – 종목정보 리스트 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10099_list (
    id                BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id         BIGINT       NOT NULL COMMENT '헤더 참조ID',
    code              VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    name              VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    list_count        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '상장주식수',
    audit_info        VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '감리구분',
    reg_day           VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '상장일',
    last_price        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일종가',
    state             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목상태',
    market_code       VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시장구분코드',
    market_name       VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '시장명',
    up_name           VARCHAR(100) NOT NULL DEFAULT '' COMMENT '업종명',
    up_size_name      VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '회사크기분류',
    order_warning     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '투자유의종목여부',
    company_class_name VARCHAR(50) NOT NULL DEFAULT '' COMMENT '회사분류',
    nxt_enable        VARCHAR(4)   NOT NULL DEFAULT '' COMMENT 'NXT가능여부',
    fetched_at        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_code_fetched (code, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목정보리스트';

-- -------------------------------------------------------------
-- ka10100 – 종목정보 조회 (scalar)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10100 (
    id                  BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    code                VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    name                VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    list_count          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '상장주식수',
    audit_info          VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '감리구분',
    reg_day             VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '상장일',
    last_price          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일종가',
    state               VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '종목상태',
    market_code         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시장구분코드',
    market_name         VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '시장명',
    up_name             VARCHAR(100) NOT NULL DEFAULT '' COMMENT '업종명',
    up_size_name        VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '회사크기분류',
    company_class_name  VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '회사분류',
    order_warning       VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '투자유의종목여부',
    nxt_enable          VARCHAR(4)   NOT NULL DEFAULT '' COMMENT 'NXT가능여부',
    fetched_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_code_fetched (code, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목정보조회';

-- -------------------------------------------------------------
-- ka10101 – 업종코드 리스트 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10101_list (
    id           BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id    BIGINT       NOT NULL COMMENT '헤더 참조ID',
    market_code  VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시장구분코드',
    code         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '코드',
    name         VARCHAR(100) NOT NULL DEFAULT '' COMMENT '업종명',
    grp          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '그룹',
    fetched_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_code_fetched (code, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='업종코드리스트';

-- -------------------------------------------------------------
-- ka10102 – 회원사 리스트 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10102_list (
    id         BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id  BIGINT       NOT NULL COMMENT '헤더 참조ID',
    code       VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '코드',
    name       VARCHAR(100) NOT NULL DEFAULT '' COMMENT '회원사명',
    gb         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '구분',
    fetched_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_code_fetched (code, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='회원사리스트';

-- -------------------------------------------------------------
-- ka90003 – 프로그램순매수상위50 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka90003_prm_netprps_upper_50 (
    id               BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id        BIGINT       NOT NULL COMMENT '헤더 참조ID',
    rank             VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '순위',
    stk_cd           VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm           VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    flu_sig          VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '등락기호',
    pred_pre         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    flu_rt           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락율',
    acc_trde_qty     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '누적거래량',
    prm_sell_amt     VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '프로그램매도금액',
    prm_buy_amt      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '프로그램매수금액',
    prm_netprps_amt  VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '프로그램순매수금액',
    fetched_at       DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='프로그램순매수상위50';

-- -------------------------------------------------------------
-- ka90004 – 종목별프로그램매매현황 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka90004_header (
    id         BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    tot_1      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '매수체결수량합계',
    tot_2      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '매수체결금액합계',
    tot_3      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '매도체결수량합계',
    tot_4      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '매도체결금액합계',
    tot_5      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '순매수대금합계',
    tot_6      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '합계6',
    fetched_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_fetched (fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목별프로그램매매현황 헤더';

CREATE TABLE IF NOT EXISTS ka90004_stk_prm_trde_prst (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID (ka90004_header.id)',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    flu_sig         VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '등락기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    buy_cntr_qty    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매수체결수량',
    buy_cntr_amt    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '매수체결금액',
    sel_cntr_qty    VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '매도체결수량',
    sel_cntr_amt    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '매도체결금액',
    netprps_prica   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '순매수대금',
    all_trde_rt     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전체거래비율',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='종목별프로그램매매현황';

-- -------------------------------------------------------------
-- kt20016 – 신용융자 가능종목요청 (scalar header + LIST)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt20016_header (
    id              BIGINT      NOT NULL AUTO_INCREMENT COMMENT 'PK',
    crd_loan_able   VARCHAR(4)  NOT NULL DEFAULT '' COMMENT '신용융자가능여부',
    fetched_at      DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_fetched (fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신용융자가능종목 헤더';

CREATE TABLE IF NOT EXISTS kt20016_crd_loan_pos_stk (
    id                    BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id             BIGINT       NOT NULL COMMENT '헤더 참조ID (kt20016_header.id)',
    stk_cd                VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm                VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    crd_assr_rt           VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '신용보증금율',
    repl_pric             VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '대용가',
    pred_close_pric       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일종가',
    crd_limit_over_yn     VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '신용한도초과여부',
    crd_limit_over_txt    VARCHAR(50)  NOT NULL DEFAULT '' COMMENT '신용한도초과',
    fetched_at            DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신용융자가능종목';

-- -------------------------------------------------------------
-- kt20017 – 신용융자 가능문의 (scalar)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt20017 (
    id           BIGINT      NOT NULL AUTO_INCREMENT COMMENT 'PK',
    stk_cd       VARCHAR(12) NOT NULL DEFAULT '' COMMENT '종목코드 (요청파라미터)',
    crd_alow_yn  VARCHAR(4)  NOT NULL DEFAULT '' COMMENT '신용가능여부',
    fetched_at   DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='신용융자가능문의';

-- =============================================================
-- 순위정보 (RKINFO_RESPONSE_SPECS)
-- =============================================================

-- -------------------------------------------------------------
-- ka10023 – 거래량급증요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10023_trde_qty_sdnin (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    mrkt_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시장구분',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    prev_trde_qty   VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '이전거래량',
    now_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '현재거래량',
    sdnin_qty       VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '급증량',
    sdnin_rt        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '급증률',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='거래량급증';

-- -------------------------------------------------------------
-- ka10030 – 당일거래량상위요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10030_tdy_trde_qty_upper (
    req_dt              VARCHAR(8)   NOT NULL DEFAULT '' COMMENT '요청 일자',
    req_mrkt_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 시장구분',
    req_sort_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 정렬구분',
    req_mang_stk_incls  VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 관리종목포함',
    req_crd_tp          VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 신용구분',
    req_trde_qty_tp     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 거래량구분',
    req_pric_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 가격구분',
    req_trde_prica_tp   VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 거래대금구분',
    req_mrkt_open_tp    VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 장운영구분',
    req_stex_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '요청 거래소구분',
    rsp_rank        INT         NOT NULL DEFAULT 1   COMMENT '응답 순위',
    rsp_stk_cd      VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '응답 종목코드',
    rsp_stk_nm      VARCHAR(100) NOT NULL DEFAULT '' COMMENT '응답 종목명',
    rsp_mrkt_tp     VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '응답 시장구분',
    rsp_cur_prc     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 현재가',
    rsp_flu_rt      VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 등락률',
    rsp_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '응답 거래량',
    rsp_pred_rt     VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '응답 전일비',
    rsp_trde_amt    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '응답 거래금액(백만)',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (req_dt, req_mrkt_tp, req_sort_tp, req_mang_stk_incls, req_crd_tp, req_trde_qty_tp, req_pric_tp, req_trde_prica_tp, req_mrkt_open_tp, req_stex_tp, rsp_rank),
    INDEX idx_dt_rank (req_dt, rsp_rank),
    INDEX idx_dt_stk (req_dt, rsp_stk_cd)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='당일거래량상위';

-- -------------------------------------------------------------
-- ka10031 – 전일거래량상위요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10031_pred_trde_qty_upper (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    mrkt_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시장구분',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    pred_pre_sig    VARCHAR(4)   NOT NULL DEFAULT '' COMMENT '전일대비기호',
    pred_pre        VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '전일대비',
    trde_qty        VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래량',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='전일거래량상위';

-- -------------------------------------------------------------
-- ka10032 – 거래대금상위요청 (LIST only)
-- -------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10032_trde_prica_upper (
    id              BIGINT       NOT NULL AUTO_INCREMENT COMMENT 'PK',
    header_id       BIGINT       NOT NULL COMMENT '헤더 참조ID',
    now_rank        VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '현재순위',
    pred_rank       VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '전일순위',
    stk_cd          VARCHAR(12)  NOT NULL DEFAULT '' COMMENT '종목코드',
    stk_nm          VARCHAR(100) NOT NULL DEFAULT '' COMMENT '종목명',
    mrkt_tp         VARCHAR(10)  NOT NULL DEFAULT '' COMMENT '시장구분',
    cur_prc         VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '현재가',
    flu_rt          VARCHAR(20)  NOT NULL DEFAULT '' COMMENT '등락률',
    now_trde_qty    VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '현재거래량',
    trde_prica      VARCHAR(30)  NOT NULL DEFAULT '' COMMENT '거래대금(백만)',
    fetched_at      DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수집일시',
    PRIMARY KEY (id),
    INDEX idx_header (header_id),
    INDEX idx_stk_fetched (stk_cd, fetched_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='거래대금상위';
