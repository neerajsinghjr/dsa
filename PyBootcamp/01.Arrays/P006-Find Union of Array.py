'''
Problem Description:
Given two arrays a[] and b[] of size n and m respectively. 
The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing
distinct elements from both the arrays. If there are repetitions, 
then only one occurrence of element should be printed in the union.

Example 1:

Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
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
    def doUnionV1(self,a,b):
        print("V1")
        return len(set(a).union(set(b)))
              
    def doUnionV2(self,a,b):
        print("V2")
        myset = set()
        if(a):
            for i in a:
                myset.add(i)
        if(b):
            for j in b:
                myset.add(j)
        return len(myset)
        


def main():
    try:
        num1, num2 = [1,2,3,4,5], [4,5,6,7,8]               # ~ data
        obj = Solution()
        res = obj.doUnionV1(num1, num2)
        # res = obj.doUnionV2(num1, num2)
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
    