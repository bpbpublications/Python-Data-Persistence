#fetchallrecs.py
#example 9.14
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from myclasses import Product,base, Customers
engine = create_engine('sqlite:///mydb.sqlite', echo=True)
base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
sessionobj = Session()
q=sessionobj.query(Products)
rows=q.all()
for row in rows:
        print (row) 
