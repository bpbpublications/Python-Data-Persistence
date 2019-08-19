#8.10
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
nm=input ('Enter name of product:')
cur=conn.cursor()
qry="select * from Products where name=?";
cur.execute(qry, (nm,))
row=cur.fetchone()
print (row)
conn.close()
