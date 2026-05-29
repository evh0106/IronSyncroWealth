type StockMasterPageProps = {
  title: string;
  tableName: string;
  summary: string;
};

export function StockMasterPage({ title, tableName, summary }: StockMasterPageProps) {
  return (
    <div className="page-stack">
      <h1>{title}</h1>
      <p className="lead">{summary}</p>

      <section className="panel">
        <h3>조회 대상 테이블</h3>
        <p>{tableName}</p>
        <p className="lead">세부 조회 화면은 다음 단계에서 연결합니다.</p>
      </section>
    </div>
  );
}