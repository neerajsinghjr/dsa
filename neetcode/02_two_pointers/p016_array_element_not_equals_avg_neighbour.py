'''
-------------------------------------------------------------------------------------
-> Problem Title: 1968. Array With Elements Not Equal to Average of Neighbors
-> Problem Status: Completed
-> Problem Attempted: 2024-04-14
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/

Reference:-
https://youtu.be/Wmb3YdVYfqM

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

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        _stdin:
            args1: list[int]
        _stdout: list[int]
        """
        # return self.ansv1(nums)
        return self.ansv2(nums)


    def ansv1(self, nums):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- explanation ---
        """
        nums.sort()

        i, j, n = 0, 0, len(nums)
        ans = [0]*n

        while i < n and j < n:
            ans[i] = nums[j]
            i = i + 2
            j = j + 1

        i = 1
        while i < n and j < n:
            ans[i] = nums[j]
            i = i + 2
            j = j + 1

        return ans


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
        print("Program C˙ompleted : Success")

    finally:
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
