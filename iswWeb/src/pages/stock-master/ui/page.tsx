import { useState } from "react";
import { useUiStore } from "@/app/store/ui-store";
import { apiClient } from "@/shared/api/client";

type StockMasterPageProps = {
  title: string;
  tableName: string;
  summary: string;
  mode?: "default" | "top";
};

export function StockMasterPage({ title, tableName, summary, mode = "default" }: StockMasterPageProps) {
  const isTopMode = mode === "top";
  const broker = useUiStore((state) => state.broker);
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadSuccess, setDownloadSuccess] = useState<string | null>(null);
  const [downloadError, setDownloadError] = useState<string | null>(null);

  const handleDownloadAll = async () => {
    setIsDownloading(true);
    setDownloadSuccess(null);
    setDownloadError(null);

    try {
      const { data } = await apiClient(broker).post<{ status: string; message: string }>(
        "/api/v1/stock-master/download-all"
      );

      if (data.status === "accepted") {
        setDownloadSuccess(data.message);
        return;
      }

      setDownloadError("다운로드 요청이 정상적으로 접수되지 않았습니다.");
    } catch {
      setDownloadError("다운로드 요청 중 오류가 발생했습니다.");
    } finally {
      setIsDownloading(false);
    }
  };

  return (
    <div className="page-stack">
      <h1>{title}</h1>
      <p className="lead">{summary}</p>

      <section className="panel">
        {isTopMode ? (
          <>
            <h3>종목 마스터 파일 목록</h3>
            <div className="stock-master-top-actions">
              <button type="button" onClick={handleDownloadAll} disabled={isDownloading}>
                {isDownloading ? "요청 중..." : "모든 마스터 파일 다운로드"}
              </button>
            </div>
            {downloadSuccess ? <p className="ok">{downloadSuccess}</p> : null}
            {downloadError ? <p className="err">{downloadError}</p> : null}
            <table className="basic-table" aria-label="종목 마스터 파일 목록">
              <thead>
                <tr>
                  <th scope="col">시장</th>
                  <th scope="col">파일명</th>
                  <th scope="col">수정일</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td colSpan={3}>표 데이터는 다음 단계에서 연결합니다.</td>
                </tr>
              </tbody>
            </table>
          </>
        ) : (
          <>
            <h3>조회 대상 테이블</h3>
            <p>{tableName}</p>
            <p className="lead">세부 조회 화면은 다음 단계에서 연결합니다.</p>
          </>
        )}
      </section>
    </div>
  );
}