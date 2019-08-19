#example 9.26
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, and_, or_
from myclasses import Product,base, Customer, Invoice
engine = create_engine('sqlite:///mydb.sqlite', echo=True)
base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
sessionobj = Session()
q=sessionobj.query(Invoice,Product)
for i,p in q.filter(Product.ProductID==Invoice.ProductID).all():
        print (i.InvID, p.name, p.price, i.quantity)
