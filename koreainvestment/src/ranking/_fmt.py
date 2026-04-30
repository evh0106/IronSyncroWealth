"""전각 문자 폭을 고려한 정렬 유틸리티."""

from __future__ import annotations

import unicodedata


def _wcslen(s: str) -> int:
    total = 0
    for c in str(s):
        total += 2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
    return total


def _ljust(s: str, width: int) -> str:
    s = str(s)
    total = 0
    out: list[str] = []
    for c in s:
        cw = 2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
        if total + cw > width:
            if width - total > 0:
                out.append(" " * (width - total))
            break
        out.append(c)
        total += cw
    else:
        out.append(" " * (width - total))
    return "".join(out)


def _rjust(s: str, width: int) -> str:
    s = str(s)
    return " " * max(width - _wcslen(s), 0) + s
