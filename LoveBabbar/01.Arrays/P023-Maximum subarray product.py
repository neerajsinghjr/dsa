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
    
    def maxProduct(self,nums,n):
        #base case
        if not nums: return nums

        # return self._funcV1(num)
        return self._funcV2(nums, n)


    def _funcV2(self, nums, n):
        res = maxi = mini = nums[0]
        for i in range(1,n):
            if(nums[i] < 0):
                maxi, mini = mini, maxi
            maxi = max(maxi*nums[i], nums[i])
            mini = min(mini*nums[i], nums[i])
            res = max(res,maxi)

        return res 


    # Brute Force ~ O(n^2)
    def _funcV1(self,nums,n):
        # main case
        res = nums[0]
        for x in range(n):
            temp = nums[x]
            for y in range(x+1,n):
                temp *= nums[y]
                res = max(res, temp)
        return res



def main():
    try:
        data = []               # ~ data
        obj = Solution()
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
    