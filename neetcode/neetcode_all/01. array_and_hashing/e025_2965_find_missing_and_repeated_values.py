'''
-------------------------------------------------------------------------------------
-> Problem Title: 2965. Find Missing and Repeated Values
-> Problem Status: Completed
-> Problem Attempted: 09/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/find-missing-and-repeated-values/description/

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

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
            _stdin:
                arg1: list[list[int]]
            _stdout: list[int]
        """
        # return self._ansv1(grid)
        return self._ansv2(grid)
    
    def _ansv2(self, grid: List[int]) -> List[int]:
        """
        _run: accepted (code-level-optimization)
        _code: tc: o(n), sc: o(n), rt: 3 ms, tcz: 584/584 
        _choke: none
        _brief: --- ref: 448: find missing number ---
        - core of the problem is similar to parent problem where we were finding the missing number 
        in an array
        - here we used hashmap to count the occurence of each element if there is any duplicate then 
        it is expected to have more than 1 count.
        - later we calculate the total length of grid and iterate over from 1 to (n+1) length of the 
        grid; and iteratively verifies if the cur_idx is there in our pre-fetch hashmap or not;
        - if its present inside our hashmap then we check if its occurence if more than 1 or not;
        """
        unq, dup = 0, 0
        n = len(grid) * len(grid[0])
        hashmap = collections.Counter(num for row in grid for num in row)
        for idx in range(1, n+1):
            if hashmap.get(idx, 0) == 0:
                unq = idx
            elif hashmap.get(idx, 0) > 1:
                dup = idx
            if unq and dup:
                break
        return [dup, unq]

    def _ansv1(self, grid: List[int]) -> List[int]:
        """
        _run: accepted (brute-force)
        _code: tc: o(n), sc: o(n), rt: 11 ms, tcz: 584/584 
        _choke: none
        _brief: --- ref: 448: find missing number ---
        - core of the problem is similar to parent problem where we were finding the missing number 
        in an array
        - here we used hashmap to count the occurence of each element if there is any duplicate then 
        it is expected to have more than 1 count.
        - later we calculate the total length of grid and iterate over from 1 to (n+1) length of the 
        grid; and iteratively verifies if the cur_idx is there in our pre-fetch hashmap or not;
        - if its present inside our hashmap then we check if its occurence if more than 1 or not;
        """
        ans = [0]*2
        n = self._get_grid_size(grid)
        hashmap = {}
        for row in grid:
            for num in row:
                hashmap[num] = hashmap.get(num, 0) + 1
        for idx in range(1, n+1):
            count = hashmap.get(idx, 0)
            if count == 0 or count > 1:
                ans_idx = 0 if count > 1 else 1
                ans[ans_idx] = idx
        return ans

    def _get_grid_size(self, grid: List[List[int]]) -> int:
        """ helper to fetch grid size """
        count = 0
        for row in grid:
            count += len(row)
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
