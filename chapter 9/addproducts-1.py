#example 9.9
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from myclasses import Products,base
engine = create_engine('sqlite:///mydb.sqlite', echo=True)
base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
sessionobj = Session()
p1 = Product(name='Laptop', price=25000)
sessionobj.add(p1)
sessionobj.commit()
