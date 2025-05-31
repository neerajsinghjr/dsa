'''
-------------------------------------------------------------------------------------
-> Problem Title: 118. Pascal's Triangle
-> Problem Status: Completed
-> Problem Attempted: 28/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/pascals-triangle/description/

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

    def generate(self, n: int) -> List[List[int]]:
        """
        _stdin:
            arg1: int
        _stdout: list[list[int]]
        """
        rows = [[1]]
        if n == 1:
            return rows
        rows.append([1,1])
        if n == 2:
            return rows
        return self._ansv1(rows, n)
    
    def _ansv1(self, rows: List[List[int]], n: int) -> List[List[int]]:
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(1), rt: 0 ms
        _choke: none
        _brief:
        - divide the problem based on multi-level for instance when n eq 1 then return 
        [[1]] and similarly when $n eq 2 then [[1], [1,1]]
        - for level n > 2, we are simply using the two loops, where loop_1 takes care
        of creating level of triangle and child loop_2 fills items at required indices.
        - catch here is now level n in (1,2) are already calculated. so keep in mind to
        start loop_1 from level 3 onwards to (n+1) level.
        - child_loop only calculates the element at particular indices. So it was just 
        pulling last row and on the basis of current index; do the maths of adding both 
        prev_row[idx-1] + prev_row[idx];;
        - finally append the cur_row to our master rows list. that's it
        """
        for level in range(3, n+1):
            row = []
            for idx in range(level):
                p_row = rows[-1]  # last row would be previous row;;
                if idx == 0 or idx == level-1:
                    row.append(1)
                else:
                    row.append(p_row[idx-1] + p_row[idx])
            rows.append(row)
        return rows 


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
