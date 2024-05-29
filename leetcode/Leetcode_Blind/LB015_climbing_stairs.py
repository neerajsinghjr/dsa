'''
-------------------------------------------------------------------------------------
-> Problem Title: 70. Climbing Stairs
-> Problem Status: Completed
-> Problem Attempted: 2024-05-28
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/climbing-stairs/description/

Reference:-
https://youtu.be/Y0lT9Fck7qI?si=E2RcxDXQDpR5Koda

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

    def climbStairs(self, n: int) -> int:
        """
        _stdin:
            arg1: n: __int__
        _stdout: __int__
        """
        # return self.ansv1(n)
        return self.ansv2(n)

    def ansv2(self, n):
        """
        _run: accepted
        _code: ts: o(n), sc: o(1)
        _study:
        --- problem ---
        [+] You are climbing a staircase. It takes n steps to reach the top. Each time
        you can either climb 1 step or 2 steps.
        [+] In how many distinct ways can you climb to the top ?
        --- problem brief ---
        [+] Let's break down the problem with some examples:
            [-] if n == 1, there is only 1 way to climb the staircase (just take 1 step)
            [-] if n == 2, there are 2 ways to climb the staircase:
            (1 step + 1 step) or (2 steps).
        [+] For larger n, you can think about the last step you take to reach the top.
            If you're at step 𝑖, you could have gotten there either from step i−1 (by taking
            1 step) or from step i−2 (by taking 2 steps).
        [+] Therefore, the total number of ways to reach step i step, is the sum of the number
            of ways to reach step i-1 and the number of ways to reach step i−2.
        [+] The observations is like this,
            ways(i) = ways(i-1) + ways(i-2)
        --- explanation ---
        [+] Base Case Check: If n is 1 or less, return 1 because there's only one way to
            reach step 0 or step 1.
        [+] Initialization: Initialize prev1 and prev2 to 1, representing the number of ways
            to reach step 1 and step 0, respectively.
        [+] Iterative Calculation: For each step from 2 to n, calculate the current number of
            ways as the sum of the ways to reach the previous two steps (prev1 and prev2).
        [+] Update prev2 to prev1 and prev1 to the current number of ways.
        """
        prev1, prev2 = 1, 1
        for i in range(n - 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1

    def ansv1(self, n):
        """
        _run: accepted
        _code: ts: o(n), sc: o(n)
        _study:
        --- explanation ---
        [+] refer ansv3() for better explanation
        """

        @lru_cache(None)
        def hop(n):
            if (n == 0 or n == 1):
                return 1
            return hop(n - 1) + hop(n - 2)

        return hop(n)


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
