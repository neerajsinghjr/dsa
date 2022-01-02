'''
Problem Description:
Given an array of stick lengths, use  of them to construct a non-degenerate 
triangle with the maximum possible perimeter. Return an array of the lengths
of its sides as  integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

1) Choose the one with the longest maximum side.
2) If more than one has that maximum, choose from them the one with the longest minimum side. 
3) If more than one has that maximum as well, print any one them.

If no non-degenerate triangle exists, return [-1]

Example:
The example states that the array [1,2,3,4,5,10], contains the triangles:
a) 1,2,3 ([0,1,2]).
b) 2,3,4 ([1,2,3]).
c) 3,4,5 ([2,3,4]).
d) 4,5,10 ([4,5,10]).

So far, so good. However, the example considers also the array e) 2,3,5 ([1,2,4]).

That implies that there are some other triangles that should be considered: 
[0,1,3], [0,1,4], [0,1,5], [1,2,4], etc.    

Note:
If a, b, and c are the lengths of the three sides of a triangle, then...
a + b > c
a + c > b
b + c > a
otherwise, it is a degenerate triangle.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def maximumPerimeterTriangle(sticks):
    s = sorted(sticks,reverse=True)
    for i in range(len(sticks)-2):
        if(s[i] < s[i+1] + s[i+2]):
            return (s[i+2],s[i+1],s[i])
    return [-1]


def main():
    try:
        data = [1,2,3,2,4,5,10]
        res = maximumPerimeterTriangle(data)
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
    