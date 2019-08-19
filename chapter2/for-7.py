#secret-number.py
import random
secret=random.randint(1,10)
chances=0
while chances<10:
        guess=int(input('enter your guess..'))
        if guess==secret:
                print ('you got that right!')
                break
                print ('try again..')

                chances=chances+1
                if chances==10:
                        print ('chances exhausted. secret number is:',secret)
