#8.2
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
cur=conn.cursor()
qry='''
CREATE TABLE Products (
ProductID INTEGER   PRIMARY KEY AUTOINCREMENT,
Name      TEXT (20),
Price     INTEGER
);
'''
try:
        cur.execute(qry)
        print ('Table created successfully')
except:
        print ('error in creating table')
conn.close() 
