'''
-------------------------------------------------------------------------------------
-> Problem Title: 1496. Path Crossing
-> Problem Status: Completed
-> Problem Attempted: 13/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/path-crossing/description/

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

    def isPathCrossing(self, path: str) -> bool:
        """
        _stdin:
            arg1: str
        _stdout: bool
        """
        return self._ansv1(path)

    def _ansv1(self, path: str):
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 85/85
        _choke: none
        _brief: --- optimized and optimal approach --- 
        - This method determines if a path, traced on a 2D Cartesian plane starting from (0,0), 
        crosses itself at any point.
        - A path crosses itself if it revisits a coordinate that it has been to before.
        - Approach:
            - It simulates the traversal by tracking the current (x, y) coordinates.
            - A set named x_map (used as visited_points) is maintained to store all unique 
            coordinates visited so far. The origin (0,0) is added to this set initially.
            - For each character in the path string ('N', 'S', 'E', 'W'), the (x, y) coordinates 
            are updated accordingly.
            - After each move, the new (x, y) coordinate is checked against the visited_points 
            set. If the coordinate is already in the set, it means a crossing has occurred, and the 
            method immediately returns True.
            - If the new coordinate has not been visited, it is added to the visited_points set.
        - If the entire path is traversed without detecting any revisited points; returns False
        """
        x, y = 0, 0
        x_map = {(x,y)} # visited point - (0,0)

        for p in path:
            if p == 'N':
                y += 1  # North: Increase Y
            elif p == "S":
                y -= 1  # North: Decrease Y
            elif p == "E":
                x += 1  # East: Increase X
            else:
                x -= 1  # West: Decrease X
            cur_path = (x,y)
            if cur_path in x_map:
                return True
            x_map.add(cur_path)

        return False


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
