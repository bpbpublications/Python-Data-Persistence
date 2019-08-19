#example 9.29
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///mydb.sqlite', echo=True)
meta=MetaData()
Products = Table('Products', meta, Column('ProductID', Integer, primary_key=True), Column('name', String), Column('Price', Integer), )
meta.create_all(engine)
