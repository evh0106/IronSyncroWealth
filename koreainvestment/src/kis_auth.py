from __future__ import annotations

import json
from typing import Any

import requests

from kis_config import load_config


def _base_url(env_dv: str, cfg: dict[str, Any]) -> str:
    return cfg["my_url_vts"] if env_dv == "demo" else cfg["my_url"]


def issue_access_token(grant_type: str = "client_credentials") -> dict[str, Any]:
    cfg = load_config()
    env_dv = cfg.get("env_dv", "real")
    url = f"{_base_url(env_dv, cfg)}/oauth2/tokenP"

    payload = {
        "grant_type": grant_type,
        "appkey": cfg["my_app"],
        "appsecret": cfg["my_sec"],
    }
    headers = {"content-type": "application/json; charset=UTF-8"}

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def issue_ws_approval_key(grant_type: str = "client_credentials") -> dict[str, Any]:
    cfg = load_config()
    env_dv = cfg.get("env_dv", "real")
    url = f"{_base_url(env_dv, cfg)}/oauth2/Approval"

    payload = {
        "grant_type": grant_type,
        "appkey": cfg["my_app"],
        "secretkey": cfg["my_sec"],
    }
    headers = {"content-type": "application/json; charset=UTF-8"}

    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()
