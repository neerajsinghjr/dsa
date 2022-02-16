'''
Problem Description:
Find first occurrence of the target item inside an array;

Example 1:
Input : [1,2,2,3,4,5,5,6,7,8,8,8,9,10], Target : 8
Output : 9 (~index of value : 8)
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# Method 1 : Binary Search in Log(n) Times
def findClosestToTarget(nums, target):
    nearby,size = None,len(nums)            # nearby : None, for start
    low, high = 0,size-1
    # base case;
    if(size == 1):  return nums

    # main case;
    while(low <= high):
        mid = low + (high-low)//2
        nearby = isNearBy(target, nearby, nums[mid])
        if(nums[mid] == target):
            return f"Found Exact : {mid}"
        elif(nums[mid] >= target):
            high = mid - 1
        elif(nums[mid] <= target):
            low = mid + 1

    print(f"@nearby: {nearby}")
    return f"Found Nearby : {nearby}"

def isNearBy(target, nearby, newNearby):
    if nearby == None:                  # Nearby : None, only
        nearby = newNearby
        return nearby

    return min(nearby, newNearby)


def main():
    try:
        nums = [10,20,30,40,50,60,70,80]        
        res1 = findClosestToTarget(nums, target=21)
        print(res1) if res1 else print("Empty!")
        
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
    