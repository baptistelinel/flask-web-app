import psycopg2


class DatabaseConnector:
    def __init__(self):
        connection = psycopg2.connect(
            database='supermarket',
            user='user',
            password='password',
            host='database',
            port='5432')
        self._cursor = connection.cursor()

    def run_fetchall_sql(self, sql: str):
        self._cursor.execute(sql)
        return str(self._cursor.fetchall())
