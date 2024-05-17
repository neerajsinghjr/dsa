'''
-------------------------------------------------------------------------------------
-> Problem Title: 456. 132 Pattern
-> Problem Status: Completed
-> Problem Attempted: 2024-05-17
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/132-pattern/description/

Reference:-
https://youtu.be/q5ANAl8Z458

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

    def find132pattern(self, nums: List[int]) -> bool:
        """
        _stdin:
            arg1: nums : __int__
        _stdout: __bool__
        """
        # return self.ansv1(nums)
        return self.ansv2(nums)

    def ansv2(self, nums):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- datastructure ---
        [+] stack is preferred because here as well the order is important.
        --- discussion ---
        [+] here the approach is a bit tricky becasue at the top level view of this
        problem will give you no space to adjust stack datastrucutre in it.
        [+] crux of the problem is we have to look for num[i] < num[k] < num[j], where
        index weightages is like this, i < j < k.
        --- explanation ---
        [+] here we are using the stack to hold a pair which is consist of current stack
        value  with the minimum value so far from past index.
        [+] again we are using a for loop which sequentially iterate over the values and
        as soon as if fetch any value which is greater than the top of the stack. Then we
        start popping values from it. Becasue we dont need it. This value can be a nums[j].
        [+] after popping we check whether we reach num[i] < num[k] < num[j] else we move
        forward with pushing the current value in the stack with the current minimum
        """
        # stack will hold a pair([value, cur_min_value]) ...
        # [3,1,4,2] => (3,3), (1,3), (4,1), (2,1))]
        stack = []
        cur_min = nums[0]

        for num in nums:
            # here if current number is greater that means nums[j] > nums[i]
            # so stack[-1] will give you a pari of(num, min_value) in which
            # $num will
            while stack and num > stack[-1][0]:
                stack.pop()

            # here as per our constraints, we need : num[i] < num[k] < num[k]
            # so $num will be chosen for num[k] and stack[-1][0] will be chosen
            # for num[j] because it should be greater than num[k] & num[i]
            # and num[i] will come from stack[-1][1];;
            if stack and num > stack[-1][1] and num < stack[-1][0]:
                return True

            # appending pair(num, cur_min) in stack for the next iteration;;
            stack.append((num, cur_min))
            cur_min = min(num, cur_min)

        return False

    def ansv1(self, nums):
        """
        _run: TLE [89/107]
        _code: time: o(n^3), space: o(1)
        _study:
        --- explanation ---
        [+] brute force for running 3 x loop in a go and check for respective condition
        (nums[i] < nums[k] < nums[j]) if satisfied then true else False

        """
        n = len(nums)
        if n == 3:
            return nums[0] < nums[2] < nums[1]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True

        return False


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
