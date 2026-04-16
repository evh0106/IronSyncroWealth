"""키움증권 계좌 API 메뉴."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json

import requests

from oauth2 import HOST
from .specs import ACCOUNT_API_SPECS, ACCOUNT_RESPONSE_SPECS
from volume._fmt import _ljust, _rjust, _wcslen


_ACNT_URL = HOST + '/api/dostk/acnt'


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
    for raw_spec in ACCOUNT_API_SPECS:
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
    print('\n[계좌 API 목록 - /api/dostk/acnt]')
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
        if spec.api_id == 'ka01690' and field.element == 'qry_dt':
            default_value = datetime.now().strftime('%Y%m%d')
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


def _post_acnt_api(token: str, spec: ApiSpec, body: dict, cont_yn: str = 'N', next_key: str = ''):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': f'Bearer {token}',
        'cont-yn': cont_yn,
        'next-key': next_key,
        'api-id': spec.api_id,
    }
    response = requests.post(_ACNT_URL, headers=headers, json=body)
    response.raise_for_status()
    return response


def _is_number_like(value) -> bool:
    if isinstance(value, (int, float)):
        return True
    if not isinstance(value, str):
        return False
    text = value.strip().replace(',', '')
    if not text:
        return False
    if text[0] in '+-':
        text = text[1:]
    if text.count('.') > 1:
        return False
    return text.replace('.', '', 1).isdigit()


def _stringify(value) -> str:
    if value is None:
        return ''
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def _build_label_map(api_id: str) -> dict[str, str]:
    """element -> label 매핑 딕셔너리를 반환합니다. 서브 항목(- prefix)도 포함."""
    label_map: dict[str, str] = {}
    for field in ACCOUNT_RESPONSE_SPECS.get(api_id, []):
        element = field['element']
        label = field.get('label', '')
        if label:
            # '- stk_cd' -> 'stk_cd'
            key = element.lstrip('- ').strip()
            label_map[key] = label
    return label_map


def _display_key(key: str, label_map: dict[str, str]) -> str:
    label = label_map.get(key, '')
    if label:
        return f'{label}({key})'
    return key


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


def _infer_columns(items: list[dict]) -> list[str]:
    columns: list[str] = []
    for item in items:
        for key in item:
            if key not in columns:
                columns.append(key)
    return columns


def _column_width(items: list[dict], column: str) -> int:
    width = _wcslen(column)
    for item in items:
        value = _stringify(item.get(column, ''))
        width = max(width, _wcslen(value))
    return min(max(width, 8), 24)


def _print_list_table(title: str, items: list, label_map: dict[str, str] | None = None):
    if not items:
        return

    label_map = label_map or {}
    label = label_map.get(title, '')
    display_title = f'{label}({title})' if label else title
    print(f'\n[{display_title}]')

    if not all(isinstance(item, dict) for item in items):
        for index, item in enumerate(items, 1):
            print(f'  {_rjust(index, 3)}. {_stringify(item)}')
        return

    columns = _infer_columns(items)
    widths = {column: _column_width(items, column) for column in columns}
    col_labels = {col: _display_key(col, label_map) for col in columns}
    widths = {col: max(widths[col], _wcslen(col_labels[col])) for col in columns}

    header = '  ' + '  '.join(_ljust(col_labels[col], widths[col]) for col in columns)
    divider = '  ' + '  '.join('─' * widths[col] for col in columns)
    print(header)
    print(divider)

    for item in items:
        row = []
        for column in columns:
            value = _stringify(item.get(column, ''))
            if _wcslen(value) > widths[column]:
                value = value[:max(widths[column] - 3, 0)] + '...'
            if _is_number_like(value):
                row.append(_rjust(value, widths[column]))
            else:
                row.append(_ljust(value, widths[column]))
        print('  ' + '  '.join(row))


def _print_payload(payload: dict, label_map: dict[str, str] | None = None):
    label_map = label_map or {}
    nested_dicts = {
        key: value
        for key, value in payload.items()
        if isinstance(value, dict)
    }
    list_values = {
        key: value
        for key, value in payload.items()
        if isinstance(value, list)
    }

    for key, value in nested_dicts.items():
        if value:
            _print_kv_block(key, value, label_map)
        else:
            label = label_map.get(key, '')
            display = f'{label}({key})' if label else key
            print(f'\n[{display}]')
            print('  내용이 없습니다.')

    for key, value in list_values.items():
        if value:
            _print_list_table(key, value, label_map)
        else:
            label = label_map.get(key, '')
            display = f'{label}({key})' if label else key
            print(f'\n[{display}]')
            print('  조회 결과가 없습니다.')


def _print_response(response: requests.Response, api_id: str = ''):
    cont_yn = response.headers.get('cont-yn', '')
    next_key = response.headers.get('next-key', '')
    payload = response.json()
    label_map = _build_label_map(api_id) if api_id else {}

    _print_kv_block('응답 헤더', {
        'api-id': response.headers.get('api-id', ''),
        'cont-yn': cont_yn or 'N',
        'next-key': next_key,
    })

    print(f'\n[처리 결과] {payload.get("return_msg", "") or "응답 수신"} (code={payload.get("return_code", "")})')

    if payload.get('return_code') == 0:
        _print_payload(payload, label_map)
    else:
        print(json.dumps(payload, indent=4, ensure_ascii=False))

    show_raw = input('\n원시 JSON 출력? (y/N): ').strip().lower()
    if show_raw == 'y':
        print('\n[원시 JSON]')
        print(json.dumps(payload, indent=4, ensure_ascii=False))

    return cont_yn, next_key


def run_account_api_menu(token: str):
    """파이썬 코드로 정의된 계좌 API 실행 메뉴."""
    specs = _load_specs()
    if not specs:
        print('계좌 API 목록을 찾지 못했습니다.')
        return

    while True:
        spec = _select_spec(specs)
        if spec is None:
            return

        body = _prompt_body(spec)
        cont_yn = 'N'
        next_key = ''

        while True:
            print(f'\n  → {spec.name} ({spec.api_id}) 호출 중...')
            try:
                response = _post_acnt_api(token, spec, body, cont_yn=cont_yn, next_key=next_key)
            except requests.HTTPError as exc:
                print(f'  [HTTP 오류] {exc}')
                if exc.response is not None:
                    try:
                        print(json.dumps(exc.response.json(), indent=4, ensure_ascii=False))
                    except Exception:
                        print(exc.response.text)
                break
            except Exception as exc:
                print(f'  [오류] {exc}')
                break

            cont_yn, next_key = _print_response(response, api_id=spec.api_id)
            if cont_yn != 'Y' or not next_key:
                break

            again = input('\n다음 페이지를 이어서 조회할까요? (y/N): ').strip().lower()
            if again != 'y':
                break

        again = input('\n다른 계좌 API를 계속 조회할까요? (Y/n): ').strip().lower()
        if again == 'n':
            return