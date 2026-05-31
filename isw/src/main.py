from __future__ import annotations

import asyncio
import time
from datetime import datetime, timezone
from typing import Literal

from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import stock_master
from logger import access_logger, error_logger
from schemas import AccountSummary, MarketQuote, OrderRequest, OrderResponse, StockMasterDownloadItem, StockMasterDownloadResponse
from service import service

Broker = Literal["kiwoom", "kis"]

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
