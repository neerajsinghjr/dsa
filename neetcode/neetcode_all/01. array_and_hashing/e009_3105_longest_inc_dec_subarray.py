'''
-------------------------------------------------------------------------------------
-> Problem Title: 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
-> Problem Status: Completed
-> Problem Attempted: 03/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

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

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            # Choke: Either Inc/Dec or can be same;; 
            return 1 if nums[0] == nums[1] else 2

        return self._ansv1(nums, n)
        # return self._ansv2(nums, n)

    def _ansv2(self, nums: List[int], n: int) -> int:
        """
        _run: accepted, rt: 2 ms
        _code: tc: o(n), sc: o(1), rt: nan
        _choke:
        - keep in mind to reset the variable length when you trace any duplicate value one
        after another
        _brief:
        - we keep three variable - max_len, asc_len and des_len. i.e max_len for max length,
        asc_len for increasing variable length and des_len for decreasing variable length.
        - if_constraint: if prev_val < cur_val then asc_len++ & reset des_len to 1
        - elif_constraint: if prev_val > cur_val then des_len++ & reset asc_len to 1
        - else_constraint: reset both variable asc_len and des_len to 1 b'cz its duplicate.
        """
        max_len = 1
        asc_len, des_len = 1, 1
        for idx in range(1, n):
            if nums[idx-1] < nums[idx]:
                asc_len, des_len = asc_len+1, 1
            elif nums[idx-1] > nums[idx]:
                asc_len, des_len = 1, des_len+1
            else:
                asc_len, des_len = 1, 1
            max_len = max(max_len, asc_len, des_len)
        
        return max_len

    def _ansv1(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(k), rt: 1 ms
        _choke: none
        _brief:
        - approach used stack to pull the last element on every iteration thats new only
        - we keep three variable - max_len, asc_len and des_len. i.e max_len for max length,
        asc_len for increasing variable length and des_len for decreasing variable length.
        - if_constraint: if prev_val < cur_val then asc_len++ & reset des_len to 1
        - elif_constraint: if prev_val > cur_val then des_len++ & reset asc_len to 1
        - else_constraint: reset both variable asc_len and des_len to 1 b'cz its duplicate.
        """
        stack = []
        len_mx = 1
        asc_cur, des_cur = 1, 1
        for num in nums:
            while stack:
                if stack[-1] < num:
                    asc_cur, des_cur = asc_cur+1, 1
                elif stack[-1] > num:
                    des_cur, asc_cur = des_cur+1, 1
                else:
                    asc_cur, des_cur = 1, 1
                stack.pop()
            stack.append(num)
            len_mx = max(asc_cur, des_cur, len_mx)
        
        return len_mx


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
