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

    # Method 1 : General Optimized, sort O(nlogn)
    def shiftNegativePositiveV1(self, nums):
        print("Solution V1...")
        nums.sort()
        return nums
    

    # Method 2 : DNF algorithm
    def shiftNegativePositiveV2(self, nums):
        print("Solution V2 ...")
        low = 0
        for i in range(0,len(nums)):
            if(nums[i] < 0):
                nums[i],nums[low] = nums[low], nums[i]
                low += 1
            

    # Method 3 : 
    def shiftNegativePositiveV3(self,nums):
        print("Solution V3...")
        low,high = 0, len(nums)-1
        while(low < high):
            # Case 1 : Low SMALL and High LARGE
            if(nums[low] > 0 and nums[high] < 0):
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
            
            # Case 2 : Low SMALL and High LARGE
            elif(nums[low] < 0 and nums[high] > 0):
                low += 1
                high -= 1
            
            # Case 3 : Both LARGE
            elif(nums[low] > 0 and nums[high] > 0):
                high -= 1
            
            # Case 4 : Both SMALL
            elif(nums[low] < 0 and nums[high] < 0):
                low += 1
                


def main():
    try:
        # Output : [-110, -90, -80, -40, -11, -10, -2, 20, 30, 40, 50, 150, 200, 210, 230]
        data = [ 0, 20, -11, -110, 30, 40, -2, 230, -10, -40, 50, 150, 200,-80, -90, 210 ]
        obj = Solution()
        obj.shiftNegativePositiveV1(data)
        # obj.shiftNegativePositiveV2(data)
        # obj.shiftNegativePositiveV3(data)
        print(data) if data else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print("Program Completion : Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    
