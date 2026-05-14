"""주문 API 라우터 (/api/v1/ordr).

엔드포인트
-----------
GET  /api/v1/ordr/specs          - 지원 주문 API 스펙 목록 반환
POST /api/v1/ordr/{api_id}       - 지정된 주문 API 범용 호출

주의
----
주문 변경 API (kt10000/kt10001/kt10002/kt10003/kt50000~kt50003) 호출 시
요청 바디에 ``"confirm": true`` 를 반드시 포함해야 합니다.
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Path
from fastapi import status as http_status

from app.schemas.ordr import (
    OrdrApiRequest,
    OrdrApiResponse,
    OrdrApiSpecListResponse,
)
from app.services.ordr_service import OrdrService, get_ordr_service

router = APIRouter(prefix="/ordr", tags=["ordr"])

ServiceDep = Annotated[OrdrService, Depends(get_ordr_service)]


@router.get(
    "/specs",
    response_model=OrdrApiSpecListResponse,
    summary="주문 API 스펙 목록",
    description=(
        "지원하는 주문 API 목록과 각 API의 요청 필드 스펙을 반환합니다.  \n"
        "`is_mutation=true` 인 항목이 실제 주문 발생 API (매수/매도/정정/취소) 입니다."
    ),
)
async def list_ordr_specs(svc: ServiceDep) -> OrdrApiSpecListResponse:
    specs = svc.list_specs()
    return OrdrApiSpecListResponse(total=len(specs), specs=specs)


@router.post(
    "/{api_id}",
    response_model=OrdrApiResponse,
    status_code=http_status.HTTP_200_OK,
    summary="주문 API 범용 호출",
    description=(
        "``api_id`` 에 해당하는 주문 API를 호출합니다.  \n"
        "유효한 api_id 목록은 `GET /api/v1/ordr/specs` 에서 확인하세요.  \n\n"
        "**주문 변경 API** (is_mutation=true) 호출 시 요청 바디에 `\"confirm\": true` 필수."
    ),
)
async def call_ordr_api(
    api_id: Annotated[str, Path(description="주문 API 식별자 (예: kt10000, kt10001)")],
    req: OrdrApiRequest,
    svc: ServiceDep,
) -> OrdrApiResponse:
    return await svc.call(
        api_id=api_id,
        body=req.body,
        confirm=req.confirm,
    )
