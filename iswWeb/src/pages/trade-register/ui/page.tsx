import { FormEvent, useMemo, useState } from "react";
import { useUiStore } from "@/app/store/ui-store";
import { apiClient } from "@/shared/api/client";

type OrderSide = "buy" | "sell";
type OrderType = "limit" | "market";

const MARKET_OPTIONS = [
  { value: "kospi", label: "KOSPI", tableName: "isw_mst_kospi" },
  { value: "kosdaq", label: "KOSDAQ", tableName: "isw_mst_kosdaq" },
  { value: "konex", label: "KONEX", tableName: "isw_mst_konex" },
  { value: "domestic-elw", label: "국내 ELW", tableName: "isw_mst_domestic_elw" },
  { value: "domestic-index-future", label: "지수선물옵션", tableName: "isw_mst_domestic_index_future" },
  { value: "domestic-stock-future", label: "주식선물옵션", tableName: "isw_mst_domestic_stock_future" },
  { value: "domestic-cme-future", label: "CME 연계 야간선물", tableName: "isw_mst_domestic_cme_future" },
  { value: "domestic-commodity-future", label: "상품선물옵션", tableName: "isw_mst_domestic_commodity_future" },
  { value: "domestic-eurex-option", label: "EUREX 연계 야간옵션", tableName: "isw_mst_domestic_eurex_option" },
  { value: "domestic-bond", label: "장내채권", tableName: "isw_mst_domestic_bond" },
  { value: "overseas-stock", label: "해외주식", tableName: "isw_mst_overseas_stock" },
  { value: "overseas-index", label: "해외주식지수", tableName: "isw_mst_overseas_index" },
  { value: "overseas-future", label: "해외선물옵션", tableName: "isw_mst_overseas_future" },
] as const;

type TablePreviewResponse = {
  status: string;
  message: string;
  tableName: string;
  rowCount: number;
  totalCount: number;
  page: number;
  pageSize: number;
  totalPages: number;
  columns: string[];
  columnLabels?: Record<string, string>;
  rows: Array<Record<string, string | number | null>>;
};

function todayForInput(): string {
  const now = new Date();
  const y = now.getFullYear();
  const m = String(now.getMonth() + 1).padStart(2, "0");
  const d = String(now.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

function toYyyymmdd(dateStr: string): string {
  return dateStr.replaceAll("-", "");
}

function extractCellText(value: string | number | null | undefined): string {
  if (value === null || value === undefined) {
    return "";
  }
  return String(value);
}

function pickCodeKey(columns: string[]): string | null {
  const priorities = ["code", "symbol", "shcode", "stock_code", "stk_cd", "isu_cd"];
  for (const priority of priorities) {
    const hit = columns.find((column) => column.toLowerCase().includes(priority));
    if (hit) {
      return hit;
    }
  }
  return columns[0] ?? null;
}

function pickNameKey(columns: string[]): string | null {
  const priorities = ["name", "nm", "kor", "eng"];
  for (const priority of priorities) {
    const hit = columns.find((column) => column.toLowerCase().includes(priority));
    if (hit) {
      return hit;
    }
  }
  return columns[1] ?? null;
}

export function TradeRegisterPage() {
  const broker = useUiStore((state) => state.broker);
  const [accountNo, setAccountNo] = useState("");
  const [symbol, setSymbol] = useState("");
  const [market, setMarket] = useState("");
  const [orderDateTime, setOrderDateTime] = useState("");
  const [side, setSide] = useState<OrderSide>("buy");
  const [orderType, setOrderType] = useState<OrderType>("limit");
  const [quantity, setQuantity] = useState(1);
  const [price, setPrice] = useState(0);
  const [memo, setMemo] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [isLookupOpen, setIsLookupOpen] = useState(false);
  const [lookupKeyword, setLookupKeyword] = useState("");
  const [isLookupLoading, setIsLookupLoading] = useState(false);
  const [lookupError, setLookupError] = useState<string | null>(null);
  const [lookupColumns, setLookupColumns] = useState<string[]>([]);
  const [lookupRows, setLookupRows] = useState<Array<Record<string, string | number | null>>>([]);

  const estimatedAmount = useMemo(() => quantity * price, [quantity, price]);

  const canSubmit = accountNo.trim() !== "" && symbol.trim() !== "" && market !== "" && quantity > 0;
  const selectedMarket = MARKET_OPTIONS.find((option) => option.value === market);
  const selectedMarketLabel = selectedMarket?.label || "-";
  const codeKey = pickCodeKey(lookupColumns);
  const nameKey = pickNameKey(lookupColumns);
  const filteredLookupRows = lookupRows.filter((row) => {
    const keyword = lookupKeyword.trim().toLowerCase();
    if (!keyword) {
      return true;
    }
    return Object.values(row).some((value) => extractCellText(value).toLowerCase().includes(keyword));
  });

  const openLookup = async () => {
    if (!selectedMarket) {
      setLookupError("시장 구분을 먼저 선택하세요.");
      setIsLookupOpen(true);
      return;
    }

    setLookupError(null);
    setLookupKeyword((prev) => (prev.trim() ? prev : symbol));
    setIsLookupOpen(true);
    setIsLookupLoading(true);

    try {
      const { data } = await apiClient(broker).get<TablePreviewResponse>(
        `/api/v1/stock-master/table/${selectedMarket.tableName}`,
        {
          params: {
            page: 1,
            limit: 200,
            base_date: toYyyymmdd(todayForInput()),
          },
        }
      );
      setLookupColumns(data.columns || []);
      setLookupRows(data.rows || []);
    } catch {
      setLookupColumns([]);
      setLookupRows([]);
      setLookupError("종목 마스터 조회 중 오류가 발생했습니다.");
    } finally {
      setIsLookupLoading(false);
    }
  };

  const selectSymbol = (row: Record<string, string | number | null>) => {
    const symbolKey = codeKey;
    if (!symbolKey) {
      return;
    }
    const selectedSymbol = extractCellText(row[symbolKey]);
    setSymbol(selectedSymbol.toUpperCase());
    setIsLookupOpen(false);
  };

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
              종목코드
              <div style={{ display: "flex", gap: 8 }}>
                <input
                  value={symbol}
                  onChange={(event) => setSymbol(event.target.value.toUpperCase())}
                  placeholder="예: 005930"
                />
                <button type="button" onClick={openLookup} disabled={!selectedMarket}>
                  검색
                </button>
              </div>
            </label>

            <label>
              주문일시
              <input
                type="datetime-local"
                value={orderDateTime}
                onChange={(event) => setOrderDateTime(event.target.value)}
              />
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
                  <th>주문일시</th>
                  <td>{orderDateTime || "-"}</td>
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

      {isLookupOpen ? (
        <div className="lookup-modal-backdrop" role="presentation">
          <section className="panel lookup-modal" role="dialog" aria-modal="true" aria-label="종목코드 검색">
            <h3>종목코드 검색</h3>
            <p className="lead">시장: {selectedMarketLabel}</p>
            <div className="stock-master-top-actions">
              <input
                value={lookupKeyword}
                onChange={(event) => setLookupKeyword(event.target.value)}
                placeholder="종목코드 또는 종목명 검색"
              />
              <button type="button" onClick={openLookup} disabled={isLookupLoading}>
                새로고침
              </button>
              <button type="button" onClick={() => setIsLookupOpen(false)}>
                닫기
              </button>
            </div>
            {lookupError ? <p className="err">{lookupError}</p> : null}
            <table className="basic-table" aria-label="시장 종목 검색 결과">
              <thead>
                <tr>
                  <th scope="col">선택</th>
                  <th scope="col">종목코드</th>
                  <th scope="col">종목명</th>
                </tr>
              </thead>
              <tbody>
                {isLookupLoading ? (
                  <tr>
                    <td colSpan={3}>검색 데이터를 불러오는 중입니다...</td>
                  </tr>
                ) : filteredLookupRows.length > 0 ? (
                  filteredLookupRows.map((row, index) => (
                    <tr key={`lookup-${index}`}>
                      <td>
                        <button type="button" onClick={() => selectSymbol(row)} disabled={!codeKey}>
                          선택
                        </button>
                      </td>
                      <td>{codeKey ? extractCellText(row[codeKey]) : "-"}</td>
                      <td>{nameKey ? extractCellText(row[nameKey]) : "-"}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={3}>검색 결과가 없습니다.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </section>
        </div>
      ) : null}
    </div>
  );
}
