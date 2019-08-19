#classattr2.py
#4.30
class player:
        __total=0
        def __init__(self, name, runs):
                self.__name=name
                self.__runs=runs
                player.__total+=self.__runs
                print ('Total runs so far:',player.__total)
        @classmethod
        def printtotal(cls):
                print ('Total runs so far:',cls.__total)
        @staticmethod
        def displaytotal():
                print ('Total runs so far:',player.__total)
