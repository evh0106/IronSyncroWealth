import { useUiStore } from "@/app/store/ui-store";
import { useAccountSummary } from "@/entities/account/api/queries";

type Props = {
  accountNo: string;
};

export function AccountSummary({ accountNo }: Props) {
  const broker = useUiStore((state) => state.broker);
  const { data, isLoading } = useAccountSummary(broker, accountNo);

  return (
    <section className="panel">
      <h3>Account Summary</h3>
      {isLoading ? <p>Loading account...</p> : null}
      {data ? (
        <div className="kv-grid">
          <p>Account</p>
          <p>{data.accountNo}</p>
          <p>Balance</p>
          <p>{data.balance.toLocaleString()}</p>
          <p>PnL</p>
          <p>{data.pnlRate}%</p>
        </div>
      ) : (
        <p>계좌 데이터가 없습니다.</p>
      )}
    </section>
  );
}