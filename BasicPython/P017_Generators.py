#!/bin/python3

import os
import re
import sys
import time
import math
import random


"""
"""
def hunderNumberV2(n):
    i = 0
    while(i < 100):
        print("before special line...")
        yield i                 # Special 
        print("after special line...")
        i += 1


"""
Insufficient: Taking More RAM or Memory Space;;
"""
def hundredNumbers(n):      # n : 4 * 100 x 10,00,000 
    res = []
    for i in range(n):
        res.append(i)

    return res 
        

##---Main Execution;;
def main():
   # nums = hundredNumbers(100)
   nums = hunderNumberV2(100)

   print(f"nums: {nums}")                        # generator object;
   print(f"current number: {next(nums)}")          # here 1: Output: 0
   print(f"current number: {next(nums)}")          # here 2: Output: 1
   print(f"current number: {next(nums)}")          # here 3: Output: 2

    # List Comprehension
    # nums = [n for n in range(100)]
    # print(f"nums -> obj: {nums}")               # direct list;;
    # print(f"nums -> list: {list(nums)}")    

    # Generator Comprehension;;
    # nums = (n for n in range(100))    
    # print(f"nums -> obj: {nums}")
    # print(f"nums -> list: {list(nums)}")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
