'''
-------------------------------------------------------------------------------------
-> Problem Title: 167. Two Sum II - Input Array Is Sorted
-> Problem Status: Completed
-> Problem Attempted: 2024-03-
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Reference:-
https://youtu.be/cQ1Oz4ckceM

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

    def twoSum(self, nums: List[int], x: int) -> List[int]:
        """
        _stdin:
            arg1: list[int]
            arg2: int
        _stdout: list[int]
        """
        # return self.ansv1(nums, x)
        return self.ansv2(nums, x)

    def ansv2(self, nums, x):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- constraints ---
        [+] nums are in sorted order
        --- explanation ---
        [+] this apporach comprises of two pointer approach.
        [+] two pointer $lo and $hi, where nums[lo] + nums[hi] is greater than the
        target_sum then reduce the hi pointer.
        [+] if the nums[lo] + nums[hi] < target_sum then increment the lo pointer
        [+] otherwise the nums[lo] + nums[hi] is equals to target_sum then index.
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            cur_x = nums[lo] + nums[hi]
            if cur_x < x:
                lo += 1
            elif cur_x > x:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
        return

    def ansv1(self, nums, x):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- constraints ---
        [+] nums are sorted in order, which we will gonna use it
        --- explanation ---
        [+] this apporach comprises of hashmap, just like the ordinary two sum.
        [+] where we iterate over the loop and find the needed sum by subtracting
        the target_sum with the cur_index number.
        [+] if the needed_sum is found in hashmap then return the index well
        [+] otherwise iterate forward and look again.
        """
        idx = 0
        hashmap = {}
        for idx, val in enumerate(nums):
            needed = x - val
            if needed in hashmap:
                return [hashmap[needed], idx + 1]
            else:
                hashmap[val] = idx + 1

        return


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
