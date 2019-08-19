#8.3
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
cur=conn.cursor()
qry='''
CREATE TABLE Customers (
        CustID INTEGER   PRIMARY KEY AUTOINCREMENT,
        Name   TEXT (20),
        GSTIN  TEXT (15)
    );
CREATE TABLE Invoices (
        InvID     INTEGER     PRIMARY KEY AUTOINCREMENT,
        CustID    TEXT        REFERENCES Customers (CustID),
        ProductID INTEGER     REFERENCES Products (ProductID),
        Quantity  INTEGER (5)
    );
'''
try:
        cur.executescript(qry)
        print ('Table created successfully')
except:
        print ('error in creating table')
conn.close()
