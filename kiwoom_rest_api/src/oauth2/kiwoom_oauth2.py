"""
키움증권 OAuth2 공통 모듈
- conf에서 앱키/시크릿키 로드
- 접근토큰 발급/폐기
"""

from pathlib import Path
import json

import requests

HOST = 'https://api.kiwoom.com'           # 실전투자 서버
# HOST = 'https://mockapi.kiwoom.com'         # 모의투자 서버 (KRX만 지원)


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
    url = host + '/oauth2/token'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }

    data = {
        'grant_type': 'client_credentials',
        'appkey': app_key,
        'secretkey': app_secret,
    }

    response = requests.post(url, headers=headers, json=data)

    print('Code:', response.status_code)
    print('Header:', json.dumps({key: response.headers.get(key) for key in ['next-key', 'cont-yn', 'api-id']}, indent=4, ensure_ascii=False))
    print('Body:', json.dumps(response.json(), indent=4, ensure_ascii=False))

    result = response.json()
    if result.get('return_code') == 0:
        access_token = result.get('token')
        print(f'토큰 발급 성공 (만료일: {result.get("expires_dt")})')
        return access_token

    print(f'토큰 발급 실패: {result.get("return_msg")}')
    raise Exception('토큰 발급에 실패했습니다.')


def revoke_access_token(app_key: str, app_secret: str, token: str, host: str = HOST):
    """발급된 접근토큰을 폐기합니다. [au10002]"""
    url = host + '/oauth2/revoke'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
    }

    data = {
        'appkey': app_key,
        'secretkey': app_secret,
        'token': token,
    }

    response = requests.post(url, headers=headers, json=data)

    print('Code:', response.status_code)
    print('Header:', json.dumps({key: response.headers.get(key) for key in ['next-key', 'cont-yn', 'api-id']}, indent=4, ensure_ascii=False))
    print('Body:', json.dumps(response.json(), indent=4, ensure_ascii=False))

    result = response.json()
    if result.get('return_code') == 0:
        print('토큰 폐기 성공')
    else:
        print(f'토큰 폐기 실패: {result.get("return_msg")}')

    return response
