'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description: 
----------------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

#---Main Solution
class Solution:
    
    """
    Run: Accepted
    Code: Brute Force | T:O(N) | S:O(1)
    Study: 
    Calculated difference of natural number sum with the current sum (non duplicate),
    and the difference of current sum (duplicate) current sum with (non duplicate).
    """
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n,a,b = len(nums), sum(nums), sum(set(nums))
        s = n*(n+1)//2
        return [a-b, s-b]
    
    
##---Main Execution;;
def main(res=None):
    try:
        print(f"res: {res}")
        
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
    