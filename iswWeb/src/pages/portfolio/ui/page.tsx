type HoldingRow = {
  symbol: string;
  name: string;
  market: string;
  quantity: number;
  avgPrice: number;
  currentPrice: number;
};

const HOLDINGS: HoldingRow[] = [
  { symbol: "005930", name: "삼성전자", market: "KOSPI", quantity: 38, avgPrice: 74200, currentPrice: 78100 },
  { symbol: "000660", name: "SK하이닉스", market: "KOSPI", quantity: 14, avgPrice: 173000, currentPrice: 188200 },
  { symbol: "035420", name: "NAVER", market: "KOSPI", quantity: 9, avgPrice: 214000, currentPrice: 205500 },
  { symbol: "091990", name: "셀트리온헬스케어", market: "KOSDAQ", quantity: 27, avgPrice: 68800, currentPrice: 71300 },
  { symbol: "196170", name: "알테오젠", market: "KOSDAQ", quantity: 6, avgPrice: 289000, currentPrice: 302000 },
];

function formatKrw(value: number): string {
  return `${value.toLocaleString("ko-KR")}원`;
}

export function PortfolioPage() {
  const enriched = HOLDINGS.map((row) => {
    const buyAmount = row.quantity * row.avgPrice;
    const evalAmount = row.quantity * row.currentPrice;
    const pnl = evalAmount - buyAmount;
    const pnlRate = buyAmount > 0 ? (pnl / buyAmount) * 100 : 0;
    return { ...row, buyAmount, evalAmount, pnl, pnlRate };
  });

  const totalBuy = enriched.reduce((sum, row) => sum + row.buyAmount, 0);
  const totalEval = enriched.reduce((sum, row) => sum + row.evalAmount, 0);
  const totalPnl = totalEval - totalBuy;
  const totalRate = totalBuy > 0 ? (totalPnl / totalBuy) * 100 : 0;

  const cashBalance = 3_450_000;
  const totalAsset = totalEval + cashBalance;
  const stockWeight = totalAsset > 0 ? (totalEval / totalAsset) * 100 : 0;
  const cashWeight = totalAsset > 0 ? (cashBalance / totalAsset) * 100 : 0;

  const maxWin = enriched.reduce((max, row) => (row.pnlRate > max.pnlRate ? row : max), enriched[0]);
  const maxLoss = enriched.reduce((min, row) => (row.pnlRate < min.pnlRate ? row : min), enriched[0]);

  return (
    <div className="page-stack">
      <h2>보유 종목</h2>
      <p className="lead">현재 포지션의 평가금액, 평가손익, 비중 정보를 한 화면에서 확인합니다.</p>

      <section className="panel portfolio-metrics">
        <article>
          <h3>총 평가금액</h3>
          <strong>{formatKrw(totalEval)}</strong>
          <p>매수금액 {formatKrw(totalBuy)}</p>
        </article>
        <article>
          <h3>평가손익</h3>
          <strong className={totalPnl >= 0 ? "ok" : "err"}>{formatKrw(totalPnl)}</strong>
          <p className={totalRate >= 0 ? "ok" : "err"}>{totalRate.toFixed(2)}%</p>
        </article>
        <article>
          <h3>예수금</h3>
          <strong>{formatKrw(cashBalance)}</strong>
          <p>총 자산 {formatKrw(totalAsset)}</p>
        </article>
      </section>

      <section className="panel portfolio-split-grid">
        <article>
          <h3>자산 비중</h3>
          <div className="portfolio-weight-row">
            <span>주식 {stockWeight.toFixed(1)}%</span>
            <div className="portfolio-weight-track">
              <div className="portfolio-weight-fill stock" style={{ width: `${stockWeight}%` }} />
            </div>
          </div>
          <div className="portfolio-weight-row">
            <span>현금 {cashWeight.toFixed(1)}%</span>
            <div className="portfolio-weight-track">
              <div className="portfolio-weight-fill cash" style={{ width: `${cashWeight}%` }} />
            </div>
          </div>
        </article>
        <article>
          <h3>수익률 포인트</h3>
          <p>
            최고 수익: <strong className="ok">{maxWin.name} ({maxWin.pnlRate.toFixed(2)}%)</strong>
          </p>
          <p>
            최저 수익: <strong className="err">{maxLoss.name} ({maxLoss.pnlRate.toFixed(2)}%)</strong>
          </p>
        </article>
      </section>

      <section className="panel">
        <h3>보유 종목 상세</h3>
        <table className="basic-table" aria-label="보유 종목 테이블">
          <thead>
            <tr>
              <th>종목코드</th>
              <th>종목명</th>
              <th>시장</th>
              <th>보유수량</th>
              <th>평균단가</th>
              <th>현재가</th>
              <th>매수금액</th>
              <th>평가금액</th>
              <th>평가손익</th>
              <th>수익률</th>
            </tr>
          </thead>
          <tbody>
            {enriched.map((row) => (
              <tr key={row.symbol}>
                <td>{row.symbol}</td>
                <td>{row.name}</td>
                <td>{row.market}</td>
                <td style={{ textAlign: "right" }}>{row.quantity.toLocaleString("ko-KR")}</td>
                <td style={{ textAlign: "right" }}>{formatKrw(row.avgPrice)}</td>
                <td style={{ textAlign: "right" }}>{formatKrw(row.currentPrice)}</td>
                <td style={{ textAlign: "right" }}>{formatKrw(row.buyAmount)}</td>
                <td style={{ textAlign: "right" }}>{formatKrw(row.evalAmount)}</td>
                <td style={{ textAlign: "right" }} className={row.pnl >= 0 ? "ok" : "err"}>
                  {formatKrw(row.pnl)}
                </td>
                <td style={{ textAlign: "right" }} className={row.pnlRate >= 0 ? "ok" : "err"}>
                  {row.pnlRate.toFixed(2)}%
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}
