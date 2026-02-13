'''
-------------------------------------------------------------------------------------
-> Problem Title: 169. Majority Element
-> Problem Status: Completed
-> Problem Attempted: 25/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/majority-element/description/

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

    def majorityElement(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        # return self._ansv3(nums, n)
        # return self._ansv4(nums, n)
        # return self._ansv5(nums, n)
        return self._ansv6(nums, n)
    
    def _ansv6(self, nums, n):
        """
        _run: accepted (BEST!!!)
        _code: tc: o(n), sc: o(1), rt: 7 ms
        _choke: 
        - There has to be majority element in the list to work.
        _brief: Based on algo --- Boyer Moore ---
        - another way of writing the _ansv5() solution.
        """
        count = 0
        for num in nums:
            candidate = num if count == 0 else candidate
            count += 1 if num == candidate else -1
        return candidate
    
    def _ansv5(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (BEST!!!)
        _code: tc: o(n), sc: o(1), rt: 9 ms
        _choke: 
        - There has to be majority element in the list to work.
        _brief: Based on algo --- Boyer Moore ---
        - There has to be a majority element in the provided list to implement the algorithms. 
        Otherwise it can provide the ambiguous result.
        """
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if res == num else -1

        return res
    
    def _ansv4(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(1), rt: 0 ms
        _choke: none
        _brief: --- assumption here is that the majority element always exists ---
        - the list nums is sorted in ascending order. Sorting helps to bring the 
        majority element in the middle of the sorted list.
        - return nums[n//2]: Since the list is sorted, the majority element will 
        be at the index ⌊n/2⌋ (integer division). 
        - fyi, inside a sorted list the majority element (appearing more than ⌊n/2⌋ 
        times) will have more occurrences than any other element, and hence, it will 
        be positioned at the middle.
        """
        nums.sort()
        return nums[n//2]

    def _ansv3(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (brute-force-code-level-optimization)
        _code: tc: o(n), sc: o (n), rt: 29 ms
        _choke: none
        _brief: 
        - hashmap elements with their occurence and iterative over hashmap and look 
        for majority element.
        """
        limit  = n//2
        hashmap = {}
        res, max_count = 0, 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            res = num if hashmap[num] > max_count else res
            max_count = max(max_count, hashmap[num])

        return res
    
    def _ansv2(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n), rt: 11 ms
        _choke: none
        _brief:
        - hashmap used for mapping each element with its occurences mapping but
        to find the majority element we are using limit which is nothing but
        n//2 where n is the total length of the list.
        """
        n_map = {}
        limit = n // 2
        for num in nums:
            n_map[num] = n_map.get(num, 0) + 1
        for k, v in n_map.items():
            if v > limit:
                max_val = k
        return max_val


    def _ansv1(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n), rt: 5 ms
        _choke: none
        _brief:
        - first loop works for mapping the character with its occurrences
        - second loop we are checking the max occurence with its max value.
        """
        n_map = {}
        max_v = float("-inf")
        max_k = float("-inf")
        for num in nums:
            n_map[num] = n_map.get(num, 0) + 1
        for k, v in n_map.items():
            if v > max_v:
                max_k, max_v = k, v
        return max_k


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
