'''
-------------------------------------------------------------------------------------
-> Problem Title: 125. Valid Palindrome
-> Problem Status: Completed
-> Problem Attempted: 2024-03-17
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/valid-palindrome/description/

Reference:-
https://youtu.be/jJXJ16kPFWg

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
    def isPalindrome(self, s: str) -> bool:
        """
        _stdin: string
        _stdout: bool
        """
        return self.ansv1(s)

    def ansv1(self, s):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- choke ---
        convert the given string to lowercase to avoid caps conflicts
        --- explanation ----
        simple create a new string by removing all non-alphanumeric
        character. then check for pallindrome by reversing the given
        string.
        """
        res = ""
        strs = s.lower()
        for c in strs:
            if c.isalpha() or c.isdigit():
                res += c
        return res == res[::-1]


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






