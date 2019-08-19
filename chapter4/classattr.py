#classattr.py
class player:
        __total=0
        def __init__(self, name, runs):
                self.__name=name
                self.__runs=runs
                player.__total+=self.__runs
                print ('Total runs so far:',player.__total)
