#myclass5.py
#4.21
class MyClass:
        __slots__=['__myname', '__myage']
        def __init__(self, name=None, age=None):
                self.__myname=name
                self.__myage=age
        def getname(self):
                print ('name getter method')
                return self.__myname
        def setname(self, name):
                print ('name setter method')
                self.__myname=name
        def getage(self):
                print ('age getter method')
                return self.__myage
        def setage(self, age):
                print ('age setter method')
                self.__myage=age
        name=property(getname, setname, "Name")
        age=property(getage, setage, "Age")
        def about(self):
                print ('My name is {} and I am {} years old'.format(self.__myname,self.__myage))
