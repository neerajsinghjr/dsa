'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Unique Subset
-> Problem Status: 03.09.2022
-> Problem Attempted: 
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given a string write a function to find the largest substring with unique characters only.

Input: string = "prateekbhaiya"
Output: 8

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

    def uniqueSubstring(self,string) -> int:
        n = len(string)

        if(n == 0): return 0

        if(n == 1): return 1

        if(n == 2):
            if not(string[0] == string[1]):
                return 2
            return 1

        return self.ansv1(string,n)
        return self.ansv2(string,n)


    """
    Run: 
    Code: 
    Study:
    """
    def ansv2(self,string,n):
        dataset = set()
        start,cur,count = 0,0,0
        for cur in range(n):
            if not(string[cur] in dataset):
                dataset.add(string[cur])
                count = max(count,len(dataset))
            else:
                if(string[cur] in dataset):
                    dataset.remove(string[start])
                    start += 1
            
        return count



    """
    Run:
    Code: Brute Force
    Study:
    """
    def ansv1(self,string,n):
        count = 0
        for i in range(n):
            runner = 0
            for j in range(1,n):
                if (string[i] in string[i:j]):
                    break
                runner += 1

            count = max(count,runner)

        return count




##---Main Execution;;
def main():
    # try:
    data = "prateekbhaiya"               # ~ data
    obj = Solution()
    res = obj.uniqueSubstring(data)
    print(f"Result: {res}") if res else print("Empty!")
        
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
    