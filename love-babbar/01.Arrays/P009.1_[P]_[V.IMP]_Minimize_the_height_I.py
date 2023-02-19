'''
Problem Description: (Non-Negative Tower Height Included)
Given an array arr[] denoting heights of N towers and a positive integer K, 
you have to modify the height of each tower either by increasing or decreasing
them by K only once. After modifying, height should be a non-negative integer. 
Find out the minimum possible difference of the height of shortest and longest 
towers after you have modified each tower.

Note: Assume that height of the tower can be negative.
A slight modification of the problem can be found here. 

Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.

Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11.
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
    
    def getMinDiff(self, nums, n, k):
        nums = sorted(nums)
        tempMin = nums[0]+k
        tempMax = nums[n-1]-k
        maxi = mini = 0
        ans = tempMax-tempMin
        print(f"")
        for i in range(n-1):
            print("before tempMax:",tempMax,"|",tempMin)
            maxi = max(nums[i-1]+k,tempMax)
            mini = min(nums[i+1]-k,tempMin)
            ans = min(ans,maxi-mini)
            print("after tempMax:",tempMax,"|",tempMin)
            print("ans: ans:",ans)
                    
        return ans


def main():
    try:
        data = [1,2,2,2,3,3,4,6,7,10]
        obj = Solution()
        res = obj.getMinDiff(data,len(data),5)
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
    