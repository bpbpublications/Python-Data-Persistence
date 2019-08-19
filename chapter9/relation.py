#example 9.23
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Invoice(base):
    __tablename__='Invoices'

    InvID=Column(Integer, primary_key=True)
    CustID=Column(Integer, ForeignKey('Customers.CustID'))
    ProductID=Column(Integer, ForeignKey('Products.ProductID'))
    prod=relationship("Customer", back_populates="Invoices")
    cst=relationship("Product", back_populates="Invoices")
    quantity=Column(Integer)

Product.Invoices=relationship('Invoice', order_by=Invoice.InvID, back_populates='cst')
Customer.Invoices=relationship('Invoice', order_by=Invoice.InvID, back_populates='prod')
