import os
import psycopg2

conn = psycopg2.connect(database=os.environ.get('POSTGRES_NAME'),
                        user=os.environ.get('POSTGRES_USER'),
                        password=os.environ.get('POSTGRES_PASSWORD'),
                        host="db",
                        port=5432)

cur = conn.cursor()

cur.execute("INSERT INTO film (login, password) VALUES (%s, %s)",
    ("afiskon", "123"))

conn.commit()