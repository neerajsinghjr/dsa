'''
-------------------------------------------------------------------------------------
-> Problem Title: 554. Brick Wall
-> Problem Status: Completed
-> Problem Attempted: 2024-03-16
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/brick-wall/

Reference:-
https://youtu.be/Kkmv2h48ekw

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

    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        _stdin: List[List]
        _stdout: int
        """
        return self.ansv1(wall)

    def ansv1(self, wall):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- example ---
        Input:
        [
            [1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]
        ]
        Output: 2
        --- explanation ---
        In the given example, the wall is represented by the 2D list.
        If we draw a vertical line at position 4 (0-indexed), it will
        cross two bricks, which is the minimum number of bricks that
        need to be crossed.
        --- solution approach ---
        We can solve this problem using a hashmap to store the positions
        where the vertical lines intersect with the edges of each brick.
        By keeping track of the most common position of the intersections,
        we can find the minimum number of bricks to cross.
        --- step wise solution ---
        1) create a hashmap to store the positions of the intersections and
        their frequencies.
        2) traverse each row of the wall.
        3) for each row, calculate the cumulative sum of brick widths.
        4) for each cumulative sum (excluding the last brick edge), update
        the hashmap with the count of intersections.
        5) find the maximum count of intersections from the hashmap.
        6) subtract the maximum count from the total number of rows to get
        the minimum number of bricks to cross.
        """
        count_gap = {0: 0}  # default 0 if not gap found
        for brick_row in wall:
            cur_gap = 0
            for brick in brick_row[:-1]:
                cur_gap += brick
                count_gap[cur_gap] = count_gap.get(cur_gap, 0) + 1

        return len(wall) - max(count_gap.values())


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
