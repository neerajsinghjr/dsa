'''
-------------------------------------------------------------------------------------
-> Problem Title: 1758. Minimum Changes To Make Alternating Binary String
-> Problem Status: Completed
-> Problem Attempted: 14/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

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

    def minOperations(self, s: str) -> int:
        """
        _stdin:
            arg1: str
        _stodut: int
        """
        if not s:
            return 0
        # return self._ansv1(s)
        return self._ansv2(s)
    
    def _ansv2(self, strs: str) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 12 ms, tcz: 89/89
        _choke: 
        - the previous version only calculated the changes for *one* of the two possible 
        alternating patterns (the one implied by the first character).
        - it failed to consider the alternative pattern, which could potentially require 
        fewer changes. 
        - this fix addresses that by calculating mismatches for both ideal alternating patterns.
        _brief:
        - this method efficiently calculates the minimum number of operations (character flips) 
        required to transform the input binary string `s` into an alternating binary string. 
        - alternating string is one where no two adjacent characters are the same eg, "0101" or "1010"
        - the solution works by comparing the input string `s` against the only two possible ideal
        alternating patterns:
            1. One that starts with '0' (e.g., "010101...")
            2. One that starts with '1' (e.g., "101010...")
        - it counts the number of mismatches for `s` against each of these two ideal patterns.
        - the minimum of these two mismatch counts is the answer, as it represents the fewest flips 
        needed to achieve an alternating sequence.
        """
        
        bin_pattern_01s_count = 0   # Count changes needed to match "010101..."
        bin_pattern_10s_count = 0   # Count changes needed to match "101010..."

        for idx in range(len(strs)):
            # Determine expected character for "0101..." pattern at current index 'i'
            bin_pattern_01s = '0' if idx%2 == 0 else '1'
            
            # Determine expected character for "1010..." pattern at current index 'i'
            bin_pattern_10s = '1' if idx%2 == 0 else '0'

            # Compare s[i] with expected for "0101..."
            if strs[idx] != bin_pattern_01s:
                bin_pattern_01s_count += 1

            # Compare s[i] with expected for "1010..."
            if strs[idx] != bin_pattern_10s:
                bin_pattern_10s_count += 1

        # The minimum of the two counts is the answer
        return min(bin_pattern_01s_count, bin_pattern_10s_count)

    def _ansv1(self, strs: str) -> int:
        """
        _run: rejected
        _code: tc: o(n), sc: o(n), rt: nan, tcz: 64/89
        _choke: 
        - this method fails on test cases where the optimal alternating string does not begin 
        with the same character as `strs[0]`. 
        - the logic only calculates the changes needed to make the string alternating assuming 
        strs[0] remains unchanged (or more accurately, assuming strs[0] is the correct starting 
        character for the target pattern).
        - it does not consider the alternative scenario where strs[0] might need to be flipped 
        to achieve the true minimum changes.
        - example of failure:
            - input: strs = "001"
            - expected Output: 1 (change "001" to "101")
            - Your method's Output: 2 (changes "001" to "010" by flipping '0' at index 1 and 
            '1' at index 2)
        _brief: 
        - this method attempts to find the minimum number of changes by comparing the input string 
        against one of the two possible alternating patterns.
        - it implicitly derives this target pattern by assuming the first character strs[0] 
        aligns with the desired alternating sequence. 
        - it then iterates through the rest of the string, incrementing a counter for every 
        character that does not match the expected alternating sequence based on the previous 
        character.
        """
        idx, cnt = 1, 0
        bin_exp = '1' if strs[0] == '0' else '0'
        while idx < len(strs):
            if strs[idx] != bin_exp:
                cnt += 1
            idx += 1
            bin_exp = '1' if bin_exp == '0' else '0'
        return cnt
    

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
