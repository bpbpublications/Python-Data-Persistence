#cassandra-prepare.py
#example 12.10
from cassandra.cluster import Cluster
from cassandra.query import PreparedStatement
clstr=Cluster()
session=clstr.connect('mykeyspace')
stmt=session.prepare("INSERT INTO customers (custID, name,GSTIN) VALUES (?,?,?)")
boundstmt=stmt.bind([11,'HarishKumar', '12PQRDF22431ZN'])
session.execute(boundstmt)
