from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

with open('schema.sql', 'r') as file:
    sql = file.read()

cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()