'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Generate Pascal's Triangle
-> Problem Status: Completed
-> Problem Attempted: 25-06-2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Program to print the pascal triangle for any limit. Like,

Example 1:	
Input: Limit = 4
Output:
			1
		1		1
	1		2      1	
1	    3 		3 		1

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
    
     def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        
        if(numRows == 0): 
            return res
        
        res.append([1])
        
        if(numRows == 1): 
            return res
        
        res.append([1,1])
        
        if(numRows == 2): 
            return res 
        
        return self.ansv1(numRows,res)
        # return self.ansv2(numRows)


    # Approach: Optimised | Time: O(N*N) | Space: O(1)
    def ansv2(self,numRows):
        i = 0
        res = []
        prev = None
        while(i < numRows):
            j = 0
            row = []
            while(j <= i):
                if(j == 0 or j == i):
                    row.append(1)
                else:   
                    if(len(prev) > 0):
                        row.append(prev[j-1] + prev[j])
                    else:
                        exit(1)
                j += 1
            
            prev = row
            res.append(row)
            
            i += 1        
            
        return res


    # Approach: Optimised | Time: O(N*N) | Space: O(1)
    def ansv1(self,numRows, res):
        i = 2                   # Index of next row, previously i = 0,1 index are handled ;;
        prev = res[-1]
        
        while(i < numRows):
            j = 0
            row = []
            while(j <= i):
                if(j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(prev[j-1]+prev[j])
                
                j += 1
            
            prev = row
            res.append(row)
        
            i += 1
        
        return res



def main():
    try:
        obj = Solution()
        res = obj.generate(limit=5)

        if type(res) == tuple:
        	print(f"Result: {res[1]}")
        	print(f"Status: {res[0]}")
        else:
        	print(f"Result: {res}")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Completed: Success")

    finally:    
        print("Program Terminated!")
        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    