"""국내주식 trading API 응답 스펙."""

from __future__ import annotations

import json
from typing import Any


_RESPONSE_SPECS_JSON = r"""[
  {
    "tr_id": "CTRGA011R",
    "name": "기간별계좌권리현황조회",
    "url": "/uapi/domestic-stock/v1/trading/period-rights",
    "sheet": "기간별계좌권리현황조회",
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
        "element": "acno10",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rght_type_cd",
        "type": "string",
        "required": "Y",
        "description": "1\t유상\r\n2\t무상\r\n3\t배당\r\n4\t매수청구\r\n5\t공개매수\r\n6\t주주총회\r\n7\t신주인수권증서\r\n8\t반대의사\r\n9\t신주인수권증권\r\n11\t합병\r\n12\t회사분할\r\n13\t주식교환\r\n14\t액면분할\r\n15\t액면병합\r\n16\t종목변경\r\n17\t감자\r\n18\t신구주합병\r\n21\t후합병\r\n22\t후회사분할\r\n23\t후주식교환\r\n24\t후액면분할\r\n25\t후액면병합\r\n26\t후종목변경\r\n27\t후감자\r\n28\t후신구주합병\r\n31\t뮤츄얼펀드\r\n32\tETF\r\n33\t선박투자회사\r\n34\t투융자회사\r\n35\t해외자원\r\n36\t부동산신탁(Ritz)\r\n37\t상장수익증권\r\n41\tELW만기\r\n42\tELS분배\r\n43\tDLS분배\r\n44\t하일드펀드\r\n45\tETN\r\n51\t전환청구\r\n52\t교환청구\r\n53\tBW청구\r\n54\tWRT청구\r\n55\t채권풋옵션청구\r\n56\t전환우선주청구\r\n57\t전환조건부청구\r\n58\t전자증권일괄입고\r\n59\t클라우드펀딩일괄입고\r\n61\t원리금상환\r\n62\t스트립채권\r\n71\tWRT소멸\r\n72\tWRT증권\r\n73\tDR전환\r\n74\t배당옵션\r\n75\t특별배당\r\n76\tISINCODE변경\r\n77\t실권주청약\r\n81\t해외분배금(청산)\r\n82\t해외분배금(조기상환)\r\n83\t해외분배금(상장폐지)\r\n84\tDR FEE\r\n85\tSECTION 871M\r\n86\t종목전환\r\n87\t재매수\r\n88\t종목교환\r\n89\t기타이벤트\r\n91\t공모주\r\n92\t청약\r\n93\t환매\r\n99\t기타권리사유"
      },
      {
        "element": "bass_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rght_cblc_type_cd",
        "type": "string",
        "required": "Y",
        "description": "1\t입고\r\n2\t출고\r\n3\t출고입고\r\n4\t출고입금\r\n5\t출고출금\r\n10\t현금입금\r\n11\t단수주대금입금\r\n12\t교부금입금\r\n13\t유상감자대금입금\r\n14\t지연이자입금\r\n15\t이자지급\r\n16\t대주권리금출금\r\n17\t분할상환\r\n18\t만기상환\r\n19\t조기상환\r\n20\t출금\r\n21\t입고&입금\r\n22\t입고&입금&단수주대금입금\r\n25\t유상환불금입금\r\n26\t중도상환\r\n27\t분할합병세금출금"
      },
      {
        "element": "rptt_pdno",
        "type": "string",
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
        "element": "shtn_pdno",
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
        "element": "cblc_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "last_alct_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "excs_alct_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_alct_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "last_ftsk_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "last_alct_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "last_ftsk_chgs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rdpt_prca",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dlay_int_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lstg_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sbsc_end_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cash_dfrm_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rqst_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rqst_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rqst_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rfnd_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rfnd_amt",
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
        "element": "tax_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sbsc_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTRP6548R",
    "name": "투자계좌자산현황조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-account-balance",
    "sheet": "투자계좌자산현황조회",
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
        "description": "Array [아래 순서대로 출력 : 20항목]\r\n1: 주식\r\n2: 펀드/MMW\r\n3: IMA\r\n4: 채권\r\n5: ELS/DLS\r\n6: WRAP\r\n7: 신탁\r\n8: RP/발행어음\r\n9: 해외주식\r\n10: 해외채권\r\n11: 금현물\r\n12: CD/CP\r\n13: 전자단기사채\r\n14: 타사상품\r\n15: 외화전자단기사채\r\n16: 외화 ELS/DLS\r\n17: 외화\r\n18: 예수금\r\n19: 청약자예수금\r\n20: 합계\r\n\r\n[21번 계좌일 경우 : 17항목]\r\n1: 수익증권\r\n2: IMA\r\n3: 채권\r\n4: ELS/DLS\r\n5: WRAP\r\n6: 신탁\r\n7: RP\r\n8: 외화rp\r\n9: 해외채권\r\n10: CD/CP\r\n11: 전자단기사채\r\n12: 외화전자단기사채\r\n13: 외화ELS/DLS\r\n14: 외화평가금액\r\n15: 예수금+cma\r\n16: 청약자예수금\r\n17: 합계"
      },
      {
        "element": "pchs_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "crdt_lnd_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "real_nass_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "whol_weit_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "Output2",
        "type": "object",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": "유가매입금액"
      },
      {
        "element": "nass_tot_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": "평가손익금액"
      },
      {
        "element": "evlu_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": "유가평가금액"
      },
      {
        "element": "tot_asst_amt",
        "type": "string",
        "required": "Y",
        "description": "총 자산금액"
      },
      {
        "element": "tot_lnda_tot_ulst_lnda",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cma_auto_loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_mgln_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stln_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "crdt_fncg_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ocl_apl_loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pldg_stup_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "frcr_evlu_tota",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_dncl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cma_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "dncl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_sbst_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_rcvb_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovrs_stck_evlu_amt1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovrs_bond_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "mmf_cma_mgge_loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sbsc_dncl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pbst_sbsc_fnds_loan_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "etpr_crdt_grnt_loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0506R",
    "name": "퇴직연금 예수금조회",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-deposit",
    "sheet": "퇴직연금 예수금조회",
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
        "element": "dnca_tota",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nxdy_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nxdy_sttl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nx2_day_sttl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTSC0009U",
    "name": "주식예약주문정정취소",
    "url": "/uapi/domestic-stock/v1/trading/order-resv-rvsecncl",
    "sheet": "주식예약주문정정취소",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "0 : 성공 \r\n0 이외의 값 : 실패"
      },
      {
        "element": "msg_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "msg",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output",
        "type": "array",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nrml_prcs_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC8909R",
    "name": "신용매수가능조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-credit-psamount",
    "sheet": "신용매수가능조회",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "0 : 성공\r\n0 이외의 값 : 실패"
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
        "description": "응답메시지"
      },
      {
        "element": "output",
        "type": "object",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_cash",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_sbst",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ruse_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fund_rpch_chgs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "psbl_qty_calc_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nrcvb_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nrcvb_buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "max_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "max_buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cma_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovrs_re_use_amt_wcrc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_frcr_amt_wcrc",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0869R",
    "name": "주식통합증거금 현황",
    "url": "/uapi/domestic-stock/v1/trading/intgr-margin",
    "sheet": "주식통합증거금 현황",
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
        "element": "acmga_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "acmga_pct100_aptm_rson",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sbst_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_evlu_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_ruse_psbl_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fund_rpch_chgs_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg_rdpt_objt_atm",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bond_ruse_psbl_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sbst_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_evlu_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_ruse_psbl_amt_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fund_rpch_chgs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg_rdpt_amt_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bond_ruse_psbl_amt_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sbst_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_evlu_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_ruse_psbl_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fund_rpch_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bond_ruse_psbl_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rcvb_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_loan_grta_ruse_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash20_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash30_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash40_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash50_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash60_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash100_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_rsip100_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bond_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg45_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg50_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg60_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg70_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_stln_max_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "lmt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovrs_stck_itgr_mgna_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_ruse_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_ruse_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_ruse_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_ruse_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_ruse_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_ruse_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_ruse_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_ruse_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_ruse_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_ruse_objt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_ruse_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_ruse_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_gnrl_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_itgr_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_gnrl_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_itgr_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_gnrl_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_itgr_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_gnrl_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_itgr_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_cash20_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_cash30_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_cash40_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_cash50_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_cash60_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_cash100_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_100_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_fncg45_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_fncg50_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_fncg60_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_fncg70_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_itgr_stln_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bond_itgr_ord_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_cash_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_sbst_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_evlu_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_re_use_amt_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fund_rpch_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_fncg_rdpt_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bond_re_use_ovrs_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_re_use_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_re_use_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_re_use_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_re_use_oth_mket_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hgkg_cny_re_use_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "usd_frst_bltn_exrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hkd_frst_bltn_exrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "jpy_frst_bltn_exrt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cny_frst_bltn_exrt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC2201R",
    "name": "퇴직연금 미체결내역",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-daily-ccld",
    "sheet": "퇴직연금 미체결내역",
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
        "element": "ord_gno_brno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_buy_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trad_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "odno",
        "type": "string",
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
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_ccld_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nccs_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_odno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_tmd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "objt_cust_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stpm_cndt_pric",
        "type": "string",
        "required": "Y",
        "description": "신규 API용 필드"
      },
      {
        "element": "stpm_efct_occr_dtmd",
        "type": "string",
        "required": "Y",
        "description": "신규 API용 필드"
      },
      {
        "element": "stpm_efct_occr_yn",
        "type": "string",
        "required": "Y",
        "description": "신규 API용 필드"
      },
      {
        "element": "excg_id_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": "신규 API용 필드"
      }
    ]
  },
  {
    "tr_id": "TTTC8715R",
    "name": "기간별매매손익현황조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-period-trade-profit",
    "sheet": "기간별매매손익현황조회",
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
        "element": "ctx_area_nk100",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ctx_area_fk100",
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
        "element": "trad_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": "종목번호(뒤 6자리만 해당)"
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trad_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hldg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rlzt_pfls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pfls_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fee",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tl_tax",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_int",
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
        "element": "sll_qty_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_tr_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_fee_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_tltx_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_excc_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buyqty_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_tr_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_fee_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_tax_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_excc_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_tr_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_fee",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_tltx",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_rlzt_pfls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_int",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_pftrt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0013U",
    "name": "주식주문(정정취소)",
    "url": "/uapi/domestic-stock/v1/trading/order-rvsecncl",
    "sheet": "주식주문(정정취소)",
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
        "description": "single"
      },
      {
        "element": "krx_fwdg_ord_orgno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "odno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_tmd",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTSC0004R",
    "name": "주식예약주문조회",
    "url": "/uapi/domestic-stock/v1/trading/order-resv-ccnl",
    "sheet": "주식예약주문조회",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "0 : 성공 \r\n0 이외의 값 : 실패"
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
        "type": "array",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rsvn_ord_seq",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "rsvn_ord_ord_dt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "rsvn_ord_rcit_dt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "pdno",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ord_dvsn_cd",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ord_rsvn_qty",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "tot_ccld_qty",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "cncl_ord_dt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ord_tmd",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ctac_tlno",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "rjct_rson2",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "odno",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "rsvn_ord_rcit_tmd",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "kor_item_shtn_name",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "sll_buy_dvsn_cd",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ord_rsvn_unpr",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "tot_ccld_amt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "loan_dt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "cncl_rcit_tmd",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "prcs_rslt",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "ord_dvsn_name",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "tmnl_mdia_kind_cd",
        "type": "string",
        "required": "N",
        "description": ""
      },
      {
        "element": "rsvn_end_dt",
        "type": "string",
        "required": "N",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0503R",
    "name": "퇴직연금 매수가능조회",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-psbl-order",
    "sheet": "퇴직연금 매수가능조회",
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
        "element": "ord_psbl_cash",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ruse_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "psbl_qty_calc_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "max_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "max_buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC8434R",
    "name": "주식잔고조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-balance",
    "sheet": "주식잔고조회",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "0 : 성공\r\n0 이외의 값 : 실패"
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
        "element": "ctx_area_fk100",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ctx_area_nk100",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "output1",
        "type": "object array",
        "required": "Y",
        "description": "Array"
      },
      {
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": "종목번호(뒷 6자리)"
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": "종목명"
      },
      {
        "element": "trad_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": "매수매도구분"
      },
      {
        "element": "bfdy_buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_buyqty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hldg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": "매입금액 / 보유수량"
      },
      {
        "element": "pchs_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": "평가금액 - 매입금액"
      },
      {
        "element": "evlu_pfls_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_erng_rt",
        "type": "string",
        "required": "Y",
        "description": "미사용항목(0으로 출력)"
      },
      {
        "element": "loan_dt",
        "type": "string",
        "required": "Y",
        "description": "INQR_DVSN(조회구분)을 01(대출일별)로 설정해야 값이 나옴"
      },
      {
        "element": "loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stln_slng_chgs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "expd_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fltt_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_cprs_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "item_mgna_rt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "grta_rt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sbst_pric",
        "type": "string",
        "required": "Y",
        "description": "증권매매의 위탁보증금으로서 현금 대신에 사용되는 유가증권 가격"
      },
      {
        "element": "stck_loan_unpr",
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
        "element": "dnca_tot_amt",
        "type": "string",
        "required": "Y",
        "description": "예수금"
      },
      {
        "element": "nxdy_excc_amt",
        "type": "string",
        "required": "Y",
        "description": "D+1 예수금"
      },
      {
        "element": "prvs_rcdl_excc_amt",
        "type": "string",
        "required": "Y",
        "description": "D+2 예수금"
      },
      {
        "element": "cma_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nxdy_auto_rdpt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d2_auto_rdpt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_tlex_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_tlex_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scts_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": "유가증권 평가금액 합계금액 + D+2 예수금"
      },
      {
        "element": "nass_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fncg_gld_auto_rdpt_yn",
        "type": "string",
        "required": "Y",
        "description": "보유현금에 대한 융자금만 차감여부\r\n신용융자 매수체결 시점에서는 융자비율을 매매대금 100%로 계산 하였다가 수도결제일에 보증금에 해당하는 금액을 고객의 현금으로 충당하여 융자금을 감소시키는 업무"
      },
      {
        "element": "pchs_amt_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": "유가증권 평가금액 합계금액"
      },
      {
        "element": "evlu_pfls_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_stln_slng_chgs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_tot_asst_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "asst_icdc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "asst_icdc_erng_rt",
        "type": "string",
        "required": "Y",
        "description": "데이터 미제공"
      }
    ]
  },
  {
    "tr_id": "TTTC2202R",
    "name": "퇴직연금 체결기준잔고",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-present-balance",
    "sheet": "퇴직연금 체결기준잔고",
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
        "description": "Array"
      },
      {
        "element": "cblc_dvsn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cblc_dvsn_name",
        "type": "string",
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
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hldg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "slpsb_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cblc_weit",
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
        "element": "pchs_amt_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "trad_pfls_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_tot_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pftrt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC8908R",
    "name": "매수가능조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-psbl-order",
    "sheet": "매수가능조회",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "0 : 성공\r\n0 이외의 값 : 실패"
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
        "type": "object",
        "required": "Y",
        "description": "Single"
      },
      {
        "element": "ord_psbl_cash",
        "type": "string",
        "required": "Y",
        "description": "예수금으로 계산된 주문가능금액"
      },
      {
        "element": "ord_psbl_sbst",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ruse_psbl_amt",
        "type": "string",
        "required": "Y",
        "description": "전일/금일 매도대금으로 계산된 주문가능금액"
      },
      {
        "element": "fund_rpch_chgs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "psbl_qty_calc_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nrcvb_buy_amt",
        "type": "string",
        "required": "Y",
        "description": "미수를 사용하지 않으실 경우 nrcvb_buy_amt(미수없는매수금액)을 확인"
      },
      {
        "element": "nrcvb_buy_qty",
        "type": "string",
        "required": "Y",
        "description": "미수를 사용하지 않으실 경우 nrcvb_buy_qty(미수없는매수수량)을 확인\r\n\r\n* 특정 종목 전량매수 시 가능수량을 확인하실 경우\r\n  조회 시 ORD_DVSN:01(시장가)로 지정 필수\r\n* 다만, 조건부지정가 등 특정 주문구분(ex.IOC)으로 주문 시 가능수량을 확인할 경우 주문 시와 동일한 주문구분(ex.IOC) 입력"
      },
      {
        "element": "max_buy_amt",
        "type": "string",
        "required": "Y",
        "description": "미수를 사용하시는 경우 max_buy_amt(최대매수금액)를 확인"
      },
      {
        "element": "max_buy_qty",
        "type": "string",
        "required": "Y",
        "description": "미수를 사용하시는 경우 max_buy_qty(최대매수수량)를 확인\r\n\r\n* 특정 종목 전량매수 시 가능수량을 확인하실 경우\r\n  조회 시 ORD_DVSN:01(시장가)로 지정 필수\r\n* 다만, 조건부지정가 등 특정 주문구분(ex.IOC)으로 주문 시 가능수량을 확인할 경우 주문 시와 동일한 주문구분(ex.IOC) 입력"
      },
      {
        "element": "cma_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ovrs_re_use_amt_wcrc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_frcr_amt_wcrc",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC8708R",
    "name": "기간별손익일별합산조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-period-profit",
    "sheet": "기간별손익일별합산조회",
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
        "element": "trad_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rlzt_pfls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fee",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_int",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tl_tax",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pfls_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_qty1",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_qty1",
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
        "element": "sll_qty_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_tr_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_fee_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_tltx_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_excc_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_qty_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_tr_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_fee_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_tax_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "buy_excc_amt_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_tr_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_fee",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_tltx",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_rlzt_pfls",
        "type": "string",
        "required": "Y",
        "description": "※ HTS[0856] 기간별 매매손익 '일별' 화면의 우측 하단 '총손익률' 항목은 \r\n기간별매매손익현황조회(TTTC8715R) > output2 > tot_pftrt(총수익률) 으로 확인 가능"
      },
      {
        "element": "loan_int",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0011U",
    "name": "주식주문(현금)",
    "url": "/uapi/domestic-stock/v1/trading/order-cash",
    "sheet": "주식주문(현금)",
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
        "description": "single"
      },
      {
        "element": "KRX_FWDG_ORD_ORGNO",
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
        "element": "ORD_TMD",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC8408R",
    "name": "매도가능수량조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-psbl-sell",
    "sheet": "매도가능수량조회",
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
        "element": "buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cblc_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nsvg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "now_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0081R",
    "name": "주식일별주문체결조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-daily-ccld",
    "sheet": "주식일별주문체결조회",
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
        "element": "ord_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_gno_brno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "odno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "orgn_odno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_buy_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "sll_buy_dvsn_cd_name",
        "type": "string",
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
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_tmd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_ccld_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "avg_prvs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cncl_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_ccld_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ordr_empno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cnc_cfrm_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rmn_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rjct_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ccld_cndt_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "inqr_ip_addr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cpbc_ordp_ord_rcit_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cpbc_ordp_infm_mthd_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "infm_tmd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ctac_tlno",
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
        "element": "excg_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cpbc_ordp_mtrl_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_orgno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rsvn_ord_end_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "excg_id_dvsn_Cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stpm_cndt_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stpm_efct_occr_dtmd",
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
        "element": "tot_ord_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_ccld_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_ccld_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prsm_tlex_smtl",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0084R",
    "name": "주식정정취소가능주문조회",
    "url": "/uapi/domestic-stock/v1/trading/inquire-psbl-rvsecncl",
    "sheet": "주식정정취소가능주문조회",
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
        "element": "ord_gno_brno",
        "type": "string",
        "required": "Y",
        "description": "주문시 한국투자증권 시스템에서 지정된 영업점코드"
      },
      {
        "element": "odno",
        "type": "string",
        "required": "Y",
        "description": "주문시 한국투자증권 시스템에서 채번된 주문번호"
      },
      {
        "element": "orgn_odno",
        "type": "string",
        "required": "Y",
        "description": "정정/취소주문 인경우 원주문번호"
      },
      {
        "element": "ord_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": "종목번호(뒤 6자리만 해당)"
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": "종목명"
      },
      {
        "element": "rvse_cncl_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": "정정 또는 취소 여부 표시"
      },
      {
        "element": "ord_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_unpr",
        "type": "string",
        "required": "Y",
        "description": "1주당 주문가격"
      },
      {
        "element": "ord_tmd",
        "type": "string",
        "required": "Y",
        "description": "주문시각(시분초HHMMSS)"
      },
      {
        "element": "tot_ccld_qty",
        "type": "string",
        "required": "Y",
        "description": "주문 수량 중 체결된 수량"
      },
      {
        "element": "tot_ccld_amt",
        "type": "string",
        "required": "Y",
        "description": "주문금액 중 체결금액"
      },
      {
        "element": "psbl_qty",
        "type": "string",
        "required": "Y",
        "description": "정정/취소 주문 가능 수량"
      },
      {
        "element": "sll_buy_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": "01 : 매도 / 02 : 매수"
      },
      {
        "element": "ord_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": "[KRX]\r\n00 : 지정가\r\n01 : 시장가\r\n02 : 조건부지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n05 : 장전 시간외\r\n06 : 장후 시간외\r\n07 : 시간외 단일가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[NXT]\r\n00 : 지정가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)\r\n21 : 중간가\r\n22 : 스톱지정가\r\n23 : 중간가IOC\r\n24 : 중간가FOK\r\n\r\n[SOR]\r\n00 : 지정가\r\n01 : 시장가\r\n03 : 최유리지정가\r\n04 : 최우선지정가\r\n11 : IOC지정가 (즉시체결,잔량취소)\r\n12 : FOK지정가 (즉시체결,전량취소)\r\n13 : IOC시장가 (즉시체결,잔량취소)\r\n14 : FOK시장가 (즉시체결,전량취소)\r\n15 : IOC최유리 (즉시체결,잔량취소)\r\n16 : FOK최유리 (즉시체결,전량취소)"
      },
      {
        "element": "mgco_aptm_odno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "excg_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "excg_id_dvsn_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "excg_id_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stpm_cndt_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stpm_efct_occr_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "CTSC0008U",
    "name": "주식예약주문",
    "url": "/uapi/domestic-stock/v1/trading/order-resv",
    "sheet": "주식예약주문",
    "fields": [
      {
        "element": "rt_cd",
        "type": "string",
        "required": "Y",
        "description": "0 : 성공 \r\n0 이외의 값 : 실패"
      },
      {
        "element": "msg_cd",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "msg",
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
        "element": "rsvn_ord_seq",
        "type": "string",
        "required": "N",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC0051U",
    "name": "주식주문(신용)",
    "url": "/uapi/domestic-stock/v1/trading/order-credit",
    "sheet": "주식주문(신용)",
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
        "description": "single"
      },
      {
        "element": "krx_fwdg_ord_orgno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "odno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_tmd",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC2208R",
    "name": "퇴직연금 잔고조회",
    "url": "/uapi/domestic-stock/v1/trading/pension/inquire-balance",
    "sheet": "퇴직연금 잔고조회",
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
        "description": "Array"
      },
      {
        "element": "cblc_dvsn_name",
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
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "item_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_buyqty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hldg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_erng_rt",
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
        "element": "dnca_tot_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nxdy_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prvs_rcdl_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_tlex_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scts_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  },
  {
    "tr_id": "TTTC8494R",
    "name": "주식잔고조회_실현손익",
    "url": "/uapi/domestic-stock/v1/trading/inquire-balance-rlz-pl",
    "sheet": "주식잔고조회_실현손익",
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
        "description": "Array"
      },
      {
        "element": "pdno",
        "type": "string",
        "required": "Y",
        "description": "종목번호(뒷 6자리)"
      },
      {
        "element": "prdt_name",
        "type": "string",
        "required": "Y",
        "description": "종목명"
      },
      {
        "element": "trad_dvsn_name",
        "type": "string",
        "required": "Y",
        "description": "매수매도구분"
      },
      {
        "element": "bfdy_buy_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_buyqty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_sll_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "hldg_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "ord_psbl_qty",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_avg_pric",
        "type": "string",
        "required": "Y",
        "description": "매입금액 / 보유수량"
      },
      {
        "element": "pchs_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_amt",
        "type": "string",
        "required": "Y",
        "description": "평가금액 - 매입금액"
      },
      {
        "element": "evlu_pfls_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_erng_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stln_slng_chgs",
        "type": "string",
        "required": "Y",
        "description": "신용 거래에서, 고객이 증권 회사로부터 대부받은 주식의 매각 대금"
      },
      {
        "element": "expd_dt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "stck_loan_unpr",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_cprs_icdc",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fltt_rt",
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
        "element": "dnca_tot_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nxdy_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "prvs_rcdl_excc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "cma_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_buy_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nxdy_auto_rdpt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_sll_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "d2_auto_rdpt_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_tlex_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "thdt_tlex_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_loan_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "scts_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "nass_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "fncg_gld_auto_rdpt_yn",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "pchs_amt_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_amt_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "evlu_pfls_smtl_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "tot_stln_slng_chgs",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "bfdy_tot_asst_evlu_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "asst_icdc_amt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "asst_icdc_erng_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rlzt_pfls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "rlzt_erng_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "real_evlu_pfls",
        "type": "string",
        "required": "Y",
        "description": ""
      },
      {
        "element": "real_evlu_pfls_erng_rt",
        "type": "string",
        "required": "Y",
        "description": ""
      }
    ]
  }
]"""


def load_trading_response_specs() -> list[dict[str, Any]]:
    return json.loads(_RESPONSE_SPECS_JSON)


TRADING_API_RESPONSE_SPECS = load_trading_response_specs()
TRADING_API_RESPONSE_SPECS_BY_TR_ID = {
    str(spec.get("tr_id", "")): spec for spec in TRADING_API_RESPONSE_SPECS if spec.get("tr_id")
}
