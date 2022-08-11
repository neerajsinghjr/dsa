'''
#Problem Title: Mountain Problem
#Problem Attempted: 28/07/2022
#Problem Description:
Write a function that takes input an array of distinct integer and return the length of highest mountain.

- A mountain is defined as adjacent integer that are strictly increasing until they reach a peak, at which
the become strictly decreasing.
- At least 3 number are required to form a triangle.

for eg,
array = [1,2,3,4,4,5,3,2,7,8,9,8,7,0,1,2,4,3,2,1]

Output = 8 

Mountain range from {1,2,3,4,4,5,3,2} => 8 and rest peak are small
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
	
	def highestPeak(self,nums,n):
		if not nums:
			return 0

		if(n == 1):
			return 1

		return self.ansv1(nums,n)


	def ansv1(self,nums,n):
		i = 1
		maxLen = 0
		count,loopCounter = 1,1
		
		while(i <= n-2):    
			# S1: Find peak 
			if(nums[i-1] <= nums[i] and nums[i] > nums[i+1]):
				print(f"PI: {i} and PV: {nums[i]}")
				count = 1

				# S2: Tracing nodes to the left of it;
				j = i
				while(j >= 1 and nums[j] >= nums[j-1]):
					count += 1
					print(f"j++ : {count}")
					j = j - 1 					# j++;

				if(j == 0 and nums[j] <= nums[j+1]):
					count += 1
					print(f"j[0]++ : {count}")

				# S3: Find nodes to the right of it;
				i += 1
				while(i < n-1 and nums[i] >= nums[i+1]):
					count += 1
					print(f"i++ : {count}")
					# print(f"index:value:count >> {i} : {nums[i]} : {count}")
					i += 1

				if(i == n-1 and nums[i] <= nums[n-1]):
					count += 1
					print(f"i[n-1]++ : {count}")
					i += 1

				# S4: Compare max peak;
				maxLen = max(maxLen, count)

				i += 1
				loopCounter += 1

				if loopCounter == 1000: 
					print("LOOP BREAKED @ 1000")
					break

			else:
				print(f"else: i: {i}")
				i += 1

		return maxLen


def main():
	# try:
	# data = [1,2,3,4,4,5,3,2,7,8,9,8,7,0,1,2,4,3,2,1]              # ~ data
	# data = [1,2,3,4,5,4,3,2,1]              # ~ data
	data = [7,4,5,4,7]              # ~ data
	obj = Solution()
	res = obj.highestPeak(data,len(data))
	print(f"Max Peak Count: {res}")
		
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
	