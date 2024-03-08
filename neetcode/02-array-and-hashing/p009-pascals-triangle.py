'''
-------------------------------------------------------------------------------------
-> Problem Title: 118. Pascal's Triangle
-> Problem Status: Completed
-> Problem Attempted: 2024-03-02
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/pascals-triangle/description/

Reference:-
https://youtu.be/nPVEaB3AjUM

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
    def generate(self, rows: int) -> List[List[int]]:
        resp = []

        if rows == 0:  # pascal triangle base case;;
            return resp

        resp.append([1])  # 0th row pascal triangle;;

        if rows == 1:
            return resp

        resp.append([1, 1])  # 1th row pascal triangle;;

        if rows == 2:
            return resp

        return self.ansv1(resp, rows)

    def ansv1(self, resp, rows):
        """
        run: accepted
        time: o(n^2)
        space: o(1)
        choke: none
        brief: Need to iterative from 1th row to the target row everytime and
        need to generate new row based on the previous row.
        """
        i = 2  # 2th row pascal triangle;;
        prev = resp[-1]

        # this loop will handle the required number of rows after 2th row only;;
        while (i < rows):
            j = 0
            row = []

            # this loop will be used to generate new row as per the previous row;;
            while (j <= i):
                if (j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(prev[j - 1] + prev[j])
                j += 1

            prev = row
            resp.append(row)

            i += 1

        return resp


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
