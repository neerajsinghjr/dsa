'''
Problem Description:
Given an array of integers, where all elements but one occur twice, find the unique element.
for eg,
nums = [1,2,3,4,3,2,1]
The Unique Element is 4
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def lonelyInteger(nums):
    size = len(nums)
    # base case;
    if(size <= 1):
        return nums[0] if size == 1 else None
        
    # main case
    res, temp = 0, dict()
    for key in nums:
        if key in temp:
            temp.pop(key)
            
            
        else:
            temp[key] = True
        
    res = list(temp.keys())
    return res[0]
    


def main():
    try:
        arrays = [
            [],
            [1,1,2],
            [1,2,3,4,3,2,1]
        ]
        for arr in arrays:
            res = lonelyInteger(arr)
            print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Program Stopped: {e}")
    
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
    