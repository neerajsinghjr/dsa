'''
Problem Description:
Given an array of size n, find all elements in array that appear more than n/k times. For example, 
if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note 
that size of array is 8 (or n = 8), so we need to find all e
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

    # PivotOccurrences
    def morethanNbyK(self, nums, key):
        if not nums: return nums
        # return self.bruteForceSolution(nums, key)
        return self.hashOptimized(nums, key)


    # Hash Optimized Solution : Big O(n) + Bigo(k) ~ o(n)
    def hashOptimized(self, nums, key):
        res = []
        hash = {}
        key = key//len(nums)
        for num in nums:                    # o(n)
            if(num in hash):
                hash[num] += 1
            else:
                hash[num] = 1
        print(hash)
        for (k,v) in hash.items():          # o(k)
            if(v > key):
                res.append(k)
        return res
    

    # Brute Force Solution : Big O(n^2)
    def bruteForceSol1ution(self, nums, key):
        size,res = len(nums),[]
        key = key//size
        for x in range(size):
            count = 1
            for y in range(x+1,size):       
                if(nums[x] == nums[y]):     # count key
                    count += 1
            if(count > key):                # count greater than key
                res.append(nums[x])
                
        return res



def main():
    try:
        nums = [3, 1, 2, 2, 1, 2, 3, 3]
        key = 2
        obj = Solution()
        res = obj.morethanNbyK(nums, key)
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
    