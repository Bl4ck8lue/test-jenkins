import sys

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

def main(name1, email1, passw):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host)
    cursor = conn.cursor()

    person = (name1, email1, passw)

    conn.autocommit = True
    # команда для создания базы данных metanit
    sql = "select * from clients"
    # sql2 = "insert into clients (name, email, hash_pass) values (%s, %s, md5(%s))"

    # выполняем код sql
    cursor.execute("insert into clients (name, email, hash_pass) values (%s, %s, md5(%s))", person)
    cursor.execute(sql)
    print(cursor.fetchall())

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
