'''
-------------------------------------------------------------------------------------
-> Problem Title: 605. Can Place Flowers
-> Problem Status: Completed
-> Problem Attempted: 29/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/can-place-flowers/description/

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

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        _stdin:
            arg1: list[int]
        _stdout: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        return self._ansv1(flowerbed, n)
    
    def _ansv1(self, fb: List[int], n: int) -> bool:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 12ms
        _choke: flowerbed indices are the key player here ...
        - make a note of it, when u are checking for idx=0 index and similarly for 
        idx=(n-1)th index.
        _brief:
        - simple for loop did the job, we are checking iteratively if the (ith == 0)
        and (ith+1 == 0) - both should be zero then flowerbed can be place
        - simultaneously, from upper bound we're also validating the same set of values
        - in between if the (ith-1 == 0) and (idx == 0) and (idx+1 == 0); then we can 
        place the flowerbed.    
        """
        for idx in range(len(fb)):
            if n == 0:
                break
            elif idx == 0 and fb[idx] == 0 and fb[idx+1] == 0:
                n, fb[idx] = n-1, 1
            elif idx == len(fb)-1 and fb[idx] == 0 and fb[idx-1] == 0:
                n, fb[idx] = n-1, 1
            elif fb[idx] == 0 and fb[idx-1] == 0 and fb[idx+1] == 0:
                n, fb[idx] = n-1, 1
        return True if n == 0 else False


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
