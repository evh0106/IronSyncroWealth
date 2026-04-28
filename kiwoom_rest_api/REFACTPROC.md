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

```bash
pip install -r requirements-fastapi.txt
```

2. 서버 실행

```bash
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