#!/bin/python3

import os
import re
import sys
import time
import math
import random


friends = [
    {
        'name' : "Alexa",
        'age' : 18,
        'location': "W-DC",
    },
    {
        'name' : "Anna",
        'age' : 18,
        'location': "NY",
    },
    {
        'name' : "Chloe",
        'age' : 18,
        'location': "LA",
    },
]

##---Main Execution;;
def main():
	location = input("Enter Location: ")
	friendNearBy = [ friend for friend in friends if(friend['location'] == location) ]

	# any() return True when result should have atleast one value else false;
	if(any(friendNearBy)):
		print("You are not alone...")

	# all() return False even if one value is false and True only if all values if True;
	nums = [1,2,3,4,5]
	nums.append(0)		# 0 is consider False;
	if(all(nums)):
		print(f"True:nums -> {nums}")
	else:
		print(f"False:nums -> {nums}")



if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    