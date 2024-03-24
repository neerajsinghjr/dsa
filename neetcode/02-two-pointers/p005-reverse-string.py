'''
-------------------------------------------------------------------------------------
-> Problem Title: 344. Reverse String
-> Problem Status: Completed
-> Problem Attempted: 2024-03-19
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/reverse-string/description/

Reference:-
https://youtu.be/P1Ic85RarKY

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
    def reverseString(self, s: List[str]) -> None:
        """
        _stdin: str
        _stdout: str
        """
        # Do not return anything, modify s in-place instead.
        return self.ansv1(s)

    def ansv1(self, s):
        """
        _run: accepted (brute-force)
        _code: time: o(n), space: o(n)
        _study:
        --- intution ---
        [+] use two pointer variable namely `start` and `end` i.e, `start`
        will run from start of the string and similarly `end` from end.
        [+] at which loop iterative both variable gonna swipe the value of
        itself with one another.
        """
        start, end = 0, len(s) - 1
        while (start <= end):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
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
