#8.19
import sqlite3
conn=sqlite3.connect('sample.db')
qry='create table names (name text (20), address text(20));'
conn.execute(qry)
qry="insert into names values('Anurag', 'Mumbai');"
cur=conn.cursor()
try:
        cur.execute(qry)
        print ('record added')
        conn.commit()
except:
        print ('error in insert operation')
        conn.rollback()
conn.close()
#creating dump
conn=sqlite3.connect('sample.db')
f=open('dump.sql','w')
for line in conn.iterdump():
        f.write('{}\n'.format(line))
f.close()
conn.close()
