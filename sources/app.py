from flask import Flask, request

from database_conector import DatabaseConnector
from product_business import ProductBusiness

app = Flask(__name__)
product_business = ProductBusiness(DatabaseConnector())


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/products', methods=['GET', 'POST'])
def product_resource():
    if request.method == 'GET':
        products = product_business.get_list_products()
        return {
            'products': products
        }
    elif request.method == 'POST':
        data = request.form
        product_business.add_product(data)
        return 'Product added'
    else:
        return 'Unauthorized HTTP verb.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
