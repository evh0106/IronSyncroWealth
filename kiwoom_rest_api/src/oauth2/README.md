# OAuth2 API 응답 DB 저장 기능

## 개요

키움증권 OAuth2 API의 응답 결과(토큰 발급/폐기)를 자동으로 MySQL 데이터베이스에 저장합니다.

## 기능

### 1. 토큰 발급 응답 저장 (au10001)
- 액세스 토큰 발급 요청의 응답을 `au10001` 테이블에 저장
- 저장 내용: grant_type, 앱키, 만료일, 토큰타입, 토큰, 결과코드, 결과메시지

### 2. 토큰 폐기 응답 저장 (au10002)
- 액세스 토큰 폐기 요청의 응답을 `au10002` 테이블에 저장
- 저장 내용: 앱키, 토큰, 결과코드, 결과메시지

## 아키텍처

```
┌──────────────────────────────────────────────────────────┐
│         OAuth2 응답 처리 파이프라인                      │
└──────────────────────────────────────────────────────────┘

1. get_access_token() 또는 revoke_access_token() 호출
   ↓
2. OAuth2 API 요청 실행 (POST)
   ↓
3. 응답 수신 & 파싱 (JSON)
   ↓
4. DB 저장 (신규)
   ├─ save_au10001_response() → au10001 테이블 INSERT
   └─ save_au10002_response() → au10002 테이블 INSERT
   ↓
5. 콘솔 출력 & 반환
```

## DB 테이블

### au10001 – 액세스 토큰 발급

| 컬럼명 | 타입 | 설명 |
|-------|------|------|
| id | BIGINT | PK |
| grant_type | VARCHAR(50) | 요청 grant_type (client_credentials) |
| req_appkey | VARCHAR(50) | 요청 시 사용된 앱키 |
| expires_dt | VARCHAR(50) | 토큰 만료일 |
| token_type | VARCHAR(50) | 토큰 타입 (Bearer 등) |
| token | VARCHAR(1000) | 발급된 액세스 토큰 |
| return_code | VARCHAR(10) | 결과 코드 (0=성공) |
| return_msg | VARCHAR(200) | 결과 메시지 |
| fetched_at | DATETIME | 저장 시간 |

### au10002 – 액세스 토큰 폐기

| 컬럼명 | 타입 | 설명 |
|-------|------|------|
| id | BIGINT | PK |
| req_appkey | VARCHAR(50) | 요청 시 사용된 앱키 |
| req_token | VARCHAR(1000) | 요청 시 사용된 토큰 |
| return_code | VARCHAR(10) | 결과 코드 (0=성공) |
| return_msg | VARCHAR(200) | 결과 메시지 |
| fetched_at | DATETIME | 저장 시간 |

## 사용 방법

### 환경 준비

```bash
# MySQL 시작
cd db && docker-compose up -d

# 스키마 생성
docker exec -i kiwoom-db mysql -uroot -pmy-secret-pw < dbschema_oauth.sql
```

### 코드 사용

```python
from oauth2 import get_access_token, revoke_access_token, load_api_keys

# 1. 앱키/시크릿키 로드
app_key, app_secret = load_api_keys()

# 2. 토큰 발급 (자동으로 au10001 테이블에 저장)
token = get_access_token(app_key, app_secret)
# [DB 저장] au10001: 1행 저장됨

# 3. 토큰 폐기 (자동으로 au10002 테이블에 저장)
revoke_access_token(app_key, app_secret, token)
# [DB 저장] au10002: 1행 저장됨
```

### DB 조회

```sql
-- au10001: 발급된 토큰 이력 조회
SELECT id, req_appkey, expires_dt, return_code, return_msg, fetched_at
FROM au10001
WHERE fetched_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
ORDER BY fetched_at DESC
LIMIT 20;

-- au10002: 폐기된 토큰 이력 조회
SELECT id, req_appkey, return_code, fetched_at
FROM au10002
WHERE fetched_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
ORDER BY fetched_at DESC
LIMIT 20;

-- 성공/실패 통계
SELECT 
    return_code,
    COUNT(*) as count
FROM au10001
WHERE fetched_at >= DATE(NOW())
GROUP BY return_code;
```

## 파일 구조

```
kiwoom_rest_api/
├── db/
│   └── dbschema_oauth.sql        # [신규] OAuth2 테이블 스키마
│
├── src/
│   └── oauth2/
│       ├── oauth.py              # [신규] DB 저장 모듈
│       ├── kiwoom_oauth2.py      # [수정] DB 저장 통합
│       ├── specs_response.py     # API 응답 스펙
│       ├── specs_request.py      # API 요청 스펙
│       └── __init__.py
│
└── README.md
```

## 에러 처리

- **DB 연결 실패**: 콘솔에 오류 메시지 출력, 토큰은 정상 반환
- **INSERT 실패**: 콘솔에 오류 메시지 출력, 토큰은 정상 반환
- **토큰 발급 실패**: 예외 발생, 함수 호출자에서 처리

## 이점

✅ **감시 및 감사**
- 토큰 발급/폐기 이력 추적
- 실패 원인 분석 가능

✅ **보안 모니터링**
- 발급된 토큰 만료일 확인
- 비정상 요청 탐지

✅ **운영 분석**
- 토큰 발급/폐기 통계
- 장애 발생 빈도 분석

## 주요 모듈

### oauth.py

**함수:**
- `save_au10001_response(app_key, grant_type, response)` – 토큰 발급 응답 저장
- `save_au10002_response(app_key, token, response)` – 토큰 폐기 응답 저장

**반환값:**
- `True`: 저장 성공
- `False`: 저장 실패

### kiwoom_oauth2.py (수정)

**변경사항:**
```python
# get_access_token() 함수 수정
# → 토큰 발급 후 자동으로 au10001에 저장

# revoke_access_token() 함수 수정  
# → 토큰 폐기 후 자동으로 au10002에 저장
```

## 성능 특성

- **저장 속도**: 1~5ms/요청 (네트워크 포함)
- **테이블 크기**: 하루 약 10~100행 (앱별 발급/폐기 빈도에 따라)
- **쿼리 성능**: `idx_req_dt`, `idx_return_code` 인덱스로 빠른 조회

## 향후 개선

1. 토큰 갱신(refresh) 응답 저장
2. 토큰 검증 결과 로깅
3. 자동 정리 정책 (오래된 데이터 삭제)
4. 알림 (토큰 만료 임박 시)

## 테스트

```bash
cd src

# 주요 테스트: main.py의 토큰 발급/폐기 부분 실행 시 자동 저장
python main.py
# → 선택지에서 메뉴 선택 후 자동으로 DB에 저장됨
```

## 참고

- **토큰 타입**: 보통 `Bearer` (OAuth2 표준)
- **만료일 형식**: `YYYYMMDDHHMMSS` (예: 20260504143022)
- **결과 코드**: `0` = 성공, 그 외 = 실패
