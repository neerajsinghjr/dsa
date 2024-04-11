'''
-------------------------------------------------------------------------------------
-> Problem Title: 946. Validate Stack Sequences
-> Problem Status: Completed
-> Problem Attempted: 2024-04-11
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/validate-stack-sequences/description/

Reference:-
https://youtu.be/mzua0r94kb8

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

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        _stdin:
            arg1: list[int]
            arg2: list[int]
        _stdout: bool
        """
        n = len(pushed)
        if n == 1:
            return pushed[0] == popped[0]

        # return self.ansv1(pushed, popped)
        # return self.ansv2(pushed, popped)
        return self.ansv3(pushed, popped)

    def ansv3(self, pushed, popped):
        """
        _run: accepted (code optimize only)
        _code: time: o(n), space: o(n)
        _study:
        ---- explanation ---
        [+] refer explanation in ansv1() or ansv2() for depth
        """
        i = 0  # pointer to popped list
        stack = []
        for val in pushed:
            stack.append(val)

            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i = i + 1

        return not stack

    def ansv2(self, pushed, popped):
        """
        _run: accepted (optimised)
        _code: time: o(n), space: o(n)
        _study:
        --- optimization ---
        [+] the second while loop is not needed because if our $pushed_list match
        $popped_list then this $while loop will never needed.
        [+] if its needed then our $pushed_list != $popped_list, we can directly
        return False.
        --- ds picked ---
        [+] stack is preferred due to order is required for pushing the element onto
        the stack and also the popping pattern should also exactly match.
        [+] for searching a order always try to use stack, otherwise using for loop or
        some 2 pointer approach will dump you into some choked scenario.
        --- explanation ---
        [+] here i used a stack which we will use to push element from the $pushed element
        while iterating over the loop to our custom stack variable.
        [+] we are also using a $pop_idx pointer which is pointing to $popped list default
        will start from 0.
        [+] as soon as for loop starts iterating over the $pushed list and we found out
        ith element match the ith element of $popped list.
        [+] then we start a child loop in which we check for existing top element from our
        custom stack matches the ith + 1 index of $popped list.
        [+] if yes then we popped value from our custom stack and also increase again our
        ith pointer. and check again this process goes on till matches successfull
        [+] if match not success then we are appending the value to our custom stack only.
        """
        stack = []
        pop_idx = 0

        for idx, val in enumerate(pushed):

            if val == popped[pop_idx]:
                # block will take care if current val match poppped array index;;

                pop_idx += 1  # from next pop_idx value;;
                while pop_idx <= len(popped) and stack:
                    # break loop if previous element from stack not matched with
                    # the next pop_idx element;;
                    if popped[pop_idx] != stack[-1]:
                        break
                    stack.pop()
                    pop_idx += 1

            else:

                # block will take care if no match found then push to stack only;;
                stack.append(val)

        # we are expecting if everything match then our stack array should be empty
        # else pushed array != popped array;;
        return True if not stack else False

    def ansv1(self, pushed, popped):
        """
        _run: accepted (brute-force)
        _code: time: o(n), space: o(n)
        _study:
        --- ds picked ---
        [+] stack is preferred due to order is required for pushing the element onto
        the stack and also the popping pattern should also exactly match.
        [+] for searching a order always try to use stack, otherwise using for loop or
        some 2 pointer approach will dump you into some choked scenario.
        --- explanation ---
        [+] here i used a stack which we will use to push element from the $pushed element
        while iterating over the loop to our custom stack variable.
        [+] we are also using a $pop_idx pointer which is pointing to $popped list default
        will start from 0.
        [+] as soon as for loop starts iterating over the $pushed list and we found out
        ith element match the ith element of $popped list.
        [+] then we start a child loop in which we check for existing top element from our
        custom stack matches the ith + 1 index of $popped list.
        [+] if yes then we popped value from our custom stack and also increase again our
        ith pointer. and check again this process goes on till matches successfull
        [+] if match not success then we are appending the value to our custom stack only.
        """
        stack = []
        pop_idx = 0

        for idx, val in enumerate(pushed):

            if val == popped[pop_idx]:
                # block will take care if current val match poppped array index;;

                pop_idx += 1  # from next pop_idx value;;
                while pop_idx <= len(popped) and stack:
                    # break loop if previous element from stack not matched with
                    # the next pop_idx element;;
                    if popped[pop_idx] != stack[-1]:
                        break
                    stack.pop()
                    pop_idx += 1

            else:

                # block will take care if no match found then push to stack only;;
                stack.append(val)

        # Note: Removing the leftover among the popped and stack index;;
        while pop_idx < len(popped) and stack:
            if popped[pop_idx] != stack[-1]:
                return False
            pop_idx += 1
            stack.pop()

        # we are expecting if everything match then our stack array should be empty
        # else pushed array != popped array;;
        return True if not stack else False


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
