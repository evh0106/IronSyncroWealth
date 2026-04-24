"""
키움증권 WebSocket 클라이언트
URL: wss://api.kiwoom.com:10000/api/dostk/websocket
"""

import asyncio
import json
import websockets
from oauth2 import HOST
from logger import log_websocket_message
from . import db as ws_db

# ─────────────────────────────────────────────
# 서버 URL
# ─────────────────────────────────────────────
_WS_HOST_PROD = 'wss://api.kiwoom.com:10000'
_WS_HOST_MOCK = 'wss://mockapi.kiwoom.com:10000'
_WS_PATH = '/api/dostk/websocket'

SOCKET_URL_PROD = _WS_HOST_PROD + _WS_PATH
SOCKET_URL_MOCK = _WS_HOST_MOCK + _WS_PATH

# oauth2 HOST 설정에 따라 자동 선택
SOCKET_URL = SOCKET_URL_MOCK if 'mockapi' in HOST else SOCKET_URL_PROD


# ─────────────────────────────────────────────
# WebSocket 클라이언트
# ─────────────────────────────────────────────
class WebSocketClient:
    """
    키움증권 실시간 WebSocket 클라이언트.

    Parameters
    ----------
    uri : str
        WebSocket 서버 URL (기본값: SOCKET_URL)
    access_token : str
        Bearer 토큰 (로그인 패킷에 사용)
    on_message : callable | None
        수신 메시지 콜백 함수 (response: dict) → None
        None이면 기본 출력(print)을 사용합니다.
    """

    def __init__(self, uri: str, access_token: str, on_message=None):
        self.uri = uri
        self.access_token = access_token
        self.on_message = on_message
        self.websocket = None
        self.connected = False
        self.keep_running = True
        self.login_ok = False
        self._login_event = asyncio.Event()

    # ────────────────────────────────
    # 연결 및 로그인
    # ────────────────────────────────
    async def connect(self):
        """서버에 연결하고 로그인 패킷을 전송합니다."""
        try:
            self.login_ok = False
            self._login_event.clear()
            self.websocket = await websockets.connect(self.uri)
            self.connected = True
            print('서버와 연결되었습니다.')
            await self.send_message({'trnm': 'LOGIN', 'token': self.access_token})
        except Exception as exc:
            print(f'[연결 오류] {exc}')
            self.connected = False
            self._login_event.set()

    # ────────────────────────────────
    # 메시지 송신
    # ────────────────────────────────
    async def send_message(self, message: dict | str):
        """
        서버로 메시지를 전송합니다.

        Parameters
        ----------
        message : dict | str
            dict이면 JSON으로 직렬화하여 전송합니다.
        """
        if not self.keep_running:
            return
        if not self.connected:
            await self.connect()
        if self.connected:
            payload = message if isinstance(message, str) else json.dumps(message)
            await self.websocket.send(payload)
            print(f'[송신] {payload}')

    async def wait_for_login(self, timeout: float = 5.0) -> bool:
        """LOGIN 응답을 timeout 내에 기다리고 성공 여부를 반환합니다."""
        try:
            await asyncio.wait_for(self._login_event.wait(), timeout=timeout)
        except asyncio.TimeoutError:
            return False
        return self.login_ok

    # ────────────────────────────────
    # 메시지 수신
    # ────────────────────────────────
    async def receive_messages(self):
        """서버로부터 메시지를 지속적으로 수신합니다."""
        while self.keep_running:
            try:
                raw = await self.websocket.recv()
                response = json.loads(raw)
                trnm = response.get('trnm', '')

                # 로그인 응답
                if trnm == 'LOGIN':
                    if response.get('return_code') != 0:
                        self.login_ok = False
                        self._login_event.set()
                        print(f'[로그인 실패] {response.get("return_msg")}')
                        await self.disconnect()
                    else:
                        self.login_ok = True
                        self._login_event.set()
                        print('[로그인 성공]')

                # PING → 그대로 되돌려 보냄 (연결 유지)
                elif trnm == 'PING':
                    await self.send_message(response)

                # 그 외 실시간 데이터
                else:
                    if self.on_message:
                        self.on_message(response)
                    else:
                        pretty = json.dumps(response, indent=2, ensure_ascii=False)
                        print(f'[수신] {pretty}')
                    
                    # 로그 저장
                    log_path = log_websocket_message(response, direction='recv')
                    print(f'[로그] {log_path}')
                    
                    # DB 저장
                    try:
                        saved_count = ws_db.save_websocket_realtime(response)
                        if saved_count > 0:
                            print(f'[DB 저장] {saved_count} 행 저장됨')
                    except Exception as exc:
                        print(f'[DB 저장 오류] {exc}')

            except websockets.ConnectionClosed:
                print('[연결 종료] 서버와의 연결이 끊어졌습니다.')
                self.connected = False
                if not self._login_event.is_set():
                    self._login_event.set()
                break
            except Exception as exc:
                print(f'[수신 오류] {exc}')
                if not self._login_event.is_set():
                    self._login_event.set()
                break

    # ────────────────────────────────
    # 실행 / 종료
    # ────────────────────────────────
    async def run(self):
        """연결 후 메시지 수신을 시작합니다."""
        await self.connect()
        await self.receive_messages()

    async def disconnect(self):
        """WebSocket 연결을 안전하게 종료합니다."""
        self.keep_running = False
        if self.connected and self.websocket:
            await self.websocket.close()
            self.connected = False
            print('[연결 해제] WebSocket 서버와의 연결이 종료되었습니다.')
