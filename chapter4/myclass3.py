#myclass3.py
#4.15
class MyClass:
        __slots__=['myname', 'myage']
        def __init__(self, name=None, age=None):
                self.myname=name
                self.myage=age                
        def about(self):
                print ('My name is {} and I am {} years old'.format(self.myname,self.myage))
