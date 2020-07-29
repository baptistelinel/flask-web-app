from sqlalchemy import Column, String, Float
from sqlalchemy.databases import postgres
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class ProductMapping(base):
    __tablename__ = 'products'

    uuid = Column(postgres.UUID(), primary_key=True)
    name = Column(String)
    price = Column(Float)
