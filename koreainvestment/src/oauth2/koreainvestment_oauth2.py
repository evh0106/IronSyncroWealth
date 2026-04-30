"""Korea Investment OAuth2 common module."""

from __future__ import annotations

import json
from typing import Any

import requests

from kis_config import load_config
from logger import log_http_request, log_http_response
from oauth2.specs_request import OAUTH2_API_SPECS
from oauth2.specs_response import OAUTH2_RESPONSE_SPECS


_REQ_SPEC: dict[str, dict[str, Any]] = {spec["api_id"]: spec for spec in OAUTH2_API_SPECS}
_RES_SPEC = OAUTH2_RESPONSE_SPECS


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


def get_access_token(grant_type: str = "client_credentials", env_dv: str | None = None) -> dict[str, Any]:
    """Issue an access token via /oauth2/tokenP."""
    cfg = load_config()
    current_env = _resolve_env_dv(env_dv, cfg)
    url = _base_url(current_env, cfg) + _REQ_SPEC["ka10001"]["url"]

    payload = _build_request_body(
        "ka10001",
        {
            "grant_type": grant_type,
            "appkey": cfg["my_app"],
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
    return response.json()


def revoke_access_token(token: str, env_dv: str | None = None) -> dict[str, Any]:
    """Revoke an access token via /oauth2/revokeP."""
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
    return response.json()


def get_approval_key(grant_type: str = "client_credentials", env_dv: str | None = None) -> dict[str, Any]:
    """Issue a websocket approval key via /oauth2/Approval."""
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
    return response.json()
