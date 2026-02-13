'''
-------------------------------------------------------------------------------------
-> Problem Title: 1051. Height Checker
-> Problem Status: Completed
-> Problem Attempted: 18/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/height-checker/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:
    
    def heightChecker(self, nums: List[int]) -> int:
        """
        _stdin: 
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return 0
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        return self._ansv3(nums, n)

    def _ansv3(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (code-level-optimization)
        _code: tc: o(n), sc: o(n), rt: 0ms, tcz: 81/81
        _choke: none
        _brief: --- python level optimization only --- 
        - key factor observed is that we can have only 100 elements and nums[i] <= 100
        - keeping this fact in mind, we can avoid _ansv2() sorting requirement and use
        counting sort which can help us with o(n) time complexity same as space. 
        """
        count, idx = 0, 0
        freq_map = collections.Counter(nums) 
        for exp_height in range(101):
            freq_count = freq_map.get(exp_height)
            while freq_count:
                if nums[idx] != exp_height:
                    count += 1
                freq_count -=1
                idx += 1
        return count

    def _ansv2(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (code-level-optimization)
        _code: tc: o(n), sc: o(n), rt: 0ms, tcz: 81/81
        _choke: none
        _brief: --- optimization of previous sort to counting_sort ~ o(n) --- 
        - key factor observed is that we can have only 100 elements and nums[i] <= 100
        - keeping this fact in mind, we can avoid _ansv1() sorting requirement and use
        counting sort which can help us with o(n) time complexity same as space. 
        """
        count = 0
        freq_map = {}
        expected = []
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for idx in range(101):
            val = freq_map.get(idx)
            if val:
                while val:
                    expected.append(idx)
                    val -= 1
        for idx in range(n):
            if expected[idx] != nums[idx]:
                count += 1
        return count

    def _ansv1(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(n), tc: o(n), tcz: 81/81
        _choke: none
        _brief:
        - we calculate the expected string by sorting the existing array and compare every 
        element to each other;;
        - for every mismatch we note the $count
        """
        count = 0
        expected = sorted(nums)
        for idx in range(n):
            count = count+1 if nums[idx] != expected[idx] else count
        return count 


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
