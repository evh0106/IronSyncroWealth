import { createBrowserRouter, NavLink, Outlet } from "react-router-dom";
import { HomePage } from "@/pages/home/ui/page";
import { RealtimePage } from "@/pages/realtime/ui/page";
import { OrdersPage } from "@/pages/orders/ui/page";
import { PortfolioPage } from "@/pages/portfolio/ui/page";
import { AnalysisPage } from "@/pages/analysis/ui/page";
import { StrategiesPage } from "@/pages/strategies/ui/page";
import { BacktestPage } from "@/pages/backtest/ui/page";
import { SchedulerPage } from "@/pages/scheduler/ui/page";
import { SettingsPage } from "@/pages/settings/ui/page";
import { NotificationsPage } from "@/pages/notifications/ui/page";
import { LogsPage } from "@/pages/logs/ui/page";
import { StockMasterPage } from "@/pages/stock-master/ui/page";
import { BrokerSwitch } from "@/features/broker-switch/ui/broker-switch";
import { useUiStore } from "@/app/store/ui-store";

function AppShell() {
  const sidebarOpen = useUiStore((state) => state.sidebarOpen);
  const toggleSidebar = useUiStore((state) => state.toggleSidebar);

  return (
    <div className={`app-shell ${sidebarOpen ? "" : "sidebar-collapsed"}`}>
      <aside className={`side-menu ${sidebarOpen ? "open" : "closed"}`}>
        <div className="side-brand">IronSyncroWealth</div>
        <nav className="side-nav">
          <div className="nav-group">
            <span className="nav-group-label">메인</span>
            <NavLink to="/" end>대시보드</NavLink>
            <NavLink to="/realtime">실시간 시세</NavLink>
          </div>
          <div className="nav-group">
            <span className="nav-group-label">종목 마스터 조회</span>
            <NavLink to="/stock-master/kospi">KOSPI</NavLink>
            <NavLink to="/stock-master/kosdaq">KOSDAQ</NavLink>
            <NavLink to="/stock-master/konex">KONEX</NavLink>
            <NavLink to="/stock-master/domestic-elw">국내 ELW</NavLink>
            <NavLink to="/stock-master/domestic-index-future">지수선물옵션</NavLink>
            <NavLink to="/stock-master/domestic-stock-future">주식선물옵션</NavLink>
            <NavLink to="/stock-master/domestic-cme-future">CME 연계 야간선물</NavLink>
            <NavLink to="/stock-master/domestic-commodity-future">상품선물옵션</NavLink>
            <NavLink to="/stock-master/domestic-eurex-option">EUREX 연계 야간옵션</NavLink>
            <NavLink to="/stock-master/domestic-bond">장내채권</NavLink>
            <NavLink to="/stock-master/overseas-stock">해외주식</NavLink>
            <NavLink to="/stock-master/overseas-index">해외주식지수</NavLink>
            <NavLink to="/stock-master/overseas-future">해외선물옵션</NavLink>
          </div>
          <div className="nav-group">
            <span className="nav-group-label">매매</span>
            <NavLink to="/orders">주문 / 체결</NavLink>
            <NavLink to="/portfolio">보유 종목</NavLink>
            <NavLink to="/analysis">수익 분석</NavLink>
          </div>
          <div className="nav-group">
            <span className="nav-group-label">자동화</span>
            <NavLink to="/strategies">전략 관리</NavLink>
            <NavLink to="/backtest">백테스트</NavLink>
            <NavLink to="/scheduler">스케줄러</NavLink>
          </div>
          <div className="nav-group">
            <span className="nav-group-label">계정</span>
            <NavLink to="/settings">API 설정</NavLink>
            <NavLink to="/notifications">알림 설정</NavLink>
            <NavLink to="/logs">시스템 로그</NavLink>
          </div>
        </nav>
      </aside>

      <div className="app-content">
        <header className="app-header">
          <button
            type="button"
            className="sidebar-toggle"
            onClick={toggleSidebar}
            aria-label="사이드 메뉴 토글"
            aria-expanded={sidebarOpen}
          >
            메뉴
          </button>
          <BrokerSwitch />
        </header>

        <main className="app-main">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export const appRouter = createBrowserRouter([
  {
    path: "/",
    element: <AppShell />,
    children: [
      { index: true, element: <HomePage /> },
      { path: "realtime", element: <RealtimePage /> },
      {
        path: "stock-master/kospi",
        element: (
          <StockMasterPage
            title="KOSPI 종목 마스터 조회"
            tableName="isw_mst_kospi"
            summary="유가증권시장 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/kosdaq",
        element: (
          <StockMasterPage
            title="KOSDAQ 종목 마스터 조회"
            tableName="isw_mst_kosdaq"
            summary="코스닥 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/konex",
        element: (
          <StockMasterPage
            title="KONEX 종목 마스터 조회"
            tableName="isw_mst_konex"
            summary="코넥스 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-elw",
        element: (
          <StockMasterPage
            title="국내 ELW 종목 마스터 조회"
            tableName="isw_mst_domestic_elw"
            summary="국내 ELW 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-index-future",
        element: (
          <StockMasterPage
            title="국내 지수선물옵션 종목 마스터 조회"
            tableName="isw_mst_domestic_index_future"
            summary="국내 지수선물옵션 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-stock-future",
        element: (
          <StockMasterPage
            title="국내 주식선물옵션 종목 마스터 조회"
            tableName="isw_mst_domestic_stock_future"
            summary="국내 주식선물옵션 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-cme-future",
        element: (
          <StockMasterPage
            title="국내 CME 연계 야간선물 종목 마스터 조회"
            tableName="isw_mst_domestic_cme_future"
            summary="국내 CME 연계 야간선물 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-commodity-future",
        element: (
          <StockMasterPage
            title="국내 상품선물옵션 종목 마스터 조회"
            tableName="isw_mst_domestic_commodity_future"
            summary="국내 상품선물옵션 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-eurex-option",
        element: (
          <StockMasterPage
            title="국내 EUREX 연계 야간옵션 종목 마스터 조회"
            tableName="isw_mst_domestic_eurex_option"
            summary="국내 EUREX 연계 야간옵션 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/domestic-bond",
        element: (
          <StockMasterPage
            title="장내채권 종목 마스터 조회"
            tableName="isw_mst_domestic_bond"
            summary="장내채권 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/overseas-stock",
        element: (
          <StockMasterPage
            title="해외주식 종목 마스터 조회"
            tableName="isw_mst_overseas_stock"
            summary="해외주식 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/overseas-index",
        element: (
          <StockMasterPage
            title="해외주식지수 종목 마스터 조회"
            tableName="isw_mst_overseas_index"
            summary="해외주식지수 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      {
        path: "stock-master/overseas-future",
        element: (
          <StockMasterPage
            title="해외선물옵션 종목 마스터 조회"
            tableName="isw_mst_overseas_future"
            summary="해외선물옵션 종목 마스터를 조회하는 메뉴입니다."
          />
        ),
      },
      { path: "orders", element: <OrdersPage /> },
      { path: "portfolio", element: <PortfolioPage /> },
      { path: "analysis", element: <AnalysisPage /> },
      { path: "strategies", element: <StrategiesPage /> },
      { path: "backtest", element: <BacktestPage /> },
      { path: "scheduler", element: <SchedulerPage /> },
      { path: "settings", element: <SettingsPage /> },
      { path: "notifications", element: <NotificationsPage /> },
      { path: "logs", element: <LogsPage /> },
    ]
  }
]);