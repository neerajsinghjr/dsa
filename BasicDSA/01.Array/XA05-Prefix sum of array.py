'''
Problem Description:
Calculate the prefix sum of subarray which is equals to zero

Example 1:
Input : [-1,2,1,-4,2,3,-1,2]
Output : [[0,4],[3,6]] ~ index
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# Brute Force Approach ~ O(n^2)
def prefixSumV1(nums):
    res,size = [],len(nums)
    for x in range (size):
        arrSum = nums[x]
        for y in range(x+1,size):
            arrSum += nums[y]
            if(arrSum == 0):
                res.append([x,y])
                break
    return res


# Optimised Approach 
def prefixSumV2(nums):                      ## Output : [[0, 4], [3, 6]]
    arrSum, res, store = 0, [], {}
    for (key,value) in enumerate(nums):
        arrSum += value
        print("value: ", value, "arrSum: ", arrSum)
        print("res:", res)
        if(arrSum == 0):
            res.append([0,key])
        else:
            if(value in store.keys()):
                print("value:",value)
                print("store:", store)
                res.append([store[sum]+1, key])
            else:
                store[value] = key
    return res


def main():
    # try:
    # data = [1,-2,-3,4,-7,5,1,1,3,4,5,-6]
    data = [-1,2,1,-4,2,3,-1,2]                  
    res1 = prefixSumV1(data)         # Brute Force;
    print(res1) if res1 else print("Empty!")
    # res2 = prefixSumV2(data)           # Prefix Sum
    # print(res2) if res2 else print("Empty!")
        
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
    