'''
-------------------------------------------------------------------------------------
-> Problem Title: 22. Generate Parentheses
-> Problem Status: Completed
-> Problem Attempted: 2024-04-13
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/generate-parentheses/

Reference:-
https://youtu.be/s9fokUqJ76A

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

    def generateParenthesis(self, n: int) -> List[str]:
        """
        _stdin:
            arg1: int
        _stdout: list[str]
        """
        return self.ansv1(n)

    def ansv1(self, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- explanation ---
        [+] start with an empty string representing the current combination.
        [+] recursively explore all possible combinations by adding opening and closing
        parentheses.
        [+] At each step, we have two choices:
            [a] Add an opening parenthesis if there are still remaining opening parentheses
            to be used.
            [b] Add a closing parenthesis if the number of closing parentheses is less than
            the number of opening parentheses already added.
        [+] Terminate the recursion when the length of the current combination equals 2n or
        when the count of open_bracket count and close_bracket equals to n
        [+] Add the valid combinations to the result list.
        """
        res = []

        def _backtrack(brackets, open_br, close_br):
            # return if the open and close bracket count reached n;;
            # eg, open_br == close_br == n == 3;;
            if open_br == close_br == n:
                res.append(brackets)

            # if count of open_br is lesser than n we can add one more open bracket;;
            if open_br < n:
                _backtrack(brackets + '(', open_br + 1, close_br)

            # we will add close_br only when we have count of open bracket is lesser
            # than close bracket otherwise the parenthesis combination will not valid;;
            if close_br < open_br:
                _backtrack(brackets + ')', open_br, close_br + 1)

        _backtrack("", 0, 0)  # open and close are of 0 length

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
