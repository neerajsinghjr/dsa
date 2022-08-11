'''
#Day 01: ...
#Problem 02: ... 
#Problem Description: 
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    
    def __init__(self, data):
        self.data = data


def main():
    try:
        obj = Solution()
        if type(res) == tuple:
        	print(f"Result: {res[1]}")
        	print(f"Return: {res[0]}")
        else:
        	print(f"Result: {res}")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Completed: Success")

    finally:    
        print("Program Terminated!")
        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    