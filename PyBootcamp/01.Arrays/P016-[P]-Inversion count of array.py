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


class Solution:
    
    # Method 1: Brute Force
    def inversionCountV1(self, nums):
        count, size = 0,len(nums)
        for i in range(size):
            for j in range(i+1,size):
                if(nums[i]>nums[j]):
                    count += 1
        return count


    # Method 2: Optimised Approach
    def inversionCountV2(self, nums):
        # base case
        if not nums: return nums

        # main case 
        count = self.mergeSort(nums)
        return count


    def mergeSort(self, nums):
        size = len(nums)-1
        low = high = count = 0
        if(low < high):
            mid = low + (high-low)//2
            count += self.mergeSort(nums,low,mid)
            count += self.mergeSort(nums,mid,high)
            count += self.merge(nums,low,mid,high)
        return count


    def merge(self,nums,low,high):
        temp = [0]*len(nums)
        


def main():
    try:
        data = [
            [2, 4, 1, 3, 5],
            [2, 3, 0, 4, 5, 6],
            [10, 10, 10],
        ]             
        obj = Solution()
        for d in data:
            res1 = obj.inversionCountV1(d)               # Brute Force
            res2 = obj.inversionCountV2(d)
            print(res1) if res2 != None else print("Empty!")
            print(res1) if res2 != None else print("Empty!")
        
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
    