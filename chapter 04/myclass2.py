#myclass2.py
4.12
class MyClass:
        def __init__(self, name=None, age=None):
                self.myname=name
                self.myage=age
        def about(self):
                print ('My name is {} and I am {} years old'.format(self.myname,self.myage))
