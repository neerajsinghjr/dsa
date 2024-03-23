'''
-------------------------------------------------------------------------------------
-> Problem Title: 26. Remove Duplicates from Sorted Array
-> Problem Status: Completed
-> Problem Attempted: 2024-03-23
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Reference:-
https://youtu.be/DEJAZBq0FDA

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

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return 1

        return self.ansv1(nums, n)

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- intution ---
        we are tracing the unique integer value iteratively over the loop and
        simultaneously started storing the unique values from the left side of
        the same array.
        """
        last_unique_index = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[last_unique_index] = nums[i]
                last_unique_index += 1

        return last_unique_index


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
