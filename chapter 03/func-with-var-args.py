#func-with-var-args.py
def addall(*nums):
        ttl=0
        for num in nums:
                ttl=ttl+num
        return ttl
total=addall(10,20,50,70)
print ('Total of 4 numbers:',total)
total=addall(11,34,43)
print ('Total of 3 numbers:',total)
