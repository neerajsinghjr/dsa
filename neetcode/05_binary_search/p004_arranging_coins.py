'''
-------------------------------------------------------------------------------------
-> Problem Title: 441. Arranging Coins
-> Problem Status: Completed
-> Problem Attempted: 2024-03-28
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/arranging-coins/description/

Reference:-
https://youtu.be/5rHz_6s2Buw

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

    def arrangeCoins(self, n: int) -> int:
        """
        _stdin: int
        _stdout: int
        """
        return self.ansv1(n)

    def ansv1(self, n):
        """
        _run: accepted
        _code: time: o(n), space; o(1)
        _study:
        --- approach ---
        decrementing the coins as per the row values and finally return the rows
        """
        row = 1
        while (n > 0):
            n = n - row
            if not n < 0:
                row += 1
        return row - 1


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
