"""국내주식 websocket/quotations 혼합 요청 스펙."""

from __future__ import annotations

import json
from typing import Any


_REQUEST_SPECS_JSON = r"""[
  {
    "name": "채권지수 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0BICNT0",
    "tr_id": "H0BICNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "채권지수 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0BICNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "채권 종목코드 (ex. KR103502GA34)"
      }
    ]
  },
  {
    "name": "일반채권 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0BJASP0",
    "tr_id": "H0BJCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "일반채권 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0BJCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "채권 종목코드 (ex. KR103502GA34)"
      }
    ]
  },
  {
    "name": "일반채권 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0BJCNT0",
    "tr_id": "H0BJCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "일반채권 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0BJCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "채권 종목코드 (ex. KR103502GA34)"
      }
    ]
  },
  {
    "name": "상품선물 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0CFASP0",
    "tr_id": "H0CFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "상품선물 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0CFASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "상품선물 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0CFCNT0",
    "tr_id": "H0CFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "상품선물 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0CFCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "KRX야간옵션실시간예상체결",
    "method": "POST",
    "url": "/tryitout/H0EUANC0",
    "tr_id": "H0EUANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션실시간예상체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0EUANC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "야간옵션 종목코드"
      }
    ]
  },
  {
    "name": "KRX야간옵션 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0EUASP0",
    "tr_id": "H0EUASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0EUASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "야간옵션 종목코드"
      }
    ]
  },
  {
    "name": "KRX야간옵션실시간체결통보",
    "method": "POST",
    "url": "/tryitout/H0EUCNI0",
    "tr_id": "H0MFCNI0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션실시간체결통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0MFCNI0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HTS ID"
      }
    ]
  },
  {
    "name": "KRX야간옵션 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0EUCNT0",
    "tr_id": "H0EUCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0EUCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "야간옵션 종목코드"
      }
    ]
  },
  {
    "name": "ELW 실시간예상체결",
    "method": "POST",
    "url": "/tryitout/H0EWANC0",
    "tr_id": "H0EWANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "ELW 실시간예상체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0EWANC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "ELW 종목코드(ex. 57LA24)"
      }
    ]
  },
  {
    "name": "ELW 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0EWASP0",
    "tr_id": "H0EWASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "ELW 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0EWASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "ELW 종목코드(ex. 57LA24)"
      }
    ]
  },
  {
    "name": "ELW 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0EWCNT0",
    "tr_id": "H0EWCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "ELW 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0EWCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "ELW 종목코드(ex. 57LA24)"
      }
    ]
  },
  {
    "name": "해외주식 실시간체결통보",
    "method": "POST",
    "url": "/tryitout/H0GSCNI0",
    "tr_id": "H0GSCNI0",
    "tr_id_demo": "H0GSCNI9",
    "sheet": "해외주식 실시간체결통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[실전투자]\r\nH0GSCNI0 : 실시간 해외주식 체결통보\r\n\r\n[모의투자]\r\nH0GSCNI9 : 실시간 해외주식 체결통보"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HTSID"
      }
    ]
  },
  {
    "name": "지수선물 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0IFASP0",
    "tr_id": "H0IFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수선물 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0IFASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "예:101S12"
      }
    ]
  },
  {
    "name": "선물옵션 실시간체결통보",
    "method": "POST",
    "url": "/tryitout/H0IFCNI0",
    "tr_id": "H0IFCNI0",
    "tr_id_demo": "H0IFCNI9",
    "sheet": "선물옵션 실시간체결통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[실전투자]\r\nH0IFCNI0 : 실시간 선물옵션 체결통보\r\n\r\n[모의투자]\r\nH0IFCNI9 : 실시간 선물옵션 체결통보"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "예:101S12"
      }
    ]
  },
  {
    "name": "지수선물 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0IFCNT0",
    "tr_id": "H0IFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수선물 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0IFCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "예:101S12"
      }
    ]
  },
  {
    "name": "지수옵션 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0IOASP0",
    "tr_id": "H0IOASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수옵션 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0IOASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "예:201S11305"
      }
    ]
  },
  {
    "name": "지수옵션  실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0IOCNT0",
    "tr_id": "H0IOCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수옵션  실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0IOCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "예:201S11305"
      }
    ]
  },
  {
    "name": "KRX야간선물 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0MFASP0",
    "tr_id": "H0MFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간선물 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0MFASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "야간선물 종목코드"
      }
    ]
  },
  {
    "name": "KRX야간선물 실시간체결통보",
    "method": "POST",
    "url": "/tryitout/H0MFCNI0",
    "tr_id": "H0MFCNI0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간선물 실시간체결통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0MFCNI0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HTS ID"
      }
    ]
  },
  {
    "name": "KRX야간선물 실시간종목체결",
    "method": "POST",
    "url": "/tryitout/H0MFCNT0",
    "tr_id": "H0MFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간선물 실시간종목체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0MFCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "야간선물 종목코드"
      }
    ]
  },
  {
    "name": "국내주식 실시간예상체결 (NXT)",
    "method": "POST",
    "url": "/tryitout/H0NXANC0",
    "tr_id": "H0NXANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간예상체결 (NXT)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0NXANC0 : 국내주식 실시간예상체결 (NXT)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간호가 (NXT)",
    "method": "POST",
    "url": "/tryitout/H0NXASP0",
    "tr_id": "H0NXASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간호가 (NXT)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0NXASP0 : 실시간 주식 호가 (NXT)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간체결가 (NXT)",
    "method": "POST",
    "url": "/tryitout/H0NXCNT0",
    "tr_id": "H0NXCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간체결가 (NXT)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0NXCNT0 : 주식종목체결 (NXT)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간회원사 (NXT)",
    "method": "POST",
    "url": "/tryitout/H0NXMBC0",
    "tr_id": "H0NXMBC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간회원사 (NXT)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0NXMBC0 : 국내주식 주식종목회원사 (NXT)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간프로그램매매 (NXT)",
    "method": "POST",
    "url": "/tryitout/H0NXPGM0",
    "tr_id": "H0NXPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간프로그램매매 (NXT)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0NXPGM0 : 실시간 주식프로그램매매 (NXT)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간예상체결 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STANC0",
    "tr_id": "H0STANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간예상체결 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STANC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간호가 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STASP0",
    "tr_id": "H0STASP0",
    "tr_id_demo": "H0STASP0",
    "sheet": "국내주식 실시간호가 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[실전/모의투자]\r\nH0STASP0 : 주식호가"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목번호 (6자리)\r\nETN의 경우, Q로 시작 (EX. Q500001)"
      }
    ]
  },
  {
    "name": "국내주식 실시간체결통보",
    "method": "POST",
    "url": "/tryitout/H0STCNI0",
    "tr_id": "H0STCNI0",
    "tr_id_demo": "H0STCNI9",
    "sheet": "국내주식 실시간체결통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "'[실전/모의투자]\r\nH0STCNI0 : 국내주식 실시간체결통보\r\nH0STCNI9 : 모의투자 실시간 체결통보"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HTS ID"
      }
    ]
  },
  {
    "name": "국내주식 실시간체결가 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STCNT0",
    "tr_id": "H0STCNT0",
    "tr_id_demo": "H0STCNT0",
    "sheet": "국내주식 실시간체결가 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[실전/모의투자]\r\nH0STCNT0 : 실시간 주식 체결가"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목번호 (6자리)\r\nETN의 경우, Q로 시작 (EX. Q500001)"
      }
    ]
  },
  {
    "name": "국내주식 실시간회원사 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STMBC0",
    "tr_id": "H0STMBC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간회원사 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STMBC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "국내주식 장운영정보 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STMKO0",
    "tr_id": "H0STMKO0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 장운영정보 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STMKO0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "국내ETF NAV추이",
    "method": "POST",
    "url": "/tryitout/H0STNAV0",
    "tr_id": "H0STNAV0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내ETF NAV추이",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STNAV0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex. 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 시간외 실시간호가 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STOAA0",
    "tr_id": "H0STOAA0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 시간외 실시간호가 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STOAA0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 시간외 실시간예상체결 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STOAC0",
    "tr_id": "H0STOAC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 시간외 실시간예상체결 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STOAC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 시간외 실시간체결가 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STOUP0",
    "tr_id": "H0STOUP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 시간외 실시간체결가 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STOUP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간프로그램매매 (KRX)",
    "method": "POST",
    "url": "/tryitout/H0STPGM0",
    "tr_id": "H0STPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간프로그램매매 (KRX)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0STPGM0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "국내주식 실시간예상체결 (통합)",
    "method": "POST",
    "url": "/tryitout/H0UNANC0",
    "tr_id": "H0UNANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간예상체결 (통합)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "[실전투자]\r\nH0UNANC0 : 국내주식 실시간예상체결 (통합)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간호가 (통합)",
    "method": "POST",
    "url": "/tryitout/H0UNASP0",
    "tr_id": "H0UNASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간호가 (통합)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UNASP0 : 실시간 주식 체결가 통합"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간체결가 (통합)",
    "method": "POST",
    "url": "/tryitout/H0UNCNT0",
    "tr_id": "H0UNCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간체결가 (통합)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UNCNT0 : 실시간 주식 체결가 통합"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간회원사 (통합)",
    "method": "POST",
    "url": "/tryitout/H0UNMBC0",
    "tr_id": "H0UNMBC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간회원사 (통합)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UNMBC0 : 국내주식 주식종목회원사 (통합)"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 실시간프로그램매매 (통합)",
    "method": "POST",
    "url": "/tryitout/H0UNPGM0",
    "tr_id": "H0UNPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간프로그램매매 (통합)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UNPGM0 : 실시간 주식종목프로그램매매 통합"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내지수 실시간예상체결",
    "method": "POST",
    "url": "/tryitout/H0UPANC0",
    "tr_id": "H0UPANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내지수 실시간예상체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UPANC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "업종구분코드"
      }
    ]
  },
  {
    "name": "국내지수 실시간체결",
    "method": "POST",
    "url": "/tryitout/H0UPCNT0",
    "tr_id": "H0UPCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내지수 실시간체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UPCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "업종구분코드"
      }
    ]
  },
  {
    "name": "국내지수 실시간프로그램매매",
    "method": "POST",
    "url": "/tryitout/H0UPPGM0",
    "tr_id": "H0UPPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내지수 실시간프로그램매매",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0UPPGM0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "업종구분코드"
      }
    ]
  },
  {
    "name": "주식선물 실시간예상체결",
    "method": "POST",
    "url": "/tryitout/H0ZFANC0",
    "tr_id": "H0ZFANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식선물 실시간예상체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0ZFANC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주식선물 종목코드"
      }
    ]
  },
  {
    "name": "주식선물 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0ZFASP0",
    "tr_id": "H0ZFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식선물 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0ZFASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "주식선물 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0ZFCNT0",
    "tr_id": "H0ZFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식선물 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0ZFCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "주식옵션 실시간예상체결",
    "method": "POST",
    "url": "/tryitout/H0ZOANC0",
    "tr_id": "H0ZOANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식옵션 실시간예상체결",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0ZOANC0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "주식옵션 종목코드"
      }
    ]
  },
  {
    "name": "주식옵션 실시간호가",
    "method": "POST",
    "url": "/tryitout/H0ZOASP0",
    "tr_id": "H0ZOASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식옵션 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0ZOASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "주식옵션 실시간체결가",
    "method": "POST",
    "url": "/tryitout/H0ZOCNT0",
    "tr_id": "H0ZOCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식옵션 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "H0ZOCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간호가",
    "method": "POST",
    "url": "/tryitout/HDFFF010",
    "tr_id": "HDFFF010",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFFF010"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드\r\n\r\n※ CME, SGX 실시간시세 유료시세 신청 필수 \r\n\"포럼 > FAQ > 해외선물옵션 API 유료시세 신청방법(CME, SGX 거래소)\""
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간체결가",
    "method": "POST",
    "url": "/tryitout/HDFFF020",
    "tr_id": "HDFFF020",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFFF020"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "종목코드\r\n\r\n※ CME, SGX 실시간시세 유료시세 신청 필수 \r\n\"포럼 > FAQ > 해외선물옵션 API 유료시세 신청방법(CME, SGX 거래소)\""
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간주문내역통보",
    "method": "POST",
    "url": "/tryitout/HDFFF1C0",
    "tr_id": "HDFFF1C0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간주문내역통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFFF1C0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HTSID"
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간체결내역통보",
    "method": "POST",
    "url": "/tryitout/HDFFF2C0",
    "tr_id": "HDFFF2C0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간체결내역통보",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFFF2C0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HTSID"
      }
    ]
  },
  {
    "name": "해외주식 실시간호가",
    "method": "POST",
    "url": "/tryitout/HDFSASP0",
    "tr_id": "HDFSASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외주식 실시간호가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFSASP0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "<미국 야간거래 - 무료시세>\r\nD+시장구분(3자리)+종목코드\r\n예) DNASAAPL : D+NAS(나스닥)+AAPL(애플)\r\n[시장구분]\r\nNYS : 뉴욕, NAS : 나스닥, AMS : 아멕스\r\n\r\n<미국 주간거래>\r\nR+시장구분(3자리)+종목코드\r\n예) RBAQAAPL : R+BAQ(나스닥)+AAPL(애플)\r\n[시장구분]\r\nBAY : 뉴욕(주간), BAQ : 나스닥(주간). BAA : 아멕스(주간)\r\n\r\n<아시아국가 - 유료시세>\r\n※ 유료시세 신청시에만 유료시세 수신가능\r\n\"포럼 > FAQ > 해외주식 유료시세 신청방법\" 참고\r\nR+시장구분(3자리)+종목코드\r\n예) RHKS00003 : R+HKS(홍콩)+00003(홍콩중화가스)\r\n[시장구분]\r\nTSE : 도쿄, HKS : 홍콩,\r\nSHS : 상해, SZS : 심천\r\nHSX : 호치민, HNX : 하노이"
      }
    ]
  },
  {
    "name": "해외주식 지연호가(아시아)",
    "method": "POST",
    "url": "/tryitout/HDFSASP1",
    "tr_id": "HDFSASP1",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외주식 지연호가(아시아)",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFSASP1"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "<아시아국가 - 무료시세>\r\nD+시장구분(3자리)+종목코드\r\n예) DHKS00003 : D+HKS(홍콩)+00003(홍콩중화가스)\r\n[시장구분]\r\nTSE : 도쿄, HKS : 홍콩,\r\nSHS : 상해, SZS : 심천\r\nHSX : 호치민, HNX : 하노이"
      }
    ]
  },
  {
    "name": "해외주식 실시간지연체결가",
    "method": "POST",
    "url": "/tryitout/HDFSCNT0",
    "tr_id": "HDFSCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외주식 실시간지연체결가",
    "fields": [
      {
        "element": "tr_id",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "HDFSCNT0"
      },
      {
        "element": "tr_key",
        "required": "Y",
        "type": "string",
        "location": "body",
        "description": "<미국 야간거래/아시아 주간거래 - 무료시세>\r\nD+시장구분(3자리)+종목코드\r\n예) DNASAAPL : D+NAS(나스닥)+AAPL(애플)\r\n[시장구분]\r\nNYS : 뉴욕, NAS : 나스닥, AMS : 아멕스 ,\r\nTSE : 도쿄, HKS : 홍콩,\r\nSHS : 상해, SZS : 심천\r\nHSX : 호치민, HNX : 하노이\r\n\r\n<미국 야간거래/아시아 주간거래 - 유료시세>\r\n※ 유료시세 신청시에만 유료시세 수신가능\r\n\"포럼 > FAQ > 해외주식 유료시세 신청방법\" 참고\r\nR+시장구분(3자리)+종목코드\r\n예) RNASAAPL : R+NAS(나스닥)+AAPL(애플)\r\n[시장구분]\r\nNYS : 뉴욕, NAS : 나스닥, AMS : 아멕스 ,\r\nTSE : 도쿄, HKS : 홍콩,\r\nSHS : 상해, SZS : 심천\r\nHSX : 호치민, HNX : 하노이\r\n\r\n<미국 주간거래>\r\nR+시장구분(3자리)+종목코드\r\n예) RBAQAAPL : R+BAQ(나스닥)+AAPL(애플)\r\n[시장구분]\r\nBAY : 뉴욕(주간), BAQ : 나스닥(주간). BAA : 아멕스(주간)"
      }
    ]
  },
  {
    "name": "회원사 실시간 매매동향(틱)",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-trade-trend",
    "tr_id": "FHPST04320000",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "회원사 실시간 매매동향(틱)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "J 고정 입력"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "20432(primary key)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "ex. 005930(삼성전자) \r\n\r\n※ FID_INPUT_ISCD(종목코드) 혹은 FID_MRKT_CLS_CODE(시장구분코드) 둘 중 하나만 입력"
      },
      {
        "element": "FID_INPUT_ISCD_2",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "ex. 99999(전체)\r\n\r\n※ 회원사코드 (kis developers 포탈 사이트 포럼-> FAQ -> 종목정보 다운로드(국내) 참조)"
      },
      {
        "element": "FID_MRKT_CLS_CODE",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "A(전체),K(코스피), Q(코스닥), K2(코스피200), W(ELW)\r\n\r\n※ FID_INPUT_ISCD(종목코드) 혹은 FID_MRKT_CLS_CODE(시장구분코드) 둘 중 하나만 입력"
      },
      {
        "element": "FID_VOL_CNT",
        "required": "Y",
        "type": "string",
        "location": "query",
        "description": "거래량 ~"
      }
    ]
  }
]"""


def load_websocket_request_specs() -> list[dict[str, Any]]:
    return json.loads(_REQUEST_SPECS_JSON)


WEBSOCKET_REQUEST_SPECS = load_websocket_request_specs()
WEBSOCKET_REQUEST_SPECS_BY_URL = {
    str(spec.get("url", "")): spec for spec in WEBSOCKET_REQUEST_SPECS if spec.get("url")
}
