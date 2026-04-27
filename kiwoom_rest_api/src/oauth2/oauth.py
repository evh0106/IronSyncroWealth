"""
OAuth2 응답 데이터 DB 저장 모듈

OAuth2 API 응답 결과 (토큰 발급/폐기)를 데이터베이스에 저장합니다.
"""

import db


def get_unrevoked_token(app_key: str) -> str | None:
    """DB에서 app_key 기준으로 가장 최근의 미폐기 토큰을 반환합니다."""
    conn = None
    try:
        conn = db.get_connection()

        with conn.cursor() as cur:
            sql = """
                SELECT t1.token
                FROM au10001 t1
                LEFT JOIN au10002 t2
                  ON t2.req_appkey = t1.req_appkey
                 AND t2.req_token = t1.token
                 AND t2.return_code = '0'
                WHERE t1.req_appkey = %s
                  AND t1.return_code = '0'
                  AND t1.token <> ''
                  AND t2.id IS NULL
                ORDER BY t1.id DESC
                LIMIT 1
            """
            cur.execute(sql, (app_key,))
            row = cur.fetchone()

        if not row:
            print('  [DB 조회] 미폐기 토큰이 DB에 존재하지 않습니다.')
            return None
        
        print('  [DB 조회] 미폐기 토큰이 DB에서 발견되었습니다.')

        return row.get('token')

    except Exception as exc:
        print(f'  [DB 조회 오류] 미폐기 토큰 조회 실패: {exc}')
        return None

    finally:
        if conn is not None:
            conn.close()


def save_au10001_response(app_key: str, grant_type: str, response: dict) -> bool:
    """
    au10001 (액세스 토큰 발급) 응답을 DB에 저장합니다.
    
    Parameters
    ----------
    app_key : str
        발급 요청에 사용된 앱키
    grant_type : str
        요청에 사용된 grant_type
    response : dict
        OAuth2 응답 JSON
        
    Returns
    -------
    bool
        저장 성공 여부
    """
    try:
        conn = db.get_connection()
        
        with conn.cursor() as cur:
            sql = """
                INSERT INTO au10001 
                (grant_type, req_appkey, expires_dt, token_type, token, return_code, return_msg)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s)
            """
            
            params = (
                grant_type,
                app_key,
                response.get('expires_dt', ''),
                response.get('token_type', ''),
                response.get('token', ''),
                response.get('return_code', ''),
                response.get('return_msg', ''),
            )
            
            cur.execute(sql, params)
        
        conn.commit()
        print(f'  [DB 저장] au10001: 1행 저장됨')
        return True
    
    except Exception as exc:
        print(f'  [DB 저장 오류] au10001: {exc}')
        conn.rollback()
        return False
    
    finally:
        conn.close()


def save_au10002_response(app_key: str, token: str, response: dict) -> bool:
    """
    au10002 (액세스 토큰 폐기) 응답을 DB에 저장합니다.
    
    Parameters
    ----------
    app_key : str
        폐기 요청에 사용된 앱키
    token : str
        폐기 요청에 사용된 토큰
    response : dict
        OAuth2 응답 JSON
        
    Returns
    -------
    bool
        저장 성공 여부
    """
    try:
        conn = db.get_connection()
        
        with conn.cursor() as cur:
            sql = """
                INSERT INTO au10002
                (req_appkey, req_token, return_code, return_msg)
                VALUES
                (%s, %s, %s, %s)
            """
            
            params = (
                app_key,
                token,
                response.get('return_code', ''),
                response.get('return_msg', ''),
            )
            
            cur.execute(sql, params)
        
        conn.commit()
        print(f'  [DB 저장] au10002: 1행 저장됨')
        return True
    
    except Exception as exc:
        print(f'  [DB 저장 오류] au10002: {exc}')
        conn.rollback()
        return False
    
    finally:
        conn.close()
