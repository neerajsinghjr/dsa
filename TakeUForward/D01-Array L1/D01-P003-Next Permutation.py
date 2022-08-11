'''
#Day 01: 25-06-2022

#Problem 02: Find Next Permutation

#Problem Description: Given an array Arr[] of integers, rearrange the numbers of the given array into the 
lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order 
(i.e., sorted in ascending order).

Example 1:
Input format: Arr[] = {1,3,2}
Output: Arr[] = {2,1,3}
Explanation: All permutations of {1,2,3} are ...
{ {1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1} }
So, the next permutation just after {1,3,2} is {2,1,3}.

Example 2:
Input format: Arr[] = {3,2,1}
Output: Arr[] = {1,2,3}
Explanation: As we see all permutations of {1,2,3} are, we find {3,2,1} at the last position. 
So, we have to return the topmost permutation.

'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

from itertools import permutations


## Main Working Function, here...
# class Solution:
    
#     def __init__(self, nums):
#         self.nums = nums


#     # @return: 
#     def getPermutations(self):
#     	pass


# 	# @return: 
#     def nextPermutation_v1(self):
# 		pass


def permutation(lst):

	# If lst is empty then there are no permutations
	if len(lst) == 0: return []

	# If there is only one element in lst then, only one permutation is possible;
	if len(lst) == 1: return [lst]

	# Find the permutations for lst if there are more than 1 characters

	l = []
 
	# Iterate the input(lst) and calculate the permutation
	for i in range(len(lst)):
		m = lst[i]
		print(f"m: {m}")

		# Extract lst[i] or m from the list.  remLst is remaining list
		remList = lst[:i] + lst[i+1:]
		print(f"remList: {remList}")

		# Generating all permutations where m is first element
		for p in permutation(remList):
			print(f"p: {p}")
			print(f"$l: {l}")
			l.append([m] + p)

	return l


data = list('123')
for p in permutation(data):
	print (p)
 

# def main():
#     try:
# 		data = list('123')
# 		for p in permutation(data):
#     		print (p)

#     	# print(list(permutations(nums = [1,2,3])))
#         # obj = Solution(nums = [1,2,3])
#         # if type(res) == tuple:
#         # 	print(f"Result: {res[1]}")
#         # 	print(f"Return: {res[0]}")
#         # else:
#         # 	print(f"Result: {res}")
        
#     except(Exception) as e:
#         print(f"Exception Traced: {e}")
    
#     else:
#         print("Program Completed: Success")

#     finally:    
#         print("Program Terminated!")
        

# if __name__ == '__main__':
#     print("#------------ Code Start --------------#")
#     startTime = time.time()
#     main()
#     endTime = time.time()
#     print("Run Time:",endTime-startTime,"ms")
#     print("#------------ Code Stop ----------------#")
#     