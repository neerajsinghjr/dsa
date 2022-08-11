'''
Problem Description:
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
    
    # Method 1: Brute Force
    def findPathV1(self, nums):
        pass

    # Method 2: Optimized Force
    def findPathV2(self, nums):
        pass


def main():
    try:
        nums = [
            [],
            [],
            [],
            [],
        ]
        obj = Solution()
        res1 = obj.findPathV1(nums)
        print(res1) if res1 else print("Empty!")
        res2 = obj.findPathV2(nums)
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
    