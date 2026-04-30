"""OAuth2 request specs for Korea Investment Open API."""

OAUTH2_API_SPECS = [
    {
        "api_id": "ka10001",
        "name": "access token issue",
        "url": "/oauth2/tokenP",
        "overview": "Issue an access token with appkey and appsecret.",
        "fields": [
            {"element": "grant_type", "label": "grant_type", "required": True, "description": "client_credentials"},
            {"element": "appkey", "label": "appkey", "required": True, "description": "KIS appkey"},
            {"element": "appsecret", "label": "appsecret", "required": True, "description": "KIS appsecret"},
        ],
        "request_example": {
            "grant_type": "client_credentials",
            "appkey": "PSg5...",
            "appsecret": "yo2t...",
        },
    },
    {
        "api_id": "ka10002",
        "name": "access token revoke",
        "url": "/oauth2/revokeP",
        "overview": "Revoke an access token.",
        "fields": [
            {"element": "appkey", "label": "appkey", "required": True, "description": "KIS appkey"},
            {"element": "appsecret", "label": "appsecret", "required": True, "description": "KIS appsecret"},
            {"element": "token", "label": "token", "required": True, "description": "issued access token"},
        ],
        "request_example": {
            "appkey": "PSg5...",
            "appsecret": "yo2t...",
            "token": "eyJ0...",
        },
    },
    {
        "api_id": "ka10003",
        "name": "websocket approval key issue",
        "url": "/oauth2/Approval",
        "overview": "Issue a websocket approval key.",
        "fields": [
            {"element": "grant_type", "label": "grant_type", "required": True, "description": "client_credentials"},
            {"element": "appkey", "label": "appkey", "required": True, "description": "KIS appkey"},
            {"element": "secretkey", "label": "secretkey", "required": True, "description": "same value as appsecret"},
        ],
        "request_example": {
            "grant_type": "client_credentials",
            "appkey": "PSg5...",
            "secretkey": "yo2t...",
        },
    },
]
