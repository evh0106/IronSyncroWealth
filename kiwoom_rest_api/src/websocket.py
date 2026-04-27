"""
키움증권 WebSocket 메뉴 - 동기 진입점
독립 실행은 `python -m websocket.websocket`으로 가능합니다.
"""

import asyncio
import sys
import threading
from contextlib import suppress

if __package__ is None or __package__ == '':
    # `python .../websocket.py` 직접 실행 시 상대 import가 가능하도록 패키지 컨텍스트를 보정합니다.
    from pathlib import Path

    src_dir = str(Path(__file__).resolve().parent)
    while src_dir in sys.path:
        sys.path.remove(src_dir)
    sys.path.insert(0, src_dir)
    __package__ = 'websocket'

from websocket.client import WebSocketClient, SOCKET_URL
from websocket.realtime import register
from websocket.condition import (
    get_condition_list,
    request_condition,
    request_condition_realtime,
    remove_condition_realtime,
)
from websocket.menu import REALTIME_TYPES, ACCOUNT_TYPES
from oauth2 import HOST, get_access_token, get_server_mode_label, load_api_keys, revoke_access_token


# ─────────────────────────────────────────────────────────────
# 공통 유틸
# ─────────────────────────────────────────────────────────────
async def _command_loop(client: WebSocketClient, prompt: str = '\n명령 입력 [q: 종료] > ') -> str:
    """
    사용자 키보드 입력을 기다립니다.
    q 입력 시 'quit', EOFError 시 'eof'를 반환합니다.
    receive_task가 먼저 종료되면 이 코루틴은 취소됩니다.
    """
    while client.keep_running:
        try:
            cmd = (await asyncio.to_thread(input, prompt)).strip().lower()
        except EOFError:
            return 'eof'
        if cmd == 'q':
            return 'quit'


async def _cancel(task: asyncio.Task):
    """태스크를 취소하고 CancelledError를 무시하며 대기합니다."""
    if not task.done():
        task.cancel()
        with suppress(asyncio.CancelledError):
            await task


async def _run_session(token: str, items: list[str] | None, types: list[str]):
    """
    WebSocket 세션을 열고 실시간 항목을 등록한 뒤,
    receive_task / command_task 중 먼저 완료된 쪽을 기준으로 정상 종료합니다.
    """
    client = WebSocketClient(SOCKET_URL, token)
    receive_task = asyncio.create_task(client.run())
    login_ok = await client.wait_for_login(timeout=5)
    if not login_ok:
        print('\n[중단] WebSocket 로그인에 실패하여 실시간 등록을 수행하지 않습니다.')
        await client.disconnect()
        await _cancel(receive_task)
        return
    await register(client, types, items=items or None)

    print('\n실시간 데이터를 수신 중입니다. [q + Enter] 로 종료하세요.')
    command_task = asyncio.create_task(_command_loop(client))

    try:
        while client.keep_running:
            done, _ = await asyncio.wait(
                {receive_task, command_task},
                return_when=asyncio.FIRST_COMPLETED,
            )

            if command_task in done:
                # 사용자가 q 또는 EOF 입력
                await client.disconnect()
                break

            if receive_task in done:
                # 서버 연결이 먼저 끊어진 경우
                break
    finally:
        await client.disconnect()
        await _cancel(command_task)
        await _cancel(receive_task)


# ─────────────────────────────────────────────────────────────
# 내부 async 로직
# ─────────────────────────────────────────────────────────────
async def _run_realtime_quote(token: str, items: list[str], types: list[str]):
    """종목 기반 실시간 시세 세션."""
    await _run_session(token, items, types)


async def _run_condition(token: str):
    """조건검색 WebSocket 세션."""
    client = WebSocketClient(SOCKET_URL, token)
    receive_task = asyncio.create_task(client.run())
    login_ok = await client.wait_for_login(timeout=5)
    if not login_ok:
        print('\n[중단] WebSocket 로그인에 실패하여 조건검색을 수행하지 않습니다.')
        await client.disconnect()
        await _cancel(receive_task)
        return

    try:
        # 1. 목록 조회
        print('\n조건검색 목록을 조회합니다...')
        await get_condition_list(client)
        await asyncio.sleep(1)  # 응답 수신 대기

        # 2. 일련번호 입력
        seq = (await asyncio.to_thread(input, '조건검색식 일련번호 입력: ')).strip()
        if not seq:
            print('일련번호를 입력하지 않았습니다. 종료합니다.')
            return

        mode = (await asyncio.to_thread(input, '조회 방식 [1: 일반조회, 2: 실시간]: ')).strip()

        if mode == '1':
            # 일반 조회: 결과를 받을 때까지 대기 후 종료
            await request_condition(client, seq)
            command_task = asyncio.create_task(_command_loop(client, '\n결과 수신 대기 중... [q: 종료] > '))
            done, _ = await asyncio.wait(
                {receive_task, command_task},
                return_when=asyncio.FIRST_COMPLETED,
            )
            await client.disconnect()
            await _cancel(command_task)

        elif mode == '2':
            # 실시간 조회
            await request_condition_realtime(client, seq)
            print('\n실시간 조건검색 중입니다. [q + Enter] 로 해제 후 종료합니다.')
            command_task = asyncio.create_task(_command_loop(client))

            while client.keep_running:
                done, _ = await asyncio.wait(
                    {receive_task, command_task},
                    return_when=asyncio.FIRST_COMPLETED,
                )

                if command_task in done:
                    await remove_condition_realtime(client, seq)
                    await asyncio.sleep(0.3)
                    await client.disconnect()
                    break

                if receive_task in done:
                    break

            await _cancel(command_task)

        else:
            print('올바른 방식이 아닙니다.')

    finally:
        await client.disconnect()
        await _cancel(receive_task)


# ─────────────────────────────────────────────────────────────
# 동기 진입점 (main.py에서 fn(token) 형태로 호출)
# ─────────────────────────────────────────────────────────────
def run_realtime_quote(token: str):
    """
    종목 기반 실시간 시세 수신 메뉴.
    종목코드와 실시간 타입을 대화형으로 입력받아 WebSocket 세션을 시작합니다.
    """
    print()
    print('─── 종목 기반 실시간 시세 ─────────────────────')
    codes_raw = input('종목코드 입력 (여러 개는 쉼표로 구분, 예: 005930,039490): ').strip()
    if not codes_raw:
        print('종목코드를 입력하지 않았습니다.')
        return
    items = [c.strip() for c in codes_raw.split(',') if c.strip()]

    print()
    print('실시간 항목 선택 (여러 개 선택 가능, 쉼표 구분):')
    for i, (code, name) in enumerate(REALTIME_TYPES, 1):
        print(f'  [{i:2}] {code} – {name}')
    type_input = input('번호 입력 (기본값 1=주식체결): ').strip()

    if not type_input:
        selected_types = [REALTIME_TYPES[0][0]]
    else:
        selected_types = []
        for idx_str in type_input.split(','):
            idx_str = idx_str.strip()
            if idx_str.isdigit():
                idx = int(idx_str) - 1
                if 0 <= idx < len(REALTIME_TYPES):
                    selected_types.append(REALTIME_TYPES[idx][0])
        if not selected_types:
            print('유효한 항목이 없습니다.')
            return

    print(f'\n[등록] 종목: {items}  타입: {selected_types}')
    asyncio.run(_run_realtime_quote(token, items, selected_types))


def run_account_realtime(token: str):
    """
    계좌/기타 실시간 항목 수신 메뉴.
    종목코드 없이 계좌·공통 타입을 등록합니다.
    """
    print()
    print('─── 계좌/기타 실시간 항목 ─────────────────────')
    print('항목 선택 (여러 개는 쉼표로 구분):')
    for i, (code, name) in enumerate(ACCOUNT_TYPES, 1):
        print(f'  [{i:2}] {code} – {name}')
    type_input = input('번호 입력 (기본값 1=주문체결): ').strip()

    if not type_input:
        selected_types = [ACCOUNT_TYPES[0][0]]
        need_item = False
    else:
        selected_types = []
        need_item_flags = []
        for idx_str in type_input.split(','):
            idx_str = idx_str.strip()
            if idx_str.isdigit():
                idx = int(idx_str) - 1
                if 0 <= idx < len(ACCOUNT_TYPES):
                    code = ACCOUNT_TYPES[idx][0]
                    selected_types.append(code)
                    need_item_flags.append(code not in ('00', '04', '0s'))
        need_item = any(need_item_flags)
        if not selected_types:
            print('유효한 항목이 없습니다.')
            return

    items = None
    if need_item:
        codes_raw = input('종목/업종코드 입력 (여러 개 쉼표 구분): ').strip()
        items = [c.strip() for c in codes_raw.split(',') if c.strip()] if codes_raw else None

    print(f'\n[등록] 타입: {selected_types}  아이템: {items}')
    asyncio.run(_run_realtime_quote(token, items or [], selected_types))


def run_condition_search(token: str):
    """조건검색 WebSocket 메뉴."""
    asyncio.run(_run_condition(token))


# ─────────────────────────────────────────────────────────────
# 백그라운드 WebSocket (main.py 메뉴에서 REST와 동시 사용)
# ─────────────────────────────────────────────────────────────
_bg_thread: threading.Thread | None = None
_bg_stop_event: threading.Event = threading.Event()


async def _run_session_background(
    token: str,
    items: list[str] | None,
    types: list[str],
    stop_event: threading.Event,
) -> None:
    """백그라운드 모드: stop_event가 설정되거나 연결이 끊길 때까지 수신. 화면 출력 없음."""
    client = WebSocketClient(SOCKET_URL, token, silent=True)
    receive_task = asyncio.create_task(client.run())
    login_ok = await client.wait_for_login(timeout=5)
    if not login_ok:
        print('\n[WebSocket] 로그인 실패 - 백그라운드 세션을 종료합니다.')
        await client.disconnect()
        await _cancel(receive_task)
        return
    await register(client, types, items=items or None)
    print('\n[WebSocket] 백그라운드 수신 시작. [웹소켓] → [웹소켓 종료]로 중지하세요.')
    try:
        while not stop_event.is_set() and client.keep_running:
            done, _ = await asyncio.wait({receive_task}, timeout=0.5)
            if receive_task in done:
                break
    finally:
        await client.disconnect()
        await _cancel(receive_task)
    print('\n[WebSocket] 백그라운드 세션이 종료되었습니다.')


def is_realtime_running() -> bool:
    """백그라운드 WebSocket 실행 여부를 반환합니다."""
    return _bg_thread is not None and _bg_thread.is_alive()


def _launch_background(token: str, items: list[str] | None, types: list[str]) -> bool:
    """백그라운드 스레드를 시작합니다. 이미 실행 중이면 False 반환."""
    global _bg_thread, _bg_stop_event
    if is_realtime_running():
        print('\n이미 백그라운드 WebSocket이 실행 중입니다. 먼저 종료해주세요.')
        return False
    _bg_stop_event = threading.Event()

    def _run() -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(
                _run_session_background(token, items, types, _bg_stop_event)
            )
        finally:
            loop.close()

    _bg_thread = threading.Thread(target=_run, daemon=True, name='ws-bg')
    _bg_thread.start()
    return True


def stop_realtime_background() -> None:
    """백그라운드 WebSocket을 안전하게 종료합니다."""
    global _bg_thread
    if not is_realtime_running():
        print('\n실행 중인 백그라운드 WebSocket이 없습니다.')
        return
    _bg_stop_event.set()
    assert _bg_thread is not None
    _bg_thread.join(timeout=5)
    _bg_thread = None
    print('\n[WebSocket] 백그라운드 세션을 종료했습니다.')


def run_realtime_quote_bg(token: str) -> None:
    """종목 실시간 시세를 백그라운드 스레드에서 시작합니다."""
    if is_realtime_running():
        print('\n이미 백그라운드 WebSocket이 실행 중입니다. 먼저 종료해주세요.')
        return
    print()
    print('─── 종목 실시간 시세 (백그라운드) ─────────────')
    codes_raw = input('종목코드 입력 (여러 개는 쉼표로 구분, 예: 005930,039490): ').strip()
    if not codes_raw:
        print('종목코드를 입력하지 않았습니다.')
        return
    items = [c.strip() for c in codes_raw.split(',') if c.strip()]

    print()
    print('실시간 항목 선택 (여러 개 선택 가능, 쉼표 구분):')
    for i, (code, name) in enumerate(REALTIME_TYPES, 1):
        print(f'  [{i:2}] {code} – {name}')
    type_input = input('번호 입력 (기본값 1=주식체결): ').strip()

    if not type_input:
        selected_types = [REALTIME_TYPES[0][0]]
    else:
        selected_types = []
        for idx_str in type_input.split(','):
            idx_str = idx_str.strip()
            if idx_str.isdigit():
                idx = int(idx_str) - 1
                if 0 <= idx < len(REALTIME_TYPES):
                    selected_types.append(REALTIME_TYPES[idx][0])
        if not selected_types:
            print('유효한 항목이 없습니다.')
            return

    print(f'\n[등록] 종목: {items}  타입: {selected_types}')
    _launch_background(token, items, selected_types)


def run_account_realtime_bg(token: str) -> None:
    """계좌/기타 실시간을 백그라운드 스레드에서 시작합니다."""
    if is_realtime_running():
        print('\n이미 백그라운드 WebSocket이 실행 중입니다. 먼저 종료해주세요.')
        return
    print()
    print('─── 계좌/기타 실시간 (백그라운드) ─────────────')
    print('항목 선택 (여러 개는 쉼표로 구분):')
    for i, (code, name) in enumerate(ACCOUNT_TYPES, 1):
        print(f'  [{i:2}] {code} – {name}')
    type_input = input('번호 입력 (기본값 1=주문체결): ').strip()

    if not type_input:
        selected_types = [ACCOUNT_TYPES[0][0]]
        need_item = False
    else:
        selected_types = []
        need_item_flags = []
        for idx_str in type_input.split(','):
            idx_str = idx_str.strip()
            if idx_str.isdigit():
                idx = int(idx_str) - 1
                if 0 <= idx < len(ACCOUNT_TYPES):
                    code = ACCOUNT_TYPES[idx][0]
                    selected_types.append(code)
                    need_item_flags.append(code not in ('00', '04', '0s'))
        need_item = any(need_item_flags)
        if not selected_types:
            print('유효한 항목이 없습니다.')
            return

    items = None
    if need_item:
        codes_raw = input('종목/업종코드 입력 (여러 개 쉼표 구분): ').strip()
        items = [c.strip() for c in codes_raw.split(',') if c.strip()] if codes_raw else None

    print(f'\n[등록] 타입: {selected_types}  아이템: {items}')
    _launch_background(token, items or [], selected_types)


def main():
    """WebSocket 전용 프로그램 진입점."""
    print('\n키움증권 WebSocket 프로그램을 시작합니다.')
    print(f'현재 서버 모드: {get_server_mode_label(HOST)} ({HOST})')

    try:
        app_key, app_secret = load_api_keys()
        token = get_access_token(app_key, app_secret)
    except FileNotFoundError as e:
        print(f'\n[오류] API 키 파일을 찾을 수 없습니다.\n  {e}')
        sys.exit(1)
    except Exception as e:
        print(f'\n[오류] 토큰 발급 실패: {e}')
        sys.exit(1)

    try:
        # 순환 import를 피하기 위해 진입 시점에 메뉴 모듈을 로드합니다.
        from websocket.menu import run_websocket_menu

        run_websocket_menu(token)
    finally:
        try:
            revoke_access_token(app_key, app_secret, token)
        except Exception:
            pass


if __name__ == '__main__':
    main()
