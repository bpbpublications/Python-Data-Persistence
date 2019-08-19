#example 9.7
#myclasses.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
base=declarative_base()
class Product(Base):
    __tablename__ = 'Products'

ProductID = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
#example 9.11
class Customer(base):
    __tablename__='Customers'

    CustID=Column(Integer, primary_key=True)
    name=Column(String)
    GSTIN=Column(String)
#example 9.13
    class Product(base):
    __tablename__ = 'Products'
    
    ProductID = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    def __str__(self):
        return 'name:{} price: {}'.format(self.name, self.price)

base.metadata.create_all(engine)
