'''
Problem Description:
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:

    def getMap(self):
        hash = {}
        hash['2'] = "ABC"
        hash['3'] = "DEF"
        hash['4'] = "GHI"
        hash['5'] = "JKL"
        hash['6'] = "MNO"
        hash['7'] = "PQRS"
        hash['8'] = "TUV"
        hash['9'] = "WXYZ"
        return hash


    # ___Main Function___
    def phoneNumber(self,digits):
        # base case;
        if not digits: return digits

        # main case;
        res = []                                                # res : result
        map = self.getMap()                                     # map : hash => Value
        # return self.bruteForce(digits, len(digits), map)  
        return self.backtracking(digits,map,0,res,"")              # startIdx : 0


    # Method 1 : Brute Force;
    def bruteForce(self, digits,size, map):
        res = []
        for i in range(size):
            keystr = map[digits[i]]            # hash values;
            for j in keystr:
                temp += j
                for k in range(j+1, x):
                    temp = keystr[j]+keystr[k]
            res.append(temp)
        return res


    # Method 2 : Recursion Backtracking
    def backtracking(self, digits, map, startIdx, res, temp):
        # base case
        if(startIdx == len(digits)):
            res.append(temp)
            return 
        # main case
        if not (digits[startIdx] in "*#01"):
            curStr = map[digits[startIdx]]
            for i in range(len(curStr)):
                temp += curStr[i]
                self.backtracking(digits, map, startIdx+1, res, temp)
                temp = temp[0:len(temp)-1]
        else:
            self.backtracking(digits, map, startIdx+1, res, temp)

        return res


def main():
    try:
        data = "233*"               # ~ data
        obj = Solution()
        res = obj.phoneNumber(data)
        print(res) if res else print("Empty!")
        
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
    