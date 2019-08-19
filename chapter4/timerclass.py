#timerclass.py
#4.42
class timer:
        def __init__(self, hr=None, min=None):
                self.hrs=hr
                self.mins=min
        def __add__(self, arg):
                temp=timer()
                temp.hrs=self.hrs+arg.hrs
                temp.mins=self.mins+arg.mins
                if temp.mins>=60:
                        temp.mins=temp.mins-60
                        temp.hrs=temp.hrs+1
                return temp
        def __str__(self):
                timestring='{} Hrs. {} mins.'.format(self.hrs,self.mins)
                return timestring
