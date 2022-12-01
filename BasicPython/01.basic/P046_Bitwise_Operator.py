'''
-------------------------------------------------------------------------------------
-> Title: Bitwise Operator
-> Attempted: 27/11/2022
-> Description: 
-------------------------------------------------------------------------------------
Bitwise Operator :
Main operator includes 
- bitwise or (|)
- bitwise and (&)
- bitwise xor (^)
- bitwise 

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

#--- Example 1: Check even or odd;

def example1():
    # Find if a number is even or odd using & operator
    nums = [45, 21, 34, 64, 4, 97, 24]

    for num in nums:
        if(num & 1) : # <-- add condition here
            print(f"{num} is odd")
        else:
            print(f"{num} is even")

#--- /Example 1;;

#--- Example 2: 

def example2():
    # Modify an even number by adding 1 and making it odd
    nums = [45, 21, 34, 64, 4, 97, 24]

    for num in nums:
        # Odd Number : Ignore it
        # Even number : num + 1
        result = num | 1
        print(f"{num} is now {result}")

#--- /Example 2;;

#--- Example 3 : Check Unique Values in list;

# Find the unique number from the list

def example3_v1():
    nums = [
        34, 3, 64, 33, 22, 574, 74, 
        6, 3, 2, 574, 43, 33, 789, 
        6, 64, 43, 22, 789, 34, 2
    ]    
    i,result = 0,0
    
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        status = nums[i] ^ nums[j]
        # Status : 0 means number is duplicate;
        if(status == 0):
          break
      # status not 0 means loop iterated success and unique number is found;
      if(status != 0):
        result = nums[i]
        break

    print(f"Result : {result}")


def example3_v2():
    nums = [
        34, 3, 64, 33, 22, 574, 74, 6, 3, 2, 574, 
        43, 33, 789, 6, 64, 43, 22, 789, 34, 2
    ]
    result = 0
    for num in nums:
        print("Current num :", num)
        result ^= num
        print(f"current result:", result)

    print("Result :", result)

#--- /Example 3

##---Main Execution;;
def main(res=None):
    example3_v2()
    # example3_v1()
    # example2()
    # example1()
 
if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    
