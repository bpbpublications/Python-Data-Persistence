'docstring of mymodule'
def isprime(num):
        x=2
        for x in range(2,num):
                if num%x==0:
                        return False
        else:
                return True

def iseven(num):
        if num%2==0:
                return True
        else:
                return False
def isleap(num):
        if num%4==0:
                return True
        else:
                return False
#modify as follows:
if __name__=='__main__':        
        n=int(input('enter a number..'))
        retval=iseven(n)
        if retval==True:
                print ('{} is even'.format(n))
        else:
                print ('{} is odd'.format(n))
