#8.15
import sqlite3
conn=sqlite3.connect('mydb.sqlite')

class myclass:
        def __init__(self):
                self.count=0
        def step(self, string):
                if string.endswith('r'):
                        self.count=self.count+1
        def finalize(self):
                return self.count
conn.create_aggregate('MyF',1,myclass)
cur=conn.cursor()

qry="select MyF(name) from products;"
cur.execute(qry)
row=cur.fetchone()
print ('number of products with name ending with 'r':',(row)[0])
conn.close()
