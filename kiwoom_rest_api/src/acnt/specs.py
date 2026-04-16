"""계좌 API 스펙 통합 진입점 (하위 호환성 유지)."""

from .specs_request import ACCOUNT_API_SPECS
from .specs_response import ACCOUNT_RESPONSE_SPECS

__all__ = ['ACCOUNT_API_SPECS', 'ACCOUNT_RESPONSE_SPECS']
