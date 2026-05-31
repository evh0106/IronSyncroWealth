from __future__ import annotations

import asyncio
import time
from datetime import date, datetime, timezone
from typing import Literal

from fastapi import FastAPI, HTTPException, Query, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import stock_master
from logger import access_logger, error_logger, web_error_logger
from schemas import (
    AccountSummary,
    BasicStatusResponse,
    ClientErrorLogRequest,
    MarketQuote,
    OrderRequest,
    OrderResponse,
    StockMasterDownloadItem,
    StockMasterDownloadResponse,
    StockMasterTableResponse,
)
from service import service

Broker = Literal["kiwoom", "kis"]

ALLOWED_STOCK_MASTER_TABLES = {
    "isw_mst_kospi",
    "isw_mst_kosdaq",
    "isw_mst_konex",
    "isw_mst_domestic_elw",
    "isw_mst_domestic_index_future",
    "isw_mst_domestic_stock_future",
    "isw_mst_domestic_cme_future",
    "isw_mst_domestic_commodity_future",
    "isw_mst_domestic_eurex_option",
    "isw_mst_domestic_bond",
    "isw_mst_overseas_stock",
    "isw_mst_overseas_index",
    "isw_mst_overseas_future",
}

app = FastAPI(title="ISW Backend Skeleton", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):  # type: ignore[type-arg]
    start = time.perf_counter()
    body_bytes = await request.body()

    # body를 소비했으므로 스트림을 재설정한다.
    async def receive():
        return {"type": "http.request", "body": body_bytes}

    request._receive = receive  # noqa: SLF001

    response = await call_next(request)
    elapsed_ms = round((time.perf_counter() - start) * 1000, 1)

    body_preview = body_bytes[:200].decode("utf-8", errors="replace") if body_bytes else ""
    access_logger.info(
        "%s %s %s %.1fms req=%s",
        request.method,
        request.url.path,
        response.status_code,
        elapsed_ms,
        body_preview or "-",
    )
    return response


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/v1/client-error-log", response_model=BasicStatusResponse)
def log_client_error(payload: ClientErrorLogRequest, request: Request) -> BasicStatusResponse:
    client_host = request.client.host if request.client else "-"
    web_error_logger.error(
        "client=%s type=%s broker=%s url=%s source=%s line=%s col=%s occurredAt=%s ua=%s msg=%s stack=%s",
        client_host,
        payload.type,
        payload.broker or "-",
        payload.url or "-",
        payload.source or "-",
        payload.line,
        payload.column,
        payload.occurredAt or "-",
        payload.userAgent or "-",
        payload.message,
        payload.stack or "-",
    )
    return BasicStatusResponse(status="ok", message="웹 오류 로그 저장 완료")


@app.get("/api/v1/account/{account_no}/summary", response_model=AccountSummary)
def get_account_summary(account_no: str) -> AccountSummary:
    return service.get_account_summary(account_no)


@app.get("/api/v1/market/{symbol}", response_model=MarketQuote)
def get_market_quote(symbol: str) -> MarketQuote:
    return service.get_market_quote(symbol)


@app.post("/api/v1/order", response_model=OrderResponse)
def submit_order(payload: OrderRequest) -> OrderResponse:
    return service.create_order(payload)


@app.post("/api/v1/stock-master/download-all", response_model=StockMasterDownloadResponse)
async def request_stock_master_download_all() -> StockMasterDownloadResponse:
    requested_at = datetime.now(timezone.utc).isoformat()
    try:
        raw_results = await asyncio.to_thread(stock_master.download_all)
        items = [StockMasterDownloadItem(**r) for r in raw_results]
        has_error = any(item.error for item in items)
        ok_count = sum(1 for item in items if not item.error)

        if has_error:
            failed_markets = [item.market for item in items if item.error]
            error_logger.error(
                "stock-master download partial failure requestedAt=%s failedMarkets=%s",
                requested_at,
                ",".join(failed_markets) or "-",
            )

        return StockMasterDownloadResponse(
            status="partial" if has_error else "ok",
            message=f"{ok_count}/{len(items)}개 시장 마스터 파일 다운로드 완료.",
            requestedAt=requested_at,
            results=items,
        )
    except Exception:
        print(f"[ERROR] stock-master download-all failed requestedAt={requested_at}")
        error_logger.exception("stock-master download-all failed requestedAt=%s", requested_at)
        raise HTTPException(status_code=500, detail="다운로드 요청 중 오류가 발생했습니다.")


@app.get("/api/v1/stock-master/files", response_model=StockMasterDownloadResponse)
def get_stock_master_files() -> StockMasterDownloadResponse:
    requested_at = datetime.now(timezone.utc).isoformat()
    try:
        raw_results = stock_master.get_mst_file_statuses()
        items = [StockMasterDownloadItem(**r) for r in raw_results]
        has_error = any(item.error for item in items)
        ok_count = sum(1 for item in items if not item.error)
        return StockMasterDownloadResponse(
            status="partial" if has_error else "ok",
            message=f"{ok_count}/{len(items)}개 마스터 파일 정보를 불러왔습니다.",
            requestedAt=requested_at,
            results=items,
        )
    except Exception:
        print(f"[ERROR] stock-master files fetch failed requestedAt={requested_at}")
        error_logger.exception("stock-master files fetch failed requestedAt=%s", requested_at)
        raise HTTPException(status_code=500, detail="마스터 파일 정보 조회 중 오류가 발생했습니다.")


@app.get("/api/v1/stock-master/table/{table_name}", response_model=StockMasterTableResponse)
def get_stock_master_table(
    table_name: str,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=50, ge=1, le=2000),
    base_date: str | None = Query(default=None, pattern=r"^\d{8}$"),
) -> StockMasterTableResponse:
    if table_name not in ALLOWED_STOCK_MASTER_TABLES:
        raise HTTPException(status_code=400, detail="허용되지 않은 테이블입니다.")

    try:
        from db import get_conn
    except Exception as exc:
        print(f"[ERROR] stock-master table db init failed table={table_name} err={exc}")
        error_logger.exception("stock-master table db init failed table=%s", table_name)
        raise HTTPException(status_code=500, detail="DB 연결 초기화에 실패했습니다.")

    try:
        conn = get_conn()
        try:
            offset = (page - 1) * limit
            where_clause = " WHERE base_date = %s" if base_date else ""
            where_params: tuple = (base_date,) if base_date else ()
            with conn.cursor() as cur:
                cur.execute(f"SELECT COUNT(*) FROM {table_name}{where_clause}", where_params)
                total_count_row = cur.fetchone()
                total_count = int(total_count_row[0]) if total_count_row else 0

                cur.execute(
                    f"SELECT * FROM {table_name}{where_clause} ORDER BY base_date DESC, short_code ASC LIMIT %s OFFSET %s",
                    (*where_params, limit, offset),
                )
                raw_rows = cur.fetchall()
                columns = [desc[0] for desc in (cur.description or [])]

                cur.execute(
                    """
                    SELECT COLUMN_NAME, COLUMN_COMMENT
                    FROM information_schema.COLUMNS
                    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = %s
                    ORDER BY ORDINAL_POSITION
                    """,
                    (table_name,),
                )
                comment_rows = cur.fetchall()

            column_labels: dict[str, str] = {}
            for col_name, col_comment in comment_rows:
                label = (col_comment or "").strip() if isinstance(col_comment, str) else ""
                column_labels[col_name] = label or col_name

            rows: list[dict[str, str | int | float | None]] = []
            for raw in raw_rows:
                row: dict[str, str | int | float | None] = {}
                for i, column in enumerate(columns):
                    value = raw[i]
                    if value is None or isinstance(value, (str, int, float)):
                        row[column] = value
                    elif isinstance(value, (datetime, date)):
                        row[column] = value.isoformat()
                    elif isinstance(value, (bytes, bytearray)):
                        row[column] = value.decode("utf-8", errors="replace")
                    else:
                        row[column] = str(value)
                rows.append(row)

            return StockMasterTableResponse(
                status="ok",
                message=f"{len(rows)}건 조회되었습니다.",
                tableName=table_name,
                rowCount=len(rows),
                totalCount=total_count,
                page=page,
                pageSize=limit,
                totalPages=((total_count + limit - 1) // limit) if total_count > 0 else 1,
                columns=columns,
                columnLabels=column_labels,
                rows=rows,
            )
        finally:
            conn.close()
    except Exception as exc:
        print(f"[ERROR] stock-master table fetch failed table={table_name} err={exc}")
        error_logger.exception("stock-master table fetch failed table=%s", table_name)
        raise HTTPException(status_code=500, detail="종목 마스터 테이블 조회 중 오류가 발생했습니다.")


@app.websocket("/ws/{broker}/{symbol}")
async def market_realtime_socket(websocket: WebSocket, broker: Broker, symbol: str) -> None:
    await websocket.accept()

    try:
        # broker 값은 현재 스켈레톤 단계에서 검증 목적만 사용한다.
        _ = broker
        while True:
            payload = service.next_realtime(symbol)
            await websocket.send_json(payload.model_dump())
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        return
