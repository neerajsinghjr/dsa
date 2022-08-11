'''
#Day 01 : 24 June 2022;

#Problem 01: Set Matrix Zeroes;

#Problem Description: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# APPROACH (BAD) || TIME: O(N*M) || SPACE: O(1)
def setZeroes_v1(matrix):
    i, rows, cols = 0, len(matrix), len(matrix[0])
    while(i < rows):
        j = 0
        while(j < cols):
            if(matrix[i][j] == 0):
                # row -> left;
                index = i-1
                while(index >= 0):
                    matrix[index][j] = -1
                    index -= 1

                # row -> right;
                index = i+1
                while(index < rows):
                    matrix[index][j] = -1
                    index += 1

                # cols -> top;
                index = j-1
                while(index >= 0):
                    matrix[i][index] = -1
                    index -= 1

                # cols -> bottom;
                index = j+1
                while(index < cols):
                    matrix[i][index] = -1
                    index += 1

            j += 1        # cols ++
        i += 1            # rows ++

    # Step 2: Set -1 value to Zeroes;
    i = 0
    while(i < rows):
        j = 0
        while(j < cols):
            if(matrix[i][j] == -1):
                matrix[i][j] = 0
            j += 1
        i += 1

    return matrix


# APPROACH (BETTER) || TIME: O(N*M) || SPACE: O(N*M)
def setZeroes_v2(matrix):
    zRows = []
    zCols = []
    i, rows, cols = 0, len(matrix), len(matrix[0])

    # Step 1: Set zeroes rows and cols;
    while(i < rows):
        j = 0
        while(j < cols):
            if(matrix[i][j] == 0):
                zRows.append(i)
                zCols.append(j)
            j += 1
        i += 1

    print(f"rows : {rows} // cols : {cols}")
    print(f"zRows: {zRows} // zCols: {zCols}")

    ## Step 2: Set the rows and cols;
    row = 0
    while(row < rows):
        if row in zRows:
            i = 0
            while(i < cols):
                matrix[row][i]= 0
                i += 1
        row += 1

    col = 0
    while(col < cols):
        if col in zCols:
            i = 0
            while(i < rows):
                matrix[i][col] = 0
                i += 1
        col += 1

    return matrix


# APPROACH (BETTER) || TIME: O(N*M) || SPACE: O(N*M)
def setZeroes_v3(matrix):
    pass


##--- Main Execution ---##
def main():
    try:
        data = [
            [0,2,0],
            [2,3,4],
            [3,8,7],
            [2,9,0]
        ]

        print("Before...")
        for d in data:
            print(d)

        res = setZeroes_v1(data)
        # res = setZeroes_v2(data)
        # res = setZeroes_v3(data)

        print("After...")
        for r in res:
            print(r)


    except(Exception) as e:
        print(f"Exception Traced: {e}")
        exit(1)

    else:
        print("Program Completed: Success")

    finally:
        print("Program Terminated!")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Ends ----------------#")
