"""
한국투자증권 REST API - 메인 진입점

실행:
    (프로젝트루트)/koreainvestment 경로에서
    scripts\run_main.bat
또는
    (프로젝트루트)/koreainvestment/src 경로에서
    python main.py
"""

from __future__ import annotations

import sys

from kis_auth import issue_access_token, issue_access_token_revoke, issue_ws_approval_key
from kis_config import load_config
from quotations import run_quotations_menu
from ranking import run_ranking_menu
from trading import run_trading_menu


MENU_ITEMS = [
    ("1", "접근토큰 발급 (/oauth2/tokenP)"),
    ("2", "웹소켓 접속키 발급 (/oauth2/Approval)"),
    ("3", "국내주식 ranking 조회 (/uapi/domestic-stock/v1/ranking/*)"),
    ("4", "국내주식 quotations 조회 (/uapi/domestic-stock/v1/quotations/*)"),
    ("5", "국내주식 trading 조회 (/uapi/domestic-stock/v1/trading/*)"),
    ("6", "접근토큰 폐기 (/oauth2/revokeP)"),
]


def _ljust(text: str, width: int) -> str:
    # 한글 출력 폭 차이를 완벽히 맞추지는 않지만, 기본 콘솔 정렬용으로 충분합니다.
    return f"{text:<{width}}"


def print_main_menu() -> None:
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║          한국투자증권 REST API 메뉴                 ║")
    print("╠══════════════════════════════════════════════════════╣")
    for key, label in MENU_ITEMS:
        print(f"║  [{key}] {_ljust(label, 46)}║")
    print(f"║  [0] {_ljust('종료', 46)}║")
    print("╚══════════════════════════════════════════════════════╝")


def _print_env_info() -> None:
    cfg = load_config()
    env_dv = cfg.get("env_dv", "real")
    base_url = cfg["my_url_vts"] if env_dv == "demo" else cfg["my_url"]
    print("\n한국투자증권 REST API 프로그램을 시작합니다.")
    print(f"현재 서버 모드: {env_dv} ({base_url})")


def _print_token_summary(access: dict) -> None:
    access_token = access.get("access_token")
    print("\n[ACCESS TOKEN]")
    print(f"token_type: {access.get('token_type')}")
    print(f"expires_at: {access.get('access_token_token_expired')}")
    print(f"has_access_token: {bool(access_token)}")


def _print_approval_summary(approval: dict) -> None:
    print("\n[WS APPROVAL]")
    print(f"approval_key: {approval.get('approval_key')}")
    print(f"message: {approval.get('message') or approval.get('msg1')}")


def _print_revoke_summary(revoke: dict) -> None:
    print("\n[TOKEN REVOKE]")
    print(f"code: {revoke.get('code')}")
    print(f"message: {revoke.get('message')}")



def main() -> None:
    try:
        _print_env_info()
    except (FileNotFoundError, ValueError) as exc:
        print(f"\n[오류] 설정 로드 실패: {exc}")
        sys.exit(1)

    current_access_token = ""
    try:
        while True:
            print_main_menu()
            choice = input("메뉴 선택: ").strip()

            if choice == "0":
                print("\n프로그램을 종료합니다.")
                break

            if choice == "1":
                try:
                    access = issue_access_token()
                except Exception as exc:
                    print(f"\n[오류] 토큰 발급 실패: {exc}")
                    continue

                _print_token_summary(access)
                current_access_token = access.get("access_token") or current_access_token
                continue

            if choice == "2":
                try:
                    approval = issue_ws_approval_key()
                except Exception as exc:
                    print(f"\n[오류] 웹소켓 접속키 발급 실패: {exc}")
                    continue

                _print_approval_summary(approval)
                continue

            if choice == "3":
                if not current_access_token:
                    print("\n[안내] ranking 조회를 위해 접근토큰 발급 여부 확인 중...")
                    try:
                        access = issue_access_token()
                    except Exception as exc:
                        print(f"\n[오류] 토큰 발급 실패: {exc}")
                        continue
                    _print_token_summary(access)
                    current_access_token = access.get("access_token") or ""

                if not current_access_token:
                    print("\n[오류] 유효한 접근토큰이 없어 ranking 메뉴를 실행할 수 없습니다.")
                    continue

                run_ranking_menu(current_access_token)
                continue

            if choice == "4":
                if not current_access_token:
                    print("\n[안내] quotations 조회를 위해 접근토큰 발급 여부 확인 중...")
                    try:
                        access = issue_access_token()
                    except Exception as exc:
                        print(f"\n[오류] 토큰 발급 실패: {exc}")
                        continue
                    _print_token_summary(access)
                    current_access_token = access.get("access_token") or ""

                if not current_access_token:
                    print("\n[오류] 유효한 접근토큰이 없어 quotations 메뉴를 실행할 수 없습니다.")
                    continue

                run_quotations_menu(current_access_token)
                continue

            if choice == "5":
                if not current_access_token:
                    print("\n[안내] trading 조회를 위해 접근토큰 발급 여부 확인 중...")
                    try:
                        access = issue_access_token()
                    except Exception as exc:
                        print(f"\n[오류] 토큰 발급 실패: {exc}")
                        continue
                    _print_token_summary(access)
                    current_access_token = access.get("access_token") or ""

                if not current_access_token:
                    print("\n[오류] 유효한 접근토큰이 없어 trading 메뉴를 실행할 수 없습니다.")
                    continue

                run_trading_menu(current_access_token)
                continue

            if choice == "6":
                token = input("폐기할 access_token 입력 (엔터 시 최근 발급 토큰 사용): ").strip()
                if not token:
                    token = current_access_token

                if not token:
                    print("\n[안내] 폐기할 토큰이 없습니다. 먼저 [1]에서 토큰을 발급하세요.")
                    continue

                try:
                    revoke = issue_access_token_revoke(token)
                except Exception as exc:
                    print(f"\n[오류] 토큰 폐기 실패: {exc}")
                    continue

                _print_revoke_summary(revoke)
                if token == current_access_token:
                    current_access_token = ""
                continue

            print(f"  알 수 없는 메뉴: {choice!r}  (0~{len(MENU_ITEMS)} 사이 값을 입력하세요)")
    finally:
        pass


if __name__ == "__main__":
    main()
