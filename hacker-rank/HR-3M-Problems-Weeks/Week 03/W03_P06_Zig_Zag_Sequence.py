'''
Problem Description:
In this challenge, the task is to debug the existing code to successfully 
execute all provided test files.

Given an array of 'n' distinct integers, transform the array into a 
zig zag sequence by permuting the array elements. A sequence will 
be called a zig zag sequence if the first  elements in the sequence 
are in increasing order and the last  elements are in decreasing order,
where k=(n+1)/2. 

You need to find the lexicographically smallest zig zag sequence of the given array.

Example: 
a = [2,3,5,1,4]
Now if we permute the array as , the result is a zig zag sequence.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence 
for the given input array.

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.

To restore the original code, click on the icon to the right of the language selector.

//----------- Begins
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    st = mid + 1
    ed = n - 2
    
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
//------------- Ends
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def findZigZagSequence(a, n):
    a.sort()
    mid = int(n/2)      # ~ Change 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2          # ~ Change 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1     # ~ Change 3

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


def main():
    try:
        res = ""
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
    