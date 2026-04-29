import { createBrowserRouter, NavLink, Outlet } from "react-router-dom";
import { HomePage } from "@/pages/home/ui/page";
import { TradePage } from "@/pages/trade/ui/page";
import { SettingsPage } from "@/pages/settings/ui/page";
import { BrokerSwitch } from "@/features/broker-switch/ui/broker-switch";

function AppShell() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="brand">IronSyncroWealth</div>
        <nav className="main-nav">
          <NavLink to="/" end>
            Home
          </NavLink>
          <NavLink to="/trade">Trade</NavLink>
          <NavLink to="/settings">Settings</NavLink>
        </nav>
        <BrokerSwitch />
      </header>
      <main className="app-main">
        <Outlet />
      </main>
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