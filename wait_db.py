# wait_for_postgres.py
import time
import psycopg2
from psycopg2 import OperationalError

while True:
    try:
        conn = psycopg2.connect(dbname='db', user='user', password='password', host='localhost', port='5432')
        conn.close()
        print('PostgreSQL is ready!')
        break
    except OperationalError:
        print('Waiting for PostgreSQL...')
        time.sleep(3)