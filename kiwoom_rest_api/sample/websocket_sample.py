"""
키움증권 WebSocket API 샘플 코드
- 실시간 주식 시세 수신 예제
"""

import asyncio
import websockets
import json

# ============================================================
# 서버 설정
# ============================================================
SOCKET_URL = 'wss://api.kiwoom.com:10000/api/dostk/websocket'

# TODO: 토큰 발급 후 실제 액세스 토큰으로 교체하세요.
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'


# ============================================================
# WebSocket 클라이언트
# ============================================================
class WebSocketClient:
    def __init__(self, uri: str):
        self.uri = uri
        self.websocket = None
        self.connected = False
        self.keep_running = True

    # --------------------------------------------------------
    # 서버 연결 및 로그인
    # --------------------------------------------------------
    async def connect(self):
        """WebSocket 서버에 연결하고 로그인 패킷을 전송합니다."""
        try:
            self.websocket = await websockets.connect(self.uri)
            self.connected = True
            print('서버와 연결을 시도 중입니다.')

            # 로그인 패킷 전송
            login_packet = {
                'trnm': 'LOGIN',
                'token': ACCESS_TOKEN,
            }
            print('실시간 시세 서버로 로그인 패킷을 전송합니다.')
            await self.send_message(login_packet)

        except Exception as e:
            print(f'연결 오류: {e}')
            self.connected = False

    # --------------------------------------------------------
    # 메시지 송신
    # --------------------------------------------------------
    async def send_message(self, message):
        """
        서버로 메시지를 전송합니다.
        연결이 끊어진 경우 자동으로 재연결을 시도합니다.

        Parameters
        ----------
        message : dict | str
            전송할 메시지 (dict이면 JSON으로 직렬화)
        """
        if not self.connected:
            await self.connect()

        if self.connected:
            if not isinstance(message, str):
                message = json.dumps(message)

            await self.websocket.send(message)
            print(f'[송신] {message}')

    # --------------------------------------------------------
    # 메시지 수신
    # --------------------------------------------------------
    async def receive_messages(self):
        """서버로부터 메시지를 지속적으로 수신합니다."""
        while self.keep_running:
            try:
                raw = await self.websocket.recv()
                response = json.loads(raw)

                trnm = response.get('trnm', '')

                # 로그인 응답 처리
                if trnm == 'LOGIN':
                    if response.get('return_code') != 0:
                        print(f'로그인 실패: {response.get("return_msg")}')
                        await self.disconnect()
                    else:
                        print('로그인 성공하였습니다.')

                # PING 응답 처리 (서버 연결 유지)
                elif trnm == 'PING':
                    await self.send_message(response)

                # 실시간 시세 데이터 출력
                else:
                    print(f'[수신] {json.dumps(response, indent=2, ensure_ascii=False)}')

            except websockets.ConnectionClosed:
                print('서버와의 연결이 종료되었습니다.')
                self.connected = False
                break
            except Exception as e:
                print(f'수신 오류: {e}')
                break

    # --------------------------------------------------------
    # 실행 진입점
    # --------------------------------------------------------
    async def run(self):
        """연결 후 메시지 수신을 시작합니다."""
        await self.connect()
        await self.receive_messages()

    # --------------------------------------------------------
    # 연결 종료
    # --------------------------------------------------------
    async def disconnect(self):
        """WebSocket 연결을 안전하게 종료합니다."""
        self.keep_running = False
        if self.connected and self.websocket:
            await self.websocket.close()
            self.connected = False
            print('WebSocket 서버와의 연결이 종료되었습니다.')


# ============================================================
# 실시간 항목 등록 헬퍼
# ============================================================
async def register_realtime(client: WebSocketClient, stock_codes: list, realtime_types: list, group_no: str = '1'):
    """
    실시간 시세 항목을 등록합니다.

    Parameters
    ----------
    client : WebSocketClient
        연결된 WebSocket 클라이언트
    stock_codes : list
        실시간 등록할 종목 코드 목록 (예: ['039490', '005930'])
    realtime_types : list
        실시간 항목 유형 목록 (예: ['0B'] - 주식 체결)
    group_no : str
        그룹 번호 (기본값: '1')
    """
    await client.send_message({
        'trnm': 'REG',          # 서비스명: 실시간 등록
        'grp_no': group_no,     # 그룹 번호
        'refresh': '1',         # 기존 등록 유지 여부 (1: 유지)
        'data': [{
            'item': stock_codes,       # 종목 코드 목록
            'type': realtime_types,    # 실시간 항목 유형
        }],
    })


# ============================================================
# 메인 실행
# ============================================================
async def main():
    client = WebSocketClient(SOCKET_URL)

    # WebSocket 수신 태스크를 백그라운드로 실행
    receive_task = asyncio.create_task(client.run())

    # 연결 및 로그인 완료 대기
    await asyncio.sleep(1)

    # 실시간 시세 등록: 키움증권(039490) 주식 체결(0B)
    await register_realtime(
        client=client,
        stock_codes=['039490'],
        realtime_types=['0B'],
    )

    # 수신 태스크 종료 대기
    await receive_task


if __name__ == '__main__':
    asyncio.run(main())
