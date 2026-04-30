# IronSyncroWealth App
이 프로젝트는 시장의 정보를 분석하고 거래를 할 수 있는 웹 프론트엔드 프로그램 개발을 한다.


## React Frontend 설계안 (Zustand + React Query)
현재 구조를 기준으로 프론트엔드는 "서버 상태"와 "클라이언트 상태"를 분리해 설계한다.

- 서버 상태: React Query(TanStack Query)로 조회/캐시/동기화/재시도/백그라운드 갱신 처리
- 클라이언트 상태: Zustand로 UI 상태, 임시 입력 상태, 사용자 환경설정 관리
- 실시간: WebSocket 이벤트 수신 후 React Query 캐시 갱신(invalidate/setQueryData)

### 기술 스택(권장)
- React 19 + TypeScript
- Vite 6
- React Router 7
- Zustand + zustand/middleware
- @tanstack/react-query + @tanstack/react-query-devtools
- axios(or fetch wrapper) + zod(응답 검증)
- echarts or lightweight-charts (차트)
- Tailwind CSS + shadcn/ui(또는 Radix 기반 컴포넌트)

### 폴더 구조(Feature-Sliced)
```
iswApp/src/
├── app/
│   ├── providers/
│   ├── routes/
│   └── store/
├── shared/
│   ├── api/
│   ├── config/
│   ├── lib/
│   ├── ui/
│   └── types/
├── entities/
│   ├── account/  (model/, api/)
│   ├── order/    (model/, api/)
│   ├── market/   (model/, api/)
│   └── strategy/ (model/)
├── features/
│   ├── auth/             (model/, ui/)
│   ├── order-submit/     (model/, ui/)
│   ├── broker-switch/    (model/, ui/)
│   └── realtime-subscribe/ (model/)
├── widgets/
│   ├── dashboard/
│   ├── market-board/
│   ├── account-summary/
│   └── order-book/
└── pages/
    ├── home/
    ├── trade/
    └── settings/
```

### 디렉토리 역할
- app/: 앱 부트스트랩, 전역 Provider, 라우팅, 전역 상태 스토어를 관리한다.
- shared/: 여러 도메인에서 공통으로 재사용하는 API 클라이언트, 설정, 유틸, 공용 UI를 둔다.
- entities/: 계좌/주문/시세 같은 핵심 도메인 단위의 타입과 조회 로직을 정의한다.
- features/: 사용자 액션 중심 기능(로그인, 주문 제출, 브로커 전환, 실시간 구독)을 캡슐화한다.
- widgets/: 여러 feature/entities를 조합한 화면 블록(대시보드, 보드, 요약 패널)을 구성한다.
- pages/: 라우트 진입점 화면을 담당하며, 위젯을 조합해 최종 페이지를 만든다.

- app/providers/: QueryProvider, RouterProvider 등 앱 전역 Provider를 등록한다.
- app/routes/: 페이지 라우트 매핑과 레이아웃 경계를 정의한다.
- app/store/: UI/인증 같은 전역 클라이언트 상태(Zustand)를 관리한다.

- shared/api/: axios 인스턴스, 인터셉터, 공통 요청/응답 처리를 담당한다.
- shared/config/: 환경변수와 런타임 설정을 중앙 관리한다.
- shared/lib/: queryClient, query key factory 같은 공통 라이브러리를 둔다.
- shared/ui/: 공통 컴포넌트와 스타일 자산을 제공한다.
- shared/types/: 공용 타입(여러 계층에서 재사용)을 보관한다.

### 상태 관리 원칙
1. React Query에는 "서버에서 온 데이터"만 저장한다.
2. Zustand에는 "로컬 UI/흐름 상태"만 저장한다.
3. 동일 데이터를 두 저장소에 중복 저장하지 않는다.
4. 폼 입력은 로컬 상태(react-hook-form 또는 Zustand slice), 제출 성공 시 query invalidate.

### Zustand Store 설계
- ui-store: 사이드바 열림/닫힘, 현재 브로커 탭, 테마, 알림 패널
- auth-store: access token, refresh status, 로그인 사용자 메타
- trade-draft-store(선택): 주문 입력 초안(종목코드, 수량, 가격, 주문유형)

예시(개념):
```ts
type UiState = {
       broker: "kiwoom" | "kis";
       theme: "light" | "dark";
       setBroker: (broker: UiState["broker"]) => void;
       setTheme: (theme: UiState["theme"]) => void;
};
```

### React Query 설계
- Query Key Factory 사용
       - ["account", broker, accountNo]
       - ["market", broker, symbol]
       - ["orders", broker, accountNo, filters]
- staleTime/cacheTime를 도메인별로 분리
       - 시세/호가: 짧게(예: 1~5초)
       - 계좌/설정: 길게(예: 30초~5분)
- Mutation 성공 시 관련 키만 정밀 invalidate
       - 주문 생성 성공 -> orders/account/balance 관련 키 invalidate

### API 통신 계층
- shared/api/client.ts에서 공통 axios 인스턴스 구성
- 브로커별 baseURL 매핑
       - kiwoom: /api/kiwoom
       - kis: /api/kis
- 인터셉터
       - 요청: 인증 헤더 자동 주입
       - 응답: 토큰 만료 시 refresh 시도 후 재요청
- zod로 핵심 응답 스키마 검증(실거래/자동매매 안정성 향상)

### 실시간(WebSocket) 연동
1. realtime-subscribe feature에서 소켓 연결/구독 관리
2. 이벤트 수신 시 우선 setQueryData로 즉시 반영
3. 불확실한 이벤트(부분 데이터)는 invalidateQueries로 재동기화
4. 재연결(backoff), heartbeat, 구독 복구 로직 포함

### 라우팅/권한
- 공개 라우트: 로그인/환경설정 일부
- 보호 라우트: 대시보드, 주문, 계좌
- 라우트 로더에서 선조회가 필요하면 queryClient.ensureQueryData 활용

### 화면 구성(권장)
- /home: 시장 요약, 관심종목, 전략 상태
- /trade: 실시간 호가, 주문 패널, 체결 내역
- /portfolio: 계좌 평가, 보유 종목, 수익률
- /settings: 브로커 키 설정, 리스크 룰, 전략 파라미터

### 코드 규칙
- entities: 순수 도메인 타입/조회 로직
- features: 사용자 액션 단위(주문 제출, 브로커 변경)
- widgets: 화면 조합 단위(보드/패널)
- pages: 라우트 엔트리만 유지(비즈니스 로직 최소화)

### 성능/운영 체크리스트
- React Query Devtools는 개발 모드에서만 활성화
- 에러 경계 + Suspense 경계 분리
- 차트/대형 리스트는 가상화 및 메모이제이션 적용
- API 장애 시 broker fallback 혹은 degrade 모드 제공
- 핵심 액션(주문, 취소)은 idempotency key 적용 고려

### 초기 구현 순서(추천)
1. app/providers + queryClient + 라우터 뼈대 구성
2. auth/ui-store + api client + 토큰 갱신 완성
3. account/market 조회 쿼리 연결
4. order mutation + 체결 반영 + invalidate 체계 구현
5. websocket 실시간 반영 및 재연결 안정화
6. 전략 설정/백테스트 결과 화면 확장

### 백엔드(현재 리포지토리)와의 매핑
- kiwoom_rest_api FastAPI 엔드포인트를 BFF처럼 사용
- 이후 kis_rest_api가 추가되면 broker adapter만 확장
- 프론트에서는 broker 파라미터만 변경하고 동일한 화면/유즈케이스 재사용

## 빠른 시작
1. iswApp 폴더로 이동
2. 패키지 설치: npm install
3. 환경변수 파일 생성: .env.example 내용을 참고해 .env 작성
4. 개발 서버 실행: npm run dev
5. 배포 빌드: npm run build

## 이번에 생성된 초기 코드 범위
- Vite + React + TypeScript 기본 프로젝트 파일
- React Query Provider/QueryClient 설정
- Zustand store(auth/ui) 설정
- 브로커 전환 UI와 주문 제출 feature 샘플
- 계좌/시세 조회 query, 주문 mutation 샘플
- WebSocket 수신 후 React Query 캐시 업데이트 샘플
- Home/Trade/Settings 라우트 및 위젯 기반 화면 뼈대