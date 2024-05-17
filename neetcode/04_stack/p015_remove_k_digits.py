'''
-------------------------------------------------------------------------------------
-> Problem Title: 402. Remove K Digits
-> Problem Status: Completed
-> Problem Attempted: 2024-0515
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/remove-k-digits/

Reference:-
https://youtu.be/cFabMOnJaq0

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
import sys


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        """
        _stdin:
            arg1: num : __str__
            arg2: k : __int__
        _stdout: __str__
        """
        # return self.ansv1(num, k)
        return self.ansv2(num, k)

    def ansv2(self, nums, k):
        """
        _run: accepted (optimized)
        _code: time: o(n), space: o(n)
        _study: refer ansv1()
        """
        stack = []
        sys.set_int_max_str_digits(100000)  # facing integer version issue;;

        for num in nums:
            while k > 0 and stack and stack[-1] > num:
                stack.pop()
                k = k - 1
            stack.append(num)

        stack = stack[:len(stack) - k]
        res = "".join(stack)

        i = 0
        # iterate over the loop to remove zero prefix;;
        while res and i < len(res) and res[i] == '0':
            i += 1

        return res[i:] if res and i < len(res) else '0'

    def ansv1(self, nums, k):
        """
        _run: brute-force
        _code: time: o(n), space: o(n)
        _study:
        --- error ---
        [+] ValueError: Exceeds the limit (4300 digits) for integer string conversion:
        value has 9001 digits; use sys.set_int_max_str_digits() to increase the limit.
        [+] sys.set_int_max_str_digits(10000)   # facing integer version issue;
        --- explanation ---
        [+] here the approach is also revolving around the Max Significant Digit.
        [+] iteratively we are trying to remove the last MSB digit which is at the top
        of the stack.
        """
        sys.set_int_max_str_digits(100000)  # facing integer version issue;
        stack = []

        for num in nums:
            while k > 0 and stack and stack[-1] > num:
                stack.pop()
                k = k - 1
            stack.append(num)

        stack = stack[:len(stack) - k]
        res = "".join(stack)

        return str(int(res)) if res else '0'


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
