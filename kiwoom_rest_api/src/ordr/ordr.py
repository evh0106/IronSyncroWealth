"""키움증권 주문 API 메뉴."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json

import requests

import db
from logger import log_http_request, log_http_response
from oauth2 import HOST
from .specs import ORDR_API_SPECS, ORDR_RESPONSE_SPECS
from volume._fmt import _ljust, _wcslen


_ORDR_URL = HOST + '/api/dostk/ordr'


_INSERT_ORDR_SQL = {
    'kt10000': """
        INSERT INTO kt10000_stk_buy_ord
            (req_dt, req_dmst_stex_tp, req_stk_cd, req_ord_qty, req_ord_uv, req_trde_tp, req_cond_uv,
             rsp_ord_no, rsp_dmst_stex_tp)
        VALUES
            (%(req_dt)s, %(req_dmst_stex_tp)s, %(req_stk_cd)s, %(req_ord_qty)s, %(req_ord_uv)s, %(req_trde_tp)s, %(req_cond_uv)s,
             %(rsp_ord_no)s, %(rsp_dmst_stex_tp)s)
    """,
    'kt10001': """
        INSERT INTO kt10001_stk_sll_ord
            (req_dt, req_dmst_stex_tp, req_stk_cd, req_ord_qty, req_ord_uv, req_trde_tp, req_cond_uv,
             rsp_ord_no, rsp_dmst_stex_tp)
        VALUES
            (%(req_dt)s, %(req_dmst_stex_tp)s, %(req_stk_cd)s, %(req_ord_qty)s, %(req_ord_uv)s, %(req_trde_tp)s, %(req_cond_uv)s,
             %(rsp_ord_no)s, %(rsp_dmst_stex_tp)s)
    """,
    'kt10002': """
        INSERT INTO kt10002_stk_mdfy_ord
            (req_dt, req_dmst_stex_tp, req_orig_ord_no, req_stk_cd, req_mdfy_qty, req_mdfy_uv, req_mdfy_cond_uv,
             rsp_ord_no, rsp_base_orig_ord_no, rsp_mdfy_qty, rsp_dmst_stex_tp)
        VALUES
            (%(req_dt)s, %(req_dmst_stex_tp)s, %(req_orig_ord_no)s, %(req_stk_cd)s, %(req_mdfy_qty)s, %(req_mdfy_uv)s, %(req_mdfy_cond_uv)s,
             %(rsp_ord_no)s, %(rsp_base_orig_ord_no)s, %(rsp_mdfy_qty)s, %(rsp_dmst_stex_tp)s)
    """,
    'kt10003': """
        INSERT INTO kt10003_stk_cncl_ord
            (req_dt, req_dmst_stex_tp, req_orig_ord_no, req_stk_cd, req_cncl_qty,
             rsp_ord_no, rsp_base_orig_ord_no, rsp_cncl_qty)
        VALUES
            (%(req_dt)s, %(req_dmst_stex_tp)s, %(req_orig_ord_no)s, %(req_stk_cd)s, %(req_cncl_qty)s,
             %(rsp_ord_no)s, %(rsp_base_orig_ord_no)s, %(rsp_cncl_qty)s)
    """,
    'kt50000': """
        INSERT INTO kt50000_gold_buy_ord
            (req_dt, req_stk_cd, req_ord_qty, req_ord_uv, req_trde_tp, rsp_ord_no)
        VALUES
            (%(req_dt)s, %(req_stk_cd)s, %(req_ord_qty)s, %(req_ord_uv)s, %(req_trde_tp)s, %(rsp_ord_no)s)
    """,
    'kt50001': """
        INSERT INTO kt50001_gold_sll_ord
            (req_dt, req_stk_cd, req_ord_qty, req_ord_uv, req_trde_tp, rsp_ord_no)
        VALUES
            (%(req_dt)s, %(req_stk_cd)s, %(req_ord_qty)s, %(req_ord_uv)s, %(req_trde_tp)s, %(rsp_ord_no)s)
    """,
    'kt50002': """
        INSERT INTO kt50002_gold_mdfy_ord
            (req_dt, req_stk_cd, req_orig_ord_no, req_mdfy_qty, req_mdfy_uv,
             rsp_ord_no, rsp_base_orig_ord_no, rsp_mdfy_qty)
        VALUES
            (%(req_dt)s, %(req_stk_cd)s, %(req_orig_ord_no)s, %(req_mdfy_qty)s, %(req_mdfy_uv)s,
             %(rsp_ord_no)s, %(rsp_base_orig_ord_no)s, %(rsp_mdfy_qty)s)
    """,
    'kt50003': """
        INSERT INTO kt50003_gold_cncl_ord
            (req_dt, req_orig_ord_no, req_stk_cd, req_cncl_qty,
             rsp_ord_no, rsp_base_orig_ord_no, rsp_cncl_qty)
        VALUES
            (%(req_dt)s, %(req_orig_ord_no)s, %(req_stk_cd)s, %(req_cncl_qty)s,
             %(rsp_ord_no)s, %(rsp_base_orig_ord_no)s, %(rsp_cncl_qty)s)
    """,
}


def _save_order_response(api_id: str, body: dict, payload: dict, req_dt: str) -> int:
    """주문 API 성공 응답을 API별 테이블에 insert 저장한다."""
    sql = _INSERT_ORDR_SQL.get(api_id)
    if not sql:
        print(f'  [저장 오류] 알 수 없는 API ID: {api_id}')
        return 0

    row = {
        'req_dt': req_dt,
        'req_dmst_stex_tp': body.get('dmst_stex_tp', ''),
        'req_stk_cd': body.get('stk_cd', ''),
        'req_ord_qty': body.get('ord_qty', ''),
        'req_ord_uv': body.get('ord_uv', ''),
        'req_trde_tp': body.get('trde_tp', ''),
        'req_cond_uv': body.get('cond_uv', ''),
        'req_orig_ord_no': body.get('orig_ord_no', ''),
        'req_mdfy_qty': body.get('mdfy_qty', ''),
        'req_mdfy_uv': body.get('mdfy_uv', ''),
        'req_mdfy_cond_uv': body.get('mdfy_cond_uv', ''),
        'req_cncl_qty': body.get('cncl_qty', ''),
        'rsp_ord_no': payload.get('ord_no', ''),
        'rsp_dmst_stex_tp': payload.get('dmst_stex_tp', ''),
        'rsp_base_orig_ord_no': payload.get('base_orig_ord_no', ''),
        'rsp_mdfy_qty': payload.get('mdfy_qty', ''),
        'rsp_cncl_qty': payload.get('cncl_qty', ''),
    }

    conn = db.get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, row)
        conn.commit()
        return 1
    except Exception as exc:
        conn.rollback()
        print(f'  [DB 오류] {exc}')
        raise
    finally:
        conn.close()


@dataclass(slots=True)
class ApiField:
    element: str
    label: str
    required: bool
    description: str


@dataclass(slots=True)
class ApiSpec:
    api_id: str
    name: str
    overview: str
    fields: list[ApiField]
    request_example: dict


_SPEC_CACHE: list[ApiSpec] | None = None


def _build_specs() -> list[ApiSpec]:
    specs: list[ApiSpec] = []
    for raw_spec in ORDR_API_SPECS:
        fields = [
            ApiField(
                element=field['element'],
                label=field['label'],
                required=field['required'],
                description=field['description'],
            )
            for field in raw_spec['fields']
        ]
        specs.append(
            ApiSpec(
                api_id=raw_spec['api_id'],
                name=raw_spec['name'],
                overview=raw_spec['overview'],
                fields=fields,
                request_example=raw_spec['request_example'],
            )
        )
    return specs


def _load_specs() -> list[ApiSpec]:
    global _SPEC_CACHE

    if _SPEC_CACHE is not None:
        return _SPEC_CACHE

    _SPEC_CACHE = _build_specs()
    return _SPEC_CACHE


def _print_api_list(specs: list[ApiSpec]):
    print('\n[주문 API 목록 - /api/dostk/ordr]')
    print('─' * 72)
    for index, spec in enumerate(specs, 1):
        print(f'  [{index:02}] {spec.api_id:<8} {spec.name}')
    print('  [0] 뒤로')


def _select_spec(specs: list[ApiSpec]) -> ApiSpec | None:
    while True:
        _print_api_list(specs)
        choice = input('실행할 API 번호 또는 api-id 입력: ').strip()

        if choice == '0':
            return None

        for index, spec in enumerate(specs, 1):
            if choice == str(index) or choice.lower() == spec.api_id.lower():
                return spec

        print(f'  알 수 없는 선택: {choice!r}')


def _prompt_body(spec: ApiSpec) -> dict:
    body: dict[str, str] = {}

    print()
    print(f'[{spec.name} ({spec.api_id})]')
    if spec.overview:
        print(f'  개요: {spec.overview}')
    if not spec.fields:
        print('  요청 바디 없음')
        return body

    print('  요청 필드 입력: Enter만 누르면 기본값 또는 생략 처리합니다.')
    for field in spec.fields:
        default_value = spec.request_example.get(field.element, '')
        required_text = '필수' if field.required else '선택'
        desc = f' / {field.description}' if field.description else ''
        prompt = f'  - {field.label} [{field.element}] ({required_text}{desc})'
        if default_value != '':
            prompt += f' [기본값: {default_value}]'
        prompt += ': '

        while True:
            value = input(prompt).strip()
            if not value and default_value != '':
                value = str(default_value)
            if value:
                body[field.element] = value
                break
            if not field.required:
                break
            print('    필수 항목입니다.')

    return body


def _post_ordr_api(token: str, spec: ApiSpec, body: dict, cont_yn: str = 'N', next_key: str = ''):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': cont_yn,
        'next-key': next_key,
        'api-id': spec.api_id,
    }
    session = requests.Session()
    req = requests.Request('POST', _ORDR_URL, headers=headers, json=body)
    preq = session.prepare_request(req)

    path, req_id = log_http_request(
        api_id=spec.api_id,
        url=_ORDR_URL,
        request_headers=preq.headers,
        request_body=preq.body,
        log_name='ordr',
    )
    print(f'  -> 요청 로그 저장: {path}')

    response = session.send(preq)
    path = log_http_response(
        req_id=req_id,
        response_status=response.status_code,
        response_headers=response.headers,
        response_body=response.text,
        log_name='ordr',
    )
    print(f'  -> 응답 로그 저장: {path}')

    return response


def _response_payload(response: requests.Response) -> dict:
    """응답 본문을 dict로 반환한다. 파싱 실패 시 상태코드/원문으로 대체한다."""
    try:
        payload = response.json()
        if isinstance(payload, dict):
            return payload
        return {
            'return_code': response.status_code,
            'return_msg': str(payload),
        }
    except Exception:
        return {
            'return_code': response.status_code,
            'return_msg': response.text,
        }


def _build_label_map(api_id: str) -> dict[str, str]:
    label_map: dict[str, str] = {}
    for field in ORDR_RESPONSE_SPECS.get(api_id, []):
        element = field['element']
        label = field.get('label', '')
        if label:
            label_map[element] = label
    return label_map


def _display_key(key: str, label_map: dict[str, str]) -> str:
    label = label_map.get(key, '')
    if label:
        return f'{label}({key})'
    return key


def _stringify(value) -> str:
    if value is None:
        return ''
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _print_kv_block(title: str, values: dict, label_map: dict[str, str] | None = None):
    if not values:
        return

    label_map = label_map or {}
    display_keys = {key: _display_key(key, label_map) for key in values}
    key_width = max(_wcslen(dk) for dk in display_keys.values())
    value_width = max(_wcslen(_stringify(value)) for value in values.values())
    key_width = min(max(key_width, 8), 32)
    value_width = min(max(value_width, 12), 72)

    print(f'\n[{title}]')
    for key, value in values.items():
        rendered = _stringify(value)
        if _wcslen(rendered) > value_width:
            rendered = rendered[:max(value_width - 3, 0)] + '...'
        print(f'  {_ljust(display_keys[key], key_width)} : {_ljust(rendered, value_width)}')


def _print_response(response: requests.Response, payload: dict, api_id: str = ''):
    cont_yn = response.headers.get('cont-yn', '')
    next_key = response.headers.get('next-key', '')
    label_map = _build_label_map(api_id) if api_id else {}

    _print_kv_block('응답 헤더', {
        'api-id': response.headers.get('api-id', ''),
        'cont-yn': cont_yn or 'N',
        'next-key': next_key,
    })

    print(f'\n[처리 결과] {payload.get("return_msg", "") or "응답 수신"} (code={payload.get("return_code", "")})')

    if payload.get('return_code') == 0:
        body_values = {
            key: value
            for key, value in payload.items()
            if key not in {'return_code', 'return_msg'}
        }
        _print_kv_block('응답 본문', body_values, label_map)
    else:
        print(json.dumps(payload, indent=4, ensure_ascii=False))

    print('\n원시 JSON은 로그 파일에 저장되었습니다. (log/YYYYMMDD_ordr.log)')

    return cont_yn, next_key


def run_order_api_menu(token: str):
    """파이썬 코드로 정의된 주문 API 실행 메뉴."""
    specs = _load_specs()
    if not specs:
        print('주문 API 목록을 찾지 못했습니다.')
        return

    while True:
        spec = _select_spec(specs)
        if spec is None:
            return

        body = _prompt_body(spec)
        req_dt = datetime.now().strftime('%Y%m%d')
        cont_yn = 'N'
        next_key = ''

        while True:
            print(f'\n  → {spec.name} ({spec.api_id}) 호출 중...')
            try:
                response = _post_ordr_api(token, spec, body, cont_yn=cont_yn, next_key=next_key)
            except Exception as exc:
                print(f'  [오류] {exc}')
                break

            payload = _response_payload(response)
            cont_yn, next_key = _print_response(response, payload, api_id=spec.api_id)
            
            try:
                count = _save_order_response(spec.api_id, body, payload, req_dt)
                if count:
                    print(f'  → {count}건 저장 완료.')
            except Exception as exc:
                print(f'  [DB 오류] {exc}')

            if cont_yn != 'Y' or not next_key:
                break

            again = input('\n다음 페이지를 이어서 조회할까요? (y/N): ').strip().lower()
            if again != 'y':
                break

        again = input('\n다른 주문 API를 계속 조회할까요? (Y/n): ').strip().lower()
        if again == 'n':
            return
