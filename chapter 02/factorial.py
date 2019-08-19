#factorial.py
n=int(input("enter number.."))
#calculating factorial of n 
f=1
for i in range(1,n+1):
        f=f*i
print ('factorial of {} = {}'.format(n,f))
