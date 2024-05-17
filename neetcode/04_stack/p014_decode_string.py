'''
-------------------------------------------------------------------------------------
-> Problem Title: 394. Decode String
-> Problem Status: Completed
-> Problem Attempted: 2024-05-15
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/decode-string/description/

Reference:-
https://youtu.be/qB0zZpBJlh8

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

    def decodeString(self, s: str) -> str:
        """
        _stdin:
            arg1: str
        _stdout: str
        """
        return self.ansv1(s)

    def ansv1(self, encode):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- dsa ---
        [+] stack
        --- choke ---
        [+] case like this
        --- explanation ---
        [+] we are using the stack for storing the encode string in sequential manner
        from left to right until received the closing bracket.
        [+] as soon as we received the closing bracket we start popping the encoded
        character in the reverse fashion untill we recieved the relative open bracket.
        [+] then we again start popping the character from the stack but time for digit
        [+] at the end result we just join the stack values as a compressed string.
        """
        res = ""
        stack = []

        for ec in encode:
            if ec != ']':
                stack.append(ec)
            else:
                num, substr = '', ''
                # s1: popping character from stack;;
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                # s2: remove current open bracket from stack;;
                if stack and stack[-1] == '[':
                    stack.pop()
                # s3: popping digits from stack;;
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * substr)

        return "".join(stack)


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
