#example.py
import MyPackage
#calling isprime function
num=int(input('enter a number..'))
retval=MyPackage.isprime(num)
if retval==True:
        print ("{} is a prime number".format(num))
else:
        print ("{} is not a prime number".format(num))

#addall function
result=MyPackage.addall(10,20)
print ("Result of addition:",result)
