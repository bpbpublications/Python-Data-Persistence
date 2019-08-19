#mongoupdate.py
#example 11.18
from pymongo import MongoClient
client=MongoClient()
db=client.newdb
prod=input('enter name:')
doc=db.products.find_one({'Name':prod})
print (doc['Name'], doc['price'])
price=int(input('enter price:'))
db['products'].update_one({'Name':prod},{"$set":{'price':price}})
client.close()
