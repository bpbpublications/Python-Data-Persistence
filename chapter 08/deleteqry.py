#8.8
import sqlite3
conn=sqlite3.connect('mydb.sqlite')
nm=input('enter product to delete:')
qry='delete from Products where name=?'
cur=conn.cursor()
try:
        cur.execute(qry, (nm,))
        print ('record deleted')
        conn.commit()
except:
        print ('error in delete operation')
        conn.rollback()
conn.close()
