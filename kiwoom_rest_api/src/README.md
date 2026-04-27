# 키움증권 REST API – 전체 프로세스 흐름

## 1. 시작 / 토큰 발급

```
main.py::main()
  │
  ├─ load_api_keys()          conf/{계좌번호}_appkey.txt / _secretkey.txt 읽기
  │
  ├─ get_access_token()       oauth2/kiwoom_oauth2.py
  │     │
  │     ├─ get_unrevoked_token(app_key)   DB(au10001/au10002) 미폐기 토큰 조회
  │     │     ├─ 있음 → 기존 토큰 반환 (서버 요청 없음)
  │     │     └─ 없음 → POST /oauth2/token 발급 → save_au10001_response() DB 저장
  │     │
  │     └─ token 반환
  │
  └─ 메뉴 루프 진입
```

---

## 2. 메인 메뉴 구조

```
╔══════════════════════════════╗
║     키움 REST API 메뉴       ║
╠══════════════════════════════╣
║  [1] 업종                    ║  → 업종현재가 조회 (ka20001)
║  [2] 계좌                    ║  → 계좌 관련 API (run_account_api_menu)
║  [3] 거래량                  ║  → 거래량 관련 7종 API
║  [4] 주문                    ║  → 주문 관련 API (run_order_api_menu)
║  [5] 웹소켓                  ║  → WebSocket 실시간 (백그라운드)
║  [0] 종료                    ║
╚══════════════════════════════╝
```

각 카테고리 선택 시:
- **callable(sub_items)** (계좌·주문): `sub_items(token)` 직접 호출 후 반환
- **list(sub_items)** (업종·거래량·웹소켓): 하위 메뉴 루프 진입

---

## 3. REST API 요청/응답 흐름 (업종·거래량 공통)

```
사용자 입력 (종목코드, 날짜 등)
  │
  ▼
fn(token)  예) print_sector_price(token)
  │
  ├─ 요청 헤더 조립
  │     authorization: Bearer {token}
  │     api-id: {ka20001 등}
  │     Content-Type: application/json;charset=UTF-8
  │
  ├─ requests.post(HOST + "/api/dostk/sect", headers, json=body)
  │
  └─ 응답 출력 (print_response)
        return_code / return_msg 확인
        data 필드 → 테이블 형태로 출력
```

### 연속 조회

```
응답 헤더 cont-yn == 'Y'
  │
  └─ 사용자에게 계속 여부 확인 → 'Y' 입력 시
        next-key 값을 다음 요청 헤더에 포함
        반복 요청
```

---

## 4. WebSocket 실시간 – 포그라운드 모드 (독립 실행: run_websocket.bat)

```
websocket.py::main()
  │
  ├─ 토큰 발급 (get_access_token)
  │
  └─ run_websocket_menu(token)   websocket/menu.py
        │
        ├─ [1] run_realtime_quote(token)     종목 시세
        ├─ [2] run_account_realtime(token)   계좌/기타
        └─ [3] run_condition_search(token)   조건검색
```

#### 종목 실시간 시세 / 계좌 실시간 흐름

```
run_realtime_quote(token)
  │
  ├─ 사용자 입력: 종목코드, 실시간 타입 선택
  │
  └─ asyncio.run(_run_realtime_quote(token, items, types))
        │
        └─ _run_session(token, items, types)
              │
              ├─ WebSocketClient(SOCKET_URL, token)
              │     silent=False  → 모든 로그 화면 출력
              │
              ├─ receive_task = create_task(client.run())
              │     ├─ client.connect()
              │     │     └─ websockets.connect(wss://...)
              │     │         └─ send {"trnm":"LOGIN","token":...}
              │     └─ client.receive_messages()  ← 루프
              │           ├─ trnm==LOGIN  → 로그인 성공/실패 처리
              │           ├─ trnm==PING   → 그대로 echo 송신
              │           └─ trnm==REAL   → on_message() 또는 print
              │                             log_websocket_message() 파일 로그
              │                             ws_db.save_websocket_realtime() DB 저장
              │
              ├─ wait_for_login(timeout=5)
              │
              ├─ register(client, types, items)
              │     └─ send {"trnm":"REG","grp_no":"1","data":[...]}
              │
              ├─ command_task = create_task(_command_loop())
              │     └─ asyncio.to_thread(input, ...) 로 키보드 대기
              │
              └─ asyncio.wait({receive_task, command_task}, FIRST_COMPLETED)
                    ├─ command_task 완료 (q 입력) → disconnect() → 종료
                    └─ receive_task 완료 (서버 끊김) → 종료
```

#### 조건검색 흐름

```
run_condition_search(token)
  │
  └─ asyncio.run(_run_condition(token))
        │
        ├─ WebSocketClient 연결 / 로그인
        │
        ├─ get_condition_list()   send {"trnm":"CNSRLST"}
        │     └─ 응답: {"trnm":"CNSRLST","data":[["seq","조건명"],...]}
        │
        ├─ 사용자 입력: 일련번호, 조회 방식 (1:일반 / 2:실시간)
        │
        ├─ [일반조회]
        │     request_condition()   send {"trnm":"CNSRREQ","search_type":"0",...}
        │     응답 수신 후 종료
        │
        └─ [실시간]
              request_condition_realtime()   send {"trnm":"CNSRREQ","search_type":"1",...}
              수신 루프 (q 입력 시)
                └─ remove_condition_realtime()   send {"trnm":"CNSRCLR",...}
                   disconnect() → 종료
```

---

## 5. WebSocket 실시간 – 백그라운드 모드 (main.py 메뉴 [5])

REST API와 **동시에** 실시간 데이터를 수신하는 구조입니다.

```
main.py 메뉴 [5] 웹소켓
  │
  ├─ [1] run_realtime_quote_bg(token)    종목 시세 백그라운드 시작
  ├─ [2] run_account_realtime_bg(token)  계좌/기타 백그라운드 시작
  ├─ [3] run_condition_search(token)     조건검색 (포그라운드 – 블로킹)
  └─ [4] stop_realtime_background()     백그라운드 종료
```

#### 백그라운드 시작 흐름

```
run_realtime_quote_bg(token)
  │
  ├─ is_realtime_running() 확인  →  이미 실행 중이면 중단
  │
  ├─ 사용자 입력: 종목코드, 실시간 타입
  │
  └─ _launch_background(token, items, types)
        │
        ├─ _bg_stop_event = threading.Event()
        │
        └─ threading.Thread(target=_run, daemon=True, name='ws-bg').start()
              │
              └─ _run()
                    asyncio.new_event_loop()  ← 메인 스레드와 독립된 이벤트 루프
                    loop.run_until_complete(
                      _run_session_background(token, items, types, stop_event)
                    )

                    _run_session_background():
                      ├─ WebSocketClient(SOCKET_URL, token, silent=True)
                      │     silent=True → 수신 데이터 화면 출력 없음
                      │     파일 로그 / DB 저장은 정상 동작
                      ├─ 로그인 / register (포그라운드와 동일)
                      └─ while not stop_event.is_set():
                              asyncio.wait({receive_task}, timeout=0.5)
```

#### REST API와 동시 실행 가능한 이유

```
메인 스레드                         백그라운드 스레드 (ws-bg)
─────────────────────────────────   ─────────────────────────────────
main() 메뉴 루프 (동기)              asyncio 이벤트 루프 (독립)
  │                                   │
  ├─ input() 대기                      ├─ WebSocket 수신 루프
  ├─ REST API 호출 (requests)          ├─ DB 저장
  └─ 화면 출력                         └─ 파일 로그
                                       (화면 출력 없음: silent=True)
```

- 키움증권 서버는 **동일 토큰**으로 WebSocket + REST API 동시 호출 지원
- WebSocket: `wss://api.kiwoom.com:10000` (별도 TCP 연결)
- REST API: `https://api.kiwoom.com` (HTTP 요청)

#### 백그라운드 종료 흐름

```
stop_realtime_background()
  │
  ├─ _bg_stop_event.set()      stop_event 플래그 설정
  │
  ├─ _bg_thread.join(timeout=5)
  │     백그라운드 루프: stop_event.is_set() → True → while 탈출
  │     client.disconnect() → websocket.close()
  │
  └─ _bg_thread = None         상태 초기화
```

---

## 6. 수신 데이터 처리 파이프라인

```
WebSocket 서버
  │  {"trnm":"REAL","data":[{"type":"0B","item":"005930","values":{...}},...]}
  ▼
client.receive_messages()
  │
  ├─ trnm == LOGIN / PING  →  제어 처리 (DB 저장 없음)
  │
  └─ trnm == REAL (실시간 데이터)
        │
        ├─ on_message(response)  또는  print (silent=False 시)
        │
        ├─ log_websocket_message(response, direction='recv')
        │     → log/YYYYMMDD_websocket.log 파일 저장
        │
        └─ ws_db.save_websocket_realtime(response)
              │
              ├─ trnm in (LOGIN, PING, REG, SYSTEM,
              │           CNSRLST, CNSRREQ, CNSRCLR)  →  skip
              │
              ├─ trnm == REAL
              │     data[].type 기준으로 항목별 분리
              │     _TABLE_MAPPING[type] → 테이블명
              │     _parse_response_data() → INSERT rows
              │     _insert_rows(table_name, rows)  → MariaDB
              │
              └─ 그 외 trnm  →  save_websocket_data(trnm, response)
                    _TABLE_MAPPING[trnm] 없으면 → 저장 오류 출력
```

---

## 7. 프로그램 종료

```
main() finally 블록
  │
  └─ revoke_access_token(app_key, app_secret, token)
        POST /oauth2/revoke
        save_au10002_response()  →  DB au10002 테이블 폐기 이력 저장
```

> 백그라운드 WebSocket 스레드는 `daemon=True` 이므로 메인 프로세스 종료 시 자동 소멸됩니다.
> 단, 정상 종료 흐름에서는 `stop_realtime_background()` 호출 또는 프로그램 종료 시 자동 종료됩니다.

---

## 8. 주요 파일 구조

```
src/
├─ main.py                  메인 진입점, 메뉴 루프, 토큰 관리
├─ websocket.py             WebSocket 동기 진입점 (포그라운드 + 백그라운드)
├─ websocket/
│   ├─ client.py            WebSocketClient (연결/로그인/송수신/종료, silent 옵션)
│   ├─ realtime.py          register / remove (REG 패킷 조립)
│   ├─ condition.py         조건검색 CNSRLST / CNSRREQ / CNSRCLR
│   ├─ db.py                실시간 데이터 MariaDB 저장
│   ├─ menu.py              WebSocket 전용 메뉴 (독립 실행용)
│   └─ main.py              websocket.py 함수 re-export 래퍼
├─ oauth2/
│   ├─ kiwoom_oauth2.py     토큰 발급/폐기, 서버 상수
│   └─ oauth.py             DB 미폐기 토큰 조회, au10001/au10002 저장
├─ acnt/                    계좌 관련 API
├─ ordr/                    주문 관련 API
├─ sect/                    업종 관련 API
└─ volume/                  거래량 관련 API
```
