import psycopg2
import streamlit as st

conn = psycopg2.connect(
    host=st.secrets['postgres']['host'],
    port=st.secrets['postgres']['port'],
    database=st.secrets['postgres']['database'],
    user=st.secrets['postgres']['user'],
    password=st.secrets['postgres']['password']
)

cursor = conn.cursor()

with open('schema.sql', 'r') as file:
    sql = file.read()

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()