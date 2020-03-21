import psycopg2
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/products')
def get_products():
    return 'Products 12'


if __name__ == '__main__':
    conn = psycopg2.connect(database='supermarket', user='user', password='password', host='database', port='5432')
    app.run(host='0.0.0.0', port=5000)
