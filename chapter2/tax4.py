#tax4.py
salary=int(input("enter salary.."))
tax=0
if salary>=50000:
        #tax @10%
        tax=salary*10/100
elif salary>25000:
        #tax @5%
        tax=salary*5/100
elif salary>10000:
        #tax @2%
        tax=salary*2/100
else:
        #no tax
        print ("No tax applicable")
net_sal=salary-tax
print ("Salary={} tax={} net payable={}".format(salary, tax, net_sal))
