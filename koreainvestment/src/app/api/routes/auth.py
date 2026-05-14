"""Authentication and token management endpoints."""

from fastapi import APIRouter, Body, Depends

from app.schemas.auth import (
    ApprovalIssueRequest,
    ApprovalIssueResponse,
    TokenIssueRequest,
    TokenIssueResponse,
    TokenRevokeRequest,
    TokenRevokeResponse,
    TokenStatusResponse,
)
from app.services.token_service import TokenService, get_token_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/token", response_model=TokenStatusResponse, summary="캐시 토큰 상태 조회")
def get_token_status(
    server_mode: str = "real",
    service: TokenService = Depends(get_token_service),
) -> TokenStatusResponse:
    return service.get_cached_token_status(server_mode=server_mode)


@router.post("/token", response_model=TokenIssueResponse, summary="access token issue [ka10001]")
def issue_token(
    request: TokenIssueRequest,
    service: TokenService = Depends(get_token_service),
) -> TokenIssueResponse:
    return service.issue_token(
        server_mode=request.server_mode,
        reuse_cached=request.reuse_cached,
    )


@router.post("/token/revoke", response_model=TokenRevokeResponse, summary="access token revoke [ka10002]")
def revoke_token(
    request: TokenRevokeRequest | None = Body(default=None),
    service: TokenService = Depends(get_token_service),
) -> TokenRevokeResponse:
    request_data = request or TokenRevokeRequest()
    return service.revoke_token(
        server_mode=request_data.server_mode,
        token=request_data.token,
    )


@router.post("/approval", response_model=ApprovalIssueResponse, summary="websocket approval key issue [ka10003]")
def issue_approval(
    request: ApprovalIssueRequest,
    service: TokenService = Depends(get_token_service),
) -> ApprovalIssueResponse:
    return service.issue_approval_key(server_mode=request.server_mode)