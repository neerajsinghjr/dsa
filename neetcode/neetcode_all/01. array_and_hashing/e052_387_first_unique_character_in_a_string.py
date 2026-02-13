'''
-------------------------------------------------------------------------------------
-> Problem Title: 387. First Unique Character in a String
-> Problem Status: Completed
-> Problem Attempted: 10/08/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/first-unique-character-in-a-string/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:

    def firstUniqChar(self, s: str) -> int:
        """
        _stdin:
            arg: str
        _stdout: int
        """
        n = len(s)
        if n == 1:
            return 0
        if n == 2:
            return 0 if s[0] != s[1] else -1
        # return self._ansv1(s, n)
        # return self._ansv2(s, n)
        # return self._ansv3(s, n)
        return self._ansv4(s, n)
    
    def _ansv4(self, s: str, n: int):
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n), rt: 51 ms, tcz: 107/107
        _choke: none
        _brief: 
        - This solution uses the collections. Counter utility to efficiently get the 
        frequency of all characters in a single pass. 
        - A second pass then iterates through the original string to return the index 
        of the first character with a frequency count of one.
        """
        hashmap = collections.Counter(s)
        for idx, ch in enumerate(s):
            if hashmap.get(ch) == 1:
                return idx
        return -1

    def _ansv3(self, s: str, n: int):
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n), rt: 72 ms, tcz: 107/107
        _choke: none
        _brief: 
        - This Solution comprises of  a fixed-size array (of 26) as a frequency map for 
        lowercase English letters. 
        - The first pass populates the array with character counts. 
        - The second pass then finds the first character in the string whose count in the 
        array is exactly one and returns its index.
        """
        lttrs = [0] * 26
        for ch in s:
            lttrs[ord(ch) - ord('a')] += 1
        for idx, ch in enumerate(s):
            if lttrs[ord(ch) - ord('a')] == 1:
                return idx
        return -1

    def _ansv2(self, s: str, n: int):
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n), rt: 51 ms, tcz: 107/107
        _choke: none
        _brief: --- optimization ---
        - This is an optimized two-pass solution. 
        - The first pass populates a hash map with both the frequency count and the index 
        of each character. 
        - The second pass then iterates through the hash map to find the first character 
        with a count of one and returns its index.

        """
        hashmap = {}
        for idx, ch in enumerate(s):
            if ch not in hashmap:
                hashmap[ch] = [0, -1]    # default - 0: count, 1:  index;;
            hashmap[ch][0] += 1
            hashmap[ch][1] = idx
        for ch, pair in hashmap.items():
            if pair[0] == 1:
                return pair[1]
        return -1

    def _ansv1(self, s: str, n: int):
        """
        _run:
        _code: tc: o(n+m+k), sc: o(n), rt: 51 ms, tcz: 107/107
        _choke:
        _brief: --- brute-force ---
        - This brute-force solution uses a hash map to count character frequencies 
        in a first pass. 
        - In a second pass, it iterates through the hash map to find the first unique 
        character and then uses a third pass (via s.index()) to find its index.

        """
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for ch, cnt in hashmap.items():
            if cnt == 1:
                return s.index(ch)
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
