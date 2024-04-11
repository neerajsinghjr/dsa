'''
-------------------------------------------------------------------------------------
-> Problem Title: 28. Find the Index of the First Occurrence in a String
-> Problem Status: Completed
-> Problem Attempted: 2024-03-08
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Reference:-
https://youtu.be/JoF0Z7nVSrA

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

    def strStr(self, htxt: str, ntxt: str) -> int:
        hlen, nlen = len(htxt), len(ntxt)

        if hlen < nlen:
            return -1  # haystack should be bigger in size logically

        if nlen == 0:
            return 0  # Empty needle is always a match

        # return self.ansv1(htxt, ntxt, hlen, nlen)
        return self.ansv2(htxt, ntxt)

    def ansv2(self, haystack, needle):
        """
        _run: accepted (optimized)
        _code: time: o(n+m) | space: o(1)
        _choke: refer ansv1(), ith index is controlled here well.
        _study: --- based on Knuth-Morris-Pratt algorithm ---
        """
        i, j = 0, 0
        hlen, nlen = len(haystack), len(needle)

        while i < hlen:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                # If needle found in haystack
                if j == nlen:
                    return i - nlen
            else:
                # NOTE: i -= j - 1 i.e i = i - (j - 1) => i = 1 when i is at 0 index.
                # Don't get confused again with i = i - j - 1 => -1 when i is at 0 index.
                i -= j - 1  # Move back to the character after the mismatch
                j = 0  # Reset j to the start of needle

        return -1  # Needle not found in haystack

    def ansv1(self, htxt, ntxt, hlen, nlen):
        """
        _run: rejected (brute-force, tried myself)
        _code: time: o(n+m), space: o(1)
        _choke: unable to control the ith index flow
        _study: think of similar apporach based on --- KMP knuth Morris Prat --- algorithm.
        I tried searching the pattern needle in the haystack iteratively.
        mantain a flag to track the needle availability in the haystack.
        if both ith and jth character matched then both pointer increased by 1
        otherwise j is reset to 0 but i think simply incrementing the i+1 for mismatch
        case would word. but that cause uncertainities.
        """
        i, j = 0, 0
        is_needle_found = True

        while i < hlen:
            while j < nlen:
                if htxt[i] != ntxt[j]:
                    print(f"i: {htxt[i]}, j: {ntxt[j]}, not matched")
                    is_needle_found = False
                    j = 0  # start from zero again;;
                else:
                    print(f"i: {htxt[i]}, j: {ntxt[j]}, matched")
                    j += 1

                i += 1

                # if needle found at the end of substring;;
                if j == nlen and is_needle_found:
                    return i - nlen - 1

                # check for upper bound of string;;
                if i == hlen:
                    return -1

        return -1


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
