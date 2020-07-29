from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnector:
    def __init__(self):
        db_string = 'postgres://user:password@database:5432/supermarket'
        db = create_engine(db_string)
        self._session = sessionmaker(db)()

    def list_resource(self, resource):
        return self._session.query(resource)

    def add_resource(self, resource: object) -> None:
        self._session.add(resource)
        self._session.commit()

