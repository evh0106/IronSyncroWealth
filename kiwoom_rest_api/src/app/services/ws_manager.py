"""WebSocket 세션 매니저.

백그라운드 스레드에서 키움증권 WebSocket 연결을 관리합니다.
FastAPI 프로세스 당 단일 세션만 허용합니다.
"""

from __future__ import annotations

import asyncio
import threading
from contextlib import suppress
from dataclasses import dataclass, field
from datetime import datetime

from app.core.exceptions import ApiError
from app.schemas.ws import ACCOUNT_TYPES, ServerMode, WsSessionStatus
from oauth2.kiwoom_oauth2 import HOST_MOC, HOST_REAL
from oauth2.oauth import get_current_unrevoked_token
from websocket.client import WebSocketClient, SOCKET_URL_PROD, SOCKET_URL_MOCK
from websocket.realtime import register, remove

_SERVER_HOSTS: dict[str, str] = {
    "real": HOST_REAL,
    "mock": HOST_MOC,
}

_SERVER_WS_URL: dict[str, str] = {
    "real": SOCKET_URL_PROD,
    "mock": SOCKET_URL_MOCK,
}


@dataclass
class _SessionState:
    server_mode: ServerMode
    items: list[str]
    types: list[str]
    group_no: str
    started_at: datetime = field(default_factory=datetime.now)


async def _cancel_task(task: asyncio.Task) -> None:
    if not task.done():
        task.cancel()
        with suppress(asyncio.CancelledError):
            await task


class WsSessionManager:
    """백그라운드 WebSocket 세션의 수명 주기를 관리합니다.

    모듈 레벨 싱글턴 ``ws_manager`` 로 접근하세요.
    """

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._thread: threading.Thread | None = None
        self._stop_event: threading.Event = threading.Event()
        self._state: _SessionState | None = None
        # 실행 중인 루프와 클라이언트 (register/remove 추가 호출용)
        self._loop: asyncio.AbstractEventLoop | None = None
        self._client: WebSocketClient | None = None

    # ─────────────────────────────────────────────
    # 내부 토큰 헬퍼
    # ─────────────────────────────────────────────
    def _resolve_token(self) -> tuple[ServerMode, str, str]:
        token_ctx = get_current_unrevoked_token()
        if not token_ctx:
            raise ApiError(
                message="No valid access token found. Issue a token first via POST /api/v1/auth/token",
                code="TOKEN_NOT_FOUND",
                status_code=401,
            )
        server_mode = token_ctx[0]  # type: ignore[assignment]
        token = token_ctx[1]
        host = _SERVER_HOSTS.get(server_mode)
        if not host:
            raise ApiError(
                message=f"Unsupported server_mode: {server_mode}",
                code="INVALID_SERVER_MODE",
                status_code=400,
            )
        return server_mode, host, token

    # ─────────────────────────────────────────────
    # 백그라운드 async 루프
    # ─────────────────────────────────────────────
    async def _session_loop(
        self,
        ws_url: str,
        token: str,
        items: list[str],
        types: list[str],
        group_no: str,
        stop_event: threading.Event,
    ) -> None:
        client = WebSocketClient(ws_url, token, silent=True)
        self._client = client
        receive_task = asyncio.create_task(client.run())

        login_ok = await client.wait_for_login(timeout=8)
        if not login_ok:
            print("[WsSessionManager] WebSocket 로그인 실패 — 세션 종료")
            await client.disconnect()
            await _cancel_task(receive_task)
            return

        item_list = items if items else None
        await register(client, types, items=item_list, group_no=group_no)

        try:
            while not stop_event.is_set() and client.keep_running:
                done, _ = await asyncio.wait({receive_task}, timeout=0.5)
                if receive_task in done:
                    break
        finally:
            await client.disconnect()
            await _cancel_task(receive_task)
            self._client = None

    def _thread_entry(
        self,
        ws_url: str,
        token: str,
        items: list[str],
        types: list[str],
        group_no: str,
        stop_event: threading.Event,
    ) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self._loop = loop
        try:
            loop.run_until_complete(
                self._session_loop(ws_url, token, items, types, group_no, stop_event)
            )
        finally:
            loop.close()
            self._loop = None

    # ─────────────────────────────────────────────
    # 공개 API
    # ─────────────────────────────────────────────
    def is_running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def status(self) -> WsSessionStatus:
        if not self.is_running() or self._state is None:
            return WsSessionStatus(running=False)
        s = self._state
        return WsSessionStatus(
            running=True,
            server_mode=s.server_mode,
            items=list(s.items),
            types=list(s.types),
            started_at=s.started_at,
            group_no=s.group_no,
        )

    def start(
        self,
        items: list[str],
        types: list[str],
        group_no: str = "1",
    ) -> ServerMode:
        with self._lock:
            if self.is_running():
                raise ApiError(
                    message="WebSocket session is already running. Stop it first.",
                    code="WS_ALREADY_RUNNING",
                    status_code=409,
                )

            server_mode, _, token = self._resolve_token()
            ws_url = _SERVER_WS_URL[server_mode]
            stop_event = threading.Event()
            self._stop_event = stop_event
            self._state = _SessionState(
                server_mode=server_mode,
                items=list(items),
                types=list(types),
                group_no=group_no,
            )

            def _run() -> None:
                self._thread_entry(ws_url, token, items, types, group_no, stop_event)
                # 스레드 종료 시 상태 초기화
                with self._lock:
                    self._state = None
                    self._thread = None

            thread = threading.Thread(target=_run, daemon=True, name="ws-bg")
            self._thread = thread
            thread.start()
            return server_mode

    def stop(self) -> None:
        with self._lock:
            if not self.is_running():
                raise ApiError(
                    message="No WebSocket session is running.",
                    code="WS_NOT_RUNNING",
                    status_code=409,
                )
            self._stop_event.set()
        assert self._thread is not None
        self._thread.join(timeout=6)
        with self._lock:
            self._thread = None
            self._state = None

    def add_items(
        self,
        items: list[str],
        types: list[str],
        group_no: str = "1",
    ) -> None:
        """실행 중인 세션에 실시간 항목을 추가 등록합니다."""
        with self._lock:
            if not self.is_running() or self._loop is None or self._client is None:
                raise ApiError(
                    message="No WebSocket session is running.",
                    code="WS_NOT_RUNNING",
                    status_code=409,
                )
            loop = self._loop
            client = self._client
            state = self._state

        async def _do():
            item_list = items if items else None
            await register(client, types, items=item_list, group_no=group_no, refresh="1")

        future = asyncio.run_coroutine_threadsafe(_do(), loop)
        future.result(timeout=5)

        if state:
            for t in types:
                if t not in state.types:
                    state.types.append(t)
            for item in items:
                if item not in state.items:
                    state.items.append(item)

    def remove_items(
        self,
        items: list[str],
        types: list[str],
        group_no: str = "1",
    ) -> None:
        """실행 중인 세션에서 실시간 항목을 해제합니다."""
        with self._lock:
            if not self.is_running() or self._loop is None or self._client is None:
                raise ApiError(
                    message="No WebSocket session is running.",
                    code="WS_NOT_RUNNING",
                    status_code=409,
                )
            loop = self._loop
            client = self._client
            state = self._state

        async def _do():
            item_list = items if items else None
            await remove(client, types, items=item_list, group_no=group_no)

        future = asyncio.run_coroutine_threadsafe(_do(), loop)
        future.result(timeout=5)

        if state:
            for t in types:
                with suppress(ValueError):
                    state.types.remove(t)
            for item in items:
                with suppress(ValueError):
                    state.items.remove(item)


# 모듈 레벨 싱글턴
ws_manager = WsSessionManager()


def get_ws_manager() -> WsSessionManager:
    return ws_manager
