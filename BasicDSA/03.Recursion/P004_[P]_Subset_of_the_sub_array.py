'''
Problem Description:
Print all combination of three from given array elements;
eg, 
nums = [1,2,3,4,5,6,7] 
Return : 123,124,125,126,127,234,235,236,237,345,346,347,456,457,567

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

    # __main__
    def subArray(self, nums):
        # base case
        if not nums: return nums

        # main case
        print("Brute Force:")
        self.bruteForce(nums)
        # return self.bruteForce(nums)
        print("\nRecursion: ")
        self.recursion(nums, [0]*3, 0, 0)
        # return self.recursion(nums, [0]*3, 0, 0)


    # Method 2: Recursion using Buffer Management;
    def recursion(self, nums, bufs, numIdx, bufsIdx):
        # BaseCase : When Buffer is Full;
        print(bufs, end=" ")
        if(bufsIdx == 3):   
            return
        
        # BaseCase : When nums reaced ends;
        if(numIdx == len(nums)):    
            return
        
        # MainCase : Loop Iterating
        for idx in range(numIdx, len(nums)-1):
            bufs[bufsIdx] = nums[idx]
            self.recursion(nums, bufs, idx+1, bufsIdx+1)

        return


    # Method 1 : Brute Force Solution ~ BigO(n^3)
    def bruteForce(self, nums):
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                for k in range(j+1, size):
                    print(f"{nums[i]}{nums[j]}{nums[k]}", end = " ")

        return None   


def main():
    try:
        # nums = [1,2,3,4,5,6,7]
        nums = [1,2,3,4,5]
        obj = Solution()
        obj.subArray(nums)
        print(end="\n")
        
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
    