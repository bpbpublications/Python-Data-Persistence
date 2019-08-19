#function-4.py
def function(string,num):
        'function assumes a string and number to be passed'
        print ('parameter received', string, num)
        print ('length of string:', len(string))
        if num%2==0:
                print (num,' is ','even')
        else:
                print (num, ' is ','odd')
        return
#call above function
function ('Hello', 10)
function (10, 'Hello')
