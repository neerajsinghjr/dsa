'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Bitmap Manipulations Expl
-> Problem Status: Ongoing...
-> Problem Attempted: 18/10/2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Notes :


----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


def bitwise():
    print("Ex1:",12 << 2) # value increasing
    print("Ex2:", 12 >> 2) # values decreasing
    
    """
    Right shift: Divide by 2 follows up under the hood
    for eg,
        5 -> 101
        5 >> 2 -> 001   (~ 2)
    
    Left shift : Multiply by 2 follows up under the hood
    for eg,
        5 -> 101
        5 << 2 : 10100
    """
    print("Ex3:", 5 << 3)


def checkOdd(num):
    """
    Remember 1 : Even value have special value of 0 at the end;
    Remember 2 : Odd value have spaecial value of 1 at the end;
    
    so whenever you will perform bit and operation of above
    result would be like this ...
    
    EVEN & 1 :- 0 if(even == True) else 1
    """
    res = num & 1
    return (True if(res == 0) else False)


def swap(a,b):
    """
    Naive Logic;
    a: 5, b: 12
    a = b - a => a = 12 - 5 => 7
    b = b - a => b = 12 - 7 => 5
    a = a + b => a = 7 + 5 => 12
    """
    # Suppose intially a: 101 ~ (5), b: 111 ~ (7)
    print(f"before swap -> a: {a}, b: {b}")
    a = a ^ b       # a: 101, b:111 -> a = a ^ b -> a = 010 ~ (2)
    b = a ^ b       # a: 010, b:111 -> b = a ^ b -> b = 101 ~ (5)
    a = a ^ b       # a: 010, b:101 -> a = a ^ b -> a = 111 ~ (7)
    print(f"after swap -> a: {a}, b: {b}")


def leftshift():
    """_summary_
    leftshift() : divide by 2^n.
    """
    print(36>>1)        # 36 / 2^1 : 18
    print(36>>2)        # 36 / 2^2 : 9
  
   
def rightshift():
    """_summary_
    rightshift(): multiplication by 2^n.
    """
    print(36<<1)        # 36 x 2^1 : 72 
    print(36<<2)        # 36 x 2^2 : 144


def xor():
    print("^ : ", 5^5)
    print("^ : ", 15^15)
    print("^ : ", 200^200)
    print("^ : ", 500^500)
    print("~^ : ", 5^~5)
    print("~^ : ", 15^~15)
    print("~^ : ", 200^~200)
    print("~^ : ", 500^~500)
    print("^1 : ", 5^1)
    print("^1 : ", 15^1)
    print("^1 : ", 200^1)
    print("^1 : ", 500^1)
   
   
def andbit():
    print("^ : ", 5^5)
    print("^ : ", 15^15)
    print("^ : ", 200^200)
    print("^ : ", 500^500)
    
   
##---Main Execution;;
def main(res=None):
    try:
        andbit()
        
        # xor()
        
        # leftshift()
        # rightshift()
        
        # swap(a=12, b=13)
        # res = checkOdd(00)
        # bitwise()
        
        # if res: print(f"res: {res}")
        
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
    