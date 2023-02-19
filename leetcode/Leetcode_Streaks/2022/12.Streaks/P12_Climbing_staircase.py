'''
-------------------------------------------------------------------------------------
-> Problem Title: 70. Climbing Stairs
-> Problem Status: Completed
-> Problem Attempted: 12-12-2022
-> Problem Description: 
-------------------------------------------------------------------------------------

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

from collections import defaultdict

class Solution:

    def climbStairs(self, n: int) -> int:
        """
        atype: int (number of steps)
        rtype: int (ways to climb staircase)
        """
        if n == 1: 
            return 1
        if n == 2:
            return 2
        
        # return self.ansv1(n)
        return self.ansv2(n)
    
    def ansv2(self, n):
        """
        _run: accepted
        _code: optimised | time: o(n) | space: o(n) + stack(k) 
        _study:
        simple approach, in this solution we 've optimised the 
        solution with the help of memoization.
        """
        dp = defaultdict(int)       # dp memoization;
        def hop(n):
            if(n == 0 or n == 1):
                return 1
            if not(n in dp):
                dp[n] += hop(n-1) + hop(n-2)

            return dp[n]
            
        return hop(n)

    def ansv1(self, n):
        """
        _run: accepted
        _code: pythonic | time: o(n) | space: O(1) + stack(n)
        _study:
        simple recursive loop checking for 
        """
        @lru_cache(None)
        def hop(n):
            if(n == 0 or n == 1):
                return 1
            return hop(n-1) + hop(n-2)
            
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
    