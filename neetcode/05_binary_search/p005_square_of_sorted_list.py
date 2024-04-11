'''
-------------------------------------------------------------------------------------
-> Problem Title: 977. Squares of a Sorted Array
-> Problem Status: Completed
-> Problem Attempted: 2024-03-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Reference:-
https://youtu.be/FPCZsG_AkUg

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

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        _stdin: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        return self.ansv1(nums, n)

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- constraints ---
        [+] nums are in sorted form that's the classic of this question
        --- explanation ---
        [+] tricky part here is that if you're taking the absolute of a number
        then you can easily apply the two pointer in this approach.
        [+] take two pointer $lo and $hi and whoever absolute is higer then
        store the square of that number in the new list in the reverse order.
        """
        lo, hi = 0, n - 1
        sqr = [0 for i in range(n)]
        while lo <= hi:
            if abs(nums[lo]) < abs(nums[hi]):
                sqr[n - 1] = nums[hi] * nums[hi]
                hi = hi - 1
            else:
                sqr[n - 1] = nums[lo] * nums[lo]
                lo = lo + 1
            # `n` global index for storing value in `sqr` list from end;;
            n = n - 1

        return sqr


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
