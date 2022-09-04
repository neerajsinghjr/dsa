'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Find smaller string in bigger string
-> Problem Status: Completed
-> Problem Attempted: 03.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are given two string and need to find out the smaller string is subset of bigger string.

Example 1:
Input: str1 = "Hello World", str2 = "lol"
Output: 'llo'
Explanation: 'lol' is a subset of "Hello World". Quantity of 'l':2 and 'o':1 oterwise return None

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

	###---Main Execution;;
	def checkSubset(self,bg,sm):
		bgLen,smLen = len(bg),len(sm)

		if(smLen == 0 and bgLen == 0):
			return None

		if(smLen > bgLen):
			sm,bg = bg,sm
			smLen,bgLen = bgLen,smLen

		return self.ansv1(bg,sm,bgLen,smLen)
		

	"""
	Run:
	Cdde:
	Study:
	"""
	def ansv2(self,bg,sm,bgLen,smLen):
		map = {}

		for (key,value) in enumerate(sm):
			if(value in sm):
				sm[value] += 1
			else:
				sm[value] = 1

		res = 0
		start,cur = 0,0
		while(cur < len(bg)):
			if(bg[cur] in map):
				map[bg[cur]] -= 1
				res += 1
			else


	"""
	Run:
	Code:
	Study:
	"""
	def ansv1(self,bg,sm,bgLen,smLen):
		res = ""
		idx = []

		for si in range(smLen):
			for bi in range(bgLen):
				if(sm[si] == bg[bi]):
					if not(bi in idx):
						continue
					res.append(bi)

		print(f"index: {idx}")
		for i in idx: res += bg[i]

		return res


##---Main Execution;;
def main():
	try:
		sm,bg = "lol","Hello World"               # ~ data
		obj = Solution()
		res = obj.checkSubset(bg,sm)
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
	