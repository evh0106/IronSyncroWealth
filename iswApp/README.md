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

## 메뉴 구성 상세

### 메인 그룹

**대시보드** — 앱의 홈 화면입니다. KPI 카드(총 자산·일 수익·승률·체결 건수), 수익 곡선 차트, 섹터 비중, 보유 종목 요약, 최근 매매 신호를 한 화면에 배치합니다.

**실시간 시세** — WebSocket으로 수신한 호가와 틱 데이터를 종목별로 표시합니다. 관심 종목 리스트를 왼쪽에, 선택 종목의 호가창과 차트를 오른쪽에 배치하는 2-패널 구조가 일반적입니다.

---

### 매매 그룹

**주문 / 체결** — 수동 주문 입력 폼(종목·수량·가격·주문 유형)과 미체결·체결 내역 탭으로 구성됩니다. 뱃지 숫자는 현재 미체결 주문 수를 실시간으로 표시합니다.

**보유 종목** — 현재 포지션의 평가금액, 평가손익, 수익률을 테이블로 보여줍니다. 종목별 목표가와 손절가 설정 인라인 편집 기능을 추가하면 유용합니다.

**수익 분석** — 일별·월별 수익 바 차트, 누적 수익 곡선, 승률·최대낙폭(MDD)·샤프지수 등 성과 지표를 시각화합니다. React Query로 기간 파라미터를 바꿔가며 데이터를 다시 요청하는 구조로 설계합니다.

---

### 자동화 그룹

**전략 관리** — 등록된 전략 목록과 각 전략의 활성화 토글, 조건식 파라미터 편집 UI입니다. 조건식 빌더는 "이동평균 5일 > 이동평균 20일"처럼 블록 방식으로 만들면 비개발자도 사용할 수 있습니다. 뱃지는 현재 활성 전략 수를 나타냅니다.

**백테스트** — 전략과 기간을 선택하면 Celery 태스크로 백그라운드 실행됩니다. 실행 상태(대기·진행·완료)를 폴링으로 갱신하고, 결과로 수익 곡선·거래 횟수·최대낙폭을 차트로 표시합니다.

**스케줄러** — Celery Beat의 주기 태스크 목록을 테이블로 보여줍니다. 각 태스크의 ON/OFF 토글, 마지막 실행 시간, 성공/실패 상태를 확인하고 즉시 실행(`apply_async`) 버튼도 제공합니다.

---

### 계정 그룹

**API 설정** — 키움·한투 API 키와 계좌 번호 입력, 액세스 토큰 발급·만료 시간 표시, 연결 테스트 버튼을 포함합니다. 민감 정보라 입력 필드는 마스킹 처리합니다.

**알림 설정** — 체결·손절·시스템 오류 알림의 수신 채널(이메일, Slack, 카카오톡)과 발생 조건(수익률 임계값 등)을 설정합니다.

**시스템 로그** — FastAPI 요청 로그, Celery 태스크 실행 이력, 외부 API 에러를 레벨별(INFO·WARN·ERROR)로 필터링해서 볼 수 있는 테이블입니다. 실시간 tail 기능이 있으면 운영 중 모니터링에 유용합니다.
