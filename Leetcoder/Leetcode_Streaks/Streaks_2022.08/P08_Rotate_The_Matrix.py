'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Rotate the grid at 90
-> Problem Status: Completed
-> Problem Attempted: 30.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
    ###---Main Execution;;
    def rotate(self, grid: List[List[int]]) -> None:
        if not(grid):
            return grid
        
        rows,cols = len(grid),len(grid[0])
        
        return self.ansv1(grid,rows,cols)
            
    
    """
    Run: Success
    Code: Brute Force | T:O(M*N+M*N) | S:(1)
    Study:
    Quite Simple approach for rotating any matrix to 90 degree...
    $$$ Rotate(90) = Grid -> Transpose -> Reverse (Vice Versa) $$$
    
    1) For Transposing...
    Iterate two loop one for rows and other for cols but make sure to
    run the second loop lesser the current iterating rows only,
    Otherwise it's gonna transpose twice the same element and alternatively
    giving the same grid again.
    
    NOTE: Always run the second loop lesser than the first loop;
    
    2) For Reversing...
    Simple iterate for rows, and reverse using two pointer approach or
    pre-defined sort function, anything.
    
    """
    def ansv1(self,grid,rows,cols):
       
        # S1: Transpose;;
        for r in range(rows):               # till $rows;
            for c in range(r):              # till $r;
                if(r != c):
                    grid[r][c],grid[c][r] = grid[c][r],grid[r][c]
        
        # S2: Reverse;;
        for r in range(rows):
            start,end = 0,cols-1
            while(start <= end):
                grid[r][start],grid[r][end] = grid[r][end],grid[r][start]    
                start += 1
                end -= 1    
        
        return grid


##---Main Execution;;
def main():
    try:
        # data = []               # ~ data
        # obj = Solution()
        # res = ""
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
    