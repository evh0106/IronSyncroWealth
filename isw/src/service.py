from __future__ import annotations

import random
import uuid
from dataclasses import dataclass

from schemas import AccountSummary, MarketQuote, OrderRequest, OrderResponse, RealtimePayload


@dataclass
class QuoteState:
    price: float
    change_rate: float
    volume: int


class MockTradingService:
    def __init__(self) -> None:
        self._quotes: dict[str, QuoteState] = {
            "005930": QuoteState(price=84200.0, change_rate=1.21, volume=3_821_403),
            "000660": QuoteState(price=214500.0, change_rate=-0.37, volume=2_042_113),
            "035420": QuoteState(price=182700.0, change_rate=0.84, volume=711_299),
        }

    def get_account_summary(self, account_no: str) -> AccountSummary:
        account_seed = sum(ord(ch) for ch in account_no) if account_no else 0
        balance = 10_000_000 + (account_seed % 1_000_000)
        pnl_rate = round(((account_seed % 500) - 250) / 100, 2)
        return AccountSummary(accountNo=account_no, balance=balance, pnlRate=pnl_rate)

    def get_market_quote(self, symbol: str) -> MarketQuote:
        state = self._quotes.get(symbol)
        if not state:
            state = QuoteState(price=50000.0, change_rate=0.0, volume=100_000)
            self._quotes[symbol] = state
        return MarketQuote(
            symbol=symbol,
            price=round(state.price, 2),
            changeRate=round(state.change_rate, 2),
            volume=state.volume,
        )

    def create_order(self, payload: OrderRequest) -> OrderResponse:
        return OrderResponse(orderId=str(uuid.uuid4()), status="accepted")

    def next_realtime(self, symbol: str) -> RealtimePayload:
        state = self._quotes.get(symbol)
        if not state:
            state = QuoteState(price=50000.0, change_rate=0.0, volume=100_000)
            self._quotes[symbol] = state

        move = random.uniform(-80, 80)
        new_price = max(100.0, state.price + move)
        state.change_rate = ((new_price - state.price) / state.price) * 100 if state.price else 0.0
        state.price = new_price
        state.volume += random.randint(100, 5_000)

        return RealtimePayload(price=round(state.price, 2), volume=state.volume)


service = MockTradingService()
