"""Korea Investment OAuth2 common module."""

from __future__ import annotations

import json
from typing import Any

import requests

import db
from kis_config import load_config
from logger import log_http_request, log_http_response
from oauth2.specs_request import OAUTH2_API_SPECS
from oauth2.specs_response import OAUTH2_RESPONSE_SPECS


_REQ_SPEC: dict[str, dict[str, Any]] = {spec["api_id"]: spec for spec in OAUTH2_API_SPECS}
_RES_SPEC = OAUTH2_RESPONSE_SPECS


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------

def _get_valid_token(app_key: str) -> str | None:
    """DB에서 appkey 기준으로 유효한(미폐기·미만료) 액세스 토큰을 반환합니다."""
    conn = None
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            sql = """
                SELECT t.access_token
                FROM tokenP t
                LEFT JOIN revokeP r
                  ON r.req_appkey = t.req_appkey
                 AND r.req_token  = t.access_token
                 AND r.code = '0'
                WHERE t.req_appkey = %s
                  AND t.access_token <> ''
                  AND STR_TO_DATE(t.access_token_token_expired, '%%Y-%%m-%%d %%H:%%i:%%s') > NOW()
                  AND r.id IS NULL
                ORDER BY t.id DESC
                LIMIT 1
            """
            cur.execute(sql, (app_key,))
            row = cur.fetchone()
        if row:
            print('  [DB 조회] 유효한 액세스 토큰이 DB에 존재합니다.')
            return row['access_token']
        print('  [DB 조회] 유효한 액세스 토큰이 없습니다. 신규 발급합니다.')
        return None
    except Exception as exc:
        print(f'  [DB 조회 오류] 액세스 토큰 조회 실패: {exc}')
        return None
    finally:
        if conn is not None:
            conn.close()


def _save_token(app_key: str, app_secret: str, grant_type: str, response: dict[str, Any]) -> None:
    """tokenP 테이블에 액세스 토큰 발급 결과를 저장합니다."""
    conn = None
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            sql = """
                INSERT INTO tokenP
                (req_grant_type, req_appkey, req_appsecret, access_token, token_type,
                 access_token_token_expired)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (
                grant_type,
                app_key,
                app_secret,
                response.get('access_token', ''),
                response.get('token_type', ''),
                response.get('access_token_token_expired', ''),
            ))
        conn.commit()
        print('  [DB 저장] tokenP: 1행 저장됨')
    except Exception as exc:
        print(f'  [DB 저장 오류] tokenP: {exc}')
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def _save_revoke(app_key: str, app_secret: str, token: str, response: dict[str, Any]) -> None:
    """revokeP 테이블에 액세스 토큰 폐기 결과를 저장합니다."""
    conn = None
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            sql = """
                INSERT INTO revokeP
                (req_appkey, req_appsecret, req_token, code, message)
                VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(sql, (
                app_key,
                app_secret,
                token,
                response.get('code', ''),
                response.get('message', ''),
            ))
        conn.commit()
        print('  [DB 저장] revokeP: 1행 저장됨')
    except Exception as exc:
        print(f'  [DB 저장 오류] revokeP: {exc}')
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def _save_approval(app_key: str, app_secret: str, grant_type: str, response: dict[str, Any]) -> None:
    """Approval 테이블에 웹소켓 승인키 발급 결과를 저장합니다."""
    conn = None
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            sql = """
                INSERT INTO Approval
                (req_grant_type, req_appkey, req_secretkey, approval_key)
                VALUES (%s, %s, %s, %s)
            """
            cur.execute(sql, (
                grant_type,
                app_key,
                app_secret,
                response.get('approval_key', ''),
            ))
        conn.commit()
        print('  [DB 저장] Approval: 1행 저장됨')
    except Exception as exc:
        print(f'  [DB 저장 오류] Approval: {exc}')
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def _resolve_env_dv(env_dv: str | None, cfg: dict[str, Any]) -> str:
    return env_dv or cfg.get("env_dv", "real")


def _base_url(env_dv: str, cfg: dict[str, Any]) -> str:
    return cfg["my_url_vts"] if env_dv == "demo" else cfg["my_url"]


def _build_request_body(api_id: str, values: dict[str, str]) -> dict[str, str]:
    spec = _REQ_SPEC[api_id]
    return {field["element"]: values[field["element"]] for field in spec["fields"]}


def _print_response(response: requests.Response, api_id: str) -> None:
    print("Code:", response.status_code)
    print(
        "Header:",
        json.dumps(
            {key: response.headers.get(key) for key in ["content-type", "tr_id"]},
            indent=4,
            ensure_ascii=False,
        ),
    )

    body = response.json()
    labels = {field["element"]: field["label"] for field in _RES_SPEC.get(api_id, [])}
    labeled_body = {labels.get(key, key): value for key, value in body.items()}
    print("Body:", json.dumps(labeled_body, indent=4, ensure_ascii=False))


def load_api_keys() -> tuple[str, str]:
    """Load appkey and appsecret from kis_devlp.yaml based config."""
    cfg = load_config()
    return cfg["my_app"], cfg["my_sec"]


def get_cached_access_token(env_dv: str | None = None) -> dict[str, Any] | None:
    """DB에 저장된 유효한 액세스 토큰 정보를 반환합니다."""
    cfg = load_config()
    current_env = _resolve_env_dv(env_dv, cfg)
    cached = _get_valid_token(cfg["my_app"])
    if not cached:
        return None
    return {
        "access_token": cached,
        "token_type": "Bearer",
        "server_mode": current_env,
        "host": _base_url(current_env, cfg),
    }


def get_access_token(
    grant_type: str = "client_credentials",
    env_dv: str | None = None,
    reuse_cached: bool = True,
) -> dict[str, Any]:
    """액세스 토큰을 반환합니다.

    DB에 유효한(미폐기·미만료) 토큰이 있으면 그대로 반환하고,
    없으면 KIS API로 신규 발급 후 DB에 저장합니다.
    """
    cfg = load_config()
    current_env = _resolve_env_dv(env_dv, cfg)
    app_key = cfg["my_app"]

    if reuse_cached:
        cached = get_cached_access_token(current_env)
        if cached:
            return {**cached, "_from_cache": True}

    url = _base_url(current_env, cfg) + _REQ_SPEC["ka10001"]["url"]

    payload = _build_request_body(
        "ka10001",
        {
            "grant_type": grant_type,
            "appkey": app_key,
            "appsecret": cfg["my_sec"],
        },
    )
    headers = {"content-type": "application/json; charset=UTF-8"}

    session = requests.Session()
    req = requests.Request("POST", url, headers=headers, json=payload)
    preq = session.prepare_request(req)
    _, req_id = log_http_request(
        api_id="ka10001",
        url=url,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name="koreainvestment",
    )

    response = session.send(preq, timeout=15)
    log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name="koreainvestment",
    )
    response.raise_for_status()
    _print_response(response, "ka10001")
    data = response.json()
    _save_token(app_key, cfg["my_sec"], grant_type, data)
    return data


def revoke_access_token(token: str, env_dv: str | None = None) -> dict[str, Any]:
    """액세스 토큰을 폐기하고 결과를 DB에 저장합니다."""
    cfg = load_config()
    current_env = _resolve_env_dv(env_dv, cfg)
    url = _base_url(current_env, cfg) + _REQ_SPEC["ka10002"]["url"]

    payload = _build_request_body(
        "ka10002",
        {
            "appkey": cfg["my_app"],
            "appsecret": cfg["my_sec"],
            "token": token,
        },
    )
    headers = {"content-type": "application/json; charset=UTF-8"}

    session = requests.Session()
    req = requests.Request("POST", url, headers=headers, json=payload)
    preq = session.prepare_request(req)
    _, req_id = log_http_request(
        api_id="ka10002",
        url=url,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name="koreainvestment",
    )

    response = session.send(preq, timeout=15)
    log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name="koreainvestment",
    )
    response.raise_for_status()
    _print_response(response, "ka10002")
    data = response.json()
    _save_revoke(cfg["my_app"], cfg["my_sec"], token, data)
    return data


def get_approval_key(grant_type: str = "client_credentials", env_dv: str | None = None) -> dict[str, Any]:
    """웹소켓 승인키를 신규 발급하고 DB에 저장합니다."""
    cfg = load_config()
    current_env = _resolve_env_dv(env_dv, cfg)
    url = _base_url(current_env, cfg) + _REQ_SPEC["ka10003"]["url"]

    payload = _build_request_body(
        "ka10003",
        {
            "grant_type": grant_type,
            "appkey": cfg["my_app"],
            "secretkey": cfg["my_sec"],
        },
    )
    headers = {"content-type": "application/json; charset=UTF-8"}

    session = requests.Session()
    req = requests.Request("POST", url, headers=headers, json=payload)
    preq = session.prepare_request(req)
    _, req_id = log_http_request(
        api_id="ka10003",
        url=url,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name="koreainvestment",
    )

    response = session.send(preq, timeout=15)
    log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name="koreainvestment",
    )
    response.raise_for_status()
    _print_response(response, "ka10003")
    data = response.json()
    _save_approval(cfg["my_app"], cfg["my_sec"], grant_type, data)
    return data
