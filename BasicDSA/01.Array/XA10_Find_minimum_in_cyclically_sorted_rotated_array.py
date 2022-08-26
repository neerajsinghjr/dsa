'''
Problem Description:
Given an Cyclically sorted array, and you are told to find the minimum of the array;

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
    
    # Brute Force Approach, O(n);
    def findMinimunV1(self, nums):
        # base case;
        if not nums : return nums

        # main case;
        minNum = nums[0]
        for num in nums:
            minNum = min(minNum, num)
        return minNum


    # Binary Search, O(logn);
    def findMinimumV2(self, nums):
        """
        Method 2: Binary Search Approach Working
        1) First mark the start, end pointer for the tracing elements.
        2) Element 'rightMost' hold the right side value. It will helps to track whether the 
        current mid value lies in the particular range.
        for eg, arr = [40,50,60,10,20,30]
        suppose, mid = 20 then wen can check, if nums[mid] lies in range(mid, rightMost)
        3) On Comparing the mid and rightMost, rotate the given pointer.
        """
        start, end = 0, len(nums)-1
        rightMost = nums[end]                       
        while(start <= end):
            mid = start + (end-start)//2
            if((nums[mid] <= rightMost) and (mid == 0 or nums[mid-1] > nums[mid])):
                return f"Min Value : {mid}/{nums[mid]}"
            elif(nums[mid] > rightMost):
                start = mid + 1
            elif(nums[mid] < rightMost):
                end = mid - 1

        return f"Not Found"


def main():
    # try:
    data = [
        [60,70,80,90,100,10,20,30,40,50],
        [6,7,8,9,10,1,2,3,4],
        [501,502,600,800,900,901,101,202,222,223,225],
    ]
    obj = Solution()
    for nums in data:
        # res = obj.findMinimunV1(nums)                # V1
        res = obj.findMinimumV2(nums)              # V2
        print(res) if res else print("Empty!")
        
    # except(Exception) as e:
    #     print(f"Exception Traced : {e}")
    
    # else:
    #     print("Program Completed : Success")

    # finally:
    #     print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    