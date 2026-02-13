'''
-------------------------------------------------------------------------------------
-> Problem Title: 2287. Rearrange Characters to Make Target String
-> Problem Status: Completed
-> Problem Attempted: 09/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/

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

    def rearrangeCharacters(self, src: str, tgt: str) -> int:
        """
        _stdin:
            arg1: str
            arg2: str
        _stdout: int
        """
        s_len, t_len = len(src), len(tgt)
        if s_len < t_len:
            return 0
        # return self._ansv1(src, tgt)
        return self._ansv2(src, tgt)
    
    def _ansv2(self, src: str, tgt: str) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 116/116
        _choke: none
        _brief: ---code-level-optimization---
        - simple hashmap under the hood to map the occurences then finally we are checking if the 
        char count exist then we are decreamenting it by 1; or else if its reaches to 0 then we
        are basically returning our existing count as answer.
        """
        count = 0
        hashmap = collections.Counter(ch for ch in src if ch in tgt)
        while True:
            for ch in tgt:
                if hashmap.get(ch, 0) == 0:
                    return count
                hashmap[ch] = hashmap.get(ch, 0) - 1
            count += 1
        return count

    def _ansv1(self, src: str, tgt: str) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 116/116
        _choke: none
        _brief: ---code-level-optimization---
        - simple hashmap under the hood to map the occurences then finally we are checking if the 
        char count exist then we are decreamenting it by 1; or else if its reaches to 0 then we
        are basically returning our existing count as answer.
        """
        count = 0
        hashmap = {}
        for ch in src:
            if ch in tgt:
                hashmap[ch] = hashmap.get(ch, 0) + 1
        while True:
            for ch in tgt:
                if hashmap.get(ch, 0) == 0:
                    return count
                hashmap[ch] = hashmap.get(ch, 0) - 1
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
