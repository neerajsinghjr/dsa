'''
Problem Description:
Fibonacci Series using a recursion backtracking.
eg, 0 1 1 2 3 5 7 . . . . . . . 
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
    
    # Method 1 : Brute Force
    def fiboV1(self, first, second):
        pass

    
    # Method 2 : Recursion Backtracking 
    def fiboV2(self, first, second):
        pass


def main():
    try:
        first, seconds = 0, 1
        obj = Solution()
        res1 = obj.fiboV1(first, seconds)                           # Brute Force
        print(res1) if res1 else print("Empty!")
        res2 = obj.fiboV2(first, seconds)                           # Recursion Backtracking
        print(res2) if res2 else print("Empty!")

        
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print("Program Completed : Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    