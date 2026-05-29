# ISW Python 개발 환경 구성

## 1. 요구 사항
- OS: Windows 10/11
- Python: 3.11 이상 권장
- 패키지 관리자: pip

## 2. 프로젝트 이동

PowerShell에서 아래 명령을 실행한다.

```powershell
cd d:\app\IronSyncroWealth\isw
```

## 3. 가상환경 생성/활성화

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

활성화 확인:

```powershell
python --version
where python
```

## 4. pip 업그레이드

```powershell
python -m pip install --upgrade pip
```

## 5. 필수 패키지 설치

`requirements.txt`가 있는 경우:

```powershell
pip install -r requirements.txt
```

`requirements.txt`가 아직 없다면 최소 개발 패키지:

```powershell
pip install fastapi uvicorn[standard] httpx pydantic python-dotenv
```

## 6. 개발 서버 실행(예시)

FastAPI 앱 엔트리포인트가 `src/app/main.py`이고 객체명이 `app`인 경우:

```powershell
$env:PYTHONPATH = "src"
python -m uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload
```

## 7. 종료 및 비활성화

서버 종료: `Ctrl + C`

가상환경 비활성화:

```powershell
deactivate
```
