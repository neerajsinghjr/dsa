'''
-------------------------------------------------------------------------------------
-> Problem Title: Possbile To Form Rectangle
-> Problem Status: Completed
-> Problem Attempted: 05/06/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381879?leftPanelTab=0

# DEGENERATE TRIANGLE CONCETPS :-

Non-degenerate triangle − it is a triangle that has a positive area. The
condition for a non-degenerate triangle with sides a, b, c is ...

a + b > c
a + c > b
b + c > a

eg1: Let’s take an example to understand the problem better −

Input − arr[2, 5 ,9, 4, 3]
Output − Yes

Explanation 1: The triangle formed is 2 3 4.

To solve this problem, we will check that the above condition is satisfied by
the values of the array.

# BRUTE FORCE APPROACH : A navie solution will involve direct checking of
  every triplet of the array.

# OPTIMISE APPROACH : A more effective solution will involve sorting the array
  elements and the checking three consecutive triplets of the array. As for
  sorted array if the sum of two elements is not greater than the next one
  check values after that is not worthy (they are already large).

Explanation 2: 

When you have three side lengths satisfying a ≤ b ≤ c and the sum a + b = c,
then the triangle is degenerate.

(Valid triangles have a + b > c and triangles with a + b < c are not possible.)
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
def possibleToMakeTriangle(arr):
    n = len(arr)
    if n < 3:
        return False
    arr.sort()  # nlogn
    for i in range(n-2):
        two_sides = arr[i]+arr[i+1]
        if two_sides > arr[i+2]:
            return True
    return False


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