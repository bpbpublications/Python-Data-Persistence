#addfunctions.py
def add(num1,num2):
        result=num1+num2
        return result
def addall(*nums):
        ttl=0
        for num in nums:
                ttl=ttl+num
        return ttl
