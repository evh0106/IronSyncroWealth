# ISW Backend Skeleton

iswWeb 프론트엔드와 인터페이스하기 위한 최소 FastAPI 스켈레톤입니다.

## 제공 API

- GET `/health`
- GET `/api/v1/account/{accountNo}/summary`
- GET `/api/v1/market/{symbol}`
- POST `/api/v1/order`
- WS `ws://localhost:8010/ws/{broker}/{symbol}`

## 실행

PowerShell 기준:

1. 프로젝트 루트로 이동
   - `cd d:\app\IronSyncroWealth\isw`
2. 가상환경 생성/활성화(최초 1회)
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate.ps1`
3. 의존성 설치
   - `pip install fastapi "uvicorn[standard]" pydantic`
4. 서버 실행
   - `uvicorn src.main:app --reload --host 0.0.0.0 --port 8010`

기본적으로 mock 데이터로 응답합니다.
