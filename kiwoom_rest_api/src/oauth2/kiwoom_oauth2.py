"""
키움증권 OAuth2 공통 모듈
- conf에서 앱키/시크릿키 로드
- 접근토큰 발급/폐기
"""

from pathlib import Path
import json

import requests

from .specs_request import OAUTH2_API_SPECS
from .specs_response import OAUTH2_RESPONSE_SPECS

# api_id → 스펙 빠른 조회용 딕셔너리
_REQ_SPEC: dict = {s['api_id']: s for s in OAUTH2_API_SPECS}
_RES_SPEC: dict = OAUTH2_RESPONSE_SPECS

HOST = 'https://api.kiwoom.com'           # 실전투자 서버
# HOST = 'https://mockapi.kiwoom.com'         # 모의투자 서버 (KRX만 지원)


def _build_request_body(api_id: str, values: dict) -> dict:
    """specs_request의 fields 순서·키 기준으로 요청 body를 조립합니다."""
    spec = _REQ_SPEC[api_id]
    return {field['element']: values[field['element']] for field in spec['fields']}


def _print_response(response: requests.Response, api_id: str):
    """응답 코드·헤더·body를 출력합니다. specs_response의 한글 라벨을 참조합니다."""
    print('Code:', response.status_code)
    print('Header:', json.dumps(
        {key: response.headers.get(key) for key in ['next-key', 'cont-yn', 'api-id']},
        indent=4, ensure_ascii=False,
    ))

    body = response.json()
    res_fields = {f['element']: f['label'] for f in _RES_SPEC.get(api_id, [])}
    labeled = {res_fields.get(k, k): v for k, v in body.items()}
    print('Body:', json.dumps(labeled, indent=4, ensure_ascii=False))


def load_api_keys(host: str = HOST) -> tuple[str, str]:
    """HOST 설정에 맞는 앱키/시크릿키를 conf 디렉토리에서 읽어옵니다."""
    base_dir = Path(__file__).resolve().parents[2]
    conf_dir = base_dir / 'conf'

    if 'mockapi.kiwoom.com' in host:
        account_no = '81241972'
    else:
        account_no = '65120003'

    app_key_file = conf_dir / f'{account_no}_appkey.txt'
    secret_key_file = conf_dir / f'{account_no}_secretkey.txt'

    if not app_key_file.exists():
        raise FileNotFoundError(f'앱키 파일을 찾을 수 없습니다: {app_key_file}')
    if not secret_key_file.exists():
        raise FileNotFoundError(f'시크릿키 파일을 찾을 수 없습니다: {secret_key_file}')

    app_key = app_key_file.read_text(encoding='utf-8').strip()
    app_secret = secret_key_file.read_text(encoding='utf-8').strip()
    return app_key, app_secret


def get_access_token(app_key: str, app_secret: str, host: str = HOST) -> str:
    """OAuth 2.0 방식으로 액세스 토큰을 발급받습니다."""
    spec = _REQ_SPEC['au10001']
    url = host + spec['url']

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }

    data = _build_request_body('au10001', {
        'grant_type': 'client_credentials',
        'appkey': app_key,
        'secretkey': app_secret,
    })

    response = requests.post(url, headers=headers, json=data)
    _print_response(response, 'au10001')

    result = response.json()
    if result.get('return_code') == 0:
        access_token = result.get('token')
        print(f'토큰 발급 성공 (만료일: {result.get("expires_dt")})')
        return access_token

    print(f'토큰 발급 실패: {result.get("return_msg")}')
    raise Exception('토큰 발급에 실패했습니다.')


def revoke_access_token(app_key: str, app_secret: str, token: str, host: str = HOST):
    """발급된 접근토큰을 폐기합니다. [au10002]"""
    spec = _REQ_SPEC['au10002']
    url = host + spec['url']

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }

    data = _build_request_body('au10002', {
        'appkey': app_key,
        'secretkey': app_secret,
        'token': token,
    })

    response = requests.post(url, headers=headers, json=data)
    _print_response(response, 'au10002')

    result = response.json()
    if result.get('return_code') == 0:
        print('토큰 폐기 성공')
    else:
        print(f'토큰 폐기 실패: {result.get("return_msg")}')

    return response
