"""국내주식 trading API 요청 스펙 로더."""

from __future__ import annotations

import json
from typing import Any


_REQUEST_SPECS_JSON = r"""[
  {
    "name": "기간별계좌권리현황조회",
    "tr_id": "CTRGA011R",
    "tr_id_demo": "CTRGA011R",
    "tr_id_real_candidates": [
      "CTRGA011R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/period-rights",
    "sheet": "기간별계좌권리현황조회",
    "fields": [
      {
        "element": "INQR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "03 입력"
      },
      {
        "element": "CUST_RNCNO25",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란"
      },
      {
        "element": "HMID",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란"
      },
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 8자리 입력 (ex.12345678)"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "상품계좌번호 2자리 입력(ex. 01 or 22)"
      },
      {
        "element": "INQR_STRT_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "조회시작일자(YYYYMMDD)"
      },
      {
        "element": "INQR_END_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "조회종료일자(YYYYMMDD)"
      },
      {
        "element": "RGHT_TYPE_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란"
      },
      {
        "element": "PRDT_TYPE_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란"
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "다음조회시 입력"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "다음조회시 입력"
      }
    ]
  },
  {
    "name": "투자계좌자산현황조회",
    "tr_id": "CTRP6548R",
    "tr_id_demo": "CTRP6548R",
    "tr_id_real_candidates": [
      "CTRP6548R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-account-balance",
    "sheet": "투자계좌자산현황조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "INQR_DVSN_1",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공백입력"
      },
      {
        "element": "BSPR_BF_DT_APLY_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공백입력"
      }
    ]
  },
  {
    "name": "퇴직연금 예수금조회",
    "tr_id": "TTTC0506R",
    "tr_id_demo": "TTTC0506R",
    "tr_id_real_candidates": [
      "TTTC0506R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-deposit",
    "sheet": "퇴직연금 예수금조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "29"
      },
      {
        "element": "ACCA_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00"
      }
    ]
  },
  {
    "name": "주식예약주문정정취소",
    "tr_id": "CTSC0009U",
    "tr_id_demo": "CTSC0009U",
    "tr_id_real_candidates": [
      "CTSC0009U",
      "CTSC0013U"
    ],
    "tr_id_demo_candidates": [],
    "method": "POST",
    "url": "/uapi/domestic-stock/v1/trading/order-resv-rvsecncl",
    "sheet": "주식예약주문정정취소",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정/취소] 계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정/취소] 계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정]"
      },
      {
        "element": "ORD_QTY",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정] 주문주식수"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정] 1주당 가격 \r\n* 장전 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 \"0\"으로 입력 권고"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정]\r\n01 : 매도\r\n02 : 매수"
      },
      {
        "element": "ORD_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정]\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n05 : 장전 시간외"
      },
      {
        "element": "ORD_OBJT_CBLC_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정]\r\n10 : 현금\r\n12 : 주식담보대출\r\n14 : 대여상환\r\n21 : 자기융자신규\r\n22 : 유통대주신규\r\n23 : 유통융자신규\r\n24 : 자기대주신규\r\n25 : 자기융자상환\r\n26 : 유통대주상환\r\n27 : 유통융자상환\r\n28 : 자기대주상환"
      },
      {
        "element": "RSVN_ORD_SEQ",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[정정/취소]"
      }
    ]
  },
  {
    "name": "신용매수가능조회",
    "tr_id": "TTTC8909R",
    "tr_id_demo": "TTTC8909R",
    "tr_id_real_candidates": [
      "TTTC8909R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-credit-psamount",
    "sheet": "신용매수가능조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "종목코드(6자리)"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "1주당 가격 \r\n* 장전 시간외, 장후 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 \"0\"으로 입력 권고"
      },
      {
        "element": "ORD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 지정가 \r\n01 : 시장가 \r\n02 : 조건부지정가 \r\n03 : 최유리지정가 \r\n04 : 최우선지정가 \r\n05 : 장전 시간외 \r\n06 : 장후 시간외 \r\n07 : 시간외 단일가  등"
      },
      {
        "element": "CRDT_TYPE",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "21 : 자기융자신규 \r\n23 : 유통융자신규 \r\n26 : 유통대주상환 \r\n28 : 자기대주상환 \r\n25 : 자기융자상환 \r\n27 : 유통융자상환 \r\n22 : 유통대주신규 \r\n24 : 자기대주신규"
      },
      {
        "element": "CMA_EVLU_AMT_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "Y/N"
      },
      {
        "element": "OVRS_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "Y/N"
      }
    ]
  },
  {
    "name": "주식통합증거금 현황",
    "tr_id": "TTTC0869R",
    "tr_id_demo": "TTTC0869R",
    "tr_id_real_candidates": [
      "TTTC0869R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/intgr-margin",
    "sheet": "주식통합증거금 현황",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "CMA_EVLU_AMT_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "N 입력"
      },
      {
        "element": "WCRC_FRCR_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "01(외화기준),02(원화기준)"
      },
      {
        "element": "FWEX_CTRT_FRCR_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "01(외화기준),02(원화기준)"
      }
    ]
  },
  {
    "name": "퇴직연금 미체결내역",
    "tr_id": "TTTC2201R",
    "tr_id_demo": "TTTC2201R",
    "tr_id_real_candidates": [
      "TTTC2201R",
      "TTTC2210R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-daily-ccld",
    "sheet": "퇴직연금 미체결내역",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "29"
      },
      {
        "element": "USER_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "%%"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 전체 / 01 : 매도 / 02 : 매수"
      },
      {
        "element": "CCLD_NCCS_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "%% : 전체 / 01 : 체결 / 02 : 미체결"
      },
      {
        "element": "INQR_DVSN_3",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 전체"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      }
    ]
  },
  {
    "name": "기간별매매손익현황조회",
    "tr_id": "TTTC8715R",
    "tr_id_demo": "TTTC8715R",
    "tr_id_real_candidates": [
      "TTTC8715R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-period-trade-profit",
    "sheet": "기간별매매손익현황조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "SORT_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00: 최근 순, 01: 과거 순, 02: 최근 순"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "\"\"공란입력 시, 전체"
      },
      {
        "element": "INQR_STRT_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "INQR_END_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CBLC_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00: 전체"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      }
    ]
  },
  {
    "name": "주식주문(정정취소)",
    "tr_id": "TTTC0013U",
    "tr_id_demo": "VTTC0013U",
    "tr_id_real_candidates": [
      "TTTC0013U"
    ],
    "tr_id_demo_candidates": [
      "VTTC0013U"
    ],
    "method": "POST",
    "url": "/uapi/domestic-stock/v1/trading/order-rvsecncl",
    "sheet": "주식주문(정정취소)",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종합계좌번호"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "상품유형코드"
      },
      {
        "element": "KRX_FWDG_ORD_ORGNO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": ""
      },
      {
        "element": "ORGN_ODNO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "원주문번호"
      },
      {
        "element": "ORD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[KRX]\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n05 : 장전 시간외\r\n06 : 장후 시간외\r\n07 : 시간외 단일가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[NXT]\r\n00 : 지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[SOR]\r\n00 : 지정가\r\n01 : 시장가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)"
      },
      {
        "element": "RVSE_CNCL_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "01@정정\r\n02@취소"
      },
      {
        "element": "ORD_QTY",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주문수량"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주문단가"
      },
      {
        "element": "QTY_ALL_ORD_YN",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "'Y@전량\r\nN@일부'"
      }
    ]
  },
  {
    "name": "주식예약주문조회",
    "tr_id": "CTSC0004R",
    "tr_id_demo": "CTSC0004R",
    "tr_id_real_candidates": [
      "CTSC0004R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/order-resv-ccnl",
    "sheet": "주식예약주문조회",
    "fields": [
      {
        "element": "RSVN_ORD_ORD_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "RSVN_ORD_END_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "RSVN_ORD_SEQ",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "TMNL_MDIA_KIND_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "\"00\" 입력"
      },
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "PRCS_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "0: 전체\r\n1: 처리내역\r\n2: 미처리내역"
      },
      {
        "element": "CNCL_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "\"Y\" 유효한 주문만 조회"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "종목코드(6자리) (공백 입력 시 전체 조회)"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CTX_AREA_FK200",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "다음 페이지 조회시 사용"
      },
      {
        "element": "CTX_AREA_NK200",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "다음 페이지 조회시 사용"
      }
    ]
  },
  {
    "name": "퇴직연금 매수가능조회",
    "tr_id": "TTTC0503R",
    "tr_id_demo": "TTTC0503R",
    "tr_id_real_candidates": [
      "TTTC0503R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-psbl-order",
    "sheet": "퇴직연금 매수가능조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "29"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ACCA_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00"
      },
      {
        "element": "CMA_EVLU_AMT_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ORD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 지정가 / 01 : 시장가"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      }
    ]
  },
  {
    "name": "주식잔고조회",
    "tr_id": "TTTC8434R",
    "tr_id_demo": "VTTC8434R",
    "tr_id_real_candidates": [
      "TTTC8434R"
    ],
    "tr_id_demo_candidates": [
      "VTTC8434R"
    ],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-balance",
    "sheet": "주식잔고조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "AFHR_FLPR_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "N : 기본값,\r\nY : 시간외단일가,\r\nX : NXT 정규장 (프리마켓, 메인, 애프터마켓)\r\n※ NXT 선택 시 : NXT 거래종목만 시세 등 정보가 NXT 기준으로 변동됩니다. KRX 종목들은 그대로 유지"
      },
      {
        "element": "INQR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "01 : 대출일별"
      },
      {
        "element": "UNPR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "01 : 기본값"
      },
      {
        "element": "FUND_STTL_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "N : 포함하지 않음\r\nY :  포함"
      },
      {
        "element": "FNCG_AMT_AUTO_RDPT_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "N : 기본값"
      },
      {
        "element": "PRCS_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 :  전일매매포함\r\n01 : 전일매매미포함"
      }
    ]
  },
  {
    "name": "퇴직연금 체결기준잔고",
    "tr_id": "TTTC2202R",
    "tr_id_demo": "TTTC2202R",
    "tr_id_real_candidates": [
      "TTTC2202R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-present-balance",
    "sheet": "퇴직연금 체결기준잔고",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "29"
      },
      {
        "element": "USER_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      }
    ]
  },
  {
    "name": "매수가능조회",
    "tr_id": "TTTC8908R",
    "tr_id_demo": "VTTC8908R",
    "tr_id_real_candidates": [
      "TTTC8908R"
    ],
    "tr_id_demo_candidates": [
      "VTTC8908R"
    ],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-psbl-order",
    "sheet": "매수가능조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "종목번호(6자리)\r\n* PDNO, ORD_UNPR 공란 입력 시, 매수수량 없이 매수금액만 조회됨"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "1주당 가격\r\n* 시장가(ORD_DVSN:01)로 조회 시, 공란으로 입력\r\n* PDNO, ORD_UNPR 공란 입력 시, 매수수량 없이 매수금액만 조회됨"
      },
      {
        "element": "ORD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "* 특정 종목 전량매수 시 가능수량을 확인할 경우\r\n    00:지정가는 증거금율이 반영되지 않으므로\r\n    증거금율이 반영되는 01: 시장가로 조회\r\n* 다만, 조건부지정가 등 특정 주문구분(ex.IOC)으로 주문 시 가능수량을 확인할 경우 주문 시와 동일한 주문구분(ex.IOC) 입력하여 가능수량 확인\r\n* 종목별 매수가능수량 조회 없이 매수금액만 조회하고자 할 경우 임의값(00) 입력\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n05 : 장전 시간외\r\n06 : 장후 시간외\r\n07 : 시간외 단일가\r\n08 : 자기주식\r\n09 : 자기주식S-Option\r\n10 : 자기주식금전신탁\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n51 : 장중대량\r\n52 : 장중바스켓\r\n62 : 장개시전 시간외대량\r\n63 : 장개시전 시간외바스켓\r\n67 : 장개시전 금전신탁자사주\r\n69 : 장개시전 자기주식\r\n72 : 시간외대량\r\n77 : 시간외자사주신탁\r\n79 : 시간외대량자기주식\r\n80 : 바스켓"
      },
      {
        "element": "CMA_EVLU_AMT_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "Y : 포함\r\nN : 포함하지 않음"
      },
      {
        "element": "OVRS_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "Y : 포함\r\nN : 포함하지 않음"
      }
    ]
  },
  {
    "name": "기간별손익일별합산조회",
    "tr_id": "TTTC8708R",
    "tr_id_demo": "TTTC8708R",
    "tr_id_real_candidates": [
      "TTTC8708R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-period-profit",
    "sheet": "기간별손익일별합산조회",
    "fields": [
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "INQR_STRT_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "\"\"공란입력 시, 전체"
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "INQR_END_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "SORT_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00: 최근 순, 01: 과거 순, 02: 최근 순"
      },
      {
        "element": "INQR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 입력"
      },
      {
        "element": "CBLC_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00: 전체"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      }
    ]
  },
  {
    "name": "주식주문(현금)",
    "tr_id": "TTTC0011U",
    "tr_id_demo": "VTTC0011U",
    "tr_id_real_candidates": [
      "TTTC0011U",
      "TTTC0012U"
    ],
    "tr_id_demo_candidates": [
      "VTTC0011U",
      "VTTC0012U"
    ],
    "method": "POST",
    "url": "/uapi/domestic-stock/v1/trading/order-cash",
    "sheet": "주식주문(현금)",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종합계좌번호"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "상품유형코드"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드(6자리) , ETN의 경우 7자리 입력"
      },
      {
        "element": "ORD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[KRX]\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n05 : 장전 시간외\r\n06 : 장후 시간외\r\n07 : 시간외 단일가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[NXT]\r\n00 : 지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[SOR]\r\n00 : 지정가\r\n01 : 시장가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)"
      },
      {
        "element": "ORD_QTY",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주문수량"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주문단가\r\n시장가 등 주문시, \"0\"으로 입력"
      }
    ]
  },
  {
    "name": "매도가능수량조회",
    "tr_id": "TTTC8408R",
    "tr_id_demo": "TTTC8408R",
    "tr_id_real_candidates": [
      "TTTC8408R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-psbl-sell",
    "sheet": "매도가능수량조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "종합계좌번호"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌상품코드"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "보유종목 코드 ex)000660"
      }
    ]
  },
  {
    "name": "주식일별주문체결조회",
    "tr_id": "TTTC0081R",
    "tr_id_demo": "VTTC0081R",
    "tr_id_real_candidates": [
      "TTTC0081R",
      "CTSC9215R"
    ],
    "tr_id_demo_candidates": [
      "VTTC0081R",
      "VTSC9215R"
    ],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-daily-ccld",
    "sheet": "주식일별주문체결조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "INQR_STRT_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "YYYYMMDD"
      },
      {
        "element": "INQR_END_DT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "YYYYMMDD"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 전체 / 01 : 매도 / 02 : 매수"
      },
      {
        "element": "ORD_GNO_BRNO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "주문시 한국투자증권 시스템에서 지정된 영업점코드"
      },
      {
        "element": "CCLD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'00 전체\r\n01 체결\r\n02 미체결'"
      },
      {
        "element": "INQR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'00 역순\r\n01 정순'"
      },
      {
        "element": "INQR_DVSN_1",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'없음: 전체\r\n1: ELW\r\n2: 프리보드'"
      },
      {
        "element": "INQR_DVSN_3",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'00 전체\r\n01 현금\r\n02 신용\r\n03 담보\r\n04 대주\r\n05 대여\r\n06 자기융자신규/상환\r\n07 유통융자신규/상환'"
      },
      {
        "element": "EXCG_ID_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "한국거래소 : KRX\r\n대체거래소 (NXT) : NXT\r\nSOR (Smart Order Routing) : SOR\r\nALL : 전체\r\n※ 모의투자는 KRX만 제공"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'공란 : 최초 조회시는 \r\n이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)'"
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'공란 : 최초 조회시 \r\n이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)'"
      }
    ]
  },
  {
    "name": "주식정정취소가능주문조회",
    "tr_id": "TTTC0084R",
    "tr_id_demo": "TTTC0084R",
    "tr_id_real_candidates": [
      "TTTC0084R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-psbl-rvsecncl",
    "sheet": "주식정정취소가능주문조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'공란 : 최초 조회시는 \r\n이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)'"
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'공란 : 최초 조회시 \r\n이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)'"
      },
      {
        "element": "INQR_DVSN_1",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'0 주문\r\n1 종목'"
      },
      {
        "element": "INQR_DVSN_2",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'0 전체\r\n1 매도\r\n2 매수'"
      }
    ]
  },
  {
    "name": "주식예약주문",
    "tr_id": "CTSC0008U",
    "tr_id_demo": "CTSC0008U",
    "tr_id_real_candidates": [
      "CTSC0008U"
    ],
    "tr_id_demo_candidates": [],
    "method": "POST",
    "url": "/uapi/domestic-stock/v1/trading/order-resv",
    "sheet": "주식예약주문",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": ""
      },
      {
        "element": "ORD_QTY",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주문주식수"
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "1주당 가격 \r\n* 장전 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 \"0\"으로 입력 권고"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "01 : 매도\r\n02 : 매수"
      },
      {
        "element": "ORD_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n05 : 장전 시간외"
      },
      {
        "element": "ORD_OBJT_CBLC_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[매도매수구분코드 01:매도/02:매수시 사용]\r\n10 : 현금 \r\n\r\n[매도매수구분코드 01:매도시 사용]\r\n12 : 주식담보대출 \r\n14 : 대여상환\r\n21 : 자기융자신규\r\n22 : 유통대주신규\r\n23 : 유통융자신규\r\n24 : 자기대주신규\r\n25 : 자기융자상환\r\n26 : 유통대주상환\r\n27 : 유통융자상환\r\n28 : 자기대주상환"
      }
    ]
  },
  {
    "name": "주식주문(신용)",
    "tr_id": "TTTC0051U",
    "tr_id_demo": "TTTC0051U",
    "tr_id_real_candidates": [
      "TTTC0051U",
      "TTTC0052U"
    ],
    "tr_id_demo_candidates": [],
    "method": "POST",
    "url": "/uapi/domestic-stock/v1/trading/order-credit",
    "sheet": "주식주문(신용)",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드(6자리)"
      },
      {
        "element": "CRDT_TYPE",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[매도] 22 : 유통대주신규, 24 : 자기대주신규, 25 : 자기융자상환, 27 : 유통융자상환\r\n[매수] 21 : 자기융자신규, 23 : 유통융자신규 , 26 : 유통대주상환, 28 : 자기대주상환"
      },
      {
        "element": "LOAN_DT",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[신용매수] \r\n신규 대출로, 오늘날짜(yyyyMMdd)) 입력 \r\n\r\n[신용매도] \r\n매도할 종목의 대출일자(yyyyMMdd)) 입력"
      },
      {
        "element": "ORD_DVSN",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[KRX]\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n05 : 장전 시간외\r\n06 : 장후 시간외\r\n07 : 시간외 단일가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[NXT]\r\n00 : 지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[SOR]\r\n00 : 지정가\r\n01 : 시장가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)"
      },
      {
        "element": "ORD_QTY",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": ""
      },
      {
        "element": "ORD_UNPR",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "1주당 가격 \r\n* 장전 시간외, 장후 시간외, 시장가의 경우 1주당 가격을 공란으로 비우지 않음 \"0\"으로 입력 권고"
      }
    ]
  },
  {
    "name": "퇴직연금 잔고조회",
    "tr_id": "TTTC2208R",
    "tr_id_demo": "TTTC2208R",
    "tr_id_real_candidates": [
      "TTTC2208R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-balance",
    "sheet": "퇴직연금 잔고조회",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "29"
      },
      {
        "element": "ACCA_DVSN_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00"
      },
      {
        "element": "INQR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 전체"
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      }
    ]
  },
  {
    "name": "주식잔고조회_실현손익",
    "tr_id": "TTTC8494R",
    "tr_id_demo": "TTTC8494R",
    "tr_id_real_candidates": [
      "TTTC8494R"
    ],
    "tr_id_demo_candidates": [],
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/trading/inquire-balance-rlz-pl",
    "sheet": "주식잔고조회_실현손익",
    "fields": [
      {
        "element": "CANO",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 앞 8자리"
      },
      {
        "element": "ACNT_PRDT_CD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "계좌번호 체계(8-2)의 뒤 2자리"
      },
      {
        "element": "AFHR_FLPR_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "'N : 기본값 \r\nY : 시간외단일가'"
      },
      {
        "element": "OFL_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란"
      },
      {
        "element": "INQR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 전체"
      },
      {
        "element": "UNPR_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "01 : 기본값"
      },
      {
        "element": "FUND_STTL_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "N : 포함하지 않음 \r\nY : 포함"
      },
      {
        "element": "FNCG_AMT_AUTO_RDPT_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "N : 기본값"
      },
      {
        "element": "PRCS_DVSN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "00 : 전일매매포함 \r\n01 : 전일매매미포함"
      },
      {
        "element": "COST_ICLD_YN",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": ""
      },
      {
        "element": "CTX_AREA_FK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란 : 최초 조회시 \r\n이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)"
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "공란 : 최초 조회시 \r\n이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)"
      }
    ]
  }
]"""


def load_trading_api_specs() -> list[dict[str, Any]]:
    return json.loads(_REQUEST_SPECS_JSON)


TRADING_API_SPECS = load_trading_api_specs()
