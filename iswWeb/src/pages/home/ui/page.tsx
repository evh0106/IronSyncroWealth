import { DashboardLayout } from "@/widgets/dashboard/ui/dashboard-layout";

export function HomePage() {
  return (
    <div className="page-stack">
      <h1>Market Command Center</h1>
      <p className="lead">실시간 시세와 계좌 요약을 하나의 보드에서 확인합니다.</p>
      <DashboardLayout />
    </div>
  );
}