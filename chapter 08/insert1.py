#8.4
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
cur=conn.cursor()
qry="insert into Products values (1,'Laptop', 25000);"
try:
        cur.execute(qry)
        conn.commit()
        print ('Record inserted successfully')
except:
        print ('error in insert operation')
        conn.rollback()
conn.close()
