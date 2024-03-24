'''
-------------------------------------------------------------------------------------
-> Problem Title: 49. Group Anagrams
-> Problem Status: Completed
-> Problem Attempted: 2024-03-10
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/group-anagrams/description/

Reference:-
https://youtu.be/vzdNOK2oB2E

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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        _stdin: list[str]
        _stdout: list[str]
        """
        n = len(strs)
        if n == 0:
            return [[""]]

        return self.ansv1(strs, n)

    def ansv1(self, strs, n):
        """
        _run: accepted (optimal-approach)
        _code: time: o(n*m), space: (1)
        _choke: understand the problem well, you have to group the anagram together
        here only.
        _study: for grouping the anagram, we just map the particular string into the
        array index.
        for eg, 'eat', 'tea' both have same count index that means they are anagram.

        --- how 'eat', and 'tea' are same ---
        we have taken array with 26th indices for holding occurence of character in
        above example.

        To assign index for single character in the array, we use ascii index.

        count = []
        count[ord('e') - ord('a')] += 1

        here, ord('e') is 101 and ord('a') is 97, so index is 101 - 97 ~ 4
        so now the count will point to 4th index and we increment the 4th index value by 1

        count[4] += 1

        in simple word we map occurrence of 'e' as 1.

        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()


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
