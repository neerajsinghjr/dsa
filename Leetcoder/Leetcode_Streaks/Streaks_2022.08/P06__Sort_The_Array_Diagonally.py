'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1329. Sort the Matrix Diagonally
-> Problem Status: Completed
-> Problem Attempted: 28.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or 
leftmost column and going in the bottom-right direction until reaching the matrix's end. 

For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes 
cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return 
the resulting matrix.

 
Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example 2:
Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
 


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

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
    
    ###---Helpers
    def countSort(self,grid,m,n,x,y):
        count = [0]*101         # grid[i][j] <= 100;
        
        i,j = x,y
        while(i < m and j < n):
            count[grid[i][j]] += 1
            i,j = i+1,j+1
        
        i,j = x,y
        for z in range(101):
            while(count[z] > 0):
                grid[i][j] = z
                i,j = i+1,j+1           # Diagonal++
                count[z] -= 1           # count--
        
        return grid
    
    
    ###---Main Solution;;;
    def diagonalSort(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        
        if(m == 1 and n == 1):
            return grid
        
        # return self.ansv1(grid,m,n)
        return self.ansv2(grid,m,n)
    
    
    """
    Run: Ongoing ...
    Code: Optimised | T:O(N) L S:(N)
    Study:
    Same algorithm as used in solution(~ansv1()), but little optimization in sorting
    because the constraints says, 1 <= grid[i][j] <= 100, for small finite number.
    
    There is a best algorithms which can optimize the sorting from O(n*LogN) => O(N)
    namely counting sort or bucket sort;
    
    1) Iterate over the same grid
    2) Sort using countSort when $i == 0 or $j == 0, only
    3) Implement countSort, then sort diagonally and store
    inside same grid;
    """
    def ansv2(self,grid,m,n):
        i = 0
        while(i < m):
            j = 0
            while(j < n):
                if(i == 0 or j == 0):           # Only for 0's index rows and cols;
                    self.countSort(grid,m,n,i,j)
                j += 1      # column++
            i += 1      # row++
                
        return grid
    
    
    """
    Run: Success
    Code Brute Force | O(N*NLogN) (N:Diagonals) | O(N)
    Study:
    Simple solution,
    1) Traverse diagonally in matrix and store inside list;
    2) Sort the items inside the list
    3) Traverse the same loop again, store the sorted matrix item
    """
    def ansv1(self,grid,m,n):
        r = 0
        
        # S1: Sort By Rows;
        while(r < m):   # Traverse -> Diagonal -> Sort;
            temp = []
            i,j = r,0
            while(i < m and j < n):
                temp.append(grid[i][j])
                i,j = i+1,j+1
            
            temp.sort()
            
            i,j,idx,count = r,0,0,len(temp)
            while(i < m and j < n and idx < count):
                grid[i][j] = temp[idx]
                i,j,idx = i+1,j+1,idx+1
                
            r += 1
        
        #S2: Sort By Columns;
        c = 1
        while(c < n):   
            temp = []
            i,j = 0,c
            while(i < m and j < n):
                temp.append(grid[i][j])
                i,j = i+1,j+1
            
            temp.sort()

            i,j,idx,count = 0,c,0,len(temp)
            while(i < m and j < n and idx < count):
                grid[i][j] = temp[idx]
                i,j,idx = i+1,j+1,idx+1
            
            c += 1        
            
        return grid
        

##---Main Execution;;
def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
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
    