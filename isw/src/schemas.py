from pydantic import BaseModel, Field


class AccountSummary(BaseModel):
    accountNo: str
    balance: float
    pnlRate: float


class MarketQuote(BaseModel):
    symbol: str
    price: float
    changeRate: float
    volume: int


class OrderRequest(BaseModel):
    accountNo: str = Field(min_length=1)
    symbol: str = Field(min_length=1)
    side: str = Field(pattern="^(buy|sell)$")
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)


class OrderResponse(BaseModel):
    orderId: str
    status: str


class RealtimePayload(BaseModel):
    price: float
    volume: int
