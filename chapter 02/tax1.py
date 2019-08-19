#tax1.py
salary=int(input("enter salary.."))
tax=0
if salary>=50000:
        #tax @10%
        tax=salary*10/100
net_sal=salary-tax
print ("Salary={} tax={} net payable={}".format(salary, tax, net_sal))
