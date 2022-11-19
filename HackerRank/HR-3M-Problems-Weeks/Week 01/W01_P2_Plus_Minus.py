'''
Problem:
Given an array of integers, calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a new line with  
places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, 
though answers with absolute error of up to 10^(-4) are acceptable.

for eg,
arr= [1,1,0,-1,-1]
output: 
positive: 0.400000
negative: 0.400000
zeroes:   0.200000
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

## Main Working Function
def plusMinus(arr):
    total = positive = zero = negative = 0
    for val in arr:
        if val > 0:
            positive += 1
        elif val == 0:
            zero += 1
        else:
            negative += 1
        total += 1            
    print(f"{positive/total:.6f}")
    print(f"{negative/total:.6f}")
    print(f"{zero/total:.6f}")


def main():
    res = ""
    print(res) if res else print("Empty!")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    