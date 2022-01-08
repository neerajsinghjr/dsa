'''
Problem Description: 
An array contains both positive and negative numbers in random order. 
Rearrange the array elements so that all negative numbers appear 
before all positive numbers.

Example 1:
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12, -13, -5, -7, -3, -6, 11, 6, 5 
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
    # Method 1 : General Optimized
    def shiftNegativePositiveV1(self, nums):
        low = high = 0
        while(low):
            if(low < high):
                nums[low], nums[high] = nums[high], nums[low]
            else:
                nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        return nums
    
    # Method 2 : DNF algorithm
    def shiftNegativePositiveV2(self, nums):
        low,mid,high = 0,0,len(nums)-1
        for i in range(0,len(nums)):
            if(nums[low] > nums[mid]):
                pass
            elif():
                pass


def main():
    try:
        data = [ 20, -11, -110, 30, 40, -2, 230, -10, -40, 50, 150, 200,-80, -90, 210 ]
        obj = Solution()
        obj.shiftNegativePositive(data)
        print(data) if data else print("Empty!")
        
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
    