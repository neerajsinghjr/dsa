'''
-------------------------------------------------------------------------------------
-> Problem Title: 1209. Remove All Adjacent Duplicates in String II
-> Problem Status: Completed
-> Problem Attempted: 2024-05-17
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

Reference:-
https://youtu.be/w6LcypDgC4w

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

    def removeDuplicates(self, s: str, k: int) -> str:
        """
        _stdin:
            arg1: s : __str__
            arg2: k : __str__
        _stdout: __str__
        """
        # return self.ansv1(s, k)
        return self.ansv2(s, k)

    def ansv2(self, strs, k):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- datastructure ---
        [+] stack is used to keep the order which we have seen in ansv1()
        --- explanation ---
        [+] here also we are counting the value with its relevant count in simple.
        [+] in stack we are storing the value with the count and if the top most
        element's value count reaches the exact match of $k then we are removing
        the value from the stack.
            [a] if the value's count match k then we remove it from stack
            [b] or if current char match the stack top character and count is lesser
            than k then only increment count.
            [c] or if char is different then add the char with count 1.
        [+] finally generate the result by popping value from stack and multiply
        with its respective count and append to the result.
        """
        res = ""
        stack = []  # pair => [val, count]

        for s in strs:
            if stack and stack[-1][0] == s:
                stack[-1][1] = stack[-1][1] + 1
            else:
                stack.append([s, 1])
            # removal of those character whose character count equals to k;;
            while stack and stack[-1][1] == k:
                stack.pop()

        # creating the result;;
        while stack:
            char, count = stack.pop()
            res = char * count + res

        return res

    def ansv1(self, strs, k):
        """
        _run: rejected [6/21]
        _code: time: o(n), space: o(n)
        _study:
        --- choke scenario ---
        s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy"
        k = 4
        output: "ytbh"
        expected: "ybth"
        --- datastructure ---
        [+] dictionary is used but there are certain drawbacks to it, like
        --- explanation ---
        [+] we have used dictionary to map the character with its related count.
        [+] here we were using dictionary to count the character string occurrence.
        [+] then in second loop we were sequentially fetching the character with its
        count and checking if the hashmap character count is not equals to $k, then
        adding the character to result else ignore.
        [+] on successfully tracing hashmap character's count then we reset the count.
        """
        res = ""
        hashmap = {}
        for s in strs:
            hashmap[s] = hashmap.get(s, 0) + 1

        for s in strs:
            if hashmap[s] not in (0, k):
                count = hashmap[s] % k if hashmap[s] > k else hashmap[s]
                res += s * count
                hashmap[s] = 0

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
