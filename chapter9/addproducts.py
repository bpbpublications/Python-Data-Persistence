#example 9.8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from myclasses import Product, base
engine = create_engine('sqlite:///mydb.sqlite', echo=True)
base.metadata.create_all(engine)
