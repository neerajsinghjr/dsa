'''
#Problem Title: Triplet Sum
#Problem Attempted: 26/07/2022
#Problem Description: 
Given an array containgin 'N' integer and an number 'S' denoting a target sum.

Find all the distinct integer that can add up to form target sum. The network in each triplet should be ordered
in ascending order, and triplets should be ordered too.

Return empty array if no such triplet exists.


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
    
    def getAllTriplets(self,nums,target):
        if not(nums or len(nums) == 2):
            return []

        if(len(nums) == 3):
            if(sum(nums) == target):
                return [nums]
            else:
                return []

        return self.ansv1(nums,target,len(nums))


    def ansv1(self,nums,target,size):
        res = []
        nums.sort() 
        for i in range(0,size):
            reqSum = target - nums[i]
            start = i + 1
            end = size - 1
            while(start < end):
                curSum = nums[start] + nums[end]
                if(curSum == reqSum):
                    triplet = [nums[i],nums[start],nums[end]]
                    if not(triplet in res):
                        res.append(triplet)
                    start += 1
                elif(curSum > reqSum):
                    end -= 1
                elif(curSum < reqSum):
                    start += 1

        return res


def main():
    try:
        data = []               # ~ data
        obj = Solution()
        nums = [1,2,3,4,5,6,7,8,9,15]
        target = 18
        res = obj.getAllTriplets(nums,target)
        if res:
            for r in res:
                print(r)
        
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
    