"""
Return the min difference in element from a sorted array
"""

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
def minDiff(nums,key):
    low,high = 0,len(nums)
    while(low <= high):
        mid = low+(high-low)//2
        if (nums[mid] == key):
            return f"mid:{mid} // {nums[mid]}"
        elif(nums[mid] < key):
            low = mid + 1
        elif(nums[mid] > key):
            high = mid - 1
    else:
        diff1 = abs(key-nums[low])
        diff2 = abs(key-nums[high])
        return f"Diff1:{nums[low]} with diff {diff1}" if diff1 < diff2 else f"Diff2:{nums[high]} with diff {diff2}"
        
    return -1 
            
            
print(minDiff(nums=[7,8,9,10,11,13,14,15,15,81,92,94],key=16))


def main():
    try:
        data = []               # ~ data
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
    