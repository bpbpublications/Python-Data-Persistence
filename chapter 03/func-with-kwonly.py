#func-with-kwonly.py
def division(*,num, denom):
        div=num/denom
        print ('numerator:{} denominator: {} division: {}'.format(num,denom,div))

division(denom=2, num=10)
division(10,2)
