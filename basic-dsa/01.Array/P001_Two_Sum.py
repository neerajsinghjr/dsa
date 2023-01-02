'''
-------------------------------------------------------------------------------------
-> Problem Title: 1. Two Sum
-> Problem Status: Completed
-> Problem Attempted: 01-12-2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time
complexity?
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        atype: list ~nums
        atype: int ~target
        rtype: list ~result 
        """
        n = len(nums)
        if n <= 2:
            return [0,1] if sum(nums) == target else []

        # return self.ansv1(nums, target, n)
        return self.ansv2(nums, target, n)
        # return self.ansv3(nums, target, n)
    

    def ansv3(self, nums, target, n):
        """
        _run: accpeted
        _code: optimised, time: o(n) and space: o(n)
        _choke: 
        _study: here set is used, refer ansv2() explanation for more.
        """
        mapped = set()
        for key,value in enumerate(nums):
            leftover_sum = target - value
            if(leftover_sum in mapped):
                return [key, nums.index(leftover_sum)]
            mapped.add(value)
        
        return []


    def ansv2(self, nums, target, n):
        """
        _run: accepted
        _code: optimised, time : o(n) and space: o(n)
        _choke: none
        _study: simple approach as we traversing forward through the
        nums array. Then at every step we are storing the current number
        in dictionary with the index.
        Same we are storing value with index and also finding the 
        difference of required sum in that dictionary.        
        """
        mapped = {}
        for key,value in enumerate(nums):
            leftover_sum = target - value
            if(leftover_sum in mapped):
                return [key, mapped[leftover_sum]]
            mapped[value] = key
            
        return []


    def ansv1(self, nums, target, n):
        """
        _run: accepted
        _code: brute force(2 pointer approach), time: o(nlogn) and space: o(n);
        _choke: 
        i) 2 pointer will not work unless untill you map every single number 
        with their index, will cause extra space;
        ii) in this question, actual answer index doesn't matter otherwise 
        this will cause another choke point.
        iii) if the requirement for this solution is give 
        _study: simple approach, we 've created another sorted_nums array and
        then implement the 2 pointer apporoach over it and then when we found the
        requirement number then we have find out the index of duplets from original
        array.
        """
        sorted_nums = sorted(nums)
        start,end = 0,n-1
        while(start <= end):
            cur_sum = sorted_nums[start] + sorted_nums[end]
            if(cur_sum == target):
                start_index = nums.index(sorted_nums[start])
                end_index = nums.index(sorted_nums[end])
                # Check if start_index and end_index is same;
                if(start_index == end_index):
                    nums[start_index] = 'x'
                    end_index = nums.index(sorted_nums[end])
                return [start_index, end_index]
            elif(cur_sum > target):
                end = end - 1
            elif(cur_sum < target):
                start = start + 1
        
        return []   


##---Main Execution;;
def main(res=None):
    try:
    	data = []				
        obj = Solution()	
        res = None
        print(f"Result: {res}") if res else print("Empty!")
        
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
    