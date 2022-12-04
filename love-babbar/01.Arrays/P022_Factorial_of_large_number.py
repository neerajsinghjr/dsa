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
    
    def factorial(self, num):
        # base case
        if not num: return num

        # main case 
        return self.fact(num)
    
    
    def _factorial(self, num):
        # carry,res = 0,[1]           # Initially, 1 only
        res = [1]
        
        x = 2
        while(x <= num):
            carry = 0
            for i in range(len(res)):
                fact = res[i]*x + carry
                res[i] = fact % 10              # Zeroes's place digit;
                carry = fact // 10              # One's place
            
            while(carry):
                res.append(carry)
                carry //= 10
            
            x += 1                              # Increament x 
            
        res.reverse()
        return res


    # Optimized : Carry Bit Multiplication
    def factV2(self, num):
        res = [None]*500           # max
        temp, res[0], resSize = "",1,1

        x = 2                       # initialy, 
        while(x <= num):
            resSize = self.multiply(x, res, resSize)
            x += 1
        
        i = resSize - 1
        while(i >= 0):  
            temp += str(res[i])
            # sys.stdout.write(str(res[i]))
            # sys.stdout.flush()
            i = i - 1
        return temp

    
    def multiply(self, x, res, resSize):
        i = carry = 0
        while(i < resSize):
            prod = res[i]*x + carry 
            res[i] = prod % 10    
            carry = prod // 10
            i += 1
        while(carry > 0):
            res[resSize] = carry % 10
            carry = carry // 10
            resSize += 1
        return resSize

    # Brute Force Approach
    def factorialV1(self, nums, n):
        pass


def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = obj.factorial(num=5)
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
    