"""주식 마스터 DB 저장 모듈.

각 시장 DataFrame을 해당 DB 테이블에 TRUNCATE + bulk INSERT한다.
"""

from __future__ import annotations

import math
from typing import Any

import pandas as pd
import pymysql.connections

from db import get_conn
from logger import db_logger


# ── 값 변환 헬퍼 ─────────────────────────────────────────────────────────

def _s(val: Any) -> str:
    """NaN/None → 빈 문자열, 그 외 → str."""
    if val is None:
        return ""
    try:
        if math.isnan(float(val)):  # type: ignore[arg-type]
            return ""
    except (TypeError, ValueError):
        pass
    return str(val).strip()


def _n(val: Any) -> int | float:
    """NaN/None/변환불가 → 0, 그 외 → 숫자."""
    try:
        v = float(val)  # type: ignore[arg-type]
        if math.isnan(v):
            return 0
        return v
    except (TypeError, ValueError):
        return 0


# ── bulk INSERT 공통 ──────────────────────────────────────────────────────

def _bulk_insert(
    conn: pymysql.connections.Connection,
    table: str,
    cols: list[str],
    rows: list[tuple],
) -> int:
    """테이블을 TRUNCATE한 뒤 rows를 일괄 INSERT하고 삽입 행 수를 반환한다."""
    if not rows:
        db_logger.info("db save table=%s rows=%d", table, 0)
        return 0
    placeholders = ", ".join(["%s"] * len(cols))
    col_list = ", ".join(cols)
    sql = f"INSERT IGNORE INTO {table} ({col_list}) VALUES ({placeholders})"
    inserted_rows = 0
    with conn.cursor() as cur:
        cur.execute(f"TRUNCATE TABLE {table}")
        cur.executemany(sql, rows)
        inserted_rows = cur.rowcount
    conn.commit()
    ignored_rows = len(rows) - inserted_rows
    db_logger.info(
        "db save table=%s rows=%d requested=%d ignored=%d",
        table,
        inserted_rows,
        len(rows),
        ignored_rows,
    )
    return inserted_rows


# ── 시장별 save 함수 ──────────────────────────────────────────────────────

def save_kospi(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_kospi"
    COLS = [
        "short_code", "standard_code", "stock_name_kr", "group_code",
        "market_cap_size_code", "index_sector_large", "index_sector_mid",
        "index_sector_small", "base_price", "regular_lot_size",
        "offhour_lot_size", "trade_halt_yn", "managed_issue_yn",
        "market_warning_code", "margin_rate", "prev_volume", "par_value",
        "listing_date", "listed_shares_thousand", "roe", "base_yyyymm",
        "prev_market_cap_100m",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글명")),
            _s(d.get("그룹코드")),
            _s(d.get("시가총액규모")),
            _s(d.get("지수업종대분류")),
            _s(d.get("지수업종중분류")),
            _s(d.get("지수업종소분류")),
            _n(d.get("기준가")),
            _n(d.get("매매수량단위")),
            _n(d.get("시간외수량단위")),
            _s(d.get("거래정지")),
            _s(d.get("관리종목")),
            _s(d.get("시장경고")),
            _n(d.get("증거금비율")),
            _n(d.get("전일거래량")),
            _n(d.get("액면가")),
            _s(d.get("상장일자")),
            _n(d.get("상장주수")),
            _n(d.get("ROE")),
            _s(d.get("기준년월")),
            _n(d.get("시가총액")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_kosdaq(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_kosdaq"
    COLS = [
        "short_code", "standard_code", "stock_name_kr", "security_group_code",
        "market_cap_size_code", "index_sector_large", "index_sector_mid",
        "index_sector_small", "venture_yn", "kosdaq150_yn", "base_price", "regular_lot_size",
        "offhour_lot_size", "trade_halt_yn", "managed_issue_yn",
        "market_warning_code", "margin_rate",
        "listing_date", "listed_shares_thousand", "roe", "base_yyyymm",
        "prev_market_cap_100m",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글명")),
            _s(d.get("그룹코드")),
            _s(d.get("시가총액규모")),
            _s(d.get("지수업종대분류")),
            _s(d.get("지수업종중분류")),
            _s(d.get("지수업종소분류")),
            _s(d.get("벤처기업여부") or d.get("벤처기업") or "N"),
            _s(d.get("KOSDAQ150")),
            _n(d.get("기준가")),
            _n(d.get("매매수량단위")),
            _n(d.get("시간외수량단위")),
            _s(d.get("거래정지")),
            _s(d.get("관리종목")),
            _s(d.get("시장경고")),
            _n(d.get("증거금비율")),
            _s(d.get("상장일자")),
            _n(d.get("상장주수")),
            _n(d.get("ROE")),
            _s(d.get("기준년월")),
            _n(d.get("시가총액")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_konex(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_konex"
    COLS = [
        "short_code", "standard_code", "stock_name_kr",
        "base_price", "regular_lot_size", "offhour_lot_size",
        "trade_halt_yn", "managed_issue_yn", "market_warning_code",
        "margin_rate", "listing_date", "listed_shares_thousand",
        "roe", "base_yyyymm", "prev_market_cap_100m",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글종목명")),
            _n(d.get("기준가")),
            _n(d.get("매매수량단위")),
            _n(d.get("시간외수량단위")),
            _s(d.get("거래정지")),
            _s(d.get("관리종목")),
            _s(d.get("시장경고")),
            _n(d.get("증거금비율")),
            _s(d.get("상장일자")),
            _n(d.get("상장주수")),
            _n(d.get("ROE")),
            _s(d.get("기준년월")),
            _n(d.get("시가총액")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_domestic_elw(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_domestic_elw"
    COLS = [
        "short_code", "standard_code", "stock_name_kr",
        "elw_right_type", "knockout_barrier_price", "basket_yn",
        "underlying_code1", "underlying_code2", "underlying_code3",
        "underlying_code4", "underlying_code5",
        "issuer_name_kr", "issuer_code", "strike_price",
        "last_trading_date", "remain_days", "right_type_code",
        "payment_date", "prev_market_cap_100m", "listed_shares_thousand",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글종목명")),
            _s(d.get("ELW권리형태")),
            _n(d.get("ELW조기종료발생기준가격")),
            _s(d.get("바스켓여부")),
            _s(d.get("기초자산코드1")),
            _s(d.get("기초자산코드2")),
            _s(d.get("기초자산코드3")),
            _s(d.get("기초자산코드4")),
            _s(d.get("기초자산코드5")),
            _s(d.get("발행사한글종목명")),
            _s(d.get("발행사코드")),
            _n(d.get("행사가")),
            _s(d.get("최종거래일")),
            _n(d.get("잔존일수")),
            _s(d.get("권리유형구분코드")),
            _s(d.get("지급일")),
            _n(d.get("전일시가총액(억)")),
            _n(d.get("상장주수(천)")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def _save_future_base(
    df: pd.DataFrame,
    conn: pymysql.connections.Connection,
    table: str,
    has_atm: bool = True,
    has_month: bool = True,
) -> int:
    """지수/주식선물옵션 공통 저장 (atm_flag, month_code 유무 파라미터화)."""
    if has_atm and has_month:
        COLS = [
            "product_type", "short_code", "standard_code", "stock_name_kr",
            "atm_flag", "strike_price", "month_code",
            "underlying_short_code", "underlying_name",
        ]
    elif has_atm and not has_month:
        COLS = [
            "product_type", "short_code", "standard_code", "stock_name_kr",
            "atm_flag", "strike_price",
            "underlying_short_code", "underlying_name",
        ]
    elif not has_atm and has_month:
        COLS = [
            "product_type", "short_code", "standard_code", "stock_name_kr",
            "strike_price", "month_code",
            "underlying_short_code", "underlying_name",
        ]
    else:
        COLS = [
            "product_type", "short_code", "standard_code", "stock_name_kr",
            "strike_price",
            "underlying_short_code", "underlying_name",
        ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        row: list = [
            _s(d.get("상품종류")),
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글종목명")),
        ]
        if has_atm:
            row.append(_s(d.get("ATM구분")))
        row.append(_n(d.get("행사가")))
        if has_month:
            row.append(_s(d.get("월물구분코드")))
        row.append(_s(d.get("기초자산단축코드")))
        row.append(_s(d.get("기초자산명")))
        rows.append(tuple(row))
    return _bulk_insert(conn, table, COLS, rows)


def save_index_future(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    return _save_future_base(df, conn, "isw_mst_domestic_index_future", has_atm=True, has_month=True)


def save_stock_future(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    return _save_future_base(df, conn, "isw_mst_domestic_stock_future", has_atm=True, has_month=True)


def save_cme_future(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_domestic_cme_future"
    COLS = [
        "product_type", "short_code", "standard_code", "stock_name_kr",
        "strike_price", "underlying_short_code", "underlying_name",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("상품종류")),
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글종목명")),
            _n(d.get("행사가")),
            _s(d.get("기초자산단축코드")),
            _s(d.get("기초자산명")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_commodity_future(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_domestic_commodity_future"
    COLS = [
        "product_group", "product_type", "short_code", "standard_code",
        "stock_name_kr", "month_code", "underlying_short_code", "underlying_name",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("상품구분")),
            _s(d.get("상품종류")),
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글종목명")),
            _s(d.get("월물구분코드")),
            _s(d.get("기초자산단축코드")),
            _s(d.get("기초자산명")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_eurex_option(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_domestic_eurex_option"
    COLS = [
        "product_type", "short_code", "standard_code", "stock_name_kr",
        "atm_flag", "strike_price", "underlying_short_code", "underlying_name",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("상품종류")),
            _s(d.get("단축코드")),
            _s(d.get("표준코드")),
            _s(d.get("한글종목명")),
            _s(d.get("ATM구분")),
            _n(d.get("행사가")),
            _s(d.get("기초자산단축코드")),
            _s(d.get("기초자산명")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_domestic_bond(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_domestic_bond"
    COLS = [
        "bond_type", "bond_class_code", "standard_code", "bond_name",
        "bond_interest_class_code", "listing_date", "issue_date", "redemption_date",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("유형")),
            _s(d.get("채권분류코드")),
            _s(d.get("표준코드")),
            _s(d.get("종목명")),
            _s(d.get("채권이자분류코드")),
            _s(d.get("상장일")),
            _s(d.get("발행일")),
            _s(d.get("상환일")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_overseas_stock(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_overseas_stock"
    COLS = [
        "national_code", "exchange_id", "exchange_code", "exchange_name",
        "symbol", "realtime_symbol", "stock_name_kr", "stock_name_en",
        "security_type", "currency", "base_price",
        "bid_order_size", "ask_order_size",
        "market_start_hhmm", "market_end_hhmm",
        "dr_yn", "dr_national_code", "industry_code",
        "index_component_yn", "tick_size_type", "etp_category_code",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("국가코드")),
            _s(d.get("거래소ID")),
            _s(d.get("거래소코드")),
            _s(d.get("거래소명")),
            _s(d.get("심볼")),
            _s(d.get("실시간심볼")),
            _s(d.get("한글명")),
            _s(d.get("영문명")),
            _s(d.get("증권유형")),
            _s(d.get("통화")),
            _n(d.get("기준가격")),
            _n(d.get("매수호가단위")),
            _n(d.get("매도호가단위")),
            _s(d.get("시장시작시간(HHMM)")),
            _s(d.get("시장종료시간(HHMM)")),
            _s(d.get("DR여부(Y/N)")),
            _s(d.get("DR국가코드")),
            _s(d.get("업종분류코드")),
            _s(d.get("지수구성종목존재여부")),
            _s(d.get("틱사이즈Type")),
            _s(d.get("구분코드")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_overseas_index(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_overseas_index"
    COLS = [
        "category_code", "symbol", "stock_name_en", "stock_name_kr",
        "issue_industry_code", "dow30_component_yn", "nasdaq100_component_yn",
        "sp500_component_yn", "exchange_code", "national_code",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("구분코드")),
            _s(d.get("심볼")),
            _s(d.get("영문명")),
            _s(d.get("한글명")),
            _s(d.get("종목업종코드")),
            _s(d.get("다우30편입여부")),
            _s(d.get("나스닥100편입여부")),
            _s(d.get("SP500편입여부")),
            _s(d.get("거래소코드")),
            _s(d.get("국가구분코드")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


def save_overseas_future(df: pd.DataFrame, conn: pymysql.connections.Connection) -> int:
    TABLE = "isw_mst_overseas_future"
    COLS = [
        "instrument_code", "auto_orderable_yn", "auto_twap_orderable_yn",
        "auto_macro_orderable_yn", "instrument_name_kr",
        "exchange_code", "item_code", "item_type",
        "output_decimals", "calc_decimals",
        "tick_size", "tick_value", "contract_size",
        "price_radix", "conversion_multiplier",
        "front_month_yn", "near_month_yn",
        "spread_yn", "spread_leg1_yn", "sub_exchange_code",
    ]
    rows = []
    for r in df.itertuples(index=False):
        d = r._asdict()
        rows.append((
            _s(d.get("종목코드")),
            _s(d.get("서버자동주문가능여부")),
            _s(d.get("TWAP가능여부")),
            _s(d.get("경제지표주문가능여부")),
            _s(d.get("종목한글명")),
            _s(d.get("거래소코드")),
            _s(d.get("품목코드")),
            _s(d.get("품목종류")),
            _n(d.get("출력소수점")),
            _n(d.get("계산소수점")),
            _n(d.get("틱사이즈")),
            _n(d.get("틱가치")),
            _n(d.get("계약크기")),
            _s(d.get("가격표시진법")),
            _n(d.get("환산승수")),
            _s(d.get("최다월물여부")),
            _s(d.get("최근월물여부")),
            _s(d.get("스프레드여부")),
            _s(d.get("스프레드기준LEG1여부")),
            _s(d.get("서브거래소코드")),
        ))
    return _bulk_insert(conn, TABLE, COLS, rows)


# ── market key → save 함수 매핑 ───────────────────────────────────────────

MARKET_SAVE_FN: dict[str, Any] = {
    "KOSPI": save_kospi,
    "KOSDAQ": save_kosdaq,
    "KONEX": save_konex,
    "국내ELW": save_domestic_elw,
    "지수선물옵션": save_index_future,
    "주식선물옵션": save_stock_future,
    "CME야간선물": save_cme_future,
    "상품선물옵션": save_commodity_future,
    "EUREX야간옵션": save_eurex_option,
    "장내채권": save_domestic_bond,
    "해외주식": save_overseas_stock,
    "해외주식지수": save_overseas_index,
    "해외선물옵션": save_overseas_future,
}
