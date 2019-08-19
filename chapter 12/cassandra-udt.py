#cassandra-udt.py
#example 12.11
from cassandra.cluster import Cluster
cluster = Cluster(protocol_version=3)
session = cluster.connect()
session.set_keyspace('mykeyspace')
session.execute("CREATE TYPE contact (email text, phone text)")
session.execute("CREATE TABLE users (userid int PRIMARY KEY, name text, contact frozen<contact>)")
class ContactInfo:

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

cluster.register_user_type('mykeyspace', 'contact', ContactInfo)

# insert a row using an instance of ContctInfo
session.execute("INSERT INTO users (userid, name, contact) VALUES (%s, %s, %s)",
                (1, 'Admin', ContactInfo("admin@testserver.com", '9988776655')))
