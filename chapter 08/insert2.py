#8.6
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
cur=conn.cursor()
qry="insert into Products values (?,?,?)"
pricelist=[(1,'Laptop',25000),(2, 'TV',40000),
           (3,'Router',2000),(4,'Scanner',5000),
           (5,'Printer',9000), (6,'Mobile',15000)]
try:
        cur.executemany(qry, pricelist)
        conn.commit()
        print ('Records inserted successfully')
except:
        print ('error in insert operation')
        conn.rollback()
conn.close()
