'''
-------------------------------------------------------------------------------------
-> Problem Title: 931. Minimum Falling Path Sum
-> Problem Status: Ongoing...
-> Problem Attempted: 2022-12-13
-> Problem Description: 
-------------------------------------------------------------------------------------

Given an n x n array of integers matrix, return the minimum sum of any falling
path through matrix.

A falling path starts at any element in the first row and chooses the element
in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1,
col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13

Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59

Explanation: The falling path with a minimum sum is shown.
 

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

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
    
    # Constructor;
    def __init__(self):
        pass


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
    