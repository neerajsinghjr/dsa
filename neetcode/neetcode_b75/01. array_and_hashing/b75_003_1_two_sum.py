'''
-------------------------------------------------------------------------------------
-> Problem Title: 1. Two Sum
-> Problem Status: Completed
-> Problem Attempted: 04/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/two-sum/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        if n == 2:
            return [0, 1]
        
        return self._ansv0(nums, target, n)
        # return self._ansv1(nums, target, n)
        # return self._ansv2(nums, target, n)
        # return self._ansv3(nums, target, n)
        # return self._ansv4(nums, target, n)
    
    def _ansv4(self, nums, target, n):
        """
        _run: accpeted
        _code: optimised, tc: o(n), sc: o(n), rt: 0 ms
        _choke: none
        _brief: 
        - here we are using set alone to trace unique encounter of elements from list.
        - code analysis ...
            - for key, value in enumerate(nums) → O(n)
            - leftover_sum in mapped → O(1) average case (set lookup)
            - nums.index(leftover_sum) → O(n) in worst case

        - So, even though the algorithm structure is linear (O(n)), the nums.index() 
        function makes the overall worst-case time complexity: O(n²) in the worst case
        """
        mapped = set()
        for key,value in enumerate(nums):
            leftover_sum = target - value
            if(leftover_sum in mapped):
                return [key, nums.index(leftover_sum)]
            mapped.add(value)
        
        return []

    def _ansv3(self, nums, target, n):
        """
        _run: accepted (~BEST)
        _code: tc: o(n), space: o(n), rt: 0 ms
        _choke:
        - fix choke situtaion by removing abs() method
        _brief:
        - approach starts with as we traversing forward through the nums array. Then at
         every step we are storing the current number in dictionary with the index.
        - same we are storing value with index and also finding the  difference of 
        required sum in that dictionary. 
        """
        hashmap = {}
        for idx, num in enumerate(nums):
            needed = target-num
            if needed in hashmap:
                return [hashmap.get(needed), idx]
            hashmap[num] = idx
        return []
    
    def _ansv2(self, nums, target, n):
        """
        _run: rejected
        _code: tc: o(n), space: o(n), rt: nan
        _choke:
        - dont use abs() function when calculating $needed sum value
        - for eg, input nums=[-3,4,3,90], target=0 || output: [0,2] || expected: [0,2]
        - run time analysis ...
            debug: needed: 3, hashmap: {}
            debug: needed: 4, hashmap: {-3: 0}
            debug: needed: 3, hashmap: {-3: 0, 4: 1}
            debug: needed: 90, hashmap: {-3: 0, 4: 1, 3: 2}
        _brief:
        - approach starts with as we traversing forward through the nums array. Then at
         every step we are storing the current number in dictionary with the index.
        - same we are storing value with index and also finding the  difference of 
        required sum in that dictionary. 
        """
        hashmap = {}
        for idx, num in enumerate(nums):
            needed = abs(target-num) # problem with these line;;
            print(f"debug: needed: {needed}, hashmap: {hashmap}")
            if needed in hashmap:
                print("rt: hashmap: ", hashmap)
                return [hashmap.get(needed), idx]
            hashmap[num] = idx
        return []

    def _ansv1(self, nums, target, n):
        """
        _run: acceped (brute-force)
        _code: tc: o(n^2), sc: o(1), rt: 1746 ms
        _choke: none
        _brief: 
        - using two for loops, first iterate from i-0th index and leading the solution
        - inner loop starts from j(i+1th) index and then adding nums[i]+nums[j]. if sum
        match target then found solution else solution doesnt exist.
        """
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
    
    def _ansv0(self, nums, target, n):
        """
        _run: accepted (brute-force: 2 pointer)
        _code: tc: o(n^2), sc: o(n), rt: 3ms
        _choke: 
        - 2 pointer will not work easy, question ask to return the indices of the nums 
        who makes up to the target sum and using 2 pointers we had to first sort the 
        nums and there we loose the original indices array.
        - for preserving the nums's indices we are pulling original indices by using 
        index() function on every loop's iteration unknowningly o(n^2) 
        _brief: 
        - simple approach, we 've created another sorted_nums array and then implement 
        the 2 pointer apporoach over it.
        - on every iteration, checking left + right indices sum if equals to target then 
        return indices by pulling from original array.
        - if cur_sum is greater than target then reducing window from right else from left.
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
