"""전각 문자(한글 등) 폭을 고려한 문자열 정렬 유틸리티"""
import unicodedata


def _wcslen(s: str) -> int:
    """문자열의 화면 표시 너비 반환 (한글 등 전각=2, 반각=1)"""
    total = 0
    for c in str(s):
        eaw = unicodedata.east_asian_width(c)
        total += 2 if eaw in ('W', 'F') else 1
    return total


def _ljust(s: str, width: int) -> str:
    """전각 문자를 고려한 왼쪽 정렬 – 넘칠 경우 width에서 잘라냄"""
    s = str(s)
    total = 0
    result = []
    for c in s:
        cw = 2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1
        if total + cw > width:
            # 더블와이드 문자가 딱 안 들어가면 공백으로 채움
            if width - total > 0:
                result.append(' ' * (width - total))
            break
        result.append(c)
        total += cw
    else:
        result.append(' ' * (width - total))
    return ''.join(result)


def _rjust(s: str, width: int) -> str:
    """전각 문자를 고려한 오른쪽 정렬 (왼쪽 공백 패딩)"""
    s = str(s)
    return ' ' * max(width - _wcslen(s), 0) + s
