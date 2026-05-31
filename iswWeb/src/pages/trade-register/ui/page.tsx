import { FormEvent, useMemo, useState } from "react";

type OrderSide = "buy" | "sell";
type OrderType = "limit" | "market";

const MARKET_OPTIONS = [
  { value: "kospi", label: "KOSPI" },
  { value: "kosdaq", label: "KOSDAQ" },
  { value: "konex", label: "KONEX" },
  { value: "domestic-elw", label: "국내 ELW" },
  { value: "domestic-index-future", label: "지수선물옵션" },
  { value: "domestic-stock-future", label: "주식선물옵션" },
  { value: "domestic-cme-future", label: "CME 연계 야간선물" },
  { value: "domestic-commodity-future", label: "상품선물옵션" },
  { value: "domestic-eurex-option", label: "EUREX 연계 야간옵션" },
  { value: "domestic-bond", label: "장내채권" },
  { value: "overseas-stock", label: "해외주식" },
  { value: "overseas-index", label: "해외주식지수" },
  { value: "overseas-future", label: "해외선물옵션" },
] as const;

export function TradeRegisterPage() {
  const [accountNo, setAccountNo] = useState("");
  const [symbol, setSymbol] = useState("");
  const [market, setMarket] = useState("");
  const [orderDate, setOrderDate] = useState("");
  const [orderTime, setOrderTime] = useState("");
  const [side, setSide] = useState<OrderSide>("buy");
  const [orderType, setOrderType] = useState<OrderType>("limit");
  const [quantity, setQuantity] = useState(1);
  const [price, setPrice] = useState(0);
  const [memo, setMemo] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const estimatedAmount = useMemo(() => quantity * price, [quantity, price]);

  const canSubmit = accountNo.trim() !== "" && symbol.trim() !== "" && market !== "" && quantity > 0;
  const selectedMarketLabel = MARKET_OPTIONS.find((option) => option.value === market)?.label || "-";

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!canSubmit) {
      return;
    }

    setSubmitted(true);
  };

  return (
    <div className="page-stack">
      <h2>매매등록</h2>
      <p className="lead">주식 매수/매도 주문 정보를 입력하고 주문 요청 내용을 확인합니다.</p>

      <section className="panel">
        <h3>주문 입력</h3>
        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <label>
              계좌번호
              <input
                value={accountNo}
                onChange={(event) => setAccountNo(event.target.value)}
                placeholder="예: 12345678-01"
              />
            </label>

            <label>
              종목코드
              <input
                value={symbol}
                onChange={(event) => setSymbol(event.target.value.toUpperCase())}
                placeholder="예: 005930"
              />
            </label>

            <label>
              주문일자
              <input
                type="date"
                value={orderDate}
                onChange={(event) => setOrderDate(event.target.value)}
              />
            </label>

            <label>
              주문시간
              <input
                type="time"
                step={1}
                value={orderTime}
                onChange={(event) => setOrderTime(event.target.value)}
              />
            </label>

            <label>
              시장 구분
              <select value={market} onChange={(event) => setMarket(event.target.value)}>
                <option value="">시장 선택</option>
                {MARKET_OPTIONS.map((option) => (
                  <option key={option.value} value={option.value}>
                    {option.label}
                  </option>
                ))}
              </select>
            </label>

            <label>
              매매구분
              <select
                value={side}
                onChange={(event) => setSide(event.target.value as OrderSide)}
              >
                <option value="buy">매수</option>
                <option value="sell">매도</option>
              </select>
            </label>

            <label>
              주문유형
              <select
                value={orderType}
                onChange={(event) => setOrderType(event.target.value as OrderType)}
              >
                <option value="limit">지정가</option>
                <option value="market">시장가</option>
              </select>
            </label>

            <label>
              수량
              <input
                type="number"
                min={1}
                step={1}
                value={quantity}
                onChange={(event) => setQuantity(Number(event.target.value) || 0)}
              />
            </label>

            <label>
              가격
              <input
                type="number"
                min={0}
                step={1}
                value={price}
                onChange={(event) => setPrice(Number(event.target.value) || 0)}
                disabled={orderType === "market"}
              />
            </label>
          </div>

          <label>
            메모
            <input
              value={memo}
              onChange={(event) => setMemo(event.target.value)}
              placeholder="주문 사유를 간단히 기록하세요."
            />
          </label>

          <p className="lead">
            예상 주문금액: {Number.isFinite(estimatedAmount) ? estimatedAmount.toLocaleString("ko-KR") : "0"}원
          </p>

          <button type="submit" disabled={!canSubmit}>
            주문 등록
          </button>
        </form>

        {submitted ? (
          <div>
            <p className="ok">주문 입력이 등록되었습니다. (시연용 화면)</p>
            <table className="basic-table">
              <tbody>
                <tr>
                  <th>계좌번호</th>
                  <td>{accountNo}</td>
                </tr>
                <tr>
                  <th>종목코드</th>
                  <td>{symbol}</td>
                </tr>
                <tr>
                  <th>시장 구분</th>
                  <td>{selectedMarketLabel}</td>
                </tr>
                <tr>
                  <th>주문일자</th>
                  <td>{orderDate || "-"}</td>
                </tr>
                <tr>
                  <th>주문시간</th>
                  <td>{orderTime || "-"}</td>
                </tr>
                <tr>
                  <th>매매구분</th>
                  <td>{side === "buy" ? "매수" : "매도"}</td>
                </tr>
                <tr>
                  <th>주문유형</th>
                  <td>{orderType === "limit" ? "지정가" : "시장가"}</td>
                </tr>
                <tr>
                  <th>수량</th>
                  <td>{quantity.toLocaleString("ko-KR")}</td>
                </tr>
                <tr>
                  <th>가격</th>
                  <td>{price.toLocaleString("ko-KR")}</td>
                </tr>
                <tr>
                  <th>메모</th>
                  <td>{memo || "-"}</td>
                </tr>
              </tbody>
            </table>
          </div>
        ) : null}
      </section>
    </div>
  );
}
