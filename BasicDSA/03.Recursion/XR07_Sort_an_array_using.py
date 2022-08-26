'''
Problem Description:
Sort an array using recursion only
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
    def sortArray(self, nums):
        if(len(nums) <= 1):
            return nums
        if(len(nums) == 2):
            return ([nums[0],num[1]] if(nums[0]<=nums[1]) else [nums[1],nums[0]])
        
        return self.sort(nums)
    
    
    def sort(self,nums):
        # Base Condition
        if(len(nums) <= 1):
            return nums
        
        # Hypothesis
        temp = nums.pop()
        self.sort(nums)
        
        # Induction
        self.insert(nums,temp)
        
        return nums
    
    
    def insert(self,nums,temp,pop=None):
        size = len(nums)
        # nums size is 0, simply append ;
        if(len(nums) == 0):
            return nums.append(temp)
        # temp is greater than last index value;
        elif(nums[size-1] < temp):
            return nums.append(temp)
        pop = nums.pop()
        self.insert(nums,temp,pop)
        nums.append(pop)
        
        return nums


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
    

