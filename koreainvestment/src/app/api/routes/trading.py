"""Trading endpoints."""

from fastapi import APIRouter, Depends

from app.schemas.common import ApiCallRequest, ApiCallResponse, ApiSpecSummary
from app.services.market_service import MarketApiService, get_trading_service
from app.api.routes._spec_router import register_spec_routes
from trading.specs_request import TRADING_API_SPECS

router = APIRouter(prefix="/trading", tags=["trading"])


@router.get("/specs", response_model=list[ApiSpecSummary], summary="스펙 목록 조회")
def list_specs(service: MarketApiService = Depends(get_trading_service)) -> list[ApiSpecSummary]:
    return service.list_specs()


# Swagger UI에 모든 스펙 URL을 개별 엔드포인트로 노출
register_spec_routes(
    router=router,
    specs=TRADING_API_SPECS,
    marker="/trading/",
    service_dep=get_trading_service,
    tags=["trading"],
)