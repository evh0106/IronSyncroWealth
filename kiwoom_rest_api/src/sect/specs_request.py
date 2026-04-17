"""정적 업종 API 요청 스펙 정의.

URL: /api/dostk/sect
메뉴: 국내주식 > 업종
"""

SECT_API_SPECS = [
    {
        'api_id': 'ka20001',
        'name': '업종현재가요청',
        'overview': '업종코드별 현재가·전일대비·등락률 등을 조회합니다.',
        'url': '/api/dostk/sect',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '0:코스피, 1:코스닥, 2:코스피200',
            },
            {
                'element': 'sect_cd',
                'label': '업종코드',
                'required': True,
                'description': (
                    '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주, '
                    '101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701:KRX100'
                ),
            },
        ],
        'request_example': {'mrkt_tp': '0', 'sect_cd': '001'},
    },
    {
        'api_id': 'ka20002',
        'name': '업종별주가요청',
        'overview': '업종에 속한 종목별 주가 정보를 조회합니다.',
        'url': '/api/dostk/sect',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '0:코스피, 1:코스닥, 2:코스피200',
            },
            {
                'element': 'sect_cd',
                'label': '업종코드',
                'required': True,
                'description': (
                    '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주, '
                    '101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701:KRX100'
                ),
            },
            {
                'element': 'stex_tp',
                'label': '거래소구분',
                'required': True,
                'description': '1:KRX, 2:NXT, 3:통합',
            },
        ],
        'request_example': {'mrkt_tp': '0', 'sect_cd': '001', 'stex_tp': '3'},
    },
    {
        'api_id': 'ka20003',
        'name': '전업종지수요청',
        'overview': '전체 업종 지수를 한 번에 조회합니다.',
        'url': '/api/dostk/sect',
        'fields': [
            {
                'element': 'sect_cd',
                'label': '업종코드',
                'required': True,
                'description': '001:종합(KOSPI), 101:종합(KOSDAQ)',
            },
        ],
        'request_example': {'sect_cd': '001'},
    },
    {
        'api_id': 'ka20009',
        'name': '업종현재가일별요청',
        'overview': '업종현재가 일별 데이터를 조회합니다.',
        'url': '/api/dostk/sect',
        'fields': [
            {
                'element': 'mrkt_tp',
                'label': '시장구분',
                'required': True,
                'description': '0:코스피, 1:코스닥, 2:코스피200',
            },
            {
                'element': 'sect_cd',
                'label': '업종코드',
                'required': True,
                'description': (
                    '001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주, '
                    '101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701:KRX100'
                ),
            },
        ],
        'request_example': {'mrkt_tp': '0', 'sect_cd': '001'},
    },
]
