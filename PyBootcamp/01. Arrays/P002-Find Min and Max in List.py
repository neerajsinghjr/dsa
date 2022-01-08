'''
Problem Description: Find min and max of an array.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


# Method 1 : Linear Approach
def minAndMaxOfArray(nums):
    minNum = maxNum = 0
    # base case : size is 1
    if(len(nums) == 1):
        minNum = maxNum = nums[0]
        return (minNum, maxNum)

    # base case : size is 2
    if(len(nums) == 2):
        minNum, maxNum = nums[0], nums[1]
        if(nums[0] > nums[1]):
            minNum, maxNum = nums[1], nums[0]
        return (minNum, maxNum)

    # main case : more than 2
    if nums:
        minNum = maxNum = nums[0]
        for num in nums:
            if(num < minNum):
                minNum = num
            if(num > maxNum):
                maxNum = num

    return (minNum,maxNum)


# Method 2 : Divide and Conquer Technique;
def minAndMaxOfArrayV2(arr,low,high):
    
    # Base Case : array size 1;
    if(low == high):
        arrMin = arrMax = arr[low]
        return (arrMin, arrMax)

    # Base Case : array size 2;
    if(high == low+1):
        arrMin, arrMax = arr[low], arr[high]
        if(arrMin > arrMax):
            arrMin, arrMax = arrMax, arrMin
        return (arrMin, arrMax)
    
    # Main Case : array size greater than 2;
    if(high > low+1):
        mid = int((low+high)/2)
        minNum1, maxNum1 = minAndMaxOfArrayV2(arr,low,mid)
        minNum2, maxNum2 = minAndMaxOfArrayV2(arr,mid+1,high)
        return (min(minNum1,minNum2),max(maxNum1,maxNum2))


def main():
    try:
        data = [12,13,23,41,41,12,14,14,12,14,34,10,212,40,12,124,140,124,12,121,241,212,440]
        # res = minAndMaxOfArray(data)
        res = minAndMaxOfArrayV2(data,low=0,high=len(data)-1)
        print(res) if res else print("Empty!")
        
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
    