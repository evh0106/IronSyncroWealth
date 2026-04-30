"""OAuth2 response specs for Korea Investment Open API."""

OAUTH2_RESPONSE_SPECS = {
    "ka10001": [
        {"element": "access_token", "label": "access token", "type": "string", "description": "issued OAuth2 token"},
        {"element": "token_type", "label": "token type", "type": "string", "description": "usually Bearer"},
        {
            "element": "access_token_token_expired",
            "label": "access token expiry datetime",
            "type": "string",
            "description": "expiry datetime from API response",
        },
    ],
    "ka10002": [
        {"element": "code", "label": "result code", "type": "integer", "description": "0 when successful"},
        {"element": "message", "label": "result message", "type": "string", "description": "success or error message"},
    ],
    "ka10003": [
        {"element": "approval_key", "label": "approval key", "type": "string", "description": "websocket approval key"},
    ],
}
