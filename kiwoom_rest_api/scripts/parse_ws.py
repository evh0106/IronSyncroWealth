"""Excel에서 websocket API 스펙을 파싱하여 JSON으로 출력합니다."""
import openpyxl
import json
import sys

wb = openpyxl.load_workbook(
    'doc/키움 REST API 문서.xlsx', read_only=True, data_only=True
)

WS_SHEETS = [
    ('00',      '주문체결(00)'),
    ('04',      '잔고(04)'),
    ('0A',      '주식기세(0A)'),
    ('0B',      '주식체결(0B)'),
    ('0C',      '주식우선호가(0C)'),
    ('0D',      '주식호가잔량(0D)'),
    ('0E',      '주식시간외호가(0E)'),
    ('0F',      '주식당일거래원(0F)'),
    ('0G',      'ETF NAV(0G)'),
    ('0H',      '주식예상체결(0H)'),
    ('0I',      '국제금환산가격(0I)'),
    ('0J',      '업종지수(0J)'),
    ('0U',      '업종등락(0U)'),
    ('0g',      '주식종목정보(0g)'),
    ('0m',      'ELW 이론가(0m)'),
    ('0s',      '장시작시간(0s)'),
    ('0u',      'ELW 지표(0u)'),
    ('0w',      '종목프로그램매매(0w)'),
    ('ka10171', '조건검색 목록조회(ka10171)'),
    ('ka10172', '조건검색 요청 일반(ka10172)'),
    ('ka10173', '조건검색 요청 실시간(ka10173)'),
    ('ka10174', '조건검색 실시간 해제(ka10174)'),
]

# 헤더 행에서 제외할 Body Element 값
SKIP_ELEMENTS = {'Element', 'api-id', 'authorization', 'cont-yn', 'next-key',
                 'cont_yn', 'next_key', 'trnm', 'grp_no', 'refresh', 'data',
                 'return_code', 'return_msg'}

result = {}
for api_id, sheet_name in WS_SHEETS:
    ws = wb[sheet_name]
    rows = [r for r in ws.iter_rows(values_only=True) if any(c for c in r if c)]

    # 개요 추출
    overview = ''
    for i, r in enumerate(rows):
        if r[0] and str(r[0]).strip() == '개요':
            for r2 in rows[i + 1:]:
                s = str(r2[0] or r2[1] or r2[2] or '').strip()
                if s in ('Request', 'Response', 'API 정보', '기본정보', '개요', ''):
                    if s in ('Request', 'Response'):
                        break
                    continue
                overview = s
                break
            break

    # Request / Response Body 필드 파싱
    req_fields, res_fields = [], []
    req_example = {}
    section = None
    table_started = False

    for r in rows:
        label = str(r[0]).strip() if r[0] else ''

        if label == 'Request':
            section = 'req'
            table_started = False
            continue
        if label == 'Response':
            section = 'res'
            table_started = False
            continue
        if label == 'Request Example':
            section = 'reqex'
            continue
        if label == 'Response Example':
            section = 'resex'
            continue

        if section in ('req', 'res'):
            group = str(r[0]).strip() if r[0] else ''
            elem  = str(r[1]).strip() if r[1] else ''
            hn    = str(r[2]).strip() if r[2] else ''
            tp    = str(r[3]).strip() if r[3] else 'String'
            req_r = str(r[4]).strip() if r[4] else 'N'
            desc  = str(r[6]).strip() if r[6] else ''

            # 헤더 행 감지
            if elem == 'Element':
                table_started = True
                continue
            if not table_started:
                continue
            # Body 행만 수집 (Header 스킵, 공통 필드 스킵)
            if group == 'Header':
                continue
            if not elem or elem in SKIP_ELEMENTS:
                continue

            entry = {
                'element': elem,
                'label': hn,
                'type': tp,
                'required': req_r == 'Y',
                'description': desc,
            }
            if section == 'req':
                req_fields.append(entry)
            else:
                res_fields.append(entry)

        if section == 'reqex' and r[0]:
            raw = str(r[0]).strip()
            if raw.startswith('{'):
                try:
                    req_example = json.loads(raw)
                except Exception:
                    # 작은따옴표 JSON 처리
                    try:
                        req_example = json.loads(raw.replace("'", '"'))
                    except Exception:
                        req_example = {}

    result[api_id] = {
        'overview': overview,
        'request': req_fields,
        'response': res_fields,
        'request_example': req_example,
    }

with open('doc/ws_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Done. Keys:', list(result.keys()))
