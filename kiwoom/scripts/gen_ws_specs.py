"""파싱된 JSON으로 specs_request.py / specs_response.py 생성"""
import json

d = json.load(open('doc/ws_parsed.json', encoding='utf-8'))

API_NAMES = {
    '00': '주문체결',
    '04': '잔고',
    '0A': '주식기세',
    '0B': '주식체결',
    '0C': '주식우선호가',
    '0D': '주식호가잔량',
    '0E': '주식시간외호가',
    '0F': '주식당일거래원',
    '0G': 'ETF NAV',
    '0H': '주식예상체결',
    '0I': '국제금환산가격',
    '0J': '업종지수',
    '0U': '업종등락',
    '0g': '주식종목정보',
    '0m': 'ELW 이론가',
    '0s': '장시작시간',
    '0u': 'ELW 지표',
    '0w': '종목프로그램매매',
    'ka10171': '조건검색 목록조회',
    'ka10172': '조건검색 요청 일반',
    'ka10173': '조건검색 요청 실시간',
    'ka10174': '조건검색 실시간 해제',
}

# --- specs_request.py ---
lines = [
    "# WebSocket API 요청 스펙 정의",
    "# 각 항목: api_id, name, overview, fields, request_example",
    "",
    "WEBSOCKET_API_SPECS = [",
]

for api_id, info in d.items():
    name = API_NAMES.get(api_id, api_id)
    overview = info['overview'].replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ').replace('\r', '')
    
    # 공통 필드 (trnm, grp_no, refresh, data)
    common_fields = [
        {'element': 'trnm', 'label': '서비스명', 'required': True,
         'description': 'REG:등록, REMOVE:해지'},
        {'element': 'grp_no', 'label': '그룹번호', 'required': True, 'description': ''},
        {'element': 'refresh', 'label': '기존등록유지여부', 'required': True,
         'description': '1:유지, 0:해제'},
        {'element': 'data', 'label': '실시간 등록 리스트', 'required': True, 'description': ''},
    ]
    extra_fields = info['request']

    lines.append("    {")
    lines.append(f"        'api_id': '{api_id}',")
    lines.append(f"        'name': '{name}',")
    lines.append(f"        'overview': '{overview}',")
    lines.append("        'fields': [")
    for f in common_fields:
        req = 'True' if f['required'] else 'False'
        desc = f['description'].replace("'", "\\'")
        lines.append(f"            {{'element': '{f['element']}', 'label': '{f['label']}', 'required': {req}, 'description': '{desc}'}},")
    for f in extra_fields:
        req = 'True' if f['required'] else 'False'
        desc = f['description'].replace('\n', ' ').replace("'", "\\'")
        label = f['label'].replace("'", "\\'")
        lines.append(f"            {{'element': '{f['element']}', 'label': '{label}', 'required': {req}, 'description': '{desc}'}},")
    lines.append("        ],")
    
    ex = info['request_example']
    if ex:
        lines.append(f"        'request_example': {json.dumps(ex, ensure_ascii=False)},")
    else:
        lines.append(f"        'request_example': {{'trnm': 'REG', 'grp_no': '1', 'refresh': '1', 'data': [{{'item': [], 'type': ['{api_id}']}}]}},")
    lines.append("    },")

lines.append("]")
lines.append("")

with open('src/websocket/specs_request.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print("specs_request.py 생성 완료")

# --- specs_response.py ---
lines2 = [
    "# WebSocket API 응답 스펙 정의",
    "# 키: api_id, 값: 응답 필드 리스트",
    "",
    "WEBSOCKET_RESPONSE_SPECS = {",
]

for api_id, info in d.items():
    # 공통 응답 필드
    common = [
        {'element': 'trnm', 'label': '서비스명', 'type': 'String', 'description': ''},
        {'element': 'return_code', 'label': '결과코드', 'type': 'String', 'description': ''},
        {'element': 'return_msg', 'label': '결과메시지', 'type': 'String', 'description': ''},
        {'element': 'data', 'label': '실시간 데이터 리스트', 'type': 'LIST', 'description': ''},
    ]
    res_fields = info['response']
    lines2.append(f"    '{api_id}': [")
    for f in common:
        desc = f['description'].replace("'", "\\'")
        lines2.append(f"        {{'element': '{f['element']}', 'label': '{f['label']}', 'type': '{f['type']}', 'description': '{desc}'}},")
    for f in res_fields:
        desc = f['description'].replace('\n', ' ').replace("'", "\\'")
        label = f['label'].replace("'", "\\'")
        lines2.append(f"        {{'element': '{f['element']}', 'label': '{label}', 'type': '{f['type']}', 'description': '{desc}'}},")
    lines2.append("    ],")

lines2.append("}")
lines2.append("")

with open('src/websocket/specs_response.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines2))
print("specs_response.py 생성 완료")
