"""국내주식 websocket/quotations 혼합 응답 스펙."""

from __future__ import annotations

import json
from typing import Any


_RESPONSE_SPECS_JSON = r"""[
  {
    "name": "채권지수 실시간체결가",
    "url": "/tryitout/H0BICNT0",
    "tr_id": "H0BICNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "채권지수 실시간체결가",
    "fields": [
      {
        "element": "NMIX_ID",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STND_DATE1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRNM_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_TOTL_ERNN_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX_PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTL_ERNN_NMIX_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CLEN_PRC_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_PRC_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_CALL_RNVS_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_ZERO_RNVS_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_FUTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_AVRG_DRTN_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_AVRG_CNVX_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_AVRG_YTM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_AVRG_FRDL_YTM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "일반채권 실시간호가",
    "url": "/tryitout/H0BJASP0",
    "tr_id": "H0BJCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "일반채권 실시간호가",
    "fields": [
      {
        "element": "STND_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_ERT1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_ERT1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_ERT2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_ERT2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_ERT3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_ERT3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_ERT4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_ERT4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_ERT5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_ERT5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN52",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN53",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "일반채권 실시간체결가",
    "url": "/tryitout/H0BJCNT0",
    "tr_id": "H0BJCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "일반채권 실시간체결가",
    "fields": [
      {
        "element": "STND_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_ISNM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRDY_CLPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BOND_CNTG_ERT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_ERT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_ERT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_ERT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_TYPE_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "상품선물 실시간호가",
    "url": "/tryitout/H0CFASP0",
    "tr_id": "H0CFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "상품선물 실시간호가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "상품선물 실시간체결가",
    "url": "/tryitout/H0CFCNT0",
    "tr_id": "H0CFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "상품선물 실시간체결가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SPEAD_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DSCS_BLTR_ACML_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_MXPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_LLAM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_PRC_LIMT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간옵션실시간예상체결",
    "url": "/tryitout/H0EUANC0",
    "tr_id": "H0EUANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션실시간예상체결",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNQN",
        "type": "number",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간옵션 실시간호가",
    "url": "/tryitout/H0EUASP0",
    "tr_id": "H0EUASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션 실시간호가",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간옵션실시간체결통보",
    "url": "/tryitout/H0EUCNI0",
    "tr_id": "H0MFCNI0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션실시간체결통보",
    "fields": [
      {
        "element": "CUST_ID",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_BYOV_CLS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RCTF_CLS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_KIND2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_UNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RFUS_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACPT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BRNC_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NAME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_ISNM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_COND",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간옵션 실시간체결가",
    "url": "/tryitout/H0EUCNT0",
    "tr_id": "H0EUCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간옵션 실시간체결가",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "INVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TMVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DELTA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GAMA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VEGA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THETA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RHO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_INTS_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "UNAS_HIST_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_MXPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_PRC_LIMT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_LLAM",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "ELW 실시간예상체결",
    "url": "/tryitout/H0EWANC0",
    "tr_id": "H0EWANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "ELW 실시간예상체결",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TMVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRIT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GEAR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRLS_QRYR_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "INVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CFP",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LVRG_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DELTA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GAMA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VEGA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THETA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RHO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_INTS_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_HVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_HLDN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "ELW 실시간호가",
    "url": "/tryitout/H0EWASP0",
    "tr_id": "H0EWASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "ELW 실시간호가",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_ASKP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "ELW 실시간체결가",
    "url": "/tryitout/H0EWCNT0",
    "tr_id": "H0EWCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "ELW 실시간체결가",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TMVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRIT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GEAR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRLS_QRYR_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "INVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CFP",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LVRG_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DELTA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GAMA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VEGA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THETA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RHO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_INTS_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "APPRCH_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_HVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_HLDN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LP_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외주식 실시간체결통보",
    "url": "/tryitout/H0GSCNI0",
    "tr_id": "H0GSCNI0",
    "tr_id_demo": "H0GSCNI9",
    "sheet": "해외주식 실시간체결통보",
    "fields": [
      {
        "element": "CUST_ID",
        "type": "string",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "ACNT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_BYOV_CLS",
        "type": "string",
        "required": "Y",
        "description": "01:매도 02:매수 03:전매도 04:환매수"
      },
      {
        "element": "RCTF_CLS",
        "type": "string",
        "required": "Y",
        "description": "0:정상 1:정정 2:취소"
      },
      {
        "element": "ODER_KIND2",
        "type": "string",
        "required": "Y",
        "description": "1:시장가 2:지정자 6:단주시장가 7:단주지정가\r\nA:MOO B:LOO C:MOC D:LOC"
      },
      {
        "element": "STCK_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_QTY",
        "type": "string",
        "required": "Y",
        "description": "- 주문통보의 경우 해당 위치에 주문수량이 출력\r\n- 체결통보인 경우 해당 위치에 체결수량이 출력"
      },
      {
        "element": "CNTG_UNPR",
        "type": "string",
        "required": "Y",
        "description": "※ 주문통보 시에는 주문단가가, 체결통보 시에는 체결단가가 수신 됩니다.\r\n※ 체결단가의 경우, 국가에 따라 소수점 생략 위치가 상이합니다.\r\n미국 4 일본 1 중국 3 홍콩 3 베트남 0\r\nEX) 미국 AAPL(현재가 : 148.0100)의 경우 001480100으로 체결단가가 오는데, \r\n4번째 자리에 소수점을 찍어 148.01로 해석하시면 됩니다."
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": "특정 거래소의 체결시간 데이터는 수신되지 않습니다. \r\n체결시간 데이터가 필요할 경우, 체결통보 데이터 수신 시 타임스탬프를 찍는 것으로 대체하시길 바랍니다."
      },
      {
        "element": "RFUS_YN",
        "type": "string",
        "required": "Y",
        "description": "0:정상 1:거부"
      },
      {
        "element": "CNTG_YN",
        "type": "string",
        "required": "Y",
        "description": "1:주문,정정,취소,거부 2:체결"
      },
      {
        "element": "ACPT_YN",
        "type": "string",
        "required": "Y",
        "description": "1:주문접수 2:확인 3:취소(FOK/IOC)"
      },
      {
        "element": "BRNC_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_QTY",
        "type": "string",
        "required": "Y",
        "description": "- 주문통보인 경우 해당 위치 미출력 (주문통보의 주문수량은 CNTG_QTY 위치에 출력)\r\n- 체결통보인 경우 해당 위치에 주문수량이 출력"
      },
      {
        "element": "ACNT_NAME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_ISNM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_COND",
        "type": "string",
        "required": "Y",
        "description": "4:홍콩(HKD) 5:상해B(USD) \r\n6:NASDAQ 7:NYSE 8:AMEX 9:OTCB\r\nC:홍콩(CNY) A:상해A(CNY) B:심천B(HKD)\r\nD:도쿄 E:하노이 F:호치민"
      },
      {
        "element": "DEBT_GB",
        "type": "string",
        "required": "Y",
        "description": "10:현금 15:해외주식담보대출"
      },
      {
        "element": "DEBT_DATE",
        "type": "string",
        "required": "Y",
        "description": "대출일(YYYYMMDD)"
      },
      {
        "element": "START_TM",
        "type": "string",
        "required": "Y",
        "description": "HHMMSS"
      },
      {
        "element": "END_TM",
        "type": "string",
        "required": "Y",
        "description": "HHMMSS"
      },
      {
        "element": "TM_DIV_TP",
        "type": "string",
        "required": "Y",
        "description": "00 시간직접설정, 02 : 정규장까지"
      },
      {
        "element": "CNTG_UNPR12",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "지수선물 실시간호가",
    "url": "/tryitout/H0IFASP0",
    "tr_id": "H0IFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수선물 실시간호가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "선물옵션 실시간체결통보",
    "url": "/tryitout/H0IFCNI0",
    "tr_id": "H0IFCNI0",
    "tr_id_demo": "H0IFCNI9",
    "sheet": "선물옵션 실시간체결통보",
    "fields": [
      {
        "element": "CUST_ID",
        "type": "array",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "ACNT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_BYOV_CLS",
        "type": "string",
        "required": "Y",
        "description": "01:매도, 02매수"
      },
      {
        "element": "RCTF_CLS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_KIND2",
        "type": "string",
        "required": "Y",
        "description": "L: 주문접수통보, 0: 체결통보"
      },
      {
        "element": "STCK_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_UNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RFUS_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_YN",
        "type": "string",
        "required": "Y",
        "description": "1: 주문,정정,취소,거부 통보, 2 체결"
      },
      {
        "element": "ACPT_YN",
        "type": "string",
        "required": "Y",
        "description": "1:주문접수, 2:확인, 3, 취소"
      },
      {
        "element": "BRNC_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NAME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_ISNM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_COND",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_GRP",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_GRPSEQ",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORDER_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "지수선물 실시간체결가",
    "url": "/tryitout/H0IFCNT0",
    "tr_id": "H0IFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수선물 실시간체결가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": "체결량"
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SPEAD_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DSCS_BLTR_ACML_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_MXPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_LLAM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_PRC_LIMT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "지수옵션 실시간호가",
    "url": "/tryitout/H0IOASP0",
    "tr_id": "H0IOASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수옵션 실시간호가",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "지수옵션  실시간체결가",
    "url": "/tryitout/H0IOCNT0",
    "tr_id": "H0IOCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "지수옵션  실시간체결가",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "INVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TMVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DELTA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GAMA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VEGA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THETA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RHO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_INTS_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "UNAS_HIST_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "AVRG_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DSCS_LRQN_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_MXPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_LLAM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_PRC_LIMT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간선물 실시간호가",
    "url": "/tryitout/H0MFASP0",
    "tr_id": "H0MFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간선물 실시간호가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간선물 실시간체결통보",
    "url": "/tryitout/H0MFCNI0",
    "tr_id": "H0MFCNI0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간선물 실시간체결통보",
    "fields": [
      {
        "element": "CUST_ID",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_BYOV_CLS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RCTF_CLS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_KIND2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_UNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RFUS_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACPT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BRNC_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NAME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_ISNM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_COND",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "KRX야간선물 실시간종목체결",
    "url": "/tryitout/H0MFCNT0",
    "tr_id": "H0MFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "KRX야간선물 실시간종목체결",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SPEAD_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_MXPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_LLAM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_PRC_LIMT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간예상체결 (NXT)",
    "url": "/tryitout/H0NXANC0",
    "tr_id": "H0NXANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간예상체결 (NXT)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VI_STND_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간호가 (NXT)",
    "url": "/tryitout/H0NXASP0",
    "tr_id": "H0NXASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간호가 (NXT)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_DEAL_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KMID_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KMID_TOTAL_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KMID_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMID_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMID_TOTAL_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMID_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간체결가 (NXT)",
    "url": "/tryitout/H0NXCNT0",
    "tr_id": "H0NXCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간체결가 (NXT)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VI_STND_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간회원사 (NXT)",
    "url": "/tryitout/H0NXMBC0",
    "tr_id": "H0NXMBC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간회원사 (NXT)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SELN_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SHNU_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SELN_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SHNU_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_SELN_RLIM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_SHNU_RLIM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간프로그램매매 (NXT)",
    "url": "/tryitout/H0NXPGM0",
    "tr_id": "H0NXPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간프로그램매매 (NXT)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간예상체결 (KRX)",
    "url": "/tryitout/H0STANC0",
    "tr_id": "H0STANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간예상체결 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간호가 (KRX)",
    "url": "/tryitout/H0STASP0",
    "tr_id": "H0STASP0",
    "tr_id_demo": "H0STASP0",
    "sheet": "국내주식 실시간호가 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "0 : 장중\r\nA : 장후예상\r\nB : 장전예상\r\nC : 9시이후의 예상가, VI발동\r\nD : 시간외 단일가 예상"
      },
      {
        "element": "ASKP1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP6",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP7",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP8",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP9",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP10",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP6",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP7",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP8",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP9",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP10",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN10",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN10",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_RSQN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_RSQN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "number",
        "required": "Y",
        "description": "동시호가 등 특정 조건하에서만 발생"
      },
      {
        "element": "ANTC_CNQN",
        "type": "number",
        "required": "Y",
        "description": "동시호가 등 특정 조건하에서만 발생"
      },
      {
        "element": "ANTC_VOL",
        "type": "number",
        "required": "Y",
        "description": "동시호가 등 특정 조건하에서만 발생"
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "number",
        "required": "Y",
        "description": "동시호가 등 특정 조건하에서만 발생"
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": "동시호가 등 특정 조건하에서만 발생\r\n\r\n1 : 상한\r\n2 : 상승\r\n3 : 보합\r\n4 : 하한\r\n5 : 하락"
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_ICDC",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_ICDC",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_DEAL_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "사용 X (삭제된 값)"
      }
    ]
  },
  {
    "name": "국내주식 실시간체결통보",
    "url": "/tryitout/H0STCNI0",
    "tr_id": "H0STCNI0",
    "tr_id_demo": "H0STCNI9",
    "sheet": "국내주식 실시간체결통보",
    "fields": [
      {
        "element": "CUST_ID",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OODER_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_BYOV_CLS",
        "type": "string",
        "required": "Y",
        "description": "01 : 매도 \r\n02 : 매수"
      },
      {
        "element": "RCTF_CLS",
        "type": "string",
        "required": "Y",
        "description": "0:정상 \r\n1:정정 \r\n2:취소"
      },
      {
        "element": "ODER_KIND",
        "type": "string",
        "required": "Y",
        "description": "[KRX]\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n05 : 장전 시간외\r\n06 : 장후 시간외\r\n07 : 시간외 단일가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[NXT]\r\n00 : 지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[SOR]\r\n00 : 지정가\r\n01 : 시장가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)"
      },
      {
        "element": "ODER_COND",
        "type": "string",
        "required": "Y",
        "description": "0:없음\r\n1:IOC \r\n2:FOK"
      },
      {
        "element": "STCK_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_UNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RFUS_YN",
        "type": "string",
        "required": "Y",
        "description": "0 : 승인 \r\n1 : 거부"
      },
      {
        "element": "CNTG_YN",
        "type": "string",
        "required": "Y",
        "description": "1 : 주문,정정,취소,거부\r\n2 : 체결"
      },
      {
        "element": "ACPT_YN",
        "type": "string",
        "required": "Y",
        "description": "1 : 주문접수\r\n2 : 확인\r\n3 : 취소(FOK/IOC)"
      },
      {
        "element": "BRNC_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACNT_NAME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_COND_PRC",
        "type": "string",
        "required": "Y",
        "description": "스톱지정가 시 표시"
      },
      {
        "element": "ORD_EXG_GB",
        "type": "string",
        "required": "Y",
        "description": "1:KRX, 2:NXT, 3:SOR-KRX, 4:SOR-NXT"
      },
      {
        "element": "POPUP_YN",
        "type": "string",
        "required": "Y",
        "description": "Y/N"
      },
      {
        "element": "FILLER",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CRDT_CLS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CRDT_LOAN_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_ISNM40",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODER_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간체결가 (KRX)",
    "url": "/tryitout/H0STCNT0",
    "tr_id": "H0STCNT0",
    "tr_id_demo": "H0STCNT0",
    "sheet": "국내주식 실시간체결가 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "number",
        "required": "Y",
        "description": "체결가격"
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": "1 : 상한\r\n2 : 상승\r\n3 : 보합\r\n4 : 하한\r\n5 : 하락"
      },
      {
        "element": "PRDY_VRSS",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CCLD_DVSN",
        "type": "string",
        "required": "Y",
        "description": "1:매수(+) \r\n3:장전 \r\n5:매도(-)"
      },
      {
        "element": "SHNU_RATE",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": "1 : 상한\r\n2 : 상승\r\n3 : 보합\r\n4 : 하한\r\n5 : 하락"
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": "1 : 상한\r\n2 : 상승\r\n3 : 보합\r\n4 : 하한\r\n5 : 하락"
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": "1 : 상한\r\n2 : 상승\r\n3 : 보합\r\n4 : 하한\r\n5 : 하락"
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "(1) 첫 번째 비트\r\n1 : 장개시전\r\n2 : 장중\r\n3 : 장종료후\r\n4 : 시간외단일가\r\n7 : 일반Buy-in\r\n8 : 당일Buy-in\r\n\r\n(2) 두 번째 비트\r\n0 : 보통\r\n1 : 종가\r\n2 : 대량\r\n3 : 바스켓\r\n7 : 정리매매\r\n8 : Buy-in"
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": "Y : 정지\r\nN : 정상거래"
      },
      {
        "element": "ASKP_RSQN1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "number",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "0 : 장중\r\nA : 장후예상\r\nB : 장전예상\r\nC : 9시이후의 예상가, VI발동\r\nD : 시간외 단일가 예상"
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VI_STND_PRC",
        "type": "number",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간회원사 (KRX)",
    "url": "/tryitout/H0STMBC0",
    "tr_id": "H0STMBC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간회원사 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "SELN2_MBCR_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SELN_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SHNU_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SELN_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SHNU_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_SELN_RLIM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_SHNU_RLIM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 장운영정보 (KRX)",
    "url": "/tryitout/H0STMKO0",
    "tr_id": "H0STMKO0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 장운영정보 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TR_SUSP_REAS_CNTT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "110        장전 동시호가 개시                      \r\n112        장개시                                  \r\n121        장후 동시호가 개시                      \r\n129        장마감                                  \r\n130        장개시전시간외개시                      \r\n139        장개시전시간외종료                      \r\n140        시간외 종가 매매 개시                   \r\n146        장종료후시간외 체결지시                 \r\n149        시간외 종가 매매 종료                   \r\n150        시간외 단일가 매매 개시                 \r\n156        시간외단일가 체결지시                   \r\n159        시간외 단일가 매매 종료                 \r\n164        시장임시정지                            \r\n174        서킷브레이크 발동                       \r\n175        서킷브레이크 해제                       \r\n182        서킷브레이크 장중동시마감               \r\n184        서킷브레이크 개시                       \r\n185        서킷브레이크 해제                       \r\n387        사이드카 매도발동                       \r\n388        사이드카 매도발동해제                   \r\n397        사이드카 매수발동                       \r\n398        사이드카 매수발동해제                   \r\n???        단일가개시                              \r\n???        서킷브레이크 단일가접수                 \r\nF01        장개시 10초전                           \r\nF06        장개시 1분전                            \r\nF07        장개시 5분전                            \r\nF08        장개시 10분전                           \r\nF09        장개시 3분전                            \r\nF11        장마감 10초전                           \r\nF16        장마감 1분전                            \r\nF17        장마감 5분전                            \r\nF18        장마감 3분전                            \r\nP01        장개시 10초전                           \r\nP06        장개시 1분전                            \r\nP07        장개시 5분전                            \r\nP08        장개시 10분전                           \r\nP09        장개시 30분전                           \r\nP11        장마감 10초전                           \r\nP16        장마감 1분전                            \r\nP17        장마감 5분전                            \r\nP18        장마감 3분전"
      },
      {
        "element": "ANTC_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "112    장전예상종료 \r\n121   장후예상시작\r\n129   장후예상종료\r\n311  장전예상시작"
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "1  시초동시 임의종료 지정\r\n2  시초동시 임의종료 해제 \r\n3  마감동시 임의종료 지정 \r\n4  마감동시 임의종료 해제  \r\n5  시간외단일가임의종료 지정 \r\n6  시간외단일가임의종료 해제"
      },
      {
        "element": "DIVI_APP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "divi_app_cls_code[0]  1: 배분개시 2: 배분해제\r\ndivi_app_cls_code[1] 1: 매수상한 2: 매수하한 3: 매도상한 4: 매도하한"
      },
      {
        "element": "ISCD_STAT_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "51  관리종목 지정 종목\r\n52  시장경고 구분이 '투자위험'인 종목\r\n53  시장경고 구분이 '투자경고'인 종목\r\n54  시장경고 구분이 '투자주의'인 종목\r\n55  당사 신용가능 종목\r\n57  당사 증거금률이 100인 종목\r\n58  거래정지 지정된 종목  \r\n59  단기과열종목으로 지정되거나 지정 연장된 종목\r\n00 그 외 종목"
      },
      {
        "element": "VI_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "Y  VI적용된 종목\r\nN  VI적용되지 않은 종목"
      },
      {
        "element": "OVTM_VI_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": "Y 시간외단일가VI 적용된 종목\r\nN 시간외단일가VI 적용되지 않은 종목"
      },
      {
        "element": "EXCH_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내ETF NAV추이",
    "url": "/tryitout/H0STNAV0",
    "tr_id": "H0STNAV0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내ETF NAV추이",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NAV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NAV_PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NAV_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NAV_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_NAV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HPRC_NAV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LPRC_NAV",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 시간외 실시간호가 (KRX)",
    "url": "/tryitout/H0STOAA0",
    "tr_id": "H0STOAA0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 시간외 실시간호가 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 시간외 실시간예상체결 (KRX)",
    "url": "/tryitout/H0STOAC0",
    "tr_id": "H0STOAC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 시간외 실시간예상체결 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 시간외 실시간체결가 (KRX)",
    "url": "/tryitout/H0STOUP0",
    "tr_id": "H0STOUP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 시간외 실시간체결가 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간프로그램매매 (KRX)",
    "url": "/tryitout/H0STPGM0",
    "tr_id": "H0STPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간프로그램매매 (KRX)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간예상체결 (통합)",
    "url": "/tryitout/H0UNANC0",
    "tr_id": "H0UNANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간예상체결 (통합)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VI_STND_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간호가 (통합)",
    "url": "/tryitout/H0UNASP0",
    "tr_id": "H0UNASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간호가 (통합)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_ASKP_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OVTM_TOTAL_BIDP_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_DEAL_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KMID_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KMID_TOTAL_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KMID_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMID_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMID_TOTAL_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMID_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간체결가 (통합)",
    "url": "/tryitout/H0UNCNT0",
    "tr_id": "H0UNCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간체결가 (통합)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WGHN_AVRG_STCK_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CNTG_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NEW_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRHT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL_TNRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_SMNS_HOUR_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HOUR_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_TRTM_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VI_STND_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간회원사 (통합)",
    "url": "/tryitout/H0UNMBC0",
    "tr_id": "H0UNMBC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간회원사 (통합)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_QTY5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_GLOB_YN_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_GLOB_YN_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_NO5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_NO5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_MBCR_RLIM5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_MBCR_RLIM5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_QTY_ICDC5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_QTY_ICDC5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SELN_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SHNU_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SELN_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_TOTAL_SHNU_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_SELN_RLIM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GLOB_SHNU_RLIM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN2_MBCR_ENG_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BYOV_MBCR_ENG_NAME5",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내주식 실시간프로그램매매 (통합)",
    "url": "/tryitout/H0UNPGM0",
    "tr_id": "H0UNPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내주식 실시간프로그램매매 (통합)",
    "fields": [
      {
        "element": "MKSC_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_CNTG_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내지수 실시간예상체결",
    "url": "/tryitout/H0UPANC0",
    "tr_id": "H0UPANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내지수 실시간예상체결",
    "fields": [
      {
        "element": "BSTP_CLS_CODE",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRPR_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSTP_NMIX_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PCAS_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PCAS_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_NMIX",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMIX_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMIX_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CLPR_VRSS_OPRC_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CLPR_VRSS_HGPR_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CLPR_VRSS_LWPR_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "UPLM_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASCN_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STNR_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DOWN_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LSLM_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "QTQT_ASCN_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "QTQT_DOWN_ISSU_CNT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TICK_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내지수 실시간체결",
    "url": "/tryitout/H0UPCNT0",
    "tr_id": "H0UPCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내지수 실시간체결",
    "fields": [
      {
        "element": "bstp_cls_code",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "bsop_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prpr_nmix",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pcas_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pcas_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_nmix",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_vrss_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_vrss_nmix_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_vrss_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_vrss_nmix_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_vrss_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_vrss_nmix_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_clpr_vrss_oprc_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_clpr_vrss_hgpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_clpr_vrss_lwpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "uplm_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ascn_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stnr_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "down_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lslm_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "qtqt_ascn_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "qtqt_down_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tick_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "국내지수 실시간프로그램매매",
    "url": "/tryitout/H0UPPGM0",
    "tr_id": "H0UPPGM0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "국내지수 실시간프로그램매매",
    "fields": [
      {
        "element": "BSTP_CLS_CODE",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SELN_ENTM_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SELN_ONSL_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SHNU_ENTM_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SHNU_ONSL_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SELN_ENTM_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SELN_ONSL_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SHNU_ENTM_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SHNU_ONSL_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SELN_ENTM_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SELN_ONSL_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SHNU_ENTM_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SHNU_ONSL_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SELN_ENTM_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SELN_ONSL_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SHNU_ENTM_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SHNU_ONSL_CNTG_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTN_SELN_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTM_SELN_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTN_SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTM_SELN_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTN_SHNU_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTM_SHNU_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTN_SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTM_SHNU_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTN_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTM_NTBY_QTY_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTN_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_SMTM_NTBY_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTN_SELN_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTM_SELN_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTN_SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTM_SELN_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTN_SHNU_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTM_SHNU_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTN_SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTM_SHNU_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTN_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTM_NTBY_QTY_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTN_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_SMTM_NTBY_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ENTM_SELN_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ENTM_SELN_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ENTM_SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ENTM_SELN_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ENTM_SHNU_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ENTM_SHNU_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ENTM_SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ENTM_SHNU_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ENTM_NTBY_QT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ENTM_NTBY_QTY_RAT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ENTM_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ENTM_NTBY_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ONSL_SELN_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ONSL_SELN_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ONSL_SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ONSL_SELN_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ONSL_SHNU_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ONSL_SHNU_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ONSL_SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ONSL_SHNU_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ONSL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ONSL_NTBY_QTY_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_ONSL_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ONSL_NTBY_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_SELN_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SELN_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_SELN_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_SHUN_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_SHNU_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_SHUN_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_SMTM_NTBY_QTY_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WHOL_NTBY_TR_PBMN_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_ENTM_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_ENTM_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_ONSL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ARBT_ONSL_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_ENTM_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_ENTM_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_ONSL_NTBY_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NABT_ONSL_NTBY_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "주식선물 실시간예상체결",
    "url": "/tryitout/H0ZFANC0",
    "tr_id": "H0ZFANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식선물 실시간예상체결",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "주식선물 실시간호가",
    "url": "/tryitout/H0ZFASP0",
    "tr_id": "H0ZFASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식선물 실시간호가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "주식선물 실시간체결가",
    "url": "/tryitout/H0ZFCNT0",
    "tr_id": "H0ZFCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식선물 실시간체결가",
    "fields": [
      {
        "element": "FUTS_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUTS_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STCK_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FMSC_FCTN_STPL_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SPEAD_PRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_MXPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_LLAM",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DYNM_PRC_LIMT_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "주식옵션 실시간예상체결",
    "url": "/tryitout/H0ZOANC0",
    "tr_id": "H0ZOANC0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식옵션 실시간예상체결",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_CNTG_PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ANTC_MKOP_CLS_CODE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "주식옵션 실시간호가",
    "url": "/tryitout/H0ZOASP0",
    "tr_id": "H0ZOASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식옵션 실시간호가",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_CSNU10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_CSNU10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN10",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "주식옵션 실시간체결가",
    "url": "/tryitout/H0ZOCNT0",
    "tr_id": "H0ZOCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "주식옵션 실시간체결가",
    "fields": [
      {
        "element": "OPTN_SHRN_ISCD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSOP_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VRSS_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_PRDY_VRSS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_CTRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_OPRC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_HGPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_LWPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_CNQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ACML_TR_PBMN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_THPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_OTST_STPL_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRC_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HGPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_HOUR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_PRPR_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LWPR_VRSS_NMIX_PRPR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRMM_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "INVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TMVL_VAL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DELTA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "GAMA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VEGA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THETA",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RHO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HTS_INTS_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ESDG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OTST_STPL_RGBF_QTY_ICDC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "THPR_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "UNAS_HIST_VLTL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CTTR",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DPRT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_BASIS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_ASKP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPTN_BIDP1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASKP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIDP_RSQN1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "NTBY_CNTG_CSNU",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SELN_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SHNU_CNTG_SMTN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_ASKP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOTAL_BIDP_RSQN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PRDY_VOL_VRSS_ACML_VOL_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간호가",
    "url": "/tryitout/HDFFF010",
    "tr_id": "HDFFF010",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간호가",
    "fields": [
      {
        "element": "SERIES_CD",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "RECV_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RECV_TIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PREV_PRICE",
        "type": "string",
        "required": "Y",
        "description": "전일종가, 매수1호가~매도5호가\r\n※ ffcode.mst(해외선물종목마스터 파일)의 sCalcDesz(계산 소수점) 값 참고"
      },
      {
        "element": "BID_QNTT_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_NUM_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_PRICE_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_QNTT_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_NUM_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_PRICE_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_QNTT_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_NUM_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_PRICE_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_QNTT_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_NUM_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_PRICE_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_QNTT_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_NUM_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_PRICE_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_QNTT_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_NUM_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_PRICE_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_QNTT_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_NUM_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_PRICE_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_QNTT_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_NUM_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_PRICE_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_QNTT_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_NUM_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BID_PRICE_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_QNTT_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_NUM_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ASK_PRICE_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "STTL_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간체결가",
    "url": "/tryitout/HDFFF020",
    "tr_id": "HDFFF020",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간체결가",
    "fields": [
      {
        "element": "SERIES_CD",
        "type": "string",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "BSNS_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_OPEN_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_OPEN_TIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_CLOSE_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_CLOSE_TIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PREV_PRICE",
        "type": "string",
        "required": "Y",
        "description": "전일종가, 체결가격, 전일대비가, 시가, 고가, 저가\r\n※ ffcode.mst(해외선물종목마스터 파일)의 sCalcDesz(계산 소수점) 값 참고"
      },
      {
        "element": "RECV_DATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RECV_TIME",
        "type": "string",
        "required": "Y",
        "description": "수신시각(recv_time) = 실제 체결시각"
      },
      {
        "element": "ACTIVE_FLAG",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST_QNTT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PREV_DIFF_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PREV_DIFF_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPEN_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HIGH_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LOW_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PREV_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "QUOTSIGN",
        "type": "string",
        "required": "Y",
        "description": "2:매수체결 5:매도체결"
      },
      {
        "element": "RECV_TIME2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PSTTL_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PSTTL_SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PSTTL_DIFF_PRICE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PSTTL_DIFF_RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간주문내역통보",
    "url": "/tryitout/HDFFF1C0",
    "tr_id": "HDFFF1C0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간주문내역통보",
    "fields": [
      {
        "element": "USER_ID",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "ACCT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_DT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORGN_ORD_DT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORGN_ODNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SERIES",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RVSE_CNCL_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "해당없음 : 00 , 정정 : 01 , 취소 : 02"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "01 : 매도,  02 : 매수"
      },
      {
        "element": "CPLX_ORD_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "0 (hedge청산만 이용)"
      },
      {
        "element": "PRCE_TP",
        "type": "string",
        "required": "Y",
        "description": "1:Limit, 2:Market, 3:Stop(Stop가격시 시장가)"
      },
      {
        "element": "FM_EXCG_RCIT_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "01:접수전, 02:응답, 03:거부"
      },
      {
        "element": "ORD_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_LMT_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_STOP_ORD_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOT_CCLD_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOT_CCLD_UV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_REMQ",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_ORD_GRP_DT",
        "type": "string",
        "required": "Y",
        "description": "주문일자(ORD_DT)와 동일"
      },
      {
        "element": "ORD_GRP_STNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_DTL_DTIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRT_DTL_DTIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WORK_EMPL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CRCY_CD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LQD_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LQD_LMT_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LQD_STOP_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRD_COND",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TERM_ORD_VALD_DTIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SPEC_TP",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ECIS_RSVN_ORD_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUOP_ITEM_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "AUTO_ORD_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외선물옵션 실시간체결내역통보",
    "url": "/tryitout/HDFFF2C0",
    "tr_id": "HDFFF2C0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외선물옵션 실시간체결내역통보",
    "fields": [
      {
        "element": "USER_ID",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "ACCT_NO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_DT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ODNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORGN_ORD_DT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORGN_ODNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SERIES",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RVSE_CNCL_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "해당없음 : 00 , 정정 : 01 , 취소 : 02"
      },
      {
        "element": "SLL_BUY_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "01 : 매도,  02 : 매수"
      },
      {
        "element": "CPLX_ORD_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": "0 (hedge청산만 이용)"
      },
      {
        "element": "PRCE_TP",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_EXCG_RCIT_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_QTY",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_LMT_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_STOP_ORD_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TOT_CCLD_QTY",
        "type": "string",
        "required": "Y",
        "description": "동일한 주문건에 대한 누적된 체결수량 (하나의 주문건에 여러건의 체결내역 발생)"
      },
      {
        "element": "TOT_CCLD_UV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_REMQ",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_ORD_GRP_DT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_GRP_STNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_DTL_DTIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPRT_DTL_DTIME",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "WORK_EMPL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CCLD_DT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CCNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "API_CCNO",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CCLD_QTY",
        "type": "string",
        "required": "Y",
        "description": "매 체결 단위 체결수량임 (여러건 체결내역 누적 체결수량인 총체결수량과 다름)"
      },
      {
        "element": "FM_CCLD_PRIC",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "CRCY_CD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TRST_FEE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ORD_MDIA_ONLINE_YN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FM_CCLD_AMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FUOP_ITEM_DVSN_CD",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외주식 실시간호가",
    "url": "/tryitout/HDFSASP0",
    "tr_id": "HDFSASP0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외주식 실시간호가",
    "fields": [
      {
        "element": "RSYM",
        "type": "object",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "SYMB",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ZDIV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "XYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "XHMS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KHMS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "AVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BDVL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ADVL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK10",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외주식 지연호가(아시아)",
    "url": "/tryitout/HDFSASP1",
    "tr_id": "HDFSASP1",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외주식 지연호가(아시아)",
    "fields": [
      {
        "element": "RSYM",
        "type": "string",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "SYMB",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ZDIV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "XYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "XHMS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KHMS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "AVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BDVL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ADVL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DBID1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DASK1",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "해외주식 실시간지연체결가",
    "url": "/tryitout/HDFSCNT0",
    "tr_id": "HDFSCNT0",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "해외주식 실시간지연체결가",
    "fields": [
      {
        "element": "RSYM",
        "type": "string",
        "required": "Y",
        "description": "'각 항목사이에는 구분자로 ^ 사용,\r\n모든 데이터타입은 String으로 변환되어 push 처리됨'"
      },
      {
        "element": "SYMB",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ZDIV",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "XYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "XHMS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KYMD",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "KHMS",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "OPEN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "HIGH",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LOW",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "LAST",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "SIGN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "DIFF",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "RATE",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PBID",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "PASK",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VBID",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "VASK",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "EVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TVOL",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TAMT",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "BIVL",
        "type": "string",
        "required": "Y",
        "description": "매수호가가 매도주문 수량을 따라가서 체결된것을 표현하여 BIVL 이라는 표현을 사용"
      },
      {
        "element": "ASVL",
        "type": "string",
        "required": "Y",
        "description": "매도호가가 매수주문 수량을 따라가서 체결된것을 표현하여 ASVL 이라는 표현을 사용"
      },
      {
        "element": "STRN",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MTYP",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "name": "회원사 실시간 매매동향(틱)",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-trade-trend",
    "tr_id": "FHPST04320000",
    "tr_id_demo": "모의투자 미지원",
    "sheet": "회원사 실시간 매매동향(틱)",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "msg_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "msg1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output1",
        "type": "object",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "total_seln_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_shnu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "bsop_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mbcr_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cntg_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_qty_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  }
]"""


def load_websocket_response_specs() -> list[dict[str, Any]]:
    return json.loads(_RESPONSE_SPECS_JSON)


WEBSOCKET_RESPONSE_SPECS = load_websocket_response_specs()
WEBSOCKET_RESPONSE_SPECS_BY_URL = {
    str(spec.get("url", "")): spec for spec in WEBSOCKET_RESPONSE_SPECS if spec.get("url")
}
