#8.13
import sqlite3
conn=sqlite3.connect('mydb.sqlite')

def myfunction(num):
        return str(round(num/1000))+"k"
conn.create_function('priceinK',1,myfunction)        
cur=conn.cursor()

qry="select name, priceinK(price) from products;"
cur.execute(qry)
rows=cur.fetchall()
print (rows)
conn.close()
