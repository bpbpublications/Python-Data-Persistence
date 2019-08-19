#8.9
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
cur=conn.cursor()
qry="select * from Products;"
cur.execute(qry)
rows=cur.fetchall()
for row in rows:
        print (row)
conn.close()
