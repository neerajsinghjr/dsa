'''
-------------------------------------------------------------------------------------
-> Problem Title: 739. Daily Temperatures
-> Problem Status: Completed
-> Problem Attempted: 2024-04-14
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/daily-temperatures/description/

Reference:-
https://youtu.be/cTBiBSnjO3c

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

    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]
        """
        n = len(temps)
        if n == 1:
            return [0]

        # return self.ansv1(temps, n)
        return self.ansv2(temps, n)

    def ansv2(self, temps, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- wrong approach ---
        [+] in earlier apporach i used the temperature value to be stored inside the
        stack list. but it was very hard to maintain the days count.
        --- explanation ---
        [+] but in this approach, we are using the index instead of values and popping
        the different of current index with the last_indx from the stack.
        [+] store the respective difference in the result as days and that's it.
        """
        res = [0] * n
        stack = []

        for idx, temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                last_idx = stack.pop()
                res[last_idx] = idx - last_idx

            stack.append(idx)

        return res

    def ansv1(self, temps, n):
        """
        _run: TLE [35/48] (brute-force)
        _code: time: o(n^2), space: o(n)
        _study:
        --- explanation ---
        [+] brute-force approach with nested loop approach where we iterate over the ith index
        and we check for next ith+1 index using the for loop.
        [+] if no warner day found in the upcoming temperature list then add 0 by default.
        """
        res = []

        for i in range(n):
            days = 1
            is_next_warm_day_available = False

            for j in range(i + 1, n):
                if temps[i] < temps[j]:
                    is_next_warm_day_available = True
                    res.append(days)
                    break

                days += 1

            # if next warmer day not found then placed 0 days by default;;
            if not is_next_warm_day_available:
                res.append(0)

        return res


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
