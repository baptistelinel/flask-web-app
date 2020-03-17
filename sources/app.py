import psycopg2
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    # conn = psycopg2.connect('dbname=products user=user password=password')
    app.run(host="0.0.0.0", port=5000)
