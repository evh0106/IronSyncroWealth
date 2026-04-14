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
pip install requests asyncio websockets 
```