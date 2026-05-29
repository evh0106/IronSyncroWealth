"""주문 API 스펙 통합 진입점."""

from .specs_request import ORDR_API_SPECS
from .specs_response import ORDR_RESPONSE_SPECS

__all__ = ['ORDR_API_SPECS', 'ORDR_RESPONSE_SPECS']
