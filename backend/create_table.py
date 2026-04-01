from connection import get_connection

conn = get_connection()
cursor = conn.cursor()

with open('schema.sql', 'r') as file:
    sql_commands = file.read().split(';')

for command in sql_commands:
    if command.strip():
        cursor.execute(command)


conn.commit()

cursor.close()
conn.close()