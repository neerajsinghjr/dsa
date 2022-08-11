'''
#Day 01: 25-06-2022

#Problem 02: Generate Pascal's Triangle

#Problem Description: Program to print the pascal triangle for any limit. Like,

Example 1:	
Input: Limit = 4
Output:
			1
		1		1
	1		2      1	
1	    3 		3 		1
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
    
    def __init__(self, limit):
        self.limit = limit


    def pascalTraingle_v1(self):
    	if not self.limit: return []
    	if self.limit == 1: return [1]

    	i = 0
    	res = []
    	prev = None
    	while(i < self.limit):
    		j = 0
    		row = []
    		while(j <= i):
    			if(j == 0 or j == i):
    				row.append(1)
    			else:
    				if len(prev) > 0:
    					row.append(prev[j-1]+prev[j])
    				else:
    					return(False, "Error:Previous List index is None")

    			j += 1 			# j++;

    		prev = row
    		res.append(row)
    		i += 1 			# i++;

    	return(True, res)


def main():
    try:
        obj = Solution(limit = 5)
        res = obj.pascalTraingle_v1()

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
    