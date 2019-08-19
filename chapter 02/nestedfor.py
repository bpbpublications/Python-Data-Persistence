#nestedfor.py
for num in range(1,101):
        for x in range(2,num):
                if num%x==0:
                        break
                x=x+1
        else:
                print (num,sep=' ', end=' ')
