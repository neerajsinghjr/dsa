
'''
-------------------------------------------------------------------------------------
-> Problem Title: Maximum Subarray Sum after K Concatenation
-> Problem Status: Completed
-> Problem Attempted: 02/02/2023
-> Problem Description:
-> Problem Link: https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118820/offering/1381873
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


def maxSubSumKConcat(arr, n, k):
	"""
	run: ???
	time: o(n)
	space: o(n)
	choke: ???
	study: Muliply the array kth time and then 
	find the sub array sum.
	"""
	cur_sum = 0
	max_sum = float('-inf')
	for i in range(n*k):
		if cur_sum < 0:
			cur_sum = 0		
		cur_sum += arr[(i)%n]
		max_sum = max(cur_sum, max_sum)

	return max_sum

def maxSubSumKConcat_v3(arr, n, k):
	"""
	study: pythonic approach;;
	"""
	arr = arr*k
	cur_sum = -maxsize
	max_sum = -maxsize

	for a in arr:
		cur_sum = max(a, cur_sum+a)
		max_sum = max(max_sum, cur_sum)

	return max_sum

def maxSubSumKConcat_v2(arr, n, k):
	"""
	run: TLE
	time: o(n)
	space: o(1)
	choke: TLE
	study: Muliply the array kth time and then 
	find the sub array sum.
	"""
	i = 0 
	cur_sum = 0
	max_sum = float('-inf')
	while(i < k):
		for a in arr:
			if cur_sum < 0:
				cur_sum = 0		
			cur_sum += a
			max_sum = max(cur_sum, max_sum)
		i += 1

	return max_sum

def maxSubSumKConcat_v1(arr, n, k):
	"""
	run: TLE
	time: o(n)
	space: o(n)
	choke: TLE
	study: Muliply the array kth time and then 
	find the sub array sum.
	"""
	arr = arr*k
	cur_sum = 0
	max_sum = max(arr)
	for a in arr:
		if cur_sum < 0:
			cur_sum = 0
		cur_sum += a
		max_sum = max(cur_sum, max_sum)
	
	return max_sum


##---Main Execution;;
def main(res=None):
    try:
    	data = []				
        obj = Solution()	
        res = None
        print(f"Result: {res}") if res else print("Empty!")
        
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