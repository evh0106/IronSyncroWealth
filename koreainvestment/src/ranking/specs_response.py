"""국내주식 ranking API 응답 스펙."""

from __future__ import annotations

from copy import deepcopy
import json
from typing import Any


_RESPONSE_SPECS_JSON = r"""[
  {
    "tr_id": "FHKST11860000",
    "name": "국내주식 시간외예상체결등락률",
    "url": "/uapi/domestic-stock/v1/ranking/overtime-exp-trans-fluct",
    "sheet_found": true,
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
        "element": "output",
        "type": "object",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iscd_stat_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_shrn_iscd",
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
        "element": "ovtm_untp_antc_cnpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_vrsssign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "itmt_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01820000",
    "name": "국내주식 예상체결 상승/하락상위",
    "url": "/uapi/domestic-stock/v1/ranking/exp-trans-updown",
    "sheet_found": false,
    "fields": []
  },
  {
    "tr_id": "FHPST01720000",
    "name": "국내주식 호가잔량 순위",
    "url": "/uapi/domestic-stock/v1/ranking/quote-balance",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "mksc_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_ctrt",
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
        "element": "total_askp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_bidp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_ntsl_bidp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_rsqn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_rsqn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST17010000",
    "name": "국내주식 신용잔고 상위",
    "url": "/uapi/domestic-stock/v1/ranking/credit-balance",
    "sheet_found": true,
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
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "bstp_cls_code",
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
        "element": "stnd_date1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stnd_date2",
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
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_ctrt",
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
        "element": "whol_loan_rmnd_stcn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_loan_rmnd_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_loan_rmnd_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_stln_rmnd_stcn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_stln_rmnd_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_stln_rmnd_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nday_vrss_loan_rmnd_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nday_vrss_stln_rmnd_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST02350000",
    "name": "국내주식 시간외거래량순위",
    "url": "/uapi/domestic-stock/v1/ranking/overtime-volume",
    "sheet_found": true,
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
        "description": ""
      },
      {
        "element": "ovtm_untp_exch_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_exch_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_kosdaq_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_kosdaq_tr_pbmn",
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
        "element": "stck_shrn_iscd",
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
        "element": "ovtm_untp_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_seln_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_shnu_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_vrss_acml_vol_rlim",
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
        "element": "acml_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHKDB13470100",
    "name": "국내주식 배당률 상위",
    "url": "/uapi/domestic-stock/v1/ranking/dividend-rate",
    "sheet_found": true,
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
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "rank",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sht_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "isin_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "record_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "per_sto_divi_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "divi_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "divi_kind",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01760000",
    "name": "국내주식 시간외잔량 순위",
    "url": "/uapi/domestic-stock/v1/ranking/after-hour-balance",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "stck_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_total_askp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_total_bidp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mkob_otcp_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mkfa_otcp_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST04820000",
    "name": "국내주식 공매도 상위종목",
    "url": "/uapi/domestic-stock/v1/ranking/short-sale",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_ctrt",
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
        "element": "ssts_cntg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ssts_vol_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ssts_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ssts_tr_pbmn_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stnd_date1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stnd_date2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "avrg_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01780000",
    "name": "국내주식 이격도 순위",
    "url": "/uapi/domestic-stock/v1/ranking/disparity",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "mksc_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_ctrt",
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
        "element": "acml_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d5_dsrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d10_dsrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d20_dsrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d60_dsrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d120_dsrt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHMCM000100C0",
    "name": "HTS조회상위20종목",
    "url": "/uapi/domestic-stock/v1/ranking/hts-top-view",
    "sheet_found": true,
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
        "description": ""
      },
      {
        "element": "mrkt_div_cls_code",
        "type": "string",
        "required": "Y",
        "description": "J : 코스피, Q : 코스닥"
      },
      {
        "element": "mksc_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": "종목코드"
      }
    ]
  },
  {
    "tr_id": "FHPST01730000",
    "name": "국내주식 수익자산지표 순위",
    "url": "/uapi/domestic-stock/v1/ranking/profit-asset-index",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "data_rank",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_ctrt",
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
        "element": "sale_totl_prfi",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bsop_prti",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "op_prfi",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thtr_ntin",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_aset",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_lblt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_cptl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stac_month",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stac_month_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iqry_csnu",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01870000",
    "name": "국내주식 신고/신저근접종목 상위",
    "url": "/uapi/domestic-stock/v1/ranking/near-new-highlow",
    "sheet_found": false,
    "fields": []
  },
  {
    "tr_id": "FHPST01770000",
    "name": "국내주식 우선주/괴리율 상위",
    "url": "/uapi/domestic-stock/v1/ranking/prefer-disparate-ratio",
    "sheet_found": false,
    "fields": []
  },
  {
    "tr_id": "FHKST190900C0",
    "name": "국내주식 대량체결건수 상위",
    "url": "/uapi/domestic-stock/v1/ranking/bulk-trans-num",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "mksc_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_vrss_sign",
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
        "element": "prdy_ctrt",
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
        "element": "shnu_cntg_csnu",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_cntg_csnu",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ntby_cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01750000",
    "name": "국내주식 재무비율 순위",
    "url": "/uapi/domestic-stock/v1/ranking/finance-ratio",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "data_rank",
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
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_ctrt",
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
        "element": "cptl_op_prfi",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cptl_ntin_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sale_totl_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sale_ntin_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bis",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lblt_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bram_depn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rsrv_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "grs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "op_prfi_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bsop_prfi_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ntin_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "equt_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cptl_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sale_bond_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "totl_aset_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stac_month",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stac_month_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iqry_csnu",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01740000",
    "name": "국내주식 시가총액 상위",
    "url": "/uapi/domestic-stock/v1/ranking/market-cap",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "mksc_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_ctrt",
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
        "element": "lstn_stcn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_avls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_whol_avls_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01860000",
    "name": "국내주식 당사매매종목 상위",
    "url": "/uapi/domestic-stock/v1/ranking/traded-by-company",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "data_rank",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_vrss_sign",
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
        "element": "prdy_ctrt",
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
        "element": "seln_cnqn_smtn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_cnqn_smtn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ntby_cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01700000",
    "name": "국내주식 등락률 순위",
    "url": "/uapi/domestic-stock/v1/ranking/fluctuation",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "stck_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_ctrt",
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
        "element": "stck_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_lwpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dsgt_date_clpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cnnt_ascn_dynu",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cnnt_down_dynu",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_vrss_prpr_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_vrss_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prd_rsfl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prd_rsfl_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01790000",
    "name": "국내주식 시장가치 순위",
    "url": "/uapi/domestic-stock/v1/ranking/market-value",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "data_rank",
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
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_ctrt",
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
        "element": "per",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pbr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pcr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "psr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "eps",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "eva",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ebitda",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pv_div_ebitda",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ebitda_div_fnnc_expn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stac_month",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stac_month_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iqry_csnu",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01800000",
    "name": "국내주식 관심종목등록 상위",
    "url": "/uapi/domestic-stock/v1/ranking/top-interest-stock",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "mrkt_div_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mksc_shrn_iscd",
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
        "element": "prdy_ctrt",
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
        "element": "askp",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter_issu_reg_csnu",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01680000",
    "name": "국내주식 체결강도 상위",
    "url": "/uapi/domestic-stock/v1/ranking/volume-power",
    "sheet_found": true,
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
        "element": "output",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "stck_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_rank",
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
        "element": "prdy_ctrt",
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
        "element": "tday_rltv",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_cnqn_smtn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_cnqn_smtn",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST02340000",
    "name": "국내주식 시간외등락율순위",
    "url": "/uapi/domestic-stock/v1/ranking/overtime-fluctuation",
    "sheet_found": true,
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
        "description": ""
      },
      {
        "element": "ovtm_untp_uplm_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_ascn_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_stnr_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_lslm_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_down_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_acml_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_exch_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_exch_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_kosdaq_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_kosdaq_tr_pbmn",
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
        "element": "mksc_shrn_iscd",
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
        "element": "ovtm_untp_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_seln_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_shnu_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_vrss_acml_vol_rlim",
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
        "element": "acml_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  }
]
"""

RANKING_API_RESPONSE_SPECS: list[dict[str, Any]] = json.loads(_RESPONSE_SPECS_JSON)


def load_ranking_response_specs() -> list[dict[str, Any]]:
  specs = deepcopy(RANKING_API_RESPONSE_SPECS)

  # 엑셀 원본(20260430)에 FHPST01820000 시트가 없어 응답 필드가 비어 있어,
  # 공통 응답 필드를 보정합니다.
  for spec in specs:
    if spec.get("tr_id") != "FHPST01820000":
      continue

    fields = spec.setdefault("fields", [])
    if fields:
      break

    spec["sheet_found"] = False
    fields.extend(
      [
        {"element": "rt_cd", "type": "string", "required": "Y", "description": ""},
        {"element": "msg_cd", "type": "string", "required": "Y", "description": ""},
        {"element": "msg1", "type": "string", "required": "Y", "description": ""},
        {"element": "output", "type": "array|object|null", "required": "Y", "description": ""},
      ]
    )
    break

  return specs


RANKING_API_RESPONSE_SPECS = load_ranking_response_specs()
RANKING_API_RESPONSE_SPECS_BY_TR_ID: dict[str, dict[str, Any]] = {
  spec.get("tr_id", ""): spec for spec in RANKING_API_RESPONSE_SPECS if spec.get("tr_id")
}
