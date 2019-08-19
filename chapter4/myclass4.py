#myclass4.py
#4.17
class MyClass:
        __slots__=['myname', 'myage']
        def __init__(self, name=None, age=None):
                self.myname=name
                self.myage=age
        def getname(self):
                return self.myname
        def setname(self, name):
                self.myname=name
        def getage(self):
                return self.myage
        def setage(self, age):
                self.myage=age
        def about(self):
                print ('My name is {} and I am {} years old'.format(self.myname,self.myage))
