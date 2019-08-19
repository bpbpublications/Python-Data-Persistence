#func-with-return.py
def add(num1,num2):
        'function assumes a two numbers to be passed'
        result=num1+num2
        return result
#call above function
x=int(input('enter a number..'))
y=int(input('enter another number..'))
z=add(x,y)
print ('addition of {} and {} is {}'.format(x,y,z))
