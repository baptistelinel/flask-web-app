import psycopg2
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    conn = psycopg2.connect(database='products', user='user', password='password', host='database', port='5432')
    app.run(host='0.0.0.0', port=5000)
