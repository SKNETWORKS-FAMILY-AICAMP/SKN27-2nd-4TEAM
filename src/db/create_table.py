import psycopg2

def create_db_table():
    try:
        # 1. DB 연결 설정
        conn = psycopg2.connect(
            host="localhost",      # 혹은 DB 서버 주소
            database="your_db",    # 생성한 데이터베이스 이름
            user="postgres",       # 사용자 아이디
            password="your_password", # 비밀번호
            port="5432"
        )
        cur = conn.cursor()

        # 2. SQL 실행 (테이블 생성)
        # 만약 기존에 테이블이 있으면 삭제하고 새로 만들려면 DROP 문을 추가하세요.
        create_script = '''
        CREATE TABLE IF NOT EXISTS user_churn_results (
            user_id VARCHAR(50) PRIMARY KEY,
            churn_prob FLOAT,
            is_churn INT,
            is_cherry_picker BOOLEAN,
            update_at TIMESTAMP DEFAULT NOW()
        );
        '''
        
        cur.execute(create_script)
        
        # 3. 변경사항 저장 및 종료
        conn.commit()
        print("✅ 테이블이 성공적으로 생성되었습니다!")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
    
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    create_db_table()