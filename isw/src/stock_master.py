"""종목 마스터 파일 다운로드 모듈

키움증권 마스터 파일 서버에서 각 시장별 종목 마스터를 내려받아
isw/mst/ 폴더에 CSV로 저장한다.
"""
from __future__ import annotations

import os
import ssl
import tempfile
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
from logger import error_logger

# ── 저장 경로 ───────────────────────────────────────────────────────────
MST_DIR = Path(__file__).resolve().parent.parent / "mst"
_BASE_URL = "https://new.real.download.dws.co.kr/common/master/"


def _ensure_mst_dir() -> None:
    MST_DIR.mkdir(parents=True, exist_ok=True)


def _download_zip(url: str, tmp_dir: str, zip_name: str, mst_name: str) -> str:
    """URL에서 zip 파일을 내려받아 tmp_dir 에 압축 해제하고 mst 파일 경로를 반환한다."""
    ssl._create_default_https_context = ssl._create_unverified_context
    zip_path = os.path.join(tmp_dir, zip_name)
    urllib.request.urlretrieve(url, zip_path)
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(tmp_dir)
    return os.path.join(tmp_dir, mst_name)


def _result(market: str, filename: str, rows: int) -> dict[str, Any]:
    return {
        "market": market,
        "file": filename,
        "rows": rows,
        "savedAt": datetime.now(timezone.utc).isoformat(),
    }


# ── 1. KOSPI ─────────────────────────────────────────────────────────────
def download_kospi() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "kospi_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "kospi_code.mst.zip", tmp, "kospi_code.zip", "kospi_code.mst"
        )
        tmp_p1 = os.path.join(tmp, "p1.tmp")
        tmp_p2 = os.path.join(tmp, "p2.tmp")
        with open(mst_path, mode="r", encoding="cp949") as f, \
             open(tmp_p1, mode="w", encoding="utf-8") as wf1, \
             open(tmp_p2, mode="w", encoding="utf-8") as wf2:
            for row in f:
                rf1 = row[: len(row) - 228]
                wf1.write(rf1[0:9].rstrip() + "," + rf1[9:21].rstrip() + "," + rf1[21:].strip() + "\n")
                wf2.write(row[-228:])

        df1 = pd.read_csv(tmp_p1, header=None, names=["단축코드", "표준코드", "한글명"], encoding="utf-8")
        field_specs = [2, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 9, 5, 5, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 1, 3, 12,
                       12, 8, 15, 21, 2, 7, 1, 1, 1, 1, 1, 9, 9, 9, 5, 9, 8, 9, 3, 1, 1, 1]
        part2_columns = [
            "그룹코드", "시가총액규모", "지수업종대분류", "지수업종중분류", "지수업종소분류",
            "제조업", "저유동성", "지배구조지수종목", "KOSPI200섹터업종", "KOSPI100",
            "KOSPI50", "KRX", "ETP", "ELW발행", "KRX100", "KRX자동차", "KRX반도체",
            "KRX바이오", "KRX은행", "SPAC", "KRX에너지화학", "KRX철강", "단기과열",
            "KRX미디어통신", "KRX건설", "Non1", "KRX증권", "KRX선박", "KRX섹터보험",
            "KRX섹터운송", "SRI", "기준가", "매매수량단위", "시간외수량단위", "거래정지",
            "정리매매", "관리종목", "시장경고", "경고예고", "불성실공시", "우회상장",
            "락구분", "액면변경", "증자구분", "증거금비율", "신용가능", "신용기간",
            "전일거래량", "액면가", "상장일자", "상장주수", "자본금", "결산월",
            "공모가", "우선주", "공매도과열", "이상급등", "KRX300", "KOSPI",
            "매출액", "영업이익", "경상이익", "당기순이익", "ROE", "기준년월",
            "시가총액", "그룹사코드", "회사신용한도초과", "담보대출가능", "대주가능",
        ]
        df2 = pd.read_fwf(tmp_p2, widths=field_specs, names=part2_columns, encoding="utf-8")
        df = pd.concat([df1, df2], axis=1)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("KOSPI", out_path.name, len(df))


# ── 2. KOSDAQ ────────────────────────────────────────────────────────────
def download_kosdaq() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "kosdaq_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "kosdaq_code.mst.zip", tmp, "kosdaq_code.zip", "kosdaq_code.mst"
        )
        tmp_p1 = os.path.join(tmp, "p1.tmp")
        tmp_p2 = os.path.join(tmp, "p2.tmp")
        with open(mst_path, mode="r", encoding="cp949") as f, \
             open(tmp_p1, mode="w", encoding="utf-8") as wf1, \
             open(tmp_p2, mode="w", encoding="utf-8") as wf2:
            for row in f:
                rf1 = row[: len(row) - 222]
                wf1.write(rf1[0:9].rstrip() + "," + rf1[9:21].rstrip() + "," + rf1[21:].strip() + "\n")
                wf2.write(row[-222:])

        df1 = pd.read_csv(tmp_p1, header=None, names=["단축코드", "표준코드", "한글명"], encoding="utf-8")
        field_specs = [2, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 9, 5, 5, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 1, 3, 12,
                       12, 8, 15, 21, 2, 7, 1, 1, 1, 1, 1, 9, 9, 9, 5, 9, 8, 9, 3, 1, 1, 1]
        part2_columns = [
            "그룹코드", "시가총액규모", "지수업종대분류", "지수업종중분류", "지수업종소분류",
            "제조업", "저유동성", "지배구조지수종목", "KOSDAQ섹터업종", "KOSDAQ100",
            "KOSDAQ150", "KRX", "ETP", "ELW발행", "KRX100", "KRX자동차", "KRX반도체",
            "KRX바이오", "KRX은행", "SPAC", "KRX에너지화학", "KRX철강", "단기과열",
            "KRX미디어통신", "KRX건설", "Non1", "KRX증권", "KRX선박", "KRX섹터보험",
            "KRX섹터운송", "SRI", "기준가", "매매수량단위", "시간외수량단위", "거래정지",
            "정리매매", "관리종목", "시장경고", "경고예고", "불성실공시", "우회상장",
            "락구분", "액면변경", "증자구분", "증거금비율", "신용가능", "신용기간",
            "전일거래량", "액면가", "상장일자", "상장주수", "자본금", "결산월",
            "공모가", "우선주", "공매도과열", "이상급등", "KRX300", "KOSDAQ",
            "매출액", "영업이익", "경상이익", "당기순이익", "ROE", "기준년월",
            "시가총액", "그룹사코드", "회사신용한도초과", "담보대출가능", "대주가능",
        ]
        df2 = pd.read_fwf(tmp_p2, widths=field_specs, names=part2_columns, encoding="utf-8")
        df = pd.concat([df1, df2], axis=1)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("KOSDAQ", out_path.name, len(df))


# ── 3. KONEX ─────────────────────────────────────────────────────────────
def download_konex() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "konex_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "konex_code.mst.zip", tmp, "konex_code.zip", "konex_code.mst"
        )
        data = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                mksc_shrn_iscd = row[0:9].strip()
                stnd_iscd = row[9:21].strip()
                hts_kor_isnm = row[21:-184].strip()
                stck_lstg_dt = row[-8:].strip()
                stck_prpr = row[-16:-8].strip()
                lstg_stcn = row[-24:-16].strip()
                sctbd_mrkt_div = row[-25:-24].strip()
                stck_sdpr = row[-34:-25].strip()
                stck_mxpr = row[-43:-34].strip()
                stck_llam = row[-52:-43].strip()
                stck_prdy_clpr = row[-61:-52].strip()
                stck_oprc = row[-70:-61].strip()
                stck_hgpr = row[-79:-70].strip()
                stck_lwpr = row[-88:-79].strip()
                stck_clpr = row[-97:-88].strip()
                acml_vol = row[-116:-97].strip()
                bas_prc = row[-125:-116].strip()
                d250_lwpr = row[-134:-125].strip()
                d250_hgpr = row[-143:-134].strip()
                d250_hgpr_dt = row[-151:-143].strip()
                d250_hgpr_vrss_prpr_rate = row[-160:-151].strip()
                d250_lwpr_dt = row[-168:-160].strip()
                d250_lwpr_vrss_prpr_rate = row[-177:-168].strip()
                w52_lwpr = row[-184:-177].strip()
                data.append([mksc_shrn_iscd, stnd_iscd, hts_kor_isnm, stck_lstg_dt,
                              stck_prpr, lstg_stcn, sctbd_mrkt_div, stck_sdpr,
                              stck_mxpr, stck_llam, stck_prdy_clpr, stck_oprc,
                              stck_hgpr, stck_lwpr, stck_clpr, acml_vol, bas_prc,
                              d250_lwpr, d250_hgpr, d250_hgpr_dt, d250_hgpr_vrss_prpr_rate,
                              d250_lwpr_dt, d250_lwpr_vrss_prpr_rate, w52_lwpr])

        columns = ["단축코드", "표준코드", "한글종목명", "상장일자", "현재가", "상장주수",
                   "시장구분", "상한가", "상한가2", "하한가", "전일종가", "시가",
                   "고가", "저가", "종가", "누적거래량", "기준가",
                   "52주최저가", "52주최고가", "52주최고가일", "52주최고대비율",
                   "52주최저가일", "52주최저대비율", "w52저가"]
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("KONEX", out_path.name, len(df))


# ── 4. 국내ELW ───────────────────────────────────────────────────────────
def download_domestic_elw() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "elw_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "elw_code.mst.zip", tmp, "elw_code.zip", "elw_code.mst"
        )
        data = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                mksc_shrn_iscd = row[0:9].strip()
                stnd_iscd = row[9:21].strip()
                hts_kor_isnm = row[21:50].strip()
                crow = row[50:].strip()
                elw_nvlt_optn_cls_code = crow[:1].strip()
                elw_ko_barrier = crow[1:14].strip()
                bskt_yn = crow[14:15].strip()
                unas_iscd1 = crow[15:24].strip()
                unas_iscd2 = crow[24:33].strip()
                unas_iscd3 = crow[33:42].strip()
                unas_iscd4 = crow[42:51].strip()
                unas_iscd5 = crow[51:60].strip()
                mrkt_prtt_no10 = row[-6:].strip()
                mrkt_prtt_no9 = row[-11:-6].strip()
                mrkt_prtt_no8 = row[-16:-11].strip()
                mrkt_prtt_no7 = row[-21:-16].strip()
                mrkt_prtt_no6 = row[-26:-21].strip()
                mrkt_prtt_no5 = row[-31:-26].strip()
                mrkt_prtt_no4 = row[-36:-31].strip()
                mrkt_prtt_no3 = row[-41:-36].strip()
                mrkt_prtt_no2 = row[-46:-41].strip()
                mrkt_prtt_no1 = row[-51:-46].strip()
                lstn_stcn = row[-66:-51].strip()
                prdy_avls = row[-75:-66].strip()
                paym_date = row[-83:-75].strip()
                rght_type_cls_code = row[-84:-83].strip()
                rmnn_dynu = row[-88:-84].strip()
                stck_last_tr_month = row[-96:-88].strip()
                acpr = row[-105:-96].strip()
                elw_pblc_mrkt_prtt_no = row[-110:-105].strip()
                elw_pblc_istu_name = row[-11:-110].strip()
                data.append([mksc_shrn_iscd, stnd_iscd, hts_kor_isnm,
                              elw_nvlt_optn_cls_code, elw_ko_barrier, bskt_yn,
                              unas_iscd1, unas_iscd2, unas_iscd3, unas_iscd4,
                              unas_iscd5, elw_pblc_istu_name, elw_pblc_mrkt_prtt_no,
                              acpr, stck_last_tr_month, rmnn_dynu, rght_type_cls_code,
                              paym_date, prdy_avls, lstn_stcn, mrkt_prtt_no1,
                              mrkt_prtt_no2, mrkt_prtt_no3, mrkt_prtt_no4,
                              mrkt_prtt_no5, mrkt_prtt_no6, mrkt_prtt_no7,
                              mrkt_prtt_no8, mrkt_prtt_no9, mrkt_prtt_no10])

        columns = [
            "단축코드", "표준코드", "한글종목명", "ELW권리형태", "ELW조기종료발생기준가격",
            "바스켓여부", "기초자산코드1", "기초자산코드2", "기초자산코드3",
            "기초자산코드4", "기초자산코드5", "발행사한글종목명", "발행사코드",
            "행사가", "최종거래일", "잔존일수", "권리유형구분코드", "지급일",
            "전일시가총액(억)", "상장주수(천)", "시장참가자번호1",
            "시장참가자번호2", "시장참가자번호3", "시장참가자번호4",
            "시장참가자번호5", "시장참가자번호6", "시장참가자번호7",
            "시장참가자번호8", "시장참가자번호9", "시장참가자번호10",
        ]
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("국내ELW", out_path.name, len(df))


# ── 5. 지수선물옵션 ─────────────────────────────────────────────────────
def download_index_future() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "fo_idx_code_mts.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "fo_idx_code_mts.mst.zip", tmp, "fo_idx_code_mts.zip", "fo_idx_code_mts.mst"
        )
        columns = ["상품종류", "단축코드", "표준코드", "한글종목명", "ATM구분",
                   "행사가", "월물구분코드", "기초자산단축코드", "기초자산명"]
        df = pd.read_table(mst_path, sep="|", encoding="cp949", header=None)
        df.columns = columns
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("지수선물옵션", out_path.name, len(df))


# ── 6. 주식선물옵션 ─────────────────────────────────────────────────────
def download_stock_future() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "fo_stk_code_mts.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "fo_stk_code_mts.mst.zip", tmp, "fo_stk_code_mts.zip", "fo_stk_code_mts.mst"
        )
        columns = ["상품종류", "단축코드", "표준코드", "한글종목명", "ATM구분",
                   "행사가", "월물구분코드", "기초자산단축코드", "기초자산명"]
        df = pd.read_table(mst_path, sep="|", encoding="cp949", header=None)
        df.columns = columns
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("주식선물옵션", out_path.name, len(df))


# ── 7. CME야간선물 ──────────────────────────────────────────────────────
def download_cme_future() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "fo_cme_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "fo_cme_code.mst.zip", tmp, "fo_cme_code.zip", "fo_cme_code.mst"
        )
        columns = ["상품종류", "단축코드", "표준코드", "한글종목명", "행사가", "기초자산단축코드", "기초자산명"]
        rows_data = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                rows_data.append([
                    row[0:1],
                    row[1:10].strip(),
                    row[10:22].strip(),
                    row[22:63].strip(),
                    row[63:72].strip(),
                    row[72:81].strip(),
                    row[81:].strip(),
                ])
        df = pd.DataFrame(rows_data, columns=columns)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("CME야간선물", out_path.name, len(df))


# ── 8. 상품선물옵션 ─────────────────────────────────────────────────────
def download_commodity_future() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "fo_com_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "fo_com_code.mst.zip", tmp, "fo_com_code.zip", "fo_com_code.mst"
        )
        rows1: list[list[str]] = []
        rows2: list[list[str]] = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                rf1 = row[0:55]
                rows1.append([
                    rf1[0:1],
                    rf1[1:2],
                    rf1[2:11].strip(),
                    rf1[11:23].strip(),
                    rf1[23:55].strip(),
                ])
                rf2 = row[55:].lstrip()
                rows2.append([
                    rf2[8:9],
                    rf2[9:12],
                    rf2[12:].strip(),
                ])

        df1 = pd.DataFrame(rows1, columns=["상품구분", "상품종류", "단축코드", "표준코드", "한글종목명"])
        df2 = pd.DataFrame(rows2, columns=["월물구분코드", "기초자산단축코드", "기초자산명"])
        df = pd.concat([df1, df2], axis=1)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("상품선물옵션", out_path.name, len(df))


# ── 9. EUREX야간옵션 ────────────────────────────────────────────────────
def download_eurex_option() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "fo_eurex_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "fo_eurex_code.mst.zip", tmp, "fo_eurex_code.zip", "fo_eurex_code.mst"
        )
        rows1: list[list[str]] = []
        rows2: list[list[str]] = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                rf1 = row[0:59]
                rows1.append([
                    rf1[0:1],
                    rf1[1:10],
                    rf1[10:22].strip(),
                    rf1[22:59].strip(),
                ])
                rf2 = row[59:].lstrip()
                rows2.append([
                    rf2[0:1],
                    rf2[1:9],
                    rf2[9:17],
                    rf2[17:].strip(),
                ])

        df1 = pd.DataFrame(rows1, columns=["상품종류", "단축코드", "표준코드", "한글종목명"])
        df2 = pd.DataFrame(rows2, columns=["ATM구분", "행사가", "기초자산단축코드", "기초자산명"])
        df = pd.concat([df1, df2], axis=1)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("EUREX야간옵션", out_path.name, len(df))


# ── 10. 장내채권 ─────────────────────────────────────────────────────────
def download_domestic_bond() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "bond_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "bond_code.mst.zip", tmp, "bond_code.zip", "bond_code.mst"
        )
        data = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                row = row.strip()
                bond_type = row[0:2].strip()
                bond_cls_code = row[2:4].strip()
                stnd_iscd = row[4:16].strip()
                rdmp_date = row[-8:].strip()
                pblc_date = row[-16:-8].strip()
                lstn_date = row[-24:-16].strip()
                bond_int_cls_code = row[-26:-24].strip()
                sname = row[16:-26].rstrip()
                data.append([bond_type, bond_cls_code, stnd_iscd, sname,
                              bond_int_cls_code, lstn_date, pblc_date, rdmp_date])

        columns = ["유형", "채권분류코드", "표준코드", "종목명", "채권이자분류코드",
                   "상장일", "발행일", "상환일"]
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("장내채권", out_path.name, len(df))


# ── 11. 해외주식 (전 거래소 통합) ────────────────────────────────────────
_OVERSEAS_MARKETS = [
    ("nas", "나스닥"),
    ("nys", "뉴욕"),
    ("ams", "아멕스"),
    ("shs", "상해"),
    ("shi", "상해지수"),
    ("szs", "심천"),
    ("szi", "심천지수"),
    ("tse", "도쿄"),
    ("hks", "홍콩"),
    ("hnx", "하노이"),
    ("hsx", "호치민"),
]
_OVERSEAS_COLUMNS = [
    "국가코드", "거래소ID", "거래소코드", "거래소명", "심볼", "실시간심볼",
    "한글명", "영문명", "증권유형", "통화", "소수점자리수", "데이터타입",
    "기준가격", "매수호가단위", "매도호가단위", "시장시작시간(HHMM)", "시장종료시간(HHMM)",
    "DR여부(Y/N)", "DR국가코드", "업종분류코드", "지수구성종목존재여부",
    "틱사이즈Type", "구분코드", "틱사이즈type상세",
]


def download_overseas_stock() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "overseas_stock_code.csv"

    ssl._create_default_https_context = ssl._create_unverified_context
    frames = []

    with tempfile.TemporaryDirectory() as tmp:
        for code, _label in _OVERSEAS_MARKETS:
            url = _BASE_URL + f"{code}mst.cod.zip"
            zip_path = os.path.join(tmp, f"{code}mst.cod.zip")
            urllib.request.urlretrieve(url, zip_path)
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(tmp)
            mst_path = os.path.join(tmp, f"{code}mst.cod")
            df = pd.read_table(mst_path, sep="\t", encoding="cp949", header=None,
                               on_bad_lines="skip")
            # 컬럼 수 불일치 대응: 앞 24개만 사용
            if len(df.columns) >= len(_OVERSEAS_COLUMNS):
                df = df.iloc[:, : len(_OVERSEAS_COLUMNS)]
            df.columns = _OVERSEAS_COLUMNS[: len(df.columns)]
            df.insert(0, "시장코드", code)
            frames.append(df)

    merged = pd.concat(frames, axis=0, ignore_index=True)
    merged.to_csv(out_path, index=False, encoding="utf-8-sig")
    return _result("해외주식", out_path.name, len(merged))


# ── 12. 해외주식지수 ─────────────────────────────────────────────────────
def download_overseas_index() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "frgn_code.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "frgn_code.mst.zip", tmp, "frgn_code.zip", "frgn_code.mst"
        )
        rows1: list[list[str]] = []
        rows2: list[list[str]] = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                if row[0:1] == "X":
                    rf1 = row[: len(row) - 14]
                    rows1.append([
                        rf1[0:1],
                        rf1[1:11],
                        rf1[11:40].strip(),
                        rf1[40:80].strip(),
                    ])
                else:
                    rf1 = row[: len(row) - 14]
                    rows1.append([
                        rf1[0:1],
                        rf1[1:11],
                        rf1[11:50].strip(),
                        row[50:75].strip(),
                    ])
                tail = row[-15:]
                rows2.append([
                    tail[0:4],
                    tail[4:5],
                    tail[5:6],
                    tail[6:7],
                    tail[7:11],
                    tail[11:14],
                ])

        df1 = pd.DataFrame(rows1, columns=["구분코드", "심볼", "영문명", "한글명"])
        part2_columns = [
            "종목업종코드", "다우30편입여부", "나스닥100편입여부",
            "SP500편입여부", "거래소코드", "국가구분코드",
        ]
        df2 = pd.DataFrame(rows2, columns=part2_columns)
        df = pd.concat([df1, df2], axis=1)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("해외주식지수", out_path.name, len(df))


# ── 13. 해외선물옵션 ─────────────────────────────────────────────────────
def download_overseas_future() -> dict[str, Any]:
    _ensure_mst_dir()
    out_path = MST_DIR / "ffcode.csv"

    with tempfile.TemporaryDirectory() as tmp:
        mst_path = _download_zip(
            _BASE_URL + "ffcode.mst.zip", tmp, "ffcode.zip", "ffcode.mst"
        )
        columns = [
            "종목코드", "서버자동주문가능여부", "TWAP가능여부", "경제지표주문가능여부",
            "필러", "종목한글명", "거래소코드", "품목코드", "품목종류",
            "출력소수점", "계산소수점", "틱사이즈", "틱가치", "계약크기",
            "가격표시진법", "환산승수", "최다월물여부", "최근월물여부",
            "스프레드여부", "스프레드기준LEG1여부", "서브거래소코드",
        ]
        rows_data = []
        with open(mst_path, mode="r", encoding="cp949") as f:
            for row in f:
                rows_data.append([
                    row[:32],
                    row[32:33].rstrip(),
                    row[33:34].rstrip(),
                    row[34:35],
                    row[35:82].rstrip(),
                    row[82:107].rstrip(),
                    row[-92:-82],
                    row[-82:-72].rstrip(),
                    row[-72:-69].rstrip(),
                    row[-69:-64],
                    row[-64:-59].rstrip(),
                    row[-59:-45].rstrip(),
                    row[-45:-31],
                    row[-31:-21].rstrip(),
                    row[-21:-17].rstrip(),
                    row[-17:-7],
                    row[-7:-6].rstrip(),
                    row[-6:-5].rstrip(),
                    row[-5:-4].rstrip(),
                    row[-4:-3].rstrip(),
                    row[-3:].rstrip(),
                ])
        df = pd.DataFrame(rows_data, columns=columns)
        df.to_csv(out_path, index=False, encoding="utf-8-sig")

    return _result("해외선물옵션", out_path.name, len(df))


# ── 전체 다운로드 ────────────────────────────────────────────────────────
_DOWNLOAD_TASKS = [
    ("KOSPI", download_kospi),
    ("KOSDAQ", download_kosdaq),
    ("KONEX", download_konex),
    ("국내ELW", download_domestic_elw),
    ("지수선물옵션", download_index_future),
    ("주식선물옵션", download_stock_future),
    ("CME야간선물", download_cme_future),
    ("상품선물옵션", download_commodity_future),
    ("EUREX야간옵션", download_eurex_option),
    ("장내채권", download_domestic_bond),
    ("해외주식", download_overseas_stock),
    ("해외주식지수", download_overseas_index),
    ("해외선물옵션", download_overseas_future),
]


def download_all() -> list[dict[str, Any]]:
    """13개 시장 마스터 파일을 순차적으로 다운로드한다.

    각 시장별 결과(성공/오류)를 리스트로 반환한다.
    """
    db_enabled = True
    db_init_error = ""
    get_conn = None
    MARKET_SAVE_FN: dict[str, Any] = {}
    try:
        from db import get_conn as _get_conn
        from stock_master_db import MARKET_SAVE_FN as _market_save_fn

        get_conn = _get_conn
        MARKET_SAVE_FN = _market_save_fn
    except Exception as exc:
        db_enabled = False
        db_init_error = str(exc)
        print(f"[ERROR] stock-master db init failed: {exc}")
        error_logger.exception("stock-master db init failed: %s", exc)

    results: list[dict[str, Any]] = []
    for market, fn in _DOWNLOAD_TASKS:
        try:
            result = fn()
            result["db_rows"] = 0
            if db_enabled and market in MARKET_SAVE_FN and result.get("file"):
                try:
                    csv_path = MST_DIR / result["file"]
                    df = pd.read_csv(csv_path, encoding="utf-8-sig", dtype=str)
                    conn = get_conn()  # type: ignore[operator]
                    try:
                        result["db_rows"] = MARKET_SAVE_FN[market](df, conn)
                    finally:
                        conn.close()
                except Exception as db_exc:
                    result["db_error"] = str(db_exc)
                    result["error"] = f"DB 저장 실패: {db_exc}"
                    print(
                        f"[ERROR] stock-master db save failed market={market} "
                        f"file={result.get('file') or '-'} err={db_exc}"
                    )
                    error_logger.exception(
                        "stock-master db save failed market=%s file=%s",
                        market,
                        result.get("file") or "-",
                    )
            elif not db_enabled:
                result["db_error"] = f"DB 비활성화: {db_init_error}"
            results.append(result)
        except Exception as exc:
            print(f"[ERROR] stock-master download failed market={market} err={exc}")
            results.append({
                "market": market,
                "file": None,
                "rows": 0,
                "db_rows": 0,
                "error": str(exc),
                "savedAt": datetime.now(timezone.utc).isoformat(),
            })
    return results
