-- ============================================================
-- Kiwoom REST API 계좌(acnt) 응답 저장 스키마
-- ============================================================

-- 공통 메타 컬럼: acct_no (계좌번호), fetched_at (수신일시)

-- ------------------------------------------------------------
-- Drop existing tables if they exist (for development/testing purposes)
-- ------------------------------------------------------------
DROP TABLE IF EXISTS ka00001 CASCADE;
DROP TABLE IF EXISTS ka01690_header CASCADE;
DROP TABLE IF EXISTS ka01690_day_bal_rt CASCADE;
DROP TABLE IF EXISTS ka10072 CASCADE;
DROP TABLE IF EXISTS ka10073 CASCADE;
DROP TABLE IF EXISTS ka10074_header CASCADE;
DROP TABLE IF EXISTS ka10074_dt_rlzt_pl CASCADE;
DROP TABLE IF EXISTS ka10075 CASCADE;
DROP TABLE IF EXISTS ka10076 CASCADE;
DROP TABLE IF EXISTS ka10077_header CASCADE;
DROP TABLE IF EXISTS ka10077_tdy_rlzt_pl_dtl CASCADE;
DROP TABLE IF EXISTS ka10085 CASCADE;
DROP TABLE IF EXISTS ka10088 CASCADE;
DROP TABLE IF EXISTS ka10170_header CASCADE;
DROP TABLE IF EXISTS ka10170_tdy_trde_diary CASCADE;
DROP TABLE IF EXISTS kt00001_header CASCADE;
DROP TABLE IF EXISTS kt00001_stk_entr_prst CASCADE;
DROP TABLE IF EXISTS kt00002 CASCADE;
DROP TABLE IF EXISTS kt00003 CASCADE;
DROP TABLE IF EXISTS kt00004_header CASCADE;
DROP TABLE IF EXISTS kt00004_stk_acnt_evlt_prst CASCADE;
DROP TABLE IF EXISTS kt00005_header CASCADE;
DROP TABLE IF EXISTS kt00005_stk_cntr_remn CASCADE;
DROP TABLE IF EXISTS kt00007 CASCADE;
DROP TABLE IF EXISTS kt00008_header CASCADE;
DROP TABLE IF EXISTS kt00008_setl_prps CASCADE;
DROP TABLE IF EXISTS kt00009_header CASCADE;
DROP TABLE IF EXISTS kt00009_acnt_ord_cntr_prst CASCADE;
DROP TABLE IF EXISTS kt00015 CASCADE;
DROP TABLE IF EXISTS kt00018_header CASCADE;
DROP TABLE IF EXISTS kt00018_acnt_evlt_remn CASCADE;
DROP TABLE IF EXISTS kt50020_header CASCADE;
DROP TABLE IF EXISTS kt50020_gold_acnt_evlt_prst CASCADE;
DROP TABLE IF EXISTS kt50021 CASCADE;
DROP TABLE IF EXISTS kt50030 CASCADE;
DROP TABLE IF EXISTS kt50031 CASCADE;
DROP TABLE IF EXISTS kt50032_header CASCADE;
DROP TABLE IF EXISTS kt50032_gold_trde_hist CASCADE;
DROP TABLE IF EXISTS kt50075 CASCADE;


-- ------------------------------------------------------------
-- ka00001 : 계좌번호 조회
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka00001 (
    id          BIGINT       NOT NULL AUTO_INCREMENT,
    acct_no     VARCHAR(20)  NOT NULL COMMENT '요청 계좌번호',
    fetched_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '수신일시',
    acctNo      VARCHAR(20)           COMMENT '계좌번호',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka00001 계좌번호 조회';

-- ------------------------------------------------------------
-- ka01690 : 일별잔고수익률 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka01690_header (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL COMMENT '요청 계좌번호',
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dt              VARCHAR(8)             COMMENT '일자',
    tot_buy_amt     DECIMAL(20,2)          COMMENT '총 매입가',
    tot_evlt_amt    DECIMAL(20,2)          COMMENT '총 평가금액',
    tot_evltv_prft  DECIMAL(20,2)          COMMENT '총 평가손익',
    tot_prft_rt     DECIMAL(10,4)          COMMENT '수익률',
    dbst_bal        DECIMAL(20,2)          COMMENT '예수금',
    day_stk_asst    DECIMAL(20,2)          COMMENT '추정자산',
    buy_wght        DECIMAL(10,4)          COMMENT '현금비중',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka01690 일별잔고수익률 헤더';

CREATE TABLE IF NOT EXISTS ka01690_day_bal_rt (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    header_id   BIGINT        NOT NULL COMMENT 'ka01690_header.id',
    cur_prc     DECIMAL(20,2)          COMMENT '현재가',
    stk_cd      VARCHAR(20)            COMMENT '종목코드',
    stk_nm      VARCHAR(100)           COMMENT '종목명',
    rmnd_qty    DECIMAL(20,4)          COMMENT '보유 수량',
    buy_uv      DECIMAL(20,2)          COMMENT '매입 단가',
    buy_wght    DECIMAL(10,4)          COMMENT '매수비중',
    evltv_prft  DECIMAL(20,2)          COMMENT '평가손익',
    prft_rt     DECIMAL(10,4)          COMMENT '수익률',
    evlt_amt    DECIMAL(20,2)          COMMENT '평가금액',
    evlt_wght   DECIMAL(10,4)          COMMENT '평가비중',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='ka01690 일별잔고수익률 리스트';

-- ------------------------------------------------------------
-- ka10072 : 일자별종목별실현손익 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10072 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결량',
    buy_uv          DECIMAL(20,2)          COMMENT '매입단가',
    cntr_pric       DECIMAL(20,2)          COMMENT '체결가',
    tdy_sel_pl      DECIMAL(20,2)          COMMENT '당일매도손익',
    pl_rt           DECIMAL(10,4)          COMMENT '손익율',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    wthd_alowa      DECIMAL(20,2)          COMMENT '인출가능금액',
    loan_dt         VARCHAR(8)             COMMENT '대출일',
    crd_tp          VARCHAR(10)            COMMENT '신용구분',
    stk_cd_1        VARCHAR(20)            COMMENT '종목코드1',
    tdy_sel_pl_1    DECIMAL(20,2)          COMMENT '당일매도손익1',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10072 일자별종목별실현손익';

-- ------------------------------------------------------------
-- ka10073 : 일자별종목별실현손익 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10073 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dt              VARCHAR(8)             COMMENT '일자',
    tdy_htssel_cmsn DECIMAL(20,2)          COMMENT '당일hts매도수수료',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결량',
    buy_uv          DECIMAL(20,2)          COMMENT '매입단가',
    cntr_pric       DECIMAL(20,2)          COMMENT '체결가',
    tdy_sel_pl      DECIMAL(20,2)          COMMENT '당일매도손익',
    pl_rt           DECIMAL(10,4)          COMMENT '손익율',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    wthd_alowa      DECIMAL(20,2)          COMMENT '인출가능금액',
    loan_dt         VARCHAR(8)             COMMENT '대출일',
    crd_tp          VARCHAR(10)            COMMENT '신용구분',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10073 일자별종목별실현손익';

-- ------------------------------------------------------------
-- ka10074 : 일자별실현손익 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10074_header (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tot_buy_amt     DECIMAL(20,2)          COMMENT '총매수금액',
    tot_sell_amt    DECIMAL(20,2)          COMMENT '총매도금액',
    rlzt_pl         DECIMAL(20,2)          COMMENT '실현손익',
    trde_cmsn       DECIMAL(20,2)          COMMENT '매매수수료',
    trde_tax        DECIMAL(20,2)          COMMENT '매매세금',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10074 일자별실현손익 헤더';

CREATE TABLE IF NOT EXISTS ka10074_dt_rlzt_pl (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL,
    dt              VARCHAR(8)             COMMENT '일자',
    buy_amt         DECIMAL(20,2)          COMMENT '매수금액',
    sell_amt        DECIMAL(20,2)          COMMENT '매도금액',
    tdy_sel_pl      DECIMAL(20,2)          COMMENT '당일매도손익',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='ka10074 일자별실현손익 리스트';

-- ------------------------------------------------------------
-- ka10075 : 미체결 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10075 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acnt_no         VARCHAR(20)            COMMENT '계좌번호',
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    mang_empno      VARCHAR(20)            COMMENT '관리사번',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    tsk_tp          VARCHAR(10)            COMMENT '업무구분',
    ord_stt         VARCHAR(20)            COMMENT '주문상태',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_pric        DECIMAL(20,2)          COMMENT '주문가격',
    oso_qty         DECIMAL(20,4)          COMMENT '미체결수량',
    cntr_tot_amt    DECIMAL(20,2)          COMMENT '체결누계금액',
    orig_ord_no     VARCHAR(20)            COMMENT '원주문번호',
    io_tp_nm        VARCHAR(20)            COMMENT '주문구분',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    tm              VARCHAR(6)             COMMENT '시간',
    cntr_no         VARCHAR(20)            COMMENT '체결번호',
    cntr_pric       DECIMAL(20,2)          COMMENT '체결가',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결량',
    cur_prc         DECIMAL(20,2)          COMMENT '현재가',
    sel_bid         DECIMAL(20,2)          COMMENT '매도호가',
    buy_bid         DECIMAL(20,2)          COMMENT '매수호가',
    unit_cntr_pric  DECIMAL(20,2)          COMMENT '단위체결가',
    unit_cntr_qty   DECIMAL(20,4)          COMMENT '단위체결량',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    ind_invsr       VARCHAR(10)            COMMENT '개인투자자',
    stex_tp         CHAR(1)                COMMENT '거래소구분(0:통합,1:KRX,2:NXT)',
    stex_tp_txt     VARCHAR(10)            COMMENT '거래소구분텍스트',
    sor_yn          CHAR(1)                COMMENT 'SOR여부(Y/N)',
    stop_pric       DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at),
    INDEX idx_ord_no (ord_no)
) COMMENT='ka10075 미체결';

-- ------------------------------------------------------------
-- ka10076 : 체결 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10076 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    io_tp_nm        VARCHAR(20)            COMMENT '주문구분',
    ord_pric        DECIMAL(20,2)          COMMENT '주문가격',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    cntr_pric       DECIMAL(20,2)          COMMENT '체결가',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결량',
    oso_qty         DECIMAL(20,4)          COMMENT '미체결수량',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    ord_stt         VARCHAR(20)            COMMENT '주문상태',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    orig_ord_no     VARCHAR(20)            COMMENT '원주문번호',
    ord_tm          VARCHAR(6)             COMMENT '주문시간',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    stex_tp         CHAR(1)                COMMENT '거래소구분',
    stex_tp_txt     VARCHAR(10)            COMMENT '거래소구분텍스트',
    sor_yn          CHAR(1)                COMMENT 'SOR여부',
    stop_pric       DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at),
    INDEX idx_ord_no (ord_no)
) COMMENT='ka10076 체결';

-- ------------------------------------------------------------
-- ka10077 : 당일실현손익 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10077_header (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tdy_rlzt_pl     DECIMAL(20,2)          COMMENT '당일실현손익',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10077 당일실현손익 헤더';

CREATE TABLE IF NOT EXISTS ka10077_tdy_rlzt_pl_dtl (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL,
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결량',
    buy_uv          DECIMAL(20,2)          COMMENT '매입단가',
    cntr_pric       DECIMAL(20,2)          COMMENT '체결가',
    tdy_sel_pl      DECIMAL(20,2)          COMMENT '당일매도손익',
    pl_rt           DECIMAL(10,4)          COMMENT '손익율',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='ka10077 당일실현손익 상세';

-- ------------------------------------------------------------
-- ka10085 : 계좌수익률 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10085 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dt              VARCHAR(8)             COMMENT '일자',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cur_prc         DECIMAL(20,2)          COMMENT '현재가',
    pur_pric        DECIMAL(20,2)          COMMENT '매입가',
    pur_amt         DECIMAL(20,2)          COMMENT '매입금액',
    rmnd_qty        DECIMAL(20,4)          COMMENT '보유수량',
    tdy_sel_pl      DECIMAL(20,2)          COMMENT '당일매도손익',
    tdy_trde_cmsn   DECIMAL(20,2)          COMMENT '당일매매수수료',
    tdy_trde_tax    DECIMAL(20,2)          COMMENT '당일매매세금',
    crd_tp          VARCHAR(10)            COMMENT '신용구분',
    loan_dt         VARCHAR(8)             COMMENT '대출일',
    setl_remn       DECIMAL(20,4)          COMMENT '결제잔고',
    clrn_alow_qty   DECIMAL(20,4)          COMMENT '청산가능수량',
    crd_amt         DECIMAL(20,2)          COMMENT '신용금액',
    crd_int         DECIMAL(20,2)          COMMENT '신용이자',
    expr_dt         VARCHAR(8)             COMMENT '만기일',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10085 계좌수익률';

-- ------------------------------------------------------------
-- ka10088 : 미체결분할주문리스트
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10088 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_pric        DECIMAL(20,2)          COMMENT '주문가격',
    osop_qty        DECIMAL(20,4)          COMMENT '미체결수량',
    io_tp_nm        VARCHAR(20)            COMMENT '주문구분',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    sell_tp         VARCHAR(10)            COMMENT '매도/수구분',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결량',
    ord_stt         VARCHAR(20)            COMMENT '주문상태',
    cur_prc         DECIMAL(20,2)          COMMENT '현재가',
    stex_tp         CHAR(1)                COMMENT '거래소구분',
    stex_tp_txt     VARCHAR(10)            COMMENT '거래소구분텍스트',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10088 미체결분할주문';

-- ------------------------------------------------------------
-- ka10170 : 당일매매일지 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ka10170_header (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tot_sell_amt    DECIMAL(20,2)          COMMENT '총매도금액',
    tot_buy_amt     DECIMAL(20,2)          COMMENT '총매수금액',
    tot_cmsn_tax    DECIMAL(20,2)          COMMENT '총수수료_세금',
    tot_exct_amt    DECIMAL(20,2)          COMMENT '총정산금액',
    tot_pl_amt      DECIMAL(20,2)          COMMENT '총손익금액',
    tot_prft_rt     DECIMAL(10,4)          COMMENT '총수익률',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='ka10170 당일매매일지 헤더';

CREATE TABLE IF NOT EXISTS ka10170_tdy_trde_diary (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL,
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    buy_avg_pric    DECIMAL(20,2)          COMMENT '매수평균가',
    buy_qty         DECIMAL(20,4)          COMMENT '매수수량',
    sel_avg_pric    DECIMAL(20,2)          COMMENT '매도평균가',
    sell_qty        DECIMAL(20,4)          COMMENT '매도수량',
    cmsn_alm_tax    DECIMAL(20,2)          COMMENT '수수료_제세금',
    pl_amt          DECIMAL(20,2)          COMMENT '손익금액',
    sell_amt        DECIMAL(20,2)          COMMENT '매도금액',
    buy_amt         DECIMAL(20,2)          COMMENT '매수금액',
    prft_rt         DECIMAL(10,4)          COMMENT '수익률',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='ka10170 당일매매일지 리스트';

-- ------------------------------------------------------------
-- kt00001 : 예수금 현황 (헤더 + 종목별예수금 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00001_header (
    id                          BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no                     VARCHAR(20)   NOT NULL,
    fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    entr                        DECIMAL(20,2)          COMMENT '예수금',
    profa_ch                    DECIMAL(20,2)          COMMENT '주식증거금현금',
    pymn_alow_amt               DECIMAL(20,2)          COMMENT '출금가능금액',
    ord_alow_amt                DECIMAL(20,2)          COMMENT '주문가능금액',
    d1_entra                    DECIMAL(20,2)          COMMENT 'd+1추정예수금',
    d2_entra                    DECIMAL(20,2)          COMMENT 'd+2추정예수금',
    ch_uncla                    DECIMAL(20,2)          COMMENT '현금미수금',
    nrpy_loan                   DECIMAL(20,2)          COMMENT '미상환융자금',
    loan_sum                    DECIMAL(20,2)          COMMENT '융자금합계',
    crd_grnt_rt                 DECIMAL(10,4)          COMMENT '신용담보비율',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00001 예수금 현황 헤더';

CREATE TABLE IF NOT EXISTS kt00001_stk_entr_prst (
    id                  BIGINT        NOT NULL AUTO_INCREMENT,
    header_id           BIGINT        NOT NULL,
    crnc_cd             VARCHAR(10)            COMMENT '통화코드',
    fx_entr             DECIMAL(20,2)          COMMENT '외화예수금',
    fc_krw_repl_evlta   DECIMAL(20,2)          COMMENT '원화대용평가금',
    fc_trst_profa       DECIMAL(20,2)          COMMENT '해외주식증거금',
    pymn_alow_amt_entr  DECIMAL(20,2)          COMMENT '출금가능금액(예수금)',
    pymn_alow_amt       DECIMAL(20,2)          COMMENT '출금가능금액',
    ord_alow_amt_entr   DECIMAL(20,2)          COMMENT '주문가능금액(예수금)',
    fc_uncla            DECIMAL(20,2)          COMMENT '외화미수(합계)',
    d1_fx_entr          DECIMAL(20,2)          COMMENT 'd+1외화예수금',
    d2_fx_entr          DECIMAL(20,2)          COMMENT 'd+2외화예수금',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt00001 종목별예수금';

-- ------------------------------------------------------------
-- kt00002 : 일별추정예탁자산현황 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00002 (
    id                          BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no                     VARCHAR(20)   NOT NULL,
    fetched_at                  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dt                          VARCHAR(8)             COMMENT '일자',
    entr                        DECIMAL(20,2)          COMMENT '예수금',
    grnt_use_amt                DECIMAL(20,2)          COMMENT '담보대출금',
    crd_loan                    DECIMAL(20,2)          COMMENT '신용융자금',
    ls_grnt                     DECIMAL(20,2)          COMMENT '대주담보금',
    repl_amt                    DECIMAL(20,2)          COMMENT '대용금',
    prsm_dpst_aset_amt          DECIMAL(20,2)          COMMENT '추정예탁자산',
    prsm_dpst_aset_amt_bncr_skip DECIMAL(20,2)         COMMENT '추정예탁자산수익증권제외',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00002 일별추정예탁자산현황';

-- ------------------------------------------------------------
-- kt00003 : 추정예탁자산
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00003 (
    id                  BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no             VARCHAR(20)   NOT NULL,
    fetched_at          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    prsm_dpst_aset_amt  DECIMAL(20,2)          COMMENT '추정예탁자산',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00003 추정예탁자산';

-- ------------------------------------------------------------
-- kt00004 : 종목별계좌평가현황 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00004_header (
    id                  BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no             VARCHAR(20)   NOT NULL,
    fetched_at          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acnt_nm             VARCHAR(100)           COMMENT '계좌명',
    brch_nm             VARCHAR(100)           COMMENT '지점명',
    entr                DECIMAL(20,2)          COMMENT '예수금',
    d2_entra            DECIMAL(20,2)          COMMENT 'D+2추정예수금',
    tot_est_amt         DECIMAL(20,2)          COMMENT '유가잔고평가액',
    aset_evlt_amt       DECIMAL(20,2)          COMMENT '예탁자산평가액',
    tot_pur_amt         DECIMAL(20,2)          COMMENT '총매입금액',
    prsm_dpst_aset_amt  DECIMAL(20,2)          COMMENT '추정예탁자산',
    tdy_lspft_amt       DECIMAL(20,2)          COMMENT '당일투자원금',
    tdy_lspft           DECIMAL(20,2)          COMMENT '당일투자손익',
    tdy_lspft_rt        DECIMAL(10,4)          COMMENT '당일손익율',
    lspft_rt            DECIMAL(10,4)          COMMENT '누적손익율',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00004 종목별계좌평가현황 헤더';

CREATE TABLE IF NOT EXISTS kt00004_stk_acnt_evlt_prst (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    header_id   BIGINT        NOT NULL,
    stk_cd      VARCHAR(20)            COMMENT '종목코드',
    stk_nm      VARCHAR(100)           COMMENT '종목명',
    rmnd_qty    DECIMAL(20,4)          COMMENT '보유수량',
    avg_prc     DECIMAL(20,2)          COMMENT '평균단가',
    cur_prc     DECIMAL(20,2)          COMMENT '현재가',
    evlt_amt    DECIMAL(20,2)          COMMENT '평가금액',
    pl_amt      DECIMAL(20,2)          COMMENT '손익금액',
    pl_rt       DECIMAL(10,4)          COMMENT '손익율',
    loan_dt     VARCHAR(8)             COMMENT '대출일',
    pur_amt     DECIMAL(20,2)          COMMENT '매입금액',
    setl_remn   DECIMAL(20,4)          COMMENT '결제잔고',
    tdy_buyq    DECIMAL(20,4)          COMMENT '금일매수수량',
    tdy_sellq   DECIMAL(20,4)          COMMENT '금일매도수량',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt00004 종목별계좌평가현황 리스트';

-- ------------------------------------------------------------
-- kt00005 : 종목별체결잔고 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00005_header (
    id                  BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no             VARCHAR(20)   NOT NULL,
    fetched_at          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    entr                DECIMAL(20,2)          COMMENT '예수금',
    pymn_alow_amt       DECIMAL(20,2)          COMMENT '출금가능금액',
    ord_alowa           DECIMAL(20,2)          COMMENT '주문가능현금',
    evlt_amt_tot        DECIMAL(20,2)          COMMENT '평가금액합계',
    tot_pl_tot          DECIMAL(20,2)          COMMENT '총손익합계',
    tot_pl_rt           DECIMAL(10,4)          COMMENT '총손익률',
    crd_grnt_rt         DECIMAL(10,4)          COMMENT '신용담보비율',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00005 종목별체결잔고 헤더';

CREATE TABLE IF NOT EXISTS kt00005_stk_cntr_remn (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    header_id   BIGINT        NOT NULL,
    crd_tp      VARCHAR(10)            COMMENT '신용구분',
    loan_dt     VARCHAR(8)             COMMENT '대출일',
    expr_dt     VARCHAR(8)             COMMENT '만기일',
    stk_cd      VARCHAR(20)            COMMENT '종목번호',
    stk_nm      VARCHAR(100)           COMMENT '종목명',
    setl_remn   DECIMAL(20,4)          COMMENT '결제잔고',
    cur_qty     DECIMAL(20,4)          COMMENT '현재잔고',
    cur_prc     DECIMAL(20,2)          COMMENT '현재가',
    buy_uv      DECIMAL(20,2)          COMMENT '매입단가',
    pur_amt     DECIMAL(20,2)          COMMENT '매입금액',
    evlt_amt    DECIMAL(20,2)          COMMENT '평가금액',
    evltv_prft  DECIMAL(20,2)          COMMENT '평가손익',
    pl_rt       DECIMAL(10,4)          COMMENT '손익률',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt00005 종목별체결잔고 리스트';

-- ------------------------------------------------------------
-- kt00007 : 계좌별주문체결내역상세 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00007 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    stk_cd          VARCHAR(20)            COMMENT '종목번호',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    crd_tp          VARCHAR(10)            COMMENT '신용구분',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_uv          DECIMAL(20,2)          COMMENT '주문단가',
    cnfm_qty        DECIMAL(20,4)          COMMENT '확인수량',
    acpt_tp         VARCHAR(10)            COMMENT '접수구분',
    rsrv_tp         VARCHAR(10)            COMMENT '반대여부',
    ord_tm          VARCHAR(6)             COMMENT '주문시간',
    ori_ord         VARCHAR(20)            COMMENT '원주문',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    io_tp_nm        VARCHAR(20)            COMMENT '주문구분',
    loan_dt         VARCHAR(8)             COMMENT '대출일',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결수량',
    cntr_uv         DECIMAL(20,2)          COMMENT '체결단가',
    ord_remnq       DECIMAL(20,4)          COMMENT '주문잔량',
    comm_ord_tp     VARCHAR(10)            COMMENT '통신구분',
    mdfy_cncl       VARCHAR(10)            COMMENT '정정취소',
    cnfm_tm         VARCHAR(6)             COMMENT '확인시간',
    dmst_stex_tp    VARCHAR(10)            COMMENT '국내거래소구분',
    cond_uv         DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at),
    INDEX idx_ord_no (ord_no)
) COMMENT='kt00007 계좌별주문체결내역상세';

-- ------------------------------------------------------------
-- kt00008 : 계좌별익일결제예정내역 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00008_header (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    trde_dt         VARCHAR(8)             COMMENT '매매일자',
    setl_dt         VARCHAR(8)             COMMENT '결제일자',
    sell_amt_sum    DECIMAL(20,2)          COMMENT '매도정산합',
    buy_amt_sum     DECIMAL(20,2)          COMMENT '매수정산합',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00008 익일결제예정내역 헤더';

CREATE TABLE IF NOT EXISTS kt00008_setl_prps (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    header_id   BIGINT        NOT NULL,
    seq         VARCHAR(10)            COMMENT '일련번호',
    stk_cd      VARCHAR(20)            COMMENT '종목번호',
    loan_dt     VARCHAR(8)             COMMENT '대출일',
    qty         DECIMAL(20,4)          COMMENT '수량',
    engg_amt    DECIMAL(20,2)          COMMENT '약정금액',
    cmsn        DECIMAL(20,2)          COMMENT '수수료',
    stk_nm      VARCHAR(100)           COMMENT '종목명',
    sell_tp     VARCHAR(10)            COMMENT '매도수구분',
    unp         DECIMAL(20,2)          COMMENT '단가',
    exct_amt    DECIMAL(20,2)          COMMENT '정산금액',
    trde_tax    DECIMAL(20,2)          COMMENT '거래세',
    crd_tp      VARCHAR(10)            COMMENT '신용구분',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt00008 익일결제예정내역 리스트';

-- ------------------------------------------------------------
-- kt00009 : 계좌별주문체결현황 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00009_header (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    sell_grntl_engg_amt DECIMAL(20,2)      COMMENT '매도약정금액',
    buy_engg_amt    DECIMAL(20,2)          COMMENT '매수약정금액',
    engg_amt        DECIMAL(20,2)          COMMENT '약정금액',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00009 계좌별주문체결현황 헤더';

CREATE TABLE IF NOT EXISTS kt00009_acnt_ord_cntr_prst (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL,
    stk_bond_tp     VARCHAR(10)            COMMENT '주식채권구분',
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    stk_cd          VARCHAR(20)            COMMENT '종목번호',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    io_tp_nm        VARCHAR(20)            COMMENT '주문유형구분',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_uv          DECIMAL(20,2)          COMMENT '주문단가',
    cnfm_qty        DECIMAL(20,4)          COMMENT '확인수량',
    orig_ord_no     VARCHAR(20)            COMMENT '원주문번호',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결수량',
    cntr_uv         DECIMAL(20,2)          COMMENT '체결단가',
    cntr_tm         VARCHAR(6)             COMMENT '체결시간',
    dmst_stex_tp    VARCHAR(10)            COMMENT '국내거래소구분',
    cond_uv         DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt00009 계좌별주문체결현황 리스트';

-- ------------------------------------------------------------
-- kt00015 : 위탁종합거래내역 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00015 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    trde_dt         VARCHAR(8)             COMMENT '거래일자',
    trde_no         VARCHAR(20)            COMMENT '거래번호',
    rmrk_nm         VARCHAR(100)           COMMENT '적요명',
    crd_deal_tp_nm  VARCHAR(20)            COMMENT '신용거래구분명',
    exct_amt        DECIMAL(20,2)          COMMENT '정산금액',
    entra_remn      DECIMAL(20,2)          COMMENT '예수금잔고',
    crnc_cd         VARCHAR(10)            COMMENT '통화코드',
    trde_ocr_tp     CHAR(1)                COMMENT '거래종류구분',
    trde_kind_nm    VARCHAR(50)            COMMENT '거래종류명',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    trde_amt        DECIMAL(20,2)          COMMENT '거래금액',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    trde_qty_jwa_cnt DECIMAL(20,4)         COMMENT '거래수량/좌수',
    cmsn            DECIMAL(20,2)          COMMENT '수수료',
    proc_tm         VARCHAR(6)             COMMENT '처리시간',
    isin_cd         VARCHAR(20)            COMMENT 'ISIN코드',
    trde_unit       DECIMAL(20,6)          COMMENT '거래단가/환율',
    loan_dt         VARCHAR(8)             COMMENT '대출일',
    io_tp           VARCHAR(10)            COMMENT '입출구분',
    io_tp_nm        VARCHAR(20)            COMMENT '입출구분명',
    orig_deal_no    VARCHAR(20)            COMMENT '원거래번호',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at),
    INDEX idx_trde_dt (trde_dt)
) COMMENT='kt00015 위탁종합거래내역';

-- ------------------------------------------------------------
-- kt00018 : 계좌평가잔고개별합산 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt00018_header (
    id                  BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no             VARCHAR(20)   NOT NULL,
    fetched_at          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tot_pur_amt         DECIMAL(20,2)          COMMENT '총매입금액',
    tot_evlt_amt        DECIMAL(20,2)          COMMENT '총평가금액',
    tot_evlt_pl         DECIMAL(20,2)          COMMENT '총평가손익금액',
    tot_prft_rt         DECIMAL(10,4)          COMMENT '총수익률(%)',
    prsm_dpst_aset_amt  DECIMAL(20,2)          COMMENT '추정예탁자산',
    tot_loan_amt        DECIMAL(20,2)          COMMENT '총대출금',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt00018 계좌평가잔고 헤더';

CREATE TABLE IF NOT EXISTS kt00018_acnt_evlt_remn (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL,
    stk_cd          VARCHAR(20)            COMMENT '종목번호',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    evltv_prft      DECIMAL(20,2)          COMMENT '평가손익',
    prft_rt         DECIMAL(10,4)          COMMENT '수익률(%)',
    pur_pric        DECIMAL(20,2)          COMMENT '매입가',
    pred_close_pric DECIMAL(20,2)          COMMENT '전일종가',
    rmnd_qty        DECIMAL(20,4)          COMMENT '보유수량',
    trde_able_qty   DECIMAL(20,4)          COMMENT '매매가능수량',
    cur_prc         DECIMAL(20,2)          COMMENT '현재가',
    pur_amt         DECIMAL(20,2)          COMMENT '매입금액',
    evlt_amt        DECIMAL(20,2)          COMMENT '평가금액',
    tax             DECIMAL(20,2)          COMMENT '세금',
    poss_rt         DECIMAL(10,4)          COMMENT '보유비중(%)',
    crd_tp          VARCHAR(10)            COMMENT '신용구분',
    crd_tp_nm       VARCHAR(20)            COMMENT '신용구분명',
    crd_loan_dt     VARCHAR(8)             COMMENT '대출일',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt00018 계좌평가잔고 리스트';

-- ------------------------------------------------------------
-- kt50020 : 금현물계좌평가현황 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50020_header (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no     VARCHAR(20)   NOT NULL,
    fetched_at  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tot_entr    DECIMAL(20,2)          COMMENT '예수금',
    net_entr    DECIMAL(20,2)          COMMENT '추정예수금',
    tot_est_amt DECIMAL(20,2)          COMMENT '잔고평가액',
    net_amt     DECIMAL(20,2)          COMMENT '예탁자산평가액',
    tot_book_amt2 DECIMAL(20,2)        COMMENT '총매입금액',
    tot_dep_amt DECIMAL(20,2)          COMMENT '추정예탁자산',
    paym_alowa  DECIMAL(20,2)          COMMENT '출금가능금액',
    pl_amt      DECIMAL(20,2)          COMMENT '실현손익',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt50020 금현물계좌평가 헤더';

CREATE TABLE IF NOT EXISTS kt50020_gold_acnt_evlt_prst (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    header_id   BIGINT        NOT NULL,
    stk_cd      VARCHAR(20)            COMMENT '종목코드',
    stk_nm      VARCHAR(100)           COMMENT '종목명',
    real_qty    DECIMAL(20,4)          COMMENT '보유수량',
    avg_prc     DECIMAL(20,2)          COMMENT '평균단가',
    cur_prc     DECIMAL(20,2)          COMMENT '현재가',
    est_amt     DECIMAL(20,2)          COMMENT '평가금액',
    est_lspft   DECIMAL(20,2)          COMMENT '손익금액',
    est_ratio   DECIMAL(10,4)          COMMENT '손익율',
    book_amt2   DECIMAL(20,2)          COMMENT '매입금액',
    qty         DECIMAL(20,4)          COMMENT '결제잔고',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt50020 금현물계좌평가 리스트';

-- ------------------------------------------------------------
-- kt50021 : 금현물예수금
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50021 (
    id                  BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no             VARCHAR(20)   NOT NULL,
    fetched_at          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    entra               DECIMAL(20,2)          COMMENT '예수금',
    prsm_entra          DECIMAL(20,2)          COMMENT '추정예수금',
    pymn_alow_amt       DECIMAL(20,2)          COMMENT '출금가능금액',
    ord_alow_amt        DECIMAL(20,2)          COMMENT '주문가능금액',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt50021 금현물예수금';

-- ------------------------------------------------------------
-- kt50030 : 금현물계좌별주문체결현황 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50030 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stk_bond_tp     VARCHAR(10)            COMMENT '주식채권구분',
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    stk_cd          VARCHAR(20)            COMMENT '상품코드',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    io_tp_nm        VARCHAR(20)            COMMENT '주문유형구분',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_uv          DECIMAL(20,2)          COMMENT '주문단가',
    orig_ord_no     VARCHAR(20)            COMMENT '원주문번호',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결수량',
    cntr_uv         DECIMAL(20,2)          COMMENT '체결단가',
    ord_remnq       DECIMAL(20,4)          COMMENT '미체결수량',
    dmst_stex_tp    VARCHAR(10)            COMMENT '국내거래소구분',
    cond_uv         DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt50030 금현물주문체결현황';

-- ------------------------------------------------------------
-- kt50031 : 금현물주문체결내역상세 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50031 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    stk_cd          VARCHAR(20)            COMMENT '종목번호',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    crd_tp          VARCHAR(10)            COMMENT '신용구분',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_uv          DECIMAL(20,2)          COMMENT '주문단가',
    ord_tm          VARCHAR(6)             COMMENT '주문시간',
    ori_ord         VARCHAR(20)            COMMENT '원주문',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    io_tp_nm        VARCHAR(20)            COMMENT '주문구분',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결수량',
    cntr_uv         DECIMAL(20,2)          COMMENT '체결단가',
    cnfm_tm         VARCHAR(6)             COMMENT '확인시간',
    dmst_stex_tp    VARCHAR(10)            COMMENT '국내거래소구분',
    cond_uv         DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt50031 금현물주문체결내역상세';

-- ------------------------------------------------------------
-- kt50032 : 금현물거래내역 (헤더 + 리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50032_header (
    id          BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no     VARCHAR(20)   NOT NULL,
    fetched_at  DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acnt_print  VARCHAR(20)            COMMENT '계좌번호 출력용',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt50032 금현물거래내역 헤더';

CREATE TABLE IF NOT EXISTS kt50032_gold_trde_hist (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    header_id       BIGINT        NOT NULL,
    deal_dt         VARCHAR(8)             COMMENT '거래일자',
    deal_no         VARCHAR(20)            COMMENT '거래번호',
    rmrk_nm         VARCHAR(100)           COMMENT '적요명',
    deal_qty        DECIMAL(20,4)          COMMENT '거래수량',
    gold_spot_vat   DECIMAL(20,2)          COMMENT '금현물부가가치세',
    exct_amt        DECIMAL(20,2)          COMMENT '정산금액',
    entra_remn      DECIMAL(20,2)          COMMENT '예수금잔고',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    uv_exrt         DECIMAL(20,6)          COMMENT '거래단가',
    cmsn            DECIMAL(20,2)          COMMENT '수수료',
    spot_remn       DECIMAL(20,4)          COMMENT '현물잔고',
    stk_cd          VARCHAR(20)            COMMENT '종목코드',
    deal_amt        DECIMAL(20,2)          COMMENT '거래금액',
    cntr_dt         VARCHAR(8)             COMMENT '체결일',
    PRIMARY KEY (id),
    INDEX idx_header (header_id)
) COMMENT='kt50032 금현물거래내역 리스트';

-- ------------------------------------------------------------
-- kt50075 : 금현물계좌별주문미체결현황 (리스트)
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS kt50075 (
    id              BIGINT        NOT NULL AUTO_INCREMENT,
    acct_no         VARCHAR(20)   NOT NULL,
    fetched_at      DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    stk_bond_tp     VARCHAR(10)            COMMENT '주식채권구분',
    ord_no          VARCHAR(20)            COMMENT '주문번호',
    stk_cd          VARCHAR(20)            COMMENT '상품코드',
    trde_tp         VARCHAR(10)            COMMENT '매매구분',
    io_tp_nm        VARCHAR(20)            COMMENT '주문유형구분',
    ord_qty         DECIMAL(20,4)          COMMENT '주문수량',
    ord_uv          DECIMAL(20,2)          COMMENT '주문단가',
    orig_ord_no     VARCHAR(20)            COMMENT '원주문번호',
    stk_nm          VARCHAR(100)           COMMENT '종목명',
    crd_deal_tp     VARCHAR(10)            COMMENT '신용거래구분',
    cntr_qty        DECIMAL(20,4)          COMMENT '체결수량',
    cntr_uv         DECIMAL(20,2)          COMMENT '체결단가',
    ord_remnq       DECIMAL(20,4)          COMMENT '미체결수량',
    dmst_stex_tp    VARCHAR(10)            COMMENT '국내거래소구분',
    cond_uv         DECIMAL(20,2)          COMMENT '스톱가',
    PRIMARY KEY (id),
    INDEX idx_acct_fetched (acct_no, fetched_at)
) COMMENT='kt50075 금현물주문미체결현황';
