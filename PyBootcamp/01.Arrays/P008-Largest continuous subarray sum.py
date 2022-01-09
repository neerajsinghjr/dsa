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


## Main Working Function, here...
class Solution:

    # Method 1 : Kadane Algorithms ~ O(n)
    def maxSubArraySumV1(self,arr,size):
        arrsum = temp = arr[0]
        for i in range(1,size):
            if(temp < 0):   
                temp = 0
            temp += arr[i]
            arrsum = max(arrsum, temp)
        return arrsum
           
    # Method 2 : General Approach
    def maxSubArraySumV2(self,arr):
        maxSum = -1e8
        for i in range(0, len(arr)):
            currSum = 0
            for j in range(i,len(arr)):
                currSum = currSum + arr[j]
                if(currSum > maxSum):
                   maxSum = currSum
        return maxSum


def main():
    try:
        datum = [
            [1,2,3,-2,5,7,4,-2,1,-5,-10,-11],
            [-11,-3,-2,-5,-10,-12,-1],
        ]
        obj = Solution()
        for data in datum:
            res = obj.maxSubArraySumV1(data,len(data))
            # res = obj.maxSubArraySumV2(data)
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
    