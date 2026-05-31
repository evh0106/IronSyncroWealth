import { useState } from "react";
import { useUiStore } from "@/app/store/ui-store";
import { apiClient } from "@/shared/api/client";

type DownloadResultItem = {
  market: string;
  file: string | null;
  rows: number;
  error?: string | null;
  savedAt: string;
};

type DownloadAllResponse = {
  status: string;
  message: string;
  requestedAt: string;
  results: DownloadResultItem[];
};

type StockMasterPageProps = {
  title: string;
  tableName: string;
  summary: string;
  mode?: "default" | "top";
};

function formatSavedAt(iso: string): string {
  try {
    return new Date(iso).toLocaleString("ko-KR", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  } catch {
    return iso;
  }
}

export function StockMasterPage({ title, tableName, summary, mode = "default" }: StockMasterPageProps) {
  const isTopMode = mode === "top";
  const broker = useUiStore((state) => state.broker);
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadResult, setDownloadResult] = useState<DownloadAllResponse | null>(null);
  const [downloadError, setDownloadError] = useState<string | null>(null);

  const handleDownloadAll = async () => {
    setIsDownloading(true);
    setDownloadResult(null);
    setDownloadError(null);

    try {
      const { data } = await apiClient(broker).post<DownloadAllResponse>(
        "/api/v1/stock-master/download-all"
      );
      setDownloadResult(data);
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
                {isDownloading ? "다운로드 중..." : "모든 마스터 파일 다운로드"}
              </button>
            </div>
            {downloadResult ? (
              <p className={downloadResult.status === "ok" ? "ok" : "err"}>
                {downloadResult.message}
              </p>
            ) : null}
            {downloadError ? <p className="err">{downloadError}</p> : null}
            <table className="basic-table" aria-label="종목 마스터 파일 목록">
              <thead>
                <tr>
                  <th scope="col">시장</th>
                  <th scope="col">파일명</th>
                  <th scope="col">행 수</th>
                  <th scope="col">저장일시</th>
                  <th scope="col">상태</th>
                </tr>
              </thead>
              <tbody>
                {downloadResult && downloadResult.results.length > 0 ? (
                  downloadResult.results.map((item) => (
                    <tr key={item.market}>
                      <td>{item.market}</td>
                      <td>{item.file ?? "-"}</td>
                      <td style={{ textAlign: "right" }}>{item.error ? "-" : item.rows.toLocaleString()}</td>
                      <td>{formatSavedAt(item.savedAt)}</td>
                      <td style={{ color: item.error ? "var(--err, #d33)" : "var(--ok, #2a7)" }}>
                        {item.error ? `오류: ${item.error}` : "완료"}
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={5}>
                      {isDownloading
                        ? "마스터 파일 다운로드 중입니다..."
                        : "버튼을 눌러 마스터 파일을 다운로드하세요."}
                    </td>
                  </tr>
                )}
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