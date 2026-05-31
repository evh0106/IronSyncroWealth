import { useMemo, useState } from "react";

type Timeframe = "tick" | "minute" | "day" | "week" | "month" | "year";

type Candle = {
  label: string;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
};

const TIMEFRAME_OPTIONS: Array<{ key: Timeframe; label: string; count: number }> = [
  { key: "tick", label: "틱", count: 90 },
  { key: "minute", label: "분", count: 120 },
  { key: "day", label: "일", count: 90 },
  { key: "week", label: "주", count: 60 },
  { key: "month", label: "월", count: 60 },
  { key: "year", label: "년", count: 30 },
];

const SYMBOL_OPTIONS = [
  { code: "005930", name: "삼성전자" },
  { code: "000660", name: "SK하이닉스" },
  { code: "035420", name: "NAVER" },
  { code: "051910", name: "LG화학" },
] as const;

const CHART_WIDTH = 980;
const CHART_HEIGHT = 360;
const PADDING_LEFT = 56;
const PADDING_RIGHT = 16;
const PADDING_TOP = 16;
const PADDING_BOTTOM = 36;

function hashSeed(value: string): number {
  let hash = 0;
  for (let i = 0; i < value.length; i += 1) {
    hash = (hash << 5) - hash + value.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash) + 1;
}

function rng(seed: number): () => number {
  let state = seed;
  return () => {
    state = (state * 1664525 + 1013904223) % 4294967296;
    return state / 4294967296;
  };
}

function getIntervalMs(timeframe: Timeframe): number {
  switch (timeframe) {
    case "tick":
      return 1000;
    case "minute":
      return 60 * 1000;
    case "day":
      return 24 * 60 * 60 * 1000;
    case "week":
      return 7 * 24 * 60 * 60 * 1000;
    case "month":
      return 30 * 24 * 60 * 60 * 1000;
    case "year":
      return 365 * 24 * 60 * 60 * 1000;
    default:
      return 24 * 60 * 60 * 1000;
  }
}

function formatLabel(ts: number, timeframe: Timeframe): string {
  const dt = new Date(ts);
  const yy = String(dt.getFullYear()).slice(2);
  const mm = String(dt.getMonth() + 1).padStart(2, "0");
  const dd = String(dt.getDate()).padStart(2, "0");
  const hh = String(dt.getHours()).padStart(2, "0");
  const mi = String(dt.getMinutes()).padStart(2, "0");
  const ss = String(dt.getSeconds()).padStart(2, "0");

  if (timeframe === "tick") {
    return `${hh}:${mi}:${ss}`;
  }

  if (timeframe === "minute") {
    return `${dd} ${hh}:${mi}`;
  }

  if (timeframe === "day" || timeframe === "week") {
    return `${yy}/${mm}/${dd}`;
  }

  if (timeframe === "month") {
    return `${yy}/${mm}`;
  }

  return `${dt.getFullYear()}`;
}

function basePriceForSymbol(symbol: string): number {
  switch (symbol) {
    case "005930":
      return 81000;
    case "000660":
      return 185000;
    case "035420":
      return 205000;
    case "051910":
      return 350000;
    default:
      return 100000;
  }
}

function generateTestCandles(symbol: string, timeframe: Timeframe, count: number): Candle[] {
  const seed = hashSeed(`${symbol}-${timeframe}`);
  const random = rng(seed);
  const intervalMs = getIntervalMs(timeframe);
  const now = Date.now();

  let previousClose = basePriceForSymbol(symbol);
  const rows: Candle[] = [];

  for (let i = 0; i < count; i += 1) {
    const progress = i / count;
    const trend = (progress - 0.5) * previousClose * 0.03;
    const noise = (random() - 0.5) * previousClose * 0.015;
    const open = Math.max(100, previousClose + (random() - 0.5) * previousClose * 0.007);
    const close = Math.max(100, open + trend * 0.04 + noise);
    const high = Math.max(open, close) + Math.abs((random() - 0.2) * previousClose * 0.01);
    const low = Math.min(open, close) - Math.abs((random() - 0.2) * previousClose * 0.01);
    const volume = Math.floor(400 + random() * 7000 + i * 6);
    const ts = now - (count - 1 - i) * intervalMs;

    rows.push({
      label: formatLabel(ts, timeframe),
      open: Math.round(open),
      high: Math.round(high),
      low: Math.max(1, Math.round(low)),
      close: Math.round(close),
      volume,
    });

    previousClose = close;
  }

  return rows;
}

function movingAverage(candles: Candle[], period: number): Array<number | null> {
  const result: Array<number | null> = [];
  let windowSum = 0;

  for (let i = 0; i < candles.length; i += 1) {
    const close = candles[i].close;
    windowSum += close;

    if (i >= period) {
      windowSum -= candles[i - period].close;
    }

    if (i >= period - 1) {
      result.push(windowSum / period);
    } else {
      result.push(null);
    }
  }

  return result;
}

export function TradeAnalysisPage() {
  const [timeframe, setTimeframe] = useState<Timeframe>("day");
  const [symbol, setSymbol] = useState<string>(SYMBOL_OPTIONS[0].code);

  const timeframeOption = TIMEFRAME_OPTIONS.find((option) => option.key === timeframe) || TIMEFRAME_OPTIONS[2];
  const selectedSymbol = SYMBOL_OPTIONS.find((item) => item.code === symbol) || SYMBOL_OPTIONS[0];

  const candles = useMemo(
    () => generateTestCandles(symbol, timeframe, timeframeOption.count),
    [symbol, timeframe, timeframeOption.count]
  );
  const ma5 = useMemo(() => movingAverage(candles, 5), [candles]);
  const ma20 = useMemo(() => movingAverage(candles, 20), [candles]);
  const ma60 = useMemo(() => movingAverage(candles, 60), [candles]);
  const ma120 = useMemo(() => movingAverage(candles, 120), [candles]);

  const minPrice = Math.min(...candles.map((item) => item.low));
  const maxPrice = Math.max(...candles.map((item) => item.high));
  const priceRange = Math.max(1, maxPrice - minPrice);
  const plotWidth = CHART_WIDTH - PADDING_LEFT - PADDING_RIGHT;
  const plotHeight = CHART_HEIGHT - PADDING_TOP - PADDING_BOTTOM;
  const step = plotWidth / Math.max(1, candles.length - 1);
  const candleWidth = Math.max(3, Math.min(9, step * 0.6));
  const latest = candles[candles.length - 1];
  const first = candles[0];
  const changeRate = ((latest.close - first.open) / Math.max(1, first.open)) * 100;

  const yByPrice = (price: number) => {
    const ratio = (price - minPrice) / priceRange;
    return PADDING_TOP + plotHeight - ratio * plotHeight;
  };

  const axisTicks = 5;
  const yTicks = Array.from({ length: axisTicks + 1 }, (_, idx) => {
    const ratio = idx / axisTicks;
    const price = maxPrice - ratio * priceRange;
    const y = PADDING_TOP + ratio * plotHeight;
    return { price, y };
  });

  return (
    <div className="page-stack">
      <h2>매매 분석</h2>
      <p className="lead">테스트 데이터를 사용해 특정 종목의 틱·분·일·주·월·년 차트를 확인합니다.</p>

      <section className="panel trade-analysis-toolbar">
        <label>
          종목 선택
          <select value={symbol} onChange={(event) => setSymbol(event.target.value)}>
            {SYMBOL_OPTIONS.map((item) => (
              <option key={item.code} value={item.code}>
                {item.code} {item.name}
              </option>
            ))}
          </select>
        </label>
        <div className="timeframe-group" aria-label="차트 주기 선택">
          {TIMEFRAME_OPTIONS.map((option) => (
            <button
              key={option.key}
              type="button"
              className={option.key === timeframe ? "active" : ""}
              onClick={() => setTimeframe(option.key)}
            >
              {option.label}
            </button>
          ))}
        </div>
      </section>

      <section className="panel">
        <div className="trade-analysis-summary">
          <strong>
            {selectedSymbol.code} {selectedSymbol.name}
          </strong>
          <span>
            현재가 {latest.close.toLocaleString("ko-KR")}원
          </span>
          <span className={changeRate >= 0 ? "ok" : "err"}>
            기간 수익률 {changeRate.toFixed(2)}%
          </span>
          <span>거래량 {latest.volume.toLocaleString("ko-KR")}</span>
        </div>

        <div className="chart-wrap" role="img" aria-label={`${selectedSymbol.name} ${timeframeOption.label} 캔들 차트`}>
          <svg viewBox={`0 0 ${CHART_WIDTH} ${CHART_HEIGHT}`}>
            <rect x="0" y="0" width={CHART_WIDTH} height={CHART_HEIGHT} fill="#ffffff" />

            {yTicks.map((tick) => (
              <g key={`tick-${tick.y}`}>
                <line
                  x1={PADDING_LEFT}
                  y1={tick.y}
                  x2={CHART_WIDTH - PADDING_RIGHT}
                  y2={tick.y}
                  stroke="rgba(98, 123, 168, 0.18)"
                  strokeDasharray="4 4"
                />
                <text x={PADDING_LEFT - 8} y={tick.y + 4} textAnchor="end" fontSize="11" fill="#61708c">
                  {Math.round(tick.price).toLocaleString("ko-KR")}
                </text>
              </g>
            ))}

            {candles.map((item, index) => {
              const x = PADDING_LEFT + index * step;
              const highY = yByPrice(item.high);
              const lowY = yByPrice(item.low);
              const openY = yByPrice(item.open);
              const closeY = yByPrice(item.close);
              const up = item.close >= item.open;
              const color = up ? "#1f9d72" : "#d14343";
              const bodyY = Math.min(openY, closeY);
              const bodyHeight = Math.max(1, Math.abs(closeY - openY));

              return (
                <g key={`${item.label}-${index}`}>
                  <line x1={x} y1={highY} x2={x} y2={lowY} stroke={color} strokeWidth="1.2" />
                  <rect
                    x={x - candleWidth / 2}
                    y={bodyY}
                    width={candleWidth}
                    height={bodyHeight}
                    fill={up ? "rgba(31,157,114,0.85)" : "rgba(209,67,67,0.85)"}
                    stroke={color}
                  />
                </g>
              );
            })}

            {ma5.map((value, index) => {
              if (value === null || index === 0 || ma5[index - 1] === null) {
                return null;
              }

              const prev = ma5[index - 1];
              const x1 = PADDING_LEFT + (index - 1) * step;
              const x2 = PADDING_LEFT + index * step;
              const y1 = yByPrice(prev as number);
              const y2 = yByPrice(value);

              return (
                <line
                  key={`ma5-${index}`}
                  x1={x1}
                  y1={y1}
                  x2={x2}
                  y2={y2}
                  stroke="#3b82f6"
                  strokeWidth="1.8"
                />
              );
            })}

            {ma20.map((value, index) => {
              if (value === null || index === 0 || ma20[index - 1] === null) {
                return null;
              }

              const prev = ma20[index - 1];
              const x1 = PADDING_LEFT + (index - 1) * step;
              const x2 = PADDING_LEFT + index * step;
              const y1 = yByPrice(prev as number);
              const y2 = yByPrice(value);

              return (
                <line
                  key={`ma20-${index}`}
                  x1={x1}
                  y1={y1}
                  x2={x2}
                  y2={y2}
                  stroke="#f59e0b"
                  strokeWidth="1.8"
                />
              );
            })}

            {ma60.map((value, index) => {
              if (value === null || index === 0 || ma60[index - 1] === null) {
                return null;
              }

              const prev = ma60[index - 1];
              const x1 = PADDING_LEFT + (index - 1) * step;
              const x2 = PADDING_LEFT + index * step;
              const y1 = yByPrice(prev as number);
              const y2 = yByPrice(value);

              return (
                <line
                  key={`ma60-${index}`}
                  x1={x1}
                  y1={y1}
                  x2={x2}
                  y2={y2}
                  stroke="#8b5cf6"
                  strokeWidth="1.8"
                />
              );
            })}

            {ma120.map((value, index) => {
              if (value === null || index === 0 || ma120[index - 1] === null) {
                return null;
              }

              const prev = ma120[index - 1];
              const x1 = PADDING_LEFT + (index - 1) * step;
              const x2 = PADDING_LEFT + index * step;
              const y1 = yByPrice(prev as number);
              const y2 = yByPrice(value);

              return (
                <line
                  key={`ma120-${index}`}
                  x1={x1}
                  y1={y1}
                  x2={x2}
                  y2={y2}
                  stroke="#0f766e"
                  strokeWidth="1.8"
                />
              );
            })}

            {candles
              .filter((_, index) => index % Math.max(1, Math.floor(candles.length / 8)) === 0)
              .map((item, index) => {
                const originalIndex = index * Math.max(1, Math.floor(candles.length / 8));
                const x = PADDING_LEFT + Math.min(originalIndex, candles.length - 1) * step;
                return (
                  <text key={`x-${item.label}-${index}`} x={x} y={CHART_HEIGHT - 12} fontSize="11" fill="#61708c" textAnchor="middle">
                    {item.label}
                  </text>
                );
              })}
          </svg>
        </div>

        <div className="ma-legend" aria-label="이동평균선 범례">
          <span>
            <i className="ma-dot ma5" />
            MA5
          </span>
          <span>
            <i className="ma-dot ma20" />
            MA20
          </span>
          <span>
            <i className="ma-dot ma60" />
            MA60
          </span>
          <span>
            <i className="ma-dot ma120" />
            MA120
          </span>
        </div>

        <table className="basic-table">
          <thead>
            <tr>
              <th>시점</th>
              <th>시가</th>
              <th>고가</th>
              <th>저가</th>
              <th>종가</th>
              <th>거래량</th>
            </tr>
          </thead>
          <tbody>
            {candles.slice(-12).map((item, idx) => (
              <tr key={`${item.label}-row-${idx}`}>
                <td>{item.label}</td>
                <td>{item.open.toLocaleString("ko-KR")}</td>
                <td>{item.high.toLocaleString("ko-KR")}</td>
                <td>{item.low.toLocaleString("ko-KR")}</td>
                <td>{item.close.toLocaleString("ko-KR")}</td>
                <td>{item.volume.toLocaleString("ko-KR")}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}
