'''
-------------------------------------------------------------------------------------
-> Problem Title: 680. Valid Palindrome II
-> Problem Status: Completed
-> Problem Attempted: 2024-03-18
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/valid-palindrome-ii/description/

Reference:-
https://youtu.be/JrxRYBwG6EI

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

    def validPalindrome(self, s: str) -> bool:
        """
        _stdin: string
        _stdout: bool
        """
        n = len(s)
        if n <= 2:
            # by default result true for n == 1 but will follow the same
            # nature in n == 2 b'coz here as well one char can be removed;;
            return True

        return self.ansv1(s, n)

    def ansv1(self, s, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- constaints ----
        We can skip or remove only one character to check if the current string
        is pallindrome or not.
        --- approach ---
        [+] Basically logic is same for checking pallindrome check is same which
        is using two pointer apporach.
        [+] one pointer starts from left side and one from right side and slowly
        one by one approach each other if they approach with the match of character
        then its good.
        [+] else if there is a mismatch then we are again calling a similar function
        following two pointer approach with left and right pointer but at this time.
        [+] But at this time, left and right pointer will point to those index at
        which the mismatch happens, which is prev_left+1 index and prev_right-1
        index. if any function retrun true then it is pallindrome.
        """
        lo, hi = 0, n - 1
        while (lo <= hi):
            if s[lo] == s[hi]:
                # if both the string are equals
                lo += 1
                hi -= 1
            else:
                # if any character mismatch then checking by skipping character;;
                return self._validate(s, lo + 1, hi) or self._validate(s, lo, hi - 1)

        return True

    def _validate(self, s, lo, hi):
        while (lo <= hi):
            if not (s[lo] == s[hi]):
                return False
            lo += 1
            hi -= 1
        return True


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
