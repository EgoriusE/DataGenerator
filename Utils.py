import psycopg2

conn = psycopg2.connect(dbname='EgMusic', user='postgres',
                        password='9368', host='localhost')
cursor = conn.cursor()


def close_connection():
    cursor.execute('commit;')
    cursor.close()
    conn.close()
