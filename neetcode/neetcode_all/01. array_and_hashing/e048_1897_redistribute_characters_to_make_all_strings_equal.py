'''
-------------------------------------------------------------------------------------
-> Problem Title: 1897. Redistribute Characters to Make All Strings Equal
-> Problem Status: Completed
-> Problem Attempted: 19/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/

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

    def makeEqual(self, words: List[str]) -> bool:
        """
        _stdin:
            arg: str
        _stdout: bool
        """
        n = len(words)
        if n == 1:
            return True
        # return self._ansv1(words, n)
        return self._ansv2(words, n)
    
    def _ansv2(self, words: List[str], n: int) -> bool:
        """
        _run: accepted
        _code: tc: o(n), sc: (n), rt: 13 ms, tcz: 179/179
        _choke: none
        _brief:
        - approach is still counting the char but instead of matching the count with 
        tht total length of the string. this time we are modulo divide the character 
        count and if its modulo not equals 0; thens it false else true
        """
        char_map = {}
        for word in words:
            for char in word:
                char_map[char] = char_map.get(char, 0) + 1
        for key, val in char_map.items():
            if val%n != 0:
                return False
        return True

    def _ansv1(self, words: List[str], n: int) -> bool:
        """
        _run: rejected
        _code: tc: o(n), sc: (n), rt: nan, tcz: 130/179
        _choke: refer brief section ...
        _brief:
        - the core idea of the approach is counting the char and checking the count
        of single char should be equals to total number of list length
        - eg1, --- working scenario
            - input: ["abc","aabc","bc"], my_out: true, exp_out: true 
            - n = 3
            - char_map={'a': 3, 'b': 3, 'c': 3}
            - we validte if single char is equals to n; if not then false
        - eg2, --- non working scenario
            - input: [
                "caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","c","c"
                "cccccccccccc","ccccccc","ccccccc","cc","cccc","cccccccc"
            ] , my_out: false, exp_out: true
            - n = 15
            - char_map={'c': 45, 'a': 15, 'b': 15}
            - here is a mismatch between single char and total length
        """
        char_map = {}
        for word in words:
            for char in word:
                char_map[char] = char_map.get(char, 0) + 1
        for key, val in char_map.items():
            if val != n:
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
