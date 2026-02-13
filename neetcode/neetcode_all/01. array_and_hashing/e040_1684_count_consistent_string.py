'''
-------------------------------------------------------------------------------------
-> Problem Title: 1684. Count the Number of Consistent Strings
-> Problem Status: Completed
-> Problem Attempted: 01/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

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

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        _stdin:
            arg1: str
            arg2: list[str]
        _stdout: int
        """
        # return self._ansv1(words, allowed)
        # return self._ansv2(words, allowed)
        return self._ansv3(words, allowed)

    def _ansv3(self, words: List[str], allowed: str) -> int:
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(k), rt: 208 ms, tcz: 213/213
        _choke: none
        _brief:
        - every word chars should be inside our allowed char sequence; if any other char then 
        word is not eligible
        - we make the allowed char to set; iterating over the sinlge char from iterating words;
        - we check if single char not exist in our allowed set then ignore that word; else we
        set our variable is_word_consistent to false;
        - if word is good then we can update the count; finally return the count;
        """
        count = 0
        allowed_set = set(allowed)
        for word in words:
            is_word_consistent = True
            for wc in word:
                if wc not in allowed_set:
                    is_word_consistent = False
                    break
            if is_word_consistent:
                count += 1
        return count    

    def _ansv2(self, words: List[str], allowed: str) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(k), rt: 232 ms, tcz: 213/213
        _choke: none
        _brief:
        - problem says consistent string or every word chars should be inside our allowed char 
        sequence; if any other char then word is not eligible
        - we make the allowed char to set and iterating word to set; then we check if there is 
        any extra chars which is not present in allowed chars then straight skip;
        - if word_set is having no new chars then we can increment our count; 
        - finally return the count;;
        """
        count = 0
        allowed_set = set(allowed)
        for word in words:
            word_set = set(word)
            if len(word_set - allowed_set) == 0:
                count += 1
        return count
    
    def _ansv1(self, words: List[str], allowed: str) -> int:
        """
        _run: accepted (brute-force)
        _code: tc: o(n^2), sc: o(1), rt: 213 ms, tcz: 213/213
        _choke: none
        _brief:
        - simply having two for_loops, parent loop_1 takes care of iterating of the single word
        at each time
        - child_loop take single word and break it down to single char; then check if its allowed
        then its good string we increament the count; else ignore;
        - finally return the overall count 
        """
        count = 0
        for word in words:
            is_word_consistent = True
            for wc in word:
                if wc not in allowed:
                    is_word_consistent = False
                    break
            if is_word_consistent:
                count += 1
        return count


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
