from pickle import Pickler, Unpickler
class User:
        def __init__(self,name, email, pw):
                self.name=name
                self.email=email
                self.pw=pw
        def __str__(self):
return ('Name: {} email: {} password: {}'. \
                       format(self.name, self.email, self.pw))

user1=User('Rajan', 'r123@gmail.com', 'rajan123')
user2=User('Sudheer', 's.11@gmail.com', 's_11')
print ('before pickling..')
print (user1)
print (user2)
file=open('users.dat','wb')
Pickler(file).dump(user1)
Pickler(file).dump(user2)
file.close()

file=open('users.dat','rb')
obj1=Unpickler(file).load()
print ('unpickled objects')
print (obj1)
obj2=Unpickler(file).load()
print (obj2)   
