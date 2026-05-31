import { useEffect, useState } from "react";
import { useUiStore } from "@/app/store/ui-store";
import { apiClient } from "@/shared/api/client";

type DownloadResultItem = {
  market: string;
  file: string | null;
  rows: number;
  db_rows: number;
  error?: string | null;
  savedAt: string;
};

type DownloadAllResponse = {
  status: string;
  message: string;
  requestedAt: string;
  results: DownloadResultItem[];
};

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

type StockMasterPageProps = {
  title: string;
  tableName: string;
  summary: string;
  mode?: "default" | "top";
};

function toYyyymmdd(dateStr: string): string {
  return dateStr.replaceAll("-", "");
}

function todayForInput(): string {
  const now = new Date();
  const y = now.getFullYear();
  const m = String(now.getMonth() + 1).padStart(2, "0");
  const d = String(now.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

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
  const [isLoadingFiles, setIsLoadingFiles] = useState(false);
  const [isLoadingTable, setIsLoadingTable] = useState(false);
  const [tablePage, setTablePage] = useState(1);
  const [baseDateInput, setBaseDateInput] = useState(todayForInput());
  const [appliedBaseDate, setAppliedBaseDate] = useState(toYyyymmdd(todayForInput()));
  const [downloadResult, setDownloadResult] = useState<DownloadAllResponse | null>(null);
  const [downloadError, setDownloadError] = useState<string | null>(null);
  const [tableResult, setTableResult] = useState<TablePreviewResponse | null>(null);
  const [tableError, setTableError] = useState<string | null>(null);

  useEffect(() => {
    if (!isTopMode) {
      return;
    }

    const loadMstFiles = async () => {
      setIsLoadingFiles(true);
      setDownloadError(null);
      try {
        const { data } = await apiClient(broker).get<DownloadAllResponse>(
          "/api/v1/stock-master/files"
        );
        setDownloadResult(data);
      } catch {
        setDownloadError("마스터 파일 정보 조회 중 오류가 발생했습니다.");
      } finally {
        setIsLoadingFiles(false);
      }
    };

    loadMstFiles();
  }, [broker, isTopMode]);

  useEffect(() => {
    if (isTopMode) {
      return;
    }

    const loadTable = async () => {
      setIsLoadingTable(true);
      setTableError(null);
      try {
        const { data } = await apiClient(broker).get<TablePreviewResponse>(
          `/api/v1/stock-master/table/${tableName}`,
          { params: { page: tablePage, limit: 50, base_date: appliedBaseDate } }
        );
        setTableResult(data);
      } catch {
        setTableError("테이블 조회 중 오류가 발생했습니다.");
      } finally {
        setIsLoadingTable(false);
      }
    };

    loadTable();
  }, [broker, isTopMode, tableName, tablePage, appliedBaseDate]);

  useEffect(() => {
    if (!isTopMode) {
      setTablePage(1);
      const today = todayForInput();
      setBaseDateInput(today);
      setAppliedBaseDate(toYyyymmdd(today));
    }
  }, [isTopMode, tableName]);

  const handleSearchBaseDate = () => {
    const normalized = toYyyymmdd(baseDateInput);
    if (normalized.length !== 8) {
      setTableError("기준일자는 YYYY-MM-DD 형식으로 입력하세요.");
      return;
    }
    setTableError(null);
    setTablePage(1);
    setAppliedBaseDate(normalized);
  };

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
                  <th scope="col">NO</th>
                  <th scope="col">시장</th>
                  <th scope="col">파일명</th>
                  <th scope="col">행 수</th>
                  <th scope="col">DB 저장</th>
                  <th scope="col">저장일시</th>
                  <th scope="col">상태</th>
                </tr>
              </thead>
              <tbody>
                {downloadResult && downloadResult.results.length > 0
                  ? downloadResult.results.map((item, idx) => (
                      <tr key={item.market}>
                        <td style={{ textAlign: "right" }}>{idx + 1}</td>
                        <td>{item.market}</td>
                        <td>{item.file ?? "-"}</td>
                        <td style={{ textAlign: "right" }}>{item.error ? "-" : item.rows.toLocaleString()}</td>
                        <td style={{ textAlign: "right" }}>{item.error ? "-" : (item.db_rows ?? 0).toLocaleString()}</td>
                        <td>{formatSavedAt(item.savedAt)}</td>
                        <td style={{ color: item.error ? "var(--err, #d33)" : "var(--ok, #2a7)" }}>
                          {item.error ? `오류: ${item.error}` : "완료"}
                        </td>
                      </tr>
                    ))
                  : (
                  <tr>
                      <td colSpan={7}>
                      {isLoadingFiles
                        ? "마스터 파일 정보를 불러오는 중입니다..."
                        : isDownloading
                        ? "마스터 파일 다운로드 중입니다..."
                        : "표시할 마스터 파일 정보가 없습니다."}
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
            <div className="stock-master-top-actions">
              <label htmlFor="base-date-input">기준일자</label>
              <input
                id="base-date-input"
                type="date"
                value={baseDateInput}
                onChange={(e) => setBaseDateInput(e.target.value)}
              />
              <button type="button" onClick={handleSearchBaseDate} disabled={isLoadingTable}>
                조회
              </button>
            </div>
            {tableResult ? <p className="ok">{tableResult.message}</p> : null}
            {tableError ? <p className="err">{tableError}</p> : null}
            <table className="basic-table" aria-label={`${tableName} 조회 결과`}>
              <thead>
                <tr>
                  <th scope="col">NO</th>
                  {tableResult && tableResult.columns.length > 0 ? (
                    tableResult.columns.map((column) => (
                      <th key={column} scope="col">{tableResult.columnLabels?.[column] || column}</th>
                    ))
                  ) : (
                    <th scope="col">조회 결과</th>
                  )}
                </tr>
              </thead>
              <tbody>
                {tableResult && tableResult.rows.length > 0 ? (
                  tableResult.rows.map((row, rowIndex) => (
                    <tr key={`${tableName}-row-${rowIndex}`}>
                      <td style={{ textAlign: "right" }}>
                        {(tableResult.page - 1) * tableResult.pageSize + rowIndex + 1}
                      </td>
                      {tableResult.columns.map((column) => (
                        <td key={`${tableName}-${rowIndex}-${column}`}>{row[column] ?? ""}</td>
                      ))}
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={tableResult?.columns.length || 1}>
                      {isLoadingTable ? "테이블 데이터를 불러오는 중입니다..." : "표시할 데이터가 없습니다."}
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
            {!isLoadingTable && tableResult ? (
              <div className="stock-master-top-actions" style={{ marginTop: 12 }}>
                <button
                  type="button"
                  onClick={() => setTablePage((prev) => Math.max(prev - 1, 1))}
                  disabled={tableResult.page <= 1}
                >
                  이전
                </button>
                <span>
                  {tableResult.page} / {tableResult.totalPages} 페이지
                  ({tableResult.totalCount.toLocaleString()}건, 페이지당 {tableResult.pageSize}건)
                </span>
                <button
                  type="button"
                  onClick={() => setTablePage((prev) => Math.min(prev + 1, tableResult.totalPages))}
                  disabled={tableResult.page >= tableResult.totalPages}
                >
                  다음
                </button>
              </div>
            ) : null}
          </>
        )}
      </section>
    </div>
  );
}