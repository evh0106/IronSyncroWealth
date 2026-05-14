"""업종 조회 API 라우터 (국내주식 > 업종)."""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from app.schemas.sect import SectCurrentPriceResponse
from app.services.sect_service import SectService, get_sect_service

router = APIRouter(prefix="/sect", tags=["업종"])


@router.get(
    "/current-price",
    response_model=SectCurrentPriceResponse,
    summary="업종현재가요청 (ka20001)",
    description=(
        "업종코드별 현재가·전일대비·등락률 등을 조회합니다.\n\n"
        "- 유효한 액세스 토큰이 DB에 캐시되어 있어야 합니다.\n"
        "- 토큰 미존재 시 먼저 `POST /api/v1/auth/token` 을 호출하세요."
    ),
)
async def get_current_price(
    mrkt_tp: str = Query("0", description="시장구분: 0=코스피, 1=코스닥, 2=코스피200"),
    sect_cd: str = Query(
        "001",
        description=(
            "업종코드: 001=종합(KOSPI), 002=대형주, 003=중형주, 004=소형주, "
            "101=종합(KOSDAQ), 201=KOSPI200, 302=KOSTAR, 701=KRX100"
        ),
    ),
    service: SectService = Depends(get_sect_service),
) -> SectCurrentPriceResponse:
    return await service.get_current_price(
        mrkt_tp=mrkt_tp,
        sect_cd=sect_cd,
    )
