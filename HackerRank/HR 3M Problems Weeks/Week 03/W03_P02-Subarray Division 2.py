'''
Problem Description:
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

# Example
# Input :
s = [2,2,1,3,2]
d = 4
m = 2 
# Result : 2
# Explanation : [2,2] == 4 ~ d, [1,3] == 4 ~ d
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def birthday(s, d, m):
    print("s:",s,"d:",d,"m:",m)
    # base cases;
    if(len(s) < m):             # Total Splits < months;
        return 0
    if(len(s) == m):       # Total Splits == months == 1
        return (1 if sum(s) == d else 0)
    # main case;
    i = count = 0
    size = len(s)-2
    while(i<size):
        if(sum(s[i:i+m]) == d):
            count += 1
        i += 1
    return count


def main():
    try:
        data = [ 
            [[2,2,1,3,2], 4, 2], 
            [[1,2,1,3,2], 3, 2 ], 
            [[1,1,1,1,1,1], 4, 2 ],
        ]
        for arr in data:
            res = birthday(arr[0],arr[1],arr[2])
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
    