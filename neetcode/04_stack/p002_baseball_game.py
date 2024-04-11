'''
-------------------------------------------------------------------------------------
-> Problem Title: 682. Baseball Game
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/baseball-game/description/

Reference:-
https://youtu.be/Id_tqGdsZQI

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

    def calPoints(self, ops: List[str]) -> int:
        """
        _stdin: list[str]
        _stdout: int
        """
        n = len(ops)
        if n == 1:
            return int(ops[0])

        return self.ansv1(ops, n)

    def ansv1(self, ops, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- stack ---
        because in stack i can traverse back at the last index of the value
        easily. all the respective operation are supposed to implemented from
        the end only.
        --- choke ---
        alway make sure to return the sum at the end of the result because we
        are cumulating the sum anywhere.
        --- explanation ---
        [+] stack preferred for handling the operation
        [+] taken action as per the pre-requisite constraints in problem.

        """
        stack = []
        for op in ops:
            if op == 'C' and stack:
                # Invalidate the previous score, removing it from the record.
                stack.pop()
            elif op == 'D' and stack:
                # Record a new score that is the double of the previous score.
                stack.append(2 * stack[-1])
            elif op == '+' and stack:
                # Record a new score that is the sum of the previous two scores.
                stack.append(stack[-1] + stack[-2])
            else:
                # Save the record in the stack space.
                stack.append(int(op))

        # need to handle case with no operation;;
        return sum(stack) if stack else 0


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
