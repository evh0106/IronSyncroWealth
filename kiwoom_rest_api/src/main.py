"""
키움증권 REST API – 메인 진입점

실행:
    (프로젝트루트)/kiwoom_rest_api/src 경로에서
    python main.py
"""

import sys
from oauth2 import get_access_token, load_api_keys, revoke_access_token
from inds.sector_price import print_sector_price
from volume import (
    print_volume_surge,
    print_today_volume_rank,
    print_prev_volume_rank,
    print_trade_amount_rank,
    print_volume_update,
    print_broker_instant_volume,
    print_today_prev_contracts,
)
from volume._fmt import _ljust

# ─────────────────────────────────────────────
# 메뉴 항목 정의 (카테고리 → 하위 메뉴)
# ─────────────────────────────────────────────
MENU_CATEGORIES = [
    ('1', '업종', [
        ('1', '업종현재가 조회       (ka20001)', print_sector_price),
    ]),
    ('2', '거래량', [
        ('1', '거래량급증 조회       (ka10023)', print_volume_surge),
        ('2', '거래량갱신 조회       (ka10024)', print_volume_update),
        ('3', '당일거래량상위 조회   (ka10030)', print_today_volume_rank),
        ('4', '전일거래량상위 조회   (ka10031)', print_prev_volume_rank),
        ('5', '거래대금상위 조회     (ka10032)', print_trade_amount_rank),
        ('6', '거래원순간거래량 조회 (ka10052)', print_broker_instant_volume),
        ('7', '당일전일체결량 조회   (ka10055)', print_today_prev_contracts),
    ]),
]


def print_main_menu():
    print()
    print('╔══════════════════════════════════════════════╗')
    print('║           키움 REST API 메뉴                 ║')
    print('╠══════════════════════════════════════════════╣')
    for key, label, _ in MENU_CATEGORIES:
        print(f'║  [{key}] {_ljust(label, 40)}║')
    print(f'║  [0] {_ljust("종료", 40)}║')
    print('╚══════════════════════════════════════════════╝')


def print_sub_menu(cat_label, sub_items):
    print()
    print('╔══════════════════════════════════════════════╗')
    print(f'║  ▶ {_ljust(cat_label, 42)}║')
    print('╠══════════════════════════════════════════════╣')
    for key, label, _ in sub_items:
        print(f'║  [{key}] {_ljust(label, 40)}║')
    print(f'║  [0] {_ljust("뒤로", 40)}║')
    print('╚══════════════════════════════════════════════╝')


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
    cat_map = {key: (label, sub_items) for key, label, sub_items in MENU_CATEGORIES}
    try:
        while True:
            print_main_menu()
            choice = input('메뉴 선택: ').strip()

            if choice == '0':
                print('\n프로그램을 종료합니다.')
                break

            if choice not in cat_map:
                print(f'  알 수 없는 메뉴: {choice!r}  (0~{len(MENU_CATEGORIES)} 사이 값을 입력하세요)')
                continue

            cat_label, sub_items = cat_map[choice]
            sub_map = {k: fn for k, _, fn in sub_items}

            # 하위 메뉴 루프
            while True:
                print_sub_menu(cat_label, sub_items)
                sub_choice = input('메뉴 선택: ').strip()

                if sub_choice == '0':
                    break

                fn = sub_map.get(sub_choice)
                if fn is None:
                    print(f'  알 수 없는 메뉴: {sub_choice!r}  (0~{len(sub_items)} 사이 값을 입력하세요)')
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
