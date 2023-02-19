'''
Problem Description:
Given an array of integers nums containing n + 1 integers where each integer is in the range 
[1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
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
    
    def findDuplicate(self, nums):
        size = len(nums)
        # base case;
        if(size == 0 and size == 1):
            return None
        # main case;
        i,res = 0, None
        nums = sorted(nums)
        while(i < size-1):
            if(nums[i] == nums[i+1]):
                res = nums[i]
                break
            i += 1
        return res
        

def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
        print(res) if res else print("Empty!")
        
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
