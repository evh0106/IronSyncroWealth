"""Authentication and token management endpoints."""

from fastapi import APIRouter, Depends

from app.schemas.auth import (
    Au10001Request,
    Au10002Request,
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


@router.post(
    "/au10001",
    response_model=TokenIssueResponse,
    summary="접근토큰 발급 (au10001)",
    description="Kiwoom OAuth2 접근토큰 발급 API 별칭 엔드포인트",
    openapi_extra={"x-api-id": "au10001", "x-kiwoom-url": "/oauth2/token"},
)
def issue_token_au10001(
    request: Au10001Request,
    service: TokenService = Depends(get_token_service),
) -> TokenIssueResponse:
    _ = request
    return service.issue_token(
        server_mode="real",
        reuse_cached=False,
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


@router.post(
    "/au10002",
    response_model=TokenRevokeResponse,
    summary="접근토큰 폐기 (au10002)",
    description="Kiwoom OAuth2 접근토큰 폐기 API 별칭 엔드포인트",
    openapi_extra={"x-api-id": "au10002", "x-kiwoom-url": "/oauth2/revoke"},
)
def revoke_token_au10002(
    request: Au10002Request,
    service: TokenService = Depends(get_token_service),
) -> TokenRevokeResponse:
    _ = (request.appkey, request.secretkey)
    return service.revoke_token(
        server_mode="real",
        token=request.token,
    )
