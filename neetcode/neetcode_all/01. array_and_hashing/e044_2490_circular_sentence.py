'''
-------------------------------------------------------------------------------------
-> Problem Title: 2490. Circular Sentence
-> Problem Status: Completed
-> Problem Attempted: 08/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/circular-sentence/description/

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

    def isCircularSentence(self, chars: str) -> bool:
        """
        _stdin:
            arg1: str
        _stdout: bool
        """
        # return self._ansv1(chars)
        # return self._ansv2(chars)
        return self._ansv3(chars)
    
    def _ansv3(self, chars: str) -> bool:
        """
        _run: accepted
        _code: tc: o(n), sc: o(k), rt: 0 ms, tcz: 206/206
        _choke: none
        _brief:
        - catch in this question is, we have to match current word last character with the next
        word first character; for the last word too.
        - for this we implement counter reset whenever we reach at the nth positiion we modulo 
        reset it to 0th index.
        - we split the chars with split method; then used for loop where we individualy pick 
        current word and next word; 
        - we match last character of current word with first char of next character; if not 
        match then we return False; thats it. 
        """
        words = chars.split()
        n = len(words)
        for i in range(n):
            if words[i][-1] != words[(i+1)%n][0]:
                return False
        return True
    
    def _ansv2(self, chars: str) -> bool:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 206/206
        _choke: none
        _brief:
        - This method determines if a sentence (represented by the input string 'chars') forms 
        a valid circular word chain.
        - A circular word chain is defined by two conditions:
            - Sequential Linkage: The last character of each word must precisely match the first
             character of the subsequent word in the sequence.
            - **Circular Completion:** The last character of the final word in the sequence must 
            also match the first character of the very initial word, thus completing the circle.
        """
        words = chars.split()
        n = len(words)
        for i in range(n-1):
            if words[i][-1] != words[i+1][0]:
                return False
        return words[-1][-1] == words[0][0]

    def _ansv1(self, chars: str) -> bool:
        """
        _run: accepted
        _code: tc: o(n), sc: o(k), rt: 0 ms, tcz: 206/206
        _choke: none
        _brief:
        - catch in this question is, we have to match current word last character with the next
        word first character; for the last word too.
        - for this we implement counter reset whenever we reach at the nth positiion we modulo 
        reset it to 0th index.
        - we split the chars with split method; then used for loop where we individualy pick 
        current word and next word; 
        - we match last character of current word with first char of next character; if not 
        match then we return False; thats it. 
        """
        words = chars.split(" ")
        n = len(words)
        for i in range(n):
            cur_wd = words[i]
            nex_wd = words[(i+1)%n]
            if cur_wd[len(cur_wd)-1] != nex_wd[0]:
                return False
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
