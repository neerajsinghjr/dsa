'''
-------------------------------------------------------------------------------------
-> Problem Title: 3110. Score of a String
-> Problem Status: Completed
-> Problem Attempted: 05/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/score-of-a-string/description/

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
    
    def scoreOfString(self, s: str) -> int:
        """
        _stdin:
            arg1: string
        _stdout: int
        """
        return self._ansv1(s)
    
    def _ansv1(self, s):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _choke: none
        _brief:
          simple for loop which we are starting with index 1 till lesser than n.
          for every iteration, we are simple adding up the ascii value.
        """
        idx, cnt = 1, 0  
        while idx < len(s):
            cnt += abs(ord(s[idx-1]) - ord(s[idx]))
            idx += 1
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
