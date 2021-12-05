'''
Problem Description:
Find the subset or subsequnce of a given string

#Input
string = "abc"

#Output
["","a","b","c","ab","bc","ca","abc]
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def substrings(txt):
    pass


def main():
    try:
        strings = [
            "abc"
        ]
        for txt in strings:
            res = substrings(txt)
            print(res) if res else print("Empty!")
            
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")
        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    