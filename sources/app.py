import psycopg2
from flask import Flask

from database_conector import DatabaseConnector
from product_business import ProductBusiness

app = Flask(__name__)
product_business = ProductBusiness(DatabaseConnector())


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/products')
def get_products():
    return product_business.get_list_products()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
