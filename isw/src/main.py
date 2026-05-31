from __future__ import annotations

import asyncio
import time
from typing import Literal

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from logger import access_logger
from schemas import AccountSummary, MarketQuote, OrderRequest, OrderResponse, StockMasterDownloadResponse
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
def request_stock_master_download_all() -> StockMasterDownloadResponse:
    return service.request_stock_master_download_all()


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
