'''
-------------------------------------------------------------------------------------
-> Problem Title: 200. Number of Islands
-> Problem Status: Completed
-> Problem Attempted: 04/03/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

Given an m x n 2D binary grid grid which represents a map of '1's
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

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

-------------------------------------------------------------------------------------
'''


#!/bin/python3

import os
import re
import sys
import time
import math
import random


from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        return self.searchIsland(grid, rows, cols)


    def searchIsland(self, grid, rows, cols):
        count = 0
        for rc in range(rows):
            for cc in range(cols):
                if(grid[rc][cc] == '1'):
                    count += 1
                    self.bfs(grid, rc, cc, rows, cols)  # BFS;;
                    # self.dfs(grid, rc, cc, rows, cols)  # DFS;;

        return count


    def bfs(self, grid, rc, cc, rows, cols):
        que = deque()
        que.append([rc,cc])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while(que):
            coord = que.popleft()
            for (new_r, new_c) in dirs:
                nex_r, nex_c = new_r+coord[0], new_c+coord[1]
                if (0 <= nex_r < rows) and (0 <= nex_c < cols) and grid[nex_r][nex_c] == '1':
                    que.append((nex_r, nex_c))
                    grid[coord[0]][coord[1]] = '-1'
 

    def dfs(self, grid, cur_r, cur_c, rows, cols):
        grid[cur_r][cur_c] = '-1'
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        for (new_r,new_c) in dirs:
            nex_r, nex_c = cur_r+new_r, cur_c+new_c
            if (0 <= nex_r < rows) and (0 <= nex_c < cols) and grid[nex_r][nex_c] == '1':
                self.dfs(grid, nex_r, nex_c, rows, cols)

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