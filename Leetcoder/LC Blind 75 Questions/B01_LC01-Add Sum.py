'''
Problem Description:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they 
add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def twoSum(nums, target):
    i, size = 0,len(nums)
    temp = set()
    while(i<size):
        lookup = target - nums[i]
        if lookup in temp:
            return [i,nums.index(lookup)]
        else:
            temp.add(nums[i])
        i += 1
            
    return []


def main():
    try:
        target,nums = 9,[2,7,11,15]
        res = twoSum(nums,target)
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
    