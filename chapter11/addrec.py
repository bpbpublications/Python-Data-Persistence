#example 11.12
from pymongo import MongoClient
client=MongoClient()
db=client.newdb
db.create_collection("customers")
cust=db['customers']
custlist=[{'CustID':1,'Name':'Ravikumar','GSTIN':'27AAJPL7103N1ZF'},
{'CustID':2,'Name':'Patel','GSTIN':'24ASDFG1234N1ZN'},
{'CustID':3,'Name':'Nitin','GSTIN':'27AABBC7895N1ZT'},
{'CustID':4,'Name':'Nair','GSTIN':'32MMAF8963N1ZK'},
{'CustID':5,'Name':'Shah','GSTIN':'24BADEF2002N1ZB'},
{'CustID':6,'Name':'Khurana','GSTIN':'07KABCS1002N1ZV'},
{'CustID':7,'Name':'Irfan','GSTIN':'05IIAAV5103N1ZA'},
{'CustID':8,'Name':'Kiran','GSTIN':'12PPSDF22431ZC'},
{'CustID':9,'Name':'Divya','GSTIN':'15ABCDE1101N1ZA'},
{'CustID':10,'Name':'John','GSTIN':'29AAEEC4258E1ZK'}]
cust.insert_many(custlist)
client.close()
