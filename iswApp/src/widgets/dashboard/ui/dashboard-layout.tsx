import { AccountSummary } from "@/widgets/account-summary/ui/account-summary";
import { MarketBoard } from "@/widgets/market-board/ui/market-board";

export function DashboardLayout() {
  return (
    <section className="dashboard-grid">
      <MarketBoard symbol="005930" />
      <AccountSummary accountNo="81241972" />
    </section>
  );
}