'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Maximum subarray of size k
-> Problem Status: Ongoing...
-> Problem Attempted: 07.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are aksed to return the maximum sum of subarray of the size k

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

from sys import maxsize

###--- Main Solution;;
class Solution:
    
   def maxSubArraySum(self,nums,k):
        cursum = 0
        start,cur = 0,0
        maxsum = -maxsize

        for cur in range(k):
            cursum += nums[cur]

        for cur in range(k,n):
            cursum += nums[cur]
            cursum -= nums[start]



##---Main Execution;;
def main():
    try:
        num = [2,3,5,3,2,1,1,2,3,4,2,1,1,7,8,9,0]
        k  = 3
        obj = Solution()
        res = obj.maxSubArraySum(num,k)

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
    