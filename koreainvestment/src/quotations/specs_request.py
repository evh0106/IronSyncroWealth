"""국내주식 quotations API 요청 스펙 로더."""

from __future__ import annotations

import json
from typing import Any


_REQUEST_SPECS_JSON = r"""[
  {
    "name": "주식현재가 일자별",
    "tr_id": "FHKST01010400",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-price",
    "sheet": "주식현재가 일자별",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      },
      {
        "element": "FID_PERIOD_DIV_CODE",
        "required": "Y",
        "description": "'D : (일)최근 30거래일 \r\nW : (주)최근 30주 \r\nM : (월)최근 30개월'"
      },
      {
        "element": "FID_ORG_ADJ_PRC",
        "required": "Y",
        "description": "'0 : 수정주가미반영\r\n1 : 수정주가반영\r\n* 수정주가는 액면분할/액면병합 등 권리 발생 시 과거 시세를 현재 주가에 맞게 보정한 가격'"
      }
    ]
  },
  {
    "name": "주식현재가 시세",
    "tr_id": "FHKST01010100",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-price",
    "sheet": "주식현재가 시세",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)  // ETN은 종목코드 6자리 앞에 Q 입력 필수"
      }
    ]
  },
  {
    "name": "국내주식 시간외현재가",
    "tr_id": "FHPST02300000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-overtime-price",
    "sheet": "국내주식 시간외현재가",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "주식현재가 시간외시간별체결",
    "tr_id": "FHPST02310000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-overtimeconclusion",
    "sheet": "주식현재가 시간외시간별체결",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J : 주식, ETF, ETN"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목번호 (6자리)\r\nETN의 경우, Q로 시작 (EX. Q500001)"
      },
      {
        "element": "FID_HOUR_CLS_CODE",
        "required": "Y",
        "description": "1 : 시간외 (Default)"
      }
    ]
  },
  {
    "name": "주식현재가 시간외일자별주가",
    "tr_id": "FHPST02320000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-overtimeprice",
    "sheet": "주식현재가 시간외일자별주가",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J : 주식, ETF, ETN"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목번호 (6자리)\r\nETN의 경우, Q로 시작 (EX. Q500001)"
      }
    ]
  },
  {
    "name": "국내주식 시간외호가",
    "tr_id": "FHPST02300400",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-overtime-asking-price",
    "sheet": "국내주식 시간외호가",
    "fields": [
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      }
    ]
  },
  {
    "name": "주식현재가 당일시간대별체결",
    "tr_id": "FHPST01060000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-itemconclusion",
    "sheet": "주식현재가 당일시간대별체결",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "입력시간"
      }
    ]
  },
  {
    "name": "주식현재가 시세2",
    "tr_id": "FHPST01010000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-price-2",
    "sheet": "주식현재가 시세2",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "000660"
      }
    ]
  },
  {
    "name": "주식일별분봉조회",
    "tr_id": "FHKST03010230",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-dailychartprice",
    "sheet": "주식일별분봉조회",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "입력 시간(ex 13시 130000)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "입력 날짜(20241023)"
      },
      {
        "element": "FID_PW_DATA_INCU_YN",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식기간별시세(일_주_월_년)",
    "tr_id": "FHKST03010100",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice",
    "sheet": "국내주식기간별시세(일_주_월_년)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "조회 시작일자"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "조회 종료일자 (최대 100개)"
      },
      {
        "element": "FID_PERIOD_DIV_CODE",
        "required": "Y",
        "description": "D:일봉 W:주봉, M:월봉, Y:년봉"
      },
      {
        "element": "FID_ORG_ADJ_PRC",
        "required": "Y",
        "description": "0:수정주가 1:원주가"
      }
    ]
  },
  {
    "name": "주식현재가 호가_예상체결",
    "tr_id": "FHKST01010200",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn",
    "sheet": "주식현재가 호가_예상체결",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "주식현재가 체결",
    "tr_id": "FHKST01010300",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-ccnl",
    "sheet": "주식현재가 체결",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "주식현재가 회원사",
    "tr_id": "FHKST01010600",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-member",
    "sheet": "주식현재가 회원사",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목번호 (6자리)\r\nETN의 경우, Q로 시작 (EX. Q500001)"
      }
    ]
  },
  {
    "name": "주식현재가 투자자",
    "tr_id": "FHKST01010900",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-investor",
    "sheet": "주식현재가 투자자",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J : KRX, NX : NXT, UN : 통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      }
    ]
  },
  {
    "name": "국내주식 장마감 예상체결가",
    "tr_id": "FHKST117300C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/exp-closing-price",
    "sheet": "국내주식 장마감 예상체결가",
    "fields": [
      {
        "element": "FID_RANK_SORT_CLS_CODE",
        "required": "Y",
        "description": "0:전체, 1:상한가마감예상, 2:하한가마감예상, 3:직전대비상승률상위 ,4:직전대비하락률상위"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "Unique key(11173)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200, 4001: KRX100"
      },
      {
        "element": "FID_BLNG_CLS_CODE",
        "required": "Y",
        "description": "0:전체, 1:종가범위연장"
      }
    ]
  },
  {
    "name": "주식당일분봉조회",
    "tr_id": "FHKST03010200",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice",
    "sheet": "주식당일분봉조회",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드 (ex 005930 삼성전자)"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "입력시간"
      },
      {
        "element": "FID_PW_DATA_INCU_YN",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_ETC_CLS_CODE",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "ELW 현재가 시세",
    "tr_id": "FHKEW15010000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-elw-price",
    "sheet": "ELW 현재가 시세",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "W"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목번호 (6자리)"
      }
    ]
  },
  {
    "name": "국내주식 예상체결지수 추이",
    "tr_id": "FHPST01840000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/exp-index-trend",
    "sheet": "국내주식 예상체결지수 추이",
    "fields": [
      {
        "element": "FID_MKOP_CLS_CODE",
        "required": "Y",
        "description": "1: 장시작전, 2: 장마감"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "10(10초), 30(30초), 60(1분), 600(10분)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0000:전체, 0001:코스피, 1001:코스닥, 2001:코스피200, 4001: KRX100"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (주식 U)"
      }
    ]
  },
  {
    "name": "국내주식업종기간별시세(일_주_월_년)",
    "tr_id": "FHKUP03500100",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice",
    "sheet": "국내주식업종기간별시세(일_주_월_년)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "업종 : U"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "'0001 : 종합\r\n0002 : 대형주\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)'"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "조회 시작일자 (ex. 20220501)"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "조회 종료일자 (ex. 20220530)"
      },
      {
        "element": "FID_PERIOD_DIV_CODE",
        "required": "Y",
        "description": "'\tD:일봉 W:주봉, M:월봉, Y:년봉'"
      }
    ]
  },
  {
    "name": "국내업종 시간별지수(분)",
    "tr_id": "FHPUP02110200",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-timeprice",
    "sheet": "국내업종 시간별지수(분)",
    "fields": [
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "초단위, 60(1분), 300(5분), 600(10분)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0001:거래소, 1001:코스닥, 2001:코스피200, 3003:KSQ150"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (업종 U)"
      }
    ]
  },
  {
    "name": "국내업종 구분별전체시세",
    "tr_id": "FHPUP02140000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-category-price",
    "sheet": "국내업종 구분별전체시세",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (업종 U)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "코스피(0001), 코스닥(1001), 코스피200(2001)\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "Unique key( 20214 )"
      },
      {
        "element": "FID_MRKT_CLS_CODE",
        "required": "Y",
        "description": "시장구분코드(K:거래소, Q:코스닥, K2:코스피200)"
      },
      {
        "element": "FID_BLNG_CLS_CODE",
        "required": "Y",
        "description": "시장구분코드에 따라 아래와 같이 입력\r\n시장구분코드(K:거래소) 0:전업종, 1:기타구분, 2:자본금구분 3:상업별구분\r\n시장구분코드(Q:코스닥) 0:전업종, 1:기타구분, 2:벤처구분 3:일반구분\r\n시장구분코드(K2:코스닥) 0:전업종"
      }
    ]
  },
  {
    "name": "업종 분봉조회",
    "tr_id": "FHKUP03500200",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-indexchartprice",
    "sheet": "업종 분봉조회",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "U"
      },
      {
        "element": "FID_ETC_CLS_CODE",
        "required": "Y",
        "description": "0: 기본 1:장마감,시간외 제외"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0001 : 종합\r\n0002 : 대형주\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "30, 60 -> 1분, 600-> 10분, 3600 -> 1시간"
      },
      {
        "element": "FID_PW_DATA_INCU_YN",
        "required": "Y",
        "description": "Y (과거) / N (당일)"
      }
    ]
  },
  {
    "name": "국내휴장일조회",
    "tr_id": "CTCA0903R",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/chk-holiday",
    "sheet": "국내휴장일조회",
    "fields": [
      {
        "element": "BASS_DT",
        "required": "Y",
        "description": "기준일자(YYYYMMDD)"
      },
      {
        "element": "CTX_AREA_NK",
        "required": "Y",
        "description": "공백으로 입력"
      },
      {
        "element": "CTX_AREA_FK",
        "required": "Y",
        "description": "공백으로 입력"
      }
    ]
  },
  {
    "name": "국내주식 예상체결 전체지수",
    "tr_id": "FHKUP11750000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/exp-total-index",
    "sheet": "국내주식 예상체결 전체지수",
    "fields": [
      {
        "element": "fid_mrkt_cls_code",
        "required": "Y",
        "description": "0:전체 K:거래소 Q:코스닥"
      },
      {
        "element": "fid_cond_mrkt_div_code",
        "required": "Y",
        "description": "시장구분코드 (업종 U)"
      },
      {
        "element": "fid_cond_scr_div_code",
        "required": "Y",
        "description": "Unique key(11175)"
      },
      {
        "element": "fid_input_iscd",
        "required": "Y",
        "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200, 4001: KRX100"
      },
      {
        "element": "fid_mkop_cls_code",
        "required": "Y",
        "description": "1:장시작전, 2:장마감"
      }
    ]
  },
  {
    "name": "국내업종 현재지수",
    "tr_id": "FHPUP02100000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-price",
    "sheet": "국내업종 현재지수",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "업종(U)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "코스피(0001), 코스닥(1001), 코스피200(2001)\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)"
      }
    ]
  },
  {
    "name": "국내선물 영업일조회",
    "tr_id": "HHMCM000002C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/market-time",
    "sheet": "국내선물 영업일조회",
    "fields": []
  },
  {
    "name": "국내업종 시간별지수(초)",
    "tr_id": "FHPUP02110100",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-tickprice",
    "sheet": "국내업종 시간별지수(초)",
    "fields": [
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0001:거래소, 1001:코스닥, 2001:코스피200, 3003:KSQ150"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (업종 U)"
      }
    ]
  },
  {
    "name": "국내업종 일자별지수",
    "tr_id": "FHPUP02120000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-daily-price",
    "sheet": "국내업종 일자별지수",
    "fields": [
      {
        "element": "FID_PERIOD_DIV_CODE",
        "required": "Y",
        "description": "일/주/월 구분코드 ( D:일별 , W:주별, M:월별 )"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (업종 U)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "코스피(0001), 코스닥(1001), 코스피200(2001)\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "입력 날짜(ex. 20240223)"
      }
    ]
  },
  {
    "name": "금리 종합(국내채권_금리)",
    "tr_id": "FHPST07020000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/comp-interest",
    "sheet": "금리 종합(국내채권_금리)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "Unique key(I)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "Unique key(20702)"
      },
      {
        "element": "FID_DIV_CLS_CODE",
        "required": "Y",
        "description": "1: 해외금리지표"
      },
      {
        "element": "FID_DIV_CLS_CODE1",
        "required": "Y",
        "description": "공백 : 전체"
      }
    ]
  },
  {
    "name": "변동성완화장치(VI) 현황",
    "tr_id": "FHPST01390000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-vi-status",
    "sheet": "변동성완화장치(VI) 현황",
    "fields": [
      {
        "element": "FID_DIV_CLS_CODE",
        "required": "Y",
        "description": "0:전체 1:상승 2:하락"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "20139"
      },
      {
        "element": "FID_MRKT_CLS_CODE",
        "required": "Y",
        "description": "0:전체 K:거래소 Q:코스닥"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_RANK_SORT_CLS_CODE",
        "required": "Y",
        "description": "0:전체1:정적2:동적3:정적&동적"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "영업일"
      },
      {
        "element": "FID_TRGT_CLS_CODE",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_TRGT_EXLS_CLS_CODE",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "종합 시황_공시(제목)",
    "tr_id": "FHKST01011800",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/news-title",
    "sheet": "종합 시황_공시(제목)",
    "fields": [
      {
        "element": "FID_NEWS_OFER_ENTP_CODE",
        "required": "Y",
        "description": "공백 필수 입력"
      },
      {
        "element": "FID_COND_MRKT_CLS_CODE",
        "required": "Y",
        "description": "공백 필수 입력"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "공백: 전체, 종목코드 : 해당코드가 등록된 뉴스"
      },
      {
        "element": "FID_TITL_CNTT",
        "required": "Y",
        "description": "공백 필수 입력"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "공백: 현재기준, 조회일자(ex 00YYYYMMDD)"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "공백: 현재기준, 조회시간(ex 0000HHMMSS)"
      },
      {
        "element": "FID_RANK_SORT_CLS_CODE",
        "required": "Y",
        "description": "공백 필수 입력"
      },
      {
        "element": "FID_INPUT_SRNO",
        "required": "Y",
        "description": "공백 필수 입력"
      }
    ]
  },
  {
    "name": "상품기본조회",
    "tr_id": "CTPF1604R",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/search-info",
    "sheet": "상품기본조회",
    "fields": [
      {
        "element": "PDNO",
        "required": "Y",
        "description": "'주식(하이닉스) :  000660 (코드 : 300)\r\n선물(101S12) :  KR4101SC0009 (코드 : 301)\r\n미국(AAPL) : AAPL (코드 : 512)'"
      },
      {
        "element": "PRDT_TYPE_CD",
        "required": "Y",
        "description": "'300 주식\r\n301 선물옵션\r\n302 채권\r\n512  미국 나스닥 / 513  미국 뉴욕 / 529  미국 아멕스 \r\n515  일본\r\n501  홍콩 / 543  홍콩CNY / 558  홍콩USD\r\n507  베트남 하노이 / 508  베트남 호치민\r\n551  중국 상해A / 552  중국 심천A'"
      }
    ]
  },
  {
    "name": "국내주식 증권사별 투자의견",
    "tr_id": "FHKST663400C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/invest-opbysec",
    "sheet": "국내주식 증권사별 투자의견",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J(시장 구분 코드)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "16634(Primary key)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "회원사코드 (kis developers 포탈 사이트 포럼-> FAQ -> 종목정보 다운로드(국내) 참조)"
      },
      {
        "element": "FID_DIV_CLS_CODE",
        "required": "Y",
        "description": "전체(0) 매수(1) 중립(2) 매도(3)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "이후 ~"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "~ 이전"
      }
    ]
  },
  {
    "name": "국내주식 당사 신용가능종목",
    "tr_id": "FHPST04770000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/credit-by-company",
    "sheet": "국내주식 당사 신용가능종목",
    "fields": [
      {
        "element": "fid_rank_sort_cls_code",
        "required": "Y",
        "description": "0:코드순, 1:이름순"
      },
      {
        "element": "fid_slct_yn",
        "required": "Y",
        "description": "0:신용주문가능, 1: 신용주문불가"
      },
      {
        "element": "fid_input_iscd",
        "required": "Y",
        "description": "0000:전체, 0001:거래소, 1001:코스닥, 2001:코스피200, 4001: KRX100"
      },
      {
        "element": "fid_cond_scr_div_code",
        "required": "Y",
        "description": "Unique key(20477)"
      },
      {
        "element": "fid_cond_mrkt_div_code",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      }
    ]
  },
  {
    "name": "국내주식 종목투자의견",
    "tr_id": "FHKST663300C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/invest-opinion",
    "sheet": "국내주식 종목투자의견",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J(시장 구분 코드)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "16633(Primary key)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드(ex) 005930(삼성전자))"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "이후 ~(ex) 0020231113)"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "~ 이전(ex) 0020240513)"
      }
    ]
  },
  {
    "name": "당사 대주가능 종목",
    "tr_id": "CTSC2702R",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/lendable-by-company",
    "sheet": "당사 대주가능 종목",
    "fields": [
      {
        "element": "EXCG_DVSN_CD",
        "required": "Y",
        "description": "00(전체), 02(거래소), 03(코스닥)"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "description": "공백 : 전체조회, 종목코드 입력 시 해당종목만 조회"
      },
      {
        "element": "THCO_STLN_PSBL_YN",
        "required": "Y",
        "description": "Y"
      },
      {
        "element": "INQR_DVSN_1",
        "required": "Y",
        "description": "0 : 전체조회, 1: 종목코드순 정렬"
      },
      {
        "element": "CTX_AREA_FK200",
        "required": "Y",
        "description": "미입력 (다음조회 불가)"
      },
      {
        "element": "CTX_AREA_NK100",
        "required": "Y",
        "description": "미입력 (다음조회 불가)"
      }
    ]
  },
  {
    "name": "주식기본조회",
    "tr_id": "CTPF1002R",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/search-stock-info",
    "sheet": "주식기본조회",
    "fields": [
      {
        "element": "PRDT_TYPE_CD",
        "required": "Y",
        "description": "300: 주식, ETF, ETN, ELW \r\n301 : 선물옵션 \r\n302 : 채권 \r\n306 : ELS'"
      },
      {
        "element": "PDNO",
        "required": "Y",
        "description": "종목번호 (6자리)\r\nETN의 경우, Q로 시작 (EX. Q500001)"
      }
    ]
  },
  {
    "name": "국내주식 종목추정실적",
    "tr_id": "HHKST668300C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/estimate-perform",
    "sheet": "국내주식 종목추정실적",
    "fields": [
      {
        "element": "SHT_CD",
        "required": "Y",
        "description": "ex) 265520"
      }
    ]
  },
  {
    "name": "프로그램매매 종합현황(시간)",
    "tr_id": "FHPPG04600101",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/comp-program-trade-today",
    "sheet": "프로그램매매 종합현황(시간)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "KRX : J , NXT : NX, 통합 : UN"
      },
      {
        "element": "FID_MRKT_CLS_CODE",
        "required": "Y",
        "description": "K:코스피, Q:코스닥"
      },
      {
        "element": "FID_SCTN_CLS_CODE",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE1",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "공백 입력"
      }
    ]
  },
  {
    "name": "국내주식 신용잔고 일별추이",
    "tr_id": "FHPST04760000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/daily-credit-balance",
    "sheet": "국내주식 신용잔고 일별추이",
    "fields": [
      {
        "element": "fid_cond_mrkt_div_code",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      },
      {
        "element": "fid_cond_scr_div_code",
        "required": "Y",
        "description": "Unique key(20476)"
      },
      {
        "element": "fid_input_iscd",
        "required": "Y",
        "description": "종목코드 (ex 005930)"
      },
      {
        "element": "fid_input_date_1",
        "required": "Y",
        "description": "결제일자 (ex 20240313)"
      }
    ]
  },
  {
    "name": "시장별 투자자매매동향(일별)",
    "tr_id": "FHPTJ04040000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-investor-daily-by-market",
    "sheet": "시장별 투자자매매동향(일별)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (업종 U)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "코스피, 코스닥 : 업종분류코드 (종목정보파일 - 업종코드 참조)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "ex. 20240517"
      },
      {
        "element": "FID_INPUT_ISCD_1",
        "required": "Y",
        "description": "코스피(KSP), 코스닥(KSQ)"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "입력 날짜1과 동일날짜 입력"
      },
      {
        "element": "FID_INPUT_ISCD_2",
        "required": "Y",
        "description": "코스피, 코스닥 : 업종분류코드 (종목정보파일 - 업종코드 참조)"
      }
    ]
  },
  {
    "name": "국내주식 공매도 일별추이",
    "tr_id": "FHPST04830000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/daily-short-sale",
    "sheet": "국내주식 공매도 일별추이",
    "fields": [
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "~ 누적"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "공백시 전체 (기간 ~)"
      }
    ]
  },
  {
    "name": "종목별 투자자매매동향(일별)",
    "tr_id": "FHPTJ04160001",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/investor-trade-by-stock-daily",
    "sheet": "종목별 투자자매매동향(일별)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목번호 (6자리)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "입력 날짜(20250812) (해당일 조회는 장 종료 후 정상 조회 가능)"
      },
      {
        "element": "FID_ORG_ADJ_PRC",
        "required": "Y",
        "description": "공란 입력"
      },
      {
        "element": "FID_ETC_CLS_CODE",
        "required": "Y",
        "description": "\"1\" 입력"
      }
    ]
  },
  {
    "name": "종목조건검색 목록조회",
    "tr_id": "HHKST03900300",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/psearch-title",
    "sheet": "종목조건검색 목록조회",
    "fields": [
      {
        "element": "user_id",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 상하한가 포착",
    "tr_id": "FHKST130000C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/capture-uplowprice",
    "sheet": "국내주식 상하한가 포착",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분(J)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "11300(Unique key)"
      },
      {
        "element": "FID_PRC_CLS_CODE",
        "required": "Y",
        "description": "0(상한가),1(하한가)"
      },
      {
        "element": "FID_DIV_CLS_CODE",
        "required": "Y",
        "description": "'0(상하한가종목),6(8%상하한가 근접), 5(10%상하한가 근접), 1(15%상하한가 근접),2(20%상하한가 근접),\r\n3(25%상하한가 근접)'"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "전체(0000), 코스피(0001),코스닥(1001)"
      },
      {
        "element": "FID_TRGT_CLS_CODE",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_TRGT_EXLS_CLS_CODE",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_INPUT_PRICE_1",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_INPUT_PRICE_2",
        "required": "Y",
        "description": "공백 입력"
      },
      {
        "element": "FID_VOL_CNT",
        "required": "Y",
        "description": "공백 입력"
      }
    ]
  },
  {
    "name": "프로그램매매 종합현황(일별)",
    "tr_id": "FHPPG04600001",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/comp-program-trade-daily",
    "sheet": "프로그램매매 종합현황(일별)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J : KRX, NX : NXT, UN : 통합"
      },
      {
        "element": "FID_MRKT_CLS_CODE",
        "required": "Y",
        "description": "K:코스피, Q:코스닥"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "공백 입력, 입력 시 ~ 입력일자까지 조회됨\r\n* 8개월 이상 과거 조회 불가"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "공백 입력"
      }
    ]
  },
  {
    "name": "종목별 일별 대차거래추이",
    "tr_id": "HHPST074500C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/daily-loan-trans",
    "sheet": "종목별 일별 대차거래추이",
    "fields": [
      {
        "element": "MRKT_DIV_CLS_CODE",
        "required": "Y",
        "description": "1(코스피), 2(코스닥), 3(종목)"
      },
      {
        "element": "MKSC_SHRN_ISCD",
        "required": "Y",
        "description": "종목코드"
      },
      {
        "element": "START_DATE",
        "required": "Y",
        "description": "조회기간 ~"
      },
      {
        "element": "END_DATE",
        "required": "Y",
        "description": "~ 조회기간"
      },
      {
        "element": "CTS",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "종목조건검색조회",
    "tr_id": "HHKST03900400",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/psearch-result",
    "sheet": "종목조건검색조회",
    "fields": [
      {
        "element": "user_id",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seq",
        "required": "Y",
        "description": "종목조건검색 목록조회 API의 output인 'seq'을 이용\r\n(0 부터 시작)"
      }
    ]
  },
  {
    "name": "국내주식 매물대_거래비중",
    "tr_id": "FHPST01130000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/pbar-tratio",
    "sheet": "국내주식 매물대_거래비중",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT, UN:통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "주식단축종목코드"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "Uniquekey(20113)"
      },
      {
        "element": "FID_INPUT_HOUR_1",
        "required": "Y",
        "description": "공백"
      }
    ]
  },
  {
    "name": "국내기관_외국인 매매종목가집계",
    "tr_id": "FHPTJ04400000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/foreign-institution-total",
    "sheet": "국내기관_외국인 매매종목가집계",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "V(Default)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "16449(Default)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0000:전체, 0001:코스피, 1001:코스닥\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)"
      },
      {
        "element": "FID_DIV_CLS_CODE",
        "required": "Y",
        "description": "0: 수량정열, 1: 금액정열"
      },
      {
        "element": "FID_RANK_SORT_CLS_CODE",
        "required": "Y",
        "description": "0: 순매수상위, 1: 순매도상위"
      },
      {
        "element": "FID_ETC_CLS_CODE",
        "required": "Y",
        "description": "0:전체 1:외국인 2:기관계 3:기타"
      }
    ]
  },
  {
    "name": "관심종목 그룹별 종목조회",
    "tr_id": "HHKCM113004C6",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/intstock-stocklist-by-group",
    "sheet": "관심종목 그룹별 종목조회",
    "fields": [
      {
        "element": "TYPE",
        "required": "Y",
        "description": "Unique key(1)"
      },
      {
        "element": "USER_ID",
        "required": "Y",
        "description": "HTS_ID 입력"
      },
      {
        "element": "DATA_RANK",
        "required": "Y",
        "description": "공백"
      },
      {
        "element": "INTER_GRP_CODE",
        "required": "Y",
        "description": "관심그룹 조회 결과의 그룹 값 입력"
      },
      {
        "element": "INTER_GRP_NAME",
        "required": "Y",
        "description": "공백"
      },
      {
        "element": "HTS_KOR_ISNM",
        "required": "Y",
        "description": "공백"
      },
      {
        "element": "CNTG_CLS_CODE",
        "required": "Y",
        "description": "공백"
      },
      {
        "element": "FID_ETC_CLS_CODE",
        "required": "Y",
        "description": "Unique key(4)"
      }
    ]
  },
  {
    "name": "주식현재가 회원사 종목매매동향",
    "tr_id": "FHPST04540000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-member-daily",
    "sheet": "주식현재가 회원사 종목매매동향",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J: KRX, NX: NXT, UN: 통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "주식종목코드입력"
      },
      {
        "element": "FID_INPUT_ISCD_2",
        "required": "Y",
        "description": "회원사코드 (kis developers 포탈 사이트 포럼-> FAQ -> 종목정보 다운로드(국내) > 회원사 참조)"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "날짜 ~"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "~ 날짜"
      },
      {
        "element": "FID_SCTN_CLS_CODE",
        "required": "Y",
        "description": "공백"
      }
    ]
  },
  {
    "name": "종목별 프로그램매매추이(일별)",
    "tr_id": "FHPPG04650201",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/program-trade-by-stock-daily",
    "sheet": "종목별 프로그램매매추이(일별)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "KRX : J , NXT : NX, 통합 : UN"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "기준일 (ex 0020240308), 미입력시 당일부터 조회"
      }
    ]
  },
  {
    "name": "관심종목 그룹조회",
    "tr_id": "HHKCM113004C7",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/intstock-grouplist",
    "sheet": "관심종목 그룹조회",
    "fields": [
      {
        "element": "TYPE",
        "required": "Y",
        "description": "Unique key(1)"
      },
      {
        "element": "FID_ETC_CLS_CODE",
        "required": "Y",
        "description": "Unique key(00)"
      },
      {
        "element": "USER_ID",
        "required": "Y",
        "description": "HTS_ID 입력"
      }
    ]
  },
  {
    "name": "종목별 외인기관 추정가집계",
    "tr_id": "HHPTJ04160200",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/investor-trend-estimate",
    "sheet": "종목별 외인기관 추정가집계",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "required": "Y",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "종목별일별매수매도체결량",
    "tr_id": "FHKST03010800",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-trade-volume",
    "sheet": "종목별일별매수매도체결량",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J: KRX, NX: NXT, UN: 통합"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "005930"
      },
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": "from"
      },
      {
        "element": "FID_INPUT_DATE_2",
        "required": "Y",
        "description": "to"
      },
      {
        "element": "FID_PERIOD_DIV_CODE",
        "required": "Y",
        "description": "D"
      }
    ]
  },
  {
    "name": "국내주식 체결금액별 매매비중",
    "tr_id": "FHKST111900C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/tradprt-byamt",
    "sheet": "국내주식 체결금액별 매매비중",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J: KRX, NX: NXT, UN: 통합"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "Uniquekey(11119)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드(ex)(005930 (삼성전자))"
      }
    ]
  },
  {
    "name": "프로그램매매 투자자매매동향(당일)",
    "tr_id": "HHPPG046600C1",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/investor-program-trade-today",
    "sheet": "프로그램매매 투자자매매동향(당일)",
    "fields": [
      {
        "element": "EXCH_DIV_CLS_CODE",
        "required": "Y",
        "description": "J : KRX, NX : NXT, UN : 통합"
      },
      {
        "element": "MRKT_DIV_CLS_CODE",
        "required": "Y",
        "description": "1:코스피, 4:코스닥"
      }
    ]
  },
  {
    "name": "국내 증시자금 종합",
    "tr_id": "FHKST649100C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/mktfunds",
    "sheet": "국내 증시자금 종합",
    "fields": [
      {
        "element": "FID_INPUT_DATE_1",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 예상체결가 추이",
    "tr_id": "FHPST01810000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/exp-price-trend",
    "sheet": "국내주식 예상체결가 추이",
    "fields": [
      {
        "element": "fid_mkop_cls_code",
        "required": "Y",
        "description": "0:전체, 4:체결량 0 제외"
      },
      {
        "element": "fid_cond_mrkt_div_code",
        "required": "Y",
        "description": "시장구분코드 (주식 J)"
      },
      {
        "element": "fid_input_iscd",
        "required": "Y",
        "description": "종목코드(ex. 005930)"
      }
    ]
  },
  {
    "name": "회원사 실시간 매매동향(틱)",
    "tr_id": "FHPST04320000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-trade-trend",
    "sheet": "회원사 실시간 매매동향(틱)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J 고정 입력"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "20432(primary key)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "ex. 005930(삼성전자) \r\n\r\n※ FID_INPUT_ISCD(종목코드) 혹은 FID_MRKT_CLS_CODE(시장구분코드) 둘 중 하나만 입력"
      },
      {
        "element": "FID_INPUT_ISCD_2",
        "required": "Y",
        "description": "ex. 99999(전체)\r\n\r\n※ 회원사코드 (kis developers 포탈 사이트 포럼-> FAQ -> 종목정보 다운로드(국내) 참조)"
      },
      {
        "element": "FID_MRKT_CLS_CODE",
        "required": "Y",
        "description": "A(전체),K(코스피), Q(코스닥), K2(코스피200), W(ELW)\r\n\r\n※ FID_INPUT_ISCD(종목코드) 혹은 FID_MRKT_CLS_CODE(시장구분코드) 둘 중 하나만 입력"
      },
      {
        "element": "FID_VOL_CNT",
        "required": "Y",
        "description": "거래량 ~"
      }
    ]
  },
  {
    "name": "시장별 투자자매매동향(시세)",
    "tr_id": "FHPTJ04030000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market",
    "sheet": "시장별 투자자매매동향(시세)",
    "fields": [
      {
        "element": "fid_input_iscd",
        "required": "Y",
        "description": "코스피: KSP, 코스닥:KSQ,\r\n선물,콜옵션,풋옵션 : K2I, 주식선물:999,\r\nETF: ETF, ELW:ELW, ETN: ETN, \r\n미니: MKI, 위클리월 : WKM, 위클리목: WKI\r\n코스닥150: KQI"
      },
      {
        "element": "fid_input_iscd_2",
        "required": "Y",
        "description": "- fid_input_iscd: KSP(코스피) 혹은 KSQ(코스닥)인 경우\r\n코스피(0001_종합, .…0027_제조업 )\r\n코스닥(1001_종합, …. 1041_IT부품)\r\n...\r\n포탈 (FAQ : 종목정보 다운로드(국내) - 업종코드 참조)\r\n\r\n- fid_input_iscd가 K2I인 경우\r\nF001(선물)\r\nOC01(콜옵션)\r\nOP01(풋옵션)\r\n\r\n- fid_input_iscd가 999인 경우\r\nS001(주식선물)\r\n\r\n- fid_input_iscd가 ETF인 경우\r\nT000(ETF)\r\n\r\n- fid_input_iscd가 ELW인 경우\r\nW000(ELW)\r\n\r\n- fid_input_iscd가 ETN인 경우\r\nE199(ETN)\r\n\r\n- fid_input_iscd가 MKI인 경우\r\nF004(미니선물)\r\nOC02(미니콜옵션)\r\nOP02(미니풋옵션)\r\n\r\n- fid_input_iscd가 WKM인 경우\r\nOC05(위클리콜(월))\r\nOP05(위클리풋(월))\r\n\r\n- fid_input_iscd가 WKI인 경우\r\nOC04(위클리콜(목))\r\nOP04(위클리풋(목))   \r\n\r\n- fid_input_iscd가 KQI인 경우\r\nF002(코스닥150선물)\r\nOC03(코스닥150콜옵션)\r\nOP03(코스닥150풋옵션)"
      }
    ]
  },
  {
    "name": "종목별 프로그램매매추이(체결)",
    "tr_id": "FHPPG04650101",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/program-trade-by-stock",
    "sheet": "종목별 프로그램매매추이(체결)",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "KRX : J , NXT : NX, 통합 : UN"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드"
      }
    ]
  },
  {
    "name": "외국계 매매종목 가집계",
    "tr_id": "FHKST644100C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-trade-estimate",
    "sheet": "외국계 매매종목 가집계",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "시장구분코드 (J)"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "Uniquekey (16441)"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0000(전체), 1001(코스피), 2001(코스닥)"
      },
      {
        "element": "FID_RANK_SORT_CLS_CODE",
        "required": "Y",
        "description": "0(금액순), 1(수량순)"
      },
      {
        "element": "FID_RANK_SORT_CLS_CODE_2",
        "required": "Y",
        "description": "0(매수순), 1(매도순)"
      }
    ]
  },
  {
    "name": "종목별 외국계 순매수추이",
    "tr_id": "FHKST644400C0",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-pchs-trend",
    "sheet": "종목별 외국계 순매수추이",
    "fields": [
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "종목코드(ex) 005930(삼성전자))"
      },
      {
        "element": "FID_INPUT_ISCD_2",
        "required": "Y",
        "description": "외국계 전체(99999)"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J (KRX만 지원)"
      }
    ]
  },
  {
    "name": "관심종목(멀티종목) 시세조회",
    "tr_id": "FHKST11300006",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/intstock-multprice",
    "sheet": "관심종목(멀티종목) 시세조회",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE_1",
        "required": "Y",
        "description": "그룹별종목조회 결과 fid_mrkt_cls_code(시장구분) 1 입력\r\nJ: KRX, NX: NXT, UN: 통합\r\nex) J"
      },
      {
        "element": "FID_INPUT_ISCD_1",
        "required": "Y",
        "description": "그룹별종목조회 결과 jong_code(종목코드) 1 입력\r\nex) 005930"
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_2",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_2",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_3",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_3",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_4",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_4",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_5",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_5",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_6",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_6",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_7",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_7",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_8",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_8",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_9",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_9",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_10",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_10",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_11",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_11",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_12",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_12",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_13",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_13",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_14",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_14",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_15",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_15",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_16",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_16",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_17",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_17",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_18",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_18",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_19",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_19",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_20",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_20",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_21",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_21",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_22",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_22",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_23",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_23",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_24",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_24",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_25",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_25",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_26",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_26",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_27",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_27",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_28",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_28",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_29",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_29",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_30",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_INPUT_ISCD_30",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "거래량순위",
    "tr_id": "FHPST01710000",
    "method": "GET",
    "url": "/uapi/domestic-stock/v1/quotations/volume-rank",
    "sheet": "거래량순위",
    "fields": [
      {
        "element": "FID_COND_MRKT_DIV_CODE",
        "required": "Y",
        "description": "J:KRX, NX:NXT"
      },
      {
        "element": "FID_COND_SCR_DIV_CODE",
        "required": "Y",
        "description": "20171"
      },
      {
        "element": "FID_INPUT_ISCD",
        "required": "Y",
        "description": "0000(전체) 기타(업종코드)"
      },
      {
        "element": "FID_DIV_CLS_CODE",
        "required": "Y",
        "description": "0(전체) 1(보통주) 2(우선주)"
      },
      {
        "element": "FID_BLNG_CLS_CODE",
        "required": "Y",
        "description": "0 : 평균거래량 1:거래증가율 2:평균거래회전율 3:거래금액순 4:평균거래금액회전율"
      },
      {
        "element": "FID_TRGT_CLS_CODE",
        "required": "Y",
        "description": "1 or 0 9자리 (차례대로 증거금 30% 40% 50% 60% 100% 신용보증금 30% 40% 50% 60%)\r\nex) \"111111111\""
      },
      {
        "element": "FID_TRGT_EXLS_CLS_CODE",
        "required": "Y",
        "description": "1 or 0 10자리 (차례대로 투자위험/경고/주의 관리종목 정리매매 불성실공시 우선주 거래정지 ETF ETN 신용주문불가 SPAC)\r\nex) \"0000000000\""
      },
      {
        "element": "FID_INPUT_PRICE_1",
        "required": "Y",
        "description": "가격 ~\r\nex) \"0\"\r\n\r\n전체 가격 대상 조회 시 FID_INPUT_PRICE_1, FID_INPUT_PRICE_2 모두 \"\"(공란) 입력"
      },
      {
        "element": "FID_INPUT_PRICE_2",
        "required": "Y",
        "description": "~ 가격\r\nex) \"1000000\"\r\n\r\n전체 가격 대상 조회 시 FID_INPUT_PRICE_1, FID_INPUT_PRICE_2 모두 \"\"(공란) 입력"
      },
      {
        "element": "FID_VOL_CNT",
        "required": "Y",
        "description": "거래량 ~\r\nex) \"100000\"\r\n\r\n전체 거래량 대상 조회 시 FID_VOL_CNT \"\"(공란) 입력"
      }
    ]
  }
]"""


def load_quotations_api_specs() -> list[dict[str, Any]]:
    return json.loads(_REQUEST_SPECS_JSON)


QUOTATIONS_API_SPECS = load_quotations_api_specs()
