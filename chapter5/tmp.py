fn=input('enter filename..')

try:    
    f=open(fn,'r')
    data=f.read()
    print (data)
except FileNotFoundError as e:
    print ("error message",e)
print ("end of program")
