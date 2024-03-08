'''
-------------------------------------------------------------------------------------
-> Problem Title: 1822. Sign of the Product of an Array
-> Problem Status: Completed
-> Problem Attempted: 2024-03-08
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

Reference:-
https://youtu.be/ILDLM86jNow

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
    def arraySign(self, nums: List[int]) -> int:
        return self.ansv1(nums)

    def ansv1(self, nums):
        """
        run: accepted:
        _code: time: o(n), space: o(1)
        _choke: none
        _study: simple count the negative sign in nums only.
        if count is even then 1 else -1
        """
        minus = 0
        for n in nums:
            if n < 0:
                minus += 1
            elif n == 0:
                return 0

        return 1 if minus % 2 == 0 else -1


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
