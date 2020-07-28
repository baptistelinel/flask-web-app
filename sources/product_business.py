from database_conector import DatabaseConnector


class ProductBusiness:
    def __init__(self, database_connector: DatabaseConnector):
        self._database_connector = database_connector

    def get_list_products(self):
        return self._database_connector.run_fetchall_sql('SELECT * FROM products;')
