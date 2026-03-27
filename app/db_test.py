import sys
from pathlib import Path

import streamlit as st

# Make project root importable when running via Streamlit
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from db.connection import test_db_connection  # noqa: E402


st.set_page_config(page_title="DB Test", layout="centered")
st.title("DB 연결 테스트")

st.write("버튼을 눌러 `SELECT 1, now()`가 실행되면 DB 연결 성공입니다.")

if st.button("DB 연결 확인", type="primary"):
    try:
        result = test_db_connection()
        st.success(result)
    except Exception as e:
        st.error(f"DB 연결 실패: {e}")
