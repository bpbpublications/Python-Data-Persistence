#else-in-loop.py
num=int(input("enter a number.."))
x=2
while x<num:
        if num%x==0:
                print ("{} is not prime.".format(num))
                break
        x=x+1
else:
        print ("{} is prime.".format(num))
print ('end of program')
