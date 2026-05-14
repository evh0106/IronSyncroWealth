"""WebSocket 세션 제어 라우터 (/api/v1/ws).

엔드포인트
-----------
GET    /api/v1/ws/types           - 지원 실시간 타입 목록
GET    /api/v1/ws/status          - 현재 세션 상태 조회
POST   /api/v1/ws/start           - 백그라운드 세션 시작
POST   /api/v1/ws/stop            - 백그라운드 세션 중지
POST   /api/v1/ws/register        - 실행 중인 세션에 실시간 항목 추가
DELETE /api/v1/ws/register        - 실행 중인 세션에서 실시간 항목 해제
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from app.schemas.ws import (
    ACCOUNT_TYPES,
    REALTIME_TYPE_MAP,
    WsOperationResult,
    WsRegisterRequest,
    WsSessionStatus,
    WsStartRequest,
    WsTypeInfo,
    WsTypeListResponse,
)
from app.services.ws_manager import WsSessionManager, get_ws_manager

router = APIRouter(prefix="/ws", tags=["ws"])

ManagerDep = Annotated[WsSessionManager, Depends(get_ws_manager)]


@router.get(
    "/types",
    response_model=WsTypeListResponse,
    summary="실시간 타입 목록",
    description="등록 가능한 모든 실시간 항목 코드와 이름을 반환합니다.",
)
def list_realtime_types() -> WsTypeListResponse:
    types = [
        WsTypeInfo(
            code=code,
            name=name,
            needs_item=(code not in ACCOUNT_TYPES),
        )
        for code, name in REALTIME_TYPE_MAP.items()
    ]
    return WsTypeListResponse(total=len(types), types=types)


@router.get(
    "/status",
    response_model=WsSessionStatus,
    summary="WebSocket 세션 상태 조회",
    description="현재 백그라운드 WebSocket 세션의 실행 여부와 등록 항목을 반환합니다.",
)
def get_ws_status(mgr: ManagerDep) -> WsSessionStatus:
    return mgr.status()


@router.post(
    "/start",
    response_model=WsOperationResult,
    summary="WebSocket 세션 시작",
    description=(
        "백그라운드 WebSocket 세션을 시작합니다.  \n"
        "이미 실행 중인 경우 409를 반환합니다.  \n"
        "등록 가능한 타입 코드는 `GET /api/v1/ws/types` 에서 확인하세요."
    ),
)
def start_ws_session(req: WsStartRequest, mgr: ManagerDep) -> WsOperationResult:
    resolved_server_mode = mgr.start(
        items=req.items,
        types=req.types,
        group_no=req.group_no,
    )
    return WsOperationResult(
        success=True,
        message="WebSocket background session started.",
        detail={
            "server_mode": resolved_server_mode,
            "items": req.items,
            "types": req.types,
            "group_no": req.group_no,
        },
    )


@router.post(
    "/stop",
    response_model=WsOperationResult,
    summary="WebSocket 세션 중지",
    description=(
        "실행 중인 백그라운드 WebSocket 세션을 안전하게 종료합니다.  \n"
        "실행 중인 세션이 없으면 409를 반환합니다."
    ),
)
def stop_ws_session(mgr: ManagerDep) -> WsOperationResult:
    mgr.stop()
    return WsOperationResult(
        success=True,
        message="WebSocket background session stopped.",
    )


@router.post(
    "/register",
    response_model=WsOperationResult,
    summary="실시간 항목 추가 등록",
    description=(
        "실행 중인 세션에 실시간 항목을 추가합니다 (trnm=REG, refresh=1).  \n"
        "세션이 실행 중이 아니면 409를 반환합니다."
    ),
)
def register_realtime(req: WsRegisterRequest, mgr: ManagerDep) -> WsOperationResult:
    mgr.add_items(items=req.items, types=req.types, group_no=req.group_no)
    return WsOperationResult(
        success=True,
        message="Realtime items registered.",
        detail={"items": req.items, "types": req.types, "group_no": req.group_no},
    )


@router.delete(
    "/register",
    response_model=WsOperationResult,
    summary="실시간 항목 해제",
    description=(
        "실행 중인 세션에서 실시간 항목을 해제합니다 (trnm=REMOVE).  \n"
        "세션이 실행 중이 아니면 409를 반환합니다."
    ),
)
def remove_realtime(req: WsRegisterRequest, mgr: ManagerDep) -> WsOperationResult:
    mgr.remove_items(items=req.items, types=req.types, group_no=req.group_no)
    return WsOperationResult(
        success=True,
        message="Realtime items removed.",
        detail={"items": req.items, "types": req.types, "group_no": req.group_no},
    )
