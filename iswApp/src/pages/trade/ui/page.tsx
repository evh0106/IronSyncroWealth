import { OrderPanel } from "@/features/order-submit/ui/order-panel";
import { OrderBook } from "@/widgets/order-book/ui/order-book";

export function TradePage() {
  return (
    <div className="page-stack">
      <h1>Trade Deck</h1>
      <p className="lead">주문 실행과 체결 모니터링을 단일 화면에서 처리합니다.</p>
      <section className="dashboard-grid">
        <OrderPanel />
        <OrderBook />
      </section>
    </div>
  );
}