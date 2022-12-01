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
def firstOccurence(nums, target):
    low, high = 0,len(nums)-1
    while(low <= high):
        mid = low + (high-low)//2
        if(nums[mid] == target):
            while(mid > 0):
                if(nums[mid-1] != target):
                    return f"Found: {mid+1}"
                mid = mid - 1    
        elif(nums[mid] >= target):
            print(f"Greater : low:{low}/{nums[low]},high:{high}/{nums[high]}")
            high = mid - 1
        elif(nums[mid] <= target):
            print(f"Smaller : low:{low}/{nums[low]},high:{high}/{nums[high]}")
            low = mid + 1

    return f"Not Found"
    

def main():
    try:
        nums = [1,2,2,3,4,5,5,6,7,8,8,8,9,10]        
        res1 = firstOccurence(nums, target=9)
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
    