#cassandra-select.py
#example 12.7
from cassandra.cluster import Cluster
clstr=Cluster()
session=clstr.connect('mykeyspace')
rows=session.execute("select * from products;")
for row in rows:
        print ('Manufacturer: {} ProductID:{} Name:{} price:{}'.format(row[1],row[0], row[2], row[3]))
