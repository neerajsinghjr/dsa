'''
-------------------------------------------------------------------------------------
-> Problem Title: 225. Implement Stack using Queues
-> Problem Status: Completed
-> Problem Attempted: 2024-03-25
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/implement-stack-using-queues/description/

Reference:-
https://youtu.be/rW4vm0-DLYc

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
class MyStack:
    """
    _run: accepted
    _code: time: o(n), space: (1)
    _study:
    --- fix from ansv1() ---
    its is accepted though, but its not a stack implementation usings the queues...
    for eg, nums = [1,2,3]
    stack  => [1,2,3] as per LIFO 3 will be at the top pointer
    queue => [3,2,1] as per FIFO 1 will be at the top pointer.
    --- deque ---
    [+] when we are using deque and when we are asked to pop the element then
    we are removing the element from start and pushing it back to end of deque
    till the time we have reached the last element.
    [+] as soon as we have reached the last element then we popped it.
    """

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # iterativly remove element from start and pushing it to
        # end of deque till, we have found the last element of list.
        for i in range(len(self.stack) - 1):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


class MyStackV1:
    """
    _run: accepted
    _code: time: o(n), space: (1)
    _study:
    --- choke ---
    its is accepted though, but its not a stack implementation usings the queues...
    for eg, nums = [1,2,3]
    stack  => [1,2,3] as per LIFO 3 will be at the top pointer
    queue => [3,2,1] as per FIFO 1 will be at the top pointer.
    fix in the ansv2()
    --- explanation ---
    [+] as per the constraints, 100 operation is permitted.
    [+] to create stack, uses list internally where index is maintain using a pointer.
    """

    def __init__(self):
        self.idx = -1
        self.stack = [0 for i in range(100)]

    def push(self, x: int) -> None:
        self.idx += 1
        self.stack[self.idx] = x

    def pop(self) -> int:
        item = None
        if not self.empty():
            item = self.stack[self.idx]
            self.idx -= 1
        return item

    def top(self) -> int:
        if not self.empty():
            return self.stack[self.idx]

    def empty(self) -> bool:
        if self.idx < 0:
            return True
        return False


##---Main Execution;;
def main(res=None):
    try:
        # Your MyStack object will be instantiated and called as such:
        x = random.randint(1000, 9999)
        obj = MyStack()
        obj.push(x)
        param_2 = obj.pop()
        param_3 = obj.top()
        param_4 = obj.empty()

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
