'''
----------------------------------------------------------------------------------------------------
#Problem Title: Subarray Sort
#Problem Status: Completed
#Problem Attempted: 11-08-2022
#Problem Description:
----------------------------------------------------------------------------------------------------
Given an array of size atleast two, find the smallest subarray that needs to be sorted in place so 
that the entire input array becomes sorted.

If the input array is already sorted, the function should return [-1,-1], otherwise return the start 
and end index of the smallest subarray

for eg,
Input : [1,2,3,4,5,8,6,7,9,10,11]
Output : [5,7]

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from sys import maxsize

## Main Working Function, here...
class Solution:
    
    def subarraySort(self,nums,key=0):
        n = len(nums)

        if(n == 0):
            return [-1,-1]

        if(n == 1):
            return [-1,-1]

        if key == 0:
            return self.ansv1(nums,n)
        else:
            return self.ansv2(nums,n)


    def outOfOrder(self,nums,n,index):
        curValue = nums[index]
        if(index == 0):
            return curValue > nums[1]
        if(index == n-1):
            return curValue < nums[index-1]
        
        return curValue < nums[index-1] or curValue > nums[index+1]


    """
    Approach: Optimized 
    Analysis: Time: O(N) || Space: O(1)
    """
    def ansv2(self,nums,n):     
        
        smallest, largest = maxsize, -maxsize

        for idx in range(n):
            if(self.outOfOrder(nums,n,idx)):
                smallest = min(smallest,idx)
                largest = max(largest,idx)

        if(smallest == maxsize):
            return [-1,-1]

        return [smallest,largest]


    """ 
    Apporach: Brute Force Approach
    Analysis: TIME: O(NxLOGN) + O(N) + O(N) | SPACE: O(N)
    """
    def ansv1(self,nums,n): 
        res = []
        start,end = 0,n-1
        sortedNums = sorted(nums)

        while(start < n):
            if not(nums[start] == sortedNums[start]):
                res.append(start)
                break
            else:
                start = start + 1

        while(end >= 0):
            if not(nums[end] == sortedNums[end]):
                res.append(end)
                break
            else:
                end = end - 1

        if not(res):
            return [-1,-1]

        return res


#--- MAIN EXECUTION ---#
def main():
    try:
        nums = [1,2,3,4,5,8,6,7,9,10,11]            
        # nums = [1,2,3,4,5,6,7,8,9,10,11]   
        # nums = [2,1]   

        obj = Solution()
        res = obj.subarraySort(nums,1)
        print(f"Result: {res}") if res else print("Empty!")
        startTime = time.time()
        endTime = time.time()
        print("Run 1:",endTime-startTime,"ms")


        res = obj.subarraySort(nums,)
        startTime = time.time()
        endTime = time.time()
        print("Run 2:",endTime-startTime,"ms")

        
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
