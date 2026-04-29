import { useUiStore } from "@/app/store/ui-store";
import { useMarketQuote } from "@/entities/market/api/queries";
import { useRealtime } from "@/features/realtime-subscribe/model/use-realtime";

type Props = {
  symbol: string;
};

export function MarketBoard({ symbol }: Props) {
  const broker = useUiStore((state) => state.broker);
  const { data, isLoading } = useMarketQuote(broker, symbol);

  useRealtime(broker, symbol);

  return (
    <section className="panel">
      <h3>Market Board</h3>
      {isLoading ? <p>Loading quote...</p> : null}
      {data ? (
        <div className="kv-grid">
          <p>Symbol</p>
          <p>{data.symbol}</p>
          <p>Price</p>
          <p>{data.price.toLocaleString()}</p>
          <p>Change</p>
          <p>{data.changeRate}%</p>
          <p>Volume</p>
          <p>{data.volume.toLocaleString()}</p>
        </div>
      ) : (
        <p>시세 데이터가 없습니다.</p>
      )}
    </section>
  );
}