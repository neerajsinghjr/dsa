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
    