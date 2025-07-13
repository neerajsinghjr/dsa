'''
-------------------------------------------------------------------------------------
-> Problem Title: 242. Valid Anagram
-> Problem Status: Completed
-> Problem Attempted: 06/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/valid-anagram/description/

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

    def isAnagram(self, s: str, t: str) -> bool:
        """
        stdin:
            arg1: str
            arg2: str
        stdout:
            bool
        """
        # return self._ansv1(s, t)
        # return self._ansv2(s, t)
        # return self._ansv3(s, t)
        return self._ansv4(s, t)
    
    def _ansv4(self, s, t):
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n+m), rt: 15 ms, tcz: 53/53
        _choke: none
        _brief: --- fix for ansv3() ---
        - **fix** : whole solution was breaking due to the fact that both the target
        string len must be same; thats why added a based condition to handle this. 
        - firstly we map the character counts of target string $s and $t.
        - next time we opt of iterating over s_map keys and pull the respective char
        count from the t_map dict
        - if matching count doesnt match then return false; else True
        """
        # if len(s) != len(t):
        #     return False

        s_map, t_map = {}, {}
        # map the character occurrences;;
        for idx in range(len(s)):
            s_map[s[idx]] = s_map.get(s[idx], 0) + 1
            t_map[t[idx]] = t_map.get(t[idx], 0) + 1
        
        # verify the character occurrences;;
        for key in s_map:
            if s_map[key] != t_map.get(key, 0):
                return False
              
        return True
    
    def _ansv3(self, s, t):
        """
        _run: rejected
        _code: time:o(n+m), space: o(n+m)
        _choke: failure of testcase like,
            input: s,t = "a", "ab"
            output: true
            expected: false
        _brief: derivate of solution ansv1()... 
            it did worked in past but observed loop holes this time. if we are 
            checking the character count of s_map then we should definately 
            verify the other one character count too, the same way.
        """
        # if len(s) != len(t):
        #     return False

        s_map, t_map = {}, {}
        # map the character occurrences;;
        for idx in range(len(s)):
            s_map[s[idx]] = s_map.get(s[idx], 0) + 1
            t_map[t[idx]] = t_map.get(t[idx], 0) + 1
        
        # verify the character occurrences;;
        for key in s_map:
            if s_map[key] != t_map.get(key, 0):
                return False
              
        return True
    
    def _ansv2(self, s, t):
        """
        _run: accepted
        _code: time: o(nlogn + mlogm), space: o(1)
        _choke: none
        _brief:
            crux is sorted all the string if they are equal then True else False
            whole logic revolves around the fact the anagram are jumble words only.
        """
        return sorted(s) == sorted(t)

    def _ansv1(self, s, t):
        """
        _run: accepted
        _code: time: o(n+m), space: o(n+m)
        _choke: none
        _brief: crux revolves around jumble words... 
            1) firstly map the char count of both the string into dict
            2) used two loop, #loop1 check if all the $s_map chars are resides in t_map
            and similarly t_map chars are resides in s_map else False. 
        """
        s_map, t_map = {}, {}
        
        # mapping s_character into s_map;;
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1

        # mapping t_character into t_map;;
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        # c1: check s_map char count with t_map;;
        for ch in s_map.keys():
            if s_map.get(ch) != t_map.get(ch):
                return False

        # c2: check t_map char count with s_map;;
        for ch in t_map.keys():
            if t_map.get(ch) != s_map.get(ch):
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
