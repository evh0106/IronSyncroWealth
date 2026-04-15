"""
키움증권 REST API – 메인 진입점

실행:
    (프로젝트루트)/kiwoom_rest_api/src 경로에서
    python main.py
"""

import sys
from oauth2 import get_access_token, load_api_keys, revoke_access_token
from inds.sector_price import print_sector_price

# ─────────────────────────────────────────────
# 메뉴 항목 정의
# ─────────────────────────────────────────────
MENU_ITEMS = [
    ('1', '업종현재가 조회 (ka20001)', print_sector_price),
]


def print_menu():
    print()
    print('╔══════════════════════════════════════╗')
    print('║        키움 REST API 메뉴             ║')
    print('╠══════════════════════════════════════╣')
    for key, label, _ in MENU_ITEMS:
        print(f'║  [{key}] {label:<31}║')
    print('║  [0] 종료                            ║')
    print('╚══════════════════════════════════════╝')


def main():
    print('\n키움증권 REST API 프로그램을 시작합니다.')

    # 토큰 발급
    try:
        app_key, app_secret = load_api_keys()
        token = get_access_token(app_key, app_secret)
    except FileNotFoundError as e:
        print(f'\n[오류] API 키 파일을 찾을 수 없습니다.\n  {e}')
        sys.exit(1)
    except Exception as e:
        print(f'\n[오류] 토큰 발급 실패: {e}')
        sys.exit(1)

    # 메뉴 루프
    menu_map = {key: fn for key, _, fn in MENU_ITEMS}
    try:
        while True:
            print_menu()
            choice = input('메뉴 선택: ').strip()

            if choice == '0':
                print('\n프로그램을 종료합니다.')
                break

            fn = menu_map.get(choice)
            if fn is None:
                print(f'  알 수 없는 메뉴: {choice!r}  (0~{len(MENU_ITEMS)} 사이 값을 입력하세요)')
                continue

            try:
                fn(token)
            except Exception as e:
                print(f'\n[오류] 기능 실행 중 문제가 발생했습니다: {e}')

    finally:
        # 토큰 폐기
        try:
            revoke_access_token(app_key, app_secret, token)
        except Exception:
            pass


if __name__ == '__main__':
    main()
