"""OAuth2 API 요청 스펙 정의."""

OAUTH2_API_SPECS = [
    {
        'api_id': 'au10001',
        'name': '접근토큰 발급',
        'url': '/oauth2/token',
        'overview': '앱키와 시크릿키로 접근토큰을 발급받습니다.',
        'fields': [
            {'element': 'grant_type', 'label': 'grant_type', 'required': True, 'description': 'client_credentials 입력'},
            {'element': 'appkey',     'label': '앱키',        'required': True, 'description': ''},
            {'element': 'secretkey',  'label': '시크릿키',    'required': True, 'description': ''},
        ],
        'request_example': {
            'grant_type': 'client_credentials',
            'appkey': 'AxserEsdcredca.....',
            'secretkey': 'SEefdcwcforehDre2fdvc....',
        },
    },
    {
        'api_id': 'au10002',
        'name': '접근토큰폐기',
        'url': '/oauth2/revoke',
        'overview': '발급된 접근토큰을 폐기합니다.',
        'fields': [
            {'element': 'appkey',    'label': '앱키',     'required': True, 'description': ''},
            {'element': 'secretkey', 'label': '시크릿키', 'required': True, 'description': ''},
            {'element': 'token',     'label': '접근토큰', 'required': True, 'description': ''},
        ],
        'request_example': {
            'appkey': 'AxserEsdcredca.....',
            'secretkey': 'SEefdcwcforehDre2fdvc....',
            'token': 'WQJCwyqInphKnR3bSRtB9NE1lv...',
        },
    },
]
