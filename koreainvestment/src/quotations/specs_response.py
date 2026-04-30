"""국내주식 quotations API 응답 스펙."""

from __future__ import annotations

import json
from typing import Any


_RESPONSE_SPECS_JSON = r"""[
  {
    "tr_id": "FHKST01010400",
    "name": "주식현재가 일자별",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-price",
    "sheet": "주식현재가 일자별",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_clpr",
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
        "element": "prdy_vrss_vol_rate",
        "type": "string",
        "required": "Y",
        "description": "13(8.4)"
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
        "description": "11(8.2)"
      },
      {
        "element": "hts_frgn_ehrt",
        "type": "string",
        "required": "Y",
        "description": "11(8.2)"
      },
      {
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "flng_cls_code",
        "type": "string",
        "required": "Y",
        "description": "'01 : 권리락 \r\n02 : 배당락 \r\n03 : 분배락 \r\n04 : 권배락 \r\n05 : 중간(분기)배당락 \r\n06 : 권리중간배당락 \r\n07 : 권리분기배당락'"
      },
      {
        "element": "acml_prtt_rate",
        "type": "string",
        "required": "Y",
        "description": "13(8.4)"
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\": \"J\",\r\n\"fid_input_iscd\": \"000660\",\r\n\"fid_org_adj_prc\": \"0000000001\",\r\n\"fid_period_div_code\": \"D\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output\": [\r\n    {\r\n      \"stck_bsop_date\": \"20220111\",\r\n      \"stck_oprc\": \"125500\",\r\n      \"stck_hgpr\": \"128500\",\r\n      \"stck_lwpr\": \"124500\",\r\n      \"stck_clpr\": \"128000\",\r\n      \"acml_vol\": \"3908418\",\r\n      \"prdy_vrss_vol_rate\": \"13.31\",\r\n      \"prdy_vrss\": \"3500\",\r\n      \"prdy_vrss_sign\": \"2\",\r\n      \"prdy_ctrt\": \"2.81\",\r\n      \"hts_frgn_ehrt\": \"49.39\",\r\n      \"frgn_ntby_qty\": \"0\",\r\n      \"flng_cls_code\": \"00\",\r\n      \"acml_prtt_rate\": \"1.00\"\r\n    },\r\n    {\r\n      \"stck_bsop_date\": \"20220110\",\r\n      \"stck_oprc\": \"126500\",\r\n      \"stck_hgpr\": \"127000\",\r\n      \"stck_lwpr\": \"123000\",\r\n      \"stck_clpr\": \"124500\",\r\n      \"acml_vol\": \"3449197\",\r\n      \"prdy_vrss_vol_rate\": \"5.48\",\r\n      \"prdy_vrss\": \"-2500\",\r\n      \"prdy_vrss_sign\": \"5\",\r\n      \"prdy_ctrt\": \"-1.97\",\r\n      \"hts_frgn_ehrt\": \"49.39\",\r\n      \"frgn_ntby_qty\": \"293389\",\r\n      \"flng_cls_code\": \"00\",\r\n      \"acml_prtt_rate\": \"0.00\"\r\n    }\r\n\t  ],\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST01010100",
    "name": "주식현재가 시세",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-price",
    "sheet": "주식현재가 시세",
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
        "element": "iscd_stat_cls_code",
        "type": "string",
        "required": "Y",
        "description": "51 : 관리종목\r\n52 : 투자위험\r\n53 : 투자경고\r\n54 : 투자주의\r\n55 : 신용가능\r\n57 : 증거금 100%\r\n58 : 거래정지\r\n59 : 단기과열종목"
      },
      {
        "element": "marg_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rprs_mrkt_kor_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "new_hgpr_lwpr_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "temp_stop_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_rang_cont_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "clpr_rang_cont_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "crdt_able_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "grmn_rate_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elw_pblc_yn",
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
        "element": "acml_tr_pbmn",
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
        "element": "prdy_vrss_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_mxpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_llam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sdpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "wghn_avrg_stck_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_frgn_ehrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pgtr_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_scnd_dmrs_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_frst_dmrs_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_pont_val",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_frst_dmsp_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_scnd_dmsp_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dmrs_val",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dmsp_val",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cpfn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rstc_wdth_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fcam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sspr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "aspr_unit",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_deal_qty_unit_val",
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
        "element": "hts_avls",
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
        "element": "stac_month",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vol_tnrt",
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
        "element": "bps",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d250_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d250_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d250_hgpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d250_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d250_lwpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d250_lwpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_dryy_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_hgpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_dryy_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_lwpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_lwpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "w52_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "w52_hgpr_vrss_prpr_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "w52_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "w52_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "w52_lwpr_vrss_prpr_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "w52_lwpr_date",
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
        "element": "ssts_yn",
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
        "element": "fcam_cnnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cpfn_cnnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "apprch_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_hldn_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vi_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_vi_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "last_ssts_cntg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "invt_caful_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_warn_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "short_over_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sltr_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mang_issu_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\": \"J\",\r\n\"fid_input_iscd\": \"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output\": {\r\n    \"iscd_stat_cls_code\": \"55\",\r\n    \"marg_rate\": \"20.00\",\r\n    \"rprs_mrkt_kor_name\": \"KOSPI200\",\r\n    \"bstp_kor_isnm\": \"전기.전자\",\r\n    \"temp_stop_yn\": \"N\",\r\n    \"oprc_rang_cont_yn\": \"N\",\r\n    \"clpr_rang_cont_yn\": \"N\",\r\n    \"crdt_able_yn\": \"Y\",\r\n    \"grmn_rate_cls_code\": \"40\",\r\n    \"elw_pblc_yn\": \"Y\",\r\n    \"stck_prpr\": \"128500\",\r\n    \"prdy_vrss\": \"0\",\r\n    \"prdy_vrss_sign\": \"3\",\r\n    \"prdy_ctrt\": \"0.00\",\r\n    \"acml_tr_pbmn\": \"344570137500\",\r\n    \"acml_vol\": \"2669075\",\r\n    \"prdy_vrss_vol_rate\": \"75.14\",\r\n    \"stck_oprc\": \"128500\",\r\n    \"stck_hgpr\": \"130000\",\r\n    \"stck_lwpr\": \"128500\",\r\n    \"stck_mxpr\": \"167000\",\r\n    \"stck_llam\": \"90000\",\r\n    \"stck_sdpr\": \"128500\",\r\n    \"wghn_avrg_stck_prc\": \"129097.23\",\r\n    \"hts_frgn_ehrt\": \"49.48\",\r\n    \"frgn_ntby_qty\": \"0\",\r\n    \"pgtr_ntby_qty\": \"287715\",\r\n    \"pvt_scnd_dmrs_prc\": \"131833\",\r\n    \"pvt_frst_dmrs_prc\": \"130166\",\r\n    \"pvt_pont_val\": \"128333\",\r\n    \"pvt_frst_dmsp_prc\": \"126666\",\r\n    \"pvt_scnd_dmsp_prc\": \"124833\",\r\n    \"dmrs_val\": \"129250\",\r\n    \"dmsp_val\": \"125750\",\r\n    \"cpfn\": \"36577\",\r\n    \"rstc_wdth_prc\": \"38500\",\r\n    \"stck_fcam\": \"5000\",\r\n    \"stck_sspr\": \"97660\",\r\n    \"aspr_unit\": \"500\",\r\n    \"hts_deal_qty_unit_val\": \"1\",\r\n    \"lstn_stcn\": \"728002365\",\r\n    \"hts_avls\": \"935483\",\r\n    \"per\": \"19.67\",\r\n    \"pbr\": \"1.72\",\r\n    \"stac_month\": \"12\",\r\n    \"vol_tnrt\": \"0.37\",\r\n    \"eps\": \"6532.00\",\r\n    \"bps\": \"74721.00\",\r\n    \"d250_hgpr\": \"149500\",\r\n    \"d250_hgpr_date\": \"20210225\",\r\n    \"d250_hgpr_vrss_prpr_rate\": \"-14.05\",\r\n    \"d250_lwpr\": \"90500\",\r\n    \"d250_lwpr_date\": \"20211013\",\r\n    \"d250_lwpr_vrss_prpr_rate\": \"41.99\",\r\n    \"stck_dryy_hgpr\": \"132500\",\r\n    \"dryy_hgpr_vrss_prpr_rate\": \"-3.02\",\r\n    \"dryy_hgpr_date\": \"20220103\",\r\n    \"stck_dryy_lwpr\": \"121500\",\r\n    \"dryy_lwpr_vrss_prpr_rate\": \"5.76\",\r\n    \"dryy_lwpr_date\": \"20220105\",\r\n    \"w52_hgpr\": \"149500\",\r\n    \"w52_hgpr_vrss_prpr_ctrt\": \"-14.05\",\r\n    \"w52_hgpr_date\": \"20210225\",\r\n    \"w52_lwpr\": \"90500\",\r\n    \"w52_lwpr_vrss_prpr_ctrt\": \"41.99\",\r\n    \"w52_lwpr_date\": \"20211013\",\r\n    \"whol_loan_rmnd_rate\": \"0.22\",\r\n    \"ssts_yn\": \"Y\",\r\n    \"stck_shrn_iscd\": \"000660\",\r\n    \"fcam_cnnm\": \"5,000\",\r\n    \"cpfn_cnnm\": \"36,576 억\",\r\n    \"frgn_hldn_qty\": \"360220601\",\r\n    \"vi_cls_code\": \"N\",\r\n    \"ovtm_vi_cls_code\": \"N\",\r\n    \"last_ssts_cntg_qty\": \"43916\",\r\n    \"invt_caful_yn\": \"N\",\r\n    \"mrkt_warn_cls_code\": \"00\",\r\n    \"short_over_yn\": \"N\",\r\n    \"sltr_yn\": \"N\"\r\n  },\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST02300000",
    "name": "국내주식 시간외현재가",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-overtime-price",
    "sheet": "국내주식 시간외현재가",
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
        "element": "bstp_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": "※ 거래소 정보로 특정 종목은 업종구분이 없어 데이터 미회신"
      },
      {
        "element": "mang_issu_cls_name",
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
        "element": "ovtm_untp_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_mxpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_llam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "marg_rate",
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
        "element": "ovtm_untp_antc_cntg_vrss_sign",
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
        "element": "ovtm_untp_antc_cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "crdt_able_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "new_lstn_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sltr_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mang_issu_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_warn_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trht_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vlnt_deal_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_sdpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_warn_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "revl_issu_reas_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insn_pbnt_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "flng_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rprs_mrkt_kor_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_vi_cls_code",
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
      },
      {
        "element": "fid_cond_mrkt_div_code:J\r\nfid_input_iscd:005930",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": {\r\n        \"bstp_kor_isnm\": \"전기.전자\",\r\n        \"ovtm_untp_prpr\": \"83600\",\r\n        \"ovtm_untp_prdy_vrss\": \"-100\",\r\n        \"ovtm_untp_prdy_vrss_sign\": \"5\",\r\n        \"ovtm_untp_prdy_ctrt\": \"-0.12\",\r\n        \"ovtm_untp_vol\": \"3500\",\r\n        \"ovtm_untp_tr_pbmn\": \"292600000\",\r\n        \"ovtm_untp_mxpr\": \"92000\",\r\n        \"ovtm_untp_llam\": \"75400\",\r\n        \"ovtm_untp_oprc\": \"83600\",\r\n        \"ovtm_untp_hgpr\": \"83600\",\r\n        \"ovtm_untp_lwpr\": \"83600\",\r\n        \"marg_rate\": \"20.00\",\r\n        \"ovtm_untp_antc_cnpr\": \"83500\",\r\n        \"ovtm_untp_antc_cntg_vrss\": \"-200\",\r\n        \"ovtm_untp_antc_cntg_vrss_sign\": \"5\",\r\n        \"ovtm_untp_antc_cntg_ctrt\": \"-0.24\",\r\n        \"ovtm_untp_antc_cnqn\": \"4442\",\r\n        \"crdt_able_yn\": \"Y\",\r\n        \"new_lstn_cls_name\": \"        \",\r\n        \"sltr_yn\": \"N\",\r\n        \"mang_issu_yn\": \"N\",\r\n        \"mrkt_warn_cls_code\": \"00\",\r\n        \"trht_yn\": \"N\",\r\n        \"vlnt_deal_cls_name\": \" \",\r\n        \"ovtm_untp_sdpr\": \"83700\",\r\n        \"insn_pbnt_yn\": \"N\",\r\n        \"rprs_mrkt_kor_name\": \"KOSPI200\",\r\n        \"ovtm_vi_cls_code\": \"N\",\r\n        \"bidp\": \"83600\",\r\n        \"askp\": \"83700\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST02310000",
    "name": "주식현재가 시간외시간별체결",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-overtimeconclusion",
    "sheet": "주식현재가 시간외시간별체결",
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
        "required": "N",
        "description": "기본정보"
      },
      {
        "element": "ovtm_untp_prpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_ctrt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_tr_pbmn",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_mxpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_llam",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_oprc",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_hgpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_lwpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cnpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_ctrt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "uplm_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "lslm_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "N",
        "description": "Array 시간별체결 정보"
      },
      {
        "element": "stck_cntg_hour",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "stck_prpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prdy_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prdy_ctrt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "askp",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "bidp",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "acml_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "cntg_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "\"input\": {\r\n            \"fid_cond_mrkt_div_code\": \"J\",\r\n            \"fid_hour_CLS_CODE\": \"1\",\r\n            \"fid_input_iscd\": \"018000\"\r\n        }",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "\"output1\": {\r\n            \"lslm_sign\": \"4\",\r\n            \"ovtm_untp_antc_cnpr\": \"0\",\r\n            \"ovtm_untp_antc_cntg_ctrt\": \"0.00\",\r\n            \"ovtm_untp_antc_cntg_vrss\": \"0\",\r\n            \"ovtm_untp_antc_cntg_vrss_sign\": \"3\",\r\n            \"ovtm_untp_antc_vol\": \"0\",\r\n            \"ovtm_untp_hgpr\": \"2900\",\r\n            \"ovtm_untp_llam\": \"2615\",\r\n            \"ovtm_untp_lwpr\": \"2835\",\r\n            \"ovtm_untp_mxpr\": \"3195\",\r\n            \"ovtm_untp_oprc\": \"2900\",\r\n            \"ovtm_untp_prdy_ctrt\": \"-2.41\",\r\n            \"ovtm_untp_prdy_vrss\": \"-70\",\r\n            \"ovtm_untp_prdy_vrss_sign\": \"5\",\r\n            \"ovtm_untp_prpr\": \"2835\",\r\n            \"ovtm_untp_tr_pbmn\": \"194135625\",\r\n            \"ovtm_untp_vol\": \"68086\",\r\n            \"uplm_sign\": \"1\"\r\n        },\r\n        \"output2\": [\r\n            {\r\n                \"acml_vol\": \"68086\",\r\n                \"askp\": \"2840\",\r\n                \"bidp\": \"2835\",\r\n                \"cntg_vol\": \"12865\",\r\n                \"prdy_ctrt\": \"-2.41\",\r\n                \"prdy_vrss\": \"-70\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_cntg_hour\": \"180025\",\r\n                \"stck_prpr\": \"2835\"\r\n            },\r\n            {\r\n                \"acml_vol\": \"55221\",\r\n                \"askp\": \"2840\",\r\n                \"bidp\": \"2835\",\r\n                \"cntg_vol\": \"6852\",\r\n                \"prdy_ctrt\": \"-2.24\",\r\n                \"prdy_vrss\": \"-65\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_cntg_hour\": \"175026\",\r\n                \"stck_prpr\": \"2840\"\r\n            },\r\n....\r\n            {\r\n                \"acml_vol\": \"668\",\r\n                \"askp\": \"2900\",\r\n                \"bidp\": \"2895\",\r\n                \"cntg_vol\": \"668\",\r\n                \"prdy_ctrt\": \"-0.17\",\r\n                \"prdy_vrss\": \"-5\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_cntg_hour\": \"161022\",\r\n                \"stck_prpr\": \"2900\"\r\n            }\r\n        ],\r\n        \"rt_cd\": \"0\"",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST02320000",
    "name": "주식현재가 시간외일자별주가",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-overtimeprice",
    "sheet": "주식현재가 시간외일자별주가",
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
        "required": "N",
        "description": "기본정보"
      },
      {
        "element": "ovtm_untp_prpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_ctrt",
        "type": "string",
        "required": "N",
        "description": "11(8.2)"
      },
      {
        "element": "ovtm_untp_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_tr_pbmn",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_mxpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_llam",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_oprc",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_hgpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_lwpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cnpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_antc_cntg_ctrt",
        "type": "string",
        "required": "N",
        "description": "11(8.2)"
      },
      {
        "element": "ovtm_untp_antc_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "N",
        "description": "Array 일자별 정보"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_prdy_ctrt",
        "type": "string",
        "required": "N",
        "description": "11(8.2)"
      },
      {
        "element": "ovtm_untp_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "stck_clpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prdy_vrss",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prdy_ctrt",
        "type": "string",
        "required": "N",
        "description": "11(8.2)"
      },
      {
        "element": "acml_vol",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ovtm_untp_tr_pbmn",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "'\"input\": {'\r\n                '\"fid_cond_mrkt_div_code\":\"J\"'\r\n                ','\r\n                '\"fid_input_iscd\":\"000660\"'\r\n            '}'",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "\"output1\": {\r\n            \"ovtm_untp_antc_cnpr\": \"0\",\r\n            \"ovtm_untp_antc_cntg_ctrt\": \"0.00\",\r\n            \"ovtm_untp_antc_cntg_vrss\": \"0\",\r\n            \"ovtm_untp_antc_cntg_vrss_sign\": \"3\",\r\n            \"ovtm_untp_antc_vol\": \"0\",\r\n            \"ovtm_untp_hgpr\": \"106000\",\r\n            \"ovtm_untp_llam\": \"95000\",\r\n            \"ovtm_untp_lwpr\": \"105500\",\r\n            \"ovtm_untp_mxpr\": \"116000\",\r\n            \"ovtm_untp_oprc\": \"0\",\r\n            \"ovtm_untp_prdy_ctrt\": \"0.47\",\r\n            \"ovtm_untp_prdy_vrss\": \"500\",\r\n            \"ovtm_untp_prdy_vrss_sign\": \"2\",\r\n            \"ovtm_untp_prpr\": \"106000\",\r\n            \"ovtm_untp_tr_pbmn\": \"1348318000\",\r\n            \"ovtm_untp_vol\": \"12740\"\r\n        },\r\n        \"output2\": [\r\n            {\r\n                \"acml_vol\": \"4640744\",\r\n                \"ovtm_untp_prdy_ctrt\": \"0.47\",\r\n                \"ovtm_untp_prdy_vrss\": \"500\",\r\n                \"ovtm_untp_prdy_vrss_sign\": \"2\",\r\n                \"ovtm_untp_prpr\": \"106000\",\r\n                \"ovtm_untp_tr_pbmn\": \"1348318000\",\r\n                \"ovtm_untp_vol\": \"12740\",\r\n                \"prdy_ctrt\": \"-0.47\",\r\n                \"prdy_vrss\": \"-500\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_bsop_date\": \"20220609\",\r\n                \"stck_clpr\": \"105500\"\r\n            },\r\n            {\r\n                \"acml_vol\": \"3075530\",\r\n                \"ovtm_untp_prdy_ctrt\": \"0.47\",\r\n                \"ovtm_untp_prdy_vrss\": \"500\",\r\n                \"ovtm_untp_prdy_vrss_sign\": \"2\",\r\n                \"ovtm_untp_prpr\": \"106500\",\r\n                \"ovtm_untp_tr_pbmn\": \"1882068000\",\r\n                \"ovtm_untp_vol\": \"17672\",\r\n                \"prdy_ctrt\": \"1.92\",\r\n                \"prdy_vrss\": \"2000\",\r\n......\r\n            {\r\n                \"acml_vol\": \"2969516\",\r\n                \"ovtm_untp_prdy_ctrt\": \"0.00\",\r\n                \"ovtm_untp_prdy_vrss\": \"0\",\r\n                \"ovtm_untp_prdy_vrss_sign\": \"3\",\r\n                \"ovtm_untp_prpr\": \"111000\",\r\n                \"ovtm_untp_tr_pbmn\": \"2273650500\",\r\n                \"ovtm_untp_vol\": \"20565\",\r\n                \"prdy_ctrt\": \"2.78\",\r\n                \"prdy_vrss\": \"3000\",\r\n                \"prdy_vrss_sign\": \"2\",\r\n                \"stck_bsop_date\": \"20220426\",\r\n                \"stck_clpr\": \"111000\"\r\n            }\r\n        ],\r\n        \"rt_cd\": \"0\"",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST02300400",
    "name": "국내주식 시간외호가",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-overtime-asking-price",
    "sheet": "국내주식 시간외호가",
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
        "element": "ovtm_untp_last_hour",
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
        "element": "ovtm_untp_askp2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp10",
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
        "element": "ovtm_untp_bidp2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_icdc10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_icdc10",
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
        "element": "ovtm_untp_askp_rsqn2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_askp_rsqn10",
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
        "element": "ovtm_untp_bidp_rsqn2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_bidp_rsqn10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_total_askp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_total_bidp_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_total_askp_rsqn_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_total_bidp_rsqn_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_untp_ntby_bidp_rsqn",
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
        "element": "total_askp_rsqn_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_bidp_rsqn_icdc",
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
        "element": "ovtm_total_askp_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_total_bidp_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fid_cond_mrkt_div_code:J\r\nfid_input_iscd:005930",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": {\r\n        \"ovtm_untp_last_hour\": \"161847\",\r\n        \"ovtm_untp_askp1\": \"83600\",\r\n        \"ovtm_untp_askp2\": \"83700\",\r\n        \"ovtm_untp_askp3\": \"83800\",\r\n        \"ovtm_untp_askp4\": \"0\",\r\n        \"ovtm_untp_askp5\": \"0\",\r\n        \"ovtm_untp_askp6\": \"0\",\r\n        \"ovtm_untp_askp7\": \"0\",\r\n        \"ovtm_untp_askp8\": \"0\",\r\n        \"ovtm_untp_askp9\": \"0\",\r\n        \"ovtm_untp_askp10\": \"0\",\r\n        \"ovtm_untp_bidp1\": \"83500\",\r\n        \"ovtm_untp_bidp2\": \"83400\",\r\n        \"ovtm_untp_bidp3\": \"83300\",\r\n        \"ovtm_untp_bidp4\": \"0\",\r\n        \"ovtm_untp_bidp5\": \"0\",\r\n        \"ovtm_untp_bidp6\": \"0\",\r\n        \"ovtm_untp_bidp7\": \"0\",\r\n        \"ovtm_untp_bidp8\": \"0\",\r\n        \"ovtm_untp_bidp9\": \"0\",\r\n        \"ovtm_untp_bidp10\": \"0\",\r\n        \"ovtm_untp_askp_icdc1\": \"0\",\r\n        \"ovtm_untp_askp_icdc2\": \"0\",\r\n        \"ovtm_untp_askp_icdc3\": \"0\",\r\n        \"ovtm_untp_bidp_icdc1\": \"1\",\r\n        \"ovtm_untp_bidp_icdc2\": \"0\",\r\n        \"ovtm_untp_bidp_icdc3\": \"0\",\r\n        \"ovtm_untp_askp_rsqn1\": \"4498\",\r\n        \"ovtm_untp_askp_rsqn2\": \"11671\",\r\n        \"ovtm_untp_askp_rsqn3\": \"9625\",\r\n        \"ovtm_untp_askp_rsqn4\": \"0\",\r\n        \"ovtm_untp_askp_rsqn5\": \"0\",\r\n        \"ovtm_untp_askp_rsqn6\": \"0\",\r\n        \"ovtm_untp_askp_rsqn7\": \"0\",\r\n        \"ovtm_untp_askp_rsqn8\": \"0\",\r\n        \"ovtm_untp_askp_rsqn9\": \"0\",\r\n        \"ovtm_untp_askp_rsqn10\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn1\": \"1219\",\r\n        \"ovtm_untp_bidp_rsqn2\": \"2242\",\r\n        \"ovtm_untp_bidp_rsqn3\": \"5603\",\r\n        \"ovtm_untp_bidp_rsqn4\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn5\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn6\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn7\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn8\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn9\": \"0\",\r\n        \"ovtm_untp_bidp_rsqn10\": \"0\",\r\n        \"ovtm_untp_total_askp_rsqn\": \"25794\",\r\n        \"ovtm_untp_total_bidp_rsqn\": \"9064\",\r\n        \"ovtm_untp_total_askp_rsqn_icdc\": \"0\",\r\n        \"ovtm_untp_total_bidp_rsqn_icdc\": \"1\",\r\n        \"ovtm_untp_ntby_bidp_rsqn\": \"-16730\",\r\n        \"total_askp_rsqn\": \"923970\",\r\n        \"total_bidp_rsqn\": \"756893\",\r\n        \"total_askp_rsqn_icdc\": \"0\",\r\n        \"total_bidp_rsqn_icdc\": \"0\",\r\n        \"ovtm_total_askp_rsqn\": \"36230\",\r\n        \"ovtm_total_bidp_rsqn\": \"0\",\r\n        \"ovtm_total_askp_icdc\": \"0\",\r\n        \"ovtm_total_bidp_icdc\": \"0\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01060000",
    "name": "주식현재가 당일시간대별체결",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-itemconclusion",
    "sheet": "주식현재가 당일시간대별체결",
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
        "description": "single"
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
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rprs_mrkt_kor_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object",
        "required": "Y",
        "description": "single"
      },
      {
        "element": "stck_cntg_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_pbpr",
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
        "element": "tday_rltv",
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
        "element": "cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "\"input\": {\r\n            \"fid_cond_mrkt_div_code\": \"J\",\r\n            \"fid_input_hour_1\": \"141200\",\r\n            \"fid_input_iscd\": \"000660\"\r\n        }",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "\"output1\": {\r\n            \"acml_vol\": \"2315529\",\r\n            \"prdy_ctrt\": \"-2.80\",\r\n            \"prdy_vol\": \"1638006\",\r\n            \"prdy_vrss\": \"-3000\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"rprs_mrkt_kor_name\": \"KOSPI200\",\r\n            \"stck_prpr\": \"104000\"\r\n        },\r\n        \"output2\": [\r\n            {\r\n                \"acml_vol\": \"1979727\",\r\n                \"askp\": \"105000\",\r\n                \"bidp\": \"104500\",\r\n                \"cnqn\": \"20\",\r\n                \"prdy_ctrt\": \"-2.34\",\r\n                \"prdy_vrss\": \"-2500\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_cntg_hour\": \"141159\",\r\n                \"stck_prpr\": \"104500\",\r\n                \"tday_rltv\": \"42.43\"\r\n            },\r\n            {\r\n                \"acml_vol\": \"1979707\",\r\n                \"askp\": \"105000\",\r\n                \"bidp\": \"104500\",\r\n                \"cnqn\": \"4\",\r\n                \"prdy_ctrt\": \"-2.34\",\r\n                \"prdy_vrss\": \"-2500\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_cntg_hour\": \"141158\",\r\n                \"stck_prpr\": \"104500\",\r\n                \"tday_rltv\": \"42.43\"\r\n            },\r\n....\r\n            {\r\n                \"acml_vol\": \"1979079\",\r\n                \"askp\": \"105000\",\r\n                \"bidp\": \"104500\",\r\n                \"cnqn\": \"92\",\r\n                \"prdy_ctrt\": \"-2.34\",\r\n                \"prdy_vrss\": \"-2500\",\r\n                \"prdy_vrss_sign\": \"5\",\r\n                \"stck_cntg_hour\": \"141142\",\r\n                \"stck_prpr\": \"104500\",\r\n                \"tday_rltv\": \"42.44\"\r\n            }\r\n        ],\r\n        \"rt_cd\": \"0\"",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01010000",
    "name": "주식현재가 시세2",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-price-2",
    "sheet": "주식현재가 시세2",
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
        "element": "rprs_mrkt_kor_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "new_hgpr_lwpr_cls_code",
        "type": "string",
        "required": "Y",
        "description": "특정 경우에만 데이터 출력"
      },
      {
        "element": "mxpr_llam_cls_code",
        "type": "string",
        "required": "Y",
        "description": "특정 경우에만 데이터 출력"
      },
      {
        "element": "crdt_able_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_mxpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elw_pblc_yn",
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
        "element": "crdt_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "marg_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_vrss_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_vrss_prpr_sign",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_vrss_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_vrss_prpr_sign",
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
        "element": "stck_hgpr",
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
        "element": "oprc_vrss_prpr_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mang_issu_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "divi_app_cls_code",
        "type": "string",
        "required": "Y",
        "description": "11:매수상한배분 12:매수하한배분 13: 매도상한배분 14:매도하한배분"
      },
      {
        "element": "short_over_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_warn_cls_code",
        "type": "string",
        "required": "Y",
        "description": "00: 없음 01: 투자주의 02:투자경고 03:투자위험"
      },
      {
        "element": "invt_caful_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stange_runup_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ssts_hot_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "low_current_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vi_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "short_over_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_llam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "new_lstn_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vlnt_deal_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "flng_cls_name",
        "type": "string",
        "required": "Y",
        "description": "특정 경우에만 데이터 출력"
      },
      {
        "element": "revl_issu_reas_name",
        "type": "string",
        "required": "Y",
        "description": "특정 경우에만 데이터 출력"
      },
      {
        "element": "mrkt_warn_cls_name",
        "type": "string",
        "required": "Y",
        "description": "특정 경우에만 데이터 출력\r\n\"투자환기\" / \"투자경고\""
      },
      {
        "element": "stck_sdpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insn_pbnt_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fcam_mod_cls_name",
        "type": "string",
        "required": "Y",
        "description": "특정 경우에만 데이터 출력"
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
        "element": "acml_tr_pbmn",
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
        "element": "prdy_vrss_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": "※ 거래소 정보로 특정 종목은 업종구분이 없어 데이터 미회신"
      },
      {
        "element": "sltr_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trht_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_rang_cont_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vlnt_fin_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"J\",\r\n\"fid_input_iscd\":\"005930\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": {\r\n        \"rprs_mrkt_kor_name\": \"KOSPI200\",\r\n        \"insn_pbnt_yn\": \"N\",\r\n        \"stck_prpr\": \"74400\",\r\n        \"prdy_vrss\": \"1000\",\r\n        \"prdy_vrss_sign\": \"2\",\r\n        \"prdy_ctrt\": \"1.36\",\r\n        \"acml_tr_pbmn\": \"276161183000\",\r\n        \"acml_vol\": \"3733708\",\r\n        \"prdy_vol\": \"11160062\",\r\n        \"prdy_vrss_vol_rate\": \"33.46\",\r\n        \"bstp_kor_isnm\": \"전기.전자\",\r\n        \"sltr_yn\": \"N\",\r\n        \"mang_issu_yn\": \"N\",\r\n        \"trht_yn\": \"N\",\r\n        \"oprc_rang_cont_yn\": \"N\",\r\n        \"vlnt_fin_cls_code\": \"N\",\r\n        \"stck_prdy_clpr\": \"73400\",\r\n        \"stck_oprc\": \"73800\",\r\n        \"prdy_clpr_vrss_oprc_rate\": \"0.54\",\r\n        \"oprc_vrss_prpr_sign\": \"2\",\r\n        \"oprc_vrss_prpr\": \"600\",\r\n        \"stck_hgpr\": \"74500\",\r\n        \"prdy_clpr_vrss_hgpr_rate\": \"1.50\",\r\n        \"hgpr_vrss_prpr_sign\": \"5\",\r\n        \"hgpr_vrss_prpr\": \"-100\",\r\n        \"stck_lwpr\": \"73500\",\r\n        \"prdy_clpr_vrss_lwpr_rate\": \"0.14\",\r\n        \"lwpr_vrss_prpr_sign\": \"2\",\r\n        \"lwpr_vrss_prpr\": \"900\",\r\n        \"marg_rate\": \"20.00\",\r\n        \"crdt_rate\": \"20.00\",\r\n        \"crdt_able_yn\": \"Y\",\r\n        \"elw_pblc_yn\": \"Y\",\r\n        \"stck_mxpr\": \"95400\",\r\n        \"stck_llam\": \"51400\",\r\n        \"bstp_cls_code\": \"005930\",\r\n        \"stck_sdpr\": \"73400\",\r\n        \"vlnt_deal_cls_name\": \" \",\r\n        \"new_lstn_cls_name\": \"        \",\r\n        \"divi_app_cls_code\": \"  \",\r\n        \"short_over_cls_code\": \"          \",\r\n        \"vi_cls_code\": \"N\",\r\n        \"low_current_yn\": \"N\",\r\n        \"ssts_hot_yn\": \" \",\r\n        \"stange_runup_yn\": \"N\",\r\n        \"invt_caful_yn\": \"N\",\r\n        \"mrkt_warn_cls_code\": \"00\",\r\n        \"short_over_yn\": \"N\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST03010230",
    "name": "주식일별분봉조회",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-dailychartprice",
    "sheet": "주식일별분봉조회",
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
        "element": "stck_prdy_clpr",
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
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cntg_hour",
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
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
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
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_INPUT_ISCD:005930\r\nFID_INPUT_DATE_1:20241108\r\nFID_INPUT_HOUR_1:140000\r\nFID_PW_DATA_INCU_YN:Y\r\nFID_FAKE_TICK_INCU_YN:N",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"prdy_vrss\": \"-500\",\r\n        \"prdy_vrss_sign\": \"5\",\r\n        \"prdy_ctrt\": \"-0.87\",\r\n        \"stck_prdy_clpr\": \"57500\",\r\n        \"acml_vol\": \"13531211\",\r\n        \"acml_tr_pbmn\": \"779692013500\",\r\n        \"hts_kor_isnm\": \"삼성전자\",\r\n        \"stck_prpr\": \"57000\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"stck_bsop_date\": \"20241108\",\r\n            \"stck_cntg_hour\": \"140000\",\r\n            \"stck_prpr\": \"57300\",\r\n            \"stck_oprc\": \"57300\",\r\n            \"stck_hgpr\": \"57400\",\r\n            \"stck_lwpr\": \"57200\",\r\n            \"cntg_vol\": \"59047\",\r\n            \"acml_tr_pbmn\": \"538940180600\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20241108\",\r\n            \"stck_cntg_hour\": \"135900\",\r\n            \"stck_prpr\": \"57300\",\r\n            \"stck_oprc\": \"57400\",\r\n            \"stck_hgpr\": \"57500\",\r\n            \"stck_lwpr\": \"57300\",\r\n            \"cntg_vol\": \"118619\",\r\n            \"acml_tr_pbmn\": \"535556648100\"\r\n        },\r\n\t\t...\r\n        {\r\n            \"stck_bsop_date\": \"20241108\",\r\n            \"stck_cntg_hour\": \"120100\",\r\n            \"stck_prpr\": \"57700\",\r\n            \"stck_oprc\": \"57700\",\r\n            \"stck_hgpr\": \"57800\",\r\n            \"stck_lwpr\": \"57700\",\r\n            \"cntg_vol\": \"3856\",\r\n            \"acml_tr_pbmn\": \"357875441100\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST03010100",
    "name": "국내주식기간별시세(일_주_월_년)",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice",
    "sheet": "국내주식기간별시세(일_주_월_년)",
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
        "description": "single"
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
        "element": "stck_prdy_clpr",
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
        "element": "stck_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_mxpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_llam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_lwpr",
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
        "element": "prdy_vrss_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vol_tnrt",
        "type": "string",
        "required": "Y",
        "description": "11(8.2)"
      },
      {
        "element": "stck_fcam",
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
        "element": "cpfn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_avls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "per",
        "type": "string",
        "required": "Y",
        "description": "11(8.2)"
      },
      {
        "element": "eps",
        "type": "string",
        "required": "Y",
        "description": "14(11.2)"
      },
      {
        "element": "pbr",
        "type": "string",
        "required": "Y",
        "description": "11(8.2)"
      },
      {
        "element": "itewhol_loan_rmnd_ratem",
        "type": "string",
        "required": "Y",
        "description": "13(8.4)"
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
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
        "element": "flng_cls_code",
        "type": "string",
        "required": "Y",
        "description": "01 : 권리락\r\n02 : 배당락\r\n03 : 분배락\r\n04 : 권배락\r\n05 : 중간(분기)배당락\r\n06 : 권리중간배당락\r\n07 : 권리분기배당락"
      },
      {
        "element": "prtt_rate",
        "type": "string",
        "required": "Y",
        "description": "기준가/전일 종가"
      },
      {
        "element": "mod_yn",
        "type": "string",
        "required": "Y",
        "description": "현재 영업일에 체결이 발생하지 않아 시가가 없을경우 Y 로 표시(차트에서 사용)"
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
        "element": "revl_issu_reas",
        "type": "string",
        "required": "Y",
        "description": "00:해당없음\r\n01:회사분할\r\n02:자본감소\r\n03:장기간정지\r\n04:초과분배\r\n05:대규모배당\r\n06:회사분할합병\r\n07:ETN증권병합/분할\r\n08:신종증권기세조정\r\n99:기타"
      },
      {
        "element": "\"input\": {\r\n            \"fid_cond_mrkt_div_code\": \"J\",\r\n            \"fid_input_date_1\": \"20220411\",\r\n            \"fid_input_date_2\": \"20220509\",\r\n            \"fid_input_iscd\": \"000660\",\r\n            \"fid_org_adj_prc\": \"0\",\r\n            \"fid_period_div_code\": \"D\"\r\n        }",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "\"msg_cd\": \"MCA00000\",\r\n        \"output1\": {\r\n            \"acml_tr_pbmn\": \"236062833000\",\r\n            \"acml_vol\": \"2106409\",\r\n            \"askp\": \"112500\",\r\n            \"bidp\": \"112000\",\r\n            \"cpfn\": \"36577\",\r\n            \"eps\": \"13190.00\",\r\n            \"hts_avls\": \"815363\",\r\n            \"hts_kor_isnm\": \"SK\\ud558\\uc774\\ub2c9\\uc2a4\",\r\n            \"itewhol_loan_rmnd_ratem name\": \"0.32\",\r\n            \"lstn_stcn\": \"728002365\",\r\n            \"pbr\": \"1.26\",\r\n            \"per\": \"8.49\",\r\n            \"prdy_ctrt\": \"0.90\",\r\n            \"prdy_vol\": \"3680049\",\r\n            \"prdy_vrss\": \"1000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss_vol\": \"-1573640\",\r\n            \"stck_fcam\": \"5000\",\r\n            \"stck_hgpr\": \"113000\",\r\n            \"stck_llam\": \"78000\",\r\n            \"stck_lwpr\": \"111000\",\r\n            \"stck_mxpr\": \"144000\",\r\n            \"stck_oprc\": \"111500\",\r\n            \"stck_prdy_clpr\": \"111000\",\r\n            \"stck_prdy_hgpr\": \"112500\",\r\n            \"stck_prdy_lwpr\": \"110000\",\r\n            \"stck_prdy_oprc\": \"110500\",\r\n            \"stck_prpr\": \"112000\",\r\n            \"stck_shrn_iscd\": \"000660\",\r\n            \"vol_tnrt\": \"0.29\"\r\n        },\r\n        \"output2\": [\r\n            {\r\n                \"acml_tr_pbmn\": \"237914727500\",\r\n                \"acml_vol\": \"2203472\",\r\n                \"flng_cls_code\": \"00\",\r\n                \"mod_yn\": \"N\",\r\n                \"prdy_vrss\": \"0\",\r\n                \"prdy_vrss_sign\": \"3\",\r\n                \"prtt_rate\": \"0.00\",\r\n                \"revl_issu_reas\": \"\",\r\n                \"stck_bsop_date\": \"20220509\",\r\n                \"stck_clpr\": \"107500\",\r\n                \"stck_hgpr\": \"109000\",\r\n                \"stck_lwpr\": \"106500\",\r\n                \"stck_oprc\": \"107000\"\r\n            },\r\n....",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST01010200",
    "name": "주식현재가 호가_예상체결",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-asking-price-exp-ccn",
    "sheet": "주식현재가 호가_예상체결",
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
        "element": "aspr_acpt_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "askp_rsqn_icdc10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc6",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc7",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc8",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc9",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn_icdc10",
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
        "element": "total_askp_rsqn_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_bidp_rsqn_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_total_askp_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovtm_total_bidp_icdc",
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
        "element": "ntby_aspr_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "new_mkop_cls_code",
        "type": "string",
        "required": "Y",
        "description": "' '00' : 장전 예상체결가와 장마감 동시호가\r\n'49' : 장후 예상체결가\r\n\r\n(1) 첫 번째 비트\r\n1 : 장개시전\r\n2 : 장중\r\n3 : 장종료후\r\n4 : 시간외단일가\r\n7 : 일반Buy-in\r\n8 : 당일Buy-in\r\n(2) 두 번째 비트\r\n0 : 보통\r\n1 : 종가\r\n2 : 대량\r\n3 : 바스켓\r\n7 : 정리매매\r\n8 : Buy-in'"
      },
      {
        "element": "output2",
        "type": "object",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_mkop_cls_code",
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
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sdpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cnpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cntg_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cntg_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cntg_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_vol",
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
        "element": "vi_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\t\"fid_cond_mrkt_div_code\": \"J\",\r\n\t\"fid_input_iscd\": \"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output1\": {\r\n    \"aspr_acpt_hour\": \"160000\",\r\n    \"askp1\": \"128000\",\r\n    \"askp2\": \"128500\",\r\n    \"askp3\": \"129000\",\r\n    \"askp4\": \"129500\",\r\n    \"askp5\": \"130000\",\r\n    \"askp6\": \"130500\",\r\n    \"askp7\": \"131000\",\r\n    \"askp8\": \"131500\",\r\n    \"askp9\": \"132000\",\r\n    \"askp10\": \"132500\",\r\n    \"bidp1\": \"127500\",\r\n    \"bidp2\": \"127000\",\r\n    \"bidp3\": \"126500\",\r\n    \"bidp4\": \"126000\",\r\n    \"bidp5\": \"125500\",\r\n    \"bidp6\": \"125000\",\r\n    \"bidp7\": \"124500\",\r\n    \"bidp8\": \"124000\",\r\n    \"bidp9\": \"123500\",\r\n    \"bidp10\": \"123000\",\r\n    \"askp_rsqn1\": \"69454\",\r\n    \"askp_rsqn2\": \"189698\",\r\n    \"askp_rsqn3\": \"154732\",\r\n    \"askp_rsqn4\": \"85703\",\r\n    \"askp_rsqn5\": \"158696\",\r\n    \"askp_rsqn6\": \"31395\",\r\n    \"askp_rsqn7\": \"50738\",\r\n    \"askp_rsqn8\": \"21039\",\r\n    \"askp_rsqn9\": \"39424\",\r\n    \"askp_rsqn10\": \"29126\",\r\n    \"bidp_rsqn1\": \"83147\",\r\n    \"bidp_rsqn2\": \"27469\",\r\n    \"bidp_rsqn3\": \"25200\",\r\n    \"bidp_rsqn4\": \"18544\",\r\n    \"bidp_rsqn5\": \"13251\",\r\n    \"bidp_rsqn6\": \"15742\",\r\n    \"bidp_rsqn7\": \"15070\",\r\n    \"bidp_rsqn8\": \"24995\",\r\n    \"bidp_rsqn9\": \"11658\",\r\n    \"bidp_rsqn10\": \"15773\",\r\n    \"askp_rsqn_icdc1\": \"0\",\r\n    \"askp_rsqn_icdc2\": \"0\",\r\n    \"askp_rsqn_icdc3\": \"0\",\r\n    \"askp_rsqn_icdc4\": \"0\",\r\n    \"askp_rsqn_icdc5\": \"0\",\r\n    \"askp_rsqn_icdc6\": \"0\",\r\n    \"askp_rsqn_icdc7\": \"0\",\r\n    \"askp_rsqn_icdc8\": \"0\",\r\n    \"askp_rsqn_icdc9\": \"0\",\r\n    \"askp_rsqn_icdc10\": \"0\",\r\n    \"bidp_rsqn_icdc1\": \"0\",\r\n    \"bidp_rsqn_icdc2\": \"0\",\r\n    \"bidp_rsqn_icdc3\": \"0\",\r\n    \"bidp_rsqn_icdc4\": \"0\",\r\n    \"bidp_rsqn_icdc5\": \"0\",\r\n    \"bidp_rsqn_icdc6\": \"0\",\r\n    \"bidp_rsqn_icdc7\": \"0\",\r\n    \"bidp_rsqn_icdc8\": \"0\",\r\n    \"bidp_rsqn_icdc9\": \"0\",\r\n    \"bidp_rsqn_icdc10\": \"0\",\r\n    \"total_askp_rsqn\": \"830005\",\r\n    \"total_bidp_rsqn\": \"250849\",\r\n    \"total_askp_rsqn_icdc\": \"0\",\r\n    \"total_bidp_rsqn_icdc\": \"0\",\r\n    \"ovtm_total_askp_icdc\": \"0\",\r\n    \"ovtm_total_bidp_icdc\": \"0\",\r\n    \"ovtm_total_askp_rsqn\": \"2943\",\r\n    \"ovtm_total_bidp_rsqn\": \"0\",\r\n    \"ntby_aspr_rsqn\": \"-579156\",\r\n    \"new_mkop_cls_code\": \"31\"\r\n  },\r\n  \"output2\": {\r\n    \"antc_mkop_cls_code\": \"112\",\r\n    \"stck_prpr\": \"128000\",\r\n    \"stck_oprc\": \"125500\",\r\n    \"stck_hgpr\": \"128500\",\r\n    \"stck_lwpr\": \"124500\",\r\n    \"stck_sdpr\": \"124500\",\r\n    \"antc_cnpr\": \"128000\",\r\n    \"antc_cntg_vrss_sign\": \"2\",\r\n    \"antc_cntg_vrss\": \"3500\",\r\n    \"antc_cntg_prdy_ctrt\": \"2.81\",\r\n    \"antc_vol\": \"220006\",\r\n    \"stck_shrn_iscd\": \"000660\",\r\n    \"vi_cls_code\": \"N\"\r\n  },\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST01010300",
    "name": "주식현재가 체결",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-ccnl",
    "sheet": "주식현재가 체결",
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
        "element": "stck_cntg_hour",
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
        "element": "tday_rltv",
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
        "element": "{\r\n\"fid_cond_mrkt_div_code\": \"J\",\r\n\"fid_input_iscd\": \"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output\": [\r\n    {\r\n      \"stck_cntg_hour\": \"155955\",\r\n      \"stck_prpr\": \"78900\",\r\n      \"prdy_vrss\": \"900\",\r\n      \"prdy_vrss_sign\": \"2\",\r\n      \"cntg_vol\": \"2\",\r\n      \"tday_rltv\": \"114.05\",\r\n      \"prdy_ctrt\": \"1.15\"\r\n    },\r\n    {\r\n      \"stck_cntg_hour\": \"155935\",\r\n      \"stck_prpr\": \"78900\",\r\n      \"prdy_vrss\": \"900\",\r\n      \"prdy_vrss_sign\": \"2\",\r\n      \"cntg_vol\": \"10\",\r\n      \"tday_rltv\": \"114.05\",\r\n      \"prdy_ctrt\": \"1.15\"\r\n    }\r\n\t  ],\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST01010600",
    "name": "주식현재가 회원사",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-member",
    "sheet": "주식현재가 회원사",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "성공 실패 여부 \r\n성공 : 0   실패 : 0외 값"
      },
      {
        "element": "msg_cd",
        "type": "string",
        "required": "Y",
        "description": "응답코드"
      },
      {
        "element": "msg1",
        "type": "string",
        "required": "Y",
        "description": "응답메세지"
      },
      {
        "element": "output",
        "type": "array",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_no1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_no2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_no3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_no4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_no5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_name1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_name2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_name3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_name4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_name5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_seln_qty1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_seln_qty2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_seln_qty3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_seln_qty4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_seln_qty5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_rlim1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_rlim2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_rlim3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_rlim4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_rlim5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_qty_icdc1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_qty_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_qty_icdc3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_qty_icdc4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_qty_icdc5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_no1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_no2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_no3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_no4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_no5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_name1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_name2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_name3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_name4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_name5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_shnu_qty1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_shnu_qty2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_shnu_qty3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_shnu_qty4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "total_shnu_qty5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_rlim1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_rlim2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_rlim3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_rlim4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_rlim5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_qty_icdc1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_qty_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_qty_icdc3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_qty_icdc4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_qty_icdc5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_total_seln_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_seln_rlim",
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
        "element": "glob_total_shnu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_shnu_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_glob_yn_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_glob_yn_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_glob_yn_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_glob_yn_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_mbcr_glob_yn_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_glob_yn_1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_glob_yn_2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_glob_yn_3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_glob_yn_4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_mbcr_glob_yn_5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_total_seln_qty_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_total_shnu_qty_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\": \"J\",\r\n\"fid_input_iscd\": \"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output\": {\r\n    \"seln_mbcr_no1\": \"00086\",\r\n    \"seln_mbcr_no2\": \"00005\",\r\n    \"seln_mbcr_no3\": \"00050\",\r\n    \"seln_mbcr_no4\": \"00030\",\r\n    \"seln_mbcr_no5\": \"00002\",\r\n    \"seln_mbcr_name1\": \"BNK증권\",\r\n    \"seln_mbcr_name2\": \"미래에셋증권\",\r\n    \"seln_mbcr_name3\": \"키움증권\",\r\n    \"seln_mbcr_name4\": \"삼성증권\",\r\n    \"seln_mbcr_name5\": \"신한투자\",\r\n    \"total_seln_qty1\": \"801848\",\r\n    \"total_seln_qty2\": \"684589\",\r\n    \"total_seln_qty3\": \"310639\",\r\n    \"total_seln_qty4\": \"275035\",\r\n    \"total_seln_qty5\": \"235001\",\r\n    \"seln_mbcr_rlim1\": \"20.52\",\r\n    \"seln_mbcr_rlim2\": \"17.52\",\r\n    \"seln_mbcr_rlim3\": \"7.95\",\r\n    \"seln_mbcr_rlim4\": \"7.04\",\r\n    \"seln_mbcr_rlim5\": \"6.01\",\r\n    \"seln_qty_icdc1\": \"8000\",\r\n    \"seln_qty_icdc2\": \"39472\",\r\n    \"seln_qty_icdc3\": \"27755\",\r\n    \"seln_qty_icdc4\": \"13612\",\r\n    \"seln_qty_icdc5\": \"4047\",\r\n    \"shnu_mbcr_no1\": \"00086\",\r\n    \"shnu_mbcr_no2\": \"00005\",\r\n    \"shnu_mbcr_no3\": \"00033\",\r\n    \"shnu_mbcr_no4\": \"00045\",\r\n    \"shnu_mbcr_no5\": \"00036\",\r\n    \"shnu_mbcr_name1\": \"BNK증권\",\r\n    \"shnu_mbcr_name2\": \"미래에셋증권\",\r\n    \"shnu_mbcr_name3\": \"JP모간\",\r\n    \"shnu_mbcr_name4\": \"골드만\",\r\n    \"shnu_mbcr_name5\": \"모간서울\",\r\n    \"total_shnu_qty1\": \"822175\",\r\n    \"total_shnu_qty2\": \"598966\",\r\n    \"total_shnu_qty3\": \"378758\",\r\n    \"total_shnu_qty4\": \"354965\",\r\n    \"total_shnu_qty5\": \"261357\",\r\n    \"shnu_mbcr_rlim1\": \"21.04\",\r\n    \"shnu_mbcr_rlim2\": \"15.33\",\r\n    \"shnu_mbcr_rlim3\": \"9.69\",\r\n    \"shnu_mbcr_rlim4\": \"9.08\",\r\n    \"shnu_mbcr_rlim5\": \"6.69\",\r\n    \"shnu_qty_icdc1\": \"0\",\r\n    \"shnu_qty_icdc2\": \"2397\",\r\n    \"shnu_qty_icdc3\": \"20698\",\r\n    \"shnu_qty_icdc4\": \"17168\",\r\n    \"shnu_qty_icdc5\": \"11893\",\r\n    \"glob_total_seln_qty\": \"38125\",\r\n    \"glob_seln_rlim\": \"0.98\",\r\n    \"glob_ntby_qty\": \"1142513\",\r\n    \"glob_total_shnu_qty\": \"1180638\",\r\n    \"glob_shnu_rlim\": \"30.21\",\r\n    \"seln_mbcr_glob_yn_1\": \"N\",\r\n    \"seln_mbcr_glob_yn_2\": \"N\",\r\n    \"seln_mbcr_glob_yn_3\": \"N\",\r\n    \"seln_mbcr_glob_yn_4\": \"N\",\r\n    \"seln_mbcr_glob_yn_5\": \"N\",\r\n    \"shnu_mbcr_glob_yn_1\": \"N\",\r\n    \"shnu_mbcr_glob_yn_2\": \"N\",\r\n    \"shnu_mbcr_glob_yn_3\": \"Y\",\r\n    \"shnu_mbcr_glob_yn_4\": \"Y\",\r\n    \"shnu_mbcr_glob_yn_5\": \"Y\",\r\n    \"glob_total_seln_qty_icdc\": \"0\",\r\n    \"glob_total_shnu_qty_icdc\": \"49759\"\r\n  },\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST01010900",
    "name": "주식현재가 투자자",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-investor",
    "sheet": "주식현재가 투자자",
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
        "description": "Array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_clpr",
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
        "element": "prsn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\": \"J\",\r\n\"fid_input_iscd\": \"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output\": [\r\n    {\r\n      \"stck_bsop_date\": \"20220113\",\r\n      \"stck_clpr\": \"129500\",\r\n      \"prdy_vrss\": \"1000\",\r\n      \"prdy_vrss_sign\": \"2\",\r\n      \"prsn_ntby_qty\": \"-287624\",\r\n      \"frgn_ntby_qty\": \"797458\",\r\n      \"orgn_ntby_qty\": \"-503653\",\r\n      \"prsn_ntby_tr_pbmn\": \"-37176\",\r\n      \"frgn_ntby_tr_pbmn\": \"102959\",\r\n      \"orgn_ntby_tr_pbmn\": \"-64984\",\r\n      \"prsn_shnu_vol\": \"467525\",\r\n      \"frgn_shnu_vol\": \"1442791\",\r\n      \"orgn_shnu_vol\": \"2219433\",\r\n      \"prsn_shnu_tr_pbmn\": \"60368\",\r\n      \"frgn_shnu_tr_pbmn\": \"186166\",\r\n      \"orgn_shnu_tr_pbmn\": \"286505\",\r\n      \"prsn_seln_vol\": \"755149\",\r\n      \"frgn_seln_vol\": \"645333\",\r\n      \"orgn_seln_vol\": \"2723086\",\r\n      \"prsn_seln_tr_pbmn\": \"97544\",\r\n      \"frgn_seln_tr_pbmn\": \"83207\",\r\n      \"orgn_seln_tr_pbmn\": \"351489\"\r\n    },\r\n    {\r\n      \"stck_bsop_date\": \"20220112\",\r\n      \"stck_clpr\": \"128500\",\r\n      \"prdy_vrss\": \"500\",\r\n      \"prdy_vrss_sign\": \"2\",\r\n      \"prsn_ntby_qty\": \"-74249\",\r\n      \"frgn_ntby_qty\": \"-134600\",\r\n      \"orgn_ntby_qty\": \"206812\",\r\n      \"prsn_ntby_tr_pbmn\": \"-9687\",\r\n      \"frgn_ntby_tr_pbmn\": \"-17094\",\r\n      \"orgn_ntby_tr_pbmn\": \"26530\",\r\n      \"prsn_shnu_vol\": \"608748\",\r\n      \"frgn_shnu_vol\": \"721756\",\r\n      \"orgn_shnu_vol\": \"2201966\",\r\n      \"prsn_shnu_tr_pbmn\": \"77943\",\r\n      \"frgn_shnu_tr_pbmn\": \"92615\",\r\n      \"orgn_shnu_tr_pbmn\": \"281965\",\r\n      \"prsn_seln_vol\": \"682997\",\r\n      \"frgn_seln_vol\": \"856356\",\r\n      \"orgn_seln_vol\": \"1995154\",\r\n      \"prsn_seln_tr_pbmn\": \"87630\",\r\n      \"frgn_seln_tr_pbmn\": \"109708\",\r\n      \"orgn_seln_tr_pbmn\": \"255435\"\r\n    }\r\n\t  ],\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST117300C0",
    "name": "국내주식 장마감 예상체결가",
    "url": "/uapi/domestic-stock/v1/quotations/exp-closing-price",
    "sheet": "국내주식 장마감 예상체결가",
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
        "element": "sdpr_vrss_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sdpr_vrss_prpr_rate",
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
        "element": "fid_cond_mrkt_div_code:J\r\nfid_cond_scr_div_code:11173\r\nfid_input_iscd:0001\r\nfid_blng_cls_code:0\r\nfid_rank_sort_cls_code:0",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST03010200",
    "name": "주식당일분봉조회",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice",
    "sheet": "주식당일분봉조회",
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
        "element": "prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": "전일 대비 변동 (+-변동차이)"
      },
      {
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": "전일 대비 부호"
      },
      {
        "element": "prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": "소수점 두자리까지 제공"
      },
      {
        "element": "stck_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": "전일대비 종가"
      },
      {
        "element": "acml_vol",
        "type": "string",
        "required": "Y",
        "description": "누적 거래량"
      },
      {
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": "누적 거래대금"
      },
      {
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": "한글 종목명 (HTS 기준)"
      },
      {
        "element": "stck_prpr",
        "type": "string",
        "required": "Y",
        "description": "주식 현재가"
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": "주식 영업일자"
      },
      {
        "element": "stck_cntg_hour",
        "type": "string",
        "required": "Y",
        "description": "주식 체결시간"
      },
      {
        "element": "stck_prpr",
        "type": "string",
        "required": "Y",
        "description": "주식 현재가"
      },
      {
        "element": "stck_oprc",
        "type": "string",
        "required": "Y",
        "description": "주식 시가"
      },
      {
        "element": "stck_hgpr",
        "type": "string",
        "required": "Y",
        "description": "주식 최고가"
      },
      {
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": "주식 최저가"
      },
      {
        "element": "cntg_vol",
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
        "element": "{\r\n            \"fid_cond_mrkt_div_code\": \"J\",\r\n            \"fid_etc_cls_code\": \"\",\r\n            \"fid_input_hour_1\": \"100000\",\r\n            \"fid_input_iscd\": \"000660\",\r\n            \"fid_pw_data_incu_yn\": \"Y\"\r\n }",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n        \"output1\": {\r\n            \"acml_tr_pbmn\": \"96910660000\",\r\n            \"acml_vol\": \"1046883\",\r\n            \"hts_kor_isnm\": \"SK하이닉스\",\r\n            \"prdy_ctrt\": \"-0.11\",\r\n            \"prdy_vrss\": \"-100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"stck_prdy_clpr\": \"92400\",\r\n            \"stck_prpr\": \"92300\"\r\n        },\r\n        \"output2\": [\r\n            {\r\n                \"acml_tr_pbmn\": \"55858827400\",\r\n                \"cntg_vol\": \"1383\",\r\n                \"stck_bsop_date\": \"20220902\",\r\n                \"stck_cntg_hour\": \"100000\",\r\n                \"stck_hgpr\": \"92500\",\r\n                \"stck_lwpr\": \"92400\",\r\n                \"stck_oprc\": \"92400\",\r\n                \"stck_prpr\": \"92500\"\r\n            },\r\n            {\r\n                \"acml_tr_pbmn\": \"55731000300\",\r\n                \"cntg_vol\": \"1564\",\r\n                \"stck_bsop_date\": \"20220902\",\r\n                \"stck_cntg_hour\": \"095900\",\r\n                \"stck_hgpr\": \"92500\",\r\n                \"stck_lwpr\": \"92400\",\r\n                \"stck_oprc\": \"92500\",\r\n                \"stck_prpr\": \"92400\"\r\n                              \"stck_hgpr\": \"93300\",\r\n                \"stck_lwpr\": \"93100\",\r\n                \"stck_oprc\": \"93100\",\r\n                \"stck_prpr\": \"93200\"\r\n            }\r\n            ......\r\n        ],\r\n        \"rt_cd\": \"0\",\r\n         \"msg_cd\": \"MCA00000\",\r\n         \"msg1\": \"정상처리 되었습니다!\"\r\n }",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKEW15010000",
    "name": "ELW 현재가 시세",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-elw-price",
    "sheet": "ELW 현재가 시세",
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
        "element": "elw_shrn_iscd",
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
        "element": "elw_prpr",
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
        "element": "prdy_vrss_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "unas_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "unas_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "unas_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "unas_prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "unas_prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "unas_prdy_ctrt",
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
      },
      {
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vol_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elw_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elw_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elw_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_thpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dprt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "atm_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_ints_vltl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_scnd_dmrs_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_frst_dmrs_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_pont_val",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_frst_dmsp_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pvt_scnd_dmsp_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dmsp_val",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dmrs_val",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elw_sdpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "apprch_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tick_conv_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "invt_epmd_cntt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\": \"J\",\r\n\"fid_input_iscd\": \"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n  \"output\": {\r\n    \"elw_prpr\": \"0\",\r\n    \"prdy_vrss\": \"0\",\r\n    \"prdy_ctrt\": \"0.00\",\r\n    \"acml_vol\": \"0\",\r\n    \"prdy_vrss_vol_rate\": \"0.00\",\r\n    \"unas_isnm\": \"BASKET\",\r\n    \"unas_prpr\": \"0.00\",\r\n    \"unas_prdy_vrss\": \"0.00\",\r\n    \"unas_prdy_vrss_sign\": \"3\",\r\n    \"unas_prdy_ctrt\": \"0.00\",\r\n    \"bidp\": \"0\",\r\n    \"askp\": \"0\",\r\n    \"acml_tr_pbmn\": \"0\",\r\n    \"vol_tnrt\": \"0.00\",\r\n    \"elw_oprc\": \"0\",\r\n    \"elw_hgpr\": \"0\",\r\n    \"elw_lwpr\": \"0\",\r\n    \"stck_prdy_clpr\": \"0\",\r\n    \"hts_thpr\": \"0.00\",\r\n    \"dprt\": \"0.00\",\r\n    \"atm_cls_name\": \"ATM\",\r\n    \"hts_ints_vltl\": \"0.00\",\r\n    \"acpr\": \"0.00\",\r\n    \"pvt_scnd_dmrs_prc\": \"0\",\r\n    \"pvt_frst_dmrs_prc\": \"0\",\r\n    \"pvt_pont_val\": \"0\",\r\n    \"pvt_frst_dmsp_prc\": \"0\",\r\n    \"pvt_scnd_dmsp_prc\": \"0\",\r\n    \"dmsp_val\": \"0\",\r\n    \"dmrs_val\": \"0\",\r\n    \"elw_sdpr\": \"0\",\r\n    \"apprch_rate\": \"0.00\",\r\n    \"tick_conv_prc\": \"0.00\"\r\n  },\r\n  \"rt_cd\": \"0\",\r\n  \"msg_cd\": \"MCA00000\",\r\n  \"msg1\": \"정상처리 되었습니다!\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01840000",
    "name": "국내주식 예상체결지수 추이",
    "url": "/uapi/domestic-stock/v1/quotations/exp-index-trend",
    "sheet": "국내주식 예상체결지수 추이",
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
        "element": "stck_cntg_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "fid_cond_mrkt_div_code:U\r\nfid_input_iscd:0001\r\nfid_input_hour_1:\r\nfid_mkop_cls_code:1",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_cntg_hour\": \"666666\",\r\n            \"bstp_nmix_prpr\": \"2765.30\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"18.67\",\r\n            \"prdy_ctrt\": \"0.68\",\r\n            \"acml_vol\": \"5951\",\r\n            \"acml_tr_pbmn\": \"130953\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085950\",\r\n            \"bstp_nmix_prpr\": \"2766.50\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"19.87\",\r\n            \"prdy_ctrt\": \"0.72\",\r\n            \"acml_vol\": \"5641\",\r\n            \"acml_tr_pbmn\": \"122873\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085940\",\r\n            \"bstp_nmix_prpr\": \"2768.19\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"21.56\",\r\n            \"prdy_ctrt\": \"0.78\",\r\n            \"acml_vol\": \"5369\",\r\n            \"acml_tr_pbmn\": \"115013\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085930\",\r\n            \"bstp_nmix_prpr\": \"2766.70\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.07\",\r\n            \"prdy_ctrt\": \"0.73\",\r\n            \"acml_vol\": \"5168\",\r\n            \"acml_tr_pbmn\": \"107488\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085920\",\r\n            \"bstp_nmix_prpr\": \"2767.01\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.38\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"5052\",\r\n            \"acml_tr_pbmn\": \"103832\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085910\",\r\n            \"bstp_nmix_prpr\": \"2767.09\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.46\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4919\",\r\n            \"acml_tr_pbmn\": \"101950\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085900\",\r\n            \"bstp_nmix_prpr\": \"2766.91\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.28\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4840\",\r\n            \"acml_tr_pbmn\": \"99526\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085850\",\r\n            \"bstp_nmix_prpr\": \"2767.06\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.43\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4740\",\r\n            \"acml_tr_pbmn\": \"93391\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085840\",\r\n            \"bstp_nmix_prpr\": \"2767.12\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.49\",\r\n            \"prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"4655\",\r\n            \"acml_tr_pbmn\": \"92533\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085830\",\r\n            \"bstp_nmix_prpr\": \"2767.27\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.64\",\r\n            \"prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"4639\",\r\n            \"acml_tr_pbmn\": \"91639\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085820\",\r\n            \"bstp_nmix_prpr\": \"2767.35\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.72\",\r\n            \"prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"4560\",\r\n            \"acml_tr_pbmn\": \"90798\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085810\",\r\n            \"bstp_nmix_prpr\": \"2767.22\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.59\",\r\n            \"prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"4541\",\r\n            \"acml_tr_pbmn\": \"93370\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085800\",\r\n            \"bstp_nmix_prpr\": \"2767.08\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.45\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4487\",\r\n            \"acml_tr_pbmn\": \"91617\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085750\",\r\n            \"bstp_nmix_prpr\": \"2766.75\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.12\",\r\n            \"prdy_ctrt\": \"0.73\",\r\n            \"acml_vol\": \"4440\",\r\n            \"acml_tr_pbmn\": \"90268\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085740\",\r\n            \"bstp_nmix_prpr\": \"2766.96\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.33\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4483\",\r\n            \"acml_tr_pbmn\": \"90078\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085730\",\r\n            \"bstp_nmix_prpr\": \"2766.93\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.30\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4427\",\r\n            \"acml_tr_pbmn\": \"89631\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085720\",\r\n            \"bstp_nmix_prpr\": \"2766.96\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.33\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4402\",\r\n            \"acml_tr_pbmn\": \"89052\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085710\",\r\n            \"bstp_nmix_prpr\": \"2767.00\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.37\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4525\",\r\n            \"acml_tr_pbmn\": \"87706\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085700\",\r\n            \"bstp_nmix_prpr\": \"2767.08\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.45\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4660\",\r\n            \"acml_tr_pbmn\": \"84754\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085650\",\r\n            \"bstp_nmix_prpr\": \"2767.40\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.77\",\r\n            \"prdy_ctrt\": \"0.76\",\r\n            \"acml_vol\": \"4636\",\r\n            \"acml_tr_pbmn\": \"84339\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085640\",\r\n            \"bstp_nmix_prpr\": \"2767.30\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.67\",\r\n            \"prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"4569\",\r\n            \"acml_tr_pbmn\": \"84041\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085630\",\r\n            \"bstp_nmix_prpr\": \"2767.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.74\",\r\n            \"prdy_ctrt\": \"0.76\",\r\n            \"acml_vol\": \"4559\",\r\n            \"acml_tr_pbmn\": \"83314\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085620\",\r\n            \"bstp_nmix_prpr\": \"2767.43\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.80\",\r\n            \"prdy_ctrt\": \"0.76\",\r\n            \"acml_vol\": \"4490\",\r\n            \"acml_tr_pbmn\": \"83074\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085610\",\r\n            \"bstp_nmix_prpr\": \"2767.74\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"21.11\",\r\n            \"prdy_ctrt\": \"0.77\",\r\n            \"acml_vol\": \"4436\",\r\n            \"acml_tr_pbmn\": \"80274\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085600\",\r\n            \"bstp_nmix_prpr\": \"2766.95\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.32\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4032\",\r\n            \"acml_tr_pbmn\": \"78386\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085550\",\r\n            \"bstp_nmix_prpr\": \"2766.86\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.23\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"4026\",\r\n            \"acml_tr_pbmn\": \"77796\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085540\",\r\n            \"bstp_nmix_prpr\": \"2766.90\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.27\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"3946\",\r\n            \"acml_tr_pbmn\": \"76794\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085530\",\r\n            \"bstp_nmix_prpr\": \"2767.15\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.52\",\r\n            \"prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"3932\",\r\n            \"acml_tr_pbmn\": \"76859\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085520\",\r\n            \"bstp_nmix_prpr\": \"2766.95\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"20.32\",\r\n            \"prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"3922\",\r\n            \"acml_tr_pbmn\": \"75766\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"085510\",\r\n            \"bstp_nmix_prpr\": \"2766.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"19.74\",\r\n            \"prdy_ctrt\": \"0.72\",\r\n            \"acml_vol\": \"4008\",\r\n            \"acml_tr_pbmn\": \"75458\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKUP03500100",
    "name": "국내주식업종기간별시세(일_주_월_년)",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice",
    "sheet": "국내주식업종기간별시세(일_주_월_년)",
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
        "description": "Single"
      },
      {
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_nmix",
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
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "futs_prdy_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "futs_prdy_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "futs_prdy_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
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
        "element": "mod_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "\"input\": {\r\n            \"fid_cond_mrkt_div_code\": \"U\",\r\n            \"fid_input_date_1\": \"20220411\",\r\n            \"fid_input_date_2\": \"20220509\",\r\n            \"fid_input_iscd\": \"0001\",\r\n            \"fid_period_div_code\": \"D\"\r\n        }",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "\"output1\": {\r\n            \"acml_tr_pbmn\": \"4736153\",\r\n            \"acml_vol\": \"305715\",\r\n            \"bstp_cls_code\": \"0001\",\r\n            \"bstp_nmix_hgpr\": \"2653.87\",\r\n            \"bstp_nmix_lwpr\": \"2634.29\",\r\n            \"bstp_nmix_oprc\": \"2651.63\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.11\",\r\n            \"bstp_nmix_prdy_vrss\": \"2.78\",\r\n            \"bstp_nmix_prpr\": \"2642.07\",\r\n            \"futs_prdy_hgpr\": \"2641.68\",\r\n            \"futs_prdy_lwpr\": \"2605.38\",\r\n            \"futs_prdy_oprc\": \"2605.78\",\r\n            \"hts_kor_isnm\": \"\\uc885\\ud569\",\r\n            \"prdy_nmix\": \"2639.29\",\r\n            \"prdy_vol\": \"755653\",\r\n            \"prdy_vrss_sign\": \"2\"\r\n        },\r\n        \"output2\": [\r\n            {\r\n                \"acml_tr_pbmn\": \"9289660\",\r\n                \"acml_vol\": \"892653\",\r\n                \"bstp_nmix_hgpr\": \"2642.75\",\r\n                \"bstp_nmix_lwpr\": \"2606.08\",\r\n                \"bstp_nmix_oprc\": \"2634.32\",\r\n                \"bstp_nmix_prpr\": \"2610.81\",\r\n                \"mod_yn\": \"N\",\r\n                \"stck_bsop_date\": \"20220509\"\r\n            },\r\n            {\r\n                \"acml_tr_pbmn\": \"10595418\",\r\n                \"acml_vol\": \"1333936\",\r\n.....",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPUP02110200",
    "name": "국내업종 시간별지수(분)",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-timeprice",
    "sheet": "국내업종 시간별지수(분)",
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
        "element": "bsop_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "acml_vol",
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
        "element": "fid_cond_mrkt_div_code:U\r\nfid_input_iscd:1001\r\nfid_input_hour_1:120",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"bsop_hour\": \"100600\",\r\n            \"bstp_nmix_prpr\": \"916.77\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.27\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3839797\",\r\n            \"acml_vol\": \"313374\",\r\n            \"cntg_vol\": \"870\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"100400\",\r\n            \"bstp_nmix_prpr\": \"916.65\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.15\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3829216\",\r\n            \"acml_vol\": \"312504\",\r\n            \"cntg_vol\": \"4352\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"100200\",\r\n            \"bstp_nmix_prpr\": \"916.69\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.19\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3779730\",\r\n            \"acml_vol\": \"308152\",\r\n            \"cntg_vol\": \"4959\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"100000\",\r\n            \"bstp_nmix_prpr\": \"916.76\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.26\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3716791\",\r\n            \"acml_vol\": \"303193\",\r\n            \"cntg_vol\": \"5103\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"095800\",\r\n            \"bstp_nmix_prpr\": \"916.60\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3651490\",\r\n            \"acml_vol\": \"298090\",\r\n            \"cntg_vol\": \"5732\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"095600\",\r\n            \"bstp_nmix_prpr\": \"917.37\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.87\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.31\",\r\n            \"acml_tr_pbmn\": \"3588380\",\r\n            \"acml_vol\": \"292358\",\r\n            \"cntg_vol\": \"5331\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"095400\",\r\n            \"bstp_nmix_prpr\": \"917.64\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.14\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n            \"acml_tr_pbmn\": \"3521010\",\r\n            \"acml_vol\": \"287027\",\r\n            \"cntg_vol\": \"6827\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"095200\",\r\n            \"bstp_nmix_prpr\": \"916.31\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.81\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.19\",\r\n            \"acml_tr_pbmn\": \"3445942\",\r\n            \"acml_vol\": \"280200\",\r\n            \"cntg_vol\": \"7263\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"095000\",\r\n            \"bstp_nmix_prpr\": \"916.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3373037\",\r\n            \"acml_vol\": \"272937\",\r\n            \"cntg_vol\": \"5040\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"094800\",\r\n            \"bstp_nmix_prpr\": \"916.82\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.32\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3304716\",\r\n            \"acml_vol\": \"267897\",\r\n            \"cntg_vol\": \"6828\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"094600\",\r\n            \"bstp_nmix_prpr\": \"916.74\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.24\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3222590\",\r\n            \"acml_vol\": \"261069\",\r\n            \"cntg_vol\": \"8510\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"094400\",\r\n            \"bstp_nmix_prpr\": \"914.70\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.20\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.02\",\r\n            \"acml_tr_pbmn\": \"3137995\",\r\n            \"acml_vol\": \"252559\",\r\n            \"cntg_vol\": \"6781\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"094200\",\r\n            \"bstp_nmix_prpr\": \"914.33\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.83\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.98\",\r\n            \"acml_tr_pbmn\": \"3073035\",\r\n            \"acml_vol\": \"245778\",\r\n            \"cntg_vol\": \"7274\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"094000\",\r\n            \"bstp_nmix_prpr\": \"914.00\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.50\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.94\",\r\n            \"acml_tr_pbmn\": \"3001499\",\r\n            \"acml_vol\": \"238504\",\r\n            \"cntg_vol\": \"7439\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"093800\",\r\n            \"bstp_nmix_prpr\": \"913.15\",\r\n            \"bstp_nmix_prdy_vrss\": \"7.65\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.84\",\r\n            \"acml_tr_pbmn\": \"2908979\",\r\n            \"acml_vol\": \"231065\",\r\n            \"cntg_vol\": \"8180\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"093600\",\r\n            \"bstp_nmix_prpr\": \"912.23\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.73\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.74\",\r\n            \"acml_tr_pbmn\": \"2815470\",\r\n            \"acml_vol\": \"222885\",\r\n            \"cntg_vol\": \"7271\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"093400\",\r\n            \"bstp_nmix_prpr\": \"911.14\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.64\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.62\",\r\n            \"acml_tr_pbmn\": \"2729472\",\r\n            \"acml_vol\": \"215614\",\r\n            \"cntg_vol\": \"6032\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"093200\",\r\n            \"bstp_nmix_prpr\": \"911.12\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.62\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.62\",\r\n            \"acml_tr_pbmn\": \"2640030\",\r\n            \"acml_vol\": \"209582\",\r\n            \"cntg_vol\": \"7254\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"093000\",\r\n            \"bstp_nmix_prpr\": \"910.35\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.85\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.54\",\r\n            \"acml_tr_pbmn\": \"2542281\",\r\n            \"acml_vol\": \"202328\",\r\n            \"cntg_vol\": \"7789\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"092800\",\r\n            \"bstp_nmix_prpr\": \"911.05\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.55\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.61\",\r\n            \"acml_tr_pbmn\": \"2420975\",\r\n            \"acml_vol\": \"194539\",\r\n            \"cntg_vol\": \"8109\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"092600\",\r\n            \"bstp_nmix_prpr\": \"911.91\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.41\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.71\",\r\n            \"acml_tr_pbmn\": \"2312684\",\r\n            \"acml_vol\": \"186430\",\r\n            \"cntg_vol\": \"8233\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"092400\",\r\n            \"bstp_nmix_prpr\": \"912.18\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.68\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.74\",\r\n            \"acml_tr_pbmn\": \"2210228\",\r\n            \"acml_vol\": \"178197\",\r\n            \"cntg_vol\": \"8295\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"092200\",\r\n            \"bstp_nmix_prpr\": \"912.13\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.63\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.73\",\r\n            \"acml_tr_pbmn\": \"2106912\",\r\n            \"acml_vol\": \"169902\",\r\n            \"cntg_vol\": \"9285\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"092000\",\r\n            \"bstp_nmix_prpr\": \"910.92\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.42\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.60\",\r\n            \"acml_tr_pbmn\": \"1980631\",\r\n            \"acml_vol\": \"160617\",\r\n            \"cntg_vol\": \"10198\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"091800\",\r\n            \"bstp_nmix_prpr\": \"910.87\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.59\",\r\n            \"acml_tr_pbmn\": \"1836549\",\r\n            \"acml_vol\": \"150419\",\r\n            \"cntg_vol\": \"10738\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"091600\",\r\n            \"bstp_nmix_prpr\": \"910.99\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.49\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.61\",\r\n            \"acml_tr_pbmn\": \"1700334\",\r\n            \"acml_vol\": \"139681\",\r\n            \"cntg_vol\": \"11517\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"091400\",\r\n            \"bstp_nmix_prpr\": \"909.83\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.33\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.48\",\r\n            \"acml_tr_pbmn\": \"1572262\",\r\n            \"acml_vol\": \"128164\",\r\n            \"cntg_vol\": \"12918\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"091200\",\r\n            \"bstp_nmix_prpr\": \"909.84\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.48\",\r\n            \"acml_tr_pbmn\": \"1430578\",\r\n            \"acml_vol\": \"115246\",\r\n            \"cntg_vol\": \"12623\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"091000\",\r\n            \"bstp_nmix_prpr\": \"910.28\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.78\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.53\",\r\n            \"acml_tr_pbmn\": \"1296270\",\r\n            \"acml_vol\": \"102623\",\r\n            \"cntg_vol\": \"14403\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"090800\",\r\n            \"bstp_nmix_prpr\": \"909.65\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.15\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.46\",\r\n            \"acml_tr_pbmn\": \"1143581\",\r\n            \"acml_vol\": \"88220\",\r\n            \"cntg_vol\": \"11854\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"090600\",\r\n            \"bstp_nmix_prpr\": \"909.95\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.45\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.49\",\r\n            \"acml_tr_pbmn\": \"980294\",\r\n            \"acml_vol\": \"76366\",\r\n            \"cntg_vol\": \"12512\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"090400\",\r\n            \"bstp_nmix_prpr\": \"909.15\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.65\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.40\",\r\n            \"acml_tr_pbmn\": \"805755\",\r\n            \"acml_vol\": \"63854\",\r\n            \"cntg_vol\": \"14223\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"090200\",\r\n            \"bstp_nmix_prpr\": \"908.43\",\r\n            \"bstp_nmix_prdy_vrss\": \"2.93\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.32\",\r\n            \"acml_tr_pbmn\": \"606769\",\r\n            \"acml_vol\": \"49631\",\r\n            \"cntg_vol\": \"21310\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"090000\",\r\n            \"bstp_nmix_prpr\": \"910.96\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.46\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.60\",\r\n            \"acml_tr_pbmn\": \"347460\",\r\n            \"acml_vol\": \"28321\",\r\n            \"cntg_vol\": \"28321\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPUP02140000",
    "name": "국내업종 구분별전체시세",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-category-price",
    "sheet": "국내업종 구분별전체시세",
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
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
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
        "element": "down_issu_cnt",
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
        "element": "uplm_issu_cnt",
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
        "element": "prdy_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_lwpr_date",
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
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "acml_vol_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_tr_pbmn_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"U\",\r\n\"fid_input_iscd\":\"0001\",\r\n\"fid_cond_scr_div_code\":\"20214\",\r\n\"fid_mrkt_cls_code\":\"K2\",\r\n\"fid_blng_cls_code\":\"0\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"bstp_nmix_prpr\": \"2648.76\",\r\n        \"bstp_nmix_prdy_vrss\": \"34.96\",\r\n        \"prdy_vrss_sign\": \"2\",\r\n        \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n        \"acml_vol\": \"584715\",\r\n        \"acml_tr_pbmn\": \"10001487\",\r\n        \"bstp_nmix_oprc\": \"2635.63\",\r\n        \"bstp_nmix_hgpr\": \"2648.76\",\r\n        \"bstp_nmix_lwpr\": \"2625.01\",\r\n        \"prdy_vol\": \"621363\",\r\n        \"ascn_issu_cnt\": \"628\",\r\n        \"down_issu_cnt\": \"250\",\r\n        \"stnr_issu_cnt\": \"58\",\r\n        \"uplm_issu_cnt\": \"0\",\r\n        \"lslm_issu_cnt\": \"0\",\r\n        \"prdy_tr_pbmn\": \"10691024\",\r\n        \"dryy_bstp_nmix_hgpr_date\": \"20240102\",\r\n        \"dryy_bstp_nmix_hgpr\": \"2675.80\",\r\n        \"dryy_bstp_nmix_lwpr\": \"2429.12\",\r\n        \"dryy_bstp_nmix_lwpr_date\": \"20240118\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"bstp_cls_code\": \"2001\",\r\n            \"hts_kor_isnm\": \"KOSPI200\",\r\n            \"bstp_nmix_prpr\": \"355.52\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.31\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_vol\": \"118963\",\r\n            \"acml_tr_pbmn\": \"7078909\",\r\n            \"acml_vol_rlim\": \"100.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2007\",\r\n            \"hts_kor_isnm\": \"KOSPI100\",\r\n            \"bstp_nmix_prpr\": \"2691.34\",\r\n            \"bstp_nmix_prdy_vrss\": \"33.27\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_vol\": \"76784\",\r\n            \"acml_tr_pbmn\": \"6124444\",\r\n            \"acml_vol_rlim\": \"64.54\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2008\",\r\n            \"hts_kor_isnm\": \"KOSPI50\",\r\n            \"bstp_nmix_prpr\": \"2478.39\",\r\n            \"bstp_nmix_prdy_vrss\": \"28.83\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.18\",\r\n            \"acml_vol\": \"52269\",\r\n            \"acml_tr_pbmn\": \"5222300\",\r\n            \"acml_vol_rlim\": \"43.94\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2039\",\r\n            \"hts_kor_isnm\": \"K커뮤니케이션서비스\",\r\n            \"bstp_nmix_prpr\": \"1850.38\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.14\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.17\",\r\n            \"acml_vol\": \"5893\",\r\n            \"acml_tr_pbmn\": \"477398\",\r\n            \"acml_vol_rlim\": \"4.95\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2009\",\r\n            \"hts_kor_isnm\": \"K건설\",\r\n            \"bstp_nmix_prpr\": \"325.34\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.08\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.55\",\r\n            \"acml_vol\": \"6636\",\r\n            \"acml_tr_pbmn\": \"225841\",\r\n            \"acml_vol_rlim\": \"5.58\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2010\",\r\n            \"hts_kor_isnm\": \"K중공업\",\r\n            \"bstp_nmix_prpr\": \"322.92\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.05\",\r\n            \"acml_vol\": \"9613\",\r\n            \"acml_tr_pbmn\": \"203930\",\r\n            \"acml_vol_rlim\": \"8.08\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2011\",\r\n            \"hts_kor_isnm\": \"K철강소재\",\r\n            \"bstp_nmix_prpr\": \"884.98\",\r\n            \"bstp_nmix_prdy_vrss\": \"35.05\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"4.12\",\r\n            \"acml_vol\": \"4814\",\r\n            \"acml_tr_pbmn\": \"456186\",\r\n            \"acml_vol_rlim\": \"4.05\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2012\",\r\n            \"hts_kor_isnm\": \"K에너지화학\",\r\n            \"bstp_nmix_prpr\": \"1385.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"45.89\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"3.42\",\r\n            \"acml_vol\": \"7623\",\r\n            \"acml_tr_pbmn\": \"833756\",\r\n            \"acml_vol_rlim\": \"6.41\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2013\",\r\n            \"hts_kor_isnm\": \"K정보기술\",\r\n            \"bstp_nmix_prpr\": \"3233.61\",\r\n            \"bstp_nmix_prdy_vrss\": \"42.48\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.33\",\r\n            \"acml_vol\": \"20799\",\r\n            \"acml_tr_pbmn\": \"1899061\",\r\n            \"acml_vol_rlim\": \"17.48\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2014\",\r\n            \"hts_kor_isnm\": \"K금융\",\r\n            \"bstp_nmix_prpr\": \"780.59\",\r\n            \"bstp_nmix_prdy_vrss\": \"27.94\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"3.71\",\r\n            \"acml_vol\": \"23753\",\r\n            \"acml_tr_pbmn\": \"672909\",\r\n            \"acml_vol_rlim\": \"19.97\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2015\",\r\n            \"hts_kor_isnm\": \"K생활소비재\",\r\n            \"bstp_nmix_prpr\": \"793.68\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.81\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.64\",\r\n            \"acml_vol\": \"4244\",\r\n            \"acml_tr_pbmn\": \"288488\",\r\n            \"acml_vol_rlim\": \"3.57\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2016\",\r\n            \"hts_kor_isnm\": \"K경기소비재\",\r\n            \"bstp_nmix_prpr\": \"1724.67\",\r\n            \"bstp_nmix_prdy_vrss\": \"42.88\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.55\",\r\n            \"acml_vol\": \"10060\",\r\n            \"acml_tr_pbmn\": \"1004566\",\r\n            \"acml_vol_rlim\": \"8.46\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2017\",\r\n            \"hts_kor_isnm\": \"K산업재\",\r\n            \"bstp_nmix_prpr\": \"633.49\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.82\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.09\",\r\n            \"acml_vol\": \"23323\",\r\n            \"acml_tr_pbmn\": \"823914\",\r\n            \"acml_vol_rlim\": \"19.61\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2018\",\r\n            \"hts_kor_isnm\": \"K헬스케어\",\r\n            \"bstp_nmix_prpr\": \"1840.09\",\r\n            \"bstp_nmix_prdy_vrss\": \"14.36\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.79\",\r\n            \"acml_vol\": \"2204\",\r\n            \"acml_tr_pbmn\": \"192860\",\r\n            \"acml_vol_rlim\": \"1.85\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2019\",\r\n            \"hts_kor_isnm\": \"K고배당\",\r\n            \"bstp_nmix_prpr\": \"3173.16\",\r\n            \"bstp_nmix_prdy_vrss\": \"86.09\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.79\",\r\n            \"acml_vol\": \"41569\",\r\n            \"acml_tr_pbmn\": \"2859723\",\r\n            \"acml_vol_rlim\": \"34.94\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2021\",\r\n            \"hts_kor_isnm\": \"K200가치저변동성\",\r\n            \"bstp_nmix_prpr\": \"5446.64\",\r\n            \"bstp_nmix_prdy_vrss\": \"120.03\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.25\",\r\n            \"acml_vol\": \"86859\",\r\n            \"acml_tr_pbmn\": \"4469357\",\r\n            \"acml_vol_rlim\": \"73.01\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2022\",\r\n            \"hts_kor_isnm\": \"K200중소형주\",\r\n            \"bstp_nmix_prpr\": \"1221.07\",\r\n            \"bstp_nmix_prdy_vrss\": \"22.17\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.85\",\r\n            \"acml_vol\": \"42179\",\r\n            \"acml_tr_pbmn\": \"954465\",\r\n            \"acml_vol_rlim\": \"35.46\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2023\",\r\n            \"hts_kor_isnm\": \"K200경기방어소비재\",\r\n            \"bstp_nmix_prpr\": \"903.55\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.98\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.00\",\r\n            \"acml_vol\": \"8450\",\r\n            \"acml_tr_pbmn\": \"550010\",\r\n            \"acml_vol_rlim\": \"7.10\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2024\",\r\n            \"hts_kor_isnm\": \"K200에너지화학 레버리지\",\r\n            \"bstp_nmix_prpr\": \"836.53\",\r\n            \"bstp_nmix_prdy_vrss\": \"53.55\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"6.84\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2025\",\r\n            \"hts_kor_isnm\": \"K200정보기술 레버리지\",\r\n            \"bstp_nmix_prpr\": \"4350.42\",\r\n            \"bstp_nmix_prdy_vrss\": \"112.40\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.65\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2026\",\r\n            \"hts_kor_isnm\": \"K200금융 레버리지\",\r\n            \"bstp_nmix_prpr\": \"517.48\",\r\n            \"bstp_nmix_prdy_vrss\": \"35.72\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"7.41\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2027\",\r\n            \"hts_kor_isnm\": \"K200경기소비재 레버리지\",\r\n            \"bstp_nmix_prpr\": \"989.98\",\r\n            \"bstp_nmix_prdy_vrss\": \"47.94\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"5.09\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2035\",\r\n            \"hts_kor_isnm\": \"코스피200 TR\",\r\n            \"bstp_nmix_prpr\": \"449.66\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.45\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2036\",\r\n            \"hts_kor_isnm\": \"코스피200 NTR\",\r\n            \"bstp_nmix_prpr\": \"433.34\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.25\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2028\",\r\n            \"hts_kor_isnm\": \"K200건설 레버리지\",\r\n            \"bstp_nmix_prpr\": \"204.06\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.87\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"5.08\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2029\",\r\n            \"hts_kor_isnm\": \"K200중공업 레버리지\",\r\n            \"bstp_nmix_prpr\": \"169.43\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.48\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.10\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2030\",\r\n            \"hts_kor_isnm\": \"K200헬스케어 레버리지\",\r\n            \"bstp_nmix_prpr\": \"659.07\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.14\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.56\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2040\",\r\n            \"hts_kor_isnm\": \"코스피200 초대형 제외지수\",\r\n            \"bstp_nmix_prpr\": \"256.52\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.70\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.87\",\r\n            \"acml_vol\": \"105736\",\r\n            \"acml_tr_pbmn\": \"6115607\",\r\n            \"acml_vol_rlim\": \"88.88\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2037\",\r\n            \"hts_kor_isnm\": \"코스피200 예측 고배당 50\",\r\n            \"bstp_nmix_prpr\": \"1989.88\",\r\n            \"bstp_nmix_prdy_vrss\": \"49.77\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.57\",\r\n            \"acml_vol\": \"22491\",\r\n            \"acml_tr_pbmn\": \"1659649\",\r\n            \"acml_vol_rlim\": \"18.91\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2038\",\r\n            \"hts_kor_isnm\": \"코스피200 예측 배당성장 50\",\r\n            \"bstp_nmix_prpr\": \"1661.50\",\r\n            \"bstp_nmix_prdy_vrss\": \"33.18\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.04\",\r\n            \"acml_vol\": \"39463\",\r\n            \"acml_tr_pbmn\": \"2424471\",\r\n            \"acml_vol_rlim\": \"33.17\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2041\",\r\n            \"hts_kor_isnm\": \"K200 정보기술 TR\",\r\n            \"bstp_nmix_prpr\": \"3742.21\",\r\n            \"bstp_nmix_prdy_vrss\": \"49.16\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.33\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2042\",\r\n            \"hts_kor_isnm\": \"K200 금융 TR\",\r\n            \"bstp_nmix_prpr\": \"1192.40\",\r\n            \"bstp_nmix_prdy_vrss\": \"42.68\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"3.71\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2044\",\r\n            \"hts_kor_isnm\": \"K200 에너지화학 TR\",\r\n            \"bstp_nmix_prpr\": \"1786.68\",\r\n            \"bstp_nmix_prdy_vrss\": \"59.16\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"3.42\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2045\",\r\n            \"hts_kor_isnm\": \"K200 생활소비재 TR\",\r\n            \"bstp_nmix_prpr\": \"1031.76\",\r\n            \"bstp_nmix_prdy_vrss\": \"16.65\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.64\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2046\",\r\n            \"hts_kor_isnm\": \"K200 건설 TR\",\r\n            \"bstp_nmix_prpr\": \"386.22\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.59\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.55\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2047\",\r\n            \"hts_kor_isnm\": \"K200 중공업 TR\",\r\n            \"bstp_nmix_prpr\": \"356.92\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.72\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.05\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2048\",\r\n            \"hts_kor_isnm\": \"K200 철강소재 TR\",\r\n            \"bstp_nmix_prpr\": \"1172.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"46.45\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"4.12\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2049\",\r\n            \"hts_kor_isnm\": \"K200 산업재 TR\",\r\n            \"bstp_nmix_prpr\": \"753.63\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.11\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.09\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2050\",\r\n            \"hts_kor_isnm\": \"K200 헬스케어 TR\",\r\n            \"bstp_nmix_prpr\": \"1966.27\",\r\n            \"bstp_nmix_prdy_vrss\": \"15.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.79\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2051\",\r\n            \"hts_kor_isnm\": \"K200 커뮤니케이션서비스 TR\",\r\n            \"bstp_nmix_prpr\": \"2355.58\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.00\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.17\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2224\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 30%\",\r\n            \"bstp_nmix_prpr\": \"355.08\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_vol\": \"118963\",\r\n            \"acml_tr_pbmn\": \"7078909\",\r\n            \"acml_vol_rlim\": \"100.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2225\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 30%  TR\",\r\n            \"bstp_nmix_prpr\": \"449.00\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.53\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2226\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 30%  NTR\",\r\n            \"bstp_nmix_prpr\": \"432.91\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.33\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2227\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 25%\",\r\n            \"bstp_nmix_prpr\": \"351.32\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.69\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.35\",\r\n            \"acml_vol\": \"118963\",\r\n            \"acml_tr_pbmn\": \"7078909\",\r\n            \"acml_vol_rlim\": \"100.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2228\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 25%  TR\",\r\n            \"bstp_nmix_prpr\": \"444.32\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.93\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.35\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2230\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 25%  NTR\",\r\n            \"bstp_nmix_prpr\": \"428.34\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.72\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.35\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2232\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 20%\",\r\n            \"bstp_nmix_prpr\": \"341.02\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.89\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.45\",\r\n            \"acml_vol\": \"118963\",\r\n            \"acml_tr_pbmn\": \"7078909\",\r\n            \"acml_vol_rlim\": \"100.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2233\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 20%  TR\",\r\n            \"bstp_nmix_prpr\": \"430.39\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.17\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.45\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2235\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 20%  NTR\",\r\n            \"bstp_nmix_prpr\": \"415.42\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.96\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.46\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2043\",\r\n            \"hts_kor_isnm\": \"K200 경기소비재 TR\",\r\n            \"bstp_nmix_prpr\": \"2152.99\",\r\n            \"bstp_nmix_prdy_vrss\": \"53.53\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.55\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2284\",\r\n            \"hts_kor_isnm\": \"코스피 200 선물지수 TWAP형\",\r\n            \"bstp_nmix_prpr\": \"1786.47\",\r\n            \"bstp_nmix_prdy_vrss\": \"18.33\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.04\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2285\",\r\n            \"hts_kor_isnm\": \"코스피 200 선물 TWAP 인버스지수\",\r\n            \"bstp_nmix_prpr\": \"2555.41\",\r\n            \"bstp_nmix_prdy_vrss\": \"-26.53\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.03\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2286\",\r\n            \"hts_kor_isnm\": \"코스피 200 선물 TWAP 레버리지\",\r\n            \"bstp_nmix_prpr\": \"1448.92\",\r\n            \"bstp_nmix_prdy_vrss\": \"29.55\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.08\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2287\",\r\n            \"hts_kor_isnm\": \"코스피 200 선물 TWAP 인버스-2X\",\r\n            \"bstp_nmix_prpr\": \"2598.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"-54.80\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-2.07\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2751\",\r\n            \"hts_kor_isnm\": \"F-K200 에너지/화학\",\r\n            \"bstp_nmix_prpr\": \"1201.20\",\r\n            \"bstp_nmix_prdy_vrss\": \"34.48\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.96\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2752\",\r\n            \"hts_kor_isnm\": \"F-K200 정보기술\",\r\n            \"bstp_nmix_prpr\": \"2051.35\",\r\n            \"bstp_nmix_prdy_vrss\": \"18.30\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.90\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2753\",\r\n            \"hts_kor_isnm\": \"F-K200 금융\",\r\n            \"bstp_nmix_prpr\": \"1291.69\",\r\n            \"bstp_nmix_prdy_vrss\": \"40.86\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"3.27\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2754\",\r\n            \"hts_kor_isnm\": \"F-K200 경기소비재\",\r\n            \"bstp_nmix_prpr\": \"1121.37\",\r\n            \"bstp_nmix_prdy_vrss\": \"17.42\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.58\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2755\",\r\n            \"hts_kor_isnm\": \"F-K200 건설\",\r\n            \"bstp_nmix_prpr\": \"1218.34\",\r\n            \"bstp_nmix_prdy_vrss\": \"25.51\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.14\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2756\",\r\n            \"hts_kor_isnm\": \"F-K200 중공업\",\r\n            \"bstp_nmix_prpr\": \"962.17\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.96\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.94\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2757\",\r\n            \"hts_kor_isnm\": \"F-K200 헬스케어\",\r\n            \"bstp_nmix_prpr\": \"963.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"2.84\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.30\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2758\",\r\n            \"hts_kor_isnm\": \"F-K200 생활소비재\",\r\n            \"bstp_nmix_prpr\": \"637.56\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.77\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.28\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2759\",\r\n            \"hts_kor_isnm\": \"F-K200 철강/소재\",\r\n            \"bstp_nmix_prpr\": \"903.55\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.00\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.00\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2760\",\r\n            \"hts_kor_isnm\": \"F-K200 산업재\",\r\n            \"bstp_nmix_prpr\": \"1031.59\",\r\n            \"bstp_nmix_prdy_vrss\": \"7.80\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.76\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2761\",\r\n            \"hts_kor_isnm\": \"F-K200 에너지/화학  레버리지\",\r\n            \"bstp_nmix_prpr\": \"1039.81\",\r\n            \"bstp_nmix_prdy_vrss\": \"58.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"5.92\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2762\",\r\n            \"hts_kor_isnm\": \"F-K200 정보기술  레버리지\",\r\n            \"bstp_nmix_prpr\": \"3228.56\",\r\n            \"bstp_nmix_prdy_vrss\": \"57.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.81\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2763\",\r\n            \"hts_kor_isnm\": \"F-K200 금융  레버리지\",\r\n            \"bstp_nmix_prpr\": \"1311.74\",\r\n            \"bstp_nmix_prdy_vrss\": \"80.53\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"6.54\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2764\",\r\n            \"hts_kor_isnm\": \"F-K200 경기소비재  레버리지\",\r\n            \"bstp_nmix_prpr\": \"1001.75\",\r\n            \"bstp_nmix_prdy_vrss\": \"30.72\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"3.16\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2765\",\r\n            \"hts_kor_isnm\": \"F-K200 건설  레버리지\",\r\n            \"bstp_nmix_prpr\": \"976.07\",\r\n            \"bstp_nmix_prdy_vrss\": \"40.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"4.28\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2766\",\r\n            \"hts_kor_isnm\": \"F-K200 중공업  레버리지\",\r\n            \"bstp_nmix_prpr\": \"532.58\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.86\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.89\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2767\",\r\n            \"hts_kor_isnm\": \"F-K200 헬스케어  레버리지\",\r\n            \"bstp_nmix_prpr\": \"610.89\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.63\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.60\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2768\",\r\n            \"hts_kor_isnm\": \"F-K200 생활소비재  레버리지\",\r\n            \"bstp_nmix_prpr\": \"376.44\",\r\n            \"bstp_nmix_prdy_vrss\": \"2.12\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.57\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2769\",\r\n            \"hts_kor_isnm\": \"F-K200 철강/소재  레버리지\",\r\n            \"bstp_nmix_prpr\": \"546.02\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.04\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.01\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2770\",\r\n            \"hts_kor_isnm\": \"F-K200 산업재  레버리지\",\r\n            \"bstp_nmix_prpr\": \"868.46\",\r\n            \"bstp_nmix_prdy_vrss\": \"13.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.53\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2771\",\r\n            \"hts_kor_isnm\": \"F-K200 에너지/화학  인버스\",\r\n            \"bstp_nmix_prpr\": \"607.50\",\r\n            \"bstp_nmix_prdy_vrss\": \"-18.44\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-2.95\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2772\",\r\n            \"hts_kor_isnm\": \"F-K200 정보기술  인버스\",\r\n            \"bstp_nmix_prpr\": \"379.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"-3.41\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.89\",\r\n            \"acml_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"0\",\r\n            \"acml_vol_rlim\": \"0.00\",\r\n            \"acml_tr_pbmn_rlim\": \"\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2773\",\r\n            \"hts_kor_isnm\": \"F-K200 금융  인버스\",\r\n            \"bstp_nmix_prpr\": \"615.73\",\r\n            \"bstp_nmix_prdy_vrss\": \"-20.73\",",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKUP03500200",
    "name": "업종 분봉조회",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-time-indexchartprice",
    "sheet": "업종 분봉조회",
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
        "element": "Output1",
        "type": "object array",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_nmix",
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
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "futs_prdy_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "futs_prdy_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "futs_prdy_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "Output2",
        "type": "object",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cntg_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
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
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"FID_COND_MRKT_DIV_CODE\":\"U\",\r\n\"FID_INPUT_ISCD\":\"1001\",\r\n\"FID_INPUT_HOUR_1\":\"120\",\r\n\"FID_PW_DATA_INCU_YN\":\"Y\",\r\n\"FID_ETC_CLS_CODE\":\"0\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"bstp_nmix_prdy_vrss\": \"-3.68\",\r\n        \"prdy_vrss_sign\": \"5\",\r\n        \"bstp_nmix_prdy_ctrt\": \"-0.44\",\r\n        \"prdy_nmix\": \"837.24\",\r\n        \"acml_vol\": \"554702\",\r\n        \"acml_tr_pbmn\": \"5740155\",\r\n        \"hts_kor_isnm\": \"KOSDAQ\",\r\n        \"bstp_nmix_prpr\": \"833.56\",\r\n        \"bstp_cls_code\": \"1001\",\r\n        \"prdy_vol\": \"1238780\",\r\n        \"bstp_nmix_oprc\": \"841.21\",\r\n        \"bstp_nmix_hgpr\": \"841.21\",\r\n        \"bstp_nmix_lwpr\": \"830.09\",\r\n        \"futs_prdy_oprc\": \"818.76\",\r\n        \"futs_prdy_hgpr\": \"839.52\",\r\n        \"futs_prdy_lwpr\": \"817.06\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"103200\",\r\n            \"bstp_nmix_prpr\": \"833.56\",\r\n            \"bstp_nmix_oprc\": \"834.07\",\r\n            \"bstp_nmix_hgpr\": \"834.07\",\r\n            \"bstp_nmix_lwpr\": \"833.56\",\r\n            \"cntg_vol\": \"4618\",\r\n            \"acml_tr_pbmn\": \"5740155\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"103000\",\r\n            \"bstp_nmix_prpr\": \"833.99\",\r\n            \"bstp_nmix_oprc\": \"834.29\",\r\n            \"bstp_nmix_hgpr\": \"834.29\",\r\n            \"bstp_nmix_lwpr\": \"833.89\",\r\n            \"cntg_vol\": \"4601\",\r\n            \"acml_tr_pbmn\": \"5689290\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"102800\",\r\n            \"bstp_nmix_prpr\": \"834.24\",\r\n            \"bstp_nmix_oprc\": \"833.47\",\r\n            \"bstp_nmix_hgpr\": \"834.32\",\r\n            \"bstp_nmix_lwpr\": \"833.44\",\r\n            \"cntg_vol\": \"4978\",\r\n            \"acml_tr_pbmn\": \"5635506\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"102600\",\r\n            \"bstp_nmix_prpr\": \"833.46\",\r\n            \"bstp_nmix_oprc\": \"832.36\",\r\n            \"bstp_nmix_hgpr\": \"833.46\",\r\n            \"bstp_nmix_lwpr\": \"832.36\",\r\n            \"cntg_vol\": \"5033\",\r\n            \"acml_tr_pbmn\": \"5581000\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"102400\",\r\n            \"bstp_nmix_prpr\": \"832.48\",\r\n            \"bstp_nmix_oprc\": \"832.92\",\r\n            \"bstp_nmix_hgpr\": \"832.92\",\r\n            \"bstp_nmix_lwpr\": \"832.47\",\r\n            \"cntg_vol\": \"5239\",\r\n            \"acml_tr_pbmn\": \"5518332\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"102200\",\r\n            \"bstp_nmix_prpr\": \"832.85\",\r\n            \"bstp_nmix_oprc\": \"832.77\",\r\n            \"bstp_nmix_hgpr\": \"832.87\",\r\n            \"bstp_nmix_lwpr\": \"832.69\",\r\n            \"cntg_vol\": \"6042\",\r\n            \"acml_tr_pbmn\": \"5455651\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"102000\",\r\n            \"bstp_nmix_prpr\": \"832.74\",\r\n            \"bstp_nmix_oprc\": \"832.55\",\r\n            \"bstp_nmix_hgpr\": \"833.25\",\r\n            \"bstp_nmix_lwpr\": \"832.55\",\r\n            \"cntg_vol\": \"6301\",\r\n            \"acml_tr_pbmn\": \"5372736\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"101800\",\r\n            \"bstp_nmix_prpr\": \"832.83\",\r\n            \"bstp_nmix_oprc\": \"832.51\",\r\n            \"bstp_nmix_hgpr\": \"832.83\",\r\n            \"bstp_nmix_lwpr\": \"832.22\",\r\n            \"cntg_vol\": \"5676\",\r\n            \"acml_tr_pbmn\": \"5284172\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"101600\",\r\n            \"bstp_nmix_prpr\": \"832.50\",\r\n            \"bstp_nmix_oprc\": \"832.27\",\r\n            \"bstp_nmix_hgpr\": \"832.62\",\r\n            \"bstp_nmix_lwpr\": \"832.09\",\r\n            \"cntg_vol\": \"4771\",\r\n            \"acml_tr_pbmn\": \"5219827\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"101400\",\r\n            \"bstp_nmix_prpr\": \"832.44\",\r\n            \"bstp_nmix_oprc\": \"832.03\",\r\n            \"bstp_nmix_hgpr\": \"832.52\",\r\n            \"bstp_nmix_lwpr\": \"832.03\",\r\n            \"cntg_vol\": \"6639\",\r\n            \"acml_tr_pbmn\": \"5167005\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"101200\",\r\n            \"bstp_nmix_prpr\": \"832.11\",\r\n            \"bstp_nmix_oprc\": \"831.98\",\r\n            \"bstp_nmix_hgpr\": \"832.24\",\r\n            \"bstp_nmix_lwpr\": \"831.75\",\r\n            \"cntg_vol\": \"6946\",\r\n            \"acml_tr_pbmn\": \"5093186\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"101000\",\r\n            \"bstp_nmix_prpr\": \"832.23\",\r\n            \"bstp_nmix_oprc\": \"831.36\",\r\n            \"bstp_nmix_hgpr\": \"832.23\",\r\n            \"bstp_nmix_lwpr\": \"831.35\",\r\n            \"cntg_vol\": \"6579\",\r\n            \"acml_tr_pbmn\": \"5011060\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"100800\",\r\n            \"bstp_nmix_prpr\": \"831.22\",\r\n            \"bstp_nmix_oprc\": \"831.05\",\r\n            \"bstp_nmix_hgpr\": \"831.22\",\r\n            \"bstp_nmix_lwpr\": \"830.55\",\r\n            \"cntg_vol\": \"6837\",\r\n            \"acml_tr_pbmn\": \"4928657\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"100600\",\r\n            \"bstp_nmix_prpr\": \"830.98\",\r\n            \"bstp_nmix_oprc\": \"831.46\",\r\n            \"bstp_nmix_hgpr\": \"831.54\",\r\n            \"bstp_nmix_lwpr\": \"830.98\",\r\n            \"cntg_vol\": \"6694\",\r\n            \"acml_tr_pbmn\": \"4854815\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"100400\",\r\n            \"bstp_nmix_prpr\": \"831.76\",\r\n            \"bstp_nmix_oprc\": \"830.79\",\r\n            \"bstp_nmix_hgpr\": \"831.76\",\r\n            \"bstp_nmix_lwpr\": \"830.79\",\r\n            \"cntg_vol\": \"6839\",\r\n            \"acml_tr_pbmn\": \"4781557\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"100200\",\r\n            \"bstp_nmix_prpr\": \"830.92\",\r\n            \"bstp_nmix_oprc\": \"831.17\",\r\n            \"bstp_nmix_hgpr\": \"831.21\",\r\n            \"bstp_nmix_lwpr\": \"830.71\",\r\n            \"cntg_vol\": \"9589\",\r\n            \"acml_tr_pbmn\": \"4724555\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"100000\",\r\n            \"bstp_nmix_prpr\": \"831.14\",\r\n            \"bstp_nmix_oprc\": \"831.32\",\r\n            \"bstp_nmix_hgpr\": \"831.52\",\r\n            \"bstp_nmix_lwpr\": \"830.90\",\r\n            \"cntg_vol\": \"8688\",\r\n            \"acml_tr_pbmn\": \"4652376\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"095800\",\r\n            \"bstp_nmix_prpr\": \"831.56\",\r\n            \"bstp_nmix_oprc\": \"831.32\",\r\n            \"bstp_nmix_hgpr\": \"831.76\",\r\n            \"bstp_nmix_lwpr\": \"831.32\",\r\n            \"cntg_vol\": \"6519\",\r\n            \"acml_tr_pbmn\": \"4568901\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"095600\",\r\n            \"bstp_nmix_prpr\": \"831.43\",\r\n            \"bstp_nmix_oprc\": \"830.68\",\r\n            \"bstp_nmix_hgpr\": \"831.43\",\r\n            \"bstp_nmix_lwpr\": \"830.52\",\r\n            \"cntg_vol\": \"7474\",\r\n            \"acml_tr_pbmn\": \"4497224\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"095400\",\r\n            \"bstp_nmix_prpr\": \"830.50\",\r\n            \"bstp_nmix_oprc\": \"831.46\",\r\n            \"bstp_nmix_hgpr\": \"831.46\",\r\n            \"bstp_nmix_lwpr\": \"830.50\",\r\n            \"cntg_vol\": \"9190\",\r\n            \"acml_tr_pbmn\": \"4423313\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"095200\",\r\n            \"bstp_nmix_prpr\": \"831.57\",\r\n            \"bstp_nmix_oprc\": \"831.45\",\r\n            \"bstp_nmix_hgpr\": \"831.59\",\r\n            \"bstp_nmix_lwpr\": \"831.38\",\r\n            \"cntg_vol\": \"7701\",\r\n            \"acml_tr_pbmn\": \"4324541\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"095000\",\r\n            \"bstp_nmix_prpr\": \"831.60\",\r\n            \"bstp_nmix_oprc\": \"831.45\",\r\n            \"bstp_nmix_hgpr\": \"831.82\",\r\n            \"bstp_nmix_lwpr\": \"831.39\",\r\n            \"cntg_vol\": \"7529\",\r\n            \"acml_tr_pbmn\": \"4247753\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"094800\",\r\n            \"bstp_nmix_prpr\": \"831.57\",\r\n            \"bstp_nmix_oprc\": \"831.71\",\r\n            \"bstp_nmix_hgpr\": \"831.76\",\r\n            \"bstp_nmix_lwpr\": \"831.47\",\r\n            \"cntg_vol\": \"7754\",\r\n            \"acml_tr_pbmn\": \"4165554\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"094600\",\r\n            \"bstp_nmix_prpr\": \"831.77\",\r\n            \"bstp_nmix_oprc\": \"830.50\",\r\n            \"bstp_nmix_hgpr\": \"831.91\",\r\n            \"bstp_nmix_lwpr\": \"830.44\",\r\n            \"cntg_vol\": \"9213\",\r\n            \"acml_tr_pbmn\": \"4076635\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"094400\",\r\n            \"bstp_nmix_prpr\": \"830.26\",\r\n            \"bstp_nmix_oprc\": \"830.57\",\r\n            \"bstp_nmix_hgpr\": \"830.67\",\r\n            \"bstp_nmix_lwpr\": \"830.09\",\r\n            \"cntg_vol\": \"7201\",\r\n            \"acml_tr_pbmn\": \"3971601\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"094200\",\r\n            \"bstp_nmix_prpr\": \"830.53\",\r\n            \"bstp_nmix_oprc\": \"831.03\",\r\n            \"bstp_nmix_hgpr\": \"831.21\",\r\n            \"bstp_nmix_lwpr\": \"830.48\",\r\n            \"cntg_vol\": \"7992\",\r\n            \"acml_tr_pbmn\": \"3886154\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"094000\",\r\n            \"bstp_nmix_prpr\": \"830.98\",\r\n            \"bstp_nmix_oprc\": \"831.26\",\r\n            \"bstp_nmix_hgpr\": \"831.26\",\r\n            \"bstp_nmix_lwpr\": \"830.32\",\r\n            \"cntg_vol\": \"9912\",\r\n            \"acml_tr_pbmn\": \"3790733\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"093800\",\r\n            \"bstp_nmix_prpr\": \"831.32\",\r\n            \"bstp_nmix_oprc\": \"832.07\",\r\n            \"bstp_nmix_hgpr\": \"832.07\",\r\n            \"bstp_nmix_lwpr\": \"831.27\",\r\n            \"cntg_vol\": \"9575\",\r\n            \"acml_tr_pbmn\": \"3663618\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"093600\",\r\n            \"bstp_nmix_prpr\": \"832.24\",\r\n            \"bstp_nmix_oprc\": \"831.34\",\r\n            \"bstp_nmix_hgpr\": \"832.30\",\r\n            \"bstp_nmix_lwpr\": \"831.34\",\r\n            \"cntg_vol\": \"10164\",\r\n            \"acml_tr_pbmn\": \"3561037\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"093400\",\r\n            \"bstp_nmix_prpr\": \"831.44\",\r\n            \"bstp_nmix_oprc\": \"832.64\",\r\n            \"bstp_nmix_hgpr\": \"832.64\",\r\n            \"bstp_nmix_lwpr\": \"831.44\",\r\n            \"cntg_vol\": \"11415\",\r\n            \"acml_tr_pbmn\": \"3447235\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"093200\",\r\n            \"bstp_nmix_prpr\": \"832.53\",\r\n            \"bstp_nmix_oprc\": \"833.45\",\r\n            \"bstp_nmix_hgpr\": \"833.66\",\r\n            \"bstp_nmix_lwpr\": \"832.53\",\r\n            \"cntg_vol\": \"11522\",\r\n            \"acml_tr_pbmn\": \"3316543\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"093000\",\r\n            \"bstp_nmix_prpr\": \"833.58\",\r\n            \"bstp_nmix_oprc\": \"833.59\",\r\n            \"bstp_nmix_hgpr\": \"834.05\",\r\n            \"bstp_nmix_lwpr\": \"833.36\",\r\n            \"cntg_vol\": \"11105\",\r\n            \"acml_tr_pbmn\": \"3203362\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"092800\",\r\n            \"bstp_nmix_prpr\": \"833.97\",\r\n            \"bstp_nmix_oprc\": \"832.91\",\r\n            \"bstp_nmix_hgpr\": \"833.97\",\r\n            \"bstp_nmix_lwpr\": \"832.36\",\r\n            \"cntg_vol\": \"15502\",\r\n            \"acml_tr_pbmn\": \"3071005\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"092600\",\r\n            \"bstp_nmix_prpr\": \"833.08\",\r\n            \"bstp_nmix_oprc\": \"835.04\",\r\n            \"bstp_nmix_hgpr\": \"835.04\",\r\n            \"bstp_nmix_lwpr\": \"833.00\",\r\n            \"cntg_vol\": \"15656\",\r\n            \"acml_tr_pbmn\": \"2928429\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"092400\",\r\n            \"bstp_nmix_prpr\": \"834.63\",\r\n            \"bstp_nmix_oprc\": \"833.51\",\r\n            \"bstp_nmix_hgpr\": \"834.98\",\r\n            \"bstp_nmix_lwpr\": \"833.51\",\r\n            \"cntg_vol\": \"16851\",\r\n            \"acml_tr_pbmn\": \"2747155\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"092200\",\r\n            \"bstp_nmix_prpr\": \"833.45\",\r\n            \"bstp_nmix_oprc\": \"835.50\",\r\n            \"bstp_nmix_hgpr\": \"835.50\",\r\n            \"bstp_nmix_lwpr\": \"833.45\",\r\n            \"cntg_vol\": \"16696\",\r\n            \"acml_tr_pbmn\": \"2583365\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"092000\",\r\n            \"bstp_nmix_prpr\": \"835.91\",\r\n            \"bstp_nmix_oprc\": \"835.96\",\r\n            \"bstp_nmix_hgpr\": \"836.14\",\r\n            \"bstp_nmix_lwpr\": \"835.76\",\r\n            \"cntg_vol\": \"16008\",\r\n            \"acml_tr_pbmn\": \"2424467\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"091800\",\r\n            \"bstp_nmix_prpr\": \"836.05\",\r\n            \"bstp_nmix_oprc\": \"838.39\",\r\n            \"bstp_nmix_hgpr\": \"838.39\",\r\n            \"bstp_nmix_lwpr\": \"835.98\",\r\n            \"cntg_vol\": \"16778\",\r\n            \"acml_tr_pbmn\": \"2260216\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"091600\",\r\n            \"bstp_nmix_prpr\": \"838.24\",\r\n            \"bstp_nmix_oprc\": \"837.19\",\r\n            \"bstp_nmix_hgpr\": \"838.70\",\r\n            \"bstp_nmix_lwpr\": \"837.19\",\r\n            \"cntg_vol\": \"17379\",\r\n            \"acml_tr_pbmn\": \"2098721\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"091400\",\r\n            \"bstp_nmix_prpr\": \"836.82\",\r\n            \"bstp_nmix_oprc\": \"836.88\",\r\n            \"bstp_nmix_hgpr\": \"837.94\",\r\n            \"bstp_nmix_lwpr\": \"836.48\",\r\n            \"cntg_vol\": \"19020\",\r\n            \"acml_tr_pbmn\": \"1934637\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"091200\",\r\n            \"bstp_nmix_prpr\": \"836.73\",\r\n            \"bstp_nmix_oprc\": \"837.87\",\r\n            \"bstp_nmix_hgpr\": \"838.34\",\r\n            \"bstp_nmix_lwpr\": \"836.73\",\r\n            \"cntg_vol\": \"27881\",\r\n            \"acml_tr_pbmn\": \"1781817\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"091000\",\r\n            \"bstp_nmix_prpr\": \"837.70\",\r\n            \"bstp_nmix_oprc\": \"837.68\",\r\n            \"bstp_nmix_hgpr\": \"837.72\",\r\n            \"bstp_nmix_lwpr\": \"837.38\",\r\n            \"cntg_vol\": \"16983\",\r\n            \"acml_tr_pbmn\": \"1606668\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"090800\",\r\n            \"bstp_nmix_prpr\": \"837.87\",\r\n            \"bstp_nmix_oprc\": \"840.59\",\r\n            \"bstp_nmix_hgpr\": \"840.59\",\r\n            \"bstp_nmix_lwpr\": \"837.87\",\r\n            \"cntg_vol\": \"21991\",\r\n            \"acml_tr_pbmn\": \"1441148\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"090600\",\r\n            \"bstp_nmix_prpr\": \"840.98\",\r\n            \"bstp_nmix_oprc\": \"839.46\",\r\n            \"bstp_nmix_hgpr\": \"841.17\",\r\n            \"bstp_nmix_lwpr\": \"839.46\",\r\n            \"cntg_vol\": \"20366\",\r\n            \"acml_tr_pbmn\": \"1234692\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"090400\",\r\n            \"bstp_nmix_prpr\": \"839.42\",\r\n            \"bstp_nmix_oprc\": \"836.70\",\r\n            \"bstp_nmix_hgpr\": \"839.42\",\r\n            \"bstp_nmix_lwpr\": \"836.70\",\r\n            \"cntg_vol\": \"27395\",\r\n            \"acml_tr_pbmn\": \"1007681\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"090200\",\r\n            \"bstp_nmix_prpr\": \"836.69\",\r\n            \"bstp_nmix_oprc\": \"838.54\",\r\n            \"bstp_nmix_hgpr\": \"838.54\",\r\n            \"bstp_nmix_lwpr\": \"835.19\",\r\n            \"cntg_vol\": \"31941\",\r\n            \"acml_tr_pbmn\": \"754939\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240129\",\r\n            \"stck_cntg_hour\": \"090000\",\r\n            \"bstp_nmix_prpr\": \"838.62\",\r\n            \"bstp_nmix_oprc\": \"841.21\",\r\n            \"bstp_nmix_hgpr\": \"841.21\",\r\n            \"bstp_nmix_lwpr\": \"838.42\",\r\n            \"cntg_vol\": \"33919\",\r\n            \"acml_tr_pbmn\": \"422108\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"999999\",\r\n            \"bstp_nmix_prpr\": \"837.24\",\r\n            \"bstp_nmix_oprc\": \"837.24\",\r\n            \"bstp_nmix_hgpr\": \"837.24\",\r\n            \"bstp_nmix_lwpr\": \"837.24\",\r\n            \"cntg_vol\": \"21566\",\r\n            \"acml_tr_pbmn\": \"11242548\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"888888\",\r\n            \"bstp_nmix_prpr\": \"837.24\",\r\n            \"bstp_nmix_oprc\": \"837.24\",\r\n            \"bstp_nmix_hgpr\": \"837.24\",\r\n            \"bstp_nmix_lwpr\": \"837.24\",\r\n            \"cntg_vol\": \"42\",\r\n            \"acml_tr_pbmn\": \"11058431\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"153200\",\r\n            \"bstp_nmix_prpr\": \"837.20\",\r\n            \"bstp_nmix_oprc\": \"837.19\",\r\n            \"bstp_nmix_hgpr\": \"837.20\",\r\n            \"bstp_nmix_lwpr\": \"837.19\",\r\n            \"cntg_vol\": \"126\",\r\n            \"acml_tr_pbmn\": \"11057509\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"153000\",\r\n            \"bstp_nmix_prpr\": \"837.19\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"837.25\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"17043\",\r\n            \"acml_tr_pbmn\": \"11056788\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"152800\",\r\n            \"bstp_nmix_prpr\": \"836.97\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"836.97\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"10792443\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"152600\",\r\n            \"bstp_nmix_prpr\": \"836.97\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"836.97\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"10792443\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"152400\",\r\n            \"bstp_nmix_prpr\": \"836.97\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"836.97\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"10792443\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"152200\",\r\n            \"bstp_nmix_prpr\": \"836.97\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"836.97\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"0\",\r\n            \"acml_tr_pbmn\": \"10792443\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"152000\",\r\n            \"bstp_nmix_prpr\": \"836.97\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"836.97\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"1000\",\r\n            \"acml_tr_pbmn\": \"10792443\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"151800\",\r\n            \"bstp_nmix_prpr\": \"837.01\",\r\n            \"bstp_nmix_oprc\": \"836.79\",\r\n            \"bstp_nmix_hgpr\": \"837.05\",\r\n            \"bstp_nmix_lwpr\": \"836.49\",\r\n            \"cntg_vol\": \"8328\",\r\n            \"acml_tr_pbmn\": \"10784186\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"151600\",\r\n            \"bstp_nmix_prpr\": \"836.90\",\r\n            \"bstp_nmix_oprc\": \"836.72\",\r\n            \"bstp_nmix_hgpr\": \"836.93\",\r\n            \"bstp_nmix_lwpr\": \"836.64\",\r\n            \"cntg_vol\": \"6227\",\r\n            \"acml_tr_pbmn\": \"10699895\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"151400\",\r\n            \"bstp_nmix_prpr\": \"836.86\",\r\n            \"bstp_nmix_oprc\": \"836.63\",\r\n            \"bstp_nmix_hgpr\": \"836.96\",\r\n            \"bstp_nmix_lwpr\": \"836.57\",\r\n            \"cntg_vol\": \"5728\",\r\n            \"acml_tr_pbmn\": \"10633883\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"151200\",\r\n            \"bstp_nmix_prpr\": \"836.70\",\r\n            \"bstp_nmix_oprc\": \"836.71\",\r\n            \"bstp_nmix_hgpr\": \"836.84\",\r\n            \"bstp_nmix_lwpr\": \"836.44\",\r\n            \"cntg_vol\": \"6163\",\r\n            \"acml_tr_pbmn\": \"10578452\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"151000\",\r\n            \"bstp_nmix_prpr\": \"836.83\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"836.98\",\r\n            \"bstp_nmix_lwpr\": \"836.69\",\r\n            \"cntg_vol\": \"4617\",\r\n            \"acml_tr_pbmn\": \"10523064\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"150800\",\r\n            \"bstp_nmix_prpr\": \"836.92\",\r\n            \"bstp_nmix_oprc\": \"836.97\",\r\n            \"bstp_nmix_hgpr\": \"837.02\",\r\n            \"bstp_nmix_lwpr\": \"836.70\",\r\n            \"cntg_vol\": \"4728\",\r\n            \"acml_tr_pbmn\": \"10472083\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"150600\",\r\n            \"bstp_nmix_prpr\": \"836.97\",\r\n            \"bstp_nmix_oprc\": \"836.70\",\r\n            \"bstp_nmix_hgpr\": \"837.06\",\r\n            \"bstp_nmix_lwpr\": \"836.70\",\r\n            \"cntg_vol\": \"4719\",\r\n            \"acml_tr_pbmn\": \"10420811\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"150400\",\r\n            \"bstp_nmix_prpr\": \"836.66\",\r\n            \"bstp_nmix_oprc\": \"836.19\",\r\n            \"bstp_nmix_hgpr\": \"836.92\",\r\n            \"bstp_nmix_lwpr\": \"836.19\",\r\n            \"cntg_vol\": \"4377\",\r\n            \"acml_tr_pbmn\": \"10372366\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"150200\",\r\n            \"bstp_nmix_prpr\": \"836.29\",\r\n            \"bstp_nmix_oprc\": \"836.18\",\r\n            \"bstp_nmix_hgpr\": \"836.38\",\r\n            \"bstp_nmix_lwpr\": \"836.18\",\r\n            \"cntg_vol\": \"4261\",\r\n            \"acml_tr_pbmn\": \"10320188\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"150000\",\r\n            \"bstp_nmix_prpr\": \"836.28\",\r\n            \"bstp_nmix_oprc\": \"836.24\",\r\n            \"bstp_nmix_hgpr\": \"836.44\",\r\n            \"bstp_nmix_lwpr\": \"836.20\",\r\n            \"cntg_vol\": \"4420\",\r\n            \"acml_tr_pbmn\": \"10273218\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"145800\",\r\n            \"bstp_nmix_prpr\": \"836.43\",\r\n            \"bstp_nmix_oprc\": \"837.13\",\r\n            \"bstp_nmix_hgpr\": \"837.18\",\r\n            \"bstp_nmix_lwpr\": \"836.43\",\r\n            \"cntg_vol\": \"4215\",\r\n            \"acml_tr_pbmn\": \"10218137\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"145600\",\r\n            \"bstp_nmix_prpr\": \"837.23\",\r\n            \"bstp_nmix_oprc\": \"837.95\",\r\n            \"bstp_nmix_hgpr\": \"838.01\",\r\n            \"bstp_nmix_lwpr\": \"837.23\",\r\n            \"cntg_vol\": \"4978\",\r\n            \"acml_tr_pbmn\": \"10166106\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"145400\",\r\n            \"bstp_nmix_prpr\": \"837.89\",\r\n            \"bstp_nmix_oprc\": \"837.66\",\r\n            \"bstp_nmix_hgpr\": \"837.96\",\r\n            \"bstp_nmix_lwpr\": \"837.66\",\r\n            \"cntg_vol\": \"5102\",\r\n            \"acml_tr_pbmn\": \"10110923\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"145200\",\r\n            \"bstp_nmix_prpr\": \"837.66\",\r\n            \"bstp_nmix_oprc\": \"837.41\",\r\n            \"bstp_nmix_hgpr\": \"837.66\",\r\n            \"bstp_nmix_lwpr\": \"837.22\",\r\n            \"cntg_vol\": \"3840\",\r\n            \"acml_tr_pbmn\": \"10055054\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"145000\",\r\n            \"bstp_nmix_prpr\": \"837.58\",\r\n            \"bstp_nmix_oprc\": \"837.24\",\r\n            \"bstp_nmix_hgpr\": \"837.71\",\r\n            \"bstp_nmix_lwpr\": \"837.24\",\r\n            \"cntg_vol\": \"4172\",\r\n            \"acml_tr_pbmn\": \"10008690\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"144800\",\r\n            \"bstp_nmix_prpr\": \"837.37\",\r\n            \"bstp_nmix_oprc\": \"837.80\",\r\n            \"bstp_nmix_hgpr\": \"837.80\",\r\n            \"bstp_nmix_lwpr\": \"837.23\",\r\n            \"cntg_vol\": \"4593\",\r\n            \"acml_tr_pbmn\": \"9966720\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"144600\",\r\n            \"bstp_nmix_prpr\": \"837.66\",\r\n            \"bstp_nmix_oprc\": \"837.72\",\r\n            \"bstp_nmix_hgpr\": \"837.89\",\r\n            \"bstp_nmix_lwpr\": \"837.61\",\r\n            \"cntg_vol\": \"5105\",\r\n            \"acml_tr_pbmn\": \"9916624\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"144400\",\r\n            \"bstp_nmix_prpr\": \"837.72\",\r\n            \"bstp_nmix_oprc\": \"837.55\",\r\n            \"bstp_nmix_hgpr\": \"837.72\",\r\n            \"bstp_nmix_lwpr\": \"837.42\",\r\n            \"cntg_vol\": \"4214\",\r\n            \"acml_tr_pbmn\": \"9861241\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"144200\",\r\n            \"bstp_nmix_prpr\": \"837.50\",\r\n            \"bstp_nmix_oprc\": \"837.55\",\r\n            \"bstp_nmix_hgpr\": \"837.68\",\r\n            \"bstp_nmix_lwpr\": \"837.35\",\r\n            \"cntg_vol\": \"3357\",\r\n            \"acml_tr_pbmn\": \"9819268\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"144000\",\r\n            \"bstp_nmix_prpr\": \"837.56\",\r\n            \"bstp_nmix_oprc\": \"837.93\",\r\n            \"bstp_nmix_hgpr\": \"838.04\",\r\n            \"bstp_nmix_lwpr\": \"837.56\",\r\n            \"cntg_vol\": \"3515\",\r\n            \"acml_tr_pbmn\": \"9783824\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"143800\",\r\n            \"bstp_nmix_prpr\": \"837.96\",\r\n            \"bstp_nmix_oprc\": \"837.49\",\r\n            \"bstp_nmix_hgpr\": \"837.96\",\r\n            \"bstp_nmix_lwpr\": \"837.49\",\r\n            \"cntg_vol\": \"4026\",\r\n            \"acml_tr_pbmn\": \"9745091\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"143600\",\r\n            \"bstp_nmix_prpr\": \"837.50\",\r\n            \"bstp_nmix_oprc\": \"837.47\",\r\n            \"bstp_nmix_hgpr\": \"837.59\",\r\n            \"bstp_nmix_lwpr\": \"837.25\",\r\n            \"cntg_vol\": \"4327\",\r\n            \"acml_tr_pbmn\": \"9702397\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"143400\",\r\n            \"bstp_nmix_prpr\": \"837.44\",\r\n            \"bstp_nmix_oprc\": \"837.19\",\r\n            \"bstp_nmix_hgpr\": \"837.44\",\r\n            \"bstp_nmix_lwpr\": \"836.97\",\r\n            \"cntg_vol\": \"3352\",\r\n            \"acml_tr_pbmn\": \"9664056\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"143200\",\r\n            \"bstp_nmix_prpr\": \"837.19\",\r\n            \"bstp_nmix_oprc\": \"837.00\",\r\n            \"bstp_nmix_hgpr\": \"837.19\",\r\n            \"bstp_nmix_lwpr\": \"836.85\",\r\n            \"cntg_vol\": \"3969\",\r\n            \"acml_tr_pbmn\": \"9626091\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"143000\",\r\n            \"bstp_nmix_prpr\": \"836.85\",\r\n            \"bstp_nmix_oprc\": \"836.27\",\r\n            \"bstp_nmix_hgpr\": \"836.85\",\r\n            \"bstp_nmix_lwpr\": \"836.10\",\r\n            \"cntg_vol\": \"4263\",\r\n            \"acml_tr_pbmn\": \"9584077\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"142800\",\r\n            \"bstp_nmix_prpr\": \"836.18\",\r\n            \"bstp_nmix_oprc\": \"835.52\",\r\n            \"bstp_nmix_hgpr\": \"836.24\",\r\n            \"bstp_nmix_lwpr\": \"835.52\",\r\n            \"cntg_vol\": \"4294\",\r\n            \"acml_tr_pbmn\": \"9542286\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"142600\",\r\n            \"bstp_nmix_prpr\": \"835.62\",\r\n            \"bstp_nmix_oprc\": \"835.41\",\r\n            \"bstp_nmix_hgpr\": \"835.66\",\r\n            \"bstp_nmix_lwpr\": \"835.41\",\r\n            \"cntg_vol\": \"3538\",\r\n            \"acml_tr_pbmn\": \"9501271\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"142400\",\r\n            \"bstp_nmix_prpr\": \"835.44\",\r\n            \"bstp_nmix_oprc\": \"835.54\",\r\n            \"bstp_nmix_hgpr\": \"835.68\",\r\n            \"bstp_nmix_lwpr\": \"835.37\",\r\n            \"cntg_vol\": \"3291\",\r\n            \"acml_tr_pbmn\": \"9469724\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"142200\",\r\n            \"bstp_nmix_prpr\": \"835.48\",\r\n            \"bstp_nmix_oprc\": \"835.60\",\r\n            \"bstp_nmix_hgpr\": \"835.60\",\r\n            \"bstp_nmix_lwpr\": \"835.28\",\r\n            \"cntg_vol\": \"3640\",\r\n            \"acml_tr_pbmn\": \"9433016\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"142000\",\r\n            \"bstp_nmix_prpr\": \"835.70\",\r\n            \"bstp_nmix_oprc\": \"835.57\",\r\n            \"bstp_nmix_hgpr\": \"835.72\",\r\n            \"bstp_nmix_lwpr\": \"835.51\",\r\n            \"cntg_vol\": \"4522\",\r\n            \"acml_tr_pbmn\": \"9401939\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"141800\",\r\n            \"bstp_nmix_prpr\": \"835.54\",\r\n            \"bstp_nmix_oprc\": \"835.99\",\r\n            \"bstp_nmix_hgpr\": \"836.00\",\r\n            \"bstp_nmix_lwpr\": \"835.34\",\r\n            \"cntg_vol\": \"3266\",\r\n            \"acml_tr_pbmn\": \"9365741\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"141600\",\r\n            \"bstp_nmix_prpr\": \"835.98\",\r\n            \"bstp_nmix_oprc\": \"836.29\",\r\n            \"bstp_nmix_hgpr\": \"836.37\",\r\n            \"bstp_nmix_lwpr\": \"835.98\",\r\n            \"cntg_vol\": \"4813\",\r\n            \"acml_tr_pbmn\": \"9334612\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"141400\",\r\n            \"bstp_nmix_prpr\": \"836.34\",\r\n            \"bstp_nmix_oprc\": \"835.77\",\r\n            \"bstp_nmix_hgpr\": \"836.34\",\r\n            \"bstp_nmix_lwpr\": \"835.77\",\r\n            \"cntg_vol\": \"4714\",\r\n            \"acml_tr_pbmn\": \"9284831\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"141200\",\r\n            \"bstp_nmix_prpr\": \"835.79\",\r\n            \"bstp_nmix_oprc\": \"835.74\",\r\n            \"bstp_nmix_hgpr\": \"835.98\",\r\n            \"bstp_nmix_lwpr\": \"835.58\",\r\n            \"cntg_vol\": \"4125\",\r\n            \"acml_tr_pbmn\": \"9238577\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"141000\",\r\n            \"bstp_nmix_prpr\": \"835.74\",\r\n            \"bstp_nmix_oprc\": \"835.45\",\r\n            \"bstp_nmix_hgpr\": \"835.74\",\r\n            \"bstp_nmix_lwpr\": \"835.45\",\r\n            \"cntg_vol\": \"4232\",\r\n            \"acml_tr_pbmn\": \"9193950\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"140800\",\r\n            \"bstp_nmix_prpr\": \"835.10\",\r\n            \"bstp_nmix_oprc\": \"835.07\",\r\n            \"bstp_nmix_hgpr\": \"835.32\",\r\n            \"bstp_nmix_lwpr\": \"835.00\",\r\n            \"cntg_vol\": \"3639\",\r\n            \"acml_tr_pbmn\": \"9151925\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"stck_cntg_hour\": \"140600\",\r\n            \"bstp_nmix_prpr\": \"835.10\",\r\n            \"bstp_nmix_oprc\": \"835.09\",\r\n            \"bstp_nmix_hgpr\": \"835.23\",\r\n            \"bstp_nmix_lwpr\": \"834.96\",\r\n            \"cntg_vol\": \"4277\",",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTCA0903R",
    "name": "국내휴장일조회",
    "url": "/uapi/domestic-stock/v1/quotations/chk-holiday",
    "sheet": "국내휴장일조회",
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
        "element": "bass_dt",
        "type": "string",
        "required": "Y",
        "description": "기준일자(YYYYMMDD)"
      },
      {
        "element": "wday_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": "01:일요일, 02:월요일, 03:화요일, 04:수요일, 05:목요일, 06:금요일, 07:토요일"
      },
      {
        "element": "bzdy_yn",
        "type": "string",
        "required": "Y",
        "description": "Y/N\r\n금융기관이 업무를 하는 날"
      },
      {
        "element": "tr_day_yn",
        "type": "string",
        "required": "Y",
        "description": "Y/N\r\n증권 업무가 가능한 날(입출금, 이체 등의 업무 포함)"
      },
      {
        "element": "opnd_yn",
        "type": "string",
        "required": "Y",
        "description": "Y/N\r\n주식시장이 개장되는 날\r\n* 주문을 넣고자 할 경우 개장일여부(opnd_yn)를 사용"
      },
      {
        "element": "sttl_day_yn",
        "type": "string",
        "required": "Y",
        "description": "Y/N\r\n주식 거래에서 실제로 주식을 인수하고 돈을 지불하는 날"
      },
      {
        "element": "{\r\n    \"BASS_DT\":\"20221227\",\r\n    \"CTX_AREA_NK\":\"\",\r\n    \"CTX_AREA_FK\":\"\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"ctx_area_nk\": \"20230119            \",\r\n    \"ctx_area_fk\": \"20221227            \",\r\n    \"output\": [\r\n        {\r\n            \"bass_dt\": \"20221227\",\r\n            \"wday_dvsn_cd\": \"03\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20221228\",\r\n            \"wday_dvsn_cd\": \"04\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20221229\",\r\n            \"wday_dvsn_cd\": \"05\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20221230\",\r\n            \"wday_dvsn_cd\": \"06\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20221231\",\r\n            \"wday_dvsn_cd\": \"07\",\r\n            \"bzdy_yn\": \"N\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230101\",\r\n            \"wday_dvsn_cd\": \"01\",\r\n            \"bzdy_yn\": \"N\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230102\",\r\n            \"wday_dvsn_cd\": \"02\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230103\",\r\n            \"wday_dvsn_cd\": \"03\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230104\",\r\n            \"wday_dvsn_cd\": \"04\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230105\",\r\n            \"wday_dvsn_cd\": \"05\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230106\",\r\n            \"wday_dvsn_cd\": \"06\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230107\",\r\n            \"wday_dvsn_cd\": \"07\",\r\n            \"bzdy_yn\": \"N\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230108\",\r\n            \"wday_dvsn_cd\": \"01\",\r\n            \"bzdy_yn\": \"N\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230109\",\r\n            \"wday_dvsn_cd\": \"02\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230110\",\r\n            \"wday_dvsn_cd\": \"03\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230111\",\r\n            \"wday_dvsn_cd\": \"04\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230112\",\r\n            \"wday_dvsn_cd\": \"05\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230113\",\r\n            \"wday_dvsn_cd\": \"06\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230114\",\r\n            \"wday_dvsn_cd\": \"07\",\r\n            \"bzdy_yn\": \"N\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230115\",\r\n            \"wday_dvsn_cd\": \"01\",\r\n            \"bzdy_yn\": \"N\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"N\",\r\n            \"sttl_day_yn\": \"N\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230116\",\r\n            \"wday_dvsn_cd\": \"02\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230117\",\r\n            \"wday_dvsn_cd\": \"03\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230118\",\r\n            \"wday_dvsn_cd\": \"04\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"bass_dt\": \"20230119\",\r\n            \"wday_dvsn_cd\": \"05\",\r\n            \"bzdy_yn\": \"Y\",\r\n            \"tr_day_yn\": \"Y\",\r\n            \"opnd_yn\": \"Y\",\r\n            \"sttl_day_yn\": \"Y\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"KIOK0500\",\r\n    \"msg1\": \"조회가 계속됩니다..다음버튼을 Click 하십시오.                                   \"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKUP11750000",
    "name": "국내주식 예상체결 전체지수",
    "url": "/uapi/domestic-stock/v1/quotations/exp-total-index",
    "sheet": "국내주식 예상체결 전체지수",
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
        "element": "bstp_nmix_prpr",
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
        "element": "ascn_issu_cnt",
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
        "element": "stnr_issu_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_cls_code",
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
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "nmix_sdpr",
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
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"U\",\r\n\"fid_cond_scr_div_code\":\"11175\",\r\n\"fid_input_iscd\":\"1001\",\r\n\"fid_mkop_cls_code\":\"1\",\r\n\"fid_mrkt_cls_code\":\"K\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"bstp_nmix_prpr\": \"883.03\",\r\n        \"bstp_nmix_prdy_vrss\": \"2.57\",\r\n        \"prdy_vrss_sign\": \"2\",\r\n        \"prdy_ctrt\": \"0.29\",\r\n        \"acml_vol\": \"10611\",\r\n        \"ascn_issu_cnt\": \"513\",\r\n        \"down_issu_cnt\": \"571\",\r\n        \"stnr_issu_cnt\": \"498\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"bstp_cls_code\": \"0001\",\r\n            \"hts_kor_isnm\": \"종합\",\r\n            \"bstp_nmix_prpr\": \"2676.62\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.78\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.37\",\r\n            \"acml_vol\": \"5151\",\r\n            \"nmix_sdpr\": \"2666.84\",\r\n            \"ascn_issu_cnt\": \"409\",\r\n            \"stnr_issu_cnt\": \"249\",\r\n            \"down_issu_cnt\": \"225\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2001\",\r\n            \"hts_kor_isnm\": \"KOSPI200\",\r\n            \"bstp_nmix_prpr\": \"360.44\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.05\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.29\",\r\n            \"acml_vol\": \"1687\",\r\n            \"nmix_sdpr\": \"359.39\",\r\n            \"ascn_issu_cnt\": \"148\",\r\n            \"stnr_issu_cnt\": \"35\",\r\n            \"down_issu_cnt\": \"17\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2039\",\r\n            \"hts_kor_isnm\": \"K커뮤니케이션서비스\",\r\n            \"bstp_nmix_prpr\": \"1766.78\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.03\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.51\",\r\n            \"acml_vol\": \"42\",\r\n            \"nmix_sdpr\": \"1757.75\",\r\n            \"ascn_issu_cnt\": \"7\",\r\n            \"stnr_issu_cnt\": \"2\",\r\n            \"down_issu_cnt\": \"1\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2009\",\r\n            \"hts_kor_isnm\": \"K건설\",\r\n            \"bstp_nmix_prpr\": \"320.87\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.09\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.03\",\r\n            \"acml_vol\": \"76\",\r\n            \"nmix_sdpr\": \"320.78\",\r\n            \"ascn_issu_cnt\": \"3\",\r\n            \"stnr_issu_cnt\": \"6\",\r\n            \"down_issu_cnt\": \"1\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2010\",\r\n            \"hts_kor_isnm\": \"K중공업\",\r\n            \"bstp_nmix_prpr\": \"366.27\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.35\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.48\",\r\n            \"acml_vol\": \"457\",\r\n            \"nmix_sdpr\": \"360.92\",\r\n            \"ascn_issu_cnt\": \"12\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"1\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2011\",\r\n            \"hts_kor_isnm\": \"K철강소재\",\r\n            \"bstp_nmix_prpr\": \"857.19\",\r\n            \"bstp_nmix_prdy_vrss\": \"6.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.75\",\r\n            \"acml_vol\": \"45\",\r\n            \"nmix_sdpr\": \"850.85\",\r\n            \"ascn_issu_cnt\": \"7\",\r\n            \"stnr_issu_cnt\": \"3\",\r\n            \"down_issu_cnt\": \"1\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2012\",\r\n            \"hts_kor_isnm\": \"K에너지화학\",\r\n            \"bstp_nmix_prpr\": \"1349.16\",\r\n            \"bstp_nmix_prdy_vrss\": \"8.62\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.64\",\r\n            \"acml_vol\": \"33\",\r\n            \"nmix_sdpr\": \"1340.54\",\r\n            \"ascn_issu_cnt\": \"22\",\r\n            \"stnr_issu_cnt\": \"4\",\r\n            \"down_issu_cnt\": \"2\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2013\",\r\n            \"hts_kor_isnm\": \"K정보기술\",\r\n            \"bstp_nmix_prpr\": \"3334.19\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.80\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.11\",\r\n            \"acml_vol\": \"546\",\r\n            \"nmix_sdpr\": \"3330.39\",\r\n            \"ascn_issu_cnt\": \"8\",\r\n            \"stnr_issu_cnt\": \"3\",\r\n            \"down_issu_cnt\": \"2\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2014\",\r\n            \"hts_kor_isnm\": \"K금융\",\r\n            \"bstp_nmix_prpr\": \"832.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"-2.77\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.33\",\r\n            \"acml_vol\": \"208\",\r\n            \"nmix_sdpr\": \"835.48\",\r\n            \"ascn_issu_cnt\": \"12\",\r\n            \"stnr_issu_cnt\": \"7\",\r\n            \"down_issu_cnt\": \"3\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2015\",\r\n            \"hts_kor_isnm\": \"K생활소비재\",\r\n            \"bstp_nmix_prpr\": \"807.22\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.94\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.74\",\r\n            \"acml_vol\": \"39\",\r\n            \"nmix_sdpr\": \"801.28\",\r\n            \"ascn_issu_cnt\": \"20\",\r\n            \"stnr_issu_cnt\": \"3\",\r\n            \"down_issu_cnt\": \"1\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2016\",\r\n            \"hts_kor_isnm\": \"K경기소비재\",\r\n            \"bstp_nmix_prpr\": \"1771.78\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.87\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.56\",\r\n            \"acml_vol\": \"71\",\r\n            \"nmix_sdpr\": \"1761.91\",\r\n            \"ascn_issu_cnt\": \"26\",\r\n            \"stnr_issu_cnt\": \"4\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2017\",\r\n            \"hts_kor_isnm\": \"K산업재\",\r\n            \"bstp_nmix_prpr\": \"638.85\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.52\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.55\",\r\n            \"acml_vol\": \"144\",\r\n            \"nmix_sdpr\": \"635.33\",\r\n            \"ascn_issu_cnt\": \"19\",\r\n            \"stnr_issu_cnt\": \"1\",\r\n            \"down_issu_cnt\": \"3\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2018\",\r\n            \"hts_kor_isnm\": \"K헬스케어\",\r\n            \"bstp_nmix_prpr\": \"1880.59\",\r\n            \"bstp_nmix_prdy_vrss\": \"7.50\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.40\",\r\n            \"acml_vol\": \"25\",\r\n            \"nmix_sdpr\": \"1873.09\",\r\n            \"ascn_issu_cnt\": \"12\",\r\n            \"stnr_issu_cnt\": \"2\",\r\n            \"down_issu_cnt\": \"2\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"0163\",\r\n            \"hts_kor_isnm\": \"고배당50\",\r\n            \"bstp_nmix_prpr\": \"3012.54\",\r\n            \"bstp_nmix_prdy_vrss\": \"2.40\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.08\",\r\n            \"acml_vol\": \"654\",\r\n            \"nmix_sdpr\": \"3010.14\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"0164\",\r\n            \"hts_kor_isnm\": \"배당성장50\",\r\n            \"bstp_nmix_prpr\": \"3697.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"14.09\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.38\",\r\n            \"acml_vol\": \"557\",\r\n            \"nmix_sdpr\": \"3683.62\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"0165\",\r\n            \"hts_kor_isnm\": \"우선주\",\r\n            \"bstp_nmix_prpr\": \"3159.80\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.00\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.10\",\r\n            \"acml_vol\": \"27\",\r\n            \"nmix_sdpr\": \"3156.80\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2180\",\r\n            \"hts_kor_isnm\": \"코스피 200 ESG 지수\",\r\n            \"bstp_nmix_prpr\": \"408.37\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.89\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.22\",\r\n            \"acml_vol\": \"1068\",\r\n            \"nmix_sdpr\": \"407.48\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2040\",\r\n            \"hts_kor_isnm\": \"코스피200 초대형 제외지수\",\r\n            \"bstp_nmix_prpr\": \"261.99\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.79\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.30\",\r\n            \"acml_vol\": \"1276\",\r\n            \"nmix_sdpr\": \"261.20\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2037\",\r\n            \"hts_kor_isnm\": \"코스피200 예측 고배당 50\",\r\n            \"bstp_nmix_prpr\": \"2034.64\",\r\n            \"bstp_nmix_prdy_vrss\": \"7.50\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.37\",\r\n            \"acml_vol\": \"227\",\r\n            \"nmix_sdpr\": \"2027.14\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2038\",\r\n            \"hts_kor_isnm\": \"코스피200 예측 배당성장 50\",\r\n            \"bstp_nmix_prpr\": \"1710.41\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.08\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.53\",\r\n            \"acml_vol\": \"581\",\r\n            \"nmix_sdpr\": \"1701.33\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2224\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 30%\",\r\n            \"bstp_nmix_prpr\": \"360.08\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.06\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.30\",\r\n            \"acml_vol\": \"1687\",\r\n            \"nmix_sdpr\": \"359.02\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2227\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 25%\",\r\n            \"bstp_nmix_prpr\": \"356.69\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.04\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.29\",\r\n            \"acml_vol\": \"1687\",\r\n            \"nmix_sdpr\": \"355.65\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2232\",\r\n            \"hts_kor_isnm\": \"K200 비중상한 20%\",\r\n            \"bstp_nmix_prpr\": \"346.65\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.02\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.30\",\r\n            \"acml_vol\": \"1687\",\r\n            \"nmix_sdpr\": \"345.63\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"0244\",\r\n            \"hts_kor_isnm\": \"코스피200제외 코스피지수\",\r\n            \"bstp_nmix_prpr\": \"3337.06\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.31\",\r\n            \"acml_vol\": \"3373\",\r\n            \"nmix_sdpr\": \"3326.72\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        },\r\n        {\r\n            \"bstp_cls_code\": \"2283\",\r\n            \"hts_kor_isnm\": \"코스피 200 기후변화지수\",\r\n            \"bstp_nmix_prpr\": \"1580.49\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.56\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.29\",\r\n            \"acml_vol\": \"1639\",\r\n            \"nmix_sdpr\": \"1575.93\",\r\n            \"ascn_issu_cnt\": \"0\",\r\n            \"stnr_issu_cnt\": \"0\",\r\n            \"down_issu_cnt\": \"0\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPUP02100000",
    "name": "국내업종 현재지수",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-price",
    "sheet": "국내업종 현재지수",
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
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "prdy_vol",
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
        "element": "prdy_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_nmix_vrss_nmix_oprc",
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
        "element": "bstp_nmix_oprc_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_nmix_vrss_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgpr_vrss_prpr_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_clpr_vrss_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lwpr_vrss_prpr_sign",
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
        "element": "ascn_issu_cnt",
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
        "element": "dryy_bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_hgpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_lwpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_lwpr_date",
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
        "element": "seln_rsqn_rate",
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
        "element": "ntby_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"U\"\r\n\"fid_input_iscd\":\"1001\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": {\r\n        \"bstp_nmix_prpr\": \"857.60\",\r\n        \"bstp_nmix_prdy_vrss\": \"-1.61\",\r\n        \"prdy_vrss_sign\": \"5\",\r\n        \"bstp_nmix_prdy_ctrt\": \"-0.19\",\r\n        \"acml_vol\": \"1312496\",\r\n        \"prdy_vol\": \"1222188\",\r\n        \"acml_tr_pbmn\": \"11507962\",\r\n        \"prdy_tr_pbmn\": \"11203385\",\r\n        \"bstp_nmix_oprc\": \"863.69\",\r\n        \"prdy_nmix_vrss_nmix_oprc\": \"4.48\",\r\n        \"oprc_vrss_prpr_sign\": \"2\",\r\n        \"bstp_nmix_oprc_prdy_ctrt\": \"0.52\",\r\n        \"bstp_nmix_hgpr\": \"864.24\",\r\n        \"prdy_nmix_vrss_nmix_hgpr\": \"5.03\",\r\n        \"hgpr_vrss_prpr_sign\": \"2\",\r\n        \"bstp_nmix_hgpr_prdy_ctrt\": \"0.59\",\r\n        \"bstp_nmix_lwpr\": \"854.72\",\r\n        \"prdy_clpr_vrss_lwpr\": \"-4.49\",\r\n        \"lwpr_vrss_prpr_sign\": \"5\",\r\n        \"prdy_clpr_vrss_lwpr_rate\": \"-0.52\",\r\n        \"ascn_issu_cnt\": \"828\",\r\n        \"uplm_issu_cnt\": \"5\",\r\n        \"stnr_issu_cnt\": \"94\",\r\n        \"down_issu_cnt\": \"716\",\r\n        \"lslm_issu_cnt\": \"1\",\r\n        \"dryy_bstp_nmix_hgpr\": \"890.06\",\r\n        \"dryy_hgpr_vrss_prpr_rate\": \"3.65\",\r\n        \"dryy_bstp_nmix_hgpr_date\": \"20240109\",\r\n        \"dryy_bstp_nmix_lwpr\": \"786.28\",\r\n        \"dryy_lwpr_vrss_prpr_rate\": \"-9.07\",\r\n        \"dryy_bstp_nmix_lwpr_date\": \"20240201\",\r\n        \"total_askp_rsqn\": \"24146999\",\r\n        \"total_bidp_rsqn\": \"40450437\",\r\n        \"seln_rsqn_rate\": \"37.38\",\r\n        \"shnu_rsqn_rate\": \"62.62\",\r\n        \"ntby_rsqn\": \"16303438\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHMCM000002C0",
    "name": "국내선물 영업일조회",
    "url": "/uapi/domestic-stock/v1/quotations/market-time",
    "sheet": "국내선물 영업일조회",
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
        "element": "date1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "date2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "date3",
        "type": "string",
        "required": "Y",
        "description": "영업일 당일"
      },
      {
        "element": "date4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "date5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "today",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "time",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "s_time",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "e_time",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "없음",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"date1\": \"20240909\",\r\n        \"date2\": \"20240910\",\r\n        \"date3\": \"20240911\",\r\n        \"date4\": \"20240912\",\r\n        \"date5\": \"20240913\",\r\n        \"today\": \"20240911\",\r\n        \"time\": \"083523\",\r\n        \"s_time\": \"084500\",\r\n        \"e_time\": \"154500\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPUP02110100",
    "name": "국내업종 시간별지수(초)",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-tickprice",
    "sheet": "국내업종 시간별지수(초)",
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
        "element": "stck_cntg_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "acml_vol",
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
        "element": "fid_cond_mrkt_div_code:U\r\nfid_input_iscd:1001",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_cntg_hour\": \"100520\",\r\n            \"bstp_nmix_prpr\": \"916.59\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.09\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.22\",\r\n            \"acml_tr_pbmn\": \"3818437\",\r\n            \"acml_vol\": \"311514\",\r\n            \"cntg_vol\": \"378\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100510\",\r\n            \"bstp_nmix_prpr\": \"916.56\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.06\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.22\",\r\n            \"acml_tr_pbmn\": \"3814862\",\r\n            \"acml_vol\": \"311136\",\r\n            \"cntg_vol\": \"389\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100500\",\r\n            \"bstp_nmix_prpr\": \"916.60\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3811191\",\r\n            \"acml_vol\": \"310747\",\r\n            \"cntg_vol\": \"460\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100450\",\r\n            \"bstp_nmix_prpr\": \"916.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.21\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3806215\",\r\n            \"acml_vol\": \"310287\",\r\n            \"cntg_vol\": \"347\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100440\",\r\n            \"bstp_nmix_prpr\": \"916.71\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.21\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3802603\",\r\n            \"acml_vol\": \"309940\",\r\n            \"cntg_vol\": \"378\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100430\",\r\n            \"bstp_nmix_prpr\": \"916.87\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3798885\",\r\n            \"acml_vol\": \"309562\",\r\n            \"cntg_vol\": \"390\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100420\",\r\n            \"bstp_nmix_prpr\": \"916.87\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3793980\",\r\n            \"acml_vol\": \"309172\",\r\n            \"cntg_vol\": \"331\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100410\",\r\n            \"bstp_nmix_prpr\": \"916.69\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.19\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3789649\",\r\n            \"acml_vol\": \"308841\",\r\n            \"cntg_vol\": \"387\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100400\",\r\n            \"bstp_nmix_prpr\": \"916.47\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.97\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.21\",\r\n            \"acml_tr_pbmn\": \"3784355\",\r\n            \"acml_vol\": \"308454\",\r\n            \"cntg_vol\": \"302\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100350\",\r\n            \"bstp_nmix_prpr\": \"916.69\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.19\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3779730\",\r\n            \"acml_vol\": \"308152\",\r\n            \"cntg_vol\": \"389\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100340\",\r\n            \"bstp_nmix_prpr\": \"916.64\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.14\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3774584\",\r\n            \"acml_vol\": \"307763\",\r\n            \"cntg_vol\": \"359\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100330\",\r\n            \"bstp_nmix_prpr\": \"916.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3769289\",\r\n            \"acml_vol\": \"307404\",\r\n            \"cntg_vol\": \"590\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100320\",\r\n            \"bstp_nmix_prpr\": \"916.86\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.36\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3764728\",\r\n            \"acml_vol\": \"306814\",\r\n            \"cntg_vol\": \"395\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100310\",\r\n            \"bstp_nmix_prpr\": \"916.76\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.26\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3758157\",\r\n            \"acml_vol\": \"306419\",\r\n            \"cntg_vol\": \"414\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100300\",\r\n            \"bstp_nmix_prpr\": \"917.03\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.53\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3753915\",\r\n            \"acml_vol\": \"306005\",\r\n            \"cntg_vol\": \"351\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100250\",\r\n            \"bstp_nmix_prpr\": \"917.08\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.58\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.28\",\r\n            \"acml_tr_pbmn\": \"3749232\",\r\n            \"acml_vol\": \"305654\",\r\n            \"cntg_vol\": \"440\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100240\",\r\n            \"bstp_nmix_prpr\": \"917.18\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.68\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.29\",\r\n            \"acml_tr_pbmn\": \"3741905\",\r\n            \"acml_vol\": \"305214\",\r\n            \"cntg_vol\": \"324\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100230\",\r\n            \"bstp_nmix_prpr\": \"917.27\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.77\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.30\",\r\n            \"acml_tr_pbmn\": \"3737983\",\r\n            \"acml_vol\": \"304890\",\r\n            \"cntg_vol\": \"449\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100220\",\r\n            \"bstp_nmix_prpr\": \"917.31\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.81\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.30\",\r\n            \"acml_tr_pbmn\": \"3732890\",\r\n            \"acml_vol\": \"304441\",\r\n            \"cntg_vol\": \"459\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100210\",\r\n            \"bstp_nmix_prpr\": \"916.61\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.11\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3725485\",\r\n            \"acml_vol\": \"303982\",\r\n            \"cntg_vol\": \"424\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100200\",\r\n            \"bstp_nmix_prpr\": \"916.64\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.14\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3720969\",\r\n            \"acml_vol\": \"303558\",\r\n            \"cntg_vol\": \"365\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100150\",\r\n            \"bstp_nmix_prpr\": \"916.76\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.26\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3716791\",\r\n            \"acml_vol\": \"303193\",\r\n            \"cntg_vol\": \"377\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100140\",\r\n            \"bstp_nmix_prpr\": \"916.49\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.99\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.21\",\r\n            \"acml_tr_pbmn\": \"3712492\",\r\n            \"acml_vol\": \"302816\",\r\n            \"cntg_vol\": \"392\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100130\",\r\n            \"bstp_nmix_prpr\": \"916.49\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.99\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.21\",\r\n            \"acml_tr_pbmn\": \"3707273\",\r\n            \"acml_vol\": \"302424\",\r\n            \"cntg_vol\": \"324\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100120\",\r\n            \"bstp_nmix_prpr\": \"916.60\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3702465\",\r\n            \"acml_vol\": \"302100\",\r\n            \"cntg_vol\": \"430\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100110\",\r\n            \"bstp_nmix_prpr\": \"916.55\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.05\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.22\",\r\n            \"acml_tr_pbmn\": \"3698004\",\r\n            \"acml_vol\": \"301670\",\r\n            \"cntg_vol\": \"387\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100100\",\r\n            \"bstp_nmix_prpr\": \"916.33\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.83\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.20\",\r\n            \"acml_tr_pbmn\": \"3692560\",\r\n            \"acml_vol\": \"301283\",\r\n            \"cntg_vol\": \"428\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100050\",\r\n            \"bstp_nmix_prpr\": \"916.43\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.93\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.21\",\r\n            \"acml_tr_pbmn\": \"3687275\",\r\n            \"acml_vol\": \"300855\",\r\n            \"cntg_vol\": \"437\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100040\",\r\n            \"bstp_nmix_prpr\": \"916.79\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.29\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3681346\",\r\n            \"acml_vol\": \"300418\",\r\n            \"cntg_vol\": \"465\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100030\",\r\n            \"bstp_nmix_prpr\": \"917.01\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.51\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3676019\",\r\n            \"acml_vol\": \"299953\",\r\n            \"cntg_vol\": \"453\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100020\",\r\n            \"bstp_nmix_prpr\": \"916.77\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.27\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3669136\",\r\n            \"acml_vol\": \"299500\",\r\n            \"cntg_vol\": \"443\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100010\",\r\n            \"bstp_nmix_prpr\": \"916.76\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.26\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3663148\",\r\n            \"acml_vol\": \"299057\",\r\n            \"cntg_vol\": \"523\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"100000\",\r\n            \"bstp_nmix_prpr\": \"916.49\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.99\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.21\",\r\n            \"acml_tr_pbmn\": \"3656614\",\r\n            \"acml_vol\": \"298534\",\r\n            \"cntg_vol\": \"444\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095950\",\r\n            \"bstp_nmix_prpr\": \"916.60\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.10\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3651490\",\r\n            \"acml_vol\": \"298090\",\r\n            \"cntg_vol\": \"388\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095940\",\r\n            \"bstp_nmix_prpr\": \"916.84\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3646864\",\r\n            \"acml_vol\": \"297702\",\r\n            \"cntg_vol\": \"446\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095930\",\r\n            \"bstp_nmix_prpr\": \"916.90\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.40\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3642503\",\r\n            \"acml_vol\": \"297256\",\r\n            \"cntg_vol\": \"426\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095920\",\r\n            \"bstp_nmix_prpr\": \"917.04\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.54\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3638580\",\r\n            \"acml_vol\": \"296830\",\r\n            \"cntg_vol\": \"493\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095910\",\r\n            \"bstp_nmix_prpr\": \"916.99\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.49\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3634479\",\r\n            \"acml_vol\": \"296337\",\r\n            \"cntg_vol\": \"456\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095900\",\r\n            \"bstp_nmix_prpr\": \"917.02\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.52\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3629148\",\r\n            \"acml_vol\": \"295881\",\r\n            \"cntg_vol\": \"602\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095850\",\r\n            \"bstp_nmix_prpr\": \"917.16\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.66\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.29\",\r\n            \"acml_tr_pbmn\": \"3621794\",\r\n            \"acml_vol\": \"295279\",\r\n            \"cntg_vol\": \"652\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095840\",\r\n            \"bstp_nmix_prpr\": \"917.35\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.85\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.31\",\r\n            \"acml_tr_pbmn\": \"3616303\",\r\n            \"acml_vol\": \"294627\",\r\n            \"cntg_vol\": \"361\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095830\",\r\n            \"bstp_nmix_prpr\": \"917.33\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.83\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.31\",\r\n            \"acml_tr_pbmn\": \"3612169\",\r\n            \"acml_vol\": \"294266\",\r\n            \"cntg_vol\": \"454\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095820\",\r\n            \"bstp_nmix_prpr\": \"917.37\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.87\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.31\",\r\n            \"acml_tr_pbmn\": \"3607064\",\r\n            \"acml_vol\": \"293812\",\r\n            \"cntg_vol\": \"515\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095810\",\r\n            \"bstp_nmix_prpr\": \"917.32\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.82\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.31\",\r\n            \"acml_tr_pbmn\": \"3601548\",\r\n            \"acml_vol\": \"293297\",\r\n            \"cntg_vol\": \"545\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095800\",\r\n            \"bstp_nmix_prpr\": \"917.20\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.70\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.29\",\r\n            \"acml_tr_pbmn\": \"3594204\",\r\n            \"acml_vol\": \"292752\",\r\n            \"cntg_vol\": \"394\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095750\",\r\n            \"bstp_nmix_prpr\": \"917.37\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.87\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.31\",\r\n            \"acml_tr_pbmn\": \"3588380\",\r\n            \"acml_vol\": \"292358\",\r\n            \"cntg_vol\": \"392\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095740\",\r\n            \"bstp_nmix_prpr\": \"917.29\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.79\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.30\",\r\n            \"acml_tr_pbmn\": \"3583543\",\r\n            \"acml_vol\": \"291966\",\r\n            \"cntg_vol\": \"383\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095730\",\r\n            \"bstp_nmix_prpr\": \"917.16\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.66\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.29\",\r\n            \"acml_tr_pbmn\": \"3578536\",\r\n            \"acml_vol\": \"291583\",\r\n            \"cntg_vol\": \"372\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095720\",\r\n            \"bstp_nmix_prpr\": \"917.09\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.59\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.28\",\r\n            \"acml_tr_pbmn\": \"3573648\",\r\n            \"acml_vol\": \"291211\",\r\n            \"cntg_vol\": \"387\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095710\",\r\n            \"bstp_nmix_prpr\": \"917.12\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.62\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.28\",\r\n            \"acml_tr_pbmn\": \"3568052\",\r\n            \"acml_vol\": \"290824\",\r\n            \"cntg_vol\": \"481\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095700\",\r\n            \"bstp_nmix_prpr\": \"916.83\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.33\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3562707\",\r\n            \"acml_vol\": \"290343\",\r\n            \"cntg_vol\": \"376\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095650\",\r\n            \"bstp_nmix_prpr\": \"916.72\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.22\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3558237\",\r\n            \"acml_vol\": \"289967\",\r\n            \"cntg_vol\": \"457\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095640\",\r\n            \"bstp_nmix_prpr\": \"916.76\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.26\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3552581\",\r\n            \"acml_vol\": \"289510\",\r\n            \"cntg_vol\": \"596\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095630\",\r\n            \"bstp_nmix_prpr\": \"917.30\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.80\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.30\",\r\n            \"acml_tr_pbmn\": \"3544456\",\r\n            \"acml_vol\": \"288914\",\r\n            \"cntg_vol\": \"406\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095620\",\r\n            \"bstp_nmix_prpr\": \"917.51\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.01\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.33\",\r\n            \"acml_tr_pbmn\": \"3538246\",\r\n            \"acml_vol\": \"288508\",\r\n            \"cntg_vol\": \"579\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095610\",\r\n            \"bstp_nmix_prpr\": \"917.52\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.02\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.33\",\r\n            \"acml_tr_pbmn\": \"3532214\",\r\n            \"acml_vol\": \"287929\",\r\n            \"cntg_vol\": \"495\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095600\",\r\n            \"bstp_nmix_prpr\": \"917.61\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.11\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n            \"acml_tr_pbmn\": \"3526666\",\r\n            \"acml_vol\": \"287434\",\r\n            \"cntg_vol\": \"407\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095550\",\r\n            \"bstp_nmix_prpr\": \"917.64\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.14\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n            \"acml_tr_pbmn\": \"3521010\",\r\n            \"acml_vol\": \"287027\",\r\n            \"cntg_vol\": \"614\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095540\",\r\n            \"bstp_nmix_prpr\": \"917.58\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.08\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.33\",\r\n            \"acml_tr_pbmn\": \"3514113\",\r\n            \"acml_vol\": \"286413\",\r\n            \"cntg_vol\": \"414\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095530\",\r\n            \"bstp_nmix_prpr\": \"917.70\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.20\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.35\",\r\n            \"acml_tr_pbmn\": \"3507645\",\r\n            \"acml_vol\": \"285999\",\r\n            \"cntg_vol\": \"527\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095520\",\r\n            \"bstp_nmix_prpr\": \"917.44\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.94\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.32\",\r\n            \"acml_tr_pbmn\": \"3501459\",\r\n            \"acml_vol\": \"285472\",\r\n            \"cntg_vol\": \"556\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095510\",\r\n            \"bstp_nmix_prpr\": \"917.61\",\r\n            \"bstp_nmix_prdy_vrss\": \"12.11\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n            \"acml_tr_pbmn\": \"3495215\",\r\n            \"acml_vol\": \"284916\",\r\n            \"cntg_vol\": \"584\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095500\",\r\n            \"bstp_nmix_prpr\": \"917.09\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.59\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.28\",\r\n            \"acml_tr_pbmn\": \"3485132\",\r\n            \"acml_vol\": \"284332\",\r\n            \"cntg_vol\": \"657\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095450\",\r\n            \"bstp_nmix_prpr\": \"916.99\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.49\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3478768\",\r\n            \"acml_vol\": \"283675\",\r\n            \"cntg_vol\": \"708\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095440\",\r\n            \"bstp_nmix_prpr\": \"916.84\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3473716\",\r\n            \"acml_vol\": \"282967\",\r\n            \"cntg_vol\": \"477\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095430\",\r\n            \"bstp_nmix_prpr\": \"916.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3468638\",\r\n            \"acml_vol\": \"282490\",\r\n            \"cntg_vol\": \"538\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095420\",\r\n            \"bstp_nmix_prpr\": \"916.65\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.15\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3463123\",\r\n            \"acml_vol\": \"281952\",\r\n            \"cntg_vol\": \"644\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095410\",\r\n            \"bstp_nmix_prpr\": \"916.52\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.02\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.22\",\r\n            \"acml_tr_pbmn\": \"3456930\",\r\n            \"acml_vol\": \"281308\",\r\n            \"cntg_vol\": \"557\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095400\",\r\n            \"bstp_nmix_prpr\": \"916.28\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.78\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.19\",\r\n            \"acml_tr_pbmn\": \"3451089\",\r\n            \"acml_vol\": \"280751\",\r\n            \"cntg_vol\": \"551\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095350\",\r\n            \"bstp_nmix_prpr\": \"916.31\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.81\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.19\",\r\n            \"acml_tr_pbmn\": \"3445942\",\r\n            \"acml_vol\": \"280200\",\r\n            \"cntg_vol\": \"825\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095340\",\r\n            \"bstp_nmix_prpr\": \"916.25\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.75\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.19\",\r\n            \"acml_tr_pbmn\": \"3440251\",\r\n            \"acml_vol\": \"279375\",\r\n            \"cntg_vol\": \"594\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095330\",\r\n            \"bstp_nmix_prpr\": \"916.47\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.97\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.21\",\r\n            \"acml_tr_pbmn\": \"3433966\",\r\n            \"acml_vol\": \"278781\",\r\n            \"cntg_vol\": \"896\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095320\",\r\n            \"bstp_nmix_prpr\": \"916.56\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.06\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.22\",\r\n            \"acml_tr_pbmn\": \"3423815\",\r\n            \"acml_vol\": \"277885\",\r\n            \"cntg_vol\": \"670\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095310\",\r\n            \"bstp_nmix_prpr\": \"916.81\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.31\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3416973\",\r\n            \"acml_vol\": \"277215\",\r\n            \"cntg_vol\": \"818\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095300\",\r\n            \"bstp_nmix_prpr\": \"916.85\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.35\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3409854\",\r\n            \"acml_vol\": \"276397\",\r\n            \"cntg_vol\": \"777\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095250\",\r\n            \"bstp_nmix_prpr\": \"917.09\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.59\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.28\",\r\n            \"acml_tr_pbmn\": \"3404203\",\r\n            \"acml_vol\": \"275620\",\r\n            \"cntg_vol\": \"474\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095240\",\r\n            \"bstp_nmix_prpr\": \"916.99\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.49\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3398691\",\r\n            \"acml_vol\": \"275146\",\r\n            \"cntg_vol\": \"457\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095230\",\r\n            \"bstp_nmix_prpr\": \"916.96\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.46\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3392384\",\r\n            \"acml_vol\": \"274689\",\r\n            \"cntg_vol\": \"315\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095220\",\r\n            \"bstp_nmix_prpr\": \"916.84\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3387938\",\r\n            \"acml_vol\": \"274374\",\r\n            \"cntg_vol\": \"391\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095210\",\r\n            \"bstp_nmix_prpr\": \"916.96\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.46\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3383576\",\r\n            \"acml_vol\": \"273983\",\r\n            \"cntg_vol\": \"543\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095200\",\r\n            \"bstp_nmix_prpr\": \"917.01\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.51\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3377596\",\r\n            \"acml_vol\": \"273440\",\r\n            \"cntg_vol\": \"503\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095150\",\r\n            \"bstp_nmix_prpr\": \"916.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3373037\",\r\n            \"acml_vol\": \"272937\",\r\n            \"cntg_vol\": \"407\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095140\",\r\n            \"bstp_nmix_prpr\": \"916.73\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.23\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3365439\",\r\n            \"acml_vol\": \"272530\",\r\n            \"cntg_vol\": \"487\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095130\",\r\n            \"bstp_nmix_prpr\": \"916.63\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.13\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"acml_tr_pbmn\": \"3359798\",\r\n            \"acml_vol\": \"272043\",\r\n            \"cntg_vol\": \"418\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095120\",\r\n            \"bstp_nmix_prpr\": \"916.74\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.24\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3354130\",\r\n            \"acml_vol\": \"271625\",\r\n            \"cntg_vol\": \"439\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095110\",\r\n            \"bstp_nmix_prpr\": \"916.73\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.23\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.24\",\r\n            \"acml_tr_pbmn\": \"3347725\",\r\n            \"acml_vol\": \"271186\",\r\n            \"cntg_vol\": \"459\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095100\",\r\n            \"bstp_nmix_prpr\": \"916.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3340647\",\r\n            \"acml_vol\": \"270727\",\r\n            \"cntg_vol\": \"393\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095050\",\r\n            \"bstp_nmix_prpr\": \"916.85\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.35\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3335589\",\r\n            \"acml_vol\": \"270334\",\r\n            \"cntg_vol\": \"358\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095040\",\r\n            \"bstp_nmix_prpr\": \"916.85\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.35\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3330288\",\r\n            \"acml_vol\": \"269976\",\r\n            \"cntg_vol\": \"390\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095030\",\r\n            \"bstp_nmix_prpr\": \"916.88\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.38\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3325139\",\r\n            \"acml_vol\": \"269586\",\r\n            \"cntg_vol\": \"399\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095020\",\r\n            \"bstp_nmix_prpr\": \"916.94\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3320375\",\r\n            \"acml_vol\": \"269187\",\r\n            \"cntg_vol\": \"463\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095010\",\r\n            \"bstp_nmix_prpr\": \"916.95\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.45\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.26\",\r\n            \"acml_tr_pbmn\": \"3315297\",\r\n            \"acml_vol\": \"268724\",\r\n            \"cntg_vol\": \"416\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"095000\",\r\n            \"bstp_nmix_prpr\": \"916.97\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.47\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3310129\",\r\n            \"acml_vol\": \"268308\",\r\n            \"cntg_vol\": \"411\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"094950\",\r\n            \"bstp_nmix_prpr\": \"916.82\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.32\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.25\",\r\n            \"acml_tr_pbmn\": \"3304716\",\r\n            \"acml_vol\": \"267897\",\r\n            \"cntg_vol\": \"505\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"094940\",\r\n            \"bstp_nmix_prpr\": \"917.01\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.51\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.27\",\r\n            \"acml_tr_pbmn\": \"3299470\",\r\n            \"acml_vol\": \"267392\",\r\n            \"cntg_vol\": \"432\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"094930\",\r\n            \"bstp_nmix_prpr\": \"917.16\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.66\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.29\",\r\n            \"acml_tr_pbmn\": \"3294030\",\r\n            \"acml_vol\": \"266960\",\r\n            \"cntg_vol\": \"416\"\r\n        },\r\n        {\r\n            \"stck_cntg_hour\": \"094920\",\r\n            \"bstp_nmix_prpr\": \"917.05\",\r\n            \"bstp_nmix_prdy_vrss\": \"11.55\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.28\",",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPUP02120000",
    "name": "국내업종 일자별지수",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-index-daily-price",
    "sheet": "국내업종 일자별지수",
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
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
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
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
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
        "element": "down_issu_cnt",
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
        "element": "uplm_issu_cnt",
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
        "element": "prdy_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_hgpr_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dryy_bstp_nmix_lwpr_date",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "bstp_nmix_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_vol_rlim",
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
        "element": "invt_new_psdg",
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
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"U\"\r\n\"fid_input_iscd\":\"0001\"\r\n\"fid_input_date_1\":\"20240125\"\r\n\"fid_period_div_code\":\"D\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"bstp_nmix_prpr\": \"2648.76\",\r\n        \"bstp_nmix_prdy_vrss\": \"34.96\",\r\n        \"prdy_vrss_sign\": \"2\",\r\n        \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n        \"acml_vol\": \"593842\",\r\n        \"acml_tr_pbmn\": \"10221804\",\r\n        \"bstp_nmix_oprc\": \"2635.63\",\r\n        \"bstp_nmix_hgpr\": \"2648.76\",\r\n        \"bstp_nmix_lwpr\": \"2625.01\",\r\n        \"prdy_vol\": \"621363\",\r\n        \"ascn_issu_cnt\": \"628\",\r\n        \"down_issu_cnt\": \"250\",\r\n        \"stnr_issu_cnt\": \"58\",\r\n        \"uplm_issu_cnt\": \"0\",\r\n        \"lslm_issu_cnt\": \"0\",\r\n        \"prdy_tr_pbmn\": \"10691024\",\r\n        \"dryy_bstp_nmix_hgpr_date\": \"20240102\",\r\n        \"dryy_bstp_nmix_hgpr\": \"2675.80\",\r\n        \"dryy_bstp_nmix_lwpr\": \"2429.12\",\r\n        \"dryy_bstp_nmix_lwpr_date\": \"20240118\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240125\",\r\n            \"bstp_nmix_prpr\": \"2470.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.65\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.03\",\r\n            \"bstp_nmix_oprc\": \"2467.73\",\r\n            \"bstp_nmix_hgpr\": \"2474.01\",\r\n            \"bstp_nmix_lwpr\": \"2452.36\",\r\n            \"acml_vol_rlim\": \"166.23\",\r\n            \"acml_vol\": \"357234\",\r\n            \"acml_tr_pbmn\": \"8124338\",\r\n            \"invt_new_psdg\": \"-19.94\",\r\n            \"d20_dsrt\": \"97.44\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240124\",\r\n            \"bstp_nmix_prpr\": \"2469.69\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-8.92\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.36\",\r\n            \"bstp_nmix_oprc\": \"2476.22\",\r\n            \"bstp_nmix_hgpr\": \"2476.22\",\r\n            \"bstp_nmix_lwpr\": \"2454.34\",\r\n            \"acml_vol_rlim\": \"150.16\",\r\n            \"acml_vol\": \"395464\",\r\n            \"acml_tr_pbmn\": \"7446527\",\r\n            \"invt_new_psdg\": \"-30.49\",\r\n            \"d20_dsrt\": \"97.17\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240123\",\r\n            \"bstp_nmix_prpr\": \"2478.61\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"14.26\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.58\",\r\n            \"bstp_nmix_oprc\": \"2478.32\",\r\n            \"bstp_nmix_hgpr\": \"2482.84\",\r\n            \"bstp_nmix_lwpr\": \"2464.24\",\r\n            \"acml_vol_rlim\": \"125.74\",\r\n            \"acml_vol\": \"472284\",\r\n            \"acml_tr_pbmn\": \"8029400\",\r\n            \"invt_new_psdg\": \"-32.13\",\r\n            \"d20_dsrt\": \"97.27\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240122\",\r\n            \"bstp_nmix_prpr\": \"2464.35\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-8.39\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.34\",\r\n            \"bstp_nmix_oprc\": \"2489.57\",\r\n            \"bstp_nmix_hgpr\": \"2490.69\",\r\n            \"bstp_nmix_lwpr\": \"2464.35\",\r\n            \"acml_vol_rlim\": \"153.03\",\r\n            \"acml_vol\": \"388046\",\r\n            \"acml_tr_pbmn\": \"8419916\",\r\n            \"invt_new_psdg\": \"-48.90\",\r\n            \"d20_dsrt\": \"96.48\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240119\",\r\n            \"bstp_nmix_prpr\": \"2472.74\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"32.70\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n            \"bstp_nmix_oprc\": \"2468.43\",\r\n            \"bstp_nmix_hgpr\": \"2479.00\",\r\n            \"bstp_nmix_lwpr\": \"2455.50\",\r\n            \"acml_vol_rlim\": \"114.46\",\r\n            \"acml_vol\": \"518807\",\r\n            \"acml_tr_pbmn\": \"9174537\",\r\n            \"invt_new_psdg\": \"-49.12\",\r\n            \"d20_dsrt\": \"96.52\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240118\",\r\n            \"bstp_nmix_prpr\": \"2440.04\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.14\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.17\",\r\n            \"bstp_nmix_oprc\": \"2439.96\",\r\n            \"bstp_nmix_hgpr\": \"2453.97\",\r\n            \"bstp_nmix_lwpr\": \"2429.12\",\r\n            \"acml_vol_rlim\": \"103.91\",\r\n            \"acml_vol\": \"571508\",\r\n            \"acml_tr_pbmn\": \"8300178\",\r\n            \"invt_new_psdg\": \"-76.77\",\r\n            \"d20_dsrt\": \"95.07\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240117\",\r\n            \"bstp_nmix_prpr\": \"2435.90\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-61.69\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-2.47\",\r\n            \"bstp_nmix_oprc\": \"2501.23\",\r\n            \"bstp_nmix_hgpr\": \"2503.91\",\r\n            \"bstp_nmix_lwpr\": \"2435.34\",\r\n            \"acml_vol_rlim\": \"61.50\",\r\n            \"acml_vol\": \"965595\",\r\n            \"acml_tr_pbmn\": \"11281598\",\r\n            \"invt_new_psdg\": \"-89.46\",\r\n            \"d20_dsrt\": \"94.67\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240116\",\r\n            \"bstp_nmix_prpr\": \"2497.59\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-28.40\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.12\",\r\n            \"bstp_nmix_oprc\": \"2516.27\",\r\n            \"bstp_nmix_hgpr\": \"2524.35\",\r\n            \"bstp_nmix_lwpr\": \"2491.13\",\r\n            \"acml_vol_rlim\": \"90.03\",\r\n            \"acml_vol\": \"659579\",\r\n            \"acml_tr_pbmn\": \"8828509\",\r\n            \"invt_new_psdg\": \"-89.46\",\r\n            \"d20_dsrt\": \"96.83\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240115\",\r\n            \"bstp_nmix_prpr\": \"2525.99\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"0.94\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.04\",\r\n            \"bstp_nmix_oprc\": \"2525.69\",\r\n            \"bstp_nmix_hgpr\": \"2536.06\",\r\n            \"bstp_nmix_lwpr\": \"2515.84\",\r\n            \"acml_vol_rlim\": \"74.04\",\r\n            \"acml_vol\": \"802102\",\r\n            \"acml_tr_pbmn\": \"8182707\",\r\n            \"invt_new_psdg\": \"-70.35\",\r\n            \"d20_dsrt\": \"97.84\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240112\",\r\n            \"bstp_nmix_prpr\": \"2525.05\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-15.22\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.60\",\r\n            \"bstp_nmix_oprc\": \"2536.55\",\r\n            \"bstp_nmix_hgpr\": \"2543.83\",\r\n            \"bstp_nmix_lwpr\": \"2517.76\",\r\n            \"acml_vol_rlim\": \"75.15\",\r\n            \"acml_vol\": \"790177\",\r\n            \"acml_tr_pbmn\": \"8368766\",\r\n            \"invt_new_psdg\": \"-51.99\",\r\n            \"d20_dsrt\": \"97.84\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240111\",\r\n            \"bstp_nmix_prpr\": \"2540.27\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-1.71\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.07\",\r\n            \"bstp_nmix_oprc\": \"2543.03\",\r\n            \"bstp_nmix_hgpr\": \"2557.30\",\r\n            \"bstp_nmix_lwpr\": \"2540.27\",\r\n            \"acml_vol_rlim\": \"75.32\",\r\n            \"acml_vol\": \"788423\",\r\n            \"acml_tr_pbmn\": \"13669890\",\r\n            \"invt_new_psdg\": \"-35.84\",\r\n            \"d20_dsrt\": \"98.41\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240110\",\r\n            \"bstp_nmix_prpr\": \"2541.98\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-19.26\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.75\",\r\n            \"bstp_nmix_oprc\": \"2563.97\",\r\n            \"bstp_nmix_hgpr\": \"2568.19\",\r\n            \"bstp_nmix_lwpr\": \"2539.82\",\r\n            \"acml_vol_rlim\": \"104.18\",\r\n            \"acml_vol\": \"570021\",\r\n            \"acml_tr_pbmn\": \"8795835\",\r\n            \"invt_new_psdg\": \"-24.52\",\r\n            \"d20_dsrt\": \"98.50\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240109\",\r\n            \"bstp_nmix_prpr\": \"2561.24\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-6.58\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.26\",\r\n            \"bstp_nmix_oprc\": \"2598.31\",\r\n            \"bstp_nmix_hgpr\": \"2599.37\",\r\n            \"bstp_nmix_lwpr\": \"2556.00\",\r\n            \"acml_vol_rlim\": \"75.05\",\r\n            \"acml_vol\": \"791214\",\r\n            \"acml_tr_pbmn\": \"8896714\",\r\n            \"invt_new_psdg\": \"-20.81\",\r\n            \"d20_dsrt\": \"99.29\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240108\",\r\n            \"bstp_nmix_prpr\": \"2567.82\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-10.26\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.40\",\r\n            \"bstp_nmix_oprc\": \"2584.23\",\r\n            \"bstp_nmix_hgpr\": \"2591.68\",\r\n            \"bstp_nmix_lwpr\": \"2566.34\",\r\n            \"acml_vol_rlim\": \"185.49\",\r\n            \"acml_vol\": \"320144\",\r\n            \"acml_tr_pbmn\": \"6763632\",\r\n            \"invt_new_psdg\": \"-22.42\",\r\n            \"d20_dsrt\": \"99.68\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240105\",\r\n            \"bstp_nmix_prpr\": \"2578.08\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-8.94\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.35\",\r\n            \"bstp_nmix_oprc\": \"2586.89\",\r\n            \"bstp_nmix_hgpr\": \"2592.29\",\r\n            \"bstp_nmix_lwpr\": \"2572.60\",\r\n            \"acml_vol_rlim\": \"113.70\",\r\n            \"acml_vol\": \"522290\",\r\n            \"acml_tr_pbmn\": \"8384473\",\r\n            \"invt_new_psdg\": \"2.14\",\r\n            \"d20_dsrt\": \"100.22\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240104\",\r\n            \"bstp_nmix_prpr\": \"2587.02\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-20.29\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.78\",\r\n            \"bstp_nmix_oprc\": \"2592.44\",\r\n            \"bstp_nmix_hgpr\": \"2602.64\",\r\n            \"bstp_nmix_lwpr\": \"2580.09\",\r\n            \"acml_vol_rlim\": \"77.10\",\r\n            \"acml_vol\": \"770176\",\r\n            \"acml_tr_pbmn\": \"8992274\",\r\n            \"invt_new_psdg\": \"14.68\",\r\n            \"d20_dsrt\": \"100.73\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240103\",\r\n            \"bstp_nmix_prpr\": \"2607.31\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-62.50\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-2.34\",\r\n            \"bstp_nmix_oprc\": \"2643.54\",\r\n            \"bstp_nmix_hgpr\": \"2643.72\",\r\n            \"bstp_nmix_lwpr\": \"2607.31\",\r\n            \"acml_vol_rlim\": \"128.22\",\r\n            \"acml_vol\": \"463132\",\r\n            \"acml_tr_pbmn\": \"10121578\",\r\n            \"invt_new_psdg\": \"31.03\",\r\n            \"d20_dsrt\": \"101.67\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240102\",\r\n            \"bstp_nmix_prpr\": \"2669.81\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"14.53\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.55\",\r\n            \"bstp_nmix_oprc\": \"2645.47\",\r\n            \"bstp_nmix_hgpr\": \"2675.80\",\r\n            \"bstp_nmix_lwpr\": \"2641.88\",\r\n            \"acml_vol_rlim\": \"144.88\",\r\n            \"acml_vol\": \"409872\",\r\n            \"acml_tr_pbmn\": \"9628190\",\r\n            \"invt_new_psdg\": \"70.47\",\r\n            \"d20_dsrt\": \"104.31\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231228\",\r\n            \"bstp_nmix_prpr\": \"2655.28\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"41.78\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.60\",\r\n            \"bstp_nmix_oprc\": \"2616.27\",\r\n            \"bstp_nmix_hgpr\": \"2655.28\",\r\n            \"bstp_nmix_lwpr\": \"2611.72\",\r\n            \"acml_vol_rlim\": \"129.07\",\r\n            \"acml_vol\": \"460087\",\r\n            \"acml_tr_pbmn\": \"9418930\",\r\n            \"invt_new_psdg\": \"71.51\",\r\n            \"d20_dsrt\": \"104.02\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231227\",\r\n            \"bstp_nmix_prpr\": \"2613.50\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"10.91\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.42\",\r\n            \"bstp_nmix_oprc\": \"2599.35\",\r\n            \"bstp_nmix_hgpr\": \"2613.50\",\r\n            \"bstp_nmix_lwpr\": \"2590.08\",\r\n            \"acml_vol_rlim\": \"169.80\",\r\n            \"acml_vol\": \"349733\",\r\n            \"acml_tr_pbmn\": \"10359764\",\r\n            \"invt_new_psdg\": \"44.91\",\r\n            \"d20_dsrt\": \"102.65\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231226\",\r\n            \"bstp_nmix_prpr\": \"2602.59\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.08\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.12\",\r\n            \"bstp_nmix_oprc\": \"2609.44\",\r\n            \"bstp_nmix_hgpr\": \"2612.14\",\r\n            \"bstp_nmix_lwpr\": \"2594.65\",\r\n            \"acml_vol_rlim\": \"134.83\",\r\n            \"acml_vol\": \"440428\",\r\n            \"acml_tr_pbmn\": \"9582766\",\r\n            \"invt_new_psdg\": \"44.75\",\r\n            \"d20_dsrt\": \"102.41\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231222\",\r\n            \"bstp_nmix_prpr\": \"2599.51\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-0.51\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.02\",\r\n            \"bstp_nmix_oprc\": \"2617.72\",\r\n            \"bstp_nmix_hgpr\": \"2621.37\",\r\n            \"bstp_nmix_lwpr\": \"2599.51\",\r\n            \"acml_vol_rlim\": \"127.44\",\r\n            \"acml_vol\": \"465967\",\r\n            \"acml_tr_pbmn\": \"8848288\",\r\n            \"invt_new_psdg\": \"45.45\",\r\n            \"d20_dsrt\": \"102.50\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231221\",\r\n            \"bstp_nmix_prpr\": \"2600.02\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-14.28\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.55\",\r\n            \"bstp_nmix_oprc\": \"2598.37\",\r\n            \"bstp_nmix_hgpr\": \"2610.81\",\r\n            \"bstp_nmix_lwpr\": \"2587.16\",\r\n            \"acml_vol_rlim\": \"102.68\",\r\n            \"acml_vol\": \"578335\",\r\n            \"acml_tr_pbmn\": \"9467809\",\r\n            \"invt_new_psdg\": \"59.06\",\r\n            \"d20_dsrt\": \"102.73\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231220\",\r\n            \"bstp_nmix_prpr\": \"2614.30\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"45.75\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.78\",\r\n            \"bstp_nmix_oprc\": \"2586.99\",\r\n            \"bstp_nmix_hgpr\": \"2615.38\",\r\n            \"bstp_nmix_lwpr\": \"2584.85\",\r\n            \"acml_vol_rlim\": \"104.11\",\r\n            \"acml_vol\": \"570423\",\r\n            \"acml_tr_pbmn\": \"11202543\",\r\n            \"invt_new_psdg\": \"64.02\",\r\n            \"d20_dsrt\": \"103.47\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231219\",\r\n            \"bstp_nmix_prpr\": \"2568.55\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.69\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.07\",\r\n            \"bstp_nmix_oprc\": \"2564.81\",\r\n            \"bstp_nmix_hgpr\": \"2570.06\",\r\n            \"bstp_nmix_lwpr\": \"2556.52\",\r\n            \"acml_vol_rlim\": \"151.30\",\r\n            \"acml_vol\": \"392497\",\r\n            \"acml_tr_pbmn\": \"8418111\",\r\n            \"invt_new_psdg\": \"58.54\",\r\n            \"d20_dsrt\": \"101.87\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231218\",\r\n            \"bstp_nmix_prpr\": \"2566.86\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.30\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.13\",\r\n            \"bstp_nmix_oprc\": \"2568.77\",\r\n            \"bstp_nmix_hgpr\": \"2573.13\",\r\n            \"bstp_nmix_lwpr\": \"2556.05\",\r\n            \"acml_vol_rlim\": \"154.31\",\r\n            \"acml_vol\": \"384828\",\r\n            \"acml_tr_pbmn\": \"10181568\",\r\n            \"invt_new_psdg\": \"37.41\",\r\n            \"d20_dsrt\": \"101.92\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231215\",\r\n            \"bstp_nmix_prpr\": \"2563.56\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"19.38\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.76\",\r\n            \"bstp_nmix_oprc\": \"2558.44\",\r\n            \"bstp_nmix_hgpr\": \"2574.23\",\r\n            \"bstp_nmix_lwpr\": \"2555.30\",\r\n            \"acml_vol_rlim\": \"127.62\",\r\n            \"acml_vol\": \"465314\",\r\n            \"acml_tr_pbmn\": \"12873295\",\r\n            \"invt_new_psdg\": \"38.80\",\r\n            \"d20_dsrt\": \"101.94\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231214\",\r\n            \"bstp_nmix_prpr\": \"2544.18\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"33.52\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.34\",\r\n            \"bstp_nmix_oprc\": \"2547.74\",\r\n            \"bstp_nmix_hgpr\": \"2549.65\",\r\n            \"bstp_nmix_lwpr\": \"2532.16\",\r\n            \"acml_vol_rlim\": \"112.02\",\r\n            \"acml_vol\": \"530124\",\r\n            \"acml_tr_pbmn\": \"12960671\",\r\n            \"invt_new_psdg\": \"12.67\",\r\n            \"d20_dsrt\": \"101.36\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231213\",\r\n            \"bstp_nmix_prpr\": \"2510.66\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-24.61\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.97\",\r\n            \"bstp_nmix_oprc\": \"2531.23\",\r\n            \"bstp_nmix_hgpr\": \"2531.23\",\r\n            \"bstp_nmix_lwpr\": \"2509.89\",\r\n            \"acml_vol_rlim\": \"157.13\",\r\n            \"acml_vol\": \"377934\",\r\n            \"acml_tr_pbmn\": \"7513617\",\r\n            \"invt_new_psdg\": \"6.92\",\r\n            \"d20_dsrt\": \"100.13\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231212\",\r\n            \"bstp_nmix_prpr\": \"2535.27\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.91\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.39\",\r\n            \"bstp_nmix_oprc\": \"2535.11\",\r\n            \"bstp_nmix_hgpr\": \"2543.06\",\r\n            \"bstp_nmix_lwpr\": \"2529.74\",\r\n            \"acml_vol_rlim\": \"157.09\",\r\n            \"acml_vol\": \"378034\",\r\n            \"acml_tr_pbmn\": \"7732530\",\r\n            \"invt_new_psdg\": \"15.36\",\r\n            \"d20_dsrt\": \"101.16\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231211\",\r\n            \"bstp_nmix_prpr\": \"2525.36\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"7.51\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.30\",\r\n            \"bstp_nmix_oprc\": \"2524.79\",\r\n            \"bstp_nmix_hgpr\": \"2528.89\",\r\n            \"bstp_nmix_lwpr\": \"2512.45\",\r\n            \"acml_vol_rlim\": \"136.51\",\r\n            \"acml_vol\": \"435004\",\r\n            \"acml_tr_pbmn\": \"8260508\",\r\n            \"invt_new_psdg\": \"20.45\",\r\n            \"d20_dsrt\": \"100.97\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231208\",\r\n            \"bstp_nmix_prpr\": \"2517.85\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"25.78\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.03\",\r\n            \"bstp_nmix_oprc\": \"2510.24\",\r\n            \"bstp_nmix_hgpr\": \"2521.58\",\r\n            \"bstp_nmix_lwpr\": \"2507.14\",\r\n            \"acml_vol_rlim\": \"137.53\",\r\n            \"acml_vol\": \"431797\",\r\n            \"acml_tr_pbmn\": \"7916793\",\r\n            \"invt_new_psdg\": \"7.83\",\r\n            \"d20_dsrt\": \"100.92\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231207\",\r\n            \"bstp_nmix_prpr\": \"2492.07\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-3.31\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.13\",\r\n            \"bstp_nmix_oprc\": \"2493.14\",\r\n            \"bstp_nmix_hgpr\": \"2499.73\",\r\n            \"bstp_nmix_lwpr\": \"2481.00\",\r\n            \"acml_vol_rlim\": \"132.89\",\r\n            \"acml_vol\": \"446877\",\r\n            \"acml_tr_pbmn\": \"8127636\",\r\n            \"invt_new_psdg\": \"-18.93\",\r\n            \"d20_dsrt\": \"100.10\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231206\",\r\n            \"bstp_nmix_prpr\": \"2495.38\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.10\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.04\",\r\n            \"bstp_nmix_oprc\": \"2503.57\",\r\n            \"bstp_nmix_hgpr\": \"2509.67\",\r\n            \"bstp_nmix_lwpr\": \"2495.38\",\r\n            \"acml_vol_rlim\": \"151.88\",\r\n            \"acml_vol\": \"390989\",\r\n            \"acml_tr_pbmn\": \"7685320\",\r\n            \"invt_new_psdg\": \"-6.37\",\r\n            \"d20_dsrt\": \"100.37\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231205\",\r\n            \"bstp_nmix_prpr\": \"2494.28\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-20.67\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.82\",\r\n            \"bstp_nmix_oprc\": \"2507.45\",\r\n            \"bstp_nmix_hgpr\": \"2509.74\",\r\n            \"bstp_nmix_lwpr\": \"2492.55\",\r\n            \"acml_vol_rlim\": \"139.05\",\r\n            \"acml_vol\": \"427067\",\r\n            \"acml_tr_pbmn\": \"8300522\",\r\n            \"invt_new_psdg\": \"-6.29\",\r\n            \"d20_dsrt\": \"100.47\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231204\",\r\n            \"bstp_nmix_prpr\": \"2514.95\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.94\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.40\",\r\n            \"bstp_nmix_oprc\": \"2522.22\",\r\n            \"bstp_nmix_hgpr\": \"2525.63\",\r\n            \"bstp_nmix_lwpr\": \"2510.52\",\r\n            \"acml_vol_rlim\": \"119.04\",\r\n            \"acml_vol\": \"498861\",\r\n            \"acml_tr_pbmn\": \"8772367\",\r\n            \"invt_new_psdg\": \"19.36\",\r\n            \"d20_dsrt\": \"101.41\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231201\",\r\n            \"bstp_nmix_prpr\": \"2505.01\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-30.28\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.19\",\r\n            \"bstp_nmix_oprc\": \"2520.49\",\r\n            \"bstp_nmix_hgpr\": \"2520.49\",\r\n            \"bstp_nmix_lwpr\": \"2504.06\",\r\n            \"acml_vol_rlim\": \"114.95\",\r\n            \"acml_vol\": \"516596\",\r\n            \"acml_tr_pbmn\": \"8837750\",\r\n            \"invt_new_psdg\": \"22.72\",\r\n            \"d20_dsrt\": \"101.03\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231130\",\r\n            \"bstp_nmix_prpr\": \"2535.29\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"15.48\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.61\",\r\n            \"bstp_nmix_oprc\": \"2512.11\",\r\n            \"bstp_nmix_hgpr\": \"2535.29\",\r\n            \"bstp_nmix_lwpr\": \"2507.80\",\r\n            \"acml_vol_rlim\": \"89.40\",\r\n            \"acml_vol\": \"664284\",\r\n            \"acml_tr_pbmn\": \"11992488\",\r\n            \"invt_new_psdg\": \"28.65\",\r\n            \"d20_dsrt\": \"102.54\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231129\",\r\n            \"bstp_nmix_prpr\": \"2519.81\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-1.95\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.08\",\r\n            \"bstp_nmix_oprc\": \"2518.80\",\r\n            \"bstp_nmix_hgpr\": \"2523.98\",\r\n            \"bstp_nmix_lwpr\": \"2501.44\",\r\n            \"acml_vol_rlim\": \"102.52\",\r\n            \"acml_vol\": \"579271\",\r\n            \"acml_tr_pbmn\": \"9428200\",\r\n            \"invt_new_psdg\": \"24.76\",\r\n            \"d20_dsrt\": \"102.31\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231128\",\r\n            \"bstp_nmix_prpr\": \"2521.76\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"26.10\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.05\",\r\n            \"bstp_nmix_oprc\": \"2506.14\",\r\n            \"bstp_nmix_hgpr\": \"2522.45\",\r\n            \"bstp_nmix_lwpr\": \"2502.26\",\r\n            \"acml_vol_rlim\": \"134.02\",\r\n            \"acml_vol\": \"443090\",\r\n            \"acml_tr_pbmn\": \"8753424\",\r\n            \"invt_new_psdg\": \"47.02\",\r\n            \"d20_dsrt\": \"102.84\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231127\",\r\n            \"bstp_nmix_prpr\": \"2495.66\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-0.97\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.04\",\r\n            \"bstp_nmix_oprc\": \"2501.83\",\r\n            \"bstp_nmix_hgpr\": \"2511.37\",\r\n            \"bstp_nmix_lwpr\": \"2489.18\",\r\n            \"acml_vol_rlim\": \"162.81\",\r\n            \"acml_vol\": \"364744\",\r\n            \"acml_tr_pbmn\": \"8376476\",\r\n            \"invt_new_psdg\": \"47.49\",\r\n            \"d20_dsrt\": \"102.29\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231124\",\r\n            \"bstp_nmix_prpr\": \"2496.63\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-18.33\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.73\",\r\n            \"bstp_nmix_oprc\": \"2517.88\",\r\n            \"bstp_nmix_hgpr\": \"2521.56\",\r\n            \"bstp_nmix_lwpr\": \"2496.63\",\r\n            \"acml_vol_rlim\": \"165.24\",\r\n            \"acml_vol\": \"359383\",\r\n            \"acml_tr_pbmn\": \"6537961\",\r\n            \"invt_new_psdg\": \"45.27\",\r\n            \"d20_dsrt\": \"102.71\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231123\",\r\n            \"bstp_nmix_prpr\": \"2514.96\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"3.26\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.13\",\r\n            \"bstp_nmix_oprc\": \"2515.83\",\r\n            \"bstp_nmix_hgpr\": \"2522.20\",\r\n            \"bstp_nmix_lwpr\": \"2507.30\",\r\n            \"acml_vol_rlim\": \"164.56\",\r\n            \"acml_vol\": \"360874\",\r\n            \"acml_tr_pbmn\": \"6577868\",\r\n            \"invt_new_psdg\": \"45.67\",\r\n            \"d20_dsrt\": \"103.88\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231122\",\r\n            \"bstp_nmix_prpr\": \"2511.70\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.28\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.05\",\r\n            \"bstp_nmix_oprc\": \"2493.17\",\r\n            \"bstp_nmix_hgpr\": \"2516.72\",\r\n            \"bstp_nmix_lwpr\": \"2490.43\",\r\n            \"acml_vol_rlim\": \"135.12\",\r\n            \"acml_vol\": \"439486\",\r\n            \"acml_tr_pbmn\": \"7755316\",\r\n            \"invt_new_psdg\": \"45.98\",\r\n            \"d20_dsrt\": \"104.21\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231121\",\r\n            \"bstp_nmix_prpr\": \"2510.42\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"19.22\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.77\",\r\n            \"bstp_nmix_oprc\": \"2504.70\",\r\n            \"bstp_nmix_hgpr\": \"2517.74\",\r\n            \"bstp_nmix_lwpr\": \"2500.91\",\r\n            \"acml_vol_rlim\": \"172.10\",\r\n            \"acml_vol\": \"345055\",\r\n            \"acml_tr_pbmn\": \"7713377\",\r\n            \"invt_new_psdg\": \"27.09\",\r\n            \"d20_dsrt\": \"104.48\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231120\",\r\n            \"bstp_nmix_prpr\": \"2491.20\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"21.35\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.86\",\r\n            \"bstp_nmix_oprc\": \"2464.72\",\r\n            \"bstp_nmix_hgpr\": \"2499.75\",\r\n            \"bstp_nmix_lwpr\": \"2464.04\",\r\n            \"acml_vol_rlim\": \"183.39\",\r\n            \"acml_vol\": \"323806\",\r\n            \"acml_tr_pbmn\": \"6586445\",\r\n            \"invt_new_psdg\": \"-2.39\",\r\n            \"d20_dsrt\": \"103.96\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231117\",\r\n            \"bstp_nmix_prpr\": \"2469.85\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-18.33\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.74\",\r\n            \"bstp_nmix_oprc\": \"2477.43\",\r\n            \"bstp_nmix_hgpr\": \"2481.10\",\r\n            \"bstp_nmix_lwpr\": \"2463.59\",\r\n            \"acml_vol_rlim\": \"152.67\",\r\n            \"acml_vol\": \"388974\",\r\n            \"acml_tr_pbmn\": \"8129523\",\r\n            \"invt_new_psdg\": \"14.66\",\r\n            \"d20_dsrt\": \"103.35\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231116\",\r\n            \"bstp_nmix_prpr\": \"2488.18\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"1.51\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.06\",\r\n            \"bstp_nmix_oprc\": \"2483.48\",\r\n            \"bstp_nmix_hgpr\": \"2491.98\",\r\n            \"bstp_nmix_lwpr\": \"2472.69\",\r\n            \"acml_vol_rlim\": \"145.75\",\r\n            \"acml_vol\": \"407441\",\r\n            \"acml_tr_pbmn\": \"6806414\",\r\n            \"invt_new_psdg\": \"30.54\",\r\n            \"d20_dsrt\": \"104.33\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231115\",\r\n            \"bstp_nmix_prpr\": \"2486.67\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"53.42\",\r\n            \"bstp_nmix_prdy_ctrt\": \"2.20\",\r\n            \"bstp_nmix_oprc\": \"2482.21\",\r\n            \"bstp_nmix_hgpr\": \"2487.42\",\r\n            \"bstp_nmix_lwpr\": \"2468.43\",\r\n            \"acml_vol_rlim\": \"141.44\",\r\n            \"acml_vol\": \"419843\",\r\n            \"acml_tr_pbmn\": \"9328219\",\r\n            \"invt_new_psdg\": \"33.54\",\r\n            \"d20_dsrt\": \"104.42\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231114\",\r\n            \"bstp_nmix_prpr\": \"2433.25\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"29.49\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.23\",\r\n            \"bstp_nmix_oprc\": \"2424.93\",\r\n            \"bstp_nmix_hgpr\": \"2442.37\",\r\n            \"bstp_nmix_lwpr\": \"2422.97\",\r\n            \"acml_vol_rlim\": \"193.46\",\r\n            \"acml_vol\": \"306964\",\r\n            \"acml_tr_pbmn\": \"6382101\",\r\n            \"invt_new_psdg\": \"31.36\",\r\n            \"d20_dsrt\": \"102.23\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231113\",\r\n            \"bstp_nmix_prpr\": \"2403.76\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-5.90\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.24\",\r\n            \"bstp_nmix_oprc\": \"2431.24\",\r\n            \"bstp_nmix_hgpr\": \"2435.32\",\r\n            \"bstp_nmix_lwpr\": \"2399.04\",\r\n            \"acml_vol_rlim\": \"193.36\",\r\n            \"acml_vol\": \"307123\",\r\n            \"acml_tr_pbmn\": \"5934173\",\r\n            \"invt_new_psdg\": \"12.72\",\r\n            \"d20_dsrt\": \"100.94\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231110\",\r\n            \"bstp_nmix_prpr\": \"2409.66\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-17.42\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.72\",\r\n            \"bstp_nmix_oprc\": \"2406.40\",\r\n            \"bstp_nmix_hgpr\": \"2413.62\",\r\n            \"bstp_nmix_lwpr\": \"2393.64\",\r\n            \"acml_vol_rlim\": \"190.05\",\r\n            \"acml_vol\": \"312468\",\r\n            \"acml_tr_pbmn\": \"5825602\",\r\n            \"invt_new_psdg\": \"24.51\",\r\n            \"d20_dsrt\": \"101.12\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231109\",\r\n            \"bstp_nmix_prpr\": \"2427.08\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"5.46\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.23\",\r\n            \"bstp_nmix_oprc\": \"2425.93\",\r\n            \"bstp_nmix_hgpr\": \"2437.90\",\r\n            \"bstp_nmix_lwpr\": \"2413.04\",\r\n            \"acml_vol_rlim\": \"150.33\",\r\n            \"acml_vol\": \"395031\",\r\n            \"acml_tr_pbmn\": \"7288448\",\r\n            \"invt_new_psdg\": \"38.05\",\r\n            \"d20_dsrt\": \"101.75\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231108\",\r\n            \"bstp_nmix_prpr\": \"2421.62\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-22.34\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.91\",\r\n            \"bstp_nmix_oprc\": \"2460.22\",\r\n            \"bstp_nmix_hgpr\": \"2468.43\",\r\n            \"bstp_nmix_lwpr\": \"2418.14\",\r\n            \"acml_vol_rlim\": \"127.10\",\r\n            \"acml_vol\": \"467218\",\r\n            \"acml_tr_pbmn\": \"7667332\",\r\n            \"invt_new_psdg\": \"17.07\",\r\n            \"d20_dsrt\": \"101.41\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231107\",\r\n            \"bstp_nmix_prpr\": \"2443.96\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_vrss\": \"-58.41\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-2.33\",\r\n            \"bstp_nmix_oprc\": \"2476.35\",\r\n            \"bstp_nmix_hgpr\": \"2476.35\",\r\n            \"bstp_nmix_lwpr\": \"2418.74\",\r\n            \"acml_vol_rlim\": \"129.75\",\r\n            \"acml_vol\": \"457676\",\r\n            \"acml_tr_pbmn\": \"12086570\",\r\n            \"invt_new_psdg\": \"17.35\",\r\n            \"d20_dsrt\": \"102.28\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231106\",\r\n            \"bstp_nmix_prpr\": \"2502.37\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"134.03\",\r\n            \"bstp_nmix_prdy_ctrt\": \"5.66\",\r\n            \"bstp_nmix_oprc\": \"2399.80\",\r\n            \"bstp_nmix_hgpr\": \"2502.37\",\r\n            \"bstp_nmix_lwpr\": \"2395.03\",\r\n            \"acml_vol_rlim\": \"112.35\",\r\n            \"acml_vol\": \"528585\",\r\n            \"acml_tr_pbmn\": \"15225480\",\r\n            \"invt_new_psdg\": \"39.16\",\r\n            \"d20_dsrt\": \"104.82\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231103\",\r\n            \"bstp_nmix_prpr\": \"2368.34\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"25.22\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.08\",\r\n            \"bstp_nmix_oprc\": \"2365.59\",\r\n            \"bstp_nmix_hgpr\": \"2370.28\",\r\n            \"bstp_nmix_lwpr\": \"2351.83\",\r\n            \"acml_vol_rlim\": \"102.62\",\r\n            \"acml_vol\": \"578662\",\r\n            \"acml_tr_pbmn\": \"8040958\",\r\n            \"invt_new_psdg\": \"8.74\",\r\n            \"d20_dsrt\": \"99.40\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20231102\",\r\n            \"bstp_nmix_prpr\": \"2343.12\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_vrss\": \"41.56\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.81\",\r\n            \"bstp_nmix_oprc\": \"2334.96\",\r\n            \"bstp_nmix_hgpr\": \"2351.91\",\r\n            \"bstp_nmix_lwpr\": \"2333.41\",\r\n            \"acml_vol_rlim\": \"157.33\",\r\n            \"acml_vol\": \"377462\",\r\n            \"acml_tr_pbmn\": \"7679305\",\r\n            \"invt_new_psdg\": \"-13.03\",",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST07020000",
    "name": "금리 종합(국내채권_금리)",
    "url": "/uapi/domestic-stock/v1/quotations/comp-interest",
    "sheet": "금리 종합(국내채권_금리)",
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
        "element": "bcdt_code",
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
        "element": "bond_mnrt_prpr",
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
        "element": "bond_mnrt_prdy_vrss",
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
        "element": "stck_bsop_date",
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
        "element": "bcdt_code",
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
        "element": "bond_mnrt_prpr",
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
        "element": "bond_mnrt_prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:I\r\nFID_COND_SCR_DIV_CODE:20702\r\nFID_DIV_CLS_CODE:1\r\nFID_DIV_CLS_CODE1:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": [\r\n        {\r\n            \"bcdt_code\": \"Y0201\",\r\n            \"hts_kor_isnm\": \"미국 30년T-BOND\",\r\n            \"bond_mnrt_prpr\": \"4.6500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0100\",\r\n            \"prdy_ctrt\": \"0.22\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0202\",\r\n            \"hts_kor_isnm\": \"미국 10년T-NOTE 수익률\",\r\n            \"bond_mnrt_prpr\": \"4.5600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0100\",\r\n            \"prdy_ctrt\": \"0.22\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0203\",\r\n            \"hts_kor_isnm\": \"미국 1년T-BILL\",\r\n            \"bond_mnrt_prpr\": \"5.1700\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0200\",\r\n            \"prdy_ctrt\": \"-0.39\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0204\",\r\n            \"hts_kor_isnm\": \"미국 연방기금금리(콜)\",\r\n            \"bond_mnrt_prpr\": \"5.3300\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0000\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"stck_bsop_date\": \"20240410\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0205\",\r\n            \"hts_kor_isnm\": \"미국 재할인률\",\r\n            \"bond_mnrt_prpr\": \"5.5000\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0000\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"stck_bsop_date\": \"20240410\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0206\",\r\n            \"hts_kor_isnm\": \"미국 단기우대금리\",\r\n            \"bond_mnrt_prpr\": \"8.5000\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0000\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"stck_bsop_date\": \"20240410\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0207\",\r\n            \"hts_kor_isnm\": \"일본 10년 국채수익률\",\r\n            \"bond_mnrt_prpr\": \"0.8540\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0530\",\r\n            \"prdy_ctrt\": \"6.62\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        }\r\n    ],\r\n    \"output2\": [\r\n        {\r\n            \"bcdt_code\": \"Y0101\",\r\n            \"hts_kor_isnm\": \"국고채 3년\",\r\n            \"bond_mnrt_prpr\": \"3.4080\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0580\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.67\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0102\",\r\n            \"hts_kor_isnm\": \"회사채 무보증 3년AA-\",\r\n            \"bond_mnrt_prpr\": \"3.9630\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0530\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.32\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0103\",\r\n            \"hts_kor_isnm\": \"회사채 3년 BBB-\",\r\n            \"bond_mnrt_prpr\": \"10.1690\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0510\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.50\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0104\",\r\n            \"hts_kor_isnm\": \"국고채 1년\",\r\n            \"bond_mnrt_prpr\": \"3.4360\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0220\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.64\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0105\",\r\n            \"hts_kor_isnm\": \"국고채 5년\",\r\n            \"bond_mnrt_prpr\": \"3.4690\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0420\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.20\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0106\",\r\n            \"hts_kor_isnm\": \"국고채 10년\",\r\n            \"bond_mnrt_prpr\": \"3.5460\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0390\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.09\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0107\",\r\n            \"hts_kor_isnm\": \"국민주택1종 (5년)\",\r\n            \"bond_mnrt_prpr\": \"3.6010\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0390\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.07\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0108\",\r\n            \"hts_kor_isnm\": \"한전채(3년)\",\r\n            \"bond_mnrt_prpr\": \"3.7120\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0490\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.30\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0109\",\r\n            \"hts_kor_isnm\": \"통안증권(364일)\",\r\n            \"bond_mnrt_prpr\": \"3.3710\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0250\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.74\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0110\",\r\n            \"hts_kor_isnm\": \"통안증권(2년)\",\r\n            \"bond_mnrt_prpr\": \"3.4190\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0500\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.44\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0111\",\r\n            \"hts_kor_isnm\": \"산금채(1년)\",\r\n            \"bond_mnrt_prpr\": \"3.5560\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0280\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.78\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0112\",\r\n            \"hts_kor_isnm\": \"C D (91일)\",\r\n            \"bond_mnrt_prpr\": \"3.5600\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0100\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.28\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0113\",\r\n            \"hts_kor_isnm\": \"C P (91일)\",\r\n            \"bond_mnrt_prpr\": \"4.1800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0100\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.24\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0114\",\r\n            \"hts_kor_isnm\": \"콜 (1일)\",\r\n            \"bond_mnrt_prpr\": \"3.5000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0400\",\r\n            \"bstp_nmix_prdy_ctrt\": \"1.16\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0115\",\r\n            \"hts_kor_isnm\": \"종합채권지수\",\r\n            \"bond_mnrt_prpr\": \"102.8100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.3400\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.33\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0116\",\r\n            \"hts_kor_isnm\": \"국고채 20년\",\r\n            \"bond_mnrt_prpr\": \"3.4640\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0310\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.89\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0117\",\r\n            \"hts_kor_isnm\": \"국고채 30년\",\r\n            \"bond_mnrt_prpr\": \"3.3640\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bond_mnrt_prdy_vrss\": \"-0.0240\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-0.71\",\r\n            \"stck_bsop_date\": \"20240412\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0198\",\r\n            \"hts_kor_isnm\": \"Call 지수\",\r\n            \"bond_mnrt_prpr\": \"190.2051\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0185\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.01\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        },\r\n        {\r\n            \"bcdt_code\": \"Y0199\",\r\n            \"hts_kor_isnm\": \"CD AAA 3개월(13주)\",\r\n            \"bond_mnrt_prpr\": \"203.2972\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bond_mnrt_prdy_vrss\": \"0.0198\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.01\",\r\n            \"stck_bsop_date\": \"20240411\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01390000",
    "name": "변동성완화장치(VI) 현황",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-vi-status",
    "sheet": "변동성완화장치(VI) 현황",
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
        "element": "vi_cls_code",
        "type": "string",
        "required": "Y",
        "description": "Y: 발동 / N: 해제"
      },
      {
        "element": "bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cntg_vi_hour",
        "type": "string",
        "required": "Y",
        "description": "VI발동시간"
      },
      {
        "element": "vi_cncl_hour",
        "type": "string",
        "required": "Y",
        "description": "VI해제시간"
      },
      {
        "element": "vi_kind_code",
        "type": "string",
        "required": "Y",
        "description": "1:정적 2:동적 3:정적&동적"
      },
      {
        "element": "vi_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vi_stnd_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vi_dprt",
        "type": "string",
        "required": "Y",
        "description": "%"
      },
      {
        "element": "vi_dmc_stnd_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vi_dmc_dprt",
        "type": "string",
        "required": "Y",
        "description": "%"
      },
      {
        "element": "vi_count",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\t\"fid_cond_scr_div_code\":\"20139\",\r\n\t\"fid_mrkt_cls_code\":\"0\",\r\n\t\"fid_input_iscd\":\"\",\r\n\t\"fid_rank_sort_cls_code\":\"0\",\r\n\t\"fid_input_date_1\":\"20240126\",\r\n\t\"fid_trgt_cls_code\":\"\",\r\n\t\"fid_trgt_exls_cls_code\":\"\",\r\n\t\"fid_div_cls_code\":\"0\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"hts_kor_isnm\": \"KODEX Fn멀티팩터\",\r\n            \"mksc_shrn_iscd\": \"337120\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"174012\",\r\n            \"vi_cncl_hour\": \"174212\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"12135\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"13275\",\r\n            \"vi_dmc_dprt\": \"-8.59\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"루멘스\",\r\n            \"mksc_shrn_iscd\": \"038060\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"174008\",\r\n            \"vi_cncl_hour\": \"174210\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"1337\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"1241\",\r\n            \"vi_dmc_dprt\": \"7.74\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"DL건설\",\r\n            \"mksc_shrn_iscd\": \"001880\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"173030\",\r\n            \"vi_cncl_hour\": \"173234\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"14000\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"14990\",\r\n            \"vi_dmc_dprt\": \"-6.60\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"성창기업지주\",\r\n            \"mksc_shrn_iscd\": \"000180\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"173030\",\r\n            \"vi_cncl_hour\": \"173224\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"1860\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"1992\",\r\n            \"vi_dmc_dprt\": \"-6.63\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"성창기업지주\",\r\n            \"mksc_shrn_iscd\": \"000180\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"172030\",\r\n            \"vi_cncl_hour\": \"172204\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"1992\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"1857\",\r\n            \"vi_dmc_dprt\": \"7.27\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"유아이디\",\r\n            \"mksc_shrn_iscd\": \"069330\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"172030\",\r\n            \"vi_cncl_hour\": \"172234\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"1640\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"1490\",\r\n            \"vi_dmc_dprt\": \"10.07\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"뷰웍스\",\r\n            \"mksc_shrn_iscd\": \"100120\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"172010\",\r\n            \"vi_cncl_hour\": \"172208\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"27700\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"29700\",\r\n            \"vi_dmc_dprt\": \"-6.73\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"TIGER 미국배당+3%프리미엄다우존스\",\r\n            \"mksc_shrn_iscd\": \"458750\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"171030\",\r\n            \"vi_cncl_hour\": \"171212\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"11700\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"10675\",\r\n            \"vi_dmc_dprt\": \"9.60\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"아스타\",\r\n            \"mksc_shrn_iscd\": \"246720\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"171030\",\r\n            \"vi_cncl_hour\": \"171253\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"5100\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"5490\",\r\n            \"vi_dmc_dprt\": \"-7.10\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"제일전기공업\",\r\n            \"mksc_shrn_iscd\": \"199820\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"170030\",\r\n            \"vi_cncl_hour\": \"170232\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"10050\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"9350\",\r\n            \"vi_dmc_dprt\": \"7.49\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"파인디지털\",\r\n            \"mksc_shrn_iscd\": \"038950\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"170030\",\r\n            \"vi_cncl_hour\": \"170244\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"5200\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"4800\",\r\n            \"vi_dmc_dprt\": \"8.33\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"엔시트론\",\r\n            \"mksc_shrn_iscd\": \"101400\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"170013\",\r\n            \"vi_cncl_hour\": \"170218\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"644\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"604\",\r\n            \"vi_dmc_dprt\": \"6.62\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"TIGER 2차전지TOP10\",\r\n            \"mksc_shrn_iscd\": \"364980\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"165030\",\r\n            \"vi_cncl_hour\": \"165250\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"12450\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"13740\",\r\n            \"vi_dmc_dprt\": \"-9.39\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"지니너스\",\r\n            \"mksc_shrn_iscd\": \"389030\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"165030\",\r\n            \"vi_cncl_hour\": \"165222\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"2270\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"2125\",\r\n            \"vi_dmc_dprt\": \"6.82\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"패션플랫폼\",\r\n            \"mksc_shrn_iscd\": \"225590\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"165030\",\r\n            \"vi_cncl_hour\": \"165228\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"1263\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"1153\",\r\n            \"vi_dmc_dprt\": \"9.54\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"씨엔플러스\",\r\n            \"mksc_shrn_iscd\": \"115530\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"165030\",\r\n            \"vi_cncl_hour\": \"165240\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"344\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"368\",\r\n            \"vi_dmc_dprt\": \"-6.52\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"케이비제22호스팩\",\r\n            \"mksc_shrn_iscd\": \"436530\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"164030\",\r\n            \"vi_cncl_hour\": \"164208\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"4455\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"4795\",\r\n            \"vi_dmc_dprt\": \"-7.09\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"제너셈\",\r\n            \"mksc_shrn_iscd\": \"217190\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"164030\",\r\n            \"vi_cncl_hour\": \"164230\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"14980\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"15990\",\r\n            \"vi_dmc_dprt\": \"-6.32\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"아스타\",\r\n            \"mksc_shrn_iscd\": \"246720\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"163030\",\r\n            \"vi_cncl_hour\": \"163220\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"5550\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"5090\",\r\n            \"vi_dmc_dprt\": \"9.04\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"세니젠\",\r\n            \"mksc_shrn_iscd\": \"188260\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"163030\",\r\n            \"vi_cncl_hour\": \"163252\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"3955\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"4230\",\r\n            \"vi_dmc_dprt\": \"-6.50\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"KODEX Fn멀티팩터\",\r\n            \"mksc_shrn_iscd\": \"337120\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"163024\",\r\n            \"vi_cncl_hour\": \"163250\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"13280\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"12075\",\r\n            \"vi_dmc_dprt\": \"9.98\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"ES큐브\",\r\n            \"mksc_shrn_iscd\": \"050120\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"163017\",\r\n            \"vi_cncl_hour\": \"163228\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"3055\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"2860\",\r\n            \"vi_dmc_dprt\": \"6.82\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"무학\",\r\n            \"mksc_shrn_iscd\": \"033920\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162030\",\r\n            \"vi_cncl_hour\": \"162241\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"5220\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"4880\",\r\n            \"vi_dmc_dprt\": \"6.97\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"아이씨에이치\",\r\n            \"mksc_shrn_iscd\": \"368600\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162030\",\r\n            \"vi_cncl_hour\": \"162210\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"5860\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"5460\",\r\n            \"vi_dmc_dprt\": \"7.33\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"KBSTAR 2차전지TOP10\",\r\n            \"mksc_shrn_iscd\": \"465330\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162030\",\r\n            \"vi_cncl_hour\": \"162217\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"14475\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"13485\",\r\n            \"vi_dmc_dprt\": \"7.34\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"제너셈\",\r\n            \"mksc_shrn_iscd\": \"217190\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162030\",\r\n            \"vi_cncl_hour\": \"162232\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"15990\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"14910\",\r\n            \"vi_dmc_dprt\": \"7.24\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"알엔투테크놀로지\",\r\n            \"mksc_shrn_iscd\": \"148250\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162030\",\r\n            \"vi_cncl_hour\": \"162212\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"5390\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"4915\",\r\n            \"vi_dmc_dprt\": \"9.66\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"엑서지21\",\r\n            \"mksc_shrn_iscd\": \"043090\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162030\",\r\n            \"vi_cncl_hour\": \"162206\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"463\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"507\",\r\n            \"vi_dmc_dprt\": \"-8.68\",\r\n            \"vi_count\": \"2\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"DL건설\",\r\n            \"mksc_shrn_iscd\": \"001880\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162028\",\r\n            \"vi_cncl_hour\": \"162214\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"15010\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"14000\",\r\n            \"vi_dmc_dprt\": \"7.21\",\r\n            \"vi_count\": \"1\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"뷰웍스\",\r\n            \"mksc_shrn_iscd\": \"100120\",\r\n            \"vi_cls_code\": \"N\",\r\n            \"bsop_date\": \"20240126\",\r\n            \"cntg_vi_hour\": \"162015\",\r\n            \"vi_cncl_hour\": \"162207\",\r\n            \"vi_kind_code\": \"2\",\r\n            \"vi_prc\": \"27600\",\r\n            \"vi_stnd_prc\": \"0\",\r\n            \"vi_dprt\": \"0.00\",\r\n            \"vi_dmc_stnd_prc\": \"29700\",\r\n            \"vi_dmc_dprt\": \"-7.07\",\r\n            \"vi_count\": \"1\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST01011800",
    "name": "종합 시황_공시(제목)",
    "url": "/uapi/domestic-stock/v1/quotations/news-title",
    "sheet": "종합 시황_공시(제목)",
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
        "element": "cntt_usiq_srno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "news_ofer_entp_code",
        "type": "string",
        "required": "Y",
        "description": "'2'  /* 한경  news  */\r\n'3'  /* 사용안함 */\r\n'4'  /* 이데일리    */\r\n'5'  /* 머니투데이  */\r\n'6'  /* 연합뉴스    */\r\n'7'  /* 인포스탁    */\r\n'8'  /* 아시아경제  */\r\n'9'  /* 뉴스핌      */\r\n'A'  /* 매일경제    */\r\n'B'  /* 헤럴드경제  */\r\n'C'  /* 파이낸셜    */\r\n'D'  /* 이투데이    */\r\n'F'  /* 장내공시    */\r\n'G'  /* 코스닥공시  */\r\n'H'  /* 프리보드공시*/\r\n'I'  /* 기타공시    */\r\n'N'  /* 코넥스공시  */\r\n'J'  /*  동향       */ /*  'L'   리서치 */\r\n'K'  /* 청약안내 전송             */\r\n'M'  /* 타사 추천종목             */\r\n'O'  /* edaily  fx                */\r\n'U'  /* 서울 경제 */\r\n'V'  /* 조선 경제 */\r\n'X'  /* CEO스코어               */\r\n'Y'  /* 이프렌드 Air 뉴스       */\r\n'Z'  /* 인베스트조선            */\r\n'd'  /* NSP통신              */"
      },
      {
        "element": "data_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "data_tm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_pbnt_titl_cntt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "news_lrdv_code",
        "type": "string",
        "required": "Y",
        "description": "1:0:종합\r\n1:FGHIN:공시\r\n2:F:거래소\r\n3:01:수시공시\r\n3:02:공정공시\r\n3:03:시장조치\r\n3:04:신고사항\r\n3:05:정기공시 \r\n3:06:특수공시  \r\n3:07:발행공시  \r\n3:08:지분공시\r\n3:09:워런트공시\r\n3:10:의결권행사공시\r\n3:11:공정위공시\r\n3:12:선물시장공시\r\n3:A1:시장조치안내\r\n3:A2:상장안내\r\n3:A3:안내사항\r\n3:A4:투자유의사항\r\n3:A5:수익증권\r\n3:A6:투자자참고사항\r\n3:A7:뮤츄얼펀드\r\n2:G:코스닥\r\n3:01:수시공시\r\n3:02:공정공시\r\n3:03:시장조치\r\n3:04:신고사항\r\n3:05:정기공시 \r\n3:06:특수공시  \r\n3:07:발행공시  \r\n3:08:지분공시\r\n3:09:워런트공시\r\n3:10:의결권행사공시\r\n3:11:공정위공시\r\n3:12:선물시장공시\r\n3:A1:시장조치안내\r\n3:A2:상장안내\r\n3:A3:안내사항\r\n3:A4:투자유의사항\r\n3:A5:수익증권\r\n3:A6:투자자참고사항\r\n3:A7:뮤츄얼펀드\r\n2:N:코넥스\r\n3:01:수시공시\r\n3:02:공정공시\r\n3:03:시장조치\r\n3:04:신고사항\r\n3:05:정기공시 \r\n3:06:특수공시  \r\n3:07:발행공시  \r\n3:08:지분공시\r\n3:09:워런트공시\r\n3:10:의결권행사공시\r\n3:11:공정위공시\r\n3:12:선물시장공시\r\n3:A1:시장조치안내\r\n3:A2:상장안내\r\n3:A3:안내사항\r\n3:A4:투자유의사항\r\n3:A5:수익증권\r\n3:A6:투자자참고사항\r\n3:A7:뮤츄얼펀드\r\n2:H:K-OTC\r\n2:I:기타\r\n1:6:연합뉴스\r\n3:01:정치\r\n3:02:경제\r\n3:03:증권/금융\r\n3:04:산업\r\n3:05:사회\r\n3:06:사건사고\r\n3:07:문화\r\n3:08:생활건강\r\n3:09:IT. 과학\r\n3:10:북한\r\n3:11:국제\r\n3:12:스포츠\r\n3:13:기타\r\n1:2:한경\r\n3:01:증권\r\n3:04:경제\r\n3:03:부동산\r\n3:07:IT/과학\r\n3:08:정치\r\n3:09:국제\r\n3:10:사회\r\n3:11:생활/문화\r\n3:00:오피니언\r\n3:12:스포츠\r\n3:20:연예\r\n3:18:보도자료\r\n1:A:매경\r\n3:01:경제\r\n3:02:금융\r\n3:03:산업/기업\r\n3:04:중기/벤쳐/과기\r\n3:05:증권\r\n3:06:부동산\r\n3:07:정치\r\n3:08:사회\r\n3:09:인물/동정\r\n3:10:국제\r\n3:11:문화\r\n3:12:레저/스포츠\r\n3:13:사설/칼럼\r\n3:14:기획/분석\r\n3:15:섹션\r\n3:16:English News\r\n3:17:매경이코노미\r\n3:18:mbn\r\n3:90:기타\r\n1:4:이데일리\r\n3:B1:채권시황\r\n3:B2:신종채권\r\n3:F1:외환시황\r\n3:G1:보도자료\r\n3:H1:정책뉴스\r\n3:H2:금융뉴스\r\n3:H3:금융금리/수익율\r\n3:I1:IPO뉴스\r\n3:J1:뉴욕\r\n3:J2:아시아/유럽\r\n3:J3:월드마켓\r\n3:J4:국제기업/산업\r\n3:J5:경제흐름\r\n3:L1:기업뉴스\r\n3:L2:IT\r\n3:L3:벤처\r\n3:L4:e3비즈월드\r\n3:S1:주식시황\r\n3:S2:거래소\r\n3:S3:코스닥&장외\r\n3:S4:루머\r\n3:S5:증권가\r\n1:5:머니투데이\r\n3:A01:주식\r\n3:A02:선물옵션\r\n3:A05:해외증시\r\n3:A06:외환\r\n3:A07:채권\r\n3:A08:펀드\r\n3:B01:경제\r\n3:B02:산업\r\n3:B03:정보과학\r\n3:B04:국제\r\n3:B05:금융보험\r\n3:B07:부동산\r\n3:B08:성공학\r\n3:B09:재테크\r\n3:B10:바이오\r\n1:9:뉴스핌\r\n3:01:주식\r\n3:02:채권\r\n3:03:외환\r\n3:04:국제\r\n3:05:금융/제테크\r\n3:06:산업\r\n3:07:경제\r\n3:08:광장\r\n3:09:전문가기고\r\n3:90:기타\r\n1:8:아시아경제\r\n3:A0:증권\r\n3:B0:금융\r\n3:C0:부동산\r\n3:D0:산업\r\n3:E0:경제\r\n3:F0:정치,사회\r\n3:G0:사설,칼럼\r\n3:H0:인사,동정,부고\r\n3:I0:루머&팩트\r\n3:J0:국내뉴스\r\n3:K0:아시아시각\r\n3:L0:골프\r\n3:M0:모닝브리핑\r\n3:N0:연예\r\n3:10:국제\r\n3:20:중국\r\n3:30:인도\r\n3:40:일본\r\n3:50:이머징마켓\r\n1:B:헤럴드경제 \r\n3:01:뉴스\r\n3:02:기업\r\n3:03:재테크\r\n3:04:스타\r\n3:05:문화\r\n3:90:기타\r\n1:C:파이낸셜\r\n3:01:증권\r\n3:02:금융\r\n3:03:부동산\r\n3:04:산업\r\n3:05:경제\r\n3:06:정보과학\r\n3:07:유통\r\n3:08:국제\r\n3:09:정치\r\n3:10:전국/사회\r\n3:11:문화\r\n3:12:스포츠\r\n3:13:교육\r\n3:14:피플\r\n3:15:사설/컬럼\r\n3:16:기획/연재\r\n3:17:fn재테크\r\n3:18:광고\r\n3:90:기타\r\n1:D:이투데이\r\n3:21:증권\r\n3:51:금융\r\n3:22:정치/정책\r\n3:31:글로벌\r\n3:23:산업\r\n3:24:부동산\r\n3:26:라이프\r\n3:25:칼럼/인물\r\n3:41:연예/스포츠\r\n3:90:기타\r\n1:U:서울경제\r\n3:31:증권\r\n3:32:부동산\r\n3:33:경제/금융\r\n3:34:산업/기업\r\n3:35:IT/과학\r\n3:36:정치\r\n3:37:사회\r\n3:38:국제\r\n3:39:칼럼\r\n3:3A:인사/동정/부음\r\n3:3B:문화/건강/레저\r\n3:3C:골프/스포츠\r\n1:V:조선경제i\r\n3:1:뉴스\r\n3:2:Market\r\n3:4:부동산\r\n3:6:글로벌경제\r\n3:8:위클리비즈\r\n3:B:자동차\r\n3:C:녹색BIZ\r\n1:7:인포스탁\r\n3:01:거래소종목\r\n3:02:코스닥종목\r\n3:03:해외증시\r\n3:04:선물동향\r\n3:00:기타\r\n1:X:CEO스코어\r\n3:01:경제\r\n3:02:산업\r\n3:03:금융\r\n3:04:공기업\r\n3:05:전자\r\n3:06:통신\r\n3:07:게임,인터넷\r\n3:08:자동차\r\n3:09:조선,철강\r\n3:10:식음료\r\n3:11:유통\r\n3:12:건설\r\n3:13:제약\r\n3:14:화학,에너지\r\n3:15:생활산업\r\n3:16:기타\r\n1:S:컨슈머타임스\r\n3:01:종합\r\n3:02:파이낸셜컨슈머\r\n3:03:컨슈머리뷰\r\n3:04:정치,사회\r\n3:05:스포츠,연예\r\n3:06:컨슈머뷰티\r\n3:07:오피니언\r\n3:09:기타\r\n1:Z:인베스트조선\r\n3:01:증권/금융\r\n1:d:NSP통신\r\n3:11:IT/과학\r\n3:12:금융/증권\r\n3:13:부동산\r\n3:14:자동차\r\n3:15:연예/문화\r\n3:16:생활경제\r\n3:17:물류/유통\r\n3:18:인사/동정\r\n3:19:정치/사회\r\n3:20:기업\r\n3:21:의학/건강\r\n3:23:신상품/리뷰\r\n3:24:해명/반론\r\n1:a:IRGO\r\n3:10:IR정보\r\n3:20:IR일정\r\n3:50:IR FOCUS\r\n1:Y:eFriend Air\r\n3:01:종목상담\r\n3:02:VOD\r\n1:J:동향\r\n1:L:한투리서치"
      },
      {
        "element": "dorg",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iscd1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iscd2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iscd3",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iscd4",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "iscd5",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_NEWS_OFER_ENTP_CODE:\r\nFID_COND_MRKT_CLS_CODE:\r\nFID_INPUT_ISCD:\r\nFID_TITL_CNTT:\r\nFID_INPUT_DATE_1:\r\nFID_INPUT_HOUR_1:\r\nFID_RANK_SORT_CLS_CODE:\r\nFID_INPUT_SRNO:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"cntt_usiq_srno\": \"2024041217173779111\",\r\n            \"news_ofer_entp_code\": \"9\",\r\n            \"data_dt\": \"20240412\",\r\n            \"data_tm\": \"171737\",\r\n            \"hts_pbnt_titl_cntt\": \"금융투자협회, 인도 기프트 시티 규제당국 IFSCA와 라운드테이블\",\r\n            \"news_lrdv_code\": \"10\",\r\n            \"dorg\": \"뉴스핌\",\r\n            \"iscd1\": \"\",\r\n            \"iscd2\": \"\",\r\n            \"iscd3\": \"\",\r\n            \"iscd4\": \"\",\r\n            \"iscd5\": \"\",\r\n            \"iscd6\": \"\",\r\n            \"iscd7\": \"\",\r\n            \"iscd8\": \"\",\r\n            \"iscd9\": \"\",\r\n            \"iscd10\": \"\",\r\n            \"kor_isnm1\": \" \",\r\n            \"kor_isnm2\": \"\",\r\n            \"kor_isnm3\": \"\",\r\n            \"kor_isnm4\": \"\",\r\n            \"kor_isnm5\": \"\",\r\n            \"kor_isnm6\": \"\",\r\n            \"kor_isnm7\": \"\",\r\n            \"kor_isnm8\": \"\",\r\n            \"kor_isnm9\": \"\",\r\n            \"kor_isnm10\": \"\"\r\n        },\r\n        {\r\n            \"cntt_usiq_srno\": \"2024041217173438610\",\r\n            \"news_ofer_entp_code\": \"5\",\r\n            \"data_dt\": \"20240412\",\r\n            \"data_tm\": \"171734\",\r\n            \"hts_pbnt_titl_cntt\": \"미국 매출 90% 껑충…BBQ, 지난해 4730억원 사상최대 매출\",\r\n            \"news_lrdv_code\": \"B02\",\r\n            \"dorg\": \"머니투데이\",\r\n            \"iscd1\": \"\",\r\n            \"iscd2\": \"\",\r\n            \"iscd3\": \"\",\r\n            \"iscd4\": \"\",\r\n            \"iscd5\": \"\",\r\n            \"iscd6\": \"\",\r\n            \"iscd7\": \"\",\r\n            \"iscd8\": \"\",\r\n            \"iscd9\": \"\",\r\n            \"iscd10\": \"\",\r\n            \"kor_isnm1\": \" \",\r\n            \"kor_isnm2\": \"\",\r\n            \"kor_isnm3\": \"\",\r\n            \"kor_isnm4\": \"\",\r\n            \"kor_isnm5\": \"\",\r\n            \"kor_isnm6\": \"\",\r\n            \"kor_isnm7\": \"\",\r\n            \"kor_isnm8\": \"\",\r\n            \"kor_isnm9\": \"\",\r\n            \"kor_isnm10\": \"\"\r\n        },\r\n        {\r\n            \"cntt_usiq_srno\": \"2024041217172998812\",\r\n            \"news_ofer_entp_code\": \"9\",\r\n            \"data_dt\": \"20240412\",\r\n            \"data_tm\": \"171729\",\r\n            \"hts_pbnt_titl_cntt\": \"한미-한국여자의사회 제정 '젊은의학자학술상'에 정선재 부교수\",\r\n            \"news_lrdv_code\": \"10\",\r\n            \"dorg\": \"뉴스핌\",\r\n            \"iscd1\": \"\",\r\n            \"iscd2\": \"\",\r\n            \"iscd3\": \"\",\r\n            \"iscd4\": \"\",\r\n            \"iscd5\": \"\",\r\n            \"iscd6\": \"\",\r\n            \"iscd7\": \"\",\r\n            \"iscd8\": \"\",\r\n            \"iscd9\": \"\",\r\n            \"iscd10\": \"\",\r\n            \"kor_isnm1\": \" \",\r\n            \"kor_isnm2\": \"\",\r\n            \"kor_isnm3\": \"\",\r\n            \"kor_isnm4\": \"\",\r\n            \"kor_isnm5\": \"\",\r\n            \"kor_isnm6\": \"\",\r\n            \"kor_isnm7\": \"\",\r\n            \"kor_isnm8\": \"\",\r\n            \"kor_isnm9\": \"\",\r\n            \"kor_isnm10\": \"\"\r\n        },\r\n        {\r\n            \"cntt_usiq_srno\": \"2024041217165428809\",\r\n            \"news_ofer_entp_code\": \"6\",\r\n            \"data_dt\": \"20240412\",\r\n            \"data_tm\": \"171654\",\r\n            \"hts_pbnt_titl_cntt\": \"[亞증시-종합] 강달러 속 혼조\",\r\n            \"news_lrdv_code\": \"03\",\r\n            \"dorg\": \"연합뉴스\",\r\n            \"iscd1\": \"\",\r\n            \"iscd2\": \"\",\r\n            \"iscd3\": \"\",\r\n            \"iscd4\": \"\",\r\n            \"iscd5\": \"\",\r\n            \"iscd6\": \"\",\r\n            \"iscd7\": \"\",\r\n            \"iscd8\": \"\",\r\n            \"iscd9\": \"\",\r\n            \"iscd10\": \"\",\r\n            \"kor_isnm1\": \" \",\r\n            \"kor_isnm2\": \"\",\r\n            \"kor_isnm3\": \"\",\r\n            \"kor_isnm4\": \"\",\r\n            \"kor_isnm5\": \"\",\r\n            \"kor_isnm6\": \"\",\r\n            \"kor_isnm7\": \"\",\r\n            \"kor_isnm8\": \"\",\r\n            \"kor_isnm9\": \"\",\r\n            \"kor_isnm10\": \"\"\r\n        },\r\n        {\r\n            \"cntt_usiq_srno\": \"2024041217161911807\",\r\n            \"news_ofer_entp_code\": \"5\",\r\n            \"data_dt\": \"20240412\",\r\n            \"data_tm\": \"171619\",\r\n            \"hts_pbnt_titl_cntt\": \"골드팡, 'Hello Spring' 진행..최대 61% 할인 이벤트\",\r\n            \"news_lrdv_code\": \"B02\",\r\n            \"dorg\": \"머니투데이\",\r\n            \"iscd1\": \"\",\r\n            \"iscd2\": \"\",\r\n            \"iscd3\": \"\",\r\n            \"iscd4\": \"\",\r\n            \"iscd5\": \"\",\r\n            \"iscd6\": \"\",\r\n            \"iscd7\": \"\",\r\n            \"iscd8\": \"\",\r\n            \"iscd9\": \"\",\r\n            \"iscd10\": \"\",\r\n            \"kor_isnm1\": \" \",\r\n            \"kor_isnm2\": \"\",\r\n            \"kor_isnm3\": \"\",\r\n            \"kor_isnm4\": \"\",\r\n            \"kor_isnm5\": \"\",\r\n            \"kor_isnm6\": \"\",\r\n            \"kor_isnm7\": \"\",\r\n            \"kor_isnm8\": \"\",\r\n            \"kor_isnm9\": \"\",\r\n            \"kor_isnm10\": \"\"\r\n        },\r\n        {\r\n            \"cntt_usiq_srno\": \"2024041217161867008\",\r\n            \"news_ofer_entp_code\": \"7\",\r\n            \"data_dt\": \"20240412\",\r\n            \"data_tm\": \"171618\",\r\n            \"hts_pbnt_titl_cntt\": \"자람테크놀로지, 임원ㆍ주요주주 특정증권등 소유주식수 변동\",\r\n            \"news_lrdv_code\": \"02\",\r\n            \"dorg\": \"인포스탁\",\r\n            \"iscd1\": \"389020\",\r\n            \"iscd2\": \"\",\r\n            \"iscd3\": \"\",\r\n            \"iscd4\": \"\",\r\n            \"iscd5\": \"\",\r\n            \"iscd6\": \"\",\r\n            \"iscd7\": \"\",\r\n            \"iscd8\": \"\",\r\n            \"iscd9\": \"\",\r\n            \"iscd10\": \"\",\r\n            \"kor_isnm1\": \"자람테크놀로지\",\r\n            \"kor_isnm2\": \"\",\r\n            \"kor_isnm3\": \"\",\r\n            \"kor_isnm4\": \"\",\r\n            \"kor_isnm5\": \"\",\r\n            \"kor_isnm6\": \"\",\r\n            \"kor_isnm7\": \"\",\r\n            \"kor_isnm8\": \"\",\r\n            \"kor_isnm9\": \"\",\r\n            \"kor_isnm10\": \"\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTPF1604R",
    "name": "상품기본조회",
    "url": "/uapi/domestic-stock/v1/quotations/search-info",
    "sheet": "상품기본조회",
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
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_name120",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_abrv_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_eng_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_eng_name120",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_eng_abrv_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "std_pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shtn_pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_sale_stat_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_risk_grad_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_clsf_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_clsf_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sale_strt_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sale_end_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "wrap_asst_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivst_prdt_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivst_prdt_type_cd_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frst_erlm_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\t\"PDNO\":\"AAPL\",\r\n\t\"PRDT_TYPE_CD\":\"512\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": {\r\n        \"pdno\": \"AAPL\",\r\n        \"prdt_type_cd\": \"512\",\r\n        \"prdt_name\": \"애플\",\r\n        \"prdt_name120\": \"애플\",\r\n        \"prdt_abrv_name\": \"애플\",\r\n        \"prdt_eng_name\": \"APPLE INC\",\r\n        \"prdt_eng_name120\": \"APPLE INC\",\r\n        \"prdt_eng_abrv_name\": \"APPLE INC\",\r\n        \"std_pdno\": \"US0378331005\",\r\n        \"shtn_pdno\": \"AAPL\",\r\n        \"prdt_sale_stat_cd\": \"\",\r\n        \"prdt_risk_grad_cd\": \"\",\r\n        \"prdt_clsf_cd\": \"101210\",\r\n        \"prdt_clsf_name\": \"해외주식\",\r\n        \"sale_strt_dt\": \"\",\r\n        \"sale_end_dt\": \"\",\r\n        \"wrap_asst_type_cd\": \"06\",\r\n        \"ivst_prdt_type_cd\": \"1012\",\r\n        \"ivst_prdt_type_cd_name\": \"해외주식\",\r\n        \"frst_erlm_dt\": \"\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"KIOK0530\",\r\n    \"msg1\": \"조회되었습니다                                                                  \"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST663400C0",
    "name": "국내주식 증권사별 투자의견",
    "url": "/uapi/domestic-stock/v1/quotations/invest-opbysec",
    "sheet": "국내주식 증권사별 투자의견",
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
        "element": "stck_bsop_date",
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
        "element": "invt_opnn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "invt_opnn_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rgbf_invt_opnn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rgbf_invt_opnn_cls_code",
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
        "element": "hts_goal_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stft_esdg",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dprt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_COND_SCR_DIV_CODE:16633\r\nFID_INPUT_ISCD:999\r\nFID_DIV_CLS_CODE:0\r\nFID_INPUT_DATE_1:20240428\r\nFID_INPUT_DATE_2:20240528",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"454910\",\r\n            \"hts_kor_isnm\": \"두산로보틱스\",\r\n            \"invt_opnn\": \"NotRated\",\r\n            \"invt_opnn_cls_code\": \"3\",\r\n            \"rgbf_invt_opnn\": \"NotRated\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"상상인\",\r\n            \"stck_prpr\": \"74300\",\r\n            \"prdy_vrss\": \"500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.68\",\r\n            \"hts_goal_prc\": \"0\",\r\n            \"stck_prdy_clpr\": \"71600\",\r\n            \"stft_esdg\": \"74300\",\r\n            \"dprt\": \"0.00\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"389140\",\r\n            \"hts_kor_isnm\": \"포바이포\",\r\n            \"invt_opnn\": \"NotRated\",\r\n            \"invt_opnn_cls_code\": \"3\",\r\n            \"rgbf_invt_opnn\": \"NotRated\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"상상인\",\r\n            \"stck_prpr\": \"10330\",\r\n            \"prdy_vrss\": \"0\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"hts_goal_prc\": \"0\",\r\n            \"stck_prdy_clpr\": \"10120\",\r\n            \"stft_esdg\": \"10330\",\r\n            \"dprt\": \"0.00\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"336260\",\r\n            \"hts_kor_isnm\": \"두산퓨얼셀\",\r\n            \"invt_opnn\": \"BUY\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"BUY\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"상상인\",\r\n            \"stck_prpr\": \"26150\",\r\n            \"prdy_vrss\": \"-50\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.19\",\r\n            \"hts_goal_prc\": \"33000\",\r\n            \"stck_prdy_clpr\": \"25000\",\r\n            \"stft_esdg\": \"-6850\",\r\n            \"dprt\": \"-20.76\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"298380\",\r\n            \"hts_kor_isnm\": \"에이비엘바이오\",\r\n            \"invt_opnn\": \"NotRated\",\r\n            \"invt_opnn_cls_code\": \"3\",\r\n            \"rgbf_invt_opnn\": \"NotRated\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"상상인\",\r\n            \"stck_prpr\": \"23300\",\r\n            \"prdy_vrss\": \"-100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.43\",\r\n            \"hts_goal_prc\": \"0\",\r\n            \"stck_prdy_clpr\": \"24300\",\r\n            \"stft_esdg\": \"23300\",\r\n            \"dprt\": \"0.00\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"377740\",\r\n            \"hts_kor_isnm\": \"바이오노트\",\r\n            \"invt_opnn\": \"BUY\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"BUY\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"다올투자\",\r\n            \"stck_prpr\": \"4135\",\r\n            \"prdy_vrss\": \"-10\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.24\",\r\n            \"hts_goal_prc\": \"5700\",\r\n            \"stck_prdy_clpr\": \"4175\",\r\n            \"stft_esdg\": \"-1565\",\r\n            \"dprt\": \"-27.46\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"137310\",\r\n            \"hts_kor_isnm\": \"에스디바이오센서\",\r\n            \"invt_opnn\": \"HOLD\",\r\n            \"invt_opnn_cls_code\": \"3\",\r\n            \"rgbf_invt_opnn\": \"HOLD\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"다올투자\",\r\n            \"stck_prpr\": \"10110\",\r\n            \"prdy_vrss\": \"60\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.60\",\r\n            \"hts_goal_prc\": \"11000\",\r\n            \"stck_prdy_clpr\": \"10060\",\r\n            \"stft_esdg\": \"-890\",\r\n            \"dprt\": \"-8.09\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"stck_shrn_iscd\": \"298020\",\r\n            \"hts_kor_isnm\": \"효성티앤씨\",\r\n            \"invt_opnn\": \"매수\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"매수\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"IBK투자\",\r\n            \"stck_prpr\": \"389000\",\r\n            \"prdy_vrss\": \"-19000\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-4.66\",\r\n            \"hts_goal_prc\": \"550000\",\r\n            \"stck_prdy_clpr\": \"400500\",\r\n            \"stft_esdg\": \"-161000\",\r\n            \"dprt\": \"-29.27\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST04770000",
    "name": "국내주식 당사 신용가능종목",
    "url": "/uapi/domestic-stock/v1/quotations/credit-by-company",
    "sheet": "국내주식 당사 신용가능종목",
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
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "crdt_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"J\",\r\n\"fid_cond_scr_div_code\":\"20477\",\r\n\"fid_input_iscd\":\"0000\",\r\n\"fid_slct_yn\":\"0\",\r\n\"fid_rank_sort_cls_code\":\"1\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_shrn_iscd\": \"473440\",\r\n            \"hts_kor_isnm\": \"ACE 11월만기자동연장회사채AA-이상액티브\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"105190\",\r\n            \"hts_kor_isnm\": \"ACE 200\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"332500\",\r\n            \"hts_kor_isnm\": \"ACE 200TR\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"448880\",\r\n            \"hts_kor_isnm\": \"ACE 24-12 회사채(AA-이상)액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"461270\",\r\n            \"hts_kor_isnm\": \"ACE 26-06 회사채(AA-이상)액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"414270\",\r\n            \"hts_kor_isnm\": \"ACE G2전기차&자율주행액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"365780\",\r\n            \"hts_kor_isnm\": \"ACE 국고채10년\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"446770\",\r\n            \"hts_kor_isnm\": \"ACE 글로벌반도체TOP4 Plus SOLACTIVE\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"190620\",\r\n            \"hts_kor_isnm\": \"ACE 단기통안채\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"453850\",\r\n            \"hts_kor_isnm\": \"ACE 미국30년국채액티브(H)\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"360200\",\r\n            \"hts_kor_isnm\": \"ACE 미국S&P500\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"438080\",\r\n            \"hts_kor_isnm\": \"ACE 미국S&P500채권혼합액티브\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"309230\",\r\n            \"hts_kor_isnm\": \"ACE 미국WideMoat가치주\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"367380\",\r\n            \"hts_kor_isnm\": \"ACE 미국나스닥100\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"456880\",\r\n            \"hts_kor_isnm\": \"ACE 미국달러SOFR금리(합성)\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"402970\",\r\n            \"hts_kor_isnm\": \"ACE 미국배당다우존스\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"465580\",\r\n            \"hts_kor_isnm\": \"ACE 미국빅테크TOP7 Plus\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"245710\",\r\n            \"hts_kor_isnm\": \"ACE 베트남VN30(합성)\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"448540\",\r\n            \"hts_kor_isnm\": \"ACE 엔비디아채권혼합블룸버그\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"238720\",\r\n            \"hts_kor_isnm\": \"ACE 일본Nikkei225(H)\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"356540\",\r\n            \"hts_kor_isnm\": \"ACE 종합채권(AA-이상)KIS액티브\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"457480\",\r\n            \"hts_kor_isnm\": \"ACE 테슬라밸류체인액티브\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"469170\",\r\n            \"hts_kor_isnm\": \"ACE 포스코그룹포커스\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"265520\",\r\n            \"hts_kor_isnm\": \"AP시스템\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"152100\",\r\n            \"hts_kor_isnm\": \"ARIRANG 200\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"453010\",\r\n            \"hts_kor_isnm\": \"ARIRANG KOFR금리\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"449450\",\r\n            \"hts_kor_isnm\": \"ARIRANG K방산Fn\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"161510\",\r\n            \"hts_kor_isnm\": \"ARIRANG 고배당주\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"464470\",\r\n            \"hts_kor_isnm\": \"ARIRANG 미국채30년액티브\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"195980\",\r\n            \"hts_kor_isnm\": \"ARIRANG 신흥국MSCI(합성 H)\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"421320\",\r\n            \"hts_kor_isnm\": \"ARIRANG 우주항공&UAM iSelect\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"328370\",\r\n            \"hts_kor_isnm\": \"ARIRANG 코스피TR\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"027410\",\r\n            \"hts_kor_isnm\": \"BGF\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"282330\",\r\n            \"hts_kor_isnm\": \"BGF리테일\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"126600\",\r\n            \"hts_kor_isnm\": \"BGF에코머티리얼즈\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"138930\",\r\n            \"hts_kor_isnm\": \"BNK금융지주\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"001040\",\r\n            \"hts_kor_isnm\": \"CJ\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"000120\",\r\n            \"hts_kor_isnm\": \"CJ대한통운\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"011150\",\r\n            \"hts_kor_isnm\": \"CJ씨푸드\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"097950\",\r\n            \"hts_kor_isnm\": \"CJ제일제당\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"097955\",\r\n            \"hts_kor_isnm\": \"CJ제일제당 우\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"051500\",\r\n            \"hts_kor_isnm\": \"CJ프레시웨이\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"058820\",\r\n            \"hts_kor_isnm\": \"CMG제약\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"012030\",\r\n            \"hts_kor_isnm\": \"DB\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"005830\",\r\n            \"hts_kor_isnm\": \"DB손해보험\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"000990\",\r\n            \"hts_kor_isnm\": \"DB하이텍\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"139130\",\r\n            \"hts_kor_isnm\": \"DGB금융지주\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"001530\",\r\n            \"hts_kor_isnm\": \"DI동일\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"375500\",\r\n            \"hts_kor_isnm\": \"DL이앤씨\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"068790\",\r\n            \"hts_kor_isnm\": \"DMS\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"007340\",\r\n            \"hts_kor_isnm\": \"DN오토모티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"241520\",\r\n            \"hts_kor_isnm\": \"DSC인베스트먼트\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"017940\",\r\n            \"hts_kor_isnm\": \"E1\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"007700\",\r\n            \"hts_kor_isnm\": \"F&F홀딩스\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"078930\",\r\n            \"hts_kor_isnm\": \"GS\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"001250\",\r\n            \"hts_kor_isnm\": \"GS글로벌\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"007070\",\r\n            \"hts_kor_isnm\": \"GS리테일\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"293180\",\r\n            \"hts_kor_isnm\": \"HANARO 200\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"454320\",\r\n            \"hts_kor_isnm\": \"HANARO CAPEX설비투자iSelect\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"395290\",\r\n            \"hts_kor_isnm\": \"HANARO Fn K-POP&미디어\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"395270\",\r\n            \"hts_kor_isnm\": \"HANARO Fn K-반도체\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"441540\",\r\n            \"hts_kor_isnm\": \"HANARO Fn조선해운\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"434730\",\r\n            \"hts_kor_isnm\": \"HANARO 원자력iSelect\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"078150\",\r\n            \"hts_kor_isnm\": \"HB테크놀러지\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"089470\",\r\n            \"hts_kor_isnm\": \"HDC현대EP\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"009540\",\r\n            \"hts_kor_isnm\": \"HD한국조선해양\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"267250\",\r\n            \"hts_kor_isnm\": \"HD현대\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"267270\",\r\n            \"hts_kor_isnm\": \"HD현대건설기계\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"322000\",\r\n            \"hts_kor_isnm\": \"HD현대에너지솔루션\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"042670\",\r\n            \"hts_kor_isnm\": \"HD현대인프라코어\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"329180\",\r\n            \"hts_kor_isnm\": \"HD현대중공업\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"195940\",\r\n            \"hts_kor_isnm\": \"HK이노엔\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"204320\",\r\n            \"hts_kor_isnm\": \"HL만도\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"060980\",\r\n            \"hts_kor_isnm\": \"HL홀딩스\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"011200\",\r\n            \"hts_kor_isnm\": \"HMM\",\r\n            \"crdt_rate\": \"20.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"036640\",\r\n            \"hts_kor_isnm\": \"HRS\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"095340\",\r\n            \"hts_kor_isnm\": \"ISC\",\r\n            \"crdt_rate\": \"60.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"175330\",\r\n            \"hts_kor_isnm\": \"JB금융지주\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"234080\",\r\n            \"hts_kor_isnm\": \"JW생명과학\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"035900\",\r\n            \"hts_kor_isnm\": \"JYP Ent.\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"148020\",\r\n            \"hts_kor_isnm\": \"KBSTAR 200\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"448600\",\r\n            \"hts_kor_isnm\": \"KBSTAR 25-11 회사채(AA-이상)액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"465330\",\r\n            \"hts_kor_isnm\": \"KBSTAR 2차전지TOP10\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"422420\",\r\n            \"hts_kor_isnm\": \"KBSTAR 2차전지액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"469070\",\r\n            \"hts_kor_isnm\": \"KBSTAR AI&로봇\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"290130\",\r\n            \"hts_kor_isnm\": \"KBSTAR ESG사회책임투자\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"367760\",\r\n            \"hts_kor_isnm\": \"KBSTAR Fn5G테크\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"367770\",\r\n            \"hts_kor_isnm\": \"KBSTAR Fn수소경제테마\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"326240\",\r\n            \"hts_kor_isnm\": \"KBSTAR IT플러스\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"385560\",\r\n            \"hts_kor_isnm\": \"KBSTAR KIS국고채30년Enhanced\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"401170\",\r\n            \"hts_kor_isnm\": \"KBSTAR iSelect메타버스\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"266160\",\r\n            \"hts_kor_isnm\": \"KBSTAR 고배당\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"385550\",\r\n            \"hts_kor_isnm\": \"KBSTAR 단기종합채권(AA-이상)액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"196230\",\r\n            \"hts_kor_isnm\": \"KBSTAR 단기통안채\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"315960\",\r\n            \"hts_kor_isnm\": \"KBSTAR 대형고배당10TR\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"455890\",\r\n            \"hts_kor_isnm\": \"KBSTAR 머니마켓액티브\",\r\n            \"crdt_rate\": \"30.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"379780\",\r\n            \"hts_kor_isnm\": \"KBSTAR 미국S&P500\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"453330\",\r\n            \"hts_kor_isnm\": \"KBSTAR 미국S&P500(H)\",\r\n            \"crdt_rate\": \"50.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"368590\",\r\n            \"hts_kor_isnm\": \"KBSTAR 미국나스닥100\",\r\n            \"crdt_rate\": \"40.00\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"437350\",\r\n            \"hts_kor_isnm\": \"KBSTAR 미국단기투자등급회사채액티브\",\r\n            \"crdt_rate\": \"40.00\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST663300C0",
    "name": "국내주식 종목투자의견",
    "url": "/uapi/domestic-stock/v1/quotations/invest-opinion",
    "sheet": "국내주식 종목투자의견",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "invt_opnn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "invt_opnn_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rgbf_invt_opnn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rgbf_invt_opnn_cls_code",
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
        "element": "hts_goal_prc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_nday_esdg",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nday_dprt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stft_esdg",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dprt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_COND_SCR_DIV_CODE:16633\r\nFID_INPUT_ISCD:005930\r\nFID_INPUT_DATE_1:20240101\r\nFID_INPUT_DATE_2:20240528",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"invt_opnn\": \"매수\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"매수\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"SK\",\r\n            \"hts_goal_prc\": \"105000\",\r\n            \"stck_prdy_clpr\": \"75900\",\r\n            \"stck_nday_esdg\": \"-29100\",\r\n            \"nday_dprt\": \"-27.71\",\r\n            \"stft_esdg\": \"-27400\",\r\n            \"dprt\": \"-26.10\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240520\",\r\n            \"invt_opnn\": \"BUY\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"BUY\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"하이투자\",\r\n            \"hts_goal_prc\": \"91000\",\r\n            \"stck_prdy_clpr\": \"77400\",\r\n            \"stck_nday_esdg\": \"-13600\",\r\n            \"nday_dprt\": \"-14.95\",\r\n            \"stft_esdg\": \"-13400\",\r\n            \"dprt\": \"-14.73\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240516\",\r\n            \"invt_opnn\": \"매수\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"매수\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"미래에셋\",\r\n            \"hts_goal_prc\": \"110000\",\r\n            \"stck_prdy_clpr\": \"78300\",\r\n            \"stck_nday_esdg\": \"-31700\",\r\n            \"nday_dprt\": \"-28.82\",\r\n            \"stft_esdg\": \"-32400\",\r\n            \"dprt\": \"-29.45\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240502\",\r\n            \"invt_opnn\": \"BUY\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"BUY\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"다올투자\",\r\n            \"hts_goal_prc\": \"105000\",\r\n            \"stck_prdy_clpr\": \"77500\",\r\n            \"stck_nday_esdg\": \"-27500\",\r\n            \"nday_dprt\": \"-26.19\",\r\n            \"stft_esdg\": \"-27400\",\r\n            \"dprt\": \"-26.10\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240502\",\r\n            \"invt_opnn\": \"BUY\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"BUY\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"하이투자\",\r\n            \"hts_goal_prc\": \"95000\",\r\n            \"stck_prdy_clpr\": \"77500\",\r\n            \"stck_nday_esdg\": \"-17500\",\r\n            \"nday_dprt\": \"-18.42\",\r\n            \"stft_esdg\": \"-17400\",\r\n            \"dprt\": \"-18.32\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240502\",\r\n            \"invt_opnn\": \"BUY\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"BUY\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"KB\",\r\n            \"hts_goal_prc\": \"120000\",\r\n            \"stck_prdy_clpr\": \"77500\",\r\n            \"stck_nday_esdg\": \"-42500\",\r\n            \"nday_dprt\": \"-35.42\",\r\n            \"stft_esdg\": \"-42400\",\r\n            \"dprt\": \"-35.33\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240502\",\r\n            \"invt_opnn\": \"매수\",\r\n            \"invt_opnn_cls_code\": \"2\",\r\n            \"rgbf_invt_opnn\": \"매수\",\r\n            \"rgbf_invt_opnn_cls_code\": \"3\",\r\n            \"mbcr_name\": \"신한투자증권\",\r\n            \"hts_goal_prc\": \"110000\",\r\n            \"stck_prdy_clpr\": \"77500\",\r\n            \"stck_nday_esdg\": \"-32500\",\r\n            \"nday_dprt\": \"-29.55\",\r\n            \"stft_esdg\": \"-32400\",\r\n            \"dprt\": \"-29.45\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTSC2702R",
    "name": "당사 대주가능 종목",
    "url": "/uapi/domestic-stock/v1/quotations/lendable-by-company",
    "sheet": "당사 대주가능 종목",
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
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "papr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_clpr",
        "type": "string",
        "required": "Y",
        "description": "전일종가"
      },
      {
        "element": "sbst_prvs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tr_stop_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "psbl_yn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lmt_qty1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "use_qty1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trad_psbl_qty2",
        "type": "string",
        "required": "Y",
        "description": "가능수량"
      },
      {
        "element": "rght_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bass_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "psbl_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_stup_lmt_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "brch_lmt_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rqst_psbl_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "EXCG_DVSN_CD:00\r\nPDNO:\r\nTHCO_STLN_PSBL_YN:Y\r\nINQR_DVSN_1:0\r\nCTX_AREA_FK200:\r\nCTX_AREA_NK100:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"ctx_area_fk200\": \"00!^!^Y!^0                                                                                                                                                                                              \",\r\n    \"ctx_area_nk100\": \"                                                                                                    \",\r\n    \"output1\": [\r\n        {\r\n            \"pdno\": \"130960\",\r\n            \"prdt_name\": \"CJ E&M\",\r\n            \"papr\": \"5000\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"10520\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"10520\",\r\n            \"rght_type_cd\": \"11\",\r\n            \"bass_dt\": \"20180629\",\r\n            \"psbl_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"pdno\": \"110550\",\r\n            \"prdt_name\": \"HIT 골드\",\r\n            \"papr\": \"0\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"0\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"0\",\r\n            \"rght_type_cd\": \"32\",\r\n            \"bass_dt\": \"20111222\",\r\n            \"psbl_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"pdno\": \"124090\",\r\n            \"prdt_name\": \"HIT 보험\",\r\n            \"papr\": \"0\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"0\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"0\",\r\n            \"rght_type_cd\": \"32\",\r\n            \"bass_dt\": \"20111219\",\r\n            \"psbl_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"pdno\": \"002550\",\r\n            \"prdt_name\": \"KB손해보험\",\r\n            \"papr\": \"500\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"0\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"0\",\r\n            \"rght_type_cd\": \"13\",\r\n            \"bass_dt\": \"20170706\",\r\n            \"psbl_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"pdno\": \"021960\",\r\n            \"prdt_name\": \"KB캐피탈\",\r\n            \"papr\": \"5000\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"0\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"0\",\r\n            \"rght_type_cd\": \"13\",\r\n            \"bass_dt\": \"20170706\",\r\n            \"psbl_yn\": \"Y\"\r\n        },\r\n        {\r\n            \"pdno\": \"105270\",\r\n            \"prdt_name\": \"KINDEX 성장대형F15\",\r\n            \"papr\": \"0\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"0\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"0\",\r\n            \"rght_type_cd\": \"32\",\r\n            \"bass_dt\": \"20140430\",\r\n            \"psbl_yn\": \"Y\"\r\n        },...\r\n        {\r\n            \"pdno\": \"003450\",\r\n            \"prdt_name\": \"현대증권\",\r\n            \"papr\": \"5000\",\r\n            \"bfdy_clpr\": \"0\",\r\n            \"sbst_prvs\": \"0\",\r\n            \"tr_stop_dvsn_name\": \"거래정지\",\r\n            \"psbl_yn_name\": \"가능\",\r\n            \"lmt_qty1\": \"0\",\r\n            \"use_qty1\": \"0\",\r\n            \"trad_psbl_qty2\": \"0\",\r\n            \"rght_type_cd\": \"13\",\r\n            \"bass_dt\": \"20161018\",\r\n            \"psbl_yn\": \"Y\"\r\n        }\r\n    ],\r\n    \"output2\": {\r\n        \"tot_stup_lmt_qty\": \"6441070\",\r\n        \"brch_lmt_qty\": \"-1228\",\r\n        \"rqst_psbl_qty\": \"6442095\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"KIOK0460\",\r\n    \"msg1\": \"조회 되었습니다. (마지막 자료)                                                  \"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTPF1002R",
    "name": "주식기본조회",
    "url": "/uapi/domestic-stock/v1/quotations/search-stock-info",
    "sheet": "주식기본조회",
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
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mket_id_cd",
        "type": "string",
        "required": "Y",
        "description": "AGR.농축산물파생\r\nBON.채권파생\r\nCMD.일반상품시장\r\nCUR.통화파생\r\nENG.에너지파생\r\nEQU.주식파생\r\nETF.ETF파생\r\nIRT.금리파생\r\nKNX.코넥스\r\nKSQ.코스닥\r\nMTL.금속파생\r\nSPI.주가지수파생\r\nSTK.유가증권"
      },
      {
        "element": "scty_grp_id_cd",
        "type": "string",
        "required": "Y",
        "description": "BC.수익증권\r\nDR.주식예탁증서\r\nEF.ETF\r\nEN.ETN\r\nEW.ELW\r\nFE.해외ETF\r\nFO.선물옵션\r\nFS.외국주권\r\nFU.선물\r\nFX.플렉스 선물\r\nGD.금현물\r\nIC.투자계약증권\r\nIF.사회간접자본투융자회사\r\nKN.코넥스주권\r\nMF.투자회사\r\nOP.옵션\r\nRT.부동산투자회사\r\nSC.선박투자회사\r\nSR.신주인수권증서\r\nST.주권\r\nSW.신주인수권증권\r\nTC.신탁수익증권"
      },
      {
        "element": "excg_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": "01.한국증권\r\n02.증권거래소\r\n03.코스닥\r\n04.K-OTC\r\n05.선물거래소\r\n06.CME\r\n07.EUREX\r\n21.금현물\r\n50.미국주간\r\n51.홍콩\r\n52.상해B\r\n53.심천\r\n54.홍콩거래소\r\n55.미국\r\n56.일본\r\n57.상해A\r\n58.심천A\r\n59.베트남\r\n61.장전시간외시장\r\n64.경쟁대량매매\r\n65.경매매시장\r\n81.시간외단일가시장"
      },
      {
        "element": "setl_mmdd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lstg_stqt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lstg_cptl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cpta",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "papr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "issu_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "kospi200_item_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scts_mket_lstg_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scts_mket_lstg_abol_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "kosdaq_mket_lstg_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "kosdaq_mket_lstg_abol_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frbd_mket_lstg_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frbd_mket_lstg_abol_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "reits_kind_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etf_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oilf_fund_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "idx_bztp_lcls_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "idx_bztp_mcls_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "idx_bztp_scls_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_kind_cd",
        "type": "string",
        "required": "Y",
        "description": "000.해당사항없음\r\n101.보통주\r\n201.우선주\r\n202.2우선주\r\n203.3우선주\r\n204.4우선주\r\n205.5우선주\r\n206.6우선주\r\n207.7우선주\r\n208.8우선주\r\n209.9우선주\r\n210.10우선주\r\n211.11우선주\r\n212.12우선주\r\n213.13우선주\r\n214.14우선주\r\n215.15우선주\r\n216.16우선주\r\n217.17우선주\r\n218.18우선주\r\n219.19우선주\r\n220.20우선주\r\n301.후배주\r\n401.혼합주"
      },
      {
        "element": "mfnd_opng_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mfnd_end_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dpsi_erlm_cncl_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etf_cu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_name120",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_abrv_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "std_pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_eng_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_eng_name120",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdt_eng_abrv_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dpsi_aptm_erlm_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etf_txtn_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etf_type_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lstg_abol_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nwst_odst_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sbst_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thco_sbst_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thco_sbst_pric_chng_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tr_stop_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "admn_item_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "clpr_chng_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "std_idst_clsf_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "std_idst_clsf_cd_name",
        "type": "string",
        "required": "Y",
        "description": "표준산업소분류코드\r\n000000\t해당사항없음                                     \r\n010101\t작물 재배업                                      \r\n010102\t축산업                                           \r\n010103\t작물재배 및 축산 복합농업                        \r\n010104\t작물재배 및 축산 관련 서비스업                   \r\n010105\t수렵 및 관련 서비스업                            \r\n010201\t임업                                             \r\n010301\t어로 어업                                        \r\n010302\t양식어업 및 어업관련 서비스업                    \r\n020501\t석탄 광업                                        \r\n020502\t원유 및 천연가스 채굴업                          \r\n020601\t철 광업                                          \r\n020602\t비철금속 광업                                    \r\n020701\t토사석 광업                                      \r\n020702\t기타 비금속광물 광업                             \r\n020801\t광업 지원 서비스업                               \r\n031001\t도축, 육류 가공 및 저장 처리업                   \r\n031002\t수산물 가공 및 저장 처리업                       \r\n031003\t과실, 채소 가공 및 저장 처리업                   \r\n031004\t동물성 및 식물성 유지 제조업                     \r\n031005\t낙농제품 및 식용빙과류 제조업                    \r\n031006\t곡물가공품, 전분 및 전분제품 제조업              \r\n031007\t기타 식품 제조업                                 \r\n031008\t동물용 사료 및 조제식품 제조업                   \r\n031101\t알콜음료 제조업                                  \r\n031102\t비알콜음료 및 얼음 제조업                        \r\n031201\t담배 제조업                                      \r\n031301\t방적 및 가공사 제조업                            \r\n031302\t직물직조 및 직물제품 제조업                      \r\n031303\t편조원단 및 편조제품 제조업                      \r\n031304\t섬유제품 염색, 정리 및 마무리 가공업             \r\n031309\t기타 섬유제품 제조업                             \r\n031401\t봉제의복 제조업                                  \r\n031402\t모피가공 및 모피제품 제조업                      \r\n031403\t편조의복 제조업                                  \r\n031404\t의복 액세서리 제조업                             \r\n031501\t가죽, 가방 및 유사제품 제조업                    \r\n031502\t신발 및 신발부분품 제조업                        \r\n031601\t제재 및 목재 가공업                              \r\n031602\t나무제품 제조업                                  \r\n031603\t코르크 및 조물 제품 제조업                       \r\n031701\t펄프, 종이 및 판지 제조업                        \r\n031702\t골판지, 종이 상자 및 종이용기 제조업             \r\n031709\t기타 종이 및 판지 제품 제조업                    \r\n031801\t인쇄 및 인쇄관련 산업                            \r\n031802\t기록매체 복제업                                  \r\n031901\t코크스 및 연탄 제조업                            \r\n031902\t석유 정제품 제조업                               \r\n032001\t기초화학물질 제조업                              \r\n032002\t비료 및 질소화합물 제조업                        \r\n032003\t합성고무 및 플라스틱 물질 제조업                 \r\n032004\t기타 화학제품 제조업                             \r\n032005\t화학섬유 제조업                                  \r\n032101\t기초 의약물질 및 생물학적 제제 제조업            \r\n032102\t의약품 제조업                                    \r\n032103\t의료용품 및 기타 의약관련제품 제조업             \r\n032201\t고무제품 제조업                                  \r\n032202\t플라스틱제품 제조업                              \r\n032301\t유리 및 유리제품 제조업                          \r\n032302\t도자기 및 기타 요업제품 제조업                   \r\n032303\t시멘트, 석회, 플라스터 및 그 제품 제조업         \r\n032309\t기타 비금속 광물제품 제조업                      \r\n032401\t1차 철강 제조업                                  \r\n032402\t1차 비철금속 제조업                              \r\n032403\t금속 주조업                                      \r\n032501\t구조용 금속제품, 탱크 및 증기발생기 제조업       \r\n032502\t무기 및 총포탄 제조업                            \r\n032509\t기타 금속가공제품 제조업                         \r\n032601\t반도체 제조업                                    \r\n032602\t전자부품 제조업                                  \r\n032603\t컴퓨터 및 주변장치 제조업                        \r\n032604\t통신 및 방송 장비 제조업                         \r\n032605\t영상 및 음향기기 제조업                          \r\n032606\t마그네틱 및 광학 매체 제조업                     \r\n032701\t의료용 기기 제조업                               \r\n032702\t측정, 시험, 항해, 제어 및 기타 정밀기기 제조업; ?\r\n032703\t안경, 사진장비 및 기타 광학기기 제조업           \r\n032704\t시계 및 시계부품 제조업                          \r\n032801\t전동기, 발전기 및 전기 변환 · 공급 · 제어 장치 \r\n032802\t일차전지 및 축전지 제조업                        \r\n032803\t절연선 및 케이블 제조업                          \r\n032804\t전구 및 조명장치 제조업                          \r\n032805\t가정용 기기 제조업                               \r\n032809\t기타 전기장비 제조업                             \r\n032901\t일반 목적용 기계 제조업                          \r\n032902\t특수 목적용 기계 제조업                          \r\n033001\t자동차용 엔진 및 자동차 제조업                   \r\n033002\t자동차 차체 및 트레일러 제조업                   \r\n033003\t자동차 부품 제조업                               \r\n033101\t선박 및 보트 건조업                              \r\n033102\t철도장비 제조업                                  \r\n033103\t항공기,우주선 및 부품 제조업                     \r\n033109\t그외 기타 운송장비 제조업                        \r\n033201\t가구 제조업                                      \r\n033301\t귀금속 및 장신용품 제조업                        \r\n033302\t악기 제조업                                      \r\n033303\t운동 및 경기용구 제조업                          \r\n033304\t인형,장난감 및 오락용품 제조업                   \r\n033309\t그외 기타 제품 제조업                            \r\n043501\t전기업                                           \r\n043502\t가스 제조 및 배관공급업                          \r\n043503\t증기, 냉온수 및 공기조절 공급업                  \r\n043601\t수도사업                                         \r\n053701\t하수, 폐수 및 분뇨 처리업                        \r\n053801\t폐기물 수집운반업                                \r\n053802\t폐기물 처리업                                    \r\n053803\t금속 및 비금속 원료 재생업                       \r\n053901\t환경 정화 및 복원업                              \r\n064101\t건물 건설업                                      \r\n064102\t토목 건설업                                      \r\n064201\t기반조성 및 시설물 축조관련 전문공사업           \r\n064202\t건물설비 설치 공사업                             \r\n064203\t전기 및 통신 공사업                              \r\n064204\t실내건축 및 건축 마무리 공사업                   \r\n064205\t건설장비 운영업                                  \r\n074501\t자동차 판매업                                    \r\n074502\t자동차 부품 및 내장품 판매업                     \r\n074503\t모터사이클 및 부품 판매업                        \r\n074601\t상품 중개업                                      \r\n074602\t산업용 농축산물 및 산동물 도매업                 \r\n074603\t음·식료품 및 담배 도매업                        \r\n074604\t가정용품 도매업                                  \r\n074605\t기계장비 및 관련 물품 도매업                     \r\n074606\t건축자재, 철물 및 난방장치 도매업                \r\n074607\t기타 전문 도매업                                 \r\n074608\t상품 종합 도매업                                 \r\n074701\t종합 소매업                                      \r\n074702\t음·식료품 및 담배 소매업                        \r\n074703\t정보통신장비 소매업                              \r\n074704\t섬유, 의복, 신발 및 가죽제품 소매업              \r\n074705\t기타 가정용품 소매업                             \r\n074706\t문화, 오락 및 여가 용품 소매업                   \r\n074707\t연료 소매업                                      \r\n074708\t기타 상품 전문 소매업                            \r\n074709\t무점포 소매업                                    \r\n084901\t철도운송업                                       \r\n084902\t육상 여객 운송업                                 \r\n084903\t도로 화물 운송업                                 \r\n084904\t소화물 전문 운송업                               \r\n084905\t파이프라인 운송업                                \r\n085001\t해상 운송업                                      \r\n085002\t내륙 수상 및 항만내 운송업                       \r\n085101\t정기 항공 운송업                                 \r\n085102\t부정기 항공 운송업                               \r\n085201\t보관 및 창고업                                   \r\n085209\t기타 운송관련 서비스업                           \r\n095501\t숙박시설 운영업                                  \r\n095509\t기타 숙박업                                      \r\n095601\t음식점업                                         \r\n095602\t주점 및 비알콜음료점업                           \r\n105801\t서적, 잡지 및 기타 인쇄물 출판업                 \r\n105802\t소프트웨어 개발 및 공급업                        \r\n105901\t영화, 비디오물, 방송프로그램 제작 및 배급업      \r\n105902\t오디오물 출판 및 원판 녹음업                     \r\n106001\t라디오 방송업                                    \r\n106002\t텔레비전 방송업                                  \r\n106101\t우편업                                           \r\n106102\t전기통신업                                       \r\n106201\t컴퓨터 프로그래밍, 시스템 통합 및 관리업         \r\n106301\t자료처리, 호스팅, 포털 및 기타 인터넷 정보매개서?\r\n106309\t기타 정보 서비스업                               \r\n116401\t은행 및 저축기관                                 \r\n116402\t투자기관                                         \r\n116409\t기타 금융업                                      \r\n116501\t보험업                                           \r\n116502\t재 보험업                                        \r\n116503\t연금 및 공제업                                   \r\n116601\t금융지원 서비스업                                \r\n116602\t보험 및 연금관련 서비스업                        \r\n126801\t부동산 임대 및 공급업                            \r\n126802\t부동산 관련 서비스업                             \r\n126901\t운송장비 임대업                                  \r\n126902\t개인 및 가정용품 임대업                          \r\n126903\t산업용 기계 및 장비 임대업                       \r\n126904\t무형재산권 임대업                                \r\n137001\t자연과학 및 공학 연구개발업                      \r\n137002\t인문 및 사회과학 연구개발업                      \r\n137101\t법무관련 서비스업                                \r\n137102\t회계 및 세무관련 서비스업                        \r\n137103\t광고업                                           \r\n137104\t시장조사 및 여론조사업                           \r\n137105\t회사본부, 지주회사 및 경영컨설팅 서비스업        \r\n137201\t건축기술, 엔지니어링 및 관련기술 서비스업        \r\n137209\t기타 과학기술 서비스업                           \r\n137301\t수의업                                           \r\n137302\t전문디자인업                                     \r\n137303\t사진 촬영 및 처리업                              \r\n137309\t그외 기타 전문, 과학 및 기술 서비스업            \r\n147401\t사업시설 유지관리 서비스업                       \r\n147402\t건물·산업설비 청소 및 방제 서비스업             \r\n147403\t조경 관리 및 유지 서비스업                       \r\n147501\t인력공급 및 고용알선업                           \r\n147502\t여행사 및 기타 여행보조 서비스업                 \r\n147503\t경비, 경호 및 탐정업                             \r\n147509\t기타 사업지원 서비스업                           \r\n158401\t입법 및 일반 정부 행정                           \r\n158402\t사회 및 산업정책 행정                            \r\n158403\t외무 및 국방 행정                                \r\n158404\t사법 및 공공질서 행정                            \r\n158405\t사회보장 행정                                    \r\n168501\t초등 교육기관                                    \r\n168502\t중등 교육기관                                    \r\n168503\t고등 교육기관                                    \r\n168504\t특수학교, 외국인학교 및 대안학교                 \r\n168505\t일반 교습 학원                                   \r\n168506\t기타 교육기관                                    \r\n168507\t교육지원 서비스업                                \r\n178601\t병원                                             \r\n178602\t의원                                             \r\n178603\t공중 보건 의료업                                 \r\n178609\t기타 보건업                                      \r\n178701\t거주 복지시설 운영업                             \r\n178702\t비거주 복지시설 운영업                           \r\n189001\t창작 및 예술관련 서비스업                        \r\n189002\t도서관, 사적지 및 유사 여가관련 서비스업         \r\n189101\t스포츠 서비스업                                  \r\n189102\t유원지 및 기타 오락관련 서비스업                 \r\n199401\t산업 및 전문가 단체                              \r\n199402\t노동조합                                         \r\n199409\t기타 협회 및 단체                                \r\n199501\t기계 및 장비 수리업                              \r\n199502\t자동차 및 모터사이클 수리업                      \r\n199503\t개인 및 가정용품 수리업                          \r\n199601\t미용, 욕탕 및 유사 서비스업                      \r\n199609\t그외 기타 개인 서비스업                          \r\n209701\t가구내 고용활동                                  \r\n209801\t자가 소비를 위한 가사 생산 활동                  \r\n209802\t자가 소비를 위한 가사 서비스 활동                \r\n219901\t국제 및 외국기관"
      },
      {
        "element": "idx_bztp_lcls_cd_name",
        "type": "string",
        "required": "Y",
        "description": "표준산업대분류코드\r\n00\t해당사항없음                                                            \r\n01\t농업, 임업 및 어업                                                      \r\n02\t광업                                                                    \r\n03\t제조업                                                                  \r\n04\t전기, 가스, 증기 및 수도사업                                            \r\n05\t하수-폐기물 처리, 원료재생 및환경복원업                                 \r\n06\t건설업                                                                  \r\n07\t도매 및 소매업                                                          \r\n08\t운수업                                                                  \r\n09\t숙박 및 음식점업                                                        \r\n10\t출판, 영상, 방송통신 및 정보서비스업                                    \r\n11\t금융 및 보험업                                                          \r\n12\t부동산업 및 임대업                                                      \r\n13\t전문, 과학 및 기술 서비스업                                             \r\n14\t사업시설관리 및 사업지원서비스업                                        \r\n15\t공공행정, 국방 및 사회보장 행정                                         \r\n16\t교육 서비스업                                                           \r\n17\t보건업 및 사회복지 서비스업                                             \r\n18\t예술, 스포츠 및 여가관련 서비스업                                       \r\n19\t협회 및 단체, 수리 및 기타 개인 서비스업                                \r\n20\t가구내 고용활동 및 달리 분류되지 않은 자가소비생산활동                  \r\n21\t국제 및 외국기관"
      },
      {
        "element": "idx_bztp_mcls_cd_name",
        "type": "string",
        "required": "Y",
        "description": "표준산업중분류코드                                                   \r\n0000\t해당사항없음                                                            \r\n0101\t농업                                                                    \r\n0102\t임업                                                                    \r\n0103\t어업                                                                    \r\n0205\t석탄, 원유 및 천연가스 광업                                             \r\n0206\t금속 광업                                                               \r\n0207\t비금속광물 광업; 연료용 제외                                            \r\n0208\t광업 지원 서비스업                                                      \r\n0310\t식료품 제조업                                                           \r\n0311\t음료 제조업                                                             \r\n0312\t담배 제조업                                                             \r\n0313\t섬유제품 제조업; 의복제외                                               \r\n0314\t의복, 의복액세서리 및 모피제품제조업                                    \r\n0315\t가죽, 가방 및 신발 제조업                                               \r\n0316\t목재 및 나무제품 제조업;가구제외                                        \r\n0317\t펄프, 종이 및 종이제품 제조업                                           \r\n0318\t인쇄 및 기록매체 복제업                                                 \r\n0319\t코크스, 연탄 및 석유정제품 제조업                                       \r\n0320\t화학물질 및 화학제품 제조업;의약품 제외                                 \r\n0321\t의료용 물질 및 의약품 제조업                                            \r\n0322\t고무제품 및 플라스틱제품 제조업                                         \r\n0323\t비금속 광물제품 제조업                                                  \r\n0324\t1차 금속 제조업                                                         \r\n0325\t금속가공제품 제조업;기계 및가구 제외                                    \r\n0326\t전자부품, 컴퓨터, 영상, 음향 및 통신장비 제조업                         \r\n0327\t의료, 정밀, 광학기기 및 시계 제조업                                     \r\n0328\t전기장비 제조업                                                         \r\n0329\t기타 기계 및 장비 제조업                                                \r\n0330\t자동차 및 트레일러 제조업                                               \r\n0331\t기타 운송장비 제조업                                                    \r\n0332\t가구 제조업                                                             \r\n0333\t기타 제품 제조업                                                        \r\n0435\t전기, 가스, 증기 및 공기조절 공급업                                     \r\n0436\t수도사업                                                                \r\n0537\t하수, 폐수 및 분뇨 처리업                                               \r\n0538\t폐기물 수집운반, 처리 및 원료재생업                                     \r\n0539\t환경 정화 및 복원업                                                     \r\n0641\t종합 건설업                                                             \r\n0642\t전문직별 공사업                                                         \r\n0745\t자동차 및 부품 판매업                                                   \r\n0746\t도매 및 상품중개업                                                      \r\n0747\t소매업; 자동차 제외                                                     \r\n0849\t육상운송 및 파이프라인 운송업                                           \r\n0850\t수상 운송업                                                             \r\n0851\t항공 운송업                                                             \r\n0852\t창고 및 운송관련 서비스업                                               \r\n0955\t숙박업                                                                  \r\n0956\t음식점 및 주점업                                                        \r\n1058\t출판업                                                                  \r\n1059\t영상·오디오 기록물 제작 및 배급업                                      \r\n1060\t방송업                                                                  \r\n1061\t통신업                                                                  \r\n1062\t컴퓨터 프로그래밍, 시스템 통합및 관리업                                 \r\n1063\t정보서비스업                                                            \r\n1164\t금융업                                                                  \r\n1165\t보험 및 연금업                                                          \r\n1166\t금융 및 보험 관련 서비스업                                              \r\n1268\t부동산업                                                                \r\n1269\t임대업;부동산 제외                                                      \r\n1370\t연구개발업                                                              \r\n1371\t전문서비스업                                                            \r\n1372\t건축기술, 엔지니어링 및 기타과학기술 서비스업                           \r\n1373\t기타 전문, 과학 및 기술 서비스업                                        \r\n1474\t사업시설 관리 및 조경 서비스업                                          \r\n1475\t사업지원 서비스업                                                       \r\n1584\t공공행정, 국방 및 사회보장 행정                                         \r\n1685\t교육 서비스업                                                           \r\n1786\t보건업                                                                  \r\n1787\t사회복지 서비스업                                                       \r\n1890\t창작, 예술 및 여가관련 서비스업                                         \r\n1891\t스포츠 및 오락관련 서비스업                                             \r\n1994\t협회 및 단체                                                            \r\n1995\t수리업                                                                  \r\n1996\t기타 개인 서비스업                                                      \r\n2097\t가구내 고용활동                                                         \r\n2098\t달리 분류되지 않은 자가소비를 위한가구의 재화 및 서비스 생산활동        \r\n2199\t국제 및 외국기관"
      },
      {
        "element": "idx_bztp_scls_cd_name",
        "type": "string",
        "required": "Y",
        "description": "표준산업소분류코드 참조"
      },
      {
        "element": "ocr_no",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "crfd_item_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "elec_scty_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "issu_istt_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etf_chas_erng_rt_dbnb",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etf_etn_ivst_heed_item_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stln_int_rt_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frnr_psnl_lmt_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lstg_rqsr_issu_istt_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lstg_rqsr_item_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trst_istt_issu_istt_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cptt_trad_tr_psbl_yn",
        "type": "string",
        "required": "Y",
        "description": "NXT 거래가능한 종목은 Y, 그 외 종목은 N"
      },
      {
        "element": "nxt_tr_stop_yn",
        "type": "string",
        "required": "Y",
        "description": "NXT 거래종목 중 거래정지가 된 종목은 Y, 그 외 모든 종목은 N"
      },
      {
        "element": "{\r\n\"PDNO\":\"000660\",\r\n\"PRDT_TYPE_CD\":\"300\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": {\r\n        \"pdno\": \"00000A000660\",\r\n        \"prdt_type_cd\": \"300\",\r\n        \"mket_id_cd\": \"STK\",\r\n        \"scty_grp_id_cd\": \"ST\",\r\n        \"excg_dvsn_cd\": \"02\",\r\n        \"setl_mmdd\": \"12\",\r\n        \"lstg_stqt\": \"728002365\",\r\n        \"lstg_cptl_amt\": \"0\",\r\n        \"cpta\": \"3657652050000\",\r\n        \"papr\": \"5000\",\r\n        \"issu_pric\": \"5000\",\r\n        \"kospi200_item_yn\": \"Y\",\r\n        \"scts_mket_lstg_dt\": \"19961226\",\r\n        \"scts_mket_lstg_abol_dt\": \"\",\r\n        \"kosdaq_mket_lstg_dt\": \"\",\r\n        \"kosdaq_mket_lstg_abol_dt\": \"\",\r\n        \"frbd_mket_lstg_dt\": \"19961226\",\r\n        \"frbd_mket_lstg_abol_dt\": \"\",\r\n        \"reits_kind_cd\": \"\",\r\n        \"etf_dvsn_cd\": \"0\",\r\n        \"oilf_fund_yn\": \"N\",\r\n        \"idx_bztp_lcls_cd\": \"002\",\r\n        \"idx_bztp_mcls_cd\": \"013\",\r\n        \"idx_bztp_scls_cd\": \"013\",\r\n        \"stck_kind_cd\": \"101\",\r\n        \"mfnd_opng_dt\": \"\",\r\n        \"mfnd_end_dt\": \"\",\r\n        \"dpsi_erlm_cncl_dt\": \"\",\r\n        \"etf_cu_qty\": \"0\",\r\n        \"prdt_name\": \"에스케이하이닉스보통주\",\r\n        \"prdt_name120\": \"에스케이하이닉스보통주\",\r\n        \"prdt_abrv_name\": \"SK하이닉스\",\r\n        \"std_pdno\": \"KR7000660001\",\r\n        \"prdt_eng_name\": \"SK hynix\",\r\n        \"prdt_eng_name120\": \"SK hynix\",\r\n        \"prdt_eng_abrv_name\": \"SK hynix\",\r\n        \"dpsi_aptm_erlm_yn\": \"Y\",\r\n        \"etf_txtn_type_cd\": \"00\",\r\n        \"etf_type_cd\": \"\",\r\n        \"lstg_abol_dt\": \"\",\r\n        \"nwst_odst_dvsn_cd\": \"1\",\r\n        \"sbst_pric\": \"115980\",\r\n        \"thco_sbst_pric\": \"115980\",\r\n        \"thco_sbst_pric_chng_dt\": \"20240215\",\r\n        \"tr_stop_yn\": \"N\",\r\n        \"admn_item_yn\": \"N\",\r\n        \"thdt_clpr\": \"146800\",\r\n        \"bfdy_clpr\": \"148700\",\r\n        \"clpr_chng_dt\": \"20240216\",\r\n        \"std_idst_clsf_cd\": \"032601\",\r\n        \"std_idst_clsf_cd_name\": \"반도체 제조업\",\r\n        \"idx_bztp_lcls_cd_name\": \"시가총액규모대\",\r\n        \"idx_bztp_mcls_cd_name\": \"전기,전자\",\r\n        \"idx_bztp_scls_cd_name\": \"전기,전자\",\r\n        \"ocr_no\": \"1147\",\r\n        \"crfd_item_yn\": \"N\",\r\n        \"elec_scty_yn\": \"Y\"\r\n    },\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"KIOK0530\",\r\n    \"msg1\": \"조회되었습니다                                                                  \"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHKST668300C0",
    "name": "국내주식 종목추정실적",
    "url": "/uapi/domestic-stock/v1/quotations/estimate-perform",
    "sheet": "국내주식 종목추정실적",
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
        "element": "sht_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "item_kor_nm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "name1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "name2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "estdate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rcmd_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "capital",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "forn_item_lmtrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "'(추정손익계산서-6개 array)\r\n  매출액, 매출액증감율,\r\n  영업이익, 영업이익증감율,\r\n  순이익, 순이익증감율,'"
      },
      {
        "element": "data1",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data2",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data3",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data4",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data5",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "output3",
        "type": "object array",
        "required": "Y",
        "description": "'(투자지표-8개 array)\r\n  EBITDA(십억원), EPS(원), \r\n  EPS 증감율(0.1%),  PER(배, 0.1%), \r\n  EV/EBITDA(배, 0.1), ROE(0.1%),\r\n  부채비율(0.1%), 이자보상배율(0.1%)'"
      },
      {
        "element": "data1",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data2",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data3",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data4",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "data5",
        "type": "string",
        "required": "Y",
        "description": "결산연월(outblock4) 참조"
      },
      {
        "element": "output4",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "dt",
        "type": "string",
        "required": "Y",
        "description": "DATA1 ~5 결산월 정보"
      },
      {
        "element": "SHT_CD:005930",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"sht_cd\": \"A005930\",\r\n        \"item_kor_nm\": \"삼성전자\",\r\n        \"name1\": \"김한국\",\r\n        \"name2\": \"\",\r\n        \"estdate\": \"20240109\",\r\n        \"rcmd_name\": \"매수\",\r\n        \"capital\": \"8975.0\",\r\n        \"forn_item_lmtrt\": \"0.00\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"data1\": \"2796048.0\",\r\n            \"data2\": \"3022314.0\",\r\n            \"data3\": \"2581509.0\",\r\n            \"data4\": \"3048945.0\",\r\n            \"data5\": \"3295675.0\"\r\n        },\r\n        {\r\n            \"data1\": \"181.0\",\r\n            \"data2\": \"81.0\",\r\n            \"data3\": \"-146.0\",\r\n            \"data4\": \"181.0\",\r\n            \"data5\": \"81.0\"\r\n        },\r\n        {\r\n            \"data1\": \"516339.0\",\r\n            \"data2\": \"433766.0\",\r\n            \"data3\": \"65405.0\",\r\n            \"data4\": \"330172.0\",\r\n            \"data5\": \"555410.0\"\r\n        },\r\n        {\r\n            \"data1\": \"435.0\",\r\n            \"data2\": \"-160.0\",\r\n            \"data3\": \"-849.0\",\r\n            \"data4\": \"4048.0\",\r\n            \"data5\": \"682.0\"\r\n        },\r\n        {\r\n            \"data1\": \"392438.0\",\r\n            \"data2\": \"547300.0\",\r\n            \"data3\": \"106144.0\",\r\n            \"data4\": \"253332.0\",\r\n            \"data5\": \"422055.0\"\r\n        },\r\n        {\r\n            \"data1\": \"504.0\",\r\n            \"data2\": \"395.0\",\r\n            \"data3\": \"-806.0\",\r\n            \"data4\": \"1387.0\",\r\n            \"data5\": \"666.0\"\r\n        }\r\n    ],\r\n    \"output3\": [\r\n        {\r\n            \"data1\": \"858812.0\",\r\n            \"data2\": \"824843.0\",\r\n            \"data3\": \"483199.0\",\r\n            \"data4\": \"792602.0\",\r\n            \"data5\": \"1043367.0\"\r\n        },\r\n        {\r\n            \"data1\": \"57770.0\",\r\n            \"data2\": \"80570.0\",\r\n            \"data3\": \"15609.0\",\r\n            \"data4\": \"36983.0\",\r\n            \"data5\": \"61483.0\"\r\n        },\r\n        {\r\n            \"data1\": \"504.0\",\r\n            \"data2\": \"395.0\",\r\n            \"data3\": \"-806.0\",\r\n            \"data4\": \"1369.0\",\r\n            \"data5\": \"662.0\"\r\n        },\r\n        {\r\n            \"data1\": \"136.0\",\r\n            \"data2\": \"69.0\",\r\n            \"data3\": \"503.0\",\r\n            \"data4\": \"207.0\",\r\n            \"data5\": \"124.0\"\r\n        },\r\n        {\r\n            \"data1\": \"50.0\",\r\n            \"data2\": \"34.0\",\r\n            \"data3\": \"95.0\",\r\n            \"data4\": \"53.0\",\r\n            \"data5\": \"39.0\"\r\n        },\r\n        {\r\n            \"data1\": \"139.0\",\r\n            \"data2\": \"171.0\",\r\n            \"data3\": \"31.0\",\r\n            \"data4\": \"70.0\",\r\n            \"data5\": \"109.0\"\r\n        },\r\n        {\r\n            \"data1\": \"399.0\",\r\n            \"data2\": \"264.0\",\r\n            \"data3\": \"255.0\",\r\n            \"data4\": \"226.0\",\r\n            \"data5\": \"163.0\"\r\n        },\r\n        {\r\n            \"data1\": \"1197.0\",\r\n            \"data2\": \"568.0\",\r\n            \"data3\": \"58.0\",\r\n            \"data4\": \"232.0\",\r\n            \"data5\": \"655.0\"\r\n        }\r\n    ],\r\n    \"output4\": [\r\n        {\r\n            \"dt\": \"2021.12\"\r\n        },\r\n        {\r\n            \"dt\": \"2022.12\"\r\n        },\r\n        {\r\n            \"dt\": \"2023.12E\"\r\n        },\r\n        {\r\n            \"dt\": \"2024.12E\"\r\n        },\r\n        {\r\n            \"dt\": \"2025.12E\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPPG04600101",
    "name": "프로그램매매 종합현황(시간)",
    "url": "/uapi/domestic-stock/v1/quotations/comp-program-trade-today",
    "sheet": "프로그램매매 종합현황(시간)",
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
        "element": "bsop_hour",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_shun_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_shun_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_MRKT_CLS_CODE:Q\r\nFID_SCTN_CLS_CODE:1\r\nFID_INPUT_ISCD:\r\nFID_COND_MRKT_DIV_CODE1:\r\nFID_INPUT_HOUR_1:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"bsop_hour\": \"170000\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981823\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859384\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136289\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165900\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165800\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165700\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165600\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165500\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165400\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165300\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165200\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165100\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"165000\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981818\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859379\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136284\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164900\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164800\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164700\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164600\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164500\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164400\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164300\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164200\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164100\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"164000\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122439\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981808\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859370\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136274\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163900\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163800\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163700\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163600\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163500\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163400\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163300\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163200\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"163100\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"63370\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"0.58\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"340275\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"3.11\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2122437\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.40\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2981781\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"27.25\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"276905\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"2.53\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"859343\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"7.85\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"1136248\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"10.39\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST04760000",
    "name": "국내주식 신용잔고 일별추이",
    "url": "/uapi/domestic-stock/v1/quotations/daily-credit-balance",
    "sheet": "국내주식 신용잔고 일별추이",
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
        "element": "deal_date",
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
        "element": "stlm_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_loan_new_stcn",
        "type": "string",
        "required": "Y",
        "description": "단위: 주"
      },
      {
        "element": "whol_loan_rdmp_stcn",
        "type": "string",
        "required": "Y",
        "description": "단위: 주"
      },
      {
        "element": "whol_loan_rmnd_stcn",
        "type": "string",
        "required": "Y",
        "description": "단위: 주"
      },
      {
        "element": "whol_loan_new_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 만원"
      },
      {
        "element": "whol_loan_rdmp_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 만원"
      },
      {
        "element": "whol_loan_rmnd_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 만원"
      },
      {
        "element": "whol_loan_rmnd_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_loan_gvrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_stln_new_stcn",
        "type": "string",
        "required": "Y",
        "description": "단위: 주"
      },
      {
        "element": "whol_stln_rdmp_stcn",
        "type": "string",
        "required": "Y",
        "description": "단위: 주"
      },
      {
        "element": "whol_stln_rmnd_stcn",
        "type": "string",
        "required": "Y",
        "description": "단위: 주"
      },
      {
        "element": "whol_stln_new_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 만원"
      },
      {
        "element": "whol_stln_rdmp_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 만원"
      },
      {
        "element": "whol_stln_rmnd_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 만원"
      },
      {
        "element": "whol_stln_rmnd_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_stln_gvrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"J\",\r\n\"fid_cond_scr_div_code\":\"20476\",\r\n\"fid_input_iscd\":\"005930\",\r\n\"fid_input_date_1\":\"20240315\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"deal_date\": \"20240313\",\r\n            \"stck_prpr\": \"74100\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"800\",\r\n            \"prdy_ctrt\": \"1.09\",\r\n            \"acml_vol\": \"15243134\",\r\n            \"stlm_date\": \"20240315\",\r\n            \"whol_loan_new_stcn\": \"253817\",\r\n            \"whol_loan_rdmp_stcn\": \"603451\",\r\n            \"whol_loan_rmnd_stcn\": \"7155720\",\r\n            \"whol_loan_new_amt\": \"1678904\",\r\n            \"whol_loan_rdmp_amt\": \"3982732\",\r\n            \"whol_loan_rmnd_amt\": \"47321639\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"1.65\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6861\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43104\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73700\",\r\n            \"stck_hgpr\": \"74100\",\r\n            \"stck_lwpr\": \"73500\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240312\",\r\n            \"stck_prpr\": \"73300\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"900\",\r\n            \"prdy_ctrt\": \"1.24\",\r\n            \"acml_vol\": \"13011654\",\r\n            \"stlm_date\": \"20240314\",\r\n            \"whol_loan_new_stcn\": \"357971\",\r\n            \"whol_loan_rdmp_stcn\": \"429002\",\r\n            \"whol_loan_rmnd_stcn\": \"7507526\",\r\n            \"whol_loan_new_amt\": \"2370294\",\r\n            \"whol_loan_rdmp_amt\": \"2871401\",\r\n            \"whol_loan_rmnd_amt\": \"49639923\",\r\n            \"whol_loan_rmnd_rate\": \"0.12\",\r\n            \"whol_loan_gvrt\": \"2.74\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6861\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43104\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72600\",\r\n            \"stck_hgpr\": \"73500\",\r\n            \"stck_lwpr\": \"72100\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240311\",\r\n            \"stck_prpr\": \"72400\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-900\",\r\n            \"prdy_ctrt\": \"-1.23\",\r\n            \"acml_vol\": \"9740504\",\r\n            \"stlm_date\": \"20240313\",\r\n            \"whol_loan_new_stcn\": \"395234\",\r\n            \"whol_loan_rdmp_stcn\": \"242330\",\r\n            \"whol_loan_rmnd_stcn\": \"7586197\",\r\n            \"whol_loan_new_amt\": \"2579480\",\r\n            \"whol_loan_rdmp_amt\": \"1479272\",\r\n            \"whol_loan_rmnd_amt\": \"50194590\",\r\n            \"whol_loan_rmnd_rate\": \"0.12\",\r\n            \"whol_loan_gvrt\": \"4.05\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6861\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43104\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72900\",\r\n            \"stck_hgpr\": \"73100\",\r\n            \"stck_lwpr\": \"72300\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240308\",\r\n            \"stck_prpr\": \"73300\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1100\",\r\n            \"prdy_ctrt\": \"1.52\",\r\n            \"acml_vol\": \"19271349\",\r\n            \"stlm_date\": \"20240312\",\r\n            \"whol_loan_new_stcn\": \"350421\",\r\n            \"whol_loan_rdmp_stcn\": \"580071\",\r\n            \"whol_loan_rmnd_stcn\": \"7433714\",\r\n            \"whol_loan_new_amt\": \"2212537\",\r\n            \"whol_loan_rdmp_amt\": \"3786566\",\r\n            \"whol_loan_rmnd_amt\": \"49096831\",\r\n            \"whol_loan_rmnd_rate\": \"0.12\",\r\n            \"whol_loan_gvrt\": \"1.81\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6861\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43104\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72800\",\r\n            \"stck_hgpr\": \"73400\",\r\n            \"stck_lwpr\": \"72600\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240307\",\r\n            \"stck_prpr\": \"72200\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-700\",\r\n            \"prdy_ctrt\": \"-0.96\",\r\n            \"acml_vol\": \"14516963\",\r\n            \"stlm_date\": \"20240311\",\r\n            \"whol_loan_new_stcn\": \"497407\",\r\n            \"whol_loan_rdmp_stcn\": \"252707\",\r\n            \"whol_loan_rmnd_stcn\": \"7666721\",\r\n            \"whol_loan_new_amt\": \"3207234\",\r\n            \"whol_loan_rdmp_amt\": \"1692347\",\r\n            \"whol_loan_rmnd_amt\": \"50691156\",\r\n            \"whol_loan_rmnd_rate\": \"0.12\",\r\n            \"whol_loan_gvrt\": \"3.42\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"1\",\r\n            \"whol_stln_rmnd_stcn\": \"6861\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"7\",\r\n            \"whol_stln_rmnd_amt\": \"43104\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73100\",\r\n            \"stck_hgpr\": \"73300\",\r\n            \"stck_lwpr\": \"72200\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240306\",\r\n            \"stck_prpr\": \"72900\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-800\",\r\n            \"prdy_ctrt\": \"-1.09\",\r\n            \"acml_vol\": \"21547905\",\r\n            \"stlm_date\": \"20240308\",\r\n            \"whol_loan_new_stcn\": \"619036\",\r\n            \"whol_loan_rdmp_stcn\": \"176578\",\r\n            \"whol_loan_rmnd_stcn\": \"7424246\",\r\n            \"whol_loan_new_amt\": \"4069217\",\r\n            \"whol_loan_rdmp_amt\": \"1148738\",\r\n            \"whol_loan_rmnd_amt\": \"49189736\",\r\n            \"whol_loan_rmnd_rate\": \"0.12\",\r\n            \"whol_loan_gvrt\": \"2.87\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6862\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43111\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73200\",\r\n            \"stck_hgpr\": \"73500\",\r\n            \"stck_lwpr\": \"72700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240305\",\r\n            \"stck_prpr\": \"73700\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-1200\",\r\n            \"prdy_ctrt\": \"-1.60\",\r\n            \"acml_vol\": \"19505125\",\r\n            \"stlm_date\": \"20240307\",\r\n            \"whol_loan_new_stcn\": \"422627\",\r\n            \"whol_loan_rdmp_stcn\": \"301232\",\r\n            \"whol_loan_rmnd_stcn\": \"6981765\",\r\n            \"whol_loan_new_amt\": \"2822363\",\r\n            \"whol_loan_rdmp_amt\": \"1986157\",\r\n            \"whol_loan_rmnd_amt\": \"46269511\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"2.15\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"20\",\r\n            \"whol_stln_rmnd_stcn\": \"6862\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"139\",\r\n            \"whol_stln_rmnd_amt\": \"43111\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74600\",\r\n            \"stck_hgpr\": \"74800\",\r\n            \"stck_lwpr\": \"73700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240304\",\r\n            \"stck_prpr\": \"74900\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1500\",\r\n            \"prdy_ctrt\": \"2.04\",\r\n            \"acml_vol\": \"23210474\",\r\n            \"stlm_date\": \"20240306\",\r\n            \"whol_loan_new_stcn\": \"838785\",\r\n            \"whol_loan_rdmp_stcn\": \"1450926\",\r\n            \"whol_loan_rmnd_stcn\": \"6862995\",\r\n            \"whol_loan_new_amt\": \"5536867\",\r\n            \"whol_loan_rdmp_amt\": \"9135415\",\r\n            \"whol_loan_rmnd_amt\": \"45449103\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"3.61\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74300\",\r\n            \"stck_hgpr\": \"75000\",\r\n            \"stck_lwpr\": \"74000\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240229\",\r\n            \"stck_prpr\": \"73400\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"200\",\r\n            \"prdy_ctrt\": \"0.27\",\r\n            \"acml_vol\": \"21176403\",\r\n            \"stlm_date\": \"20240305\",\r\n            \"whol_loan_new_stcn\": \"563158\",\r\n            \"whol_loan_rdmp_stcn\": \"330265\",\r\n            \"whol_loan_rmnd_stcn\": \"7477578\",\r\n            \"whol_loan_new_amt\": \"3366177\",\r\n            \"whol_loan_rdmp_amt\": \"2109787\",\r\n            \"whol_loan_rmnd_amt\": \"49063520\",\r\n            \"whol_loan_rmnd_rate\": \"0.12\",\r\n            \"whol_loan_gvrt\": \"2.65\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72600\",\r\n            \"stck_hgpr\": \"73400\",\r\n            \"stck_lwpr\": \"72000\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240228\",\r\n            \"stck_prpr\": \"73200\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"11795859\",\r\n            \"stlm_date\": \"20240304\",\r\n            \"whol_loan_new_stcn\": \"506896\",\r\n            \"whol_loan_rdmp_stcn\": \"458211\",\r\n            \"whol_loan_rmnd_stcn\": \"7245825\",\r\n            \"whol_loan_new_amt\": \"3059090\",\r\n            \"whol_loan_rdmp_amt\": \"2956451\",\r\n            \"whol_loan_rmnd_amt\": \"47813948\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"4.29\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72900\",\r\n            \"stck_hgpr\": \"73900\",\r\n            \"stck_lwpr\": \"72800\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240227\",\r\n            \"stck_prpr\": \"72900\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_ctrt\": \"0.14\",\r\n            \"acml_vol\": \"13201981\",\r\n            \"stlm_date\": \"20240229\",\r\n            \"whol_loan_new_stcn\": \"319365\",\r\n            \"whol_loan_rdmp_stcn\": \"291088\",\r\n            \"whol_loan_rmnd_stcn\": \"7199469\",\r\n            \"whol_loan_new_amt\": \"2086955\",\r\n            \"whol_loan_rdmp_amt\": \"1907718\",\r\n            \"whol_loan_rmnd_amt\": \"47725597\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"2.41\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73100\",\r\n            \"stck_hgpr\": \"73400\",\r\n            \"stck_lwpr\": \"72700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240226\",\r\n            \"stck_prpr\": \"72800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-100\",\r\n            \"prdy_ctrt\": \"-0.14\",\r\n            \"acml_vol\": \"14669352\",\r\n            \"stlm_date\": \"20240228\",\r\n            \"whol_loan_new_stcn\": \"282018\",\r\n            \"whol_loan_rdmp_stcn\": \"261288\",\r\n            \"whol_loan_rmnd_stcn\": \"7171604\",\r\n            \"whol_loan_new_amt\": \"1838364\",\r\n            \"whol_loan_rdmp_amt\": \"1639156\",\r\n            \"whol_loan_rmnd_amt\": \"47549260\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"1.91\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72300\",\r\n            \"stck_hgpr\": \"73200\",\r\n            \"stck_lwpr\": \"72200\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240223\",\r\n            \"stck_prpr\": \"72900\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-200\",\r\n            \"prdy_ctrt\": \"-0.27\",\r\n            \"acml_vol\": \"16225166\",\r\n            \"stlm_date\": \"20240227\",\r\n            \"whol_loan_new_stcn\": \"526563\",\r\n            \"whol_loan_rdmp_stcn\": \"473526\",\r\n            \"whol_loan_rmnd_stcn\": \"7151330\",\r\n            \"whol_loan_new_amt\": \"3397702\",\r\n            \"whol_loan_rdmp_amt\": \"3122338\",\r\n            \"whol_loan_rmnd_amt\": \"47353285\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"3.23\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73600\",\r\n            \"stck_hgpr\": \"74200\",\r\n            \"stck_lwpr\": \"72900\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240222\",\r\n            \"stck_prpr\": \"73100\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_ctrt\": \"0.14\",\r\n            \"acml_vol\": \"15208934\",\r\n            \"stlm_date\": \"20240226\",\r\n            \"whol_loan_new_stcn\": \"617034\",\r\n            \"whol_loan_rdmp_stcn\": \"362458\",\r\n            \"whol_loan_rmnd_stcn\": \"7098784\",\r\n            \"whol_loan_new_amt\": \"4055099\",\r\n            \"whol_loan_rdmp_amt\": \"2420852\",\r\n            \"whol_loan_rmnd_amt\": \"47080801\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"4.05\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73800\",\r\n            \"stck_hgpr\": \"73900\",\r\n            \"stck_lwpr\": \"72700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240221\",\r\n            \"stck_prpr\": \"73000\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-300\",\r\n            \"prdy_ctrt\": \"-0.41\",\r\n            \"acml_vol\": \"11503495\",\r\n            \"stlm_date\": \"20240223\",\r\n            \"whol_loan_new_stcn\": \"181753\",\r\n            \"whol_loan_rdmp_stcn\": \"159505\",\r\n            \"whol_loan_rmnd_stcn\": \"6849915\",\r\n            \"whol_loan_new_amt\": \"1154019\",\r\n            \"whol_loan_rdmp_amt\": \"997307\",\r\n            \"whol_loan_rmnd_amt\": \"45485001\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"1.57\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73400\",\r\n            \"stck_hgpr\": \"73700\",\r\n            \"stck_lwpr\": \"72900\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240220\",\r\n            \"stck_prpr\": \"73300\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-500\",\r\n            \"prdy_ctrt\": \"-0.68\",\r\n            \"acml_vol\": \"14681477\",\r\n            \"stlm_date\": \"20240222\",\r\n            \"whol_loan_new_stcn\": \"245659\",\r\n            \"whol_loan_rdmp_stcn\": \"162302\",\r\n            \"whol_loan_rmnd_stcn\": \"6827253\",\r\n            \"whol_loan_new_amt\": \"1650740\",\r\n            \"whol_loan_rdmp_amt\": \"1053242\",\r\n            \"whol_loan_rmnd_amt\": \"45325256\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"1.66\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"100\",\r\n            \"whol_stln_rmnd_stcn\": \"6882\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"699\",\r\n            \"whol_stln_rmnd_amt\": \"43251\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73700\",\r\n            \"stck_hgpr\": \"73700\",\r\n            \"stck_lwpr\": \"72800\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240219\",\r\n            \"stck_prpr\": \"73800\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1000\",\r\n            \"prdy_ctrt\": \"1.37\",\r\n            \"acml_vol\": \"12726404\",\r\n            \"stlm_date\": \"20240221\",\r\n            \"whol_loan_new_stcn\": \"196561\",\r\n            \"whol_loan_rdmp_stcn\": \"395332\",\r\n            \"whol_loan_rmnd_stcn\": \"6746234\",\r\n            \"whol_loan_new_amt\": \"1233245\",\r\n            \"whol_loan_rdmp_amt\": \"2617252\",\r\n            \"whol_loan_rmnd_amt\": \"44744474\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"1.53\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"15\",\r\n            \"whol_stln_rmnd_stcn\": \"6982\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"105\",\r\n            \"whol_stln_rmnd_amt\": \"43950\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"72800\",\r\n            \"stck_hgpr\": \"73900\",\r\n            \"stck_lwpr\": \"72800\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240216\",\r\n            \"stck_prpr\": \"72800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-200\",\r\n            \"prdy_ctrt\": \"-0.27\",\r\n            \"acml_vol\": \"13444781\",\r\n            \"stlm_date\": \"20240220\",\r\n            \"whol_loan_new_stcn\": \"353711\",\r\n            \"whol_loan_rdmp_stcn\": \"258304\",\r\n            \"whol_loan_rmnd_stcn\": \"6946822\",\r\n            \"whol_loan_new_amt\": \"2336237\",\r\n            \"whol_loan_rdmp_amt\": \"1746554\",\r\n            \"whol_loan_rmnd_amt\": \"46141630\",\r\n            \"whol_loan_rmnd_rate\": \"0.11\",\r\n            \"whol_loan_gvrt\": \"2.63\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6997\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"44055\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73300\",\r\n            \"stck_hgpr\": \"73400\",\r\n            \"stck_lwpr\": \"72500\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240215\",\r\n            \"stck_prpr\": \"73000\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-1000\",\r\n            \"prdy_ctrt\": \"-1.35\",\r\n            \"acml_vol\": \"14120600\",\r\n            \"stlm_date\": \"20240219\",\r\n            \"whol_loan_new_stcn\": \"668521\",\r\n            \"whol_loan_rdmp_stcn\": \"244617\",\r\n            \"whol_loan_rmnd_stcn\": \"6851613\",\r\n            \"whol_loan_new_amt\": \"4541397\",\r\n            \"whol_loan_rdmp_amt\": \"1581331\",\r\n            \"whol_loan_rmnd_amt\": \"45553486\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"4.72\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6997\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"44055\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74200\",\r\n            \"stck_hgpr\": \"74400\",\r\n            \"stck_lwpr\": \"73000\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240214\",\r\n            \"stck_prpr\": \"74000\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-1200\",\r\n            \"prdy_ctrt\": \"-1.60\",\r\n            \"acml_vol\": \"12434945\",\r\n            \"stlm_date\": \"20240216\",\r\n            \"whol_loan_new_stcn\": \"607994\",\r\n            \"whol_loan_rdmp_stcn\": \"168766\",\r\n            \"whol_loan_rmnd_stcn\": \"6428256\",\r\n            \"whol_loan_new_amt\": \"4042856\",\r\n            \"whol_loan_rdmp_amt\": \"1140083\",\r\n            \"whol_loan_rmnd_amt\": \"42597320\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"4.88\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"6997\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"44055\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73700\",\r\n            \"stck_hgpr\": \"74300\",\r\n            \"stck_lwpr\": \"73700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240213\",\r\n            \"stck_prpr\": \"75200\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1100\",\r\n            \"prdy_ctrt\": \"1.48\",\r\n            \"acml_vol\": \"21966745\",\r\n            \"stlm_date\": \"20240215\",\r\n            \"whol_loan_new_stcn\": \"510482\",\r\n            \"whol_loan_rdmp_stcn\": \"766361\",\r\n            \"whol_loan_rmnd_stcn\": \"5989340\",\r\n            \"whol_loan_new_amt\": \"2751983\",\r\n            \"whol_loan_rdmp_amt\": \"4536820\",\r\n            \"whol_loan_rmnd_amt\": \"39696538\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"2.32\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"139\",\r\n            \"whol_stln_rmnd_stcn\": \"6997\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"996\",\r\n            \"whol_stln_rmnd_amt\": \"44055\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74800\",\r\n            \"stck_hgpr\": \"75200\",\r\n            \"stck_lwpr\": \"74400\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240208\",\r\n            \"stck_prpr\": \"74100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-900\",\r\n            \"prdy_ctrt\": \"-1.20\",\r\n            \"acml_vol\": \"20810708\",\r\n            \"stlm_date\": \"20240214\",\r\n            \"whol_loan_new_stcn\": \"943012\",\r\n            \"whol_loan_rdmp_stcn\": \"549849\",\r\n            \"whol_loan_rmnd_stcn\": \"6247522\",\r\n            \"whol_loan_new_amt\": \"5594562\",\r\n            \"whol_loan_rdmp_amt\": \"2907687\",\r\n            \"whol_loan_rmnd_amt\": \"41495520\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"4.52\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"1\",\r\n            \"whol_stln_rmnd_stcn\": \"7136\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"6\",\r\n            \"whol_stln_rmnd_amt\": \"45052\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"75000\",\r\n            \"stck_hgpr\": \"75200\",\r\n            \"stck_lwpr\": \"73600\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240207\",\r\n            \"stck_prpr\": \"75000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"600\",\r\n            \"prdy_ctrt\": \"0.81\",\r\n            \"acml_vol\": \"16566445\",\r\n            \"stlm_date\": \"20240213\",\r\n            \"whol_loan_new_stcn\": \"252078\",\r\n            \"whol_loan_rdmp_stcn\": \"439983\",\r\n            \"whol_loan_rmnd_stcn\": \"5856240\",\r\n            \"whol_loan_new_amt\": \"1614166\",\r\n            \"whol_loan_rdmp_amt\": \"2860455\",\r\n            \"whol_loan_rmnd_amt\": \"38821115\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"1.51\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"7137\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"45059\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74600\",\r\n            \"stck_hgpr\": \"75500\",\r\n            \"stck_lwpr\": \"74300\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240206\",\r\n            \"stck_prpr\": \"74400\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_ctrt\": \"0.13\",\r\n            \"acml_vol\": \"14559254\",\r\n            \"stlm_date\": \"20240208\",\r\n            \"whol_loan_new_stcn\": \"295323\",\r\n            \"whol_loan_rdmp_stcn\": \"281735\",\r\n            \"whol_loan_rmnd_stcn\": \"6045644\",\r\n            \"whol_loan_new_amt\": \"1941262\",\r\n            \"whol_loan_rdmp_amt\": \"1889253\",\r\n            \"whol_loan_rmnd_amt\": \"40074751\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"2.02\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"0\",\r\n            \"whol_stln_rmnd_stcn\": \"7137\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"0\",\r\n            \"whol_stln_rmnd_amt\": \"45059\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74300\",\r\n            \"stck_hgpr\": \"74700\",\r\n            \"stck_lwpr\": \"73300\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240205\",\r\n            \"stck_prpr\": \"74300\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-900\",\r\n            \"prdy_ctrt\": \"-1.20\",\r\n            \"acml_vol\": \"19026021\",\r\n            \"stlm_date\": \"20240207\",\r\n            \"whol_loan_new_stcn\": \"580976\",\r\n            \"whol_loan_rdmp_stcn\": \"315236\",\r\n            \"whol_loan_rmnd_stcn\": \"6035531\",\r\n            \"whol_loan_new_amt\": \"3882685\",\r\n            \"whol_loan_rdmp_amt\": \"2127798\",\r\n            \"whol_loan_rmnd_amt\": \"40047278\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"3.04\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"728\",\r\n            \"whol_stln_rmnd_stcn\": \"7137\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"5099\",\r\n            \"whol_stln_rmnd_amt\": \"45059\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74200\",\r\n            \"stck_hgpr\": \"74800\",\r\n            \"stck_lwpr\": \"73500\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240202\",\r\n            \"stck_prpr\": \"75200\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1600\",\r\n            \"prdy_ctrt\": \"2.17\",\r\n            \"acml_vol\": \"14955881\",\r\n            \"stlm_date\": \"20240206\",\r\n            \"whol_loan_new_stcn\": \"227532\",\r\n            \"whol_loan_rdmp_stcn\": \"559999\",\r\n            \"whol_loan_rmnd_stcn\": \"5770153\",\r\n            \"whol_loan_new_amt\": \"1423587\",\r\n            \"whol_loan_rdmp_amt\": \"3552220\",\r\n            \"whol_loan_rmnd_amt\": \"38294939\",\r\n            \"whol_loan_rmnd_rate\": \"0.08\",\r\n            \"whol_loan_gvrt\": \"1.52\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"8\",\r\n            \"whol_stln_rmnd_stcn\": \"7865\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"55\",\r\n            \"whol_stln_rmnd_amt\": \"50158\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"74000\",\r\n            \"stck_hgpr\": \"75200\",\r\n            \"stck_lwpr\": \"73700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240201\",\r\n            \"stck_prpr\": \"73600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"900\",\r\n            \"prdy_ctrt\": \"1.24\",\r\n            \"acml_vol\": \"19881033\",\r\n            \"stlm_date\": \"20240205\",\r\n            \"whol_loan_new_stcn\": \"340408\",\r\n            \"whol_loan_rdmp_stcn\": \"432474\",\r\n            \"whol_loan_rmnd_stcn\": \"6103384\",\r\n            \"whol_loan_new_amt\": \"2222626\",\r\n            \"whol_loan_rdmp_amt\": \"2835418\",\r\n            \"whol_loan_rmnd_amt\": \"40428694\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"1.70\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"347\",\r\n            \"whol_stln_rmnd_stcn\": \"7873\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"2376\",\r\n            \"whol_stln_rmnd_amt\": \"50214\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73000\",\r\n            \"stck_hgpr\": \"74200\",\r\n            \"stck_lwpr\": \"72900\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240131\",\r\n            \"stck_prpr\": \"72700\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-1600\",\r\n            \"prdy_ctrt\": \"-2.15\",\r\n            \"acml_vol\": \"15703560\",\r\n            \"stlm_date\": \"20240202\",\r\n            \"whol_loan_new_stcn\": \"401245\",\r\n            \"whol_loan_rdmp_stcn\": \"234735\",\r\n            \"whol_loan_rmnd_stcn\": \"6207574\",\r\n            \"whol_loan_new_amt\": \"2627294\",\r\n            \"whol_loan_rdmp_amt\": \"1541985\",\r\n            \"whol_loan_rmnd_amt\": \"41122407\",\r\n            \"whol_loan_rmnd_rate\": \"0.10\",\r\n            \"whol_loan_gvrt\": \"2.55\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"30\",\r\n            \"whol_stln_rmnd_stcn\": \"8220\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"204\",\r\n            \"whol_stln_rmnd_amt\": \"52590\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73400\",\r\n            \"stck_hgpr\": \"74000\",\r\n            \"stck_lwpr\": \"72500\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240130\",\r\n            \"stck_prpr\": \"74300\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-100\",\r\n            \"prdy_ctrt\": \"-0.13\",\r\n            \"acml_vol\": \"12244418\",\r\n            \"stlm_date\": \"20240201\",\r\n            \"whol_loan_new_stcn\": \"308957\",\r\n            \"whol_loan_rdmp_stcn\": \"165640\",\r\n            \"whol_loan_rmnd_stcn\": \"6042179\",\r\n            \"whol_loan_new_amt\": \"1980096\",\r\n            \"whol_loan_rdmp_amt\": \"1089607\",\r\n            \"whol_loan_rmnd_amt\": \"40044649\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"2.51\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"894\",\r\n            \"whol_stln_rmnd_stcn\": \"8250\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"5983\",\r\n            \"whol_stln_rmnd_amt\": \"52795\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"75000\",\r\n            \"stck_hgpr\": \"75300\",\r\n            \"stck_lwpr\": \"73700\"\r\n        },\r\n        {\r\n            \"deal_date\": \"20240129\",\r\n            \"stck_prpr\": \"74400\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1000\",\r\n            \"prdy_ctrt\": \"1.36\",\r\n            \"acml_vol\": \"13976521\",\r\n            \"stlm_date\": \"20240131\",\r\n            \"whol_loan_new_stcn\": \"207309\",\r\n            \"whol_loan_rdmp_stcn\": \"415351\",\r\n            \"whol_loan_rmnd_stcn\": \"5901536\",\r\n            \"whol_loan_new_amt\": \"1397554\",\r\n            \"whol_loan_rdmp_amt\": \"2745405\",\r\n            \"whol_loan_rmnd_amt\": \"39169933\",\r\n            \"whol_loan_rmnd_rate\": \"0.09\",\r\n            \"whol_loan_gvrt\": \"1.47\",\r\n            \"whol_stln_new_stcn\": \"0\",\r\n            \"whol_stln_rdmp_stcn\": \"39\",\r\n            \"whol_stln_rmnd_stcn\": \"9144\",\r\n            \"whol_stln_new_amt\": \"0\",\r\n            \"whol_stln_rdmp_amt\": \"261\",\r\n            \"whol_stln_rmnd_amt\": \"58779\",\r\n            \"whol_stln_rmnd_rate\": \"0.00\",\r\n            \"whol_stln_gvrt\": \"0.00\",\r\n            \"stck_oprc\": \"73800\",\r\n            \"stck_hgpr\": \"75200\",\r\n            \"stck_lwpr\": \"73500\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPTJ04040000",
    "name": "시장별 투자자매매동향(일별)",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-investor-daily-by-market",
    "sheet": "시장별 투자자매매동향(일별)",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_ntby_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_ntby_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:U\r\nFID_INPUT_ISCD:0001\r\nFID_INPUT_DATE_1:20240517\r\nFID_INPUT_ISCD_1:KSP",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240517\",\r\n            \"bstp_nmix_prpr\": \"2724.62\",\r\n            \"bstp_nmix_prdy_vrss\": \"-28.38\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"bstp_nmix_prdy_ctrt\": \"-1.03\",\r\n            \"bstp_nmix_oprc\": \"2751.47\",\r\n            \"bstp_nmix_hgpr\": \"2752.17\",\r\n            \"bstp_nmix_lwpr\": \"2724.62\",\r\n            \"stck_prdy_clpr\": \"2753.00\",\r\n            \"frgn_ntby_qty\": \"-18565\",\r\n            \"frgn_reg_ntby_qty\": \"-18009\",\r\n            \"frgn_nreg_ntby_qty\": \"-557\",\r\n            \"prsn_ntby_qty\": \"22524\",\r\n            \"orgn_ntby_qty\": \"-4738\",\r\n            \"scrt_ntby_qty\": \"-1148\",\r\n            \"ivtr_ntby_qty\": \"-609\",\r\n            \"pe_fund_ntby_vol\": \"-431\",\r\n            \"bank_ntby_qty\": \"103\",\r\n            \"insu_ntby_qty\": \"-156\",\r\n            \"mrbn_ntby_qty\": \"-175\",\r\n            \"fund_ntby_qty\": \"-2322\",\r\n            \"etc_ntby_qty\": \"779\",\r\n            \"etc_orgt_ntby_vol\": \"0\",\r\n            \"etc_corp_ntby_vol\": \"779\",\r\n            \"frgn_ntby_tr_pbmn\": \"-597490\",\r\n            \"frgn_reg_ntby_pbmn\": \"-597676\",\r\n            \"frgn_nreg_ntby_pbmn\": \"186\",\r\n            \"prsn_ntby_tr_pbmn\": \"720787\",\r\n            \"orgn_ntby_tr_pbmn\": \"-150685\",\r\n            \"scrt_ntby_tr_pbmn\": \"-18893\",\r\n            \"ivtr_ntby_tr_pbmn\": \"-7246\",\r\n            \"pe_fund_ntby_tr_pbmn\": \"-25668\",\r\n            \"bank_ntby_tr_pbmn\": \"3326\",\r\n            \"insu_ntby_tr_pbmn\": \"-13791\",\r\n            \"mrbn_ntby_tr_pbmn\": \"-2742\",\r\n            \"fund_ntby_tr_pbmn\": \"-85671\",\r\n            \"etc_ntby_tr_pbmn\": \"27388\",\r\n            \"etc_orgt_ntby_tr_pbmn\": \"0\",\r\n            \"etc_corp_ntby_tr_pbmn\": \"27388\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240516\",\r\n            \"bstp_nmix_prpr\": \"2753.00\",\r\n            \"bstp_nmix_prdy_vrss\": \"22.66\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"bstp_nmix_prdy_ctrt\": \"0.83\",\r\n            \"bstp_nmix_oprc\": \"2770.27\",\r\n            \"bstp_nmix_hgpr\": \"2773.46\",\r\n            \"bstp_nmix_lwpr\": \"2748.22\",\r\n            \"stck_prdy_clpr\": \"2730.34\",\r\n            \"frgn_ntby_qty\": \"5326\",\r\n            \"frgn_reg_ntby_qty\": \"5287\",\r\n            \"frgn_nreg_ntby_qty\": \"38\",\r\n            \"prsn_ntby_qty\": \"-14059\",\r\n            \"orgn_ntby_qty\": \"8886\",\r\n            \"scrt_ntby_qty\": \"11036\",\r\n            \"ivtr_ntby_qty\": \"359\",\r\n            \"pe_fund_ntby_vol\": \"850\",\r\n            \"bank_ntby_qty\": \"41\",\r\n            \"insu_ntby_qty\": \"-989\",\r\n            \"mrbn_ntby_qty\": \"-341\",\r\n            \"fund_ntby_qty\": \"-2070\",\r\n            \"etc_ntby_qty\": \"-153\",\r\n            \"etc_orgt_ntby_vol\": \"0\",\r\n            \"etc_corp_ntby_vol\": \"-153\",\r\n            \"frgn_ntby_tr_pbmn\": \"425869\",\r\n            \"frgn_reg_ntby_pbmn\": \"425686\",\r\n            \"frgn_nreg_ntby_pbmn\": \"183\",\r\n            \"prsn_ntby_tr_pbmn\": \"-964779\",\r\n            \"orgn_ntby_tr_pbmn\": \"593789\",\r\n            \"scrt_ntby_tr_pbmn\": \"680881\",\r\n            \"ivtr_ntby_tr_pbmn\": \"20139\",\r\n            \"pe_fund_ntby_tr_pbmn\": \"11277\",\r\n            \"bank_ntby_tr_pbmn\": \"-589\",\r\n            \"insu_ntby_tr_pbmn\": \"-29395\",\r\n            \"mrbn_ntby_tr_pbmn\": \"-19913\",\r\n            \"fund_ntby_tr_pbmn\": \"-68611\",\r\n            \"etc_ntby_tr_pbmn\": \"-54879\",\r\n            \"etc_orgt_ntby_tr_pbmn\": \"0\",\r\n            \"etc_corp_ntby_tr_pbmn\": \"-54879\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST04830000",
    "name": "국내주식 공매도 일별추이",
    "url": "/uapi/domestic-stock/v1/quotations/daily-short-sale",
    "sheet": "국내주식 공매도 일별추이",
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
        "element": "prdy_vol",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_clpr",
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
        "element": "stnd_vol_smtn",
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
        "element": "acml_ssts_cntg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_ssts_cntg_qty_rlim",
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
        "element": "stnd_tr_pbmn_smtn",
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
        "element": "acml_ssts_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acml_ssts_tr_pbmn_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
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
    "tr_id": "FHPTJ04160001",
    "name": "종목별 투자자매매동향(일별)",
    "url": "/uapi/domestic-stock/v1/quotations/investor-trade-by-stock-daily",
    "sheet": "종목별 투자자매매동향(일별)",
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
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rprs_mrkt_kor_name",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_clpr",
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
        "description": "단위 : 주"
      },
      {
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": "단위 : 백만원"
      },
      {
        "element": "stck_oprc",
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
        "element": "stck_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": "단위 : 주"
      },
      {
        "element": "frgn_reg_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_ntby_pbmn",
        "type": "string",
        "required": "Y",
        "description": "단위 : 백만원"
      },
      {
        "element": "frgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_ntby_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_askp_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_bidp_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_askp_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_reg_bidp_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_askp_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_bidp_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_askp_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_nreg_bidp_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bold_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_INPUT_ISCD:005930\r\nFID_INPUT_DATE_1:20250811\r\nFID_ORG_ADJ_PRC:\r\nFID_ETC_CLS_CODE:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"stck_prpr\": \"71100\",\r\n        \"prdy_vrss\": \"100\",\r\n        \"prdy_vrss_sign\": \"2\",\r\n        \"prdy_ctrt\": \"0.14\",\r\n        \"acml_vol\": \"15797656\",\r\n        \"prdy_vol\": \"11354253\",\r\n        \"rprs_mrkt_kor_name\": \"KOSPI200\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"stck_bsop_date\": \"20250811\",\r\n            \"stck_clpr\": \"71000\",\r\n            \"prdy_vrss\": \"-800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.11\",\r\n            \"acml_vol\": \"11354253\",\r\n            \"acml_tr_pbmn\": \"808470078650\",\r\n            \"stck_oprc\": \"72000\",\r\n            \"stck_hgpr\": \"72100\",\r\n            \"stck_lwpr\": \"70800\",\r\n            \"frgn_ntby_qty\": \"-2029800\",\r\n            \"frgn_reg_ntby_qty\": \"-2031350\",\r\n            \"frgn_nreg_ntby_qty\": \"1550\",\r\n            \"prsn_ntby_qty\": \"1686273\",\r\n            \"orgn_ntby_qty\": \"-571822\",\r\n            \"scrt_ntby_qty\": \"-44264\",\r\n            \"ivtr_ntby_qty\": \"-205974\",\r\n            \"pe_fund_ntby_vol\": \"-125032\",\r\n            \"bank_ntby_qty\": \"2930\",\r\n            \"insu_ntby_qty\": \"-85309\",\r\n            \"mrbn_ntby_qty\": \"-737\",\r\n            \"fund_ntby_qty\": \"-113436\",\r\n            \"etc_ntby_qty\": \"915349\",\r\n            \"etc_corp_ntby_vol\": \"915349\",\r\n            \"etc_orgt_ntby_vol\": \"0\",\r\n            \"frgn_reg_ntby_pbmn\": \"-144473\",\r\n            \"frgn_ntby_tr_pbmn\": \"-144363\",\r\n            \"frgn_nreg_ntby_pbmn\": \"110\",\r\n            \"prsn_ntby_tr_pbmn\": \"120110\",\r\n            \"orgn_ntby_tr_pbmn\": \"-40903\",\r\n            \"scrt_ntby_tr_pbmn\": \"-3169\",\r\n            \"pe_fund_ntby_tr_pbmn\": \"-8887\",\r\n            \"ivtr_ntby_tr_pbmn\": \"-14641\",\r\n            \"bank_ntby_tr_pbmn\": \"209\",\r\n            \"insu_ntby_tr_pbmn\": \"-6061\",\r\n            \"mrbn_ntby_tr_pbmn\": \"-52\",\r\n            \"fund_ntby_tr_pbmn\": \"-8301\",\r\n            \"etc_ntby_tr_pbmn\": \"65156\",\r\n            \"etc_corp_ntby_tr_pbmn\": \"65156\",\r\n            \"etc_orgt_ntby_tr_pbmn\": \"0\",\r\n            \"frgn_seln_vol\": \"4557311\",\r\n            \"frgn_shnu_vol\": \"2527511\",\r\n            \"frgn_seln_tr_pbmn\": \"324535\",\r\n            \"frgn_shnu_tr_pbmn\": \"180172\",\r\n            \"frgn_reg_askp_qty\": \"4550828\",\r\n            \"frgn_reg_bidp_qty\": \"2519478\",\r\n            \"frgn_reg_askp_pbmn\": \"324074\",\r\n            \"frgn_reg_bidp_pbmn\": \"179600\",\r\n            \"frgn_nreg_askp_qty\": \"6483\",\r\n            \"frgn_nreg_bidp_qty\": \"8033\",\r\n            \"frgn_nreg_askp_pbmn\": \"461\",\r\n            \"frgn_nreg_bidp_pbmn\": \"572\",\r\n            \"prsn_seln_vol\": \"2003849\",\r\n            \"prsn_shnu_vol\": \"3690122\",\r\n            \"prsn_seln_tr_pbmn\": \"142680\",\r\n            \"prsn_shnu_tr_pbmn\": \"262790\",\r\n            \"orgn_seln_vol\": \"4694042\",\r\n            \"orgn_shnu_vol\": \"4122220\",\r\n            \"orgn_seln_tr_pbmn\": \"334201\",\r\n            \"orgn_shnu_tr_pbmn\": \"293298\",\r\n            \"scrt_seln_vol\": \"444582\",\r\n            \"scrt_shnu_vol\": \"400318\",\r\n            \"scrt_seln_tr_pbmn\": \"31639\",\r\n            \"scrt_shnu_tr_pbmn\": \"28470\",\r\n            \"ivtr_seln_vol\": \"282816\",\r\n            \"ivtr_shnu_vol\": \"76842\",\r\n            \"ivtr_seln_tr_pbmn\": \"20111\",\r\n            \"ivtr_shnu_tr_pbmn\": \"5470\",\r\n            \"pe_fund_seln_tr_pbmn\": \"13670\",\r\n            \"pe_fund_seln_vol\": \"192157\",\r\n            \"pe_fund_shnu_tr_pbmn\": \"4783\",\r\n            \"pe_fund_shnu_vol\": \"67125\",\r\n            \"bank_seln_vol\": \"6\",\r\n            \"bank_shnu_vol\": \"2936\",\r\n            \"bank_seln_tr_pbmn\": \"0\",\r\n            \"bank_shnu_tr_pbmn\": \"209\",\r\n            \"insu_seln_vol\": \"108700\",\r\n            \"insu_shnu_vol\": \"23391\",\r\n            \"insu_seln_tr_pbmn\": \"7728\",\r\n            \"insu_shnu_tr_pbmn\": \"1666\",\r\n            \"mrbn_seln_vol\": \"760\",\r\n            \"mrbn_shnu_vol\": \"23\",\r\n            \"mrbn_seln_tr_pbmn\": \"54\",\r\n            \"mrbn_shnu_tr_pbmn\": \"2\",\r\n            \"fund_seln_vol\": \"3665021\",\r\n            \"fund_shnu_vol\": \"3551585\",\r\n            \"fund_seln_tr_pbmn\": \"261000\",\r\n            \"fund_shnu_tr_pbmn\": \"252699\",\r\n            \"etc_seln_vol\": \"99051\",\r\n            \"etc_shnu_vol\": \"1014400\",\r\n            \"etc_seln_tr_pbmn\": \"7054\",\r\n            \"etc_shnu_tr_pbmn\": \"72209\",\r\n            \"etc_orgt_seln_vol\": \"0\",\r\n            \"etc_orgt_shnu_vol\": \"0\",\r\n            \"etc_orgt_seln_tr_pbmn\": \"0\",\r\n            \"etc_orgt_shnu_tr_pbmn\": \"0\",\r\n            \"etc_corp_seln_vol\": \"99051\",\r\n            \"etc_corp_shnu_vol\": \"1014400\",\r\n            \"etc_corp_seln_tr_pbmn\": \"7054\",\r\n            \"etc_corp_shnu_tr_pbmn\": \"72209\",\r\n            \"bold_yn\": \"N\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHKST03900300",
    "name": "종목조건검색 목록조회",
    "url": "/uapi/domestic-stock/v1/quotations/psearch-title",
    "sheet": "종목조건검색 목록조회",
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
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "user_id",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seq",
        "type": "string",
        "required": "Y",
        "description": "해당 값을 종목조건검색조회 API의 input으로 사용\r\n(0번부터 시작)"
      },
      {
        "element": "grp_nm",
        "type": "string",
        "required": "Y",
        "description": "HTS(eFriend Plus) [0110] \"사용자조건검색\"화면을 통해\r\n등록한 사용자조건 그룹"
      },
      {
        "element": "condition_nm",
        "type": "string",
        "required": "Y",
        "description": "등록한 사용자 조건명"
      },
      {
        "element": "{\r\n\t\"user_id\":\"abcd9876\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output2\": [\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"0\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"RSI전략1_14_9_PER_부채비율\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"1\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"모멘텀전략1_5_3_PER_부채비율\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"2\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"외국계거래량_10000이상_PER_부채비율\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"3\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"이평전략1_5_20_PER_부채비율\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"4\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"이평전략2_5_20_PER_부채비율\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"5\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"테스트3\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"6\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"테트스\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"7\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"테트스2\"\r\n        },\r\n        {\r\n            \"user_id\": \"abcd9876\",\r\n            \"seq\": \"8\",\r\n            \"grp_nm\": \"임시그룹\",\r\n            \"condition_nm\": \"투자경고제외\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST130000C0",
    "name": "국내주식 상하한가 포착",
    "url": "/uapi/domestic-stock/v1/quotations/capture-uplowprice",
    "sheet": "국내주식 상하한가 포착",
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
        "element": "askp_rsqn1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bidp_rsqn1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_cnqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_llam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_mxpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_vrss_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_COND_SCR_DIV_CODE:11300\r\nFID_PRC_CLS_CODE:0\r\nFID_DIV_CLS_CODE:0\r\nFID_INPUT_ISCD:0000\r\nFID_TRGT_CLS_CODE:\r\nFID_TRGT_EXLS_CLS_CODE:\r\nFID_INPUT_PRICE_1:\r\nFID_INPUT_PRICE_2:\r\nFID_VOL_CNT:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"mksc_shrn_iscd\": \"012800\",\r\n            \"hts_kor_isnm\": \"대창\",\r\n            \"stck_prpr\": \"2080\",\r\n            \"prdy_vrss_sign\": \"1\",\r\n            \"prdy_vrss\": \"478\",\r\n            \"prdy_ctrt\": \"29.84\",\r\n            \"acml_vol\": \"39937550\",\r\n            \"total_askp_rsqn\": \"0\",\r\n            \"total_bidp_rsqn\": \"2648946\",\r\n            \"askp_rsqn1\": \"0\",\r\n            \"bidp_rsqn1\": \"2299811\",\r\n            \"prdy_vol\": \"4003121\",\r\n            \"seln_cnqn\": \"2\",\r\n            \"shnu_cnqn\": \"0\",\r\n            \"stck_llam\": \"1122\",\r\n            \"stck_mxpr\": \"2080\",\r\n            \"prdy_vrss_vol_rate\": \"997.66\"\r\n        },\r\n        {\r\n            \"mksc_shrn_iscd\": \"215100\",\r\n            \"hts_kor_isnm\": \"로보로보\",\r\n            \"stck_prpr\": \"5680\",\r\n            \"prdy_vrss_sign\": \"1\",\r\n            \"prdy_vrss\": \"1310\",\r\n            \"prdy_ctrt\": \"29.98\",\r\n            \"acml_vol\": \"10240653\",\r\n            \"total_askp_rsqn\": \"0\",\r\n            \"total_bidp_rsqn\": \"622698\",\r\n            \"askp_rsqn1\": \"0\",\r\n            \"bidp_rsqn1\": \"553376\",\r\n            \"prdy_vol\": \"34944\",\r\n            \"seln_cnqn\": \"40\",\r\n            \"shnu_cnqn\": \"0\",\r\n            \"stck_llam\": \"3060\",\r\n            \"stck_mxpr\": \"5680\",\r\n            \"prdy_vrss_vol_rate\": \"29305.90\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPPG04600001",
    "name": "프로그램매매 종합현황(일별)",
    "url": "/uapi/domestic-stock/v1/quotations/comp-program-trade-daily",
    "sheet": "프로그램매매 종합현황(일별)",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_shun_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_shun_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_shun_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_shnu_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_shnu_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_shnu_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_shnu_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_shnu_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_shnu_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_entm_shnu_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_shnu_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_shnu_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_shnu_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_onsl_shnu_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_shun_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_ntby_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_smtm_seln_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_entm_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_onsl_seln_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_onsl_shnu_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_smtm_shun_vol_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_shun_tr_pbmn_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_entm_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:UN\r\nFID_MRKT_CLS_CODE:K\r\nFID_INPUT_DATE_1:\r\nFID_INPUT_DATE_2:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240404\",\r\n            \"arbt_entm_seln_vol\": \"945\",\r\n            \"arbt_entm_seln_vol_rate\": \"0.20\",\r\n            \"arbt_entm_seln_tr_pbmn\": \"60184\",\r\n            \"arbt_entm_seln_tr_pbmn_rate\": \"0.50\",\r\n            \"arbt_onsl_seln_tr_pbmn\": \"116742\",\r\n            \"arbt_onsl_seln_tr_pbmn_rate\": \"0.97\",\r\n            \"arbt_onsl_seln_vol\": \"1893\",\r\n            \"arbt_onsl_seln_vol_rate\": \"0.40\",\r\n            \"arbt_smtn_seln_vol\": \"2839\",\r\n            \"arbt_smtm_seln_vol_rate\": \"0.59\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"176926\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"1.48\",\r\n            \"nabt_entm_seln_vol\": \"72995\",\r\n            \"nabt_entm_seln_tr_pbmn\": \"2335987\",\r\n            \"nabt_entm_seln_vol_rate\": \"15.27\",\r\n            \"nabt_entm_seln_tr_pbmn_rate\": \"19.50\",\r\n            \"nabt_onsl_seln_vol\": \"335\",\r\n            \"nabt_onsl_seln_vol_rate\": \"0.07\",\r\n            \"nabt_onsl_seln_tr_pbmn\": \"18428\",\r\n            \"nabt_onsl_seln_tr_pbmn_rate\": \"0.15\",\r\n            \"nabt_smtn_seln_vol\": \"73331\",\r\n            \"nabt_smtm_seln_vol_rate\": \"15.34\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2354415\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"19.66\",\r\n            \"whol_entm_seln_vol\": \"73940\",\r\n            \"whol_entm_seln_tr_pbmn\": \"2396171\",\r\n            \"whol_entm_seln_vol_rate\": \"15.47\",\r\n            \"whol_entm_seln_tr_pbmn_rate\": \"20.00\",\r\n            \"whol_onsl_seln_vol\": \"2229\",\r\n            \"whol_onsl_seln_vol_rate\": \"0.47\",\r\n            \"whol_onsl_seln_tr_pbmn\": \"135170\",\r\n            \"whol_onsl_seln_tr_pbmn_rate\": \"1.13\",\r\n            \"whol_smtn_seln_vol\": \"76169\",\r\n            \"whol_seln_vol_rate\": \"15.94\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"2531340\",\r\n            \"whol_seln_tr_pbmn_rate\": \"21.13\",\r\n            \"arbt_entm_shnu_vol\": \"798\",\r\n            \"arbt_entm_shnu_vol_rate\": \"0.17\",\r\n            \"arbt_entm_shnu_tr_pbmn\": \"50818\",\r\n            \"arbt_entm_shnu_tr_pbmn_rate\": \"0.42\",\r\n            \"arbt_onsl_shnu_vol\": \"247\",\r\n            \"arbt_onsl_shnu_vol_rate\": \"0.05\",\r\n            \"arbt_onsl_shnu_tr_pbmn\": \"15309\",\r\n            \"arbt_onsl_shnu_tr_pbmn_rate\": \"0.13\",\r\n            \"arbt_smtn_shnu_vol\": \"1045\",\r\n            \"arbt_smtm_shun_vol_rate\": \"0.22\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"66127\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"0.55\",\r\n            \"nabt_entm_shnu_vol\": \"73441\",\r\n            \"nabt_entm_shnu_vol_rate\": \"15.37\",\r\n            \"nabt_entm_shnu_tr_pbmn\": \"2581806\",\r\n            \"nabt_entm_shnu_tr_pbmn_rate\": \"21.55\",\r\n            \"nabt_onsl_shnu_vol\": \"250\",\r\n            \"nabt_onsl_shnu_vol_rate\": \"0.05\",\r\n            \"nabt_onsl_shnu_tr_pbmn\": \"11652\",\r\n            \"nabt_onsl_shnu_tr_pbmn_rate\": \"0.10\",\r\n            \"nabt_smtn_shnu_vol\": \"73691\",\r\n            \"nabt_smtm_shun_vol_rate\": \"15.42\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2593458\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"21.65\",\r\n            \"whol_entm_shnu_vol\": \"74239\",\r\n            \"whol_entm_shnu_vol_rate\": \"15.53\",\r\n            \"whol_entm_shnu_tr_pbmn\": \"2632624\",\r\n            \"whol_entm_shnu_tr_pbmn_rate\": \"21.98\",\r\n            \"whol_onsl_shnu_vol\": \"497\",\r\n            \"whol_onsl_shnu_tr_pbmn\": \"26961\",\r\n            \"whol_onsl_shnu_tr_pbmn_rate\": \"0.23\",\r\n            \"whol_onsl_shnu_vol_rate\": \"0.10\",\r\n            \"whol_smtn_shnu_vol\": \"74736\",\r\n            \"whol_shun_vol_rate\": \"15.64\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"2659585\",\r\n            \"whol_shun_tr_pbmn_rate\": \"22.20\",\r\n            \"arbt_entm_ntby_qty\": \"-147\",\r\n            \"arbt_entm_ntby_qty_rate\": \"-0.03\",\r\n            \"arbt_entm_ntby_tr_pbmn\": \"-9366\",\r\n            \"arbt_entm_ntby_tr_pbmn_rate\": \"-0.08\",\r\n            \"arbt_onsl_ntby_qty\": \"-1646\",\r\n            \"arbt_onsl_ntby_qty_rate\": \"-0.34\",\r\n            \"arbt_onsl_ntby_tr_pbmn\": \"-101433\",\r\n            \"arbt_onsl_ntby_tr_pbmn_rate\": \"-0.85\",\r\n            \"arbt_smtn_ntby_qty\": \"-1793\",\r\n            \"arbt_smtm_ntby_qty_rate\": \"-0.38\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"-110799\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"-0.93\",\r\n            \"nabt_entm_ntby_qty\": \"446\",\r\n            \"nabt_entm_ntby_qty_rate\": \"0.09\",\r\n            \"nabt_entm_ntby_tr_pbmn\": \"245819\",\r\n            \"nabt_entm_ntby_tr_pbmn_rate\": \"2.05\",\r\n            \"nabt_onsl_ntby_qty\": \"-85\",\r\n            \"nabt_onsl_ntby_qty_rate\": \"-0.02\",\r\n            \"nabt_onsl_ntby_tr_pbmn\": \"-6776\",\r\n            \"nabt_onsl_ntby_tr_pbmn_rate\": \"-0.06\",\r\n            \"nabt_smtn_ntby_qty\": \"361\",\r\n            \"nabt_smtm_ntby_qty_rate\": \"0.08\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"239043\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"2.00\",\r\n            \"whol_entm_ntby_qty\": \"299\",\r\n            \"whol_entm_ntby_qty_rate\": \"0.06\",\r\n            \"whol_entm_ntby_tr_pbmn\": \"236453\",\r\n            \"whol_entm_ntby_tr_pbmn_rate\": \"1.97\",\r\n            \"whol_onsl_ntby_qty\": \"-1732\",\r\n            \"whol_onsl_ntby_qty_rate\": \"-0.36\",\r\n            \"whol_onsl_ntby_tr_pbmn\": \"-108209\",\r\n            \"whol_onsl_ntby_tr_pbmn_rate\": \"-0.90\",\r\n            \"whol_smtn_ntby_qty\": \"-1433\",\r\n            \"whol_ntby_qty_rate\": \"-0.30\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"128245\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"1.07\",\r\n            \"bstp_nmix_prpr\": \"\",\r\n            \"bstp_nmix_prdy_vrss\": \"\",\r\n            \"prdy_vrss_sign\": \"\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240403\",\r\n            \"arbt_entm_seln_vol\": \"769\",\r\n            \"arbt_entm_seln_vol_rate\": \"0.12\",\r\n            \"arbt_entm_seln_tr_pbmn\": \"48480\",\r\n            \"arbt_entm_seln_tr_pbmn_rate\": \"0.37\",\r\n            \"arbt_onsl_seln_tr_pbmn\": \"192333\",\r\n            \"arbt_onsl_seln_tr_pbmn_rate\": \"1.45\",\r\n            \"arbt_onsl_seln_vol\": \"3118\",\r\n            \"arbt_onsl_seln_vol_rate\": \"0.49\",\r\n            \"arbt_smtn_seln_vol\": \"3887\",\r\n            \"arbt_smtm_seln_vol_rate\": \"0.61\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"240813\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"1.82\",\r\n            \"nabt_entm_seln_vol\": \"94356\",\r\n            \"nabt_entm_seln_tr_pbmn\": \"3076931\",\r\n            \"nabt_entm_seln_vol_rate\": \"14.72\",\r\n            \"nabt_entm_seln_tr_pbmn_rate\": \"23.21\",\r\n            \"nabt_onsl_seln_vol\": \"3323\",\r\n            \"nabt_onsl_seln_vol_rate\": \"0.52\",\r\n            \"nabt_onsl_seln_tr_pbmn\": \"207163\",\r\n            \"nabt_onsl_seln_tr_pbmn_rate\": \"1.56\",\r\n            \"nabt_smtn_seln_vol\": \"97679\",\r\n            \"nabt_smtm_seln_vol_rate\": \"15.24\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"3284094\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"24.77\",\r\n            \"whol_entm_seln_vol\": \"95125\",\r\n            \"whol_entm_seln_tr_pbmn\": \"3125411\",\r\n            \"whol_entm_seln_vol_rate\": \"14.84\",\r\n            \"whol_entm_seln_tr_pbmn_rate\": \"23.58\",\r\n            \"whol_onsl_seln_vol\": \"6440\",\r\n            \"whol_onsl_seln_vol_rate\": \"1.01\",\r\n            \"whol_onsl_seln_tr_pbmn\": \"399496\",\r\n            \"whol_onsl_seln_tr_pbmn_rate\": \"3.01\",\r\n            \"whol_smtn_seln_vol\": \"101566\",\r\n            \"whol_seln_vol_rate\": \"15.85\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"3524908\",\r\n            \"whol_seln_tr_pbmn_rate\": \"26.59\",\r\n            \"arbt_entm_shnu_vol\": \"916\",\r\n            \"arbt_entm_shnu_vol_rate\": \"0.14\",\r\n            \"arbt_entm_shnu_tr_pbmn\": \"57765\",\r\n            \"arbt_entm_shnu_tr_pbmn_rate\": \"0.44\",\r\n            \"arbt_onsl_shnu_vol\": \"151\",\r\n            \"arbt_onsl_shnu_vol_rate\": \"0.02\",\r\n            \"arbt_onsl_shnu_tr_pbmn\": \"9682\",\r\n            \"arbt_onsl_shnu_tr_pbmn_rate\": \"0.07\",\r\n            \"arbt_smtn_shnu_vol\": \"1067\",\r\n            \"arbt_smtm_shun_vol_rate\": \"0.17\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"67446\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"0.51\",\r\n            \"nabt_entm_shnu_vol\": \"88098\",\r\n            \"nabt_entm_shnu_vol_rate\": \"13.75\",\r\n            \"nabt_entm_shnu_tr_pbmn\": \"2576437\",\r\n            \"nabt_entm_shnu_tr_pbmn_rate\": \"19.43\",\r\n            \"nabt_onsl_shnu_vol\": \"206\",\r\n            \"nabt_onsl_shnu_vol_rate\": \"0.03\",\r\n            \"nabt_onsl_shnu_tr_pbmn\": \"8168\",\r\n            \"nabt_onsl_shnu_tr_pbmn_rate\": \"0.06\",\r\n            \"nabt_smtn_shnu_vol\": \"88304\",\r\n            \"nabt_smtm_shun_vol_rate\": \"13.78\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"2584605\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"19.50\",\r\n            \"whol_entm_shnu_vol\": \"89014\",\r\n            \"whol_entm_shnu_vol_rate\": \"13.89\",\r\n            \"whol_entm_shnu_tr_pbmn\": \"2634202\",\r\n            \"whol_entm_shnu_tr_pbmn_rate\": \"19.87\",\r\n            \"whol_onsl_shnu_vol\": \"357\",\r\n            \"whol_onsl_shnu_tr_pbmn\": \"17849\",\r\n            \"whol_onsl_shnu_tr_pbmn_rate\": \"0.13\",\r\n            \"whol_onsl_shnu_vol_rate\": \"0.06\",\r\n            \"whol_smtn_shnu_vol\": \"89371\",\r\n            \"whol_shun_vol_rate\": \"13.95\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"2652051\",\r\n            \"whol_shun_tr_pbmn_rate\": \"20.00\",\r\n            \"arbt_entm_ntby_qty\": \"147\",\r\n            \"arbt_entm_ntby_qty_rate\": \"0.02\",\r\n            \"arbt_entm_ntby_tr_pbmn\": \"9284\",\r\n            \"arbt_entm_ntby_tr_pbmn_rate\": \"0.07\",\r\n            \"arbt_onsl_ntby_qty\": \"-2967\",\r\n            \"arbt_onsl_ntby_qty_rate\": \"-0.46\",\r\n            \"arbt_onsl_ntby_tr_pbmn\": \"-182651\",\r\n            \"arbt_onsl_ntby_tr_pbmn_rate\": \"-1.38\",\r\n            \"arbt_smtn_ntby_qty\": \"-2819\",\r\n            \"arbt_smtm_ntby_qty_rate\": \"-0.44\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"-173367\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"-1.31\",\r\n            \"nabt_entm_ntby_qty\": \"-6259\",\r\n            \"nabt_entm_ntby_qty_rate\": \"-0.98\",\r\n            \"nabt_entm_ntby_tr_pbmn\": \"-500494\",\r\n            \"nabt_entm_ntby_tr_pbmn_rate\": \"-3.78\",\r\n            \"nabt_onsl_ntby_qty\": \"-3116\",\r\n            \"nabt_onsl_ntby_qty_rate\": \"-0.49\",\r\n            \"nabt_onsl_ntby_tr_pbmn\": \"-198996\",\r\n            \"nabt_onsl_ntby_tr_pbmn_rate\": \"-1.50\",\r\n            \"nabt_smtn_ntby_qty\": \"-9375\",\r\n            \"nabt_smtm_ntby_qty_rate\": \"-1.46\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"-699489\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"-5.28\",\r\n            \"whol_entm_ntby_qty\": \"-6112\",\r\n            \"whol_entm_ntby_qty_rate\": \"-0.95\",\r\n            \"whol_entm_ntby_tr_pbmn\": \"-491210\",\r\n            \"whol_entm_ntby_tr_pbmn_rate\": \"-3.71\",\r\n            \"whol_onsl_ntby_qty\": \"-6083\",\r\n            \"whol_onsl_ntby_qty_rate\": \"-0.95\",\r\n            \"whol_onsl_ntby_tr_pbmn\": \"-381647\",\r\n            \"whol_onsl_ntby_tr_pbmn_rate\": \"-2.88\",\r\n            \"whol_smtn_ntby_qty\": \"-12195\",\r\n            \"whol_ntby_qty_rate\": \"-1.90\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"-872856\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"-6.58\",\r\n            \"bstp_nmix_prpr\": \"\",\r\n            \"bstp_nmix_prdy_vrss\": \"\",\r\n            \"prdy_vrss_sign\": \"\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240402\",\r\n            \"arbt_entm_seln_vol\": \"857\",\r\n            \"arbt_entm_seln_vol_rate\": \"0.14\",\r\n            \"arbt_entm_seln_tr_pbmn\": \"54673\",\r\n            \"arbt_entm_seln_tr_pbmn_rate\": \"0.42\",\r\n            \"arbt_onsl_seln_tr_pbmn\": \"78907\",\r\n            \"arbt_onsl_seln_tr_pbmn_rate\": \"0.60\",\r\n            \"arbt_onsl_seln_vol\": \"1282\",\r\n            \"arbt_onsl_seln_vol_rate\": \"0.20\",\r\n            \"arbt_smtn_seln_vol\": \"2138\",\r\n            \"arbt_smtm_seln_vol_rate\": \"0.34\",\r\n            \"arbt_smtn_seln_tr_pbmn\": \"133579\",\r\n            \"arbt_smtm_seln_tr_pbmn_rate\": \"1.02\",\r\n            \"nabt_entm_seln_vol\": \"78391\",\r\n            \"nabt_entm_seln_tr_pbmn\": \"2385531\",\r\n            \"nabt_entm_seln_vol_rate\": \"12.44\",\r\n            \"nabt_entm_seln_tr_pbmn_rate\": \"18.19\",\r\n            \"nabt_onsl_seln_vol\": \"893\",\r\n            \"nabt_onsl_seln_vol_rate\": \"0.14\",\r\n            \"nabt_onsl_seln_tr_pbmn\": \"54722\",\r\n            \"nabt_onsl_seln_tr_pbmn_rate\": \"0.42\",\r\n            \"nabt_smtn_seln_vol\": \"79284\",\r\n            \"nabt_smtm_seln_vol_rate\": \"12.58\",\r\n            \"nabt_smtn_seln_tr_pbmn\": \"2440253\",\r\n            \"nabt_smtm_seln_tr_pbmn_rate\": \"18.60\",\r\n            \"whol_entm_seln_vol\": \"79247\",\r\n            \"whol_entm_seln_tr_pbmn\": \"2440203\",\r\n            \"whol_entm_seln_vol_rate\": \"12.57\",\r\n            \"whol_entm_seln_tr_pbmn_rate\": \"18.60\",\r\n            \"whol_onsl_seln_vol\": \"2175\",\r\n            \"whol_onsl_seln_vol_rate\": \"0.35\",\r\n            \"whol_onsl_seln_tr_pbmn\": \"133628\",\r\n            \"whol_onsl_seln_tr_pbmn_rate\": \"1.02\",\r\n            \"whol_smtn_seln_vol\": \"81422\",\r\n            \"whol_seln_vol_rate\": \"12.92\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"2573832\",\r\n            \"whol_seln_tr_pbmn_rate\": \"19.62\",\r\n            \"arbt_entm_shnu_vol\": \"760\",\r\n            \"arbt_entm_shnu_vol_rate\": \"0.12\",\r\n            \"arbt_entm_shnu_tr_pbmn\": \"48775\",\r\n            \"arbt_entm_shnu_tr_pbmn_rate\": \"0.37\",\r\n            \"arbt_onsl_shnu_vol\": \"3\",\r\n            \"arbt_onsl_shnu_vol_rate\": \"0.00\",\r\n            \"arbt_onsl_shnu_tr_pbmn\": \"657\",\r\n            \"arbt_onsl_shnu_tr_pbmn_rate\": \"0.01\",\r\n            \"arbt_smtn_shnu_vol\": \"762\",\r\n            \"arbt_smtm_shun_vol_rate\": \"0.12\",\r\n            \"arbt_smtn_shnu_tr_pbmn\": \"49432\",\r\n            \"arbt_smtm_shun_tr_pbmn_rate\": \"0.38\",\r\n            \"nabt_entm_shnu_vol\": \"74157\",\r\n            \"nabt_entm_shnu_vol_rate\": \"11.76\",\r\n            \"nabt_entm_shnu_tr_pbmn\": \"3086213\",\r\n            \"nabt_entm_shnu_tr_pbmn_rate\": \"23.53\",\r\n            \"nabt_onsl_shnu_vol\": \"187\",\r\n            \"nabt_onsl_shnu_vol_rate\": \"0.03\",\r\n            \"nabt_onsl_shnu_tr_pbmn\": \"8119\",\r\n            \"nabt_onsl_shnu_tr_pbmn_rate\": \"0.06\",\r\n            \"nabt_smtn_shnu_vol\": \"74344\",\r\n            \"nabt_smtm_shun_vol_rate\": \"11.79\",\r\n            \"nabt_smtn_shnu_tr_pbmn\": \"3094332\",\r\n            \"nabt_smtm_shun_tr_pbmn_rate\": \"23.59\",\r\n            \"whol_entm_shnu_vol\": \"74916\",\r\n            \"whol_entm_shnu_vol_rate\": \"11.88\",\r\n            \"whol_entm_shnu_tr_pbmn\": \"3134988\",\r\n            \"whol_entm_shnu_tr_pbmn_rate\": \"23.90\",\r\n            \"whol_onsl_shnu_vol\": \"190\",\r\n            \"whol_onsl_shnu_tr_pbmn\": \"8775\",\r\n            \"whol_onsl_shnu_tr_pbmn_rate\": \"0.07\",\r\n            \"whol_onsl_shnu_vol_rate\": \"0.03\",\r\n            \"whol_smtn_shnu_vol\": \"75107\",\r\n            \"whol_shun_vol_rate\": \"11.91\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"3143764\",\r\n            \"whol_shun_tr_pbmn_rate\": \"23.97\",\r\n            \"arbt_entm_ntby_qty\": \"-97\",\r\n            \"arbt_entm_ntby_qty_rate\": \"-0.02\",\r\n            \"arbt_entm_ntby_tr_pbmn\": \"-5897\",\r\n            \"arbt_entm_ntby_tr_pbmn_rate\": \"-0.04\",\r\n            \"arbt_onsl_ntby_qty\": \"-1279\",\r\n            \"arbt_onsl_ntby_qty_rate\": \"-0.20\",\r\n            \"arbt_onsl_ntby_tr_pbmn\": \"-78250\",\r\n            \"arbt_onsl_ntby_tr_pbmn_rate\": \"-0.60\",\r\n            \"arbt_smtn_ntby_qty\": \"-1376\",\r\n            \"arbt_smtm_ntby_qty_rate\": \"-0.22\",\r\n            \"arbt_smtn_ntby_tr_pbmn\": \"-84147\",\r\n            \"arbt_smtm_ntby_tr_pbmn_rate\": \"-0.64\",\r\n            \"nabt_entm_ntby_qty\": \"-4234\",\r\n            \"nabt_entm_ntby_qty_rate\": \"-0.67\",\r\n            \"nabt_entm_ntby_tr_pbmn\": \"700682\",\r\n            \"nabt_entm_ntby_tr_pbmn_rate\": \"5.34\",\r\n            \"nabt_onsl_ntby_qty\": \"-706\",\r\n            \"nabt_onsl_ntby_qty_rate\": \"-0.11\",\r\n            \"nabt_onsl_ntby_tr_pbmn\": \"-46603\",\r\n            \"nabt_onsl_ntby_tr_pbmn_rate\": \"-0.36\",\r\n            \"nabt_smtn_ntby_qty\": \"-4940\",\r\n            \"nabt_smtm_ntby_qty_rate\": \"-0.78\",\r\n            \"nabt_smtn_ntby_tr_pbmn\": \"654079\",\r\n            \"nabt_smtm_ntby_tr_pbmn_rate\": \"4.99\",\r\n            \"whol_entm_ntby_qty\": \"-4331\",\r\n            \"whol_entm_ntby_qty_rate\": \"-0.69\",\r\n            \"whol_entm_ntby_tr_pbmn\": \"694785\",\r\n            \"whol_entm_ntby_tr_pbmn_rate\": \"5.30\",\r\n            \"whol_onsl_ntby_qty\": \"-1985\",\r\n            \"whol_onsl_ntby_qty_rate\": \"-0.31\",\r\n            \"whol_onsl_ntby_tr_pbmn\": \"-124853\",\r\n            \"whol_onsl_ntby_tr_pbmn_rate\": \"-0.95\",\r\n            \"whol_smtn_ntby_qty\": \"-6316\",\r\n            \"whol_ntby_qty_rate\": \"-1.00\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"569932\",\r\n            \"whol_ntby_tr_pbmn_rate\": \"4.35\",\r\n            \"bstp_nmix_prpr\": \"\",\r\n            \"bstp_nmix_prdy_vrss\": \"\",\r\n            \"prdy_vrss_sign\": \"\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHPST074500C0",
    "name": "종목별 일별 대차거래추이",
    "url": "/uapi/domestic-stock/v1/quotations/daily-loan-trans",
    "sheet": "종목별 일별 대차거래추이",
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
        "element": "bsop_date",
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
        "element": "new_stcn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rdmp_stcn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prdy_rmnd_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rmnd_stcn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rmnd_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_div_cls_code:1\r\nmksc_shrn_iscd:005930\r\nstart_date:20240401\r\nend_date:20240430\r\ncts:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output2\": [\r\n        {\r\n            \"bsop_date\": \"20240430\",\r\n            \"stck_prpr\": \"2692.06\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"4.62\",\r\n            \"prdy_ctrt\": \"0.17\",\r\n            \"acml_vol\": \"460083500\",\r\n            \"new_stcn\": \"14379227\",\r\n            \"rdmp_stcn\": \"13993603\",\r\n            \"prdy_rmnd_vrss\": \"385624\",\r\n            \"rmnd_stcn\": \"947521840\",\r\n            \"rmnd_amt\": \"47504735\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240429\",\r\n            \"stck_prpr\": \"2687.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"31.11\",\r\n            \"prdy_ctrt\": \"1.17\",\r\n            \"acml_vol\": \"470546000\",\r\n            \"new_stcn\": \"6028334\",\r\n            \"rdmp_stcn\": \"13437664\",\r\n            \"prdy_rmnd_vrss\": \"-7409330\",\r\n            \"rmnd_stcn\": \"947136216\",\r\n            \"rmnd_amt\": \"47367356\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240426\",\r\n            \"stck_prpr\": \"2656.33\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"27.71\",\r\n            \"prdy_ctrt\": \"1.05\",\r\n            \"acml_vol\": \"450520700\",\r\n            \"new_stcn\": \"14406990\",\r\n            \"rdmp_stcn\": \"12079739\",\r\n            \"prdy_rmnd_vrss\": \"2327251\",\r\n            \"rmnd_stcn\": \"954545546\",\r\n            \"rmnd_amt\": \"46874865\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240425\",\r\n            \"stck_prpr\": \"2628.62\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-47.13\",\r\n            \"prdy_ctrt\": \"-1.76\",\r\n            \"acml_vol\": \"334062400\",\r\n            \"new_stcn\": \"4765719\",\r\n            \"rdmp_stcn\": \"13112635\",\r\n            \"prdy_rmnd_vrss\": \"-8346916\",\r\n            \"rmnd_stcn\": \"952231269\",\r\n            \"rmnd_amt\": \"46089010\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240424\",\r\n            \"stck_prpr\": \"2675.75\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"52.73\",\r\n            \"prdy_ctrt\": \"2.01\",\r\n            \"acml_vol\": \"325739600\",\r\n            \"new_stcn\": \"19649840\",\r\n            \"rdmp_stcn\": \"8993910\",\r\n            \"prdy_rmnd_vrss\": \"10655930\",\r\n            \"rmnd_stcn\": \"960577194\",\r\n            \"rmnd_amt\": \"47488544\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240423\",\r\n            \"stck_prpr\": \"2623.02\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-6.42\",\r\n            \"prdy_ctrt\": \"-0.24\",\r\n            \"acml_vol\": \"430275800\",\r\n            \"new_stcn\": \"7802761\",\r\n            \"rdmp_stcn\": \"7414164\",\r\n            \"prdy_rmnd_vrss\": \"388597\",\r\n            \"rmnd_stcn\": \"949921264\",\r\n            \"rmnd_amt\": \"46108475\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240422\",\r\n            \"stck_prpr\": \"2629.44\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"37.58\",\r\n            \"prdy_ctrt\": \"1.45\",\r\n            \"acml_vol\": \"401892200\",\r\n            \"new_stcn\": \"10841550\",\r\n            \"rdmp_stcn\": \"18150018\",\r\n            \"prdy_rmnd_vrss\": \"-7308468\",\r\n            \"rmnd_stcn\": \"949532667\",\r\n            \"rmnd_amt\": \"46211861\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240419\",\r\n            \"stck_prpr\": \"2591.86\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-42.84\",\r\n            \"prdy_ctrt\": \"-1.63\",\r\n            \"acml_vol\": \"809473400\",\r\n            \"new_stcn\": \"8657583\",\r\n            \"rdmp_stcn\": \"12304586\",\r\n            \"prdy_rmnd_vrss\": \"-3647003\",\r\n            \"rmnd_stcn\": \"956841135\",\r\n            \"rmnd_amt\": \"45225405\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240418\",\r\n            \"stck_prpr\": \"2634.70\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"50.52\",\r\n            \"prdy_ctrt\": \"1.95\",\r\n            \"acml_vol\": \"478786200\",\r\n            \"new_stcn\": \"13218317\",\r\n            \"rdmp_stcn\": \"16631496\",\r\n            \"prdy_rmnd_vrss\": \"-3413179\",\r\n            \"rmnd_stcn\": \"960488138\",\r\n            \"rmnd_amt\": \"46007513\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240417\",\r\n            \"stck_prpr\": \"2584.18\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-25.45\",\r\n            \"prdy_ctrt\": \"-0.98\",\r\n            \"acml_vol\": \"414348100\",\r\n            \"new_stcn\": \"13838612\",\r\n            \"rdmp_stcn\": \"9001120\",\r\n            \"prdy_rmnd_vrss\": \"4837492\",\r\n            \"rmnd_stcn\": \"963901317\",\r\n            \"rmnd_amt\": \"45199389\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240416\",\r\n            \"stck_prpr\": \"2609.63\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-60.80\",\r\n            \"prdy_ctrt\": \"-2.28\",\r\n            \"acml_vol\": \"570212100\",\r\n            \"new_stcn\": \"8029982\",\r\n            \"rdmp_stcn\": \"9662633\",\r\n            \"prdy_rmnd_vrss\": \"-1632651\",\r\n            \"rmnd_stcn\": \"959063825\",\r\n            \"rmnd_amt\": \"45461648\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240415\",\r\n            \"stck_prpr\": \"2670.43\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-11.39\",\r\n            \"prdy_ctrt\": \"-0.42\",\r\n            \"acml_vol\": \"561950000\",\r\n            \"new_stcn\": \"13418896\",\r\n            \"rdmp_stcn\": \"9863897\",\r\n            \"prdy_rmnd_vrss\": \"3554999\",\r\n            \"rmnd_stcn\": \"960696476\",\r\n            \"rmnd_amt\": \"46397052\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240412\",\r\n            \"stck_prpr\": \"2681.82\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-25.14\",\r\n            \"prdy_ctrt\": \"-0.93\",\r\n            \"acml_vol\": \"514575300\",\r\n            \"new_stcn\": \"16291814\",\r\n            \"rdmp_stcn\": \"6220088\",\r\n            \"prdy_rmnd_vrss\": \"10071726\",\r\n            \"rmnd_stcn\": \"957141477\",\r\n            \"rmnd_amt\": \"46559127\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240411\",\r\n            \"stck_prpr\": \"2706.96\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1.80\",\r\n            \"prdy_ctrt\": \"0.07\",\r\n            \"acml_vol\": \"561333400\",\r\n            \"new_stcn\": \"14878420\",\r\n            \"rdmp_stcn\": \"10305585\",\r\n            \"prdy_rmnd_vrss\": \"4572835\",\r\n            \"rmnd_stcn\": \"947069751\",\r\n            \"rmnd_amt\": \"46395176\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240409\",\r\n            \"stck_prpr\": \"2705.16\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-12.49\",\r\n            \"prdy_ctrt\": \"-0.46\",\r\n            \"acml_vol\": \"470183700\",\r\n            \"new_stcn\": \"10784436\",\r\n            \"rdmp_stcn\": \"6933242\",\r\n            \"prdy_rmnd_vrss\": \"3851194\",\r\n            \"rmnd_stcn\": \"942496916\",\r\n            \"rmnd_amt\": \"46082940\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240408\",\r\n            \"stck_prpr\": \"2717.65\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"3.44\",\r\n            \"prdy_ctrt\": \"0.13\",\r\n            \"acml_vol\": \"620652500\",\r\n            \"new_stcn\": \"16939713\",\r\n            \"rdmp_stcn\": \"12571632\",\r\n            \"prdy_rmnd_vrss\": \"4368081\",\r\n            \"rmnd_stcn\": \"938645722\",\r\n            \"rmnd_amt\": \"46069590\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240405\",\r\n            \"stck_prpr\": \"2714.21\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-27.79\",\r\n            \"prdy_ctrt\": \"-1.01\",\r\n            \"acml_vol\": \"621030600\",\r\n            \"new_stcn\": \"5614441\",\r\n            \"rdmp_stcn\": \"11701229\",\r\n            \"prdy_rmnd_vrss\": \"-6086788\",\r\n            \"rmnd_stcn\": \"934277641\",\r\n            \"rmnd_amt\": \"45207497\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240404\",\r\n            \"stck_prpr\": \"2742.00\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"35.03\",\r\n            \"prdy_ctrt\": \"1.29\",\r\n            \"acml_vol\": \"477952800\",\r\n            \"new_stcn\": \"12221690\",\r\n            \"rdmp_stcn\": \"5093795\",\r\n            \"prdy_rmnd_vrss\": \"7127895\",\r\n            \"rmnd_stcn\": \"940364429\",\r\n            \"rmnd_amt\": \"45926211\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240403\",\r\n            \"stck_prpr\": \"2706.97\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-46.19\",\r\n            \"prdy_ctrt\": \"-1.68\",\r\n            \"acml_vol\": \"640806300\",\r\n            \"new_stcn\": \"14817975\",\r\n            \"rdmp_stcn\": \"15348355\",\r\n            \"prdy_rmnd_vrss\": \"-530380\",\r\n            \"rmnd_stcn\": \"933236534\",\r\n            \"rmnd_amt\": \"44837956\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240402\",\r\n            \"stck_prpr\": \"2753.16\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"5.30\",\r\n            \"prdy_ctrt\": \"0.19\",\r\n            \"acml_vol\": \"630392900\",\r\n            \"new_stcn\": \"12689747\",\r\n            \"rdmp_stcn\": \"9723610\",\r\n            \"prdy_rmnd_vrss\": \"2966137\",\r\n            \"rmnd_stcn\": \"933766914\",\r\n            \"rmnd_amt\": \"45180305\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240401\",\r\n            \"stck_prpr\": \"2747.86\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1.23\",\r\n            \"prdy_ctrt\": \"0.04\",\r\n            \"acml_vol\": \"397600500\",\r\n            \"new_stcn\": \"8654205\",\r\n            \"rdmp_stcn\": \"9951822\",\r\n            \"prdy_rmnd_vrss\": \"-1297617\",\r\n            \"rmnd_stcn\": \"930800777\",\r\n            \"rmnd_amt\": \"45158153\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHKST03900400",
    "name": "종목조건검색조회",
    "url": "/uapi/domestic-stock/v1/quotations/psearch-result",
    "sheet": "종목조건검색조회",
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
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "daebi",
        "type": "string",
        "required": "Y",
        "description": "1. 상한 2. 상승 3. 보합 4. 하한 5. 하락"
      },
      {
        "element": "price",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "chgrate",
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
        "element": "trade_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "change",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cttr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "open",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "high",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "low",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "high52",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "low52",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "expprice",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "expchange",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "expchggrate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "expcvol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "chgrate2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "expdaebi",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "recprice",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "uplmtprice",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dnlmtprice",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stotprice",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\t\"user_id\":\"abcd4321\",\r\n\t\"seq\":\"0\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output2\": [\r\n        {\r\n            \"code\": \"000120\",\r\n            \"name\": \"CJ대한통운\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000138600.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"     148600.0000\",\r\n            \"low52\": \"      69000.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"     138600.0000\",\r\n            \"uplmtprice\": \"     180100.0000\",\r\n            \"dnlmtprice\": \"      97100.0000\",\r\n            \"stotprice\": \"      31617.9088\"\r\n        },\r\n        {\r\n            \"code\": \"002320\",\r\n            \"name\": \"한진\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000024350.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      27300.0000\",\r\n            \"low52\": \"      18010.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      24350.0000\",\r\n            \"uplmtprice\": \"      31650.0000\",\r\n            \"dnlmtprice\": \"      17050.0000\",\r\n            \"stotprice\": \"       3639.7474\"\r\n        },\r\n        {\r\n            \"code\": \"002680\",\r\n            \"name\": \"한탑\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000001234.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       2275.0000\",\r\n            \"low52\": \"       1125.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       1234.0000\",\r\n            \"uplmtprice\": \"       1604.0000\",\r\n            \"dnlmtprice\": \"        864.0000\",\r\n            \"stotprice\": \"        398.7893\"\r\n        },\r\n        {\r\n            \"code\": \"004710\",\r\n            \"name\": \"한솔테크닉스\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000007070.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       8390.0000\",\r\n            \"low52\": \"       5230.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       7070.0000\",\r\n            \"uplmtprice\": \"       9190.0000\",\r\n            \"dnlmtprice\": \"       4950.0000\",\r\n            \"stotprice\": \"       2270.1684\"\r\n        },\r\n        {\r\n            \"code\": \"005300\",\r\n            \"name\": \"롯데칠성\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000127600.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"     174900.0000\",\r\n            \"low52\": \"     117300.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"     127600.0000\",\r\n            \"uplmtprice\": \"     165800.0000\",\r\n            \"dnlmtprice\": \"      89400.0000\",\r\n            \"stotprice\": \"      11839.8560\"\r\n        },\r\n        {\r\n            \"code\": \"009070\",\r\n            \"name\": \"KCTC\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000004145.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       5390.0000\",\r\n            \"low52\": \"       3550.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       4145.0000\",\r\n            \"uplmtprice\": \"       5380.0000\",\r\n            \"dnlmtprice\": \"       2905.0000\",\r\n            \"stotprice\": \"       1243.5000\"\r\n        },\r\n        {\r\n            \"code\": \"010420\",\r\n            \"name\": \"한솔PNS\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000001221.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       1750.0000\",\r\n            \"low52\": \"       1181.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       1221.0000\",\r\n            \"uplmtprice\": \"       1587.0000\",\r\n            \"dnlmtprice\": \"        855.0000\",\r\n            \"stotprice\": \"        250.2197\"\r\n        },\r\n        {\r\n            \"code\": \"015260\",\r\n            \"name\": \"에이엔피\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000001052.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       2620.0000\",\r\n            \"low52\": \"       1034.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       1052.0000\",\r\n            \"uplmtprice\": \"       1367.0000\",\r\n            \"dnlmtprice\": \"        737.0000\",\r\n            \"stotprice\": \"        474.6297\"\r\n        },\r\n        {\r\n            \"code\": \"015360\",\r\n            \"name\": \"예스코홀딩스\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000037000.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      37750.0000\",\r\n            \"low52\": \"      30400.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      37000.0000\",\r\n            \"uplmtprice\": \"      48100.0000\",\r\n            \"dnlmtprice\": \"      25900.0000\",\r\n            \"stotprice\": \"       2220.0000\"\r\n        },\r\n        {\r\n            \"code\": \"036460\",\r\n            \"name\": \"한국가스공사\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000026800.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      32250.0000\",\r\n            \"low52\": \"      22750.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      26800.0000\",\r\n            \"uplmtprice\": \"      34800.0000\",\r\n            \"dnlmtprice\": \"      18800.0000\",\r\n            \"stotprice\": \"      24739.8840\"\r\n        },\r\n        {\r\n            \"code\": \"036710\",\r\n            \"name\": \"심텍홀딩스\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000002900.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       4190.0000\",\r\n            \"low52\": \"       2380.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       2900.0000\",\r\n            \"uplmtprice\": \"       3770.0000\",\r\n            \"dnlmtprice\": \"       2030.0000\",\r\n            \"stotprice\": \"       1402.1542\"\r\n        },\r\n        {\r\n            \"code\": \"036800\",\r\n            \"name\": \"나이스정보통신\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000022350.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      29500.0000\",\r\n            \"low52\": \"      19910.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      22350.0000\",\r\n            \"uplmtprice\": \"      29050.0000\",\r\n            \"dnlmtprice\": \"      15650.0000\",\r\n            \"stotprice\": \"       2235.0000\"\r\n        },\r\n        {\r\n            \"code\": \"053050\",\r\n            \"name\": \"지에스이\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000003525.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       5570.0000\",\r\n            \"low52\": \"       2810.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       3525.0000\",\r\n            \"uplmtprice\": \"       4580.0000\",\r\n            \"dnlmtprice\": \"       2470.0000\",\r\n            \"stotprice\": \"       1057.0628\"\r\n        },\r\n        {\r\n            \"code\": \"053450\",\r\n            \"name\": \"세코닉스\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000008000.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       9960.0000\",\r\n            \"low52\": \"       5370.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       8000.0000\",\r\n            \"uplmtprice\": \"      10400.0000\",\r\n            \"dnlmtprice\": \"       5600.0000\",\r\n            \"stotprice\": \"       1183.4242\"\r\n        },\r\n        {\r\n            \"code\": \"058850\",\r\n            \"name\": \"KTcs\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000003800.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       5920.0000\",\r\n            \"low52\": \"       2790.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       3800.0000\",\r\n            \"uplmtprice\": \"       4940.0000\",\r\n            \"dnlmtprice\": \"       2660.0000\",\r\n            \"stotprice\": \"       1622.0300\"\r\n        },\r\n        {\r\n            \"code\": \"058860\",\r\n            \"name\": \"KTis\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000003080.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       5230.0000\",\r\n            \"low52\": \"       2695.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       3080.0000\",\r\n            \"uplmtprice\": \"       4000.0000\",\r\n            \"dnlmtprice\": \"       2160.0000\",\r\n            \"stotprice\": \"       1071.9016\"\r\n        },\r\n        {\r\n            \"code\": \"063570\",\r\n            \"name\": \"한국전자금융\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000006610.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       7520.0000\",\r\n            \"low52\": \"       4665.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       6610.0000\",\r\n            \"uplmtprice\": \"       8590.0000\",\r\n            \"dnlmtprice\": \"       4630.0000\",\r\n            \"stotprice\": \"       2257.1648\"\r\n        },\r\n        {\r\n            \"code\": \"069640\",\r\n            \"name\": \"한세엠케이\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000002095.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       4170.0000\",\r\n            \"low52\": \"       1960.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       2095.0000\",\r\n            \"uplmtprice\": \"       2720.0000\",\r\n            \"dnlmtprice\": \"       1470.0000\",\r\n            \"stotprice\": \"        630.7312\"\r\n        },\r\n        {\r\n            \"code\": \"071670\",\r\n            \"name\": \"에이테크솔루션\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000010860.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      15200.0000\",\r\n            \"low52\": \"       9500.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      10860.0000\",\r\n            \"uplmtprice\": \"      14110.0000\",\r\n            \"dnlmtprice\": \"       7610.0000\",\r\n            \"stotprice\": \"       1086.0000\"\r\n        },\r\n        {\r\n            \"code\": \"085660\",\r\n            \"name\": \"차바이오텍\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000018010.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      23100.0000\",\r\n            \"low52\": \"      11790.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      18010.0000\",\r\n            \"uplmtprice\": \"      23400.0000\",\r\n            \"dnlmtprice\": \"      12610.0000\",\r\n            \"stotprice\": \"      10142.2312\"\r\n        },\r\n        {\r\n            \"code\": \"092300\",\r\n            \"name\": \"현우산업\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000004315.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       6850.0000\",\r\n            \"low52\": \"       3570.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       4315.0000\",\r\n            \"uplmtprice\": \"       5600.0000\",\r\n            \"dnlmtprice\": \"       3025.0000\",\r\n            \"stotprice\": \"        805.7320\"\r\n        },\r\n        {\r\n            \"code\": \"111110\",\r\n            \"name\": \"호전실업\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000007740.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       9100.0000\",\r\n            \"low52\": \"       7290.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       7740.0000\",\r\n            \"uplmtprice\": \"      10060.0000\",\r\n            \"dnlmtprice\": \"       5420.0000\",\r\n            \"stotprice\": \"        754.6488\"\r\n        },\r\n        {\r\n            \"code\": \"115530\",\r\n            \"name\": \"씨엔플러스\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000000325.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"        650.0000\",\r\n            \"low52\": \"        301.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"        325.0000\",\r\n            \"uplmtprice\": \"        422.0000\",\r\n            \"dnlmtprice\": \"        228.0000\",\r\n            \"stotprice\": \"        220.8798\"\r\n        },\r\n        {\r\n            \"code\": \"128820\",\r\n            \"name\": \"대성산업\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000004000.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       5000.0000\",\r\n            \"low52\": \"       3405.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       4000.0000\",\r\n            \"uplmtprice\": \"       5200.0000\",\r\n            \"dnlmtprice\": \"       2800.0000\",\r\n            \"stotprice\": \"       1809.4191\"\r\n        },\r\n        {\r\n            \"code\": \"145210\",\r\n            \"name\": \"다이나믹디자인\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000005720.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      12630.0000\",\r\n            \"low52\": \"       2780.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       5720.0000\",\r\n            \"uplmtprice\": \"       7430.0000\",\r\n            \"dnlmtprice\": \"       4010.0000\",\r\n            \"stotprice\": \"        989.6225\"\r\n        },\r\n        {\r\n            \"code\": \"210120\",\r\n            \"name\": \"빅텐츠\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000016170.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      45700.0000\",\r\n            \"low52\": \"       9050.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      16170.0000\",\r\n            \"uplmtprice\": \"      21000.0000\",\r\n            \"dnlmtprice\": \"      11320.0000\",\r\n            \"stotprice\": \"        508.4834\"\r\n        },\r\n        {\r\n            \"code\": \"214680\",\r\n            \"name\": \"디알텍\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000003990.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       7590.0000\",\r\n            \"low52\": \"       1513.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       3990.0000\",\r\n            \"uplmtprice\": \"       5180.0000\",\r\n            \"dnlmtprice\": \"       2795.0000\",\r\n            \"stotprice\": \"       2921.4692\"\r\n        },\r\n        {\r\n            \"code\": \"216050\",\r\n            \"name\": \"인크로스\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000011110.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"      20550.0000\",\r\n            \"low52\": \"       9690.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"      11110.0000\",\r\n            \"uplmtprice\": \"      14440.0000\",\r\n            \"dnlmtprice\": \"       7780.0000\",\r\n            \"stotprice\": \"       1426.8820\"\r\n        },\r\n        {\r\n            \"code\": \"221840\",\r\n            \"name\": \"하이즈항공\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000002420.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       3835.0000\",\r\n            \"low52\": \"       2385.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       2420.0000\",\r\n            \"uplmtprice\": \"       3145.0000\",\r\n            \"dnlmtprice\": \"       1695.0000\",\r\n            \"stotprice\": \"        452.5536\"\r\n        },\r\n        {\r\n            \"code\": \"278650\",\r\n            \"name\": \"HLB바이오스텝\",\r\n            \"daebi\": \"0\",\r\n            \"price\": \"00000003870.0000\",\r\n            \"chgrate\": \"          0.0000\",\r\n            \"acml_vol\": \"          0.0000\",\r\n            \"trade_amt\": \"          0.0000\",\r\n            \"change\": \"          0.0000\",\r\n            \"cttr\": \"          0.0000\",\r\n            \"open\": \"          0.0000\",\r\n            \"high\": \"          0.0000\",\r\n            \"low\": \"          0.0000\",\r\n            \"high52\": \"       5380.0000\",\r\n            \"low52\": \"       2430.0000\",\r\n            \"expprice\": \"00000000000.0000\",\r\n            \"expchange\": \"          0.0000\",\r\n            \"expchggrate\": \"       -100.0000\",\r\n            \"expcvol\": \"          0.0000\",\r\n            \"chgrate2\": \"          0.0000\",\r\n            \"expdaebi\": \"5\",\r\n            \"recprice\": \"       3870.0000\",\r\n            \"uplmtprice\": \"       5030.0000\",\r\n            \"dnlmtprice\": \"       2710.0000\",\r\n            \"stotprice\": \"       3106.5775\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01130000",
    "name": "국내주식 매물대_거래비중",
    "url": "/uapi/domestic-stock/v1/quotations/pbar-tratio",
    "sheet": "국내주식 매물대_거래비중",
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
        "element": "rprs_mrkt_kor_name",
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
        "element": "prdy_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "wghn_avrg_stck_prc",
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
        "element": "output2",
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
        "element": "stck_prpr",
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
        "element": "acml_vol_rlim",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_INPUT_ISCD:136480\r\nFID_COND_SCR_DIV_CODE:20113\r\nFID_INPUT_HOUR_1:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"rprs_mrkt_kor_name\": \"KOSDAQ\",\r\n        \"stck_shrn_iscd\": \"136480\",\r\n        \"hts_kor_isnm\": \"하림\",\r\n        \"stck_prpr\": \"3240\",\r\n        \"prdy_vrss_sign\": \"5\",\r\n        \"prdy_vrss\": \"-65\",\r\n        \"prdy_ctrt\": \"-1.97\",\r\n        \"acml_vol\": \"847563\",\r\n        \"prdy_vol\": \"974060\",\r\n        \"wghn_avrg_stck_prc\": \"3256.34\",\r\n        \"lstn_stcn\": \"106209702\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"data_rank\": \"1\",\r\n            \"stck_prpr\": \"3255\",\r\n            \"cntg_vol\": \"124515\",\r\n            \"acml_vol_rlim\": \"14.69\"\r\n        },\r\n        {\r\n            \"data_rank\": \"2\",\r\n            \"stck_prpr\": \"3260\",\r\n            \"cntg_vol\": \"123909\",\r\n            \"acml_vol_rlim\": \"14.62\"\r\n        },\r\n        {\r\n            \"data_rank\": \"3\",\r\n            \"stck_prpr\": \"3250\",\r\n            \"cntg_vol\": \"87983\",\r\n            \"acml_vol_rlim\": \"10.38\"\r\n        },\r\n        {\r\n            \"data_rank\": \"4\",\r\n            \"stck_prpr\": \"3245\",\r\n            \"cntg_vol\": \"83496\",\r\n            \"acml_vol_rlim\": \"9.85\"\r\n        },\r\n        {\r\n            \"data_rank\": \"5\",\r\n            \"stck_prpr\": \"3235\",\r\n            \"cntg_vol\": \"72101\",\r\n            \"acml_vol_rlim\": \"8.51\"\r\n        },\r\n        {\r\n            \"data_rank\": \"6\",\r\n            \"stck_prpr\": \"3240\",\r\n            \"cntg_vol\": \"70712\",\r\n            \"acml_vol_rlim\": \"8.34\"\r\n        },\r\n        {\r\n            \"data_rank\": \"7\",\r\n            \"stck_prpr\": \"3265\",\r\n            \"cntg_vol\": \"65838\",\r\n            \"acml_vol_rlim\": \"7.77\"\r\n        },\r\n        {\r\n            \"data_rank\": \"8\",\r\n            \"stck_prpr\": \"3275\",\r\n            \"cntg_vol\": \"57283\",\r\n            \"acml_vol_rlim\": \"6.76\"\r\n        },\r\n        {\r\n            \"data_rank\": \"9\",\r\n            \"stck_prpr\": \"3270\",\r\n            \"cntg_vol\": \"56295\",\r\n            \"acml_vol_rlim\": \"6.64\"\r\n        },\r\n        {\r\n            \"data_rank\": \"10\",\r\n            \"stck_prpr\": \"3230\",\r\n            \"cntg_vol\": \"30998\",\r\n            \"acml_vol_rlim\": \"3.66\"\r\n        },\r\n        {\r\n            \"data_rank\": \"11\",\r\n            \"stck_prpr\": \"3290\",\r\n            \"cntg_vol\": \"27419\",\r\n            \"acml_vol_rlim\": \"3.24\"\r\n        },\r\n        {\r\n            \"data_rank\": \"12\",\r\n            \"stck_prpr\": \"3280\",\r\n            \"cntg_vol\": \"15080\",\r\n            \"acml_vol_rlim\": \"1.78\"\r\n        },\r\n        {\r\n            \"data_rank\": \"13\",\r\n            \"stck_prpr\": \"3295\",\r\n            \"cntg_vol\": \"13623\",\r\n            \"acml_vol_rlim\": \"1.61\"\r\n        },\r\n        {\r\n            \"data_rank\": \"14\",\r\n            \"stck_prpr\": \"3285\",\r\n            \"cntg_vol\": \"9580\",\r\n            \"acml_vol_rlim\": \"1.13\"\r\n        },\r\n        {\r\n            \"data_rank\": \"15\",\r\n            \"stck_prpr\": \"3310\",\r\n            \"cntg_vol\": \"3646\",\r\n            \"acml_vol_rlim\": \"0.43\"\r\n        },\r\n        {\r\n            \"data_rank\": \"16\",\r\n            \"stck_prpr\": \"3225\",\r\n            \"cntg_vol\": \"2199\",\r\n            \"acml_vol_rlim\": \"0.26\"\r\n        },\r\n        {\r\n            \"data_rank\": \"17\",\r\n            \"stck_prpr\": \"3300\",\r\n            \"cntg_vol\": \"1898\",\r\n            \"acml_vol_rlim\": \"0.22\"\r\n        },\r\n        {\r\n            \"data_rank\": \"18\",\r\n            \"stck_prpr\": \"3305\",\r\n            \"cntg_vol\": \"988\",\r\n            \"acml_vol_rlim\": \"0.12\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPTJ04400000",
    "name": "국내기관_외국인 매매종목가집계",
    "url": "/uapi/domestic-stock/v1/quotations/foreign-institution-total",
    "sheet": "국내기관_외국인 매매종목가집계",
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
        "element": "Output",
        "type": "object",
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
        "element": "ntby_qty",
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
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": "frgn_ntby_tr_pbmn ~ etc_corp_ntby_tr_pbmn\r\n(단위 : 백만원, 수량*현재가)"
      },
      {
        "element": "orgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHKCM113004C6",
    "name": "관심종목 그룹별 종목조회",
    "url": "/uapi/domestic-stock/v1/quotations/intstock-stocklist-by-group",
    "sheet": "관심종목 그룹별 종목조회",
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
        "element": "data_rank",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter_grp_name",
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
        "element": "fid_mrkt_cls_code",
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
        "element": "exch_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jong_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "color_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "memo",
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
        "element": "fxdt_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cntg_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cntg_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TYPE:1\r\nUSER_ID:{{HTS_ID}}\r\nDATA_RANK:\r\nINTER_GRP_CODE:002\r\nINTER_GRP_NAME:\r\nHTS_KOR_ISNM:\r\nCNTG_CLS_CODE:\r\nFID_ETC_CLS_CODE:4",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"data_rank\": \"0000000002\",\r\n        \"inter_grp_name\": \"관심종목02\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000001\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"006840\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AK홀딩스\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000002\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"054620\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"APS홀딩스\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000003\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"265520\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AP시스템\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000004\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"211270\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AP위성\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000005\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"138930\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"BNK금융지주\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000006\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"001460\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"BYC\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000007\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"001465\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"BYC우\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000008\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"013720\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CBI\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000009\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"001040\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000010\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"079160\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ CGV\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000011\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"035760\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ ENM\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000012\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"311690\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ 바이오사이언스\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000013\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"00104K\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ4우(전환)\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000014\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"000120\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ대한통운\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000015\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"011150\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ씨푸드\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000016\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"011155\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"CJ씨푸드1우\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000017\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"060310\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"3S\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000018\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"095570\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AJ네트웍스\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000019\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"006840\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AK홀딩스\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000020\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"054620\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"APS\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000021\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"265520\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AP시스템\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        },\r\n        {\r\n            \"fid_mrkt_cls_code\": \"J\",\r\n            \"data_rank\": \"0000000022\",\r\n            \"exch_code\": \"KRX\",\r\n            \"jong_code\": \"211270\",\r\n            \"color_code\": \"-1\",\r\n            \"memo\": \"\",\r\n            \"hts_kor_isnm\": \"AP위성\",\r\n            \"fxdt_ntby_qty\": \"0\",\r\n            \"cntg_unpr\": \"0.000000\",\r\n            \"cntg_cls_code\": \"0\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST04540000",
    "name": "주식현재가 회원사 종목매매동향",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-member-daily",
    "sheet": "주식현재가 회원사 종목매매동향",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
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
        "element": "ntby_qty",
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
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_INPUT_ISCD:136480\r\nFID_INPUT_ISCD_2:00003\r\nFID_INPUT_DATE_1:20240501\r\nFID_INPUT_DATE_2:20240530\r\nFID_SCTN_CLS_CODE:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240530\",\r\n            \"total_seln_qty\": \"55432\",\r\n            \"total_shnu_qty\": \"81112\",\r\n            \"ntby_qty\": \"25680\",\r\n            \"stck_prpr\": \"3240\",\r\n            \"prdy_vrss\": \"-65\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.97\",\r\n            \"acml_vol\": \"862835\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240529\",\r\n            \"total_seln_qty\": \"53901\",\r\n            \"total_shnu_qty\": \"130678\",\r\n            \"ntby_qty\": \"76777\",\r\n            \"stck_prpr\": \"3305\",\r\n            \"prdy_vrss\": \"-30\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.90\",\r\n            \"acml_vol\": \"974060\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240528\",\r\n            \"total_seln_qty\": \"139470\",\r\n            \"total_shnu_qty\": \"209017\",\r\n            \"ntby_qty\": \"69547\",\r\n            \"stck_prpr\": \"3335\",\r\n            \"prdy_vrss\": \"-30\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.89\",\r\n            \"acml_vol\": \"1553914\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240527\",\r\n            \"total_seln_qty\": \"239813\",\r\n            \"total_shnu_qty\": \"246930\",\r\n            \"ntby_qty\": \"7117\",\r\n            \"stck_prpr\": \"3365\",\r\n            \"prdy_vrss\": \"-30\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.88\",\r\n            \"acml_vol\": \"1750949\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240524\",\r\n            \"total_seln_qty\": \"1451049\",\r\n            \"total_shnu_qty\": \"1526087\",\r\n            \"ntby_qty\": \"75038\",\r\n            \"stck_prpr\": \"3395\",\r\n            \"prdy_vrss\": \"110\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.35\",\r\n            \"acml_vol\": \"11758204\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240523\",\r\n            \"total_seln_qty\": \"120530\",\r\n            \"total_shnu_qty\": \"159459\",\r\n            \"ntby_qty\": \"38929\",\r\n            \"stck_prpr\": \"3285\",\r\n            \"prdy_vrss\": \"-40\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.20\",\r\n            \"acml_vol\": \"1532424\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240522\",\r\n            \"total_seln_qty\": \"290601\",\r\n            \"total_shnu_qty\": \"292948\",\r\n            \"ntby_qty\": \"2347\",\r\n            \"stck_prpr\": \"3325\",\r\n            \"prdy_vrss\": \"60\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"1.84\",\r\n            \"acml_vol\": \"2579194\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240521\",\r\n            \"total_seln_qty\": \"118718\",\r\n            \"total_shnu_qty\": \"75046\",\r\n            \"ntby_qty\": \"-43672\",\r\n            \"stck_prpr\": \"3265\",\r\n            \"prdy_vrss\": \"20\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.62\",\r\n            \"acml_vol\": \"979173\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240520\",\r\n            \"total_seln_qty\": \"400866\",\r\n            \"total_shnu_qty\": \"290925\",\r\n            \"ntby_qty\": \"-109941\",\r\n            \"stck_prpr\": \"3245\",\r\n            \"prdy_vrss\": \"30\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.93\",\r\n            \"acml_vol\": \"3346515\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240517\",\r\n            \"total_seln_qty\": \"316302\",\r\n            \"total_shnu_qty\": \"397728\",\r\n            \"ntby_qty\": \"81426\",\r\n            \"stck_prpr\": \"3215\",\r\n            \"prdy_vrss\": \"60\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"1.90\",\r\n            \"acml_vol\": \"3089567\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240516\",\r\n            \"total_seln_qty\": \"107617\",\r\n            \"total_shnu_qty\": \"82162\",\r\n            \"ntby_qty\": \"-25455\",\r\n            \"stck_prpr\": \"3155\",\r\n            \"prdy_vrss\": \"-30\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.94\",\r\n            \"acml_vol\": \"767201\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240514\",\r\n            \"total_seln_qty\": \"59559\",\r\n            \"total_shnu_qty\": \"57909\",\r\n            \"ntby_qty\": \"-1650\",\r\n            \"stck_prpr\": \"3185\",\r\n            \"prdy_vrss\": \"45\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"1.43\",\r\n            \"acml_vol\": \"667569\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240513\",\r\n            \"total_seln_qty\": \"70787\",\r\n            \"total_shnu_qty\": \"91304\",\r\n            \"ntby_qty\": \"20517\",\r\n            \"stck_prpr\": \"3140\",\r\n            \"prdy_vrss\": \"-50\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.57\",\r\n            \"acml_vol\": \"1291905\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240510\",\r\n            \"total_seln_qty\": \"227523\",\r\n            \"total_shnu_qty\": \"160715\",\r\n            \"ntby_qty\": \"-66808\",\r\n            \"stck_prpr\": \"3190\",\r\n            \"prdy_vrss\": \"45\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"1.43\",\r\n            \"acml_vol\": \"1841506\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240509\",\r\n            \"total_seln_qty\": \"331604\",\r\n            \"total_shnu_qty\": \"160679\",\r\n            \"ntby_qty\": \"-170925\",\r\n            \"stck_prpr\": \"3145\",\r\n            \"prdy_vrss\": \"-15\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.47\",\r\n            \"acml_vol\": \"2145427\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240508\",\r\n            \"total_seln_qty\": \"158034\",\r\n            \"total_shnu_qty\": \"154720\",\r\n            \"ntby_qty\": \"-3314\",\r\n            \"stck_prpr\": \"3160\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.27\",\r\n            \"acml_vol\": \"1915227\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240507\",\r\n            \"total_seln_qty\": \"23239\",\r\n            \"total_shnu_qty\": \"52555\",\r\n            \"ntby_qty\": \"29316\",\r\n            \"stck_prpr\": \"3060\",\r\n            \"prdy_vrss\": \"-10\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.33\",\r\n            \"acml_vol\": \"351326\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240503\",\r\n            \"total_seln_qty\": \"66664\",\r\n            \"total_shnu_qty\": \"94801\",\r\n            \"ntby_qty\": \"28137\",\r\n            \"stck_prpr\": \"3070\",\r\n            \"prdy_vrss\": \"-15\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.49\",\r\n            \"acml_vol\": \"420729\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240502\",\r\n            \"total_seln_qty\": \"46034\",\r\n            \"total_shnu_qty\": \"46915\",\r\n            \"ntby_qty\": \"881\",\r\n            \"stck_prpr\": \"3085\",\r\n            \"prdy_vrss\": \"30\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.98\",\r\n            \"acml_vol\": \"473617\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPPG04650201",
    "name": "종목별 프로그램매매추이(일별)",
    "url": "/uapi/domestic-stock/v1/quotations/program-trade-by-stock-daily",
    "sheet": "종목별 프로그램매매추이(일별)",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_clpr",
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
        "element": "whol_smtn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_ntby_vol_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_ntby_tr_pbmn_icdc2",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_INPUT_ISCD:005930\r\nFID_INPUT_DATE_1:20240517",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240517\",\r\n            \"stck_clpr\": \"77400\",\r\n            \"prdy_vrss\": \"-800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.02\",\r\n            \"acml_vol\": \"15698949\",\r\n            \"acml_tr_pbmn\": \"1220563293000\",\r\n            \"whol_smtn_seln_vol\": \"6910299\",\r\n            \"whol_smtn_shnu_vol\": \"3468820\",\r\n            \"whol_smtn_ntby_qty\": \"-3441479\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"536935491000\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"270120727200\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"-266814763800\",\r\n            \"whol_ntby_vol_icdc\": \"-3989127\",\r\n            \"whol_ntby_tr_pbmn_icdc2\": \"-311124223700\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240516\",\r\n            \"stck_clpr\": \"78200\",\r\n            \"prdy_vrss\": \"-100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.13\",\r\n            \"acml_vol\": \"20989778\",\r\n            \"acml_tr_pbmn\": \"1656384883213\",\r\n            \"whol_smtn_seln_vol\": \"4747160\",\r\n            \"whol_smtn_shnu_vol\": \"5294808\",\r\n            \"whol_smtn_ntby_qty\": \"547648\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"374517364400\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"418826824300\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"44309459900\",\r\n            \"whol_ntby_vol_icdc\": \"631626\",\r\n            \"whol_ntby_tr_pbmn_icdc2\": \"50772364600\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240514\",\r\n            \"stck_clpr\": \"78300\",\r\n            \"prdy_vrss\": \"-100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-0.13\",\r\n            \"acml_vol\": \"11763992\",\r\n            \"acml_tr_pbmn\": \"920737809850\",\r\n            \"whol_smtn_seln_vol\": \"2056263\",\r\n            \"whol_smtn_shnu_vol\": \"1972285\",\r\n            \"whol_smtn_ntby_qty\": \"-83978\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"160973460500\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"154510555800\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"-6462904700\",\r\n            \"whol_ntby_vol_icdc\": \"867690\",\r\n            \"whol_ntby_tr_pbmn_icdc2\": \"67673387000\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240513\",\r\n            \"stck_clpr\": \"78400\",\r\n            \"prdy_vrss\": \"-800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.01\",\r\n            \"acml_vol\": \"18652344\",\r\n            \"acml_tr_pbmn\": \"1460962492700\",\r\n            \"whol_smtn_seln_vol\": \"3971918\",\r\n            \"whol_smtn_shnu_vol\": \"3020250\",\r\n            \"whol_smtn_ntby_qty\": \"-951668\",\r\n            \"whol_smtn_seln_tr_pbmn\": \"311400439700\",\r\n            \"whol_smtn_shnu_tr_pbmn\": \"237264148000\",\r\n            \"whol_smtn_ntby_tr_pbmn\": \"-74136291700\",\r\n            \"whol_ntby_vol_icdc\": \"-1111550\",\r\n            \"whol_ntby_tr_pbmn_icdc2\": \"-87529870000\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHKCM113004C7",
    "name": "관심종목 그룹조회",
    "url": "/uapi/domestic-stock/v1/quotations/intstock-grouplist",
    "sheet": "관심종목 그룹조회",
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
        "element": "output2",
        "type": "object",
        "required": "Y",
        "description": ""
      },
      {
        "element": "date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trnm_hour",
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
        "element": "inter_grp_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter_grp_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ask_cnt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "TYPE:1\r\nFID_ETC_CLS_CODE:00\r\nUSER_ID:{{HTS_ID}}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output2\": [\r\n        {\r\n            \"date\": \"20230517\",\r\n            \"trnm_hour\": \"171648\",\r\n            \"data_rank\": \"0000000000\",\r\n            \"inter_grp_code\": \"001\",\r\n            \"inter_grp_name\": \"조건검색결과\",\r\n            \"ask_cnt\": \"100\"\r\n        },\r\n        {\r\n            \"date\": \"20240318\",\r\n            \"trnm_hour\": \"133351\",\r\n            \"data_rank\": \"0000000001\",\r\n            \"inter_grp_code\": \"000\",\r\n            \"inter_grp_name\": \"기본그룹1\",\r\n            \"ask_cnt\": \"011\"\r\n        },\r\n        {\r\n            \"date\": \"20240529\",\r\n            \"trnm_hour\": \"090525\",\r\n            \"data_rank\": \"0000000002\",\r\n            \"inter_grp_code\": \"002\",\r\n            \"inter_grp_name\": \"관심종목02\",\r\n            \"ask_cnt\": \"022\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHPTJ04160200",
    "name": "종목별 외인기관 추정가집계",
    "url": "/uapi/domestic-stock/v1/quotations/investor-trend-estimate",
    "sheet": "종목별 외인기관 추정가집계",
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
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "bsop_hour_gb",
        "type": "string",
        "required": "Y",
        "description": "1: 09시 30분 입력\r\n2: 10시 00분 입력 \r\n3: 11시 20분 입력 \r\n4: 13시 20분 입력 \r\n5: 14시 30분 입력"
      },
      {
        "element": "frgn_fake_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_fake_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sum_fake_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n   \"MKSC_SHRN_ISCD\":\"000660\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output2\": [\r\n        {\r\n            \"bsop_hour_gb\": \"5\",\r\n            \"frgn_fake_ntby_qty\": \"-00000000000030000\",\r\n            \"orgn_fake_ntby_qty\": \"000000000000121000\",\r\n            \"sum_fake_ntby_qty\": \"000000000000091000\"\r\n        },\r\n        {\r\n            \"bsop_hour_gb\": \"4\",\r\n            \"frgn_fake_ntby_qty\": \"-00000000000093000\",\r\n            \"orgn_fake_ntby_qty\": \"000000000000130000\",\r\n            \"sum_fake_ntby_qty\": \"000000000000037000\"\r\n        },\r\n        {\r\n            \"bsop_hour_gb\": \"3\",\r\n            \"frgn_fake_ntby_qty\": \"-00000000000026000\",\r\n            \"orgn_fake_ntby_qty\": \"000000000000037000\",\r\n            \"sum_fake_ntby_qty\": \"000000000000011000\"\r\n        },\r\n        {\r\n            \"bsop_hour_gb\": \"2\",\r\n            \"frgn_fake_ntby_qty\": \"-00000000000038000\",\r\n            \"orgn_fake_ntby_qty\": \"000000000000022000\",\r\n            \"sum_fake_ntby_qty\": \"-00000000000016000\"\r\n        },\r\n        {\r\n            \"bsop_hour_gb\": \"1\",\r\n            \"frgn_fake_ntby_qty\": \"-00000000000023000\",\r\n            \"orgn_fake_ntby_qty\": \"000000000000000000\",\r\n            \"sum_fake_ntby_qty\": \"-00000000000023000\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST03010800",
    "name": "종목별일별매수매도체결량",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-daily-trade-volume",
    "sheet": "종목별일별매수매도체결량",
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
        "element": "shnu_cnqn_smtn",
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
        "element": "output2",
        "type": "object array",
        "required": "Y",
        "description": "array"
      },
      {
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
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
        "element": "{\r\n\t\"fid_cond_mrkt_div_code\":\"J\",\r\n\t\"fid_input_iscd\":\"005930\",\r\n\t\"fid_input_date_1\":\"20240101\",\r\n\t\"fid_input_date_2\":\"20240126\",\r\n\t\"fid_period_div_code\":\"D\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"shnu_cnqn_smtn\": \"4520816\",\r\n        \"seln_cnqn_smtn\": \"5285722\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240126\",\r\n            \"total_seln_qty\": \"5285722\",\r\n            \"total_shnu_qty\": \"4520816\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240125\",\r\n            \"total_seln_qty\": \"5610781\",\r\n            \"total_shnu_qty\": \"4008095\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240124\",\r\n            \"total_seln_qty\": \"7001409\",\r\n            \"total_shnu_qty\": \"4628223\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240123\",\r\n            \"total_seln_qty\": \"6929612\",\r\n            \"total_shnu_qty\": \"6221072\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240122\",\r\n            \"total_seln_qty\": \"9304203\",\r\n            \"total_shnu_qty\": \"8269298\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240119\",\r\n            \"total_seln_qty\": \"7937786\",\r\n            \"total_shnu_qty\": \"12024544\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240118\",\r\n            \"total_seln_qty\": \"7130130\",\r\n            \"total_shnu_qty\": \"8051305\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240117\",\r\n            \"total_seln_qty\": \"12448352\",\r\n            \"total_shnu_qty\": \"7781842\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240116\",\r\n            \"total_seln_qty\": \"7231456\",\r\n            \"total_shnu_qty\": \"5660392\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240115\",\r\n            \"total_seln_qty\": \"5146657\",\r\n            \"total_shnu_qty\": \"6242907\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240112\",\r\n            \"total_seln_qty\": \"6112124\",\r\n            \"total_shnu_qty\": \"5706461\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240111\",\r\n            \"total_seln_qty\": \"10835895\",\r\n            \"total_shnu_qty\": \"10905905\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240110\",\r\n            \"total_seln_qty\": \"12367976\",\r\n            \"total_shnu_qty\": \"6256368\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240109\",\r\n            \"total_seln_qty\": \"16376304\",\r\n            \"total_shnu_qty\": \"7458947\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240108\",\r\n            \"total_seln_qty\": \"5318849\",\r\n            \"total_shnu_qty\": \"4631085\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240105\",\r\n            \"total_seln_qty\": \"4907468\",\r\n            \"total_shnu_qty\": \"5219184\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240104\",\r\n            \"total_seln_qty\": \"6041013\",\r\n            \"total_shnu_qty\": \"7038798\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240103\",\r\n            \"total_seln_qty\": \"12066549\",\r\n            \"total_shnu_qty\": \"7713276\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240102\",\r\n            \"total_seln_qty\": \"5855872\",\r\n            \"total_shnu_qty\": \"9333762\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST111900C0",
    "name": "국내주식 체결금액별 매매비중",
    "url": "/uapi/domestic-stock/v1/quotations/tradprt-byamt",
    "sheet": "국내주식 체결금액별 매매비중",
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
        "element": "prpr_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "smtn_avrg_prpr",
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
        "element": "whol_ntby_qty_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ntby_cntg_csnu",
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
        "element": "whol_seln_vol_rate",
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
        "element": "shnu_cnqn_smtn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_shun_vol_rate",
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
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_COND_SCR_DIV_CODE:11119\r\nFID_INPUT_ISCD:005930",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"prpr_name\": \"3백 이하\",\r\n            \"smtn_avrg_prpr\": \"78315\",\r\n            \"acml_vol\": \"291426\",\r\n            \"whol_ntby_qty_rate\": \"0.37\",\r\n            \"ntby_cntg_csnu\": \"13297\",\r\n            \"seln_cnqn_smtn\": \"126451\",\r\n            \"whol_seln_vol_rate\": \"1.21\",\r\n            \"seln_cntg_csnu\": \"16084\",\r\n            \"shnu_cnqn_smtn\": \"164975\",\r\n            \"whol_shun_vol_rate\": \"1.58\",\r\n            \"shnu_cntg_csnu\": \"29381\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"5백 이하\",\r\n            \"smtn_avrg_prpr\": \"78317\",\r\n            \"acml_vol\": \"138138\",\r\n            \"whol_ntby_qty_rate\": \"-0.13\",\r\n            \"ntby_cntg_csnu\": \"-278\",\r\n            \"seln_cnqn_smtn\": \"75634\",\r\n            \"whol_seln_vol_rate\": \"0.73\",\r\n            \"seln_cntg_csnu\": \"1525\",\r\n            \"shnu_cnqn_smtn\": \"62504\",\r\n            \"whol_shun_vol_rate\": \"0.60\",\r\n            \"shnu_cntg_csnu\": \"1247\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"1천 이하\",\r\n            \"smtn_avrg_prpr\": \"78304\",\r\n            \"acml_vol\": \"378958\",\r\n            \"whol_ntby_qty_rate\": \"0.10\",\r\n            \"ntby_cntg_csnu\": \"110\",\r\n            \"seln_cnqn_smtn\": \"184499\",\r\n            \"whol_seln_vol_rate\": \"1.77\",\r\n            \"seln_cntg_csnu\": \"2000\",\r\n            \"shnu_cnqn_smtn\": \"194459\",\r\n            \"whol_shun_vol_rate\": \"1.87\",\r\n            \"shnu_cntg_csnu\": \"2110\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"3천 이하\",\r\n            \"smtn_avrg_prpr\": \"78328\",\r\n            \"acml_vol\": \"720672\",\r\n            \"whol_ntby_qty_rate\": \"-0.51\",\r\n            \"ntby_cntg_csnu\": \"-330\",\r\n            \"seln_cnqn_smtn\": \"387086\",\r\n            \"whol_seln_vol_rate\": \"3.72\",\r\n            \"seln_cntg_csnu\": \"1993\",\r\n            \"shnu_cnqn_smtn\": \"333586\",\r\n            \"whol_shun_vol_rate\": \"3.20\",\r\n            \"shnu_cntg_csnu\": \"1663\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"5천 이하\",\r\n            \"smtn_avrg_prpr\": \"78349\",\r\n            \"acml_vol\": \"429911\",\r\n            \"whol_ntby_qty_rate\": \"0.16\",\r\n            \"ntby_cntg_csnu\": \"63\",\r\n            \"seln_cnqn_smtn\": \"206855\",\r\n            \"whol_seln_vol_rate\": \"1.99\",\r\n            \"seln_cntg_csnu\": \"426\",\r\n            \"shnu_cnqn_smtn\": \"223056\",\r\n            \"whol_shun_vol_rate\": \"2.14\",\r\n            \"shnu_cntg_csnu\": \"489\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"1억 이하\",\r\n            \"smtn_avrg_prpr\": \"78336\",\r\n            \"acml_vol\": \"580130\",\r\n            \"whol_ntby_qty_rate\": \"-1.24\",\r\n            \"ntby_cntg_csnu\": \"-153\",\r\n            \"seln_cnqn_smtn\": \"354585\",\r\n            \"whol_seln_vol_rate\": \"3.40\",\r\n            \"seln_cntg_csnu\": \"402\",\r\n            \"shnu_cnqn_smtn\": \"225545\",\r\n            \"whol_shun_vol_rate\": \"2.17\",\r\n            \"shnu_cntg_csnu\": \"249\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"5억 이하\",\r\n            \"smtn_avrg_prpr\": \"78326\",\r\n            \"acml_vol\": \"1664623\",\r\n            \"whol_ntby_qty_rate\": \"-1.57\",\r\n            \"ntby_cntg_csnu\": \"-61\",\r\n            \"seln_cnqn_smtn\": \"914220\",\r\n            \"whol_seln_vol_rate\": \"8.78\",\r\n            \"seln_cntg_csnu\": \"306\",\r\n            \"shnu_cnqn_smtn\": \"750403\",\r\n            \"whol_shun_vol_rate\": \"7.21\",\r\n            \"shnu_cntg_csnu\": \"245\"\r\n        },\r\n        {\r\n            \"prpr_name\": \"5억 초과\",\r\n            \"smtn_avrg_prpr\": \"78316\",\r\n            \"acml_vol\": \"6210233\",\r\n            \"whol_ntby_qty_rate\": \"-18.01\",\r\n            \"ntby_cntg_csnu\": \"-55\",\r\n            \"seln_cnqn_smtn\": \"4042917\",\r\n            \"whol_seln_vol_rate\": \"38.82\",\r\n            \"seln_cntg_csnu\": \"173\",\r\n            \"shnu_cnqn_smtn\": \"2167316\",\r\n            \"whol_shun_vol_rate\": \"20.81\",\r\n            \"shnu_cntg_csnu\": \"118\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "HHPPG046600C1",
    "name": "프로그램매매 투자자매매동향(당일)",
    "url": "/uapi/domestic-stock/v1/quotations/investor-program-trade-today",
    "sheet": "프로그램매매 투자자매매동향(당일)",
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
        "element": "invr_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "all_seln_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "all_seln_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "invr_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "all_shnu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "all_shnu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "all_ntby_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_seln_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "all_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_shnu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_seln_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_shnu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "arbt_ntby_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_seln_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_shnu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_seln_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_shnu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nabt_ntby_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "MRKT_DIV_CLS_CODE:1",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": [\r\n        {\r\n            \"invr_cls_code\": \"7100\",\r\n            \"invr_cls_name\": \"기 타\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"289\",\r\n            \"nabt_shnu_qty\": \"242\",\r\n            \"nabt_ntby_qty\": \"-47\",\r\n            \"nabt_seln_amt\": \"7151\",\r\n            \"nabt_shnu_amt\": \"4006\",\r\n            \"nabt_ntby_amt\": \"-3145\",\r\n            \"all_seln_qty\": \"289\",\r\n            \"all_shnu_qty\": \"242\",\r\n            \"all_ntby_qty\": \"-47\",\r\n            \"all_seln_amt\": \"7151\",\r\n            \"all_shnu_amt\": \"4006\",\r\n            \"all_ntby_amt\": \"-3145\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"6000\",\r\n            \"invr_cls_name\": \"연기금등\",\r\n            \"arbt_seln_qty\": \"440\",\r\n            \"arbt_shnu_qty\": \"410\",\r\n            \"arbt_ntby_qty\": \"-29\",\r\n            \"arbt_seln_amt\": \"27863\",\r\n            \"arbt_shnu_amt\": \"25971\",\r\n            \"arbt_ntby_amt\": \"-1891\",\r\n            \"nabt_seln_qty\": \"608\",\r\n            \"nabt_shnu_qty\": \"474\",\r\n            \"nabt_ntby_qty\": \"-134\",\r\n            \"nabt_seln_amt\": \"16795\",\r\n            \"nabt_shnu_amt\": \"23282\",\r\n            \"nabt_ntby_amt\": \"6486\",\r\n            \"all_seln_qty\": \"1049\",\r\n            \"all_shnu_qty\": \"885\",\r\n            \"all_ntby_qty\": \"-164\",\r\n            \"all_seln_amt\": \"44658\",\r\n            \"all_shnu_amt\": \"49253\",\r\n            \"all_ntby_amt\": \"4595\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"5000\",\r\n            \"invr_cls_name\": \"기타금융\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"0\",\r\n            \"nabt_shnu_qty\": \"0\",\r\n            \"nabt_ntby_qty\": \"0\",\r\n            \"nabt_seln_amt\": \"0\",\r\n            \"nabt_shnu_amt\": \"20\",\r\n            \"nabt_ntby_amt\": \"20\",\r\n            \"all_seln_qty\": \"0\",\r\n            \"all_shnu_qty\": \"0\",\r\n            \"all_ntby_qty\": \"0\",\r\n            \"all_seln_amt\": \"0\",\r\n            \"all_shnu_amt\": \"20\",\r\n            \"all_ntby_amt\": \"20\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"2000\",\r\n            \"invr_cls_name\": \"보 험\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"211\",\r\n            \"nabt_shnu_qty\": \"110\",\r\n            \"nabt_ntby_qty\": \"-101\",\r\n            \"nabt_seln_amt\": \"12580\",\r\n            \"nabt_shnu_amt\": \"6296\",\r\n            \"nabt_ntby_amt\": \"-6283\",\r\n            \"all_seln_qty\": \"211\",\r\n            \"all_shnu_qty\": \"110\",\r\n            \"all_ntby_qty\": \"-101\",\r\n            \"all_seln_amt\": \"12580\",\r\n            \"all_shnu_amt\": \"6296\",\r\n            \"all_ntby_amt\": \"-6283\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"4000\",\r\n            \"invr_cls_name\": \"은 행\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"28\",\r\n            \"nabt_shnu_qty\": \"65\",\r\n            \"nabt_ntby_qty\": \"36\",\r\n            \"nabt_seln_amt\": \"563\",\r\n            \"nabt_shnu_amt\": \"851\",\r\n            \"nabt_ntby_amt\": \"288\",\r\n            \"all_seln_qty\": \"28\",\r\n            \"all_shnu_qty\": \"65\",\r\n            \"all_ntby_qty\": \"36\",\r\n            \"all_seln_amt\": \"563\",\r\n            \"all_shnu_amt\": \"851\",\r\n            \"all_ntby_amt\": \"288\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"3100\",\r\n            \"invr_cls_name\": \"사 모\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"303\",\r\n            \"nabt_shnu_qty\": \"181\",\r\n            \"nabt_ntby_qty\": \"-121\",\r\n            \"nabt_seln_amt\": \"12440\",\r\n            \"nabt_shnu_amt\": \"8092\",\r\n            \"nabt_ntby_amt\": \"-4348\",\r\n            \"all_seln_qty\": \"303\",\r\n            \"all_shnu_qty\": \"181\",\r\n            \"all_ntby_qty\": \"-121\",\r\n            \"all_seln_amt\": \"12440\",\r\n            \"all_shnu_amt\": \"8092\",\r\n            \"all_ntby_amt\": \"-4348\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"3000\",\r\n            \"invr_cls_name\": \"투 신\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"764\",\r\n            \"nabt_shnu_qty\": \"806\",\r\n            \"nabt_ntby_qty\": \"41\",\r\n            \"nabt_seln_amt\": \"41009\",\r\n            \"nabt_shnu_amt\": \"38826\",\r\n            \"nabt_ntby_amt\": \"-2183\",\r\n            \"all_seln_qty\": \"764\",\r\n            \"all_shnu_qty\": \"806\",\r\n            \"all_ntby_qty\": \"41\",\r\n            \"all_seln_amt\": \"41009\",\r\n            \"all_shnu_amt\": \"38826\",\r\n            \"all_ntby_amt\": \"-2183\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"1000\",\r\n            \"invr_cls_name\": \"금융투자\",\r\n            \"arbt_seln_qty\": \"445\",\r\n            \"arbt_shnu_qty\": \"2\",\r\n            \"arbt_ntby_qty\": \"-443\",\r\n            \"arbt_seln_amt\": \"28429\",\r\n            \"arbt_shnu_amt\": \"143\",\r\n            \"arbt_ntby_amt\": \"-28285\",\r\n            \"nabt_seln_qty\": \"98\",\r\n            \"nabt_shnu_qty\": \"70\",\r\n            \"nabt_ntby_qty\": \"-27\",\r\n            \"nabt_seln_amt\": \"5176\",\r\n            \"nabt_shnu_amt\": \"6003\",\r\n            \"nabt_ntby_amt\": \"826\",\r\n            \"all_seln_qty\": \"543\",\r\n            \"all_shnu_qty\": \"72\",\r\n            \"all_ntby_qty\": \"-470\",\r\n            \"all_seln_amt\": \"33605\",\r\n            \"all_shnu_amt\": \"6146\",\r\n            \"all_ntby_amt\": \"-27459\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"8888\",\r\n            \"invr_cls_name\": \"기 관\",\r\n            \"arbt_seln_qty\": \"885\",\r\n            \"arbt_shnu_qty\": \"413\",\r\n            \"arbt_ntby_qty\": \"-472\",\r\n            \"arbt_seln_amt\": \"56292\",\r\n            \"arbt_shnu_amt\": \"26114\",\r\n            \"arbt_ntby_amt\": \"-30177\",\r\n            \"nabt_seln_qty\": \"2014\",\r\n            \"nabt_shnu_qty\": \"1709\",\r\n            \"nabt_ntby_qty\": \"-305\",\r\n            \"nabt_seln_amt\": \"88565\",\r\n            \"nabt_shnu_amt\": \"83373\",\r\n            \"nabt_ntby_amt\": \"-5192\",\r\n            \"all_seln_qty\": \"2900\",\r\n            \"all_shnu_qty\": \"2122\",\r\n            \"all_ntby_qty\": \"-778\",\r\n            \"all_seln_amt\": \"144858\",\r\n            \"all_shnu_amt\": \"109487\",\r\n            \"all_ntby_amt\": \"-35370\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"8000\",\r\n            \"invr_cls_name\": \"개 인\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"0\",\r\n            \"arbt_ntby_qty\": \"0\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"0\",\r\n            \"arbt_ntby_amt\": \"0\",\r\n            \"nabt_seln_qty\": \"683\",\r\n            \"nabt_shnu_qty\": \"528\",\r\n            \"nabt_ntby_qty\": \"-154\",\r\n            \"nabt_seln_amt\": \"16867\",\r\n            \"nabt_shnu_amt\": \"9496\",\r\n            \"nabt_ntby_amt\": \"-7371\",\r\n            \"all_seln_qty\": \"683\",\r\n            \"all_shnu_qty\": \"528\",\r\n            \"all_ntby_qty\": \"-154\",\r\n            \"all_seln_amt\": \"16867\",\r\n            \"all_shnu_amt\": \"9496\",\r\n            \"all_ntby_amt\": \"-7371\"\r\n        },\r\n        {\r\n            \"invr_cls_code\": \"9100\",\r\n            \"invr_cls_name\": \"외국인\",\r\n            \"arbt_seln_qty\": \"0\",\r\n            \"arbt_shnu_qty\": \"57\",\r\n            \"arbt_ntby_qty\": \"57\",\r\n            \"arbt_seln_amt\": \"0\",\r\n            \"arbt_shnu_amt\": \"4321\",\r\n            \"arbt_ntby_amt\": \"4321\",\r\n            \"nabt_seln_qty\": \"88573\",\r\n            \"nabt_shnu_qty\": \"73539\",\r\n            \"nabt_ntby_qty\": \"-15034\",\r\n            \"nabt_seln_amt\": \"2640145\",\r\n            \"nabt_shnu_amt\": \"1983063\",\r\n            \"nabt_ntby_amt\": \"-657082\",\r\n            \"all_seln_qty\": \"88573\",\r\n            \"all_shnu_qty\": \"73596\",\r\n            \"all_ntby_qty\": \"-14976\",\r\n            \"all_seln_amt\": \"2640145\",\r\n            \"all_shnu_amt\": \"1987384\",\r\n            \"all_ntby_amt\": \"-652761\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST649100C0",
    "name": "국내 증시자금 종합",
    "url": "/uapi/domestic-stock/v1/quotations/mktfunds",
    "sheet": "국내 증시자금 종합",
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
        "element": "bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bstp_nmix_prpr",
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
        "element": "prdy_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": "1. 상한 2. 상승 3. 보합 4. 하한 5. 하락"
      },
      {
        "element": "prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hts_avls",
        "type": "string",
        "required": "Y",
        "description": "단위: 백만원"
      },
      {
        "element": "cust_dpmn_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "cust_dpmn_amt_prdy_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "amt_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "uncl_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "crdt_loan_rmnd",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "futs_tfam_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "sttp_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "mxtp_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "bntp_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "mmf_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "secu_lend_amt",
        "type": "string",
        "required": "Y",
        "description": "단위: 억원"
      },
      {
        "element": "FID_INPUT_DATE_1:20240503",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"bsop_date\": \"20240430\",\r\n            \"bstp_nmix_prpr\": \"2692.06\",\r\n            \"bstp_nmix_prdy_vrss\": \"4.62\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"100.17\",\r\n            \"hts_avls\": \"2193843858\",\r\n            \"cust_dpmn_amt\": \"572306\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"4435\",\r\n            \"amt_tnrt\": \"33.87\",\r\n            \"uncl_amt\": \"9289\",\r\n            \"crdt_loan_rmnd\": \"191730\",\r\n            \"futs_tfam_amt\": \"112724\",\r\n            \"sttp_amt\": \"1112330\",\r\n            \"mxtp_amt\": \"264052\",\r\n            \"bntp_amt\": \"1497053\",\r\n            \"mmf_amt\": \"1971372\",\r\n            \"secu_lend_amt\": \"199663\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240429\",\r\n            \"bstp_nmix_prpr\": \"2687.44\",\r\n            \"bstp_nmix_prdy_vrss\": \"31.11\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"101.17\",\r\n            \"hts_avls\": \"2189691726\",\r\n            \"cust_dpmn_amt\": \"567872\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"2770\",\r\n            \"amt_tnrt\": \"31.81\",\r\n            \"uncl_amt\": \"9770\",\r\n            \"crdt_loan_rmnd\": \"191876\",\r\n            \"futs_tfam_amt\": \"114477\",\r\n            \"sttp_amt\": \"1108725\",\r\n            \"mxtp_amt\": \"264014\",\r\n            \"bntp_amt\": \"1490082\",\r\n            \"mmf_amt\": \"1995789\",\r\n            \"secu_lend_amt\": \"205197\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240426\",\r\n            \"bstp_nmix_prpr\": \"2656.33\",\r\n            \"bstp_nmix_prdy_vrss\": \"27.71\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"101.05\",\r\n            \"hts_avls\": \"2164477451\",\r\n            \"cust_dpmn_amt\": \"565102\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"8389\",\r\n            \"amt_tnrt\": \"32.27\",\r\n            \"uncl_amt\": \"9224\",\r\n            \"crdt_loan_rmnd\": \"190610\",\r\n            \"futs_tfam_amt\": \"114228\",\r\n            \"sttp_amt\": \"1099696\",\r\n            \"mxtp_amt\": \"263514\",\r\n            \"bntp_amt\": \"1486148\",\r\n            \"mmf_amt\": \"2014269\",\r\n            \"secu_lend_amt\": \"200841\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240425\",\r\n            \"bstp_nmix_prpr\": \"2628.62\",\r\n            \"bstp_nmix_prdy_vrss\": \"-47.13\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"98.24\",\r\n            \"hts_avls\": \"2142440795\",\r\n            \"cust_dpmn_amt\": \"556713\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"9753\",\r\n            \"amt_tnrt\": \"30.55\",\r\n            \"uncl_amt\": \"9460\",\r\n            \"crdt_loan_rmnd\": \"190653\",\r\n            \"futs_tfam_amt\": \"119102\",\r\n            \"sttp_amt\": \"1091640\",\r\n            \"mxtp_amt\": \"263032\",\r\n            \"bntp_amt\": \"1486119\",\r\n            \"mmf_amt\": \"2034032\",\r\n            \"secu_lend_amt\": \"197721\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240424\",\r\n            \"bstp_nmix_prpr\": \"2675.75\",\r\n            \"bstp_nmix_prdy_vrss\": \"52.73\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"102.01\",\r\n            \"hts_avls\": \"2180629130\",\r\n            \"cust_dpmn_amt\": \"546960\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"-11693\",\r\n            \"amt_tnrt\": \"33.20\",\r\n            \"uncl_amt\": \"9503\",\r\n            \"crdt_loan_rmnd\": \"189912\",\r\n            \"futs_tfam_amt\": \"118058\",\r\n            \"sttp_amt\": \"1095621\",\r\n            \"mxtp_amt\": \"262947\",\r\n            \"bntp_amt\": \"1484163\",\r\n            \"mmf_amt\": \"2055945\",\r\n            \"secu_lend_amt\": \"199263\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240423\",\r\n            \"bstp_nmix_prpr\": \"2623.02\",\r\n            \"bstp_nmix_prdy_vrss\": \"-6.42\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"99.76\",\r\n            \"hts_avls\": \"2137640963\",\r\n            \"cust_dpmn_amt\": \"558653\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"-7143\",\r\n            \"amt_tnrt\": \"31.04\",\r\n            \"uncl_amt\": \"9454\",\r\n            \"crdt_loan_rmnd\": \"190361\",\r\n            \"futs_tfam_amt\": \"117715\",\r\n            \"sttp_amt\": \"1083125\",\r\n            \"mxtp_amt\": \"262801\",\r\n            \"bntp_amt\": \"1481191\",\r\n            \"mmf_amt\": \"2059132\",\r\n            \"secu_lend_amt\": \"198055\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240422\",\r\n            \"bstp_nmix_prpr\": \"2629.44\",\r\n            \"bstp_nmix_prdy_vrss\": \"37.58\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"101.45\",\r\n            \"hts_avls\": \"2143157216\",\r\n            \"cust_dpmn_amt\": \"565797\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"11043\",\r\n            \"amt_tnrt\": \"33.64\",\r\n            \"uncl_amt\": \"9312\",\r\n            \"crdt_loan_rmnd\": \"190326\",\r\n            \"futs_tfam_amt\": \"118954\",\r\n            \"sttp_amt\": \"1085224\",\r\n            \"mxtp_amt\": \"262713\",\r\n            \"bntp_amt\": \"1477973\",\r\n            \"mmf_amt\": \"2083552\",\r\n            \"secu_lend_amt\": \"197038\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240419\",\r\n            \"bstp_nmix_prpr\": \"2591.86\",\r\n            \"bstp_nmix_prdy_vrss\": \"-42.84\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"98.37\",\r\n            \"hts_avls\": \"2113960518\",\r\n            \"cust_dpmn_amt\": \"554754\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"4154\",\r\n            \"amt_tnrt\": \"41.58\",\r\n            \"uncl_amt\": \"9806\",\r\n            \"crdt_loan_rmnd\": \"190624\",\r\n            \"futs_tfam_amt\": \"119487\",\r\n            \"sttp_amt\": \"1083386\",\r\n            \"mxtp_amt\": \"262645\",\r\n            \"bntp_amt\": \"1475873\",\r\n            \"mmf_amt\": \"2087866\",\r\n            \"secu_lend_amt\": \"198926\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240418\",\r\n            \"bstp_nmix_prpr\": \"2634.70\",\r\n            \"bstp_nmix_prdy_vrss\": \"50.52\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"101.95\",\r\n            \"hts_avls\": \"2148591607\",\r\n            \"cust_dpmn_amt\": \"550600\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"-2090\",\r\n            \"amt_tnrt\": \"33.32\",\r\n            \"uncl_amt\": \"9932\",\r\n            \"crdt_loan_rmnd\": \"191816\",\r\n            \"futs_tfam_amt\": \"115974\",\r\n            \"sttp_amt\": \"1088431\",\r\n            \"mxtp_amt\": \"261979\",\r\n            \"bntp_amt\": \"1472540\",\r\n            \"mmf_amt\": \"2096220\",\r\n            \"secu_lend_amt\": \"199652\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240417\",\r\n            \"bstp_nmix_prpr\": \"2584.18\",\r\n            \"bstp_nmix_prdy_vrss\": \"-25.45\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"99.02\",\r\n            \"hts_avls\": \"2108636206\",\r\n            \"cust_dpmn_amt\": \"552690\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"-23278\",\r\n            \"amt_tnrt\": \"32.09\",\r\n            \"uncl_amt\": \"9653\",\r\n            \"crdt_loan_rmnd\": \"194102\",\r\n            \"futs_tfam_amt\": \"114956\",\r\n            \"sttp_amt\": \"1086475\",\r\n            \"mxtp_amt\": \"261671\",\r\n            \"bntp_amt\": \"1472499\",\r\n            \"mmf_amt\": \"2109537\",\r\n            \"secu_lend_amt\": \"198961\"\r\n        },\r\n        {\r\n            \"bsop_date\": \"20240416\",\r\n            \"bstp_nmix_prpr\": \"2609.63\",\r\n            \"bstp_nmix_prdy_vrss\": \"-60.80\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"97.72\",\r\n            \"hts_avls\": \"2129095534\",\r\n            \"cust_dpmn_amt\": \"575969\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"9287\",\r\n            \"amt_tnrt\": \"35.91\",\r\n            \"uncl_amt\": \"9583\",\r\n            \"crdt_loan_rmnd\": \"193485\",\r\n            \"futs_tfam_amt\": \"116520\",\r\n            \"sttp_amt\": \"1092931\",\r\n            \"mxtp_amt\": \"261632\",\r\n            \"bntp_amt\": \"1471604\",\r\n            \"mmf_amt\": \"2083522\",\r\n            \"secu_lend_amt\": \"198067\"\r\n        },...\r\n        {\r\n            \"bsop_date\": \"20231204\",\r\n            \"bstp_nmix_prpr\": \"2514.95\",\r\n            \"bstp_nmix_prdy_vrss\": \"9.94\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"100.40\",\r\n            \"hts_avls\": \"2012605764\",\r\n            \"cust_dpmn_amt\": \"483930\",\r\n            \"cust_dpmn_amt_prdy_vrss\": \"-2751\",\r\n            \"amt_tnrt\": \"39.82\",\r\n            \"uncl_amt\": \"9477\",\r\n            \"crdt_loan_rmnd\": \"172738\",\r\n            \"futs_tfam_amt\": \"111758\",\r\n            \"sttp_amt\": \"1020141\",\r\n            \"mxtp_amt\": \"241287\",\r\n            \"bntp_amt\": \"1372663\",\r\n            \"mmf_amt\": \"1937326\",\r\n            \"secu_lend_amt\": \"212773\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01810000",
    "name": "국내주식 예상체결가 추이",
    "url": "/uapi/domestic-stock/v1/quotations/exp-price-trend",
    "sheet": "국내주식 예상체결가 추이",
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
        "element": "rprs_mrkt_kor_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cnpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cntg_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cntg_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_cntg_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "antc_tr_pbmn",
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
        "element": "stck_bsop_date",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cntg_hour",
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
        "element": "{\r\n\"fid_cond_mrkt_div_code\":\"J\",\r\n\"fid_input_iscd\":\"005930\",\r\n\"fid_mkop_cls_code\":\"0\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": {\r\n        \"rprs_mrkt_kor_name\": \"KOSPI200\",\r\n        \"antc_cnpr\": \"72600\",\r\n        \"antc_cntg_vrss_sign\": \"2\",\r\n        \"antc_cntg_vrss\": \"300\",\r\n        \"antc_cntg_prdy_ctrt\": \"0.41\",\r\n        \"antc_vol\": \"420303\",\r\n        \"antc_tr_pbmn\": \"30513997800\"\r\n    },\r\n    \"output2\": [\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090023\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"420303\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090023\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"420196\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090023\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"420206\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090023\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"419330\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090022\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"419131\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090022\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418134\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090022\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418123\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090021\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418123\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090020\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418123\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090019\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418123\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090019\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418120\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090018\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418120\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090017\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418120\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090017\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418121\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090016\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418121\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090016\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"418003\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090016\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"417953\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090016\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"417729\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090016\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"417679\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090015\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"417679\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090015\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"417060\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090015\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"417050\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090015\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"416945\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090015\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"416921\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090015\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"416915\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090014\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"416915\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090014\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"416770\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090014\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"416759\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090014\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"415059\"\r\n        },\r\n        {\r\n            \"stck_bsop_date\": \"20240318\",\r\n            \"stck_cntg_hour\": \"090013\",\r\n            \"stck_prpr\": \"72600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.41\",\r\n            \"acml_vol\": \"414942\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST04320000",
    "name": "회원사 실시간 매매동향(틱)",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-trade-trend",
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
      },
      {
        "element": "FID_COND_SCR_DIV_CODE:20432\r\nFID_INPUT_ISCD:005930\r\nFID_INPUT_ISCD2:99999\r\nFID_MRKT_CLS_CODE:\r\nFID_VOL_CNT:",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output1\": [\r\n        {\r\n            \"total_seln_qty\": \"3403046\",\r\n            \"total_shnu_qty\": \"1539165\"\r\n        }\r\n    ],\r\n    \"output2\": [\r\n        {\r\n            \"bsop_hour\": \"153025\",\r\n            \"mbcr_name\": \"JP모간\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"stck_prpr\": \"75200\",\r\n            \"prdy_vrss\": \"-500\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"cntg_vol\": \"168484\",\r\n            \"acml_ntby_qty\": \"1473742\",\r\n            \"glob_ntby_qty\": \"-1863881\",\r\n            \"frgn_ntby_qty_icdc\": \"168484\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"153025\",\r\n            \"mbcr_name\": \"메릴린치\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"stck_prpr\": \"75200\",\r\n            \"prdy_vrss\": \"-500\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"cntg_vol\": \"-188645\",\r\n            \"acml_ntby_qty\": \"-938293\",\r\n            \"glob_ntby_qty\": \"-2032365\",\r\n            \"frgn_ntby_qty_icdc\": \"-188645\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"153025\",\r\n            \"mbcr_name\": \"씨티그룹\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"stck_prpr\": \"75200\",\r\n            \"prdy_vrss\": \"-500\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"cntg_vol\": \"-135506\",\r\n            \"acml_ntby_qty\": \"-2308688\",\r\n            \"glob_ntby_qty\": \"-1843720\",\r\n            \"frgn_ntby_qty_icdc\": \"-135506\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"152020\",\r\n            \"mbcr_name\": \"JP모간\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"stck_prpr\": \"75500\",\r\n            \"prdy_vrss\": \"-200\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"cntg_vol\": \"139\",\r\n            \"acml_ntby_qty\": \"1305258\",\r\n            \"glob_ntby_qty\": \"-1708214\",\r\n            \"frgn_ntby_qty_icdc\": \"139\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151904\",\r\n            \"mbcr_name\": \"JP모간\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"stck_prpr\": \"75400\",\r\n            \"prdy_vrss\": \"-300\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"cntg_vol\": \"2271\",\r\n            \"acml_ntby_qty\": \"1305119\",\r\n            \"glob_ntby_qty\": \"-1708353\",\r\n            \"frgn_ntby_qty_icdc\": \"2271\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151749\",\r\n            \"mbcr_name\": \"JP모간\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"stck_prpr\": \"75300\",\r\n            \"prdy_vrss\": \"-400\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"cntg_vol\": \"23867\",\r\n            \"acml_ntby_qty\": \"1302848\",\r\n            \"glob_ntby_qty\": \"-1710624\",\r\n            \"frgn_ntby_qty_icdc\": \"23867\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPTJ04030000",
    "name": "시장별 투자자매매동향(시세)",
    "url": "/uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market",
    "sheet": "시장별 투자자매매동향(시세)",
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
        "element": "frgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scrt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ivtr_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pe_fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bank_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "insu_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrbn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_orgt_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etc_corp_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "{\r\n\"FID_INPUT_ISCD\":\"KSP\",\r\n\"FID_INPUT_ISCD_2\":\"0001\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"frgn_seln_vol\": \"75588\",\r\n            \"frgn_shnu_vol\": \"70298\",\r\n            \"frgn_ntby_qty\": \"-5290\",\r\n            \"frgn_seln_tr_pbmn\": \"2818983\",\r\n            \"frgn_shnu_tr_pbmn\": \"2967639\",\r\n            \"frgn_ntby_tr_pbmn\": \"148656\",\r\n            \"prsn_seln_vol\": \"294375\",\r\n            \"prsn_shnu_vol\": \"300449\",\r\n            \"prsn_ntby_qty\": \"6074\",\r\n            \"prsn_seln_tr_pbmn\": \"5131230\",\r\n            \"prsn_shnu_tr_pbmn\": \"5020361\",\r\n            \"prsn_ntby_tr_pbmn\": \"-110869\",\r\n            \"orgn_seln_vol\": \"36911\",\r\n            \"orgn_shnu_vol\": \"37631\",\r\n            \"orgn_ntby_qty\": \"720\",\r\n            \"orgn_seln_tr_pbmn\": \"2110371\",\r\n            \"orgn_shnu_tr_pbmn\": \"2054839\",\r\n            \"orgn_ntby_tr_pbmn\": \"-55532\",\r\n            \"scrt_seln_vol\": \"8493\",\r\n            \"scrt_shnu_vol\": \"12126\",\r\n            \"scrt_ntby_qty\": \"3633\",\r\n            \"scrt_seln_tr_pbmn\": \"384357\",\r\n            \"scrt_shnu_tr_pbmn\": \"472598\",\r\n            \"scrt_ntby_tr_pbmn\": \"88241\",\r\n            \"ivtr_seln_vol\": \"4086\",\r\n            \"ivtr_shnu_vol\": \"3964\",\r\n            \"ivtr_ntby_qty\": \"-122\",\r\n            \"ivtr_seln_tr_pbmn\": \"177374\",\r\n            \"ivtr_shnu_tr_pbmn\": \"165434\",\r\n            \"ivtr_ntby_tr_pbmn\": \"-11940\",\r\n            \"pe_fund_seln_tr_pbmn\": \"213413\",\r\n            \"pe_fund_seln_vol\": \"4833\",\r\n            \"pe_fund_ntby_vol\": \"-1804\",\r\n            \"pe_fund_shnu_tr_pbmn\": \"115551\",\r\n            \"pe_fund_shnu_vol\": \"3029\",\r\n            \"pe_fund_ntby_tr_pbmn\": \"-97861\",\r\n            \"bank_seln_vol\": \"245\",\r\n            \"bank_shnu_vol\": \"51\",\r\n            \"bank_ntby_qty\": \"-193\",\r\n            \"bank_seln_tr_pbmn\": \"13382\",\r\n            \"bank_shnu_tr_pbmn\": \"2873\",\r\n            \"bank_ntby_tr_pbmn\": \"-10509\",\r\n            \"insu_seln_vol\": \"1653\",\r\n            \"insu_shnu_vol\": \"1050\",\r\n            \"insu_ntby_qty\": \"-603\",\r\n            \"insu_seln_tr_pbmn\": \"79782\",\r\n            \"insu_shnu_tr_pbmn\": \"50378\",\r\n            \"insu_ntby_tr_pbmn\": \"-29404\",\r\n            \"mrbn_seln_vol\": \"230\",\r\n            \"mrbn_shnu_vol\": \"310\",\r\n            \"mrbn_ntby_qty\": \"80\",\r\n            \"mrbn_seln_tr_pbmn\": \"10393\",\r\n            \"mrbn_shnu_tr_pbmn\": \"11896\",\r\n            \"mrbn_ntby_tr_pbmn\": \"1502\",\r\n            \"fund_seln_vol\": \"17372\",\r\n            \"fund_shnu_vol\": \"17101\",\r\n            \"fund_ntby_qty\": \"-271\",\r\n            \"fund_seln_tr_pbmn\": \"1231671\",\r\n            \"fund_shnu_tr_pbmn\": \"1236109\",\r\n            \"fund_ntby_tr_pbmn\": \"4439\",\r\n            \"etc_orgt_seln_vol\": \"0\",\r\n            \"etc_orgt_shnu_vol\": \"0\",\r\n            \"etc_orgt_ntby_vol\": \"0\",\r\n            \"etc_orgt_seln_tr_pbmn\": \"0\",\r\n            \"etc_orgt_shnu_tr_pbmn\": \"0\",\r\n            \"etc_orgt_ntby_tr_pbmn\": \"0\",\r\n            \"etc_corp_seln_vol\": \"5061\",\r\n            \"etc_corp_shnu_vol\": \"3558\",\r\n            \"etc_corp_ntby_vol\": \"-1503\",\r\n            \"etc_corp_seln_tr_pbmn\": \"95856\",\r\n            \"etc_corp_shnu_tr_pbmn\": \"113601\",\r\n            \"etc_corp_ntby_tr_pbmn\": \"17745\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPPG04650101",
    "name": "종목별 프로그램매매추이(체결)",
    "url": "/uapi/domestic-stock/v1/quotations/program-trade-by-stock",
    "sheet": "종목별 프로그램매매추이(체결)",
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
        "element": "bsop_hour",
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
        "element": "whol_smtn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_shnu_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_ntby_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_seln_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_shnu_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_smtn_ntby_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_ntby_vol_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_ntby_tr_pbmn_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST644100C0",
    "name": "외국계 매매종목 가집계",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-trade-estimate",
    "sheet": "외국계 매매종목 가집계",
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
        "element": "hts_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_ntsl_qty",
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
        "element": "glob_total_seln_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "glob_total_shnu_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE:J\r\nFID_COND_SCR_DIV_CODE:16441\r\nFID_INPUT_ISCD:0000\r\nFID_RANK_SORT_CLS_CODE:0\r\nFID_RANK_SORT_CLS_CODE_2:0",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"stck_shrn_iscd\": \"005930\",\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"glob_ntsl_qty\": \"3870530\",\r\n            \"stck_prpr\": \"81300\",\r\n            \"prdy_vrss\": \"3700\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.77\",\r\n            \"acml_vol\": \"24892595\",\r\n            \"glob_total_seln_qty\": \"547879\",\r\n            \"glob_total_shnu_qty\": \"4418409\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"000660\",\r\n            \"hts_kor_isnm\": \"SK하이닉스\",\r\n            \"glob_ntsl_qty\": \"964256\",\r\n            \"stck_prpr\": \"179600\",\r\n            \"prdy_vrss\": \"6400\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.70\",\r\n            \"acml_vol\": \"4333233\",\r\n            \"glob_total_seln_qty\": \"680043\",\r\n            \"glob_total_shnu_qty\": \"1644299\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"267260\",\r\n            \"hts_kor_isnm\": \"HD현대일렉트릭\",\r\n            \"glob_ntsl_qty\": \"329507\",\r\n            \"stck_prpr\": \"252000\",\r\n            \"prdy_vrss\": \"22000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"9.57\",\r\n            \"acml_vol\": \"955597\",\r\n            \"glob_total_seln_qty\": \"87986\",\r\n            \"glob_total_shnu_qty\": \"417493\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"005935\",\r\n            \"hts_kor_isnm\": \"삼성전자우\",\r\n            \"glob_ntsl_qty\": \"455400\",\r\n            \"stck_prpr\": \"66900\",\r\n            \"prdy_vrss\": \"2300\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.56\",\r\n            \"acml_vol\": \"1554888\",\r\n            \"glob_total_seln_qty\": \"211634\",\r\n            \"glob_total_shnu_qty\": \"667034\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"011070\",\r\n            \"hts_kor_isnm\": \"LG이노텍\",\r\n            \"glob_ntsl_qty\": \"79842\",\r\n            \"stck_prpr\": \"239500\",\r\n            \"prdy_vrss\": \"5000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"2.13\",\r\n            \"acml_vol\": \"283787\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"79842\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"012450\",\r\n            \"hts_kor_isnm\": \"한화에어로스페이스\",\r\n            \"glob_ntsl_qty\": \"56853\",\r\n            \"stck_prpr\": \"218500\",\r\n            \"prdy_vrss\": \"3000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"1.39\",\r\n            \"acml_vol\": \"334636\",\r\n            \"glob_total_seln_qty\": \"15218\",\r\n            \"glob_total_shnu_qty\": \"72071\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"010140\",\r\n            \"hts_kor_isnm\": \"삼성중공업\",\r\n            \"glob_ntsl_qty\": \"1230023\",\r\n            \"stck_prpr\": \"9600\",\r\n            \"prdy_vrss\": \"210\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"2.24\",\r\n            \"acml_vol\": \"7158181\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"1230023\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"009150\",\r\n            \"hts_kor_isnm\": \"삼성전기\",\r\n            \"glob_ntsl_qty\": \"73431\",\r\n            \"stck_prpr\": \"158000\",\r\n            \"prdy_vrss\": \"6900\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.57\",\r\n            \"acml_vol\": \"551401\",\r\n            \"glob_total_seln_qty\": \"3452\",\r\n            \"glob_total_shnu_qty\": \"76883\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"316140\",\r\n            \"hts_kor_isnm\": \"우리금융지주\",\r\n            \"glob_ntsl_qty\": \"605764\",\r\n            \"stck_prpr\": \"14190\",\r\n            \"prdy_vrss\": \"60\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.42\",\r\n            \"acml_vol\": \"2313443\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"605764\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"010120\",\r\n            \"hts_kor_isnm\": \"LS ELECTRIC\",\r\n            \"glob_ntsl_qty\": \"47936\",\r\n            \"stck_prpr\": \"164800\",\r\n            \"prdy_vrss\": \"5000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.13\",\r\n            \"acml_vol\": \"787906\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"47936\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"035420\",\r\n            \"hts_kor_isnm\": \"NAVER\",\r\n            \"glob_ntsl_qty\": \"35414\",\r\n            \"stck_prpr\": \"194800\",\r\n            \"prdy_vrss\": \"200\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.10\",\r\n            \"acml_vol\": \"1270446\",\r\n            \"glob_total_seln_qty\": \"3814\",\r\n            \"glob_total_shnu_qty\": \"39228\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"034020\",\r\n            \"hts_kor_isnm\": \"두산에너빌리티\",\r\n            \"glob_ntsl_qty\": \"407917\",\r\n            \"stck_prpr\": \"17080\",\r\n            \"prdy_vrss\": \"530\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.20\",\r\n            \"acml_vol\": \"4896880\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"407917\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"032830\",\r\n            \"hts_kor_isnm\": \"삼성생명\",\r\n            \"glob_ntsl_qty\": \"71420\",\r\n            \"stck_prpr\": \"88300\",\r\n            \"prdy_vrss\": \"4500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"5.37\",\r\n            \"acml_vol\": \"428755\",\r\n            \"glob_total_seln_qty\": \"106254\",\r\n            \"glob_total_shnu_qty\": \"177674\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"196170\",\r\n            \"hts_kor_isnm\": \"알테오젠\",\r\n            \"glob_ntsl_qty\": \"29877\",\r\n            \"stck_prpr\": \"177300\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.06\",\r\n            \"acml_vol\": \"848702\",\r\n            \"glob_total_seln_qty\": \"902\",\r\n            \"glob_total_shnu_qty\": \"30779\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"031980\",\r\n            \"hts_kor_isnm\": \"피에스케이홀딩스\",\r\n            \"glob_ntsl_qty\": \"107530\",\r\n            \"stck_prpr\": \"50500\",\r\n            \"prdy_vrss\": \"3900\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"8.37\",\r\n            \"acml_vol\": \"625360\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"107530\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"036930\",\r\n            \"hts_kor_isnm\": \"주성엔지니어링\",\r\n            \"glob_ntsl_qty\": \"139898\",\r\n            \"stck_prpr\": \"34950\",\r\n            \"prdy_vrss\": \"600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"1.75\",\r\n            \"acml_vol\": \"782431\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"139898\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"259960\",\r\n            \"hts_kor_isnm\": \"크래프톤\",\r\n            \"glob_ntsl_qty\": \"18822\",\r\n            \"stck_prpr\": \"257500\",\r\n            \"prdy_vrss\": \"6500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"2.59\",\r\n            \"acml_vol\": \"192541\",\r\n            \"glob_total_seln_qty\": \"20936\",\r\n            \"glob_total_shnu_qty\": \"39758\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"024110\",\r\n            \"hts_kor_isnm\": \"기업은행\",\r\n            \"glob_ntsl_qty\": \"296747\",\r\n            \"stck_prpr\": \"13760\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.73\",\r\n            \"acml_vol\": \"1259841\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"296747\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"047810\",\r\n            \"hts_kor_isnm\": \"한국항공우주\",\r\n            \"glob_ntsl_qty\": \"75000\",\r\n            \"stck_prpr\": \"53200\",\r\n            \"prdy_vrss\": \"0\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"acml_vol\": \"499071\",\r\n            \"glob_total_seln_qty\": \"0\",\r\n            \"glob_total_shnu_qty\": \"75000\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"298040\",\r\n            \"hts_kor_isnm\": \"효성중공업\",\r\n            \"glob_ntsl_qty\": \"13317\",\r\n            \"stck_prpr\": \"298000\",\r\n            \"prdy_vrss\": \"9500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.29\",\r\n            \"acml_vol\": \"127846\",\r\n            \"glob_total_seln_qty\": \"435\",\r\n            \"glob_total_shnu_qty\": \"13752\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"000720\",\r\n            \"hts_kor_isnm\": \"현대건설\",\r\n            \"glob_ntsl_qty\": \"105515\",\r\n            \"stck_prpr\": \"35600\",\r\n            \"prdy_vrss\": \"350\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.99\",\r\n            \"acml_vol\": \"383978\",\r\n            \"glob_total_seln_qty\": \"9872\",\r\n            \"glob_total_shnu_qty\": \"115387\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"084370\",\r\n            \"hts_kor_isnm\": \"유진테크\",\r\n            \"glob_ntsl_qty\": \"60338\",\r\n            \"stck_prpr\": \"57600\",\r\n            \"prdy_vrss\": \"2200\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"3.97\",\r\n            \"acml_vol\": \"242728\",\r\n            \"glob_total_seln_qty\": \"18396\",\r\n            \"glob_total_shnu_qty\": \"78734\"\r\n        },\r\n        {\r\n            \"stck_shrn_iscd\": \"064350\",\r\n            \"hts_kor_isnm\": \"현대로템\",\r\n            \"glob_ntsl_qty\": \"91584\",\r\n            \"stck_prpr\": \"38100\",\r\n            \"prdy_vrss\": \"150\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"0.40\",\r\n            \"acml_vol\": \"1032621\",\r\n            \"glob_total_seln_qty\": \"2256\",\r\n            \"glob_total_shnu_qty\": \"93840\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST644400C0",
    "name": "종목별 외국계 순매수추이",
    "url": "/uapi/domestic-stock/v1/quotations/frgnmem-pchs-trend",
    "sheet": "종목별 외국계 순매수추이",
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
        "element": "bsop_hour",
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
        "element": "frgn_seln_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frgn_shnu_vol",
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
      },
      {
        "element": "FID_INPUT_ISCD:005930\r\nFID_INPUT_ISCD_2:99999",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"bsop_hour\": \"153106\",\r\n            \"stck_prpr\": \"81300\",\r\n            \"prdy_vrss\": \"3700\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.77\",\r\n            \"acml_vol\": \"24771461\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4418409\",\r\n            \"glob_ntby_qty\": \"3870530\",\r\n            \"frgn_ntby_qty_icdc\": \"194396\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151952\",\r\n            \"stck_prpr\": \"81200\",\r\n            \"prdy_vrss\": \"3600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.64\",\r\n            \"acml_vol\": \"23517309\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4224013\",\r\n            \"glob_ntby_qty\": \"3676134\",\r\n            \"frgn_ntby_qty_icdc\": \"3123\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151836\",\r\n            \"stck_prpr\": \"81100\",\r\n            \"prdy_vrss\": \"3500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.51\",\r\n            \"acml_vol\": \"23404992\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4220890\",\r\n            \"glob_ntby_qty\": \"3673011\",\r\n            \"frgn_ntby_qty_icdc\": \"1700\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151724\",\r\n            \"stck_prpr\": \"81100\",\r\n            \"prdy_vrss\": \"3500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.51\",\r\n            \"acml_vol\": \"23374199\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4219190\",\r\n            \"glob_ntby_qty\": \"3671311\",\r\n            \"frgn_ntby_qty_icdc\": \"1261\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151613\",\r\n            \"stck_prpr\": \"81100\",\r\n            \"prdy_vrss\": \"3500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.51\",\r\n            \"acml_vol\": \"23327774\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4217929\",\r\n            \"glob_ntby_qty\": \"3670050\",\r\n            \"frgn_ntby_qty_icdc\": \"5152\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151503\",\r\n            \"stck_prpr\": \"81100\",\r\n            \"prdy_vrss\": \"3500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.51\",\r\n            \"acml_vol\": \"23255295\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4212777\",\r\n            \"glob_ntby_qty\": \"3664898\",\r\n            \"frgn_ntby_qty_icdc\": \"181\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151355\",\r\n            \"stck_prpr\": \"81200\",\r\n            \"prdy_vrss\": \"3600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.64\",\r\n            \"acml_vol\": \"23222914\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4212596\",\r\n            \"glob_ntby_qty\": \"3664717\",\r\n            \"frgn_ntby_qty_icdc\": \"87\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151245\",\r\n            \"stck_prpr\": \"81200\",\r\n            \"prdy_vrss\": \"3600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.64\",\r\n            \"acml_vol\": \"23207485\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4212509\",\r\n            \"glob_ntby_qty\": \"3664630\",\r\n            \"frgn_ntby_qty_icdc\": \"588\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151136\",\r\n            \"stck_prpr\": \"81300\",\r\n            \"prdy_vrss\": \"3700\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.77\",\r\n            \"acml_vol\": \"23126698\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4211921\",\r\n            \"glob_ntby_qty\": \"3664042\",\r\n            \"frgn_ntby_qty_icdc\": \"4468\"\r\n        },\r\n        {\r\n            \"bsop_hour\": \"151022\",\r\n            \"stck_prpr\": \"81200\",\r\n            \"prdy_vrss\": \"3600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_ctrt\": \"4.64\",\r\n            \"acml_vol\": \"23058530\",\r\n            \"frgn_seln_vol\": \"547879\",\r\n            \"frgn_shnu_vol\": \"4207453\",\r\n            \"glob_ntby_qty\": \"3659574\",\r\n            \"frgn_ntby_qty_icdc\": \"143\"\r\n        },...\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHKST11300006",
    "name": "관심종목(멀티종목) 시세조회",
    "url": "/uapi/domestic-stock/v1/quotations/intstock-multprice",
    "sheet": "관심종목(멀티종목) 시세조회",
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
        "element": "kospi_kosdaq_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mrkt_trtm_cls_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hour_cls_code",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter_shrn_iscd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter_kor_isnm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_prdy_vrss",
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
        "element": "inter2_oprc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_hgpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_lwpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_llam",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_mxpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_askp",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_bidp",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "seln_rsqn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "shnu_rsqn",
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
        "element": "acml_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_prdy_clpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "oprc_vrss_hgpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "intr_antc_cntg_vrss",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "intr_antc_cntg_vrss_sign",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "intr_antc_cntg_prdy_ctrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "intr_antc_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inter2_sdpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "FID_COND_MRKT_DIV_CODE_1:J\r\nFID_INPUT_ISCD_1:005930\r\nFID_COND_MRKT_DIV_CODE_2:J\r\nFID_INPUT_ISCD_2:000660\r\nFID_COND_MRKT_DIV_CODE_3:U\r\nFID_INPUT_ISCD_3:0001",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"kospi_kosdaq_cls_name\": \"거래소\",\r\n            \"mrkt_trtm_cls_name\": \"거래소\",\r\n            \"hour_cls_code\": \"0\",\r\n            \"inter_shrn_iscd\": \"005930\",\r\n            \"inter_kor_isnm\": \"삼성전자\",\r\n            \"inter2_prpr\": \"77400\",\r\n            \"inter2_prdy_vrss\": \"-800\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.02\",\r\n            \"acml_vol\": \"15713440\",\r\n            \"inter2_oprc\": \"78600\",\r\n            \"inter2_hgpr\": \"78800\",\r\n            \"inter2_lwpr\": \"77200\",\r\n            \"inter2_llam\": \"54800\",\r\n            \"inter2_mxpr\": \"101600\",\r\n            \"inter2_askp\": \"77400\",\r\n            \"inter2_bidp\": \"77300\",\r\n            \"seln_rsqn\": \"10248\",\r\n            \"shnu_rsqn\": \"269626\",\r\n            \"total_askp_rsqn\": \"1404667\",\r\n            \"total_bidp_rsqn\": \"2150657\",\r\n            \"acml_tr_pbmn\": \"1221686345500\",\r\n            \"inter2_prdy_clpr\": \"78200\",\r\n            \"oprc_vrss_hgpr_rate\": \"0.25\",\r\n            \"intr_antc_cntg_vrss\": \"0\",\r\n            \"intr_antc_cntg_vrss_sign\": \"3\",\r\n            \"intr_antc_cntg_prdy_ctrt\": \"0.00\",\r\n            \"intr_antc_vol\": \"0\",\r\n            \"inter2_sdpr\": \"78200\"\r\n        },\r\n        {\r\n            \"kospi_kosdaq_cls_name\": \"거래소\",\r\n            \"mrkt_trtm_cls_name\": \"거래소\",\r\n            \"hour_cls_code\": \"0\",\r\n            \"inter_shrn_iscd\": \"000660\",\r\n            \"inter_kor_isnm\": \"SK하이닉스\",\r\n            \"inter2_prpr\": \"189900\",\r\n            \"inter2_prdy_vrss\": \"-3100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.61\",\r\n            \"acml_vol\": \"2758944\",\r\n            \"inter2_oprc\": \"192000\",\r\n            \"inter2_hgpr\": \"193500\",\r\n            \"inter2_lwpr\": \"189900\",\r\n            \"inter2_llam\": \"135100\",\r\n            \"inter2_mxpr\": \"250500\",\r\n            \"inter2_askp\": \"190000\",\r\n            \"inter2_bidp\": \"189900\",\r\n            \"seln_rsqn\": \"5625\",\r\n            \"shnu_rsqn\": \"4782\",\r\n            \"total_askp_rsqn\": \"27318\",\r\n            \"total_bidp_rsqn\": \"33313\",\r\n            \"acml_tr_pbmn\": \"528227479600\",\r\n            \"inter2_prdy_clpr\": \"193000\",\r\n            \"oprc_vrss_hgpr_rate\": \"0.78\",\r\n            \"intr_antc_cntg_vrss\": \"0\",\r\n            \"intr_antc_cntg_vrss_sign\": \"3\",\r\n            \"intr_antc_cntg_prdy_ctrt\": \"0.00\",\r\n            \"intr_antc_vol\": \"0\",\r\n            \"inter2_sdpr\": \"193000\"\r\n        },\r\n        {\r\n            \"kospi_kosdaq_cls_name\": \"업종\",\r\n            \"mrkt_trtm_cls_name\": \"\",\r\n            \"hour_cls_code\": \"2\",\r\n            \"inter_shrn_iscd\": \"0001\",\r\n            \"inter_kor_isnm\": \"종합\",\r\n            \"inter2_prpr\": \"2724.62\",\r\n            \"inter2_prdy_vrss\": \"-28.38\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_ctrt\": \"-1.03\",\r\n            \"acml_vol\": \"561107\",\r\n            \"inter2_oprc\": \"2751.47\",\r\n            \"inter2_hgpr\": \"2752.17\",\r\n            \"inter2_lwpr\": \"2724.62\",\r\n            \"inter2_llam\": \"\",\r\n            \"inter2_mxpr\": \"\",\r\n            \"inter2_askp\": \"\",\r\n            \"inter2_bidp\": \"\",\r\n            \"seln_rsqn\": \"\",\r\n            \"shnu_rsqn\": \"\",\r\n            \"total_askp_rsqn\": \"19237981\",\r\n            \"total_bidp_rsqn\": \"49315150\",\r\n            \"acml_tr_pbmn\": \"10288958\",\r\n            \"inter2_prdy_clpr\": \"2753.00\",\r\n            \"oprc_vrss_hgpr_rate\": \"\",\r\n            \"intr_antc_cntg_vrss\": \"-28.18\",\r\n            \"intr_antc_cntg_vrss_sign\": \"5\",\r\n            \"intr_antc_cntg_prdy_ctrt\": \"-1.02\",\r\n            \"intr_antc_vol\": \"560841\",\r\n            \"inter2_sdpr\": \"2753.00\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "FHPST01710000",
    "name": "거래량순위",
    "url": "/uapi/domestic-stock/v1/quotations/volume-rank",
    "sheet": "거래량순위",
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
        "element": "Output",
        "type": "object array",
        "required": "Y",
        "description": "Array"
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
        "element": "data_rank",
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
        "element": "prdy_vol",
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
        "element": "avrg_vol",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "n_befr_clpr_vrss_prpr_rate",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vol_inrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "vol_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nday_vol_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "avrg_tr_pbmn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tr_pbmn_tnrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nday_tr_pbmn_tnrt",
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
        "element": "{\r\n\"FID_COND_MRKT_DIV_CODE\":\"J\",\r\n\"FID_COND_SCR_DIV_CODE\":\"20171\",\r\n\"FID_INPUT_ISCD\":\"0000\",\r\n\"FID_DIV_CLS_CODE\":\"0\",\r\n\"FID_BLNG_CLS_CODE\":\"0\",\r\n\"FID_TRGT_CLS_CODE\":\"111111111\",\r\n\"FID_TRGT_EXLS_CLS_CODE\":\"000000\",\r\n\"FID_INPUT_PRICE_1\":\"0\",\r\n\"FID_INPUT_PRICE_2\":\"0\",\r\n\"FID_VOL_CNT\":\"0\",\r\n\"FID_INPUT_DATE_1\":\"0\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      },
      {
        "element": "{\r\n    \"output\": [\r\n        {\r\n            \"hts_kor_isnm\": \"삼성전자\",\r\n            \"mksc_shrn_iscd\": \"005930\",\r\n            \"data_rank\": \"1\",\r\n            \"stck_prpr\": \"65100\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-300\",\r\n            \"prdy_ctrt\": \"-0.46\",\r\n            \"acml_vol\": \"8958147\",\r\n            \"prdy_vol\": \"12334657\",\r\n            \"lstn_stcn\": \"5969782550\",\r\n            \"avrg_vol\": \"8958147\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.46\",\r\n            \"vol_inrt\": \"72.63\",\r\n            \"vol_tnrt\": \"0.15\",\r\n            \"nday_vol_tnrt\": \"0.15\",\r\n            \"avrg_tr_pbmn\": \"584861890300\",\r\n            \"tr_pbmn_tnrt\": \"0.15\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.15\",\r\n            \"acml_tr_pbmn\": \"584861890300\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"두산에너빌리티\",\r\n            \"mksc_shrn_iscd\": \"034020\",\r\n            \"data_rank\": \"2\",\r\n            \"stck_prpr\": \"15730\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-90\",\r\n            \"prdy_ctrt\": \"-0.57\",\r\n            \"acml_vol\": \"3285533\",\r\n            \"prdy_vol\": \"6090991\",\r\n            \"lstn_stcn\": \"640561146\",\r\n            \"avrg_vol\": \"3285533\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.57\",\r\n            \"vol_inrt\": \"53.94\",\r\n            \"vol_tnrt\": \"0.51\",\r\n            \"nday_vol_tnrt\": \"0.51\",\r\n            \"avrg_tr_pbmn\": \"52081429080\",\r\n            \"tr_pbmn_tnrt\": \"0.52\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.52\",\r\n            \"acml_tr_pbmn\": \"52081429080\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"LG디스플레이\",\r\n            \"mksc_shrn_iscd\": \"034220\",\r\n            \"data_rank\": \"3\",\r\n            \"stck_prpr\": \"15670\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"470\",\r\n            \"prdy_ctrt\": \"3.09\",\r\n            \"acml_vol\": \"3171164\",\r\n            \"prdy_vol\": \"1476096\",\r\n            \"lstn_stcn\": \"357815700\",\r\n            \"avrg_vol\": \"3171164\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"3.09\",\r\n            \"vol_inrt\": \"214.83\",\r\n            \"vol_tnrt\": \"0.89\",\r\n            \"nday_vol_tnrt\": \"0.89\",\r\n            \"avrg_tr_pbmn\": \"50045759170\",\r\n            \"tr_pbmn_tnrt\": \"0.89\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.89\",\r\n            \"acml_tr_pbmn\": \"50045759170\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"SK하이닉스\",\r\n            \"mksc_shrn_iscd\": \"000660\",\r\n            \"data_rank\": \"4\",\r\n            \"stck_prpr\": \"91700\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1300\",\r\n            \"prdy_ctrt\": \"1.44\",\r\n            \"acml_vol\": \"2833739\",\r\n            \"prdy_vol\": \"5121364\",\r\n            \"lstn_stcn\": \"728002365\",\r\n            \"avrg_vol\": \"2833739\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"1.44\",\r\n            \"vol_inrt\": \"55.33\",\r\n            \"vol_tnrt\": \"0.39\",\r\n            \"nday_vol_tnrt\": \"0.39\",\r\n            \"avrg_tr_pbmn\": \"258969317100\",\r\n            \"tr_pbmn_tnrt\": \"0.39\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.39\",\r\n            \"acml_tr_pbmn\": \"258969317100\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"현대로템\",\r\n            \"mksc_shrn_iscd\": \"064350\",\r\n            \"data_rank\": \"5\",\r\n            \"stck_prpr\": \"31450\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-1500\",\r\n            \"prdy_ctrt\": \"-4.55\",\r\n            \"acml_vol\": \"2709946\",\r\n            \"prdy_vol\": \"1161286\",\r\n            \"lstn_stcn\": \"109142293\",\r\n            \"avrg_vol\": \"2709946\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-4.55\",\r\n            \"vol_inrt\": \"233.36\",\r\n            \"vol_tnrt\": \"2.48\",\r\n            \"nday_vol_tnrt\": \"2.48\",\r\n            \"avrg_tr_pbmn\": \"85496575550\",\r\n            \"tr_pbmn_tnrt\": \"2.49\",\r\n            \"nday_tr_pbmn_tnrt\": \"2.49\",\r\n            \"acml_tr_pbmn\": \"85496575550\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"HMM\",\r\n            \"mksc_shrn_iscd\": \"011200\",\r\n            \"data_rank\": \"6\",\r\n            \"stck_prpr\": \"18250\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-550\",\r\n            \"prdy_ctrt\": \"-2.93\",\r\n            \"acml_vol\": \"2286426\",\r\n            \"prdy_vol\": \"1530846\",\r\n            \"lstn_stcn\": \"489039496\",\r\n            \"avrg_vol\": \"2286426\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-2.93\",\r\n            \"vol_inrt\": \"149.36\",\r\n            \"vol_tnrt\": \"0.47\",\r\n            \"nday_vol_tnrt\": \"0.47\",\r\n            \"avrg_tr_pbmn\": \"42083654470\",\r\n            \"tr_pbmn_tnrt\": \"0.47\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.47\",\r\n            \"acml_tr_pbmn\": \"42083654470\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"카카오\",\r\n            \"mksc_shrn_iscd\": \"035720\",\r\n            \"data_rank\": \"7\",\r\n            \"stck_prpr\": \"57700\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1600\",\r\n            \"prdy_ctrt\": \"2.85\",\r\n            \"acml_vol\": \"1873007\",\r\n            \"prdy_vol\": \"922948\",\r\n            \"lstn_stcn\": \"445841128\",\r\n            \"avrg_vol\": \"1873007\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"2.85\",\r\n            \"vol_inrt\": \"202.94\",\r\n            \"vol_tnrt\": \"0.42\",\r\n            \"nday_vol_tnrt\": \"0.42\",\r\n            \"avrg_tr_pbmn\": \"107707977500\",\r\n            \"tr_pbmn_tnrt\": \"0.42\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.42\",\r\n            \"acml_tr_pbmn\": \"107707977500\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"삼성중공업\",\r\n            \"mksc_shrn_iscd\": \"010140\",\r\n            \"data_rank\": \"8\",\r\n            \"stck_prpr\": \"5510\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"30\",\r\n            \"prdy_ctrt\": \"0.55\",\r\n            \"acml_vol\": \"1711650\",\r\n            \"prdy_vol\": \"1979941\",\r\n            \"lstn_stcn\": \"880000000\",\r\n            \"avrg_vol\": \"1711650\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.55\",\r\n            \"vol_inrt\": \"86.45\",\r\n            \"vol_tnrt\": \"0.19\",\r\n            \"nday_vol_tnrt\": \"0.19\",\r\n            \"avrg_tr_pbmn\": \"9363354660\",\r\n            \"tr_pbmn_tnrt\": \"0.19\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.19\",\r\n            \"acml_tr_pbmn\": \"9363354660\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"한화솔루션\",\r\n            \"mksc_shrn_iscd\": \"009830\",\r\n            \"data_rank\": \"9\",\r\n            \"stck_prpr\": \"48000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"1150\",\r\n            \"prdy_ctrt\": \"2.45\",\r\n            \"acml_vol\": \"1582296\",\r\n            \"prdy_vol\": \"910120\",\r\n            \"lstn_stcn\": \"171892536\",\r\n            \"avrg_vol\": \"1582296\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"2.45\",\r\n            \"vol_inrt\": \"173.86\",\r\n            \"vol_tnrt\": \"0.92\",\r\n            \"nday_vol_tnrt\": \"0.92\",\r\n            \"avrg_tr_pbmn\": \"75841144250\",\r\n            \"tr_pbmn_tnrt\": \"0.92\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.92\",\r\n            \"acml_tr_pbmn\": \"75841144250\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"포스코인터내셔널\",\r\n            \"mksc_shrn_iscd\": \"047050\",\r\n            \"data_rank\": \"10\",\r\n            \"stck_prpr\": \"28550\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"200\",\r\n            \"prdy_ctrt\": \"0.71\",\r\n            \"acml_vol\": \"1390133\",\r\n            \"prdy_vol\": \"2369179\",\r\n            \"lstn_stcn\": \"175922788\",\r\n            \"avrg_vol\": \"1390133\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.71\",\r\n            \"vol_inrt\": \"58.68\",\r\n            \"vol_tnrt\": \"0.79\",\r\n            \"nday_vol_tnrt\": \"0.79\",\r\n            \"avrg_tr_pbmn\": \"39675793900\",\r\n            \"tr_pbmn_tnrt\": \"0.79\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.79\",\r\n            \"acml_tr_pbmn\": \"39675793900\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"한국전력\",\r\n            \"mksc_shrn_iscd\": \"015760\",\r\n            \"data_rank\": \"11\",\r\n            \"stck_prpr\": \"18450\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-230\",\r\n            \"prdy_ctrt\": \"-1.23\",\r\n            \"acml_vol\": \"1312142\",\r\n            \"prdy_vol\": \"1844472\",\r\n            \"lstn_stcn\": \"641964077\",\r\n            \"avrg_vol\": \"1312142\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-1.23\",\r\n            \"vol_inrt\": \"71.14\",\r\n            \"vol_tnrt\": \"0.20\",\r\n            \"nday_vol_tnrt\": \"0.20\",\r\n            \"avrg_tr_pbmn\": \"24308085110\",\r\n            \"tr_pbmn_tnrt\": \"0.21\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.21\",\r\n            \"acml_tr_pbmn\": \"24308085110\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"우리금융지주\",\r\n            \"mksc_shrn_iscd\": \"316140\",\r\n            \"data_rank\": \"12\",\r\n            \"stck_prpr\": \"11720\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-80\",\r\n            \"prdy_ctrt\": \"-0.68\",\r\n            \"acml_vol\": \"1270105\",\r\n            \"prdy_vol\": \"1455657\",\r\n            \"lstn_stcn\": \"728060549\",\r\n            \"avrg_vol\": \"1270105\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.68\",\r\n            \"vol_inrt\": \"87.25\",\r\n            \"vol_tnrt\": \"0.17\",\r\n            \"nday_vol_tnrt\": \"0.17\",\r\n            \"avrg_tr_pbmn\": \"14886199950\",\r\n            \"tr_pbmn_tnrt\": \"0.17\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.17\",\r\n            \"acml_tr_pbmn\": \"14886199950\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"팬오션\",\r\n            \"mksc_shrn_iscd\": \"028670\",\r\n            \"data_rank\": \"13\",\r\n            \"stck_prpr\": \"5100\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"prdy_vrss\": \"0\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"acml_vol\": \"1156091\",\r\n            \"prdy_vol\": \"1296967\",\r\n            \"lstn_stcn\": \"534569512\",\r\n            \"avrg_vol\": \"1156091\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.00\",\r\n            \"vol_inrt\": \"89.14\",\r\n            \"vol_tnrt\": \"0.22\",\r\n            \"nday_vol_tnrt\": \"0.22\",\r\n            \"avrg_tr_pbmn\": \"5900434210\",\r\n            \"tr_pbmn_tnrt\": \"0.22\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.22\",\r\n            \"acml_tr_pbmn\": \"5900434210\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"기아\",\r\n            \"mksc_shrn_iscd\": \"000270\",\r\n            \"data_rank\": \"14\",\r\n            \"stck_prpr\": \"88000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"700\",\r\n            \"prdy_ctrt\": \"0.80\",\r\n            \"acml_vol\": \"935222\",\r\n            \"prdy_vol\": \"1866373\",\r\n            \"lstn_stcn\": \"405363347\",\r\n            \"avrg_vol\": \"935222\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.80\",\r\n            \"vol_inrt\": \"50.11\",\r\n            \"vol_tnrt\": \"0.23\",\r\n            \"nday_vol_tnrt\": \"0.23\",\r\n            \"avrg_tr_pbmn\": \"82381989600\",\r\n            \"tr_pbmn_tnrt\": \"0.23\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.23\",\r\n            \"acml_tr_pbmn\": \"82381989600\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"신한지주\",\r\n            \"mksc_shrn_iscd\": \"055550\",\r\n            \"data_rank\": \"15\",\r\n            \"stck_prpr\": \"34600\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"50\",\r\n            \"prdy_ctrt\": \"0.14\",\r\n            \"acml_vol\": \"930868\",\r\n            \"prdy_vol\": \"1351786\",\r\n            \"lstn_stcn\": \"505108399\",\r\n            \"avrg_vol\": \"930868\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.14\",\r\n            \"vol_inrt\": \"68.86\",\r\n            \"vol_tnrt\": \"0.18\",\r\n            \"nday_vol_tnrt\": \"0.18\",\r\n            \"avrg_tr_pbmn\": \"32273778800\",\r\n            \"tr_pbmn_tnrt\": \"0.18\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.18\",\r\n            \"acml_tr_pbmn\": \"32273778800\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"메리츠금융지주\",\r\n            \"mksc_shrn_iscd\": \"138040\",\r\n            \"data_rank\": \"16\",\r\n            \"stck_prpr\": \"45300\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-400\",\r\n            \"prdy_ctrt\": \"-0.88\",\r\n            \"acml_vol\": \"627094\",\r\n            \"prdy_vol\": \"817468\",\r\n            \"lstn_stcn\": \"208217858\",\r\n            \"avrg_vol\": \"627094\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.88\",\r\n            \"vol_inrt\": \"76.71\",\r\n            \"vol_tnrt\": \"0.30\",\r\n            \"nday_vol_tnrt\": \"0.30\",\r\n            \"avrg_tr_pbmn\": \"28375338250\",\r\n            \"tr_pbmn_tnrt\": \"0.30\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.30\",\r\n            \"acml_tr_pbmn\": \"28375338250\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"카카오뱅크\",\r\n            \"mksc_shrn_iscd\": \"323410\",\r\n            \"data_rank\": \"17\",\r\n            \"stck_prpr\": \"24850\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-300\",\r\n            \"prdy_ctrt\": \"-1.19\",\r\n            \"acml_vol\": \"625836\",\r\n            \"prdy_vol\": \"1527116\",\r\n            \"lstn_stcn\": \"476767137\",\r\n            \"avrg_vol\": \"625836\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-1.19\",\r\n            \"vol_inrt\": \"40.98\",\r\n            \"vol_tnrt\": \"0.13\",\r\n            \"nday_vol_tnrt\": \"0.13\",\r\n            \"avrg_tr_pbmn\": \"15712615750\",\r\n            \"tr_pbmn_tnrt\": \"0.13\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.13\",\r\n            \"acml_tr_pbmn\": \"15712615750\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"KT\",\r\n            \"mksc_shrn_iscd\": \"030200\",\r\n            \"data_rank\": \"18\",\r\n            \"stck_prpr\": \"31300\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"100\",\r\n            \"prdy_ctrt\": \"0.32\",\r\n            \"acml_vol\": \"569371\",\r\n            \"prdy_vol\": \"1294632\",\r\n            \"lstn_stcn\": \"261111808\",\r\n            \"avrg_vol\": \"569371\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.32\",\r\n            \"vol_inrt\": \"43.98\",\r\n            \"vol_tnrt\": \"0.22\",\r\n            \"nday_vol_tnrt\": \"0.22\",\r\n            \"avrg_tr_pbmn\": \"17771655950\",\r\n            \"tr_pbmn_tnrt\": \"0.22\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.22\",\r\n            \"acml_tr_pbmn\": \"17771655950\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"에스디바이오센서\",\r\n            \"mksc_shrn_iscd\": \"137310\",\r\n            \"data_rank\": \"19\",\r\n            \"stck_prpr\": \"17860\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-540\",\r\n            \"prdy_ctrt\": \"-2.93\",\r\n            \"acml_vol\": \"520565\",\r\n            \"prdy_vol\": \"487837\",\r\n            \"lstn_stcn\": \"104452353\",\r\n            \"avrg_vol\": \"520565\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-2.93\",\r\n            \"vol_inrt\": \"106.71\",\r\n            \"vol_tnrt\": \"0.50\",\r\n            \"nday_vol_tnrt\": \"0.50\",\r\n            \"avrg_tr_pbmn\": \"9342427100\",\r\n            \"tr_pbmn_tnrt\": \"0.50\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.50\",\r\n            \"acml_tr_pbmn\": \"9342427100\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"NAVER\",\r\n            \"mksc_shrn_iscd\": \"035420\",\r\n            \"data_rank\": \"20\",\r\n            \"stck_prpr\": \"213000\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"5500\",\r\n            \"prdy_ctrt\": \"2.65\",\r\n            \"acml_vol\": \"484026\",\r\n            \"prdy_vol\": \"528940\",\r\n            \"lstn_stcn\": \"164049085\",\r\n            \"avrg_vol\": \"484026\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"2.65\",\r\n            \"vol_inrt\": \"91.51\",\r\n            \"vol_tnrt\": \"0.30\",\r\n            \"nday_vol_tnrt\": \"0.30\",\r\n            \"avrg_tr_pbmn\": \"102530676000\",\r\n            \"tr_pbmn_tnrt\": \"0.29\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.29\",\r\n            \"acml_tr_pbmn\": \"102530676000\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"기업은행\",\r\n            \"mksc_shrn_iscd\": \"024110\",\r\n            \"data_rank\": \"21\",\r\n            \"stck_prpr\": \"10070\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-30\",\r\n            \"prdy_ctrt\": \"-0.30\",\r\n            \"acml_vol\": \"469367\",\r\n            \"prdy_vol\": \"707261\",\r\n            \"lstn_stcn\": \"797425869\",\r\n            \"avrg_vol\": \"469367\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.30\",\r\n            \"vol_inrt\": \"66.36\",\r\n            \"vol_tnrt\": \"0.06\",\r\n            \"nday_vol_tnrt\": \"0.06\",\r\n            \"avrg_tr_pbmn\": \"4736559470\",\r\n            \"tr_pbmn_tnrt\": \"0.06\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.06\",\r\n            \"acml_tr_pbmn\": \"4736559470\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"포스코퓨처엠\",\r\n            \"mksc_shrn_iscd\": \"003670\",\r\n            \"data_rank\": \"22\",\r\n            \"stck_prpr\": \"312500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"2500\",\r\n            \"prdy_ctrt\": \"0.81\",\r\n            \"acml_vol\": \"468389\",\r\n            \"prdy_vol\": \"856091\",\r\n            \"lstn_stcn\": \"77463220\",\r\n            \"avrg_vol\": \"468389\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.81\",\r\n            \"vol_inrt\": \"54.71\",\r\n            \"vol_tnrt\": \"0.60\",\r\n            \"nday_vol_tnrt\": \"0.60\",\r\n            \"avrg_tr_pbmn\": \"145466512000\",\r\n            \"tr_pbmn_tnrt\": \"0.60\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.60\",\r\n            \"acml_tr_pbmn\": \"145466512000\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"KB금융\",\r\n            \"mksc_shrn_iscd\": \"105560\",\r\n            \"data_rank\": \"23\",\r\n            \"stck_prpr\": \"49000\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-300\",\r\n            \"prdy_ctrt\": \"-0.61\",\r\n            \"acml_vol\": \"459214\",\r\n            \"prdy_vol\": \"1293549\",\r\n            \"lstn_stcn\": \"403511072\",\r\n            \"avrg_vol\": \"459214\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.61\",\r\n            \"vol_inrt\": \"35.50\",\r\n            \"vol_tnrt\": \"0.11\",\r\n            \"nday_vol_tnrt\": \"0.11\",\r\n            \"avrg_tr_pbmn\": \"22593198000\",\r\n            \"tr_pbmn_tnrt\": \"0.11\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.11\",\r\n            \"acml_tr_pbmn\": \"22593198000\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"한화에어로스페이스\",\r\n            \"mksc_shrn_iscd\": \"012450\",\r\n            \"data_rank\": \"24\",\r\n            \"stck_prpr\": \"103900\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"400\",\r\n            \"prdy_ctrt\": \"0.39\",\r\n            \"acml_vol\": \"458706\",\r\n            \"prdy_vol\": \"345873\",\r\n            \"lstn_stcn\": \"50630000\",\r\n            \"avrg_vol\": \"458706\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.39\",\r\n            \"vol_inrt\": \"132.62\",\r\n            \"vol_tnrt\": \"0.91\",\r\n            \"nday_vol_tnrt\": \"0.91\",\r\n            \"avrg_tr_pbmn\": \"47298434100\",\r\n            \"tr_pbmn_tnrt\": \"0.90\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.90\",\r\n            \"acml_tr_pbmn\": \"47298434100\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"LG유플러스\",\r\n            \"mksc_shrn_iscd\": \"032640\",\r\n            \"data_rank\": \"25\",\r\n            \"stck_prpr\": \"11090\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"60\",\r\n            \"prdy_ctrt\": \"0.54\",\r\n            \"acml_vol\": \"451459\",\r\n            \"prdy_vol\": \"971303\",\r\n            \"lstn_stcn\": \"436611361\",\r\n            \"avrg_vol\": \"451459\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.54\",\r\n            \"vol_inrt\": \"46.48\",\r\n            \"vol_tnrt\": \"0.10\",\r\n            \"nday_vol_tnrt\": \"0.10\",\r\n            \"avrg_tr_pbmn\": \"5009396470\",\r\n            \"tr_pbmn_tnrt\": \"0.10\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.10\",\r\n            \"acml_tr_pbmn\": \"5009396470\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"삼성엔지니어링\",\r\n            \"mksc_shrn_iscd\": \"028050\",\r\n            \"data_rank\": \"26\",\r\n            \"stck_prpr\": \"28950\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-250\",\r\n            \"prdy_ctrt\": \"-0.86\",\r\n            \"acml_vol\": \"446635\",\r\n            \"prdy_vol\": \"512916\",\r\n            \"lstn_stcn\": \"196000000\",\r\n            \"avrg_vol\": \"446635\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-0.86\",\r\n            \"vol_inrt\": \"87.08\",\r\n            \"vol_tnrt\": \"0.23\",\r\n            \"nday_vol_tnrt\": \"0.23\",\r\n            \"avrg_tr_pbmn\": \"12942967050\",\r\n            \"tr_pbmn_tnrt\": \"0.23\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.23\",\r\n            \"acml_tr_pbmn\": \"12942967050\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"현대차\",\r\n            \"mksc_shrn_iscd\": \"005380\",\r\n            \"data_rank\": \"27\",\r\n            \"stck_prpr\": \"204500\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"2000\",\r\n            \"prdy_ctrt\": \"0.99\",\r\n            \"acml_vol\": \"432033\",\r\n            \"prdy_vol\": \"874247\",\r\n            \"lstn_stcn\": \"211531506\",\r\n            \"avrg_vol\": \"432033\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.99\",\r\n            \"vol_inrt\": \"49.42\",\r\n            \"vol_tnrt\": \"0.20\",\r\n            \"nday_vol_tnrt\": \"0.20\",\r\n            \"avrg_tr_pbmn\": \"88091018500\",\r\n            \"tr_pbmn_tnrt\": \"0.20\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.20\",\r\n            \"acml_tr_pbmn\": \"88091018500\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"한국항공우주\",\r\n            \"mksc_shrn_iscd\": \"047810\",\r\n            \"data_rank\": \"28\",\r\n            \"stck_prpr\": \"51700\",\r\n            \"prdy_vrss_sign\": \"2\",\r\n            \"prdy_vrss\": \"300\",\r\n            \"prdy_ctrt\": \"0.58\",\r\n            \"acml_vol\": \"418249\",\r\n            \"prdy_vol\": \"431203\",\r\n            \"lstn_stcn\": \"97475107\",\r\n            \"avrg_vol\": \"418249\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.58\",\r\n            \"vol_inrt\": \"97.00\",\r\n            \"vol_tnrt\": \"0.43\",\r\n            \"nday_vol_tnrt\": \"0.43\",\r\n            \"avrg_tr_pbmn\": \"21574340000\",\r\n            \"tr_pbmn_tnrt\": \"0.43\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.43\",\r\n            \"acml_tr_pbmn\": \"21574340000\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"대한항공\",\r\n            \"mksc_shrn_iscd\": \"003490\",\r\n            \"data_rank\": \"29\",\r\n            \"stck_prpr\": \"22500\",\r\n            \"prdy_vrss_sign\": \"3\",\r\n            \"prdy_vrss\": \"0\",\r\n            \"prdy_ctrt\": \"0.00\",\r\n            \"acml_vol\": \"400822\",\r\n            \"prdy_vol\": \"578620\",\r\n            \"lstn_stcn\": \"368220661\",\r\n            \"avrg_vol\": \"400822\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"0.00\",\r\n            \"vol_inrt\": \"69.27\",\r\n            \"vol_tnrt\": \"0.11\",\r\n            \"nday_vol_tnrt\": \"0.11\",\r\n            \"avrg_tr_pbmn\": \"9020223200\",\r\n            \"tr_pbmn_tnrt\": \"0.11\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.11\",\r\n            \"acml_tr_pbmn\": \"9020223200\"\r\n        },\r\n        {\r\n            \"hts_kor_isnm\": \"한국가스공사\",\r\n            \"mksc_shrn_iscd\": \"036460\",\r\n            \"data_rank\": \"30\",\r\n            \"stck_prpr\": \"25350\",\r\n            \"prdy_vrss_sign\": \"5\",\r\n            \"prdy_vrss\": \"-500\",\r\n            \"prdy_ctrt\": \"-1.93\",\r\n            \"acml_vol\": \"369094\",\r\n            \"prdy_vol\": \"340512\",\r\n            \"lstn_stcn\": \"92313000\",\r\n            \"avrg_vol\": \"369094\",\r\n            \"n_befr_clpr_vrss_prpr_rate\": \"-1.93\",\r\n            \"vol_inrt\": \"108.39\",\r\n            \"vol_tnrt\": \"0.40\",\r\n            \"nday_vol_tnrt\": \"0.40\",\r\n            \"avrg_tr_pbmn\": \"9408072150\",\r\n            \"tr_pbmn_tnrt\": \"0.40\",\r\n            \"nday_tr_pbmn_tnrt\": \"0.40\",\r\n            \"acml_tr_pbmn\": \"9408072150\"\r\n        }\r\n    ],\r\n    \"rt_cd\": \"0\",\r\n    \"msg_cd\": \"MCA00000\",\r\n    \"msg1\": \"정상처리 되었습니다.\"\r\n}",
        "type": "",
        "required": "",
        "description": ""
      }
    ]
  }
]"""


def load_quotations_response_specs() -> list[dict[str, Any]]:
    return json.loads(_RESPONSE_SPECS_JSON)


QUOTATIONS_API_RESPONSE_SPECS = load_quotations_response_specs()
QUOTATIONS_API_RESPONSE_SPECS_BY_TR_ID = {
    str(spec.get("tr_id", "")): spec for spec in QUOTATIONS_API_RESPONSE_SPECS if spec.get("tr_id")
}
