'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 12. Integer to Roman
-> Problem Status: Ongoing...
-> Problem Attempted: 20/10/2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
subtract it making four. The same principle applies to the number nine, which is written as IX. 

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
Accepted
872,366
Submissions
1,421,383
----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


"""
Approach Solution:
#1 Subtraction Method:
#2 Division Method:
"""

class Solution:
    
    def intToRoman(self, num: int) -> str:
        romansMap = {
            1000: "M", 900: "CM",500: "D",400: "CD",100: "C",           # Thousands;
            90: "XC",50: "L",40: "XL",                                  # Tens 
            10: "X",9: "IX",5: "V",4: "IV",1: "I"
        }
        
        # base case;
        if(num in romansMap):
            return romansMap[num]
        
         # return self.ansv1(num, romansMap)
        return self.ansv2(num, romansMap)

    
    """
    Run: Accepted
    Code: Brute Force | Time: O(K*N) | S:O(K)
    Study:
    Subtraction method : First brute force solution to this problems. 
    In this solution, we are statically mapping the romans numbers to 
    their decimal weightage and when we are subtracting the number on 
    the basis of the required key.
    """
    def ansv1(self, num, romansMap):
        res = ""
        while(num):
            for key,value in romansMap.items():
                if(key <= num):
                    res += value
                    num -= key
                    break       # no need to further iterate;

        return res
        
    
    """
    Run: Accepted
    Code: Optimised (Divide)
    Study:
    Same as in ansv1() but implemented using divide
    """
    def ansv2(self, num, romansMap):
        res = ""
        while(num != 0):
            for (key,value) in romansMap.items():
                if(key <= num):
                    rem = num // key
                    for x in range(rem):
                        res += value
                    num %= key
                    break
    
        return res
                        

##---Main Execution;;
def main(res=None):
    try:
        print(f"res: {res}")
        
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
    