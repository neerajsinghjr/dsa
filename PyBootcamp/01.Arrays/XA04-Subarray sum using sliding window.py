'''
Problem Description:
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# Brute Force Approach
def slidingSubarray_V1(nums,target):
    res,size = [], len(nums)
    for x in range(size):
        maxSum = nums[x]
        for y in range(x+1, size):
            if(maxSum == target):   
                res.append([x,y])
                break
            maxSum += nums[y]
    return res


# Sliding Window Approach
def slidingSubarray_V2(nums,target):
    start = end = 0
    arrSum = nums[0]
    res,size = [],len(nums)
    while(start <= size and end <= size):
        # When target is Found;
        if(arrSum == target):
            res.append([start, end])
            break
        
        # Case: When 'start' surpass 'end' pointer;
        elif(start > end):
            end = start
            arrSum = nums[start]     # reset arrSum, earlier items doesnt satisfy target;
            
        # Case: When Sum is greater than Target;
        elif(arrSum > target):
            arrSum -= nums[start]
            start += 1

        # Case: When Sum is Smaller than Target;
        elif(arrSum < target):
            if (end == size):       # Check for end of array;
                break
            end += 1
            arrSum += nums[end]
    return res
        


def main():
    try:
        data = [5,23,3,1,7,6,3,2,3]               # ~ data
        # data = [5,3,1,7,6,24,2,22,3]               # ~ data
        # res1 = slidingSubarray_V1(data, target=14)
        # print(res1) if res1 else print("Empty!")
        res2 = slidingSubarray_V2(data,target=14)
        print(res2) if res2 else print("Empty!")
        
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
    