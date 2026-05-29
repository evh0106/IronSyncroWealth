import { useOrderSubmit } from "@/features/order-submit/model/use-order-submit";

export function OrderPanel() {
  const order = useOrderSubmit();

  return (
    <section className="panel">
      <h3>Order Panel</h3>
      <div className="form-grid">
        <label>
          Account
          <input value={order.accountNo} onChange={(e) => order.setAccountNo(e.target.value)} />
        </label>
        <label>
          Symbol
          <input value={order.symbol} onChange={(e) => order.setSymbol(e.target.value)} />
        </label>
        <label>
          Side
          <select value={order.side} onChange={(e) => order.setSide(e.target.value as "buy" | "sell")}>
            <option value="buy">BUY</option>
            <option value="sell">SELL</option>
          </select>
        </label>
        <label>
          Qty
          <input
            type="number"
            value={order.quantity}
            onChange={(e) => order.setQuantity(Number(e.target.value))}
          />
        </label>
        <label>
          Price
          <input type="number" value={order.price} onChange={(e) => order.setPrice(Number(e.target.value))} />
        </label>
      </div>
      <button onClick={order.submit} disabled={!order.canSubmit || order.isPending} type="button">
        {order.isPending ? "Submitting..." : "Submit Order"}
      </button>
      {order.isSuccess ? <p className="ok">주문 요청이 성공적으로 전송되었습니다.</p> : null}
      {order.error ? <p className="err">주문 요청 중 오류가 발생했습니다.</p> : null}
    </section>
  );
}