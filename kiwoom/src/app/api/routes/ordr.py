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

from typing import Any
from typing import Annotated

from fastapi import APIRouter, Depends, Path
from fastapi import status as http_status
from pydantic import BaseModel, Field, create_model

from ordr.specs import ORDR_API_SPECS
from app.schemas.ordr import (
    ORDER_MUTATION_API_IDS,
    OrdrApiRequest,
    OrdrApiResponse,
    OrdrApiSpecListResponse,
)
from app.services.ordr_service import OrdrService, get_ordr_service

router = APIRouter(prefix="/ordr", tags=["ordr"])

ServiceDep = Annotated[OrdrService, Depends(get_ordr_service)]


def _create_ordr_request_model(api_id: str, spec: dict[str, Any]) -> type[BaseModel]:
    field_defs: dict[str, tuple[Any, Field]] = {}
    for field in spec.get("fields", []) or []:
        name = str(field.get("element", "")).strip()
        if not name:
            continue

        required = bool(field.get("required", False))
        label = str(field.get("label", "")).strip()
        desc = str(field.get("description", "")).strip()
        field_desc = " / ".join(x for x in [label, desc] if x)

        if required:
            field_defs[name] = (str, Field(..., description=field_desc or None))
        else:
            field_defs[name] = (str | None, Field(None, description=field_desc or None))

    model_name = f"OrdrReq_{api_id}"
    return create_model(model_name, __base__=BaseModel, **field_defs)


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


def _make_ordr_spec_handler(api_id: str):
    async def _handler(req: BaseModel, svc: ServiceDep) -> OrdrApiResponse:
        body = req.model_dump(exclude_none=True)
        confirm = api_id in ORDER_MUTATION_API_IDS
        return await svc.call(api_id=api_id, body=body, confirm=confirm)

    _handler.__name__ = f"call_ordr_{api_id}"
    return _handler


for _spec in ORDR_API_SPECS:
    _api_id = str(_spec.get("api_id", "")).strip()
    if not _api_id:
        continue

    _name = str(_spec.get("name", _api_id))
    _overview = str(_spec.get("overview", "")).strip()
    _is_mutation = _api_id in ORDER_MUTATION_API_IDS
    _safety_note = (
        "\n\n주의: 주문 변경 API이므로 요청 바디에 `\"confirm\": true` 가 필요합니다."
        if _is_mutation
        else ""
    )
    _description = (
        (f"{_overview}\n\n" if _overview else "")
        + f"- API ID: `{_api_id}`\n"
        + "- Kiwoom URL: `/api/dostk/ordr`"
        + _safety_note
    )
    _req_model = _create_ordr_request_model(_api_id, _spec)
    _handler = _make_ordr_spec_handler(_api_id)
    _handler.__annotations__["req"] = _req_model

    router.add_api_route(
        f"/{_api_id}",
        _handler,
        methods=["POST"],
        response_model=OrdrApiResponse,
        status_code=http_status.HTTP_200_OK,
        summary=f"{_name} ({_api_id})",
        description=_description,
        operation_id=f"call_ordr_{_api_id}",
        openapi_extra={
            "x-api-id": _api_id,
            "x-kiwoom-url": "/api/dostk/ordr",
        },
    )


@router.post(
    "/{api_id}",
    response_model=OrdrApiResponse,
    status_code=http_status.HTTP_200_OK,
    include_in_schema=False,
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
