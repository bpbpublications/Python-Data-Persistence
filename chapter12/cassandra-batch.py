#cassandra-batch.py
#example 12.9
from cassandra.cluster import Cluster
clstr=Cluster()
session=clstr.connect('mykeyspace')
custlist=[(1,'Ravikumar','27AAJPL7103N1ZF'),
        (2,'Patel','24ASDFG1234N1ZN'),
        (3,'Nitin','27AABBC7895N1ZT'),
        (4,'Nair','32MMAF8963N1ZK'),
        (5,'Shah','24BADEF2002N1ZB'),
        (6,'Khurana','07KABCS1002N1ZV'),
        (7,'Irfan','05IIAAV5103N1ZA'),
        (8,'Kiran','12PPSDF22431ZC'),
        (9,'Divya','15ABCDE1101N1ZA'),
        (10,'John','29AAEEC4258E1ZK')]

from cassandra.query import SimpleStatement, BatchStatement
batch=BatchStatement()
for cst in custlist:
        batch.add(SimpleStatement("INSERT INTO customers (custID,name,GSTIN) VALUES (%s, %s, %s)"), \
              (cst[0], cst[1],cst[2]))
session.execute(batch)
