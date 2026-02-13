'''
-------------------------------------------------------------------------------------
-> Problem Title: 14. Longest Common Prefix
-> Problem Status: Completed
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/longest-common-prefix/description/

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

    def longestCommonPrefix(self, words: List[str]) -> str:
        """
        _stdin:
            arg1: list[str]
        _stdout: str
        """
        n = len(words)
        if n == 1:
            return words[0]
        # return self._ansv1(words, n)
        return self._ansv2(words, n)
    
    def _ansv2(self, strlst, n):
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(1), rt: 
        _choke:
        _brief: approach is stable and accurate but its tc not gud as _ansv1()
        - gist of this approach revolves around sorting word_lst lexicographically
        because the common prefix will be common in all the words. 
        - finding common prefix for first and last word from sorted list is enough
        - first step is still sorted the word_lst and grepping the first, last word
        - loop 1: iterate over the min(first, last) to below constraints
        - if_constraints_1: if first[idx] != last[idx] then return cur_prefix
        - otherwise add the existing word[idx] to the prefix variable and that's it 
        """
        prefix = ""
        words = sorted(strlst)
        first, last = words[0], words[-1]
        for idx in range(min(len(first), len(last))):
            if first[idx] != last[idx]:
                return prefix
            prefix += first[idx]
        return prefix
    
    def _ansv1(self, words, n):
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(1), rt: 0ms
        _choke:
        - remember to check constraint first where cur_idx should not overflow 
        the total length of cur_word otherwise you will index out of bound err.
        _brief: approach is quite simple and tricky at same time too.
        - taking first word as default and checking every next word with it
        - loop 1 is iterating over idx within the length of our default word
        - loop 2 is iterating over singlular word in every iteration from word_list
        - if constraints_1 : if idx == len(word) then return prefix
        - if_constraints_2 : if cur_word[idx] != default[idx] then return prefix
        - catch: prefix will update at the end of the loop_2; when loop_2 cycles
        completes then we add cur_idx of last $word from loop_2 scope to prefix.  
        """
        prefix = ""
        default = words[0]
        for idx in range(len(default)):  # loop iterating over index;;
            for word in words:    # loop iterating over every word;;
                if idx == len(word) or word[idx] != default[idx]:
                    return prefix
            prefix += word[idx]
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
