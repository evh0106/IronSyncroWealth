export function LogsPage() {
  return (
    <div className="page-stack">
      <h2>시스템 로그</h2>
      <p className="lead">FastAPI 요청 로그, Celery 실행 이력, 외부 API 에러를 레벨별로 표시합니다.</p>
    </div>
  );
}
