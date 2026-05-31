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

## 6. scripts 실행 파일 사용법 및 기능

실행 전 공통 준비:

```powershell
cd d:\app\IronSyncroWealth\isw
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 6.1 run_fastapi.bat

- 파일 위치: `isw\scripts\run_fastapi.bat`
- 기능: FastAPI 서버를 개발 모드(reload)로 실행한다.
- 내부 동작:
	- `.venv\Scripts\python.exe` 존재 여부 확인
	- `PYTHONPATH`를 `isw\src`로 설정
	- `uvicorn src.main:app --host 0.0.0.0 --port 8010 --reload` 실행

실행 방법:

```powershell
cd d:\app\IronSyncroWealth\isw
.\scripts\run_fastapi.bat
```

정상 실행 후 확인 URL:

- Health: http://localhost:8010/health
- OpenAPI docs: http://localhost:8010/docs

### 6.2 run_main.bat

- 파일 위치: `isw\scripts\run_main.bat`
- 기능: 호환용 엔트리 스크립트. 내부적으로 `run_fastapi.bat`를 호출해 동일하게 서버를 실행한다.
- 사용 상황: 기존에 `run_main.bat`를 사용하던 실행 습관/문서를 유지하고 싶을 때.

실행 방법:

```powershell
cd d:\app\IronSyncroWealth\isw
.\scripts\run_main.bat
```

### 6.3 run_rest_api_sample.bat

- 파일 위치: `isw\scripts\run_rest_api_sample.bat`
- 기능: REST API 샘플 스크립트 실행용 배치 파일.
- 현재 상태: `isw\src\_sample\check_auth.py`가 아직 없기 때문에 실행 시 안내 메시지와 함께 종료된다.

실행 방법:

```powershell
cd d:\app\IronSyncroWealth\isw
.\scripts\run_rest_api_sample.bat
```

## 7. 빠른 실행 요약

- 서버 실행(권장): `scripts\run_fastapi.bat`
- 서버 실행(호환): `scripts\run_main.bat`
- 샘플 실행: `scripts\run_rest_api_sample.bat` (샘플 파일 추가 후 사용)

