import uuid
from database_conector import DatabaseConnector
from product_mapping import ProductMapping


class ProductBusiness:
    def __init__(self, database_connector: DatabaseConnector):
        self._database_connector = database_connector

    def get_list_products(self) -> list:
        products = []
        product_mapping_list = self._database_connector.list_resource(ProductMapping)
        for product in product_mapping_list:
            products.append({
                'uuid': product.uuid,
                'name': product.name,
                'price': product.price
            })
        return products

    def add_product(self, data):
        product = ProductMapping(uuid=str(uuid.uuid4()), name=data['name'], price=data['price'])
        self._database_connector.add_resource(product)
