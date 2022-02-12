'''
Problem Description:

Given an array Arr[] of N integers. Find the contiguous sub-array
(containing at least one number) which has the maximum sum and 
return its sum.

Example 1:
Input: N = 5, Arr[] = {1,2,3,-2,5}
Output: 9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from math import ceil



# Brute Force Approach
def maxSubArraySum_V2(arr, n):
    # base case
    if arr == None: return 0

    # main case
    maxSum = 0
    for x in range(n):
        temp = 0
        for y in range(x+1,n):
            temp += arr[y]
            maxSum = max(temp, maxSum)
    return maxSum

# Kadane's Algorithms
def maxSubArraySum_V1(arr,n):
    # base case
    if arr == None: return 0
    
    # main case
    totalSum = runningSum = arr[0]
    for idx in range(1,n):
        if(runningSum < 0):   runningSum=0      # reset running sum;
        runningSum += arr[idx]                  # add runing sum
        totalSum = max(totalSum, runningSum)    # maintain total sum;
        
    return totalSum


def main():
    try:
        # data = [-1,-2,-3,-4]               # ~ data
        # data = [1,2,3,-2,5]
        data = [-2,-3,4,-1,-2,1,5,-1]
        # res1 = maxSubArraySum_V1(data, len(data))             # Kadane Algo
        res2 = maxSubArraySum_V2(data, len(data))               # Brute Force
        # print(f"Kadane : {res1}") if res1 else print("Empty!")
        print(f"Brute : {res2}") if res2 else print("Empty!")
        
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
    