#example 9.21
from sqlalchemy import ForeignKey
class Invoice(base):
    __tablename__='Invoices'

    InvID=Column(Integer, primary_key=True)
    CustID=Column(Integer, ForeignKey('Customers.CustID'))
    ProductID=Column(Integer, ForeignKey('Products.ProductID'))
    quantity=Column(Integer)
