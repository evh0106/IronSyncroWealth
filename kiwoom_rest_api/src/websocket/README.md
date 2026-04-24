# WebSocket 실시간 데이터 DB 저장 기능

## 개요

키움증권 WebSocket API로부터 수신한 실시간 데이터를 자동으로 로그 파일과 MySQL 데이터베이스에 저장합니다.

## 기능

### 1. 로그 파일 저장
- 실시간 웹소켓 메시지를 JSON 형식으로 로그 파일에 저장
- 파일명: `log/YYYYMMDD_websocket.log`
- 기존 기능: `logger.log_websocket_message(response, direction='recv')`

### 2. DB 저장
- WebSocket 응답 데이터를 API 타입별 테이블에 INSERT
- 22개 테이블에 실시간 데이터 저장 (2026-04-24 생성)
- 자동 파싱: FID 값을 `rsp_f{FID}` 컬럼으로 매핑

## 아키텍처

```
WebSocketClient (client.py)
    ↓ receive_messages()
    ├→ 로그 저장: log_websocket_message()
    └→ DB 저장: ws_db.save_websocket_realtime() [신규]
          ↓
    ├→ API 타입 추출 (trnm 필드)
    ├→ 테이블명 조회 (_TABLE_MAPPING)
    ├→ 응답 파싱 (_parse_response_data)
    ├→ INSERT 생성 (_build_insert_sql)
    └→ DB 실행 (db.get_connection())
```

## 설정

### 환경 준비

```bash
# MySQL 시작
cd kiwoom_rest_api/db
docker-compose up -d

# 스키마 적용
docker exec -i websocket-db mysql -uroot -pmy-secret-pw < dbschema_websocket.sql
```

### DB 테이블 (22개)

| API 타입 | 테이블명 | 설명 |
|---------|---------|------|
| 00 | ws_00_ord_ccls | 주문체결 |
| 04 | ws_04_balance | 잔고 |
| 0A | ws_0a_stk_kse | 주식기세 |
| 0B | ws_0b_stk_ccls | 주식체결 |
| 0C | ws_0c_stk_prio_hga | 주식우선호가 |
| 0D | ws_0d_stk_hga_qty | 주식호가잔량 |
| 0E | ws_0e_stk_ah_hga | 주식시간외호가 |
| 0F | ws_0f_stk_dly_trd | 주식당일거래원 |
| 0G | ws_0g_etf_nav | ETF NAV |
| 0H | ws_0h_stk_exp_ccls | 주식예상체결 |
| 0I | ws_0i_intl_gold_prc | 국제금환산가격 |
| 0J | ws_0j_sect_idx | 업종지수 |
| 0U | ws_0u_sect_flct | 업종등락 |
| 0g | ws_0g_stk_nfo | 주식종목정보 |
| 0m | ws_0m_elw_thr | ELW 이론가 |
| 0s | ws_0s_mkt_tm | 장시작시간 |
| 0u | ws_0u_elw_idx | ELW 지표 |
| 0w | ws_0w_stk_prg_trd | 종목프로그램매매 |
| ka10171 | ws_ka10171_cndsr_lst | 조건검색 목록 |
| ka10172 | ws_ka10172_cndsr_req | 조건검색 요청 일반 |
| ka10173 | ws_ka10173_cndsr_rt | 조건검색 요청 실시간 |
| ka10174 | ws_ka10174_cndsr_clr | 조건검색 해제 |

## 사용법

### 1. WebSocketClient 사용

```python
from websocket.client import WebSocketClient
from oauth2 import get_access_token, load_api_keys

# 토큰 발급
app_key, app_secret = load_api_keys()
token = get_access_token(app_key, app_secret)

# 클라이언트 생성 및 실행
client = WebSocketClient(uri='wss://api.kiwoom.com:10000/api/dostk/websocket',
                         access_token=token)

# 실시간 항목 등록
from websocket.realtime import register_stock_momentum
register_stock_momentum(client, '005930')  # 삼성전자

# 실행
import asyncio
asyncio.run(client.run())
```

### 2. 데이터 확인

```sql
-- 0A (주식기세) 테이블에서 조회
SELECT * FROM ws_0a_stk_kse 
WHERE req_dt >= DATE_FORMAT(NOW(), '%Y%m%d000000')
ORDER BY fetched_at DESC LIMIT 10;

-- 모든 실시간 데이터 조회 (타입별)
SELECT req_type, COUNT(*) as count, MAX(fetched_at) as latest
FROM (
  SELECT '0A' as req_type, fetched_at FROM ws_0a_stk_kse UNION ALL
  SELECT '0B' as req_type, fetched_at FROM ws_0b_stk_ccls UNION ALL
  SELECT '04' as req_type, fetched_at FROM ws_04_balance
  -- ... 추가 UNION ALL 쿼리
) data
GROUP BY req_type;
```

## 데이터 구조

### 응답 메시지 (WebSocket)

```json
{
  "trnm": "0A",
  "return_code": "0",
  "return_msg": "success",
  "data": [
    {
      "type": "0A",
      "name": "주식기세",
      "item": "005930",
      "values": [
        {"name": "10", "value": "70000"},
        {"name": "11", "value": "500"},
        {"name": "12", "value": "0.71"}
      ]
    }
  ]
}
```

### DB 테이블 구조

```sql
CREATE TABLE ws_0a_stk_kse (
  id INT AUTO_INCREMENT PRIMARY KEY,
  req_dt VARCHAR(14),           -- 요청 날짜시간 (YYYYMMDDHHmmss)
  req_type VARCHAR(10),         -- API 타입 (0A)
  req_item VARCHAR(20),         -- 등록 요소 (종목코드 등)
  rsp_return_code VARCHAR(10),  -- 결과 코드
  rsp_return_msg VARCHAR(100),  -- 결과 메시지
  rsp_f10 VARCHAR(50),          -- FID 10 (현재가)
  rsp_f11 VARCHAR(50),          -- FID 11 (전일대비)
  rsp_f12 VARCHAR(50),          -- FID 12 (등락율)
  -- ... 추가 FID 컬럼들
  fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_req_dt (req_dt),
  INDEX idx_req_item (req_item),
  INDEX idx_fetched_at (fetched_at)
);
```

## 에러 처리

### DB 연결 오류
- 재시도 로직 없음 (현재 구현)
- 콘솔 로그에 오류 메시지 출력
- 애플리케이션은 계속 실행

### 개별 행 INSERT 오류
- 오류 행을 건너뛰고 계속 진행
- 다른 행들은 정상 저장

### 파싱 오류
- 응답 구조가 예상과 다를 경우
- 콘솔 로그에 오류 메시지 출력
- 행 저장 건너뜀

## 테스트

### 파싱 로직 테스트 (DB 연결 없음)

```bash
cd src
python websocket/_sample/parsing_test.py
```

결과:
```
✓ 파싱 성공: 1 행
  행 1:
    ├─ req_type: 0A
    ├─ req_item: 005930
    ├─ rsp_return_code: 0
    ├─ rsp_return_msg: success
    └─ FID 데이터: 7 개
       10: 70000
       11: 500
       ...
```

### 전체 기능 테스트 (DB 연결 필요)

```bash
cd src
python websocket/_sample/db_save_test.py
```

## 파일 구조

```
kiwoom_rest_api/
├── src/
│   ├── websocket/
│   │   ├── db.py              # [신규] DB 저장 모듈
│   │   ├── client.py          # [수정] DB 저장 로직 추가
│   │   ├── __init__.py
│   │   ├── realtime.py
│   │   └── _sample/
│   │       ├── parsing_test.py        # [신규] 파싱 테스트
│   │       ├── db_save_test.py        # [신규] DB 저장 테스트
│   │       └── websocket_sample.py
│   ├── db.py
│   └── logger.py
├── db/
│   ├── dbschema_websocket.sql # [기존] 22개 테이블 정의
│   └── docker-compose.yml
└── README.md
```

## 주요 모듈

### websocket/db.py

**함수:**
- `save_websocket_data(api_type, response)` - API 타입별 저장
- `save_websocket_realtime(response)` - trnm 기반 자동 저장
- `_parse_response_data(api_type, response)` - 응답 파싱
- `_build_insert_sql(table_name, columns)` - INSERT SQL 생성

**상수:**
- `_TABLE_MAPPING` - trnm → 테이블명 매핑

### websocket/client.py

**수정 사항:**
```python
# receive_messages() 메서드에서:
try:
    saved_count = ws_db.save_websocket_realtime(response)
    if saved_count > 0:
        print(f'[DB 저장] {saved_count} 행 저장됨')
except Exception as exc:
    print(f'[DB 저장 오류] {exc}')
```

## 성능 고려사항

- 각 응답마다 DB INSERT 실행 → 분당 최대 수백 행 생성
- 장기 실행 시 테이블 크기 주의 (자동 정리 로직 없음)
- 로그 파일도 날짜별로 누적됨

## 향후 개선

1. 배치 INSERT (여러 행을 한 번에 삽입)
2. 오류 재시도 로직
3. 테이블 자동 정리 (오래된 데이터 삭제)
4. 캐싱 (동일한 응답 데이터 중복 제거)
5. 비동기 처리 (DB 저장 논블로킹)
