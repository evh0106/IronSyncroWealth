"""OAuth2 API 응답 스펙 정의."""

OAUTH2_RESPONSE_SPECS = {
    'au10001': [
        {'element': 'expires_dt',   'label': '만료일',    'type': 'String', 'description': ''},
        {'element': 'token_type',   'label': '토큰타입',  'type': 'String', 'description': ''},
        {'element': 'token',        'label': '접근토큰',  'type': 'String', 'description': ''},
        {'element': 'return_code',  'label': '리턴코드',  'type': 'String', 'description': '0: 정상'},
        {'element': 'return_msg',   'label': '리턴메시지','type': 'String', 'description': ''},
    ],
    'au10002': [
        {'element': 'return_code',  'label': '리턴코드',  'type': 'String', 'description': '0: 정상'},
        {'element': 'return_msg',   'label': '리턴메시지','type': 'String', 'description': ''},
    ],
}
