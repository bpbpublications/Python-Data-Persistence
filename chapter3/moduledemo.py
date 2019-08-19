#moduledemo.py
import mymodule
print ('calling isprime function from mymodule')
n=int(input('enter a number..'))
retval=mymodule.isprime(n)
if retval==True:
        print ('{} is a prime number'.format(n))
else:
        print ('{} is not a prime number'.format(n))
