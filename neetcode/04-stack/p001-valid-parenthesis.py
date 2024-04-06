'''
-------------------------------------------------------------------------------------
-> Problem Title: 20. Valid Parentheses
-> Problem Status: Completed
-> Problem Attempted: 2024-03-25
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/valid-parentheses/description/

Reference:-
https://youtu.be/WTzjTskDFMg

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

    def isValid(self, s: str) -> bool:
        """
        _stdin: str
        _stdout: bool
        """
        n = len(s)
        if n == 1:
            return False
        return self.ansv1(s, n)

    def ansv1(self, s, n):
        """
        _run: accepted
        _code: time:o(n), space: o(n)
        _study:
        --- stack-ds ---
        used stack because
        [+] required a datastructure which can hold a data in a given order
        [+] easily accessible the last input record with single o(1) operation
        [+] IMP: i think of two pointer approach first because 2P would be hard
        to implement. to over 2P approach i use stack here 2P are as follows -
        one_pointer is pointer of for loop which will work normal iteration
        second_pointer is pointing to the top of stack for popping the item
        --- constraints ---
        question wants to check if all the open bracket have respective closing
        bracket in the give order from left to right.
        --- explanation ---
        [+] use stack to keep all the open bracket when iterating over the loop
        [+] as soon as we get any closing bracket then we pop last open bracket
        from stack and check for equality. if not good then return false else go on.
        [+] at the end make sure to check for stack length if its 0 then all good
        otherwise it means there are disparity among closing bracket. There are
        extra open brackets
        """
        stack = []
        ob_map = {'(': ')', '[': ']', '{': '}'}  # ob: open_bracket;;

        for c in s:
            if c in ob_map:
                stack.append(c)
            else:
                # if stack is empty;
                if not len(stack):
                    return False
                last_ob = stack.pop()
                if not c == ob_map.get(last_ob):
                    return False

        return True and len(stack) == 0


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
