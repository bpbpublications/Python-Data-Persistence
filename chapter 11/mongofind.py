#mongofind.py
#example 11.14
from pymongo import MongoClient
client=MongoClient()
db=client.newdb
cust=db['customers']
docs=cust.find()
while True:
        try:
                doc=docs.next()
                print (doc['Name'], doc['GSTIN'])
        except StopIteration:
                break

client.close()
