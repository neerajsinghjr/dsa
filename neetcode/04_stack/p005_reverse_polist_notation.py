'''
-------------------------------------------------------------------------------------
-> Problem Title: 150. Evaluate Reverse Polish Notation
-> Problem Status: Completed
-> Problem Attempted: 2024-04-11
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Reference:-
https://youtu.be/iu0082c4HDE

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

    def evalRPN(self, tokens: List[str]) -> int:
        """
        _stdin:
            args: list[str]
        _stdout: int
        """
        n = len(tokens)
        if n == 1:
            return int(tokens[0])
        return self.ansv1(tokens)

    def ansv1(self, tokens):
        """
        _run: accepted (brute-force)
        _code: time: o(n), space: (1)
        _study:
        --- constraints ---
        [+] length of tokens can be n i.e, where n == 1 which is only eligible
        in the case where we have only one integer.
        [+] i manually confirmed, if there can be possiblity of tokens like [10, 20]
        --- ds picked ---
        [+] preferred stack because in stack we can track the order of value in a
        particular sequence and we can go down in reverse order very easily in o(1).
        --- explanation ---
        [+] as preferred we are preferring the stack for storing the operands values
        while iterating over the loops.
        [+] as soon as we got any of the operator we pop two operand and do some maths
        and store the value again the same stack as new entry.
        --- key point ---
        [+] when you're popping the values from the stack then first_value you pop and
        second_value you pop then operation woulb be second_value / first_value.
        """
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                # top element would be num2 for below operation;;
                num2, num1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    # dont use // here for integer division because it would failed
                    # to capture the due to its in-build floor rounding mechanism
                    # eg, stack.append(int(num1//num2))
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))

        return stack[-1]


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
