'''
#Day 01: 26-06-2022

#Problem 02: Kadane's Algorithms for running sum;

#Problem Description: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum and print the subarray.

Example 1:
Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 
Output: 6 
Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 
Input: arr = [1] 
Output: 1 
Explanation: Array has only one element and which is giving positive sum of 1. 

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


    # NAIVE APPROACH: 
    def maxSubArray(self):
        nums = self.data

        if not(nums) == None: return len(nums)
        if len(nums) == 1: return nums[1]

        i = 0
        maxSumTillNow = nums[0]
        for i in range(len(nums)):
            runningSum = 0
            for j in range(i+1,len(nums)):
                runningSum += nums[j]
                if runningSum > maxSumTillNow:
                    maxSumTillNow = runningSum

        return maxSumTillNow


def main():
    try:
        data = [-2,1,-3,4,-1,2,1,-5,4]
        obj = Solution(data)
        res = obj.maxSubArray()

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
    