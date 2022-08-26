'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 326. Power of Three
-> Problem Status: Completed
-> Problem Attempted: 24.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.


Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:
1) -231 <= n <= 231 - 1

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
    #--- Main Execution;;
    def isPowerOfThree(self, n: int) -> bool:
        
        if(n == 0):
            return False
        
        # return self.ansv1(n)
        # return self.ansv2(n)
        return self.ansv3(n)
    
    
    """
    Code: Optimised | T:(1) | S:O(1)
    Study:
    One-liner (O(1)):
    1) Because 3^19(1,162,261,467) is the largest power of three under 2^31(2,147,483,648) - 1,
    for eg, 3^20(3,486,784,401) > 2^31(2,147,483,648)
    2) So we just need to check if n > 0 and whether3^19 % n is 0

    """
    def ansv3(self,n):
        return (n > 0) and (1162261467 % n == 0)
    
    
    """
    Code: Loop | T:(1) | S:(1)
    Study:
    Simple loop checking for modulo remainder and each iteration
    reducing the $n size by $n//3.
    """
    def ansv2(self,n):
        if(n == 1):
            return True
        
        while(n%3 == 0):
            n //= 3
            if(n == 1):
                return True
            
        return False
        
    
    """
    Code: Recursion | T:(1) | S:(1) (+Stack Space)
    Study:
    Simply checking for the multiple of 3, by dividing the number by 3.
    but set the base condition first.
    """
    def ansv1(self,n):
        if(n == 1):
            return True
        
        if(n % 3 == 0):
            return self.ansv1(n//3)
        
        return False


##---Main Execution;;
def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
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
    