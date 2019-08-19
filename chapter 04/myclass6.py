#myclass6.py
#4.26
class MyClass:
        __slots__=['__myname', '__myage']
        def __init__(self, name=None, age=None):
                self.__myname=name
                self.__myage=age

        @property
        def name(self):
                print ('name getter method')
                return self.__myname
        @property
        def age(self):
                print ('age getter method')
                return self.__myage
        @name.setter
        def name(self,name):
                print ('name setter method')
                self.__myname=name
        @age.setter
        def age(self, age):
                print ('age setter method')
                self.__myage=age

        def about(self):
                print ('My name is {} and I am {} years old'.format(self.__myname,self.__myage))
