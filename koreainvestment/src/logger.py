import os
import json
from datetime import datetime

_LOG_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'log'))


def _as_text(data) -> str:
    if data is None:
        return ''
    if isinstance(data, bytes):
        return data.decode('utf-8', errors='replace')
    return str(data)


def _write_headers(f, headers):
    if not headers:
        f.write('(none)\n')
        return
    for k, v in headers.items():
        f.write(f'{k}: {v}\n')


def _get_log_path(log_name: str = 'koreainvestment') -> str:
    os.makedirs(_LOG_DIR, exist_ok=True)
    fname = datetime.now().strftime('%Y%m%d') + f'_{log_name}.log'
    return os.path.join(_LOG_DIR, fname)


def log_http_request(api_id: str, url: str, request_headers, request_body,
                     log_name: str = 'koreainvestment') -> tuple[str, str]:
    """요청 직전에 헤더/JSON 원문을 즉시 append 저장"""
    path = _get_log_path(log_name)
    req_id = datetime.now().strftime('%Y%m%d%H%M%S%f')
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    req_body_text = _as_text(request_body)

    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'[{ts}] [{req_id}] api-id={api_id} url={url}\n')
        f.write('[request headers]\n')
        _write_headers(f, request_headers)
        f.write('[request json raw]\n')
        f.write(req_body_text)
        if not req_body_text.endswith('\n'):
            f.write('\n')
        f.write('\n')

    return path, req_id


def log_http_response(req_id: str, response_status: int, response_headers, response_body,
                      log_name: str = 'koreainvestment') -> str:
    """응답 수신 직후 헤더/JSON 원문을 즉시 append 저장"""
    path = _get_log_path(log_name)

    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    res_body_text = _as_text(response_body)

    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'[{ts}] [{req_id}]\n')
        f.write(f'[response status] {response_status}\n')
        f.write('[response headers]\n')
        _write_headers(f, response_headers)
        f.write('[response json raw]\n')
        f.write(res_body_text)
        if not res_body_text.endswith('\n'):
            f.write('\n')
        f.write('\n')

    return path


def log_websocket_message(message, direction: str = 'recv') -> str:
    """WebSocket 메시지를 날짜_websocket.log 파일에 append 저장"""
    path = _get_log_path('websocket')
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if isinstance(message, (dict, list)):
        payload = json.dumps(message, ensure_ascii=False, indent=2)
    else:
        payload = _as_text(message)

    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'[{ts}] [{direction}]\n')
        f.write(payload)
        if not payload.endswith('\n'):
            f.write('\n')
        f.write('\n')

    return path
