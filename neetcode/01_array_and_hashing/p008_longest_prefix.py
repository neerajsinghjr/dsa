'''
-------------------------------------------------------------------------------------
-> Problem Title: 14. Longest Common Prefix
-> Problem Status: Completed
-> Problem Attempted: 2024-03-02
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/longest-common-prefix/description/

Reference:-
https://youtu.be/0sWShKIJoo4

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

    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]

        # return self.ansv1(strs, n)
        return self.ansv2(strs, n)

    def ansv2(self, strs, n):
        # empty string for result calculatons;;
        prefix = ""

        # Sort the input list strs lexicographically. This
        # step is necessary because the common prefix should
        # be common to all the strings, so we need to find
        # the common prefix of the first and last string in the sorted list.
        strs = sorted(strs)

        # we are taking first and last index word because those words
        # can determine if we have any common prefix words or not;

        # If they have same initial character then sorting result...
        # ["ab", "acv", "abz"] => ['ab', 'abz', 'acv']

        # if they have different initial character, then sorting result...
        # ["reflower","flow","flight"] => ['flight', 'flow', 'reflower']
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            # check for fetching common string in both targetted string;;
            if first[i] != last[i]:
                return prefix

            # append common string for result;;
            prefix += first[i]

        return prefix

    def ansv1(self, strs, n):
        """
        run: accepted
        time: o(n * k) i.e k is the length of first_string in algo
        space: o(1)
        choke: here word length is different for every case. so checkpoint
        need to added to handle such case. refer if block in second for loop
        """
        # final answer and common character will be append
        # in this string and empty string if nothing commmon
        # comes out.
        prefix = ""

        # First sting is taking as default string because
        # prefix should be common in every string.
        first_string = strs[0]

        for i in range(len(first_string)):
            # now iterating over every single character
            # and checking if the iterating ith index is
            # same in every string.
            for s in strs:

                # here s refer string at ith index inside list
                # sequentially matching every character every time.
                # if not matching then return else appending to prefix.
                if i == len(s) or s[i] != first_string[i]:
                    return prefix

            # if common string found then append
            prefix += s[i]

        return prefix


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
