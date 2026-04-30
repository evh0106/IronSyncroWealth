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