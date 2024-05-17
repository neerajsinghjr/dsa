'''
-------------------------------------------------------------------------------------
-> Problem Title: 71. Simplify Path
-> Problem Status: Completed
-> Problem Attempted: 2024-05-15
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/simplify-path/description/

Reference:-
https://youtu.be/qYlHrAKJfyA

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

    def simplifyPath(self, path: str) -> str:
        """
        _stdin:
            arg1: __str__
        _stdout: __str__
        """
        # return self.ansv1(path)
        return self.ansv2(path)

    def ansv2(self, path):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- tricky ---
        [+] we have appended an exta forward slash at the end of the path to keep
        track for every folder name in between the two forward slashes.
        --- constaints ---
        [+] '/' : redundant forward slash
        [+] '..': one directory up
        [+] '.' : current directory simply ignore
        --- explanantion ---
        [+] we are using two variable cur, stack in the solution where $cur will
        trace the folder name in between the '/' slash and $stack will store the
        folder inside the stack.
        [+] then, we are using the for loop for iterating over the path and store
        the folder name inside the $cur variable.
        [+] as soon as we reached the forward slash while iterating over the current
        folder then we check for our predefined constraints and on the basis of we
        either push or pop the folder name from the stack.
        """
        cur = ''
        stack = []

        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ''  # reset cur for next folder;;
            else:
                cur += c

        return '/' + '/'.join(stack)

    def ansv1(self, path):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- constaints ---
        [+] '/' : redundant forward slash
        [+] '..': one directory up
        [+] '.' : current directory simply ignore
        --- explanation ---
        [+] here we are using the splitted path variable and splitting over the forward
        slash, then iterating over the loop.
        [+] if path is '..' then popping from the stack else appending the path to our
        stack variable.
        [+] at the end, we iterate over the stack and generate the path
        """
        stack = []
        path_split = path.split('/')

        for path in path_split:
            if path == '..':
                if stack:
                    stack.pop()
            elif path != '' and path != '.':
                stack.append(path)

        return '/' + "/".join(stack)


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
