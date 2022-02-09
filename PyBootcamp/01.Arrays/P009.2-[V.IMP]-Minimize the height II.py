'''
Problem Description:
Given an array arr[] denoting heights of N towers and a positive integer K, 
you have to modify the height of each tower either by increasing or decreasing
them by K only once. After modifying, height should be a non-negative integer. 
Find out the minimum possible difference of the height of shortest and longest 
towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease (if possible) by K to each tower.

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
    
    # Method 1 : Failed
    def getMinDiffV1(self, arr, n, k):
        for i in range(n):
            if(arr[i] < k):
                arr[i] += k
            else:
                arr[i] -= k

        return max(arr)-min


    # Method 2 : O(nlogn)
    def getMinDiff(self,nums, n, k):
        nums = sorted(nums)
        mini,maxi = nums[0],nums[n-1]
        diff = nums[n-1]-nums[0]
        for i in range(1,n):
            if(nums[i] >= k):
                maxi = max(nums[i-1]+k,nums[n-1]-k)     
                mini = min(nums[i]-k,nums[0]+k)
                diff = min(diff, maxi-mini)

        return diff


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
    