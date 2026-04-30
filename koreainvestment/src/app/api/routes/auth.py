"""Authentication and token management endpoints."""

from fastapi import APIRouter, Depends

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


@router.get("/token", response_model=TokenStatusResponse)
def get_token_status(
    server_mode: str = "real",
    service: TokenService = Depends(get_token_service),
) -> TokenStatusResponse:
    return service.get_cached_token_status(server_mode=server_mode)


@router.post("/token", response_model=TokenIssueResponse)
def issue_token(
    request: TokenIssueRequest,
    service: TokenService = Depends(get_token_service),
) -> TokenIssueResponse:
    return service.issue_token(
        server_mode=request.server_mode,
        reuse_cached=request.reuse_cached,
    )


@router.post("/token/revoke", response_model=TokenRevokeResponse)
def revoke_token(
    request: TokenRevokeRequest,
    service: TokenService = Depends(get_token_service),
) -> TokenRevokeResponse:
    return service.revoke_token(
        server_mode=request.server_mode,
        token=request.token,
    )


@router.post("/approval", response_model=ApprovalIssueResponse)
def issue_approval(
    request: ApprovalIssueRequest,
    service: TokenService = Depends(get_token_service),
) -> ApprovalIssueResponse:
    return service.issue_approval_key(server_mode=request.server_mode)