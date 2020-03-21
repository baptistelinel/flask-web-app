import psycopg2
from flask import Flask

app = Flask(__name__)
connection = psycopg2.connect(database='supermarket', user='user', password='password', host='database', port='5432')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/products')
def get_products():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products;')
    return str(cursor.fetchall())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
