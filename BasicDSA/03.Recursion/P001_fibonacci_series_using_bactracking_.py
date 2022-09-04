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
    def fiboV1(self, n):
        # base case;
        if(n <= 2):  return 1

        # main case;
        return self.fiboV1(n-1) + self.fiboV1(n-2)

    
    # Method 2 : Recursion Memoization;
    def fiboV2(self, n, map):
        # base case
        if(n <= 2): return 1

        # main case;
        if(n in map.keys()):
            return map[n]
        else:
            res = self.fiboV2(n-1,map) + self.fiboV2(n-2,map)
            map[n] = res                         # Memoization added to avoid extra logn loops
            return res


def main():
    try:
        n = 5
        obj = Solution()
        res1 = obj.fiboV1(n)                           # Brute Force
        print(res1) if res1 else print("Empty!")
        res2 = obj.fiboV2(n=n, map={})                           # Recursion Backtracking
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
    