# koreainvestment REST API
대한민국 증권사인 한국투자증권 REST API를 시장 가격 데이터 수집, 분석, 자동, 매매 전략 프로그램을 개발

## API 문서
https://apiportal.koreainvestment.com/apiservice-summary

## 예제코드
https://github.com/koreainvestment/open-trading-api.git

## 개발 환경 구성 (open-trading-api 참고)

이 디렉토리는 `open-trading-api`의 인증 흐름(`kis_devlp.yaml` + `kis_auth`)을 참고해,
로컬에서 빠르게 시작 가능한 최소 실행 환경으로 구성되어 있습니다.

### 1) Python 가상환경 생성

Windows PowerShell 기준:

```powershell
cd d:\app\IronSyncroWealth\koreainvestment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2) 설정 파일 준비

```powershell
Copy-Item .\kis_devlp.yaml.example .\kis_devlp.yaml
```

`kis_devlp.yaml`에서 계좌 ID(`my_prod`) 및 환경(`real`/`demo`) 값을 필요에 맞게 수정하세요.

앱키/시크릿키는 아래 경로를 기본으로 사용합니다.

- `conf/44471935_appkey.txt`
- `conf/44471935_secretkey.txt`

### 3) 인증 테스트 실행

```powershell
python .\src\examples\check_auth.py
```

정상 동작 시 액세스 토큰 발급 성공 여부와 웹소켓 접속키(approval key) 응답을 확인할 수 있습니다.

## 디렉토리 설명

- `kis_devlp.yaml.example`: KIS 실행 환경 템플릿
- `src/kis_config.py`: YAML/키 파일 로더
- `src/kis_auth.py`: OAuth 토큰, WebSocket approval key 발급 유틸
- `src/examples/check_auth.py`: 인증 동작 점검 예제