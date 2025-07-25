# Данные для подключения
# HOST = '185.86.147.205'
# PORT = 5432
# DATABASE = 'Eduson'
# USER = 'student'
# PASSWORD = "QweAsd1234567890!"

import psycopg2
HOST = '185.86.147.205'
PORT = 5432
DATABASE = 'Eduson'
USER = 'student'
PASSWORD = "QweAsd1234567890!"

connection = psycopg2.connect(
    host = HOST,
    port = PORT,
    database = DATABASE,
    user = USER,
    password = PASSWORD
)
cursor = connection.cursor()
query = """select * from orders limit 10"""
exec = cursor.execute(query)
res = cursor.fetchall()
print(res)

