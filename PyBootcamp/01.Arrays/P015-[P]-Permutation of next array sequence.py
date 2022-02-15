'''
#Problem Description:
A permutation of an array of integers is an arrangement of its members 
into a sequence or linear order.

For example, for arr = [1,2,3], 
the following are considered permutations of arr: 
[1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically 
greater permutation of its integer. More formally, if all the permutations 
of the array are sorted in one container according to their lexicographical 
order, then the next permutation of that array is the permutation that follows 
it in the sorted container. If such arrangement is not possible, the array must 
be rearranged as the lowest possible order (i.e., sorted in ascending order).


'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:
    
    def nextPermutationV1(self, nums):
        size = len(nums)-1
        # base case;
        if(size == 1):
            return nums
        
        # main case;
        lastPeak = -1               # Last Peak Index;
        # Step 1: Finding High Peak From The End;
        for i in range(1,size):
            if(nums[i] > nums[i-1]):
                lastPeak = i
                
        # Step 2: Check For Descending Array;
        if(lastPeak == -1):             # LastPeak Not Found : Descending Nums;
            start, end = 0, size
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return nums
            
        # Step 3: Check Left and Right Value from Last Peak;
        peakWeight = nums[lastPeak]
        j = index = lastPeak
        for j in range(lastPeak, size):
            if(nums[i] > nums[lastPeak-1] and nums[j] < nums[index]):
                index = i
        
        # Step 4: Swap the Peak Value and Reverse Right End;
        nums[lastPeak], nums[lastPeak-1] = nums[lastPeak-1], nums[lastPeak]
        start, end = lastPeak, size
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums


    def nextPermutationV2(self, nums):
        N = len(nums)
        if N == 1: return
        for i in range(N-1,-1,-1): #trace from back to front 
            if nums[i-1] < nums[i]: # find the first nums[i-1] < nums[i] (non-decreasing)
                break
        if i == 0:
            nums[0:] = nums[0:][::-1]
            # note that nums = nums[::-1] will not modify elements except create a new list
            # so we can use nums[0:] = nums[0:][::-1]        
        i-=1
        # swap nums[i-1] with the next order number in nums[i:]
        comp = nums[i]
        for j in range(N-1,-1,-1):
            if nums[j] > comp: 
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                break
        # reverse nums[i+1:]
        nums[i+1:] = nums[i+1:][::-1]
        return nums
    
def main():
    try:
        nums = [1,2,3]
        obj = Solution()
        res = obj.nextPermutationV1(nums)
        print(res) if res else print("Empty!")
        res = obj.nextPermutationV2(nums)
        print(res,nums) if res else print("Empty!")
        
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
    