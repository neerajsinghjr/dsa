'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1706. Where Will the Ball Fall
-> Problem Status: Completed
-> Problem Attempted: 1/11/2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You have a 2-D grid of size m x n representing a box, and you have n balls.
The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell
that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the
bottom-right corner and is represented in the grid as 1. A board that
redirects the ball to the left spans the top-right corner to the bottom-left
corner and is represented in the grid as -1. We drop one ball at the top of
each column of the box. Each ball can get stuck in the box or fall out of the
bottom. 

A ball gets stuck if it hits a "V" shaped pattern between two boards
or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball
falls out of at the bottom after dropping the ball from the ith column at the
top, or -1 if the ball gets stuck in the box.

Example 1:



Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.
Example 3:

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
----------------------------------------------------------------------------------------------------
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
    
    ###--- Main Execution;
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        if(m == n == 1):
            return [-1]
        
        return self.ansv1(grid, m, n)
    
    
    """
    Run: Accepted
    Code: Brute Force | T: O(M*N) | S:O(N)
    Study:
    idea: we can simulate the movement of each ball
    if a ball is stuck at some point, then it would be -1
    otherwise, get the final destination column

    """
    def ansv1(self, grid, m, n):
        res = []    # holding result;
        # Increase by column traversing...
        for col in range(n):
            # Initialised with current position i.e, current column
            cur_col = col

            # Increase by row traversing...
            for row in range(m):
                # next position is current column value + next column value;
                nex_col = cur_col + grid[row][cur_col]
                
                # ball will trap only when the current col value is not same 
                # as next column value, or if they're opposite to each other
                # check image.
                if(nex_col < 0 or nex_col >= n or grid[row][cur_col] != grid[row][nex_col]):
                    cur_col = -1
                    break
                
                # Update col for next iteration;
                cur_col = nex_col
                
            res.append(cur_col)
        
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
    