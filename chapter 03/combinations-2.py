#combinations-2.py

#calculate factorial
def factorial(x):
        f=1
        for i in range(1,x+1):
                f=f*i
        return f

n=int(input("enter n.."))
r=int(input("enter r.."))
combinations=factorial(n)/(factorial(r)*factorial(n-r))
print ("C({},{})={}".format(n,r, combinations))
