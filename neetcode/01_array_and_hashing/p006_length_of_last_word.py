'''
-------------------------------------------------------------------------------------
-> Problem Title: 58. Length of Last Word
-> Problem Status: Completed
-> Problem Attempted: 2024/03/02
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/length-of-last-word/

Reference:-
https://youtu.be/KT9rltZTybQ

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

    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        # return self.ansv1(s)
        # return self.ansv2(s)
        # return self.ansv3(s)
        return self.ansv4(s)

    def ansv4(self, s):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: a bit clean code only
        """
        i, count = len(s) - 1, 0
        # Stripping the blank space;
        while s[i] == ' ':
            i = i - 1
        # Calculating the final length of last word;
        while i >= 0 and s[i] != ' ':
            count += 1
            i = i - 1
        return count

    def ansv3(self, s):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: need to take care blank character in upper bound.
        brief: Simple iteration from the end and grepping the character.
        """
        count = 0
        is_char_traced = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and not is_char_traced:
                continue
            if s[i] != ' ':
                count, is_char_traced = count + 1, True
            if s[i] == ' ':
                break
        return count

    def ansv2(self, s):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        breif: simple striping and calculating values from front till coming blank.
        """
        count = 0
        s = s.strip()
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == ' ':
                break
            count += 1
        return count

    def ansv1(self, s):
        """
        run: accepted
        time: o(n)
        space: o(k) ~ worst case (n)
        choke: none
        brief: python oriented solution using striping the string
        to remove extra blank space from start and end.
        then converting to list and fetching last index word length.
        """
        s = s.strip()
        s_list = s.split(" ")
        return len(s_list[-1])


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
