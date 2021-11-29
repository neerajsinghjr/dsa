'''
Problem Description:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example,
The square matrix arr is shown below:
1 2 3
4 5 6
9 8 9  

The left-to-right diagonal, 1 + 5 + 9 = 15
The right to left diagonal, 3 + 5 + 9 = 17

Result, |15 - 17| = 2  (Absolute Difference)

Inputs: arr[n][m] matrix;

Outputs: Integer : Absolute Difference of Type INT;
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here



def main():
    try:
        res = ""
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Program Stopped: {e}")
    
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
    