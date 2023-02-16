'''
-------------------------------------------------------------------------------------
-> Title: 
-> Attempted:
-> Description: 
-------------------------------------------------------------------------------------



-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from functools import reduce


###--- Reduce Function;;
def main(res=None):
    mylist = [12,13,11,14,14,14,14,15,16]
    
    # Scenario 1: Without Lambda;
    def _sum(a, b):
        count = 1
        print(f"count {count}, : {a},{b}")
        return a+b

    print("sum >", sum(mylist))

    a = reduce(_sum, mylist)
    print("sum >> ", a)

    # Scenario 2 : With Lambda;;
    res2 = reduce(lambda a,b : a+b, mylist)
    print(f"res2: {res2}")


    

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    
