# kiwoom rest api
대한민국 증권사인 키움증권의 REST API를 이용한 주식 자동 매매 프로그램이다.

## API 공식 문서
- https://openapi.kiwoom.com/guide/apiguide

## API 사용 신청 절차
- 키움증권 계좌 개설
- API 사용 신청
- 모의투자 신청
- 모의투자 API 사용 신청

## 개발 사양
- 개발언어 : Python
- 개발IDE : VSCode
- DB : MariaDB
- OS : Windows

## 개발환경 구성

### 1. python 설치
```
python --version
```

### 1. pip 업데이트 (권장)
```
python -m pip install --upgrade pip
```

### 1. python 가상환경 구성
```
python -m venv .venv

.\.venv\Scripts\activate
```

### 2. 필수 라이브러리 설치
```
pip install -r requirements.txt
```

---

## 실행 방식 비교: run_main.bat vs run_fastapi.bat

### 개요

| 항목 | `run_main.bat` | `run_fastapi.bat` |
|---|---|---|
| 진입점 | `src/main.py` | `src/app/main.py` (uvicorn) |
| 실행 방식 | 터미널 CLI 대화형 | HTTP 서버 (REST API) |
| 인터페이스 | 콘솔 메뉴 (stdin/stdout) | HTTP 요청/응답 (JSON) |
| 동시 처리 | 단일 사용자, 순차 처리 | 다중 클라이언트, 비동기 처리 |
| 포트 | 없음 | 8000 (0.0.0.0) |

---

### run_main.bat — CLI 대화형 방식

```bat
call %BASE_DIR%\.venv\Scripts\activate
set PYTHONPATH=%BASE_DIR%\src
python %BASE_DIR%\src\main.py
deactivate
```

**요청 처리 흐름**

```
사용자 키보드 입력 (stdin)
    → main.py: 메뉴 루프 (while True)
        → 메뉴 선택 → 해당 함수 호출 (예: print_prev_volume_rank)
            → 키움증권 REST API 직접 호출 (requests / httpx)
                → 결과를 콘솔(stdout)에 출력
```

**특징**

- `src/main.py`가 직접 실행됨 — 별도 웹 프레임워크 없음
- `PYTHONPATH=src`로 설정하여 모듈 임포트 경로 해결
- 사용자가 번호를 입력할 때마다 순차적으로 API를 호출하고 결과를 출력
- 한 번에 한 작업만 처리 (단일 스레드, blocking I/O)
- 토큰 발급 → 메뉴 루프 → 토큰 반납의 생명주기
- 웹소켓 실시간 시세는 백그라운드 스레드로 병행 가능

---

### run_fastapi.bat — HTTP 서버 방식

```bat
cd /d "%BASE_DIR%\src"
"%VENV_PYTHON%" -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**요청 처리 흐름**

```
클라이언트 HTTP 요청 (curl / Invoke-RestMethod / 브라우저 등)
    → uvicorn (ASGI 서버): 요청 수신 및 비동기 디스패치
        → FastAPI 라우터: 경로 매핑 → 엔드포인트 핸들러 호출
            → 미들웨어: 요청 로깅 (request_logging_middleware)
                → 서비스 레이어: 키움증권 REST API 비동기 호출 (httpx AsyncClient)
                    → JSON 응답 반환 (HTTP 200 / 4xx / 5xx)
```

**특징**

- `uvicorn`이 ASGI 서버로 `app.main:app` 팩토리 패턴을 로드
- `--reload` 옵션: 소스 파일 변경 시 자동 재시작 (개발용)
- `0.0.0.0:8000` 바인딩: 로컬 및 네트워크 외부 접근 허용
- 비동기(`async/await`) 처리 — 다수 요청을 동시에 처리 가능
- 미들웨어, 예외 핸들러, 라우터가 계층적으로 분리됨
- Swagger UI (`/docs`), ReDoc (`/redoc`) 자동 제공
- 가상환경 python 존재 여부를 사전 검증 후 실행

---

### 핵심 차이: 요청과 응답 처리 방식

| 구분 | run_main.bat | run_fastapi.bat |
|---|---|---|
| **요청 입력** | `input()` — 키보드 stdin | HTTP 메서드 + URL + JSON Body |
| **응답 출력** | `print()` — 콘솔 stdout | HTTP 응답 (JSON, 상태 코드) |
| **I/O 모델** | 동기 blocking | 비동기 non-blocking (asyncio) |
| **오류 처리** | try/except → 콘솔 메시지 | HTTP 예외 핸들러 → JSON 에러 응답 |
| **확장성** | 단일 사용자 전용 | 다중 클라이언트 동시 접속 가능 |
| **토큰 관리** | 실행 시 1회 발급, 종료 시 반납 | 요청마다 또는 캐시 방식으로 관리 |
| **인증** | 파일에서 API 키 읽어 토큰 발급 | `app.core.config` 설정 기반 관리 |
| **재시작** | 프로세스 종료 후 재실행 | `--reload`로 코드 변경 시 자동 반영 |

---

## 토큰 요청 프로세스 비교: run_main.bat vs run_fastapi.bat

### run_main.bat — 프로세스 시작 시 1회 발급

**흐름**

```
프로세스 시작 (main.py::main())
    │
    ├─ load_api_keys()
    │     └─ conf/{계좌번호}_appkey.txt / _secretkey.txt 파일에서 키 읽기
    │         서버 모드(실전/모의)에 따라 계좌번호 자동 선택
    │             실전: 65120003 / 모의: 81241972
    │
    ├─ get_access_token(app_key, app_secret)   ← oauth2/kiwoom_oauth2.py
    │     │
    │     ├─ [1단계] DB 캐시 조회: get_unrevoked_token(app_key)
    │     │     ├─ 미폐기 토큰 있음 → 즉시 반환 (서버 요청 없음)
    │     │     └─ 없음 → [2단계]로
    │     │
    │     └─ [2단계] 신규 발급: POST /oauth2/token
    │           Body: { grant_type, appkey, secretkey }
    │           응답: { token, token_type, expires_dt, return_code, return_msg }
    │           → save_au10001_response() → DB(au10001) 저장
    │           → token 반환
    │
    ├─ token 변수에 보관 → 메뉴 루프 전체에서 공유
    │     fn(token)  ← 각 기능 함수에 인자로 전달
    │
    └─ [프로세스 종료 시] finally 블록
          revoke_access_token(app_key, app_secret, token)
              POST /oauth2/revoke → DB(au10002) 저장
```

**특징**

| 항목 | 내용 |
|---|---|
| 발급 시점 | 프로세스 시작 시 **1회** |
| 토큰 보관 | 메모리 변수 (`token`) |
| 전달 방식 | 함수 인자 `fn(token)` |
| 폐기 시점 | 프로세스 종료 시 `finally` 블록 |
| 실패 처리 | `sys.exit(1)` — 프로세스 강제 종료 |
| 캐시 조회 | DB에서 미폐기 토큰 재사용 가능 |

---

### run_fastapi.bat — HTTP 엔드포인트로 분리된 토큰 관리

**흐름**

```
클라이언트: POST /api/v1/auth/token/issue
    Body: { "server_mode": "real" | "mock", "reuse_cached": true }
    │
    └─ TokenService.issue_token(server_mode, reuse_cached)
          │
          ├─ _host_for_mode(server_mode)
          │     real → https://api.kiwoom.com
          │     mock → https://mockapi.kiwoom.com
          │
          ├─ load_api_keys(host=host)
          │     서버 모드에 따라 계좌번호 자동 선택
          │
          ├─ [1단계] reuse_cached=True → get_unrevoked_token(app_key)
          │     미폐기 토큰 있음 → TokenIssueResponse(reused_cached_token=True) 즉시 반환
          │
          └─ [2단계] 신규 발급: POST /oauth2/token  (timeout=15s)
                성공 → save_au10001_response() → DB 저장
                       → TokenIssueResponse JSON 반환 (HTTP 200)
                실패 → ApiError → HTTP 502 (키움 서버 오류)
                     → HTTP 500 (DB 저장 실패)
                     → HTTP 400 (잘못된 server_mode)

클라이언트: POST /api/v1/auth/token/revoke
    Body: { "server_mode": "real", "token": "(선택, 없으면 DB 캐시 사용)" }
    │
    └─ TokenService.revoke_token(server_mode, token)
          │
          ├─ token 미제공 → get_unrevoked_token() 캐시 조회
          │     없음 → HTTP 404
          │
          └─ POST /oauth2/revoke
                성공 → TokenRevokeResponse JSON (HTTP 200)
                실패 → ApiError → HTTP 502 / 500
```

**특징**

| 항목 | 내용 |
|---|---|
| 발급 시점 | 클라이언트 **명시적 HTTP 요청** 시 |
| 토큰 보관 | 클라이언트가 응답 JSON에서 직접 수령 |
| 전달 방식 | 이후 API 요청의 `Authorization: Bearer {token}` 헤더 |
| 폐기 시점 | 클라이언트가 명시적 revoke 요청 시 |
| 실패 처리 | HTTP 상태 코드 (400 / 404 / 500 / 502) + JSON 에러 |
| 캐시 조회 | `reuse_cached` 파라미터로 제어 가능 |
| 타임아웃 | 키움 서버 요청에 `timeout=15s` 적용 |

---

### 핵심 차이 요약: 토큰 프로세스

| 구분 | run_main.bat | run_fastapi.bat |
|---|---|---|
| **발급 주체** | `main()` 함수가 자동 발급 | 클라이언트가 HTTP 요청으로 요청 |
| **발급 시점** | 프로세스 시작 시 1회 | HTTP 호출 시마다 (또는 캐시 재사용) |
| **토큰 수명** | 프로세스 전체 생명주기 | 클라이언트가 직접 관리 |
| **전달 방식** | 함수 인자 `fn(token)` | `Authorization: Bearer` 헤더 |
| **폐기 방식** | `finally` 블록 자동 폐기 | 클라이언트가 revoke API 명시적 호출 |
| **실패 시** | `sys.exit(1)` 프로세스 종료 | HTTP 에러 코드 반환, 서버 계속 운영 |
| **server_mode** | `HOST` 전역 상수로 고정 | 요청 body의 `server_mode` 파라미터로 동적 지정 |


