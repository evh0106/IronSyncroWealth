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
- [ ] 3단계: 조회성 REST API(업종/거래량)부터 엔드포인트화
- [ ] 4단계: 계좌/주문 API 이관
- [ ] 5단계: WebSocket 제어 API(시작/중지/상태) 추가
- [ ] 6단계: 필요 시 비동기 I/O와 작업 큐 도입

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

**예상 공수 (대략)**
1. 최소 MVP(조회 API + 토큰 + 기본 로깅): 3~5일
2. 계좌/주문 + DB 저장 + 운영형 예외 처리: 1~2주
3. WebSocket 제어/모니터링까지 포함: 2~3주