'''
Problem Description:
'''

#!/bin/python3

from binascii import a2b_base64
import os
import re
import sys
import time
import math
import random
from math import ceil


## Main Working Function, here...
class Solution:

    # Method 1: Big O((n+m)*log(n+m)) using sort approach
    def merge_V1(self, a1, a2, n, m): 
        a1[:] = sorted(a1 + a2)
        a2 = []
        return 


    # Helper for Method 2: Gap
    def _gap(self, gap):
        if(gap <= 1):
            return 0
        return (gap//2) + (gap%2)


    # Method 2: Running Gaps;
    def merge_V2(self, a1, a2, n, m):
        size = n + m
        gap = self._gap(gap=size)
        while(gap > 0):
            # For array ~a1;
            i = 0
            while(i < n):
                if(a1[i] > a1[i+gap]):
                    a1[i], a1[i+gap] = a1[i+gap], a1[i]
                i += 1

            # For array ~a2;
            j = gap-n if gap > n else 0
            while i < n and j < m:
                if (a1[i] > a2[j]):
                    a1[i], a2[j] = a2[j], a1[i]
                i += 1
                j += 1

            if(j < m):
                j = 0
                while((j + gap) < m):
                    if (a2[j] > a2[j + gap]):
                        a2[j], a2[j + gap] = a2[j + gap], a2[j]
                    j += 1
            
            gap = self._gap(gap)        

        return


    # Method 3: Swap x Sort Solution, ~TLE REACHED 
    def merge_V3(self, a1, a2, n, m):
        i = j = 0
        while(i < n and j < m):
            if(a1[i] > a2[j]):              
                a1[i], a2[j] = a2[j],a1[i]
                a2.sort()                   # GFG: TLE Reached
            i += 1
        return None


    # Method 4: Swap + Sort Solution, ~ Better Than Method 3
    def merge_V4(self, a1, a2, n,m):
        # base case 
        if not a1:  return a2
        if not a2:  return a1
        
        # main case
        i = n-1
        j = 0
        while(i >= 0 and j < m):
            if(a1[i] > a2[j]):
                a1[i],a2[j] = a2[j],a1[i]
            i -= 1
            j += 1
        a1.sort()
        a2.sort()        


def main():
    try:
        a1,a2 = [1, 3, 5, 7], [0, 2, 6, 8, 9]
        n, m = len(a1), len(a2)
        obj = Solution()
        # obj.merge_V1(a1,a2,n,m)
        obj.merge_V2(a1,a2,n,m)
        # obj.merge_V3(a1,a2,n,m)
        # obj.merge_V4(a1,a2,n,m)
        print(a1+a2)
        
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
    