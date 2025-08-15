'''
-------------------------------------------------------------------------------------
-> Problem Title: 1002. Find Common Characters
-> Problem Status: Completed...
-> Problem Attempted: 15/08/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/find-common-characters/description/

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

    def commonChars(self, words: List[str]) -> List[str]:
        """
        _stdin:
            arg1: list[str]
        _stdout: list[str]
        """
        n = len(words)
        if n == 1:
            return list(words[0])
        return self._ansv1(words, n)
    
    def _ansv1(self, words: List[str], n: int) -> List[str]:
        """
        _run: accepted
        _code: tc: o(n*m), sc: o(1), rt: 16 ms, tcz: 85/85
        _choke: none
        _brief:  
        - This method efficiently finds common characters by maintaining a frequency count. 
        - It starts with a frequency map of the first word as master frequency. 
        - It then iterates through the remaining words and update the master frequency map 
        to the minimum count of each character found in both the master frequency map and
        the current frequency word's map. 
        - This process effectively computes the intersection of character frequencies. 
        - Finally, it constructs the result list by appending each character the number of 
        times it appeared in the final, shared frequency map.
        """
        res = []
        master_freq = collections.Counter(words[0])
        for word in words[1:]:
            cur_freq = collections.Counter(word)
            # update the master freq;;
            for k,v in master_freq.items():
                master_freq[k] = min(v, cur_freq.get(k, 0))
        # generating final result list;;
        for k,v in master_freq.items():
            while v > 0:
                res.append(k)
                v = v - 1
        return res


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
