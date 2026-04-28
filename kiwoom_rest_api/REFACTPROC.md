# FastAPI 구조로 리펙토링

**권장 아키텍처**
1. app/api  
REST 엔드포인트 라우터 (sect, volume, acnt, order, ws-control)

2. app/services  
키움 호출 서비스, 토큰 서비스, WebSocket 세션 매니저

3. app/repositories  
DB 저장 로직 캡슐화

4. app/schemas  
Pydantic 요청/응답 모델

5. app/core  
설정, 로깅, 예외 처리, 의존성 주입

**현실적인 마이그레이션 순서**
1. 1단계: FastAPI 뼈대 + 헬스체크 + 공통 예외/로깅
2. 2단계: 인증/토큰 서비스 이관
3. 3단계: 조회성 REST API(업종/거래량)부터 엔드포인트화
4. 4단계: 계좌/주문 API 이관
5. 5단계: WebSocket 제어 API(시작/중지/상태) 추가
6. 6단계: 필요 시 비동기 I/O와 작업 큐 도입

## 진행 현황

- [x] 1단계: FastAPI 뼈대 + 헬스체크 + 공통 예외/로깅
- [x] 2단계: 인증/토큰 서비스 이관
- [x] 3단계: 조회성 REST API(업종/거래량)부터 엔드포인트화
- [x] 4단계: 계좌/주문 API 이관
- [x] 5단계: WebSocket 제어 API(시작/중지/상태) 추가
- [x] 6단계: 필요 시 비동기 I/O와 작업 큐 도입

## 1단계 산출물

### 추가된 경로

- src/app/main.py
- src/app/api/router.py
- src/app/api/routes/health.py
- src/app/api/routes/auth.py
- src/app/core/config.py
- src/app/core/logging.py
- src/app/core/exceptions.py
- src/app/services/token_service.py
- src/app/schemas/auth.py
- scripts/run_fastapi.bat
- requirements-fastapi.txt

### 실행 방법

1. 의존성 설치

```powershell
pip install -r requirements-fastapi.txt
```

2. 서버 실행

```powershell
scripts\run_fastapi.bat
```

3. 확인 URL

- 루트: http://localhost:8000/
- 헬스체크: http://localhost:8000/api/v1/health
- 토큰 상태 조회: http://localhost:8000/api/v1/auth/token?server_mode=real
- Swagger: http://localhost:8000/docs

## 2단계 산출물

### 추가된 엔드포인트

- GET /api/v1/auth/token
- POST /api/v1/auth/token
- POST /api/v1/auth/token/revoke

### 엔드포인트 요약

1. GET /api/v1/auth/token
- DB에 저장된 미폐기 토큰 존재 여부를 조회합니다.
- `server_mode=real|mock` 쿼리 지원

2. POST /api/v1/auth/token
- 키움 접근 토큰을 발급합니다.
- 기본적으로 DB의 미폐기 토큰이 있으면 재사용합니다.
- 요청 예시:

```json
{
  "server_mode": "real",
  "reuse_cached": true
}
```

3. POST /api/v1/auth/token/revoke
- 전달된 토큰 또는 DB의 현재 미폐기 토큰을 폐기합니다.
- 요청 예시:

```json
{
  "server_mode": "real",
  "token": null
}
```

### 검증 메모

- `app.main` import 성공
- 등록 라우트 확인: `/api/v1/auth/token`, `/api/v1/auth/token/revoke`, `/api/v1/health`

## 3단계 산출물

### 추가된 파일

- src/app/services/kiwoom_client.py — Kiwoom API 공통 HTTP 클라이언트 (print 의존성 없음)
- src/app/schemas/sect.py — 업종 요청/응답 Pydantic 모델
- src/app/schemas/volume.py — 거래량 요청/응답 Pydantic 모델
- src/app/services/sect_service.py — 업종 서비스 (ka20001)
- src/app/services/volume_service.py — 거래량 서비스 (ka10023/30/31/32/24/52/55)
- src/app/api/routes/sect.py — 업종 라우터
- src/app/api/routes/volume.py — 거래량 라우터

### 추가된 엔드포인트 (전체 17개 라우트)

| 엔드포인트 | API ID | 설명 |
|---|---|---|
| GET /api/v1/sect/current-price | ka20001 | 업종현재가요청 |
| GET /api/v1/volume/surge | ka10023 | 거래량급증요청 |
| GET /api/v1/volume/today-rank | ka10030 | 당일거래량상위 |
| GET /api/v1/volume/prev-rank | ka10031 | 전일거래량상위 |
| GET /api/v1/volume/trade-amount-rank | ka10032 | 거래대금상위 |
| GET /api/v1/volume/update | ka10024 | 거래량갱신요청 |
| GET /api/v1/volume/broker-instant | ka10052 | 거래원순간거래량 |
| GET /api/v1/volume/today-prev-contracts | ka10055 | 당일전일체결량 |

### 검증 메모

- 모든 6개 신규 파일 오류 없음 확인
- import 검증: 17개 라우트 정상 등록 확인

**예상 공수 (대략)**
1. 최소 MVP(조회 API + 토큰 + 기본 로깅): 3~5일
2. 계좌/주문 + DB 저장 + 운영형 예외 처리: 1~2주
3. WebSocket 제어/모니터링까지 포함: 2~3주

## 4단계 산출물

### 추가된 파일

- src/app/schemas/acnt.py — 계좌 요청/응답 Pydantic 모델
- src/app/schemas/ordr.py — 주문 요청/응답 Pydantic 모델 + 주문 변경 API 목록
- src/app/services/acnt_service.py — 계좌 서비스 (33개 API 범용 처리)
- src/app/services/ordr_service.py — 주문 서비스 (8개 API + confirm 안전장치)
- src/app/api/routes/acnt.py — 계좌 라우터
- src/app/api/routes/ordr.py — 주문 라우터

### 추가된 엔드포인트 (총 16개 라우트)

| 엔드포인트 | 설명 |
|---|---|
| GET /api/v1/acnt/specs | 계좌 API 스펙 목록 (33개) |
| POST /api/v1/acnt/{api_id} | 계좌 API 범용 호출 |
| GET /api/v1/ordr/specs | 주문 API 스펙 목록 (8개) |
| POST /api/v1/ordr/{api_id} | 주문 API 범용 호출 |

### 주요 설계 결정

- 계좌(33개)·주문(8개) 모두 범용 `POST /{api_id}` 단일 엔드포인트로 처리
- 주문 변경 API (kt10000/kt10001/kt10002/kt10003/kt50000~kt50003) 호출 시 `confirm=true` 필수 (실 매매 이중 확인)
- API 스펙 유효성 검증: 등록되지 않은 api_id 400 에러 반환
- 기존 acnt.acnt / ordr.ordr CLI 코드 무손상 유지

### 검증 메모

- import 검증: 16개 라우트 정상 등록 확인
  - /acnt/specs, /acnt/{api_id}
  - /ordr/specs, /ordr/{api_id}

## 5단계 산출물

### 추가된 파일

- src/app/schemas/ws.py — WebSocket 세션 제어 스키마 + 실시간 타입 맵
- src/app/services/ws_manager.py — `WsSessionManager` 싱글턴 (백그라운드 스레드 관리)
- src/app/api/routes/ws.py — WebSocket 세션 제어 라우터

### 추가된 엔드포인트

| 엔드포인트 | 설명 |
|---|---|
| GET /api/v1/ws/types | 실시간 타입 코드 목록 (19종) |
| GET /api/v1/ws/status | 세션 상태 (running, items, types, started_at) |
| POST /api/v1/ws/start | 백그라운드 WebSocket 세션 시작 |
| POST /api/v1/ws/stop | 백그라운드 세션 중지 |
| POST /api/v1/ws/register | 실행 중 세션에 실시간 항목 추가 (trnm=REG) |
| DELETE /api/v1/ws/register | 실행 중 세션에서 실시간 항목 해제 (trnm=REMOVE) |

### 주요 설계 결정

- `WsSessionManager` 모듈 레벨 싱글턴 — FastAPI 프로세스 당 단일 세션
- 백그라운드 스레드에 자체 asyncio 이벤트 루프 — `asyncio.run_coroutine_threadsafe`로 add/remove 호출
- 중복 시작/없는데 중지 시 409 에러
- 기존 websocket.py CLI 코드 무손상 유지

### 검증 메모

- import 검증: 총 22개 라우트 정상 등록
  - /ws/types, /ws/status, /ws/start, /ws/stop, /ws/register (POST/DELETE)

## 6단계 산출물

### 변경된 파일

- `requirements-fastapi.txt` — `httpx>=0.27.0,<1.0.0` 추가
- `src/app/services/kiwoom_client.py` — `requests` 제거 → `httpx.AsyncClient` 기반 `async def kiwoom_post`
- `src/app/services/sect_service.py` — `get_current_price` → `async def`
- `src/app/services/volume_service.py` — 7개 메서드 → `async def`
- `src/app/services/acnt_service.py` — `call` → `async def`
- `src/app/services/ordr_service.py` — `call` → `async def`
- `src/app/api/routes/sect.py` — 핸들러 → `async def` + `await`
- `src/app/api/routes/volume.py` — 7개 핸들러 → `async def` + `await`
- `src/app/api/routes/acnt.py` — 핸들러 → `async def` + `await`
- `src/app/api/routes/ordr.py` — 핸들러 → `async def` + `await`

### 주요 설계 결정

- `httpx.AsyncClient(timeout=30)` — 요청마다 생성 (컨텍스트 매니저)
- `requests.HTTPError` → `httpx.HTTPStatusError`, `requests.RequestException` → `httpx.RequestError`
- `ws_manager.py` 백그라운드 스레드는 자체 asyncio 루프를 사용하므로 변경 대상 제외
- 작업 큐(Celery/ARQ)는 현재 불필요하므로 도입 생략

### 검증 메모

- import 검증: 총 27개 라우트 정상 등록 확인

## 통합테스트

### 개요

서버를 실행한 상태에서 `curl.exe` 또는 브라우저(Swagger UI)로 각 엔드포인트를 검증합니다.  
**모든 조회/주문 API는 유효한 액세스 토큰이 DB에 캐시되어 있어야 합니다.**  
테스트 순서: 서버 기동 → 인증 토큰 발급 → 조회 API → WebSocket 세션 → 주문 API (모의투자)

---

### 사전 준비

#### powershell 설정
```
chcp 65001
[Console]::InputEncoding  = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [Console]::OutputEncoding
```

#### 서버 기동

```bat
cd d:\app\IronSyncroWealth\kiwoom_rest_api
scripts\run_fastapi.bat
```

정상 기동 확인 로그:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---
> Swagger UI: Swagger UI는 API 문서를 웹 화면으로 보여주고, 바로 테스트까지 할 수 있게 해주는 인터페이스입니다.  
> API 명세(OpenAPI)를 사람이 읽기 쉽게 화면으로 표시  
> 1. 각 엔드포인트의 요청 파라미터/응답 스키마를 확인  
> 2. 브라우저에서 직접 Try it out으로 호출 테스트 가능  
> 3. 즉, “백엔드 API 설명서 + 테스트 콘솔”이라고 보면 됩니다.  
> ReDoc: ReDoc은 OpenAPI 스펙을 읽기 중심으로 정리해 보여주는 정적 문서 UI입니다.  
> 1. 엔드포인트를 카테고리별로 길게 탐색하기 좋음  
> 2. 요청/응답 스키마, 필드 설명, 예시를 문서처럼 확인 가능  
> 3. 즉, “배포/공유용 API 레퍼런스 문서”에 더 적합합니다.

### 명령 표기 규칙 (curl.exe + Invoke-RestMethod)

아래 통합테스트는 `curl.exe`와 `Invoke-RestMethod`를 함께 사용할 수 있습니다.

```powershell
# GET 예시
curl.exe -s "http://localhost:8000/api/v1/health"
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/health" -Method Get

# POST(JSON) 예시
curl.exe -s -X POST "http://localhost:8000/api/v1/auth/token" -H "Content-Type: application/json" --data-raw "{\"server_mode\":\"real\",\"reuse_cached\":true}"
$body = @{ server_mode = "real"; reuse_cached = $true } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token" -Method Post -ContentType "application/json" -Body $body
```

> 참고: PowerShell에서는 JSON 본문 전달 안정성을 위해 `Invoke-RestMethod` 사용을 권장합니다.


### TC-01 헬스체크

**목적**: 서버가 정상 응답하는지 확인합니다.

```powershell
curl.exe -s http://localhost:8000/api/v1/health
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/health" -Method Get
```

**예상 응답 (200 OK)**:

```json
{
  "status": "ok",
  "timestamp_utc": "2026-04-28T10:00:00.000000+00:00"
}
```

**검증 항목**:
- `status` 가 `"ok"` 인지 확인
- `timestamp_utc` 가 현재 시각 근처인지 확인

---

### TC-02 인증 · 토큰 관리

#### TC-02-1 토큰 상태 조회 (캐시 없음)

토큰 발급 전에 DB에 캐시된 토큰이 없는 상태를 확인합니다.

```powershell
curl.exe -s "http://localhost:8000/api/v1/auth/token?server_mode=real"
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token?server_mode=real" -Method Get
```

**예상 응답 (200 OK)**:

```json
{
  "server_mode": "real",
  "host": "https://api.kiwoom.com",
  "app_key_source": "65120003",
  "has_cached_token": false,
  "cached_token": null
}
```

#### TC-02-2 토큰 발급 (실서버)

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/auth/token -H "Content-Type: application/json" -d '{"server_mode": "real", "reuse_cached": true}'

# 방법 2: PowerShell 네이티브 (권장)
$body = @{ server_mode = "real"; reuse_cached = $true } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답 (200 OK)**:

```json
{
  "server_mode": "real",
  "host": "https://api.kiwoom.com",
  "reused_cached_token": false,
  "app_key_source": "65120003",
  "token": "eyJ...",
  "token_type": "Bearer",
  "expires_dt": "20260429",
  "return_code": 0,
  "return_msg": ""
}
```

**검증 항목**:
- `return_code` 가 `0` 인지 확인
- `token` 이 비어 있지 않은지 확인

#### TC-02-3 토큰 재사용 (캐시 히트)

같은 요청을 한 번 더 보내면 기존 캐시 토큰을 재사용해야 합니다.

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/auth/token `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "real", "reuse_cached": true}'

$body = @{ server_mode = "real"; reuse_cached = $true } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답**: `"reused_cached_token": true`

#### TC-02-4 토큰 상태 조회 (캐시 있음)

```powershell
curl.exe -s "http://localhost:8000/api/v1/auth/token?server_mode=real"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token?server_mode=real" -Method Get
```

**예상 응답**: `"has_cached_token": true`, `"cached_token"` 에 토큰 값

#### TC-02-5 토큰 폐기

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/auth/token/revoke `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "real", "token": null}'

$body = @{ server_mode = "real"; token = $null } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token/revoke" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답 (200 OK)**:

```json
{
  "server_mode": "real",
  "host": "https://api.kiwoom.com",
  "revoked_token": "eyJ...",
  "return_code": 0,
  "return_msg": "..."
}
```

> 이후 TC-03 이하 테스트 전에 TC-02-2 로 토큰을 재발급하세요.

#### TC-02-6 모의투자 토큰 발급

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/auth/token `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "mock", "reuse_cached": true}'

$body = @{ server_mode = "mock"; reuse_cached = $true } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/auth/token" -Method Post -ContentType "application/json" -Body $body
```

**검증 항목**: `"host": "https://mockapi.kiwoom.com"` 인지 확인

---

### TC-03 업종 조회 API

> 사전 조건: 실서버 토큰이 캐시되어 있어야 합니다.

#### TC-03-1 업종현재가 (코스피 종합)

```powershell
curl.exe -s "http://localhost:8000/api/v1/sect/current-price?server_mode=real&mrkt_tp=0&sect_cd=001"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/sect/current-price?server_mode=real&mrkt_tp=0&sect_cd=001" -Method Get
```

**예상 응답 (200 OK)**:

```json
{
  "server_mode": "real",
  "api_id": "ka20001",
  "data": {
    "return_code": 0,
    "inds_cd": "001",
    "inds_nmkr": "종합(KOSPI)",
    "cur_prc": "...",
    ...
  }
}
```

**검증 항목**:
- `data.return_code` 가 `0`
- `data.inds_cd` 가 요청한 업종코드 (`001`) 와 일치

#### TC-03-2 업종현재가 (코스닥 종합)

```powershell
curl.exe -s "http://localhost:8000/api/v1/sect/current-price?server_mode=real&mrkt_tp=1&sect_cd=101"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/sect/current-price?server_mode=real&mrkt_tp=1&sect_cd=101" -Method Get
```

#### TC-03-3 토큰 없을 때 401 에러

캐시 토큰을 폐기한 뒤 실행합니다.

```powershell
curl.exe -s "http://localhost:8000/api/v1/sect/current-price?server_mode=real&mrkt_tp=0&sect_cd=001"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/sect/current-price?server_mode=real&mrkt_tp=0&sect_cd=001" -Method Get
```

**예상 응답 (401 Unauthorized)**:

```json
{
  "error": {
    "code": "TOKEN_NOT_FOUND",
    "message": "No valid access token found. Issue a token first via POST /api/v1/auth/token",
    "detail": null
  }
}
```

---

### TC-04 거래량 조회 API

> 사전 조건: 실서버 토큰이 캐시되어 있어야 합니다.

#### TC-04-1 거래량 급증 (ka10023)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/surge?server_mode=real&mrkt_tp=000&sort_tp=1&tm_tp=2&trde_qty_tp=5&tm=&stk_cnd=0&pric_tp=0&stex_tp=3"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/surge?server_mode=real&mrkt_tp=000&sort_tp=1&tm_tp=2&trde_qty_tp=5&tm=&stk_cnd=0&pric_tp=0&stex_tp=3" -Method Get
```

**검증 항목**: `data.return_code` 가 `0`

#### TC-04-2 당일거래량 상위 (ka10030)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/today-rank?server_mode=real&mrkt_tp=000&sort_tp=1&mang_stk_incls=0&crd_tp=0&trde_qty_tp=0&pric_tp=0&trde_prica_tp=0&mrkt_open_tp=0&stex_tp=3"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/today-rank?server_mode=real&mrkt_tp=000&sort_tp=1&mang_stk_incls=0&crd_tp=0&trde_qty_tp=0&pric_tp=0&trde_prica_tp=0&mrkt_open_tp=0&stex_tp=3" -Method Get
```

#### TC-04-3 전일거래량 상위 (ka10031)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/prev-rank?server_mode=real&mrkt_tp=000&qry_tp=1&rank_strt=0&rank_end=20&stex_tp=3"

$response = Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/prev-rank?server_mode=real&mrkt_tp=000&qry_tp=1&rank_strt=0&rank_end=20&stex_tp=3" -Method Get
$response | ConvertTo-Json -Depth 10
```

#### TC-04-4 거래대금 상위 (ka10032)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/trade-amount-rank?server_mode=real&mrkt_tp=001&mang_stk_incls=1&stex_tp=3"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/trade-amount-rank?server_mode=real&mrkt_tp=001&mang_stk_incls=1&stex_tp=3" -Method Get
```

#### TC-04-5 거래량 갱신 (ka10024)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/update?server_mode=real&mrkt_tp=000&cycle_tp=5&trde_qty_tp=5&stex_tp=3"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/update?server_mode=real&mrkt_tp=000&cycle_tp=5&trde_qty_tp=5&stex_tp=3" -Method Get
```

#### TC-04-6 거래원 순간거래량 (ka10052)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/broker-instant?server_mode=real&mmcm_cd=888&mrkt_tp=0&stk_cd=&qty_tp=0&pric_tp=0&stex_tp=3"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/broker-instant?server_mode=real&mmcm_cd=888&mrkt_tp=0&stk_cd=&qty_tp=0&pric_tp=0&stex_tp=3" -Method Get
```

`mmcm_cd=888` 은 외국계 합계입니다.

#### TC-04-7 당일전일 체결량 (ka10055)

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/today-prev-contracts?server_mode=real&stk_cd=005930&tdy_pred=1"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/today-prev-contracts?server_mode=real&stk_cd=005930&tdy_pred=1" -Method Get
```

`stk_cd=005930` 은 삼성전자입니다.

#### TC-04-8 쿼리 파라미터 누락 → 422 에러

`mmcm_cd` 필수 파라미터를 생략합니다.

```powershell
curl.exe -s "http://localhost:8000/api/v1/volume/broker-instant?server_mode=real"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/volume/broker-instant?server_mode=real" -Method Get
```

**예상 응답 (422 Unprocessable Entity)**:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "detail": [{"loc": ["query", "mmcm_cd"], "msg": "Field required", ...}]
  }
}
```

---

### TC-05 계좌 API

> 사전 조건: 모의투자 토큰이 캐시되어 있어야 합니다 (TC-02-6).

#### TC-05-1 계좌 API 스펙 목록 조회

```powershell
curl.exe -s http://localhost:8000/api/v1/acnt/specs

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/acnt/specs" -Method Get
```

**예상 응답 (200 OK)**:

```json
{
  "total": 33,
  "specs": [
    {
      "api_id": "ka00001",
      "name": "...",
      "overview": "...",
      "fields": [...],
      "request_example": {...}
    }
  ]
}
```

**검증 항목**: `total` 이 `33` 인지 확인

#### TC-05-2 주식잔고 조회 (ka00001) — 모의투자

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/acnt/ka00001 `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "mock", "body": {}}'

$body = @{ server_mode = "mock"; body = @{} } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/acnt/ka00001" -Method Post -ContentType "application/json" -Body $body
```

**검증 항목**: `data.return_code` 가 `0`

#### TC-05-3 미체결 주문 조회 (ka00002)

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/acnt/ka00002 `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "mock", "body": {"stk_cd": "005930", "stex_tp": "3"}}'

$body = @{ server_mode = "mock"; body = @{ stk_cd = "005930"; stex_tp = "3" } } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/acnt/ka00002" -Method Post -ContentType "application/json" -Body $body
```

#### TC-05-4 등록되지 않은 api_id → 400 에러

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/acnt/ka99999 `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "mock", "body": {}}'

$body = @{ server_mode = "mock"; body = @{} } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/acnt/ka99999" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답 (400 Bad Request)**:

```json
{
  "error": {
    "code": "UNKNOWN_API_ID",
    "message": "Unknown acnt api_id: ka99999",
    "detail": {"api_id": "ka99999", "valid_ids": [...]}
  }
}
```

---

### TC-06 주문 API

> **경고**: 실서버(`server_mode=real`) 주문 변경 API 호출 시 실제 매매가 발생합니다.  
> 반드시 모의투자(`server_mode=mock`)로 테스트하세요.

#### TC-06-1 주문 API 스펙 목록 조회

```powershell
curl.exe -s http://localhost:8000/api/v1/ordr/specs

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ordr/specs" -Method Get
```

**예상 응답 (200 OK)**:

```json
{
  "total": 8,
  "specs": [
    {"api_id": "kt10000", "is_mutation": true, ...}
  ]
}
```

**검증 항목**: `total` 이 `8`, 주문 변경 API의 `is_mutation` 이 `true`

#### TC-06-2 confirm 없이 주문 → 422 에러 (안전장치 검증)

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ordr/kt10000 `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "mock", "confirm": false, "body": {}}'

$body = @{ server_mode = "mock"; confirm = $false; body = @{} } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ordr/kt10000" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답 (422 Unprocessable Entity)**:

```json
{
  "error": {
    "code": "ORDER_CONFIRM_REQUIRED",
    "message": "'kt10000' is an order-mutation API. Set confirm=true in the request body to proceed.",
    "detail": {"api_id": "kt10000", "is_mutation": true}
  }
}
```

#### TC-06-3 모의투자 매수주문 (kt10000) — confirm=true

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ordr/kt10000 `
  -H "Content-Type: application/json" `
  -d '{
    "server_mode": "mock",
    "confirm": true,
    "body": {
      "dmst_stk_yn": "Y",
      "acnt_no": "<모의투자 계좌번호>",
      "acnt_pwd": "<모의투자 비밀번호>",
      "stk_cd": "005930",
      "ord_qty": "1",
      "ord_uv": "0",
      "trde_tp": "3",
      "stex_tp": "3"
    }
  }'

$body = @{
  server_mode = "mock"
  confirm = $true
  body = @{
    dmst_stk_yn = "Y"
    acnt_no = "<모의투자 계좌번호>"
    acnt_pwd = "<모의투자 비밀번호>"
    stk_cd = "005930"
    ord_qty = "1"
    ord_uv = "0"
    trde_tp = "3"
    stex_tp = "3"
  }
} | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ordr/kt10000" -Method Post -ContentType "application/json" -Body $body
```

> `trde_tp=3` 은 시장가 주문입니다. `acnt_no`, `acnt_pwd` 는 모의투자 계좌 정보로 교체하세요.

**검증 항목**: `data.return_code` 가 `0`

#### TC-06-4 매도주문 (kt10001) — confirm=true

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ordr/kt10001 `
  -H "Content-Type: application/json" `
  -d '{
    "server_mode": "mock",
    "confirm": true,
    "body": {
      "dmst_stk_yn": "Y",
      "acnt_no": "<모의투자 계좌번호>",
      "acnt_pwd": "<모의투자 비밀번호>",
      "stk_cd": "005930",
      "ord_qty": "1",
      "ord_uv": "0",
      "trde_tp": "3",
      "stex_tp": "3"
    }
  }'

$body = @{
  server_mode = "mock"
  confirm = $true
  body = @{
    dmst_stk_yn = "Y"
    acnt_no = "<모의투자 계좌번호>"
    acnt_pwd = "<모의투자 비밀번호>"
    stk_cd = "005930"
    ord_qty = "1"
    ord_uv = "0"
    trde_tp = "3"
    stex_tp = "3"
  }
} | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ordr/kt10001" -Method Post -ContentType "application/json" -Body $body
```

---

### TC-07 WebSocket 세션 제어

#### TC-07-1 실시간 타입 목록 조회

```powershell
curl.exe -s http://localhost:8000/api/v1/ws/types

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/types" -Method Get
```

**예상 응답 (200 OK)**:

```json
{
  "total": 19,
  "types": [
    {"code": "0B", "name": "주식체결", "needs_item": true},
    {"code": "00", "name": "주문체결 (계좌)", "needs_item": false}
  ]
}
```

**검증 항목**: `total` 이 `19`

#### TC-07-2 세션 상태 조회 (시작 전)

```powershell
curl.exe -s http://localhost:8000/api/v1/ws/status

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/status" -Method Get
```

**예상 응답**:

```json
{
  "running": false,
  "items": [],
  "types": [],
  "started_at": null
}
```

#### TC-07-3 세션 시작 (삼성전자 주식체결 구독)

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ws/start `
  -H "Content-Type: application/json" `
  -d '{
    "server_mode": "real",
    "items": ["005930"],
    "types": ["0B", "0D"],
    "group_no": "1"
  }'

$body = @{ server_mode = "real"; items = @("005930"); types = @("0B", "0D"); group_no = "1" } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/start" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답 (200 OK)**:

```json
{
  "success": true,
  "message": "WebSocket session started",
  "session_status": {
    "running": true,
    "items": ["005930"],
    "types": ["0B", "0D"],
    "started_at": "2026-04-28T10:00:00..."
  }
}
```

#### TC-07-4 세션 상태 조회 (시작 후)

```powershell
curl.exe -s http://localhost:8000/api/v1/ws/status

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/status" -Method Get
```

**검증 항목**: `running` 이 `true`, `items`/`types` 가 요청값과 일치

#### TC-07-5 중복 시작 → 409 에러

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ws/start `
  -H "Content-Type: application/json" `
  -d '{"server_mode": "real", "items": ["000660"], "types": ["0B"], "group_no": "1"}'

$body = @{ server_mode = "real"; items = @("000660"); types = @("0B"); group_no = "1" } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/start" -Method Post -ContentType "application/json" -Body $body
```

**예상 응답 (409 Conflict)**:

```json
{
  "error": {
    "code": "SESSION_ALREADY_RUNNING",
    "message": "WebSocket session is already running."
  }
}
```

#### TC-07-6 실시간 항목 추가 (REG)

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ws/register `
  -H "Content-Type: application/json" `
  -d '{
    "items": ["000660"],
    "types": ["0B"],
    "group_no": "1"
  }'

$body = @{ items = @("000660"); types = @("0B"); group_no = "1" } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/register" -Method Post -ContentType "application/json" -Body $body
```

#### TC-07-7 실시간 항목 해제 (REMOVE)

```powershell
curl.exe -s -X DELETE http://localhost:8000/api/v1/ws/register `
  -H "Content-Type: application/json" `
  -d '{
    "items": ["005930"],
    "types": ["0B"],
    "group_no": "1"
  }'

$body = @{ items = @("005930"); types = @("0B"); group_no = "1" } | ConvertTo-Json -Compress
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/register" -Method Delete -ContentType "application/json" -Body $body
```

#### TC-07-8 세션 중지

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ws/stop

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/stop" -Method Post
```

**예상 응답**: `"success": true`

#### TC-07-9 세션 없이 중지 → 409 에러

```powershell
curl.exe -s -X POST http://localhost:8000/api/v1/ws/stop

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/ws/stop" -Method Post
```

**예상 응답 (409 Conflict)**:

```json
{
  "error": {
    "code": "SESSION_NOT_RUNNING",
    "message": "No WebSocket session is currently running."
  }
}
```

---

### TC-08 공통 에러 응답 검증

#### TC-08-1 잘못된 server_mode → 400 에러

```powershell
curl.exe -s "http://localhost:8000/api/v1/sect/current-price?server_mode=staging&mrkt_tp=0&sect_cd=001"

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/sect/current-price?server_mode=staging&mrkt_tp=0&sect_cd=001" -Method Get
```

**예상 응답 (400 Bad Request)**:

```json
{
  "error": {
    "code": "INVALID_SERVER_MODE",
    "message": "Unsupported server_mode: staging"
  }
}
```

#### TC-08-2 존재하지 않는 경로 → 404 에러

```powershell
curl.exe -s http://localhost:8000/api/v1/not-exist

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/not-exist" -Method Get
```

**예상 응답 (404 Not Found)**

---

### TC-09 Swagger UI 통합 확인

브라우저에서 http://localhost:8000/docs 접속 후 아래를 확인합니다.

| 확인 항목 | 기대값 |
|---|---|
| 표시되는 태그 그룹 수 | health, auth, 업종, 거래량, acnt, ordr, ws — 7개 |
| `POST /api/v1/acnt/{api_id}` 요청 예시 | `body` 필드 포함 |
| `POST /api/v1/ordr/{api_id}` 요청 예시 | `confirm` 필드 포함 |
| `POST /api/v1/ws/start` 요청 예시 | `items`, `types` 배열 포함 |

---

### 테스트 체크리스트

| ID | 엔드포인트 | 시나리오 | 예상 코드 | 완료 |
|---|---|---|---|---|
| TC-01 | GET /health | 정상 응답 | 200 | ☐ |
| TC-02-1 | GET /auth/token | 캐시 없음 | 200 | ☐ |
| TC-02-2 | POST /auth/token | 토큰 발급 | 200 | ☐ |
| TC-02-3 | POST /auth/token | 토큰 재사용 | 200 | ☐ |
| TC-02-4 | GET /auth/token | 캐시 있음 | 200 | ☐ |
| TC-02-5 | POST /auth/token/revoke | 토큰 폐기 | 200 | ☐ |
| TC-02-6 | POST /auth/token | 모의투자 발급 | 200 | ☐ |
| TC-03-1 | GET /sect/current-price | 코스피 종합 | 200 | ☐ |
| TC-03-2 | GET /sect/current-price | 코스닥 종합 | 200 | ☐ |
| TC-03-3 | GET /sect/current-price | 토큰 없음 | 401 | ☐ |
| TC-04-1 | GET /volume/surge | 거래량 급증 | 200 | ☐ |
| TC-04-2 | GET /volume/today-rank | 당일거래량 상위 | 200 | ☐ |
| TC-04-3 | GET /volume/prev-rank | 전일거래량 상위 | 200 | ☐ |
| TC-04-4 | GET /volume/trade-amount-rank | 거래대금 상위 | 200 | ☐ |
| TC-04-5 | GET /volume/update | 거래량 갱신 | 200 | ☐ |
| TC-04-6 | GET /volume/broker-instant | 거래원 순간 | 200 | ☐ |
| TC-04-7 | GET /volume/today-prev-contracts | 삼성전자 | 200 | ☐ |
| TC-04-8 | GET /volume/broker-instant | mmcm_cd 누락 | 422 | ☐ |
| TC-05-1 | GET /acnt/specs | 스펙 목록 | 200 | ☐ |
| TC-05-2 | POST /acnt/ka00001 | 잔고 조회 | 200 | ☐ |
| TC-05-3 | POST /acnt/ka00002 | 미체결 조회 | 200 | ☐ |
| TC-05-4 | POST /acnt/ka99999 | 없는 api_id | 400 | ☐ |
| TC-06-1 | GET /ordr/specs | 스펙 목록 | 200 | ☐ |
| TC-06-2 | POST /ordr/kt10000 | confirm 없음 | 422 | ☐ |
| TC-06-3 | POST /ordr/kt10000 | 모의 매수 | 200 | ☐ |
| TC-06-4 | POST /ordr/kt10001 | 모의 매도 | 200 | ☐ |
| TC-07-1 | GET /ws/types | 타입 목록 | 200 | ☐ |
| TC-07-2 | GET /ws/status | 시작 전 상태 | 200 | ☐ |
| TC-07-3 | POST /ws/start | 세션 시작 | 200 | ☐ |
| TC-07-4 | GET /ws/status | 시작 후 상태 | 200 | ☐ |
| TC-07-5 | POST /ws/start | 중복 시작 | 409 | ☐ |
| TC-07-6 | POST /ws/register | 항목 추가 | 200 | ☐ |
| TC-07-7 | DELETE /ws/register | 항목 해제 | 200 | ☐ |
| TC-07-8 | POST /ws/stop | 세션 중지 | 200 | ☐ |
| TC-07-9 | POST /ws/stop | 세션 없음 | 409 | ☐ |
| TC-08-1 | GET /sect/current-price | 잘못된 server_mode | 400 | ☐ |
| TC-08-2 | GET /api/v1/not-exist | 없는 경로 | 404 | ☐ |
