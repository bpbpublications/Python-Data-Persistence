#combinations.py
n=int(input("enter n.."))
r=int(input("enter r.."))
t=n-r
#calculating factorial of n - fn
fn=1
for i in range(1,n+1):
        fn=fn*i
#calculating factorial of r - fr
fr=1
for i in range(1,r+1):
        fr=fr*i
#calculating factorial of t - tr
ft=1
for i in range(1,t+1):
        ft=ft*i
combinations=fn/(fr*ft)
print ("C({},{})={}".format(n,r, combinations))
