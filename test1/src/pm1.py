'''
Created on 2023 Sep 14

@author: leo
'''
from dateutil.parser._parser import parse
from locale import str

def __main__():
    l = [x for x in (1, 3, 4, 6)]
    print( l)
    r=range(5)
    for i in r:
        s = "paso {"+str(i)+ " "+str(i%2)+"} "
        print(s)

if __name__ == '__main__':
    __main__()