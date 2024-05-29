'''
-------------------------------------------------------------------------------------
-> Problem Title: 338. Counting Bits
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/counting-bits/description/

Reference:-
https://youtu.be/RyBM56RIWrM?si=Gk8_4xv07-4aFlro

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

    def countBits(self, n: int) -> List[int]:
        """
        _stdin:
            arg1: n : __int__
        _stdout: list[int]
        """
        # return self.ansv1(n)
        return self.ansv2(n)

    def ansv2(self, n):
        """
        _run: accepted
        _code: ts: o(n), sc: o(n)
        _study:
        --- explanation ---
        [+] here we are using the DP approach to store the previous calculated record in our
        result and on the basis of current resultset we calculate the upcoming resultset.
        [+] we are storing 0 as the default and +1 for incrementing on every iteration
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i - offset] + 1

        return dp

    def ansv1(self, n):
        """
        _run: brute-force
        _code: ts: o(n*k), sc: o(1)
        _study:
        --- explanation ---
        [+] we are iterating two nest loop. outer loop keep the iterative over i from 0 to n
        and the inner loop count the 1's bit each time.
        """
        i = 0
        res = []

        while (i <= n):
            count = self._get_count(i)
            res.append(count)
            i += 1

        return res

    def _get_count(self, num):
        """ helper count to return count """
        count = 0
        while num:
            num = num & (num - 1)
            count += 1
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
