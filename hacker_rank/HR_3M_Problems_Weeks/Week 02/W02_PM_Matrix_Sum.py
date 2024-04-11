'''
Problem Description:
Sean invented a game involving a 2n * 2n matrix where each cell of the matrix contains an integer. 
He can reverse any of its rows or columns any number of times. The goal of the game is to maximize 
the sum of the elements in the n * n submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for q matrices, help Sean reverse the rows and columns of each 
matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant 
is maximal.

Example
matrix = [[1,2],[3,4]]
1 2
3 4
It is 2*2 and we want to maximize the top left quadrant, a 1*1 matrix. Reverse row 1:

1 2
4 3
And now reverse column 0:

4 2
1 3
The maximal sum is 4.

# Function Description

Complete the flippingMatrix function in the editor below.

flippingMatrix has the following parameters:
- int matrix[2n][2n]: a 2-dimensional array of integers

# Returns
- int: the maximum sum possible.

#Input Format

The first line contains an integer q, the number of queries.

The next q sets of lines are in the following format:

The first line of each query contains an integer, n.
Each of the next 2n lines contains 2n space-separated integers matrix[i][j] in row i of the matrix.

#Constraints
1 <= q <= 16
1 <= n <= 128
0 <= matrix[i][j] <= 4096, where 0 <= i,j < 2n.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def matrixSumV1(nums):
    start,end = 0,len(nums)
    temp, n = [],end//2
    while(start <= end):
        x,y = start,end
        for():
            begin,stop = 0, 
            max(max(nums[x][i],nums[x][j]))

    



def main():
    try:
        nums = [
            [119,42,83,119],
            [56,125,56,49],
            [15,78,101,43],
            [62,98,114,108],
        ]
        res = matrixSumV1(nums)
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    