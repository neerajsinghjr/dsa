'''
----------------------------------------------------------------------------------------------------
#Problem Title: Longest Band
#Problem Status: Completed
#Problem Attempted: 03-08-2022
#Problem Description:
----------------------------------------------------------------------------------------------------
Given an array containing N integers and find the length of the longest band.

A band is defined as a subsequence which can be re-ordered in such a manner all 
elements appear consecutive (ie with absolute difference of 1 between neighbouring
elements)

A longest band is the band (Subsequence) which contains maximum integer.

for eg,

Input : [1,9,3,0,18,5,2,4,10,7,12,6]
Output : 8

Largest subset containing consecutive numbers is {0,1,2,3,4,5,6,7}

----------------------------------------------------------------------------------------------------
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
    
    def largestBand(self,bands,n):
        if n == 0: return 0

        if n == 1: return 1

        if n == 2 and abs(bands[0]-band[1]) == 1: 
            return 2

        # return self.ansv1(bands,n)
        return self.ansv2(bands,n)


    """
    Analysis: TIME: O(NxLOGN) || SPACE: O(1)
    Approach: In this apprach everything cooked through the sorting. Then simple 
    check values with -1 differences. Then concluded result.
    """
    def ansv2(self,bands,n):
        bands.sort()
        maxCount = -1
        curCount = 1
        for i in range(1,n):
            if(bands[i]-1 == bands[i-1]):
                curCount += 1
                maxCount = max(curCount,maxCount)
            else:
                curCount = 0

        return maxCount


    """
    Analysis : TIME: O(N+N) || SPACE: O(N)
    Approach : In this approach, we take the first element from the band and 
    remember every other element would be +1 or -1 different. Then that means,
    if I look for current band (value-1) in the set or dictionary. Then I would
    get to know whether the current element reside in between some chain or the
    first one in any chain.
    There are two cases originated from this...
        a) if element is in between element,
            then skip it;
        b) If element is the first element,
            then check for next element by +1 to it;

    """
    def ansv1(self,bands,n):
        # NOTE: Python Created Ordered Set by default;
        maxCount = -1               
        dataset = set()
        print(f"bands: {bands}")
        for band in bands:
            dataset.add(band)

        print(f"dataset: {dataset}")

        for i in range(n):
            startBand = bands[i] - 1

            """
            # If current band(~curBand) is an element of in between band; 
            # then, start counting 
            # left <- curBand -> right;
            # and track count;
            """

            if not(startBand in dataset):
                curCount = 0
                curBand = bands[i]
                
                while(curBand in dataset):
                    curCount += 1
                    maxCount = max(curCount, maxCount)
                    curBand += 1
            else:
                continue

        return maxCount


# -- MAIN EXECUTION --#
def main():
    # try:
    data = []               # ~ data
    obj = Solution()
    bands = [1,9,3,18,5,2,4,10,7,12,6]
    res = obj.largestBand(bands,len(bands))
    print(res) if res else print("Empty!")
        
    # except(Exception) as e:
    #     print(f"Exception Traced : {e}")
    
    # else:
    #     print("Program Completed : Success")

    # finally:    
    #     print("Program Terminated!")
      

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    
