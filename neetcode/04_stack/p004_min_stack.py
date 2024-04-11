'''
-------------------------------------------------------------------------------------
-> Problem Title: 155. Min Stack
-> Problem Status: Completed
-> Problem Attempted: 2024-04-11
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/min-stack/

Reference:-
https://youtu.be/qkLl7nAwDPo

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
class MinStack:
    """
    _run: accepted (optimal)
    _code: time: o(1), space: o(1) + o(n) for stack only
    _brief:
    --- explanation ---
    [+] approach use a quite clever method for storing the min_value. we map min_val
    from the very start for stack filling.
    [+] whenever there is a value to be added inside the stack then we are also storing
    the min_value at that level only.
    [+] for eg, in stack index 0 is the value and index 1 is the min_value till that point.
    numbers given = [-2, 0, -1, 10, 20, -10]
    inside stack = [
        (-10, 10)
        (20, -1)
        (10, -1)
        (-1, -1)
        (0, 0)
        (-2, -2)
    ]
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            min_val = val
        else:
            min_val = min(val, self.stack[-1][1])
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][1]


class MinStackV1:
    """
    _run: accepted (brute-force)
    _code: time: o(1), space: o(1) + o(n) for stack only
    _brief:
    --- explanation ---
    [+] simple store the stack value inside a list in a stack manner
    [+] getMin() use temporary list which is used to pop value from stack
    and everytime we compare for min_value and store it inside the temp list.
    [+] after stack values got empty then at that we do have a min_value
    [+] before return min_value we dump againt  the temp value into stack variable.
    """

    def __init__(self):
        self.stack = []
        self.idx = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.idx += 1

    def pop(self) -> None:
        self.stack.pop()
        self.idx -= 1

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[self.idx]

    def getMin(self) -> int:
        temp = []
        min_val = None

        if self.stack:
            min_val = self.stack[-1]
            while self.stack:
                cur_val = self.stack.pop()
                temp.append(cur_val)
                min_val = min(min_val, cur_val)
            while temp:
                temp_val = temp.pop()
                self.stack.append(temp_val)

        return min_val


##---Main Execution;;
def main(res=None):
    try:

        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        min_val = minStack.getMin()   # return -3
        print(f"min_val: {min_val}")

        minStack.pop()
        print(">>>>>>> 1")

        minStack.top()  # return 0
        print(">>>>>>> 2")

        min_val = minStack.getMin()   # return -2
        print(f"min_val: {min_val}")

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
