#8.7
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
nm=input('enter name of product:')
p=int(input('new price:'))
qry='update Products set price=? where name=?'
cur=conn.cursor()
try:
        cur.execute(qry, (p,nm))
        print ('record updated')
        conn.commit()
except:
        print ('error in update operation')
        conn.rollback()
conn.close()
