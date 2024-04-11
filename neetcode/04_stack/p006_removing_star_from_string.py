'''
-------------------------------------------------------------------------------------
-> Problem Title: 2390. Removing Stars From a String
-> Problem Status: Completed
-> Problem Attempted: 2024-04-11
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/removing-stars-from-a-string/description/

Reference:-
https://youtu.be/pRyFZIaKegA

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

    def removeStars(self, s: str) -> str:
        """
        _stdin:
            arg1: str
        _stdout: str
        """
        n = len(s)
        if n == 1:
            return s

        # return self.ansv1(s)
        return self.ansv2(s)


    def ansv2(self, s):
        """
        _run: accepted (optimal)
        _code: time: o(n), space: o(n) + o(n)
        _brief:
        --- ds picked ---
        [+] we are using the stack datastructure in which we keep the order of the char
        as per given to us in the questions.
        [+] to remove anything from the end we dont need to do o(n) operation instead
        we are directly remove it using the last index straight which is o(1)
        [+] stack provide us linear time complexity.
        --- explanation ---
        [+] as described we are using the stack to put char inside of it but as soon as
        we trace any star then pop the last character and do the same for rest of it.
        [+] at the time of result make sure to return the stack based character in
        string format not list. if stack is empty then empty string only.
        """
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)

        return '' if not stack else ''.join(stack)


    def ansv1(self, s):
        """
        _run: accepted (brute-force)
        _code: time: o(n^2), space: o(n)
        _brief:
        --- analysis ---
        [+] The loop iterates through each character in the string s, performing
        operations based on the character.
        [+] Appending a character to a string (res += char) takes O(1) time.
        [+] Slicing a string (res = res[:slen]) takes O(n) time, where n is the
        length of the string
        --- explanation ---
        [+] we are using the for loop for iterating over the string and we are using
        two variable to res(~result) and slen(for result string length)
        [+] if the ith character is not star then we are appending the char to result
        [+] else we are trimming the end character from the end of the resultant string.
        """
        res, slen = '', 0

        for idx, char in enumerate(s):
            if char == '*':
                slen = slen - 1
                res = res[:slen]  # o(n)
            else:
                res += char
                slen += 1

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
