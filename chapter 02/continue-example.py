#continue-example.py
count=1
sum=0
while count<=5:
        num=int(input('enter a number..'))
        if num<0:
                print ('negative number is not accepted. Try again..')
                continue
        sum=sum+num
        count=count+1
print ('sum=',sum) 
