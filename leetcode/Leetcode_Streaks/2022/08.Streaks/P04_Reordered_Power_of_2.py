'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 869. Reordered Power of 2
-> Problem Status: Completed
-> Problem Attempted: 26.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are given an integer n. We reorder the digits in any order (including the original order) such 
that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:
Input: n = 1
Output: true
Explanation: 1 is power of 2.

Example 2:
Input: n = 10
Output: false
Explanation: 10 is not a power of 2.

Example 3:
Input: n = 34
Output: false
Explanation: Neither 34 is not power of 2, nor 43 is power of 2.

Example 4:
Input: n = 10
Output: false
Explanation: Neither 10 is not power of 2, nor 43 is power of 2.

Example 5:
Input: n = 46
Output: True
Explanation: 46 is not power of 2 but 64 is power of 2.


Constraints
1) 1 <= n <= 10^9
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
from collections import Counter

class Solution:
    
    #---Main Execution;;
    def reorderedPowerOf2(self, n: int) -> bool:
        if(n == 1):
            return True
        
        if(n == 2):
            return True
        
        # return self.ansv1(n)
        # return self.ansv2(n)
        return self.ansv3(n)
    
    
    """
    Run: Success
    Code: Optimised | T:O(K) | S:O(K)
    Study:
    In this appproach, we are going to calculate all the power of 2 under the 
    limits of 10^9 which is of base 10 but in terms of base 2. For smaller base
    it can adpat the power of 2^29 < 10^9.
    - After calculating the power till 2^29 which is lesser than 30 in numbers.
    - Make sure to convert the integer to string before hand, which is beneficial 
    for using Counter function on them. 
    - Return True if matched else False;
    
    """
    def ansv3(self,n):
        count = Counter(str(n))
        for i in range(2,30):                   # 2^29 < 10^9 i.e Calculated Data;;
            num = str(pow(2,i))
            if(count == Counter(num)):
                return True
            
        return False
            
            
    """
    Run: Failed
    Code: Brute Force | T:O(1) | S:O(1)
    Study:
    This approach simple calculating the power of a given single number recursively but
    not able to handle the shuffing of the number (See Example 5)
    """    
    def ansv2(self,n):
        if(n == 1):
            return True
        if(n%2 != 0):
            return False
        
        return self.ansv2(n//2)
    
    
    """
    Run: FAILED
    Code: Brute Force | T:O(1) | S:O(1)
    Study:
    This approach simple calculating the power of a given single number iteratively but
    not able to handle the shuffing of the number (See Example 5)
    
    """
    def ansv1(self,n):
        while(n%2 == 0):
            if(n == 1):
                return True
            n = n // 2
        
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
    