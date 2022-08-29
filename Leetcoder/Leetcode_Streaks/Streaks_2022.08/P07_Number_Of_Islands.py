'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 200. Number of Islands
-> Problem Status: Completed
-> Problem Attempted: 29.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the 
number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

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
from collections import deque

class Solution:
    
    ###---Main Execution;;;
    def numIslands(self, grid: List[List[str]]) -> int:
        if(grid == None):
            return 0
        
        rows,cols = len(grid),len(grid[0])
        
        # return self.ansv1(grid,rows,cols)
        return self.ansv2(grid,rows,cols)
    
    
    """
    Run: Success
    Code: BFS approach | T:O(N*M) | S:O(1)
    Study:
    This approach also works like DFS in ansv1() but little bit difference
    as in this solution we use queue to hold all pair of index of 1 and while
    iterating all the neighbour of the particular index in search of 1 and 
    marking the visited node as -1.
    """
    def ansv2(self,grid,rows,cols):
        islands = 0
        
        def bfs(x,y):              
            que = deque()
            que.append((x,y))
            while(que):
                r,c = que.popleft()
                dirs = [(-1,0), (1,0), (0,-1), (0,1)]
                grid[r][c] = -1             # Marked Island as Visited;
                for dr,dc in dirs:
                    nexR,nexC = r+dr,c+dc           # nexR and nexC is next row and col index with value 1;
                    if(nexR in range(rows) and nexC in range(cols) and grid[nexR][nexC] == "1"):
                        que.append((nexR,nexC))
                        grid[nexR][nexC] = -1
                        
            return # bfs();;
                    
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1"):
                    bfs(r,c)
                    islands += 1
        
        return islands
    
    
    """
    Run: Success
    Code: DFS Approach | T:(N*M) | S:(1) + Stack(N*M)
    Study:
    In this approach, we are just simple following the DFS approach
    1) First we trace the single item, make DFS call
    2) Set the current index of grid as visted, 
    3) Again make DFS() call with top,bottom,left,right.
    """
    def ansv1(self,grid,rows,cols):
        islands = 0
        
        def dfs(r,c):
            # Choke 1: Check for rows index
            if(r < 0 or r >= rows): return
            
            # Choke 2: Check for cols index
            if(c < 0 or c >= cols): return
            
            # Choke 3: Check for visited;
            if(grid[r][c] != "1"): return
            
            grid[r][c] = -1         # Mark the current indices as visited;
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            return # dfs();;
        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1"):
                    dfs(r,c)
                    islands += 1
        
        return islands
                
        


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
    