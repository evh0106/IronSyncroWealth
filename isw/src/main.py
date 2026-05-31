from __future__ import annotations

import asyncio
from typing import Literal

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from schemas import AccountSummary, MarketQuote, OrderRequest, OrderResponse
from service import service

Broker = Literal["kiwoom", "kis"]

app = FastAPI(title="ISW Backend Skeleton", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
