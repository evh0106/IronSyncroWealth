from __future__ import annotations

import inspect
from typing import Any
from typing import Annotated

from fastapi import APIRouter, Body, Depends, Query
from pydantic import BaseModel, Field, create_model

from app.services.kiwoom_raw_service import (
    KiwoomRawApiSpec,
    KiwoomRawService,
    get_kiwoom_raw_service,
)

router = APIRouter(prefix="/kiwoom-missing", tags=["kiwoom-missing"])


class KiwoomMissingSpecResponse(BaseModel):
    total: int
    api_ids: list[str]


class KiwoomMissingCallResponse(BaseModel):
    server_mode: str
    api_id: str
    url_path: str
    data: dict[str, Any]


ServiceDep = Annotated[KiwoomRawService, Depends(get_kiwoom_raw_service)]


@router.get(
    "/specs",
    response_model=KiwoomMissingSpecResponse,
    summary="Swagger 누락 API 목록",
    description="문서 대비 Swagger UI 누락 항목을 기반으로 자동 등록된 API ID 목록을 반환합니다.",
)
def list_missing_specs(svc: ServiceDep) -> KiwoomMissingSpecResponse:
    specs = svc.list_specs()
    return KiwoomMissingSpecResponse(
        total=len(specs),
        api_ids=[s.api_id for s in specs],
    )


def _make_handler(api_id: str, use_query_params: bool):
    async def _handler(**kwargs: Any) -> KiwoomMissingCallResponse:
        svc: KiwoomRawService = kwargs.pop("svc")
        if use_query_params:
            body = {k: v for k, v in kwargs.items() if v is not None}
        else:
            body_model = kwargs.get("body")
            if isinstance(body_model, BaseModel):
                body = body_model.model_dump(exclude_none=True)
            else:
                body = {}

        payload = await svc.call(api_id=api_id, body=body)
        return KiwoomMissingCallResponse(**payload)

    _handler.__name__ = f"call_kiwoom_missing_{api_id}"
    return _handler


def _build_request_model(spec: KiwoomRawApiSpec) -> type[BaseModel]:
    fields: dict[str, tuple[Any, Field]] = {}
    for f in spec.request_fields:
        py_type: Any = list[dict[str, Any]] if f.kind == "list" else str
        if f.required:
            fields[f.name] = (py_type, Field(..., description=f.description or None))
        else:
            fields[f.name] = (py_type | None, Field(None, description=f.description or None))

    if not fields:
        # Keep schema visible even when docs have no request body fields.
        fields["body"] = (
            dict[str, Any] | None,
            Field(None, description="요청 본문 JSON 객체"),
        )

    return create_model(f"KiwoomMissingReq_{spec.api_id}", __base__=BaseModel, **fields)


def _build_handler_signature(spec: KiwoomRawApiSpec) -> tuple[inspect.Signature, bool]:
    has_list_field = any(f.kind == "list" for f in spec.request_fields)
    use_query_params = bool(spec.request_fields) and not has_list_field

    parameters: list[inspect.Parameter] = []

    if use_query_params:
        for f in spec.request_fields:
            parameters.append(
                inspect.Parameter(
                    f.name,
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    annotation=str if f.required else (str | None),
                    default=Query(
                        ... if f.required else None,
                        description=f.description or None,
                    ),
                )
            )
    else:
        req_model = _build_request_model(spec)
        parameters.append(
            inspect.Parameter(
                "body",
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                annotation=Annotated[
                    req_model,
                    Body(description="API 요청 파라미터"),
                ],
            )
        )

    parameters.append(
        inspect.Parameter(
            "svc",
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            annotation=KiwoomRawService,
            default=Depends(get_kiwoom_raw_service),
        )
    )
    return inspect.Signature(parameters=parameters), use_query_params


def _register_routes() -> None:
    svc = get_kiwoom_raw_service()
    specs: list[KiwoomRawApiSpec] = svc.list_specs()
    for spec in specs:
        signature, use_query_params = _build_handler_signature(spec)
        handler = _make_handler(spec.api_id, use_query_params=use_query_params)
        handler.__signature__ = signature
        description = (
            f"- API ID: `{spec.api_id}`\n"
            f"- API 명: {spec.name}\n"
            f"- Kiwoom URL: `{spec.url_path}`\n"
            f"- 문서: `docs/키움 REST API 문서/{spec.doc_rel_path}`"
        )

        router.add_api_route(
            f"/{spec.api_id}",
            handler,
            methods=["POST"],
            response_model=KiwoomMissingCallResponse,
            summary=f"{spec.name} ({spec.api_id})",
            description=description,
            operation_id=f"call_kiwoom_missing_{spec.api_id}",
            openapi_extra={
                "x-api-id": spec.api_id,
                "x-kiwoom-url": spec.url_path,
            },
        )


_register_routes()
