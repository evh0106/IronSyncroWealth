import { createBrowserRouter, NavLink, Outlet } from "react-router-dom";
import { HomePage } from "@/pages/home/ui/page";
import { TradePage } from "@/pages/trade/ui/page";
import { SettingsPage } from "@/pages/settings/ui/page";
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
          <NavLink to="/" end>
            Home
          </NavLink>
          <NavLink to="/trade">Trade</NavLink>
          <NavLink to="/settings">Settings</NavLink>
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
      { path: "trade", element: <TradePage /> },
      { path: "settings", element: <SettingsPage /> }
    ]
  }
]);