"""계좌 조회 API 라우터 (/api/v1/acnt).

엔드포인트
-----------
GET  /api/v1/acnt/specs          - 지원 계좌 API 스펙 목록 반환
POST /api/v1/acnt/{api_id}       - 지정된 계좌 API 범용 호출
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Path
from fastapi import status as http_status

from acnt.specs import ACCOUNT_API_SPECS
from app.schemas.acnt import (
    AcntApiRequest,
    AcntApiResponse,
    AcntApiSpecListResponse,
)
from app.services.acnt_service import AcntService, get_acnt_service

router = APIRouter(prefix="/acnt", tags=["acnt"])

ServiceDep = Annotated[AcntService, Depends(get_acnt_service)]


@router.get(
    "/specs",
    response_model=AcntApiSpecListResponse,
    summary="계좌 API 스펙 목록",
    description="지원하는 계좌 조회 API 목록과 각 API의 요청 필드 스펙을 반환합니다.",
)
async def list_acnt_specs(svc: ServiceDep) -> AcntApiSpecListResponse:
    specs = svc.list_specs()
    return AcntApiSpecListResponse(total=len(specs), specs=specs)


def _make_acnt_spec_handler(api_id: str):
    async def _handler(req: AcntApiRequest, svc: ServiceDep) -> AcntApiResponse:
        return await svc.call(api_id=api_id, body=req.body)

    _handler.__name__ = f"call_acnt_{api_id}"
    return _handler


for _spec in ACCOUNT_API_SPECS:
    _api_id = str(_spec.get("api_id", "")).strip()
    if not _api_id:
        continue

    _name = str(_spec.get("name", _api_id))
    _overview = str(_spec.get("overview", "")).strip()
    _description = (
        (f"{_overview}\n\n" if _overview else "")
        + f"- API ID: `{_api_id}`\n"
        + "- Kiwoom URL: `/api/dostk/acnt`"
    )

    router.add_api_route(
        f"/{_api_id}",
        _make_acnt_spec_handler(_api_id),
        methods=["POST"],
        response_model=AcntApiResponse,
        status_code=http_status.HTTP_200_OK,
        summary=f"{_name} ({_api_id})",
        description=_description,
        operation_id=f"call_acnt_{_api_id}",
        openapi_extra={
            "x-api-id": _api_id,
            "x-kiwoom-url": "/api/dostk/acnt",
        },
    )


@router.post(
    "/{api_id}",
    response_model=AcntApiResponse,
    status_code=http_status.HTTP_200_OK,
    include_in_schema=False,
    summary="계좌 API 범용 호출",
    description=(
        "``api_id`` 에 해당하는 계좌 조회 API를 호출합니다.  \n"
        "유효한 api_id 목록은 `GET /api/v1/acnt/specs` 에서 확인하세요."
    ),
)
async def call_acnt_api(
    api_id: Annotated[str, Path(description="계좌 API 식별자 (예: ka00001, kt00001)")],
    req: AcntApiRequest,
    svc: ServiceDep,
) -> AcntApiResponse:
    return await svc.call(
        api_id=api_id,
        body=req.body,
    )
