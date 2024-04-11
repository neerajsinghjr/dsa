'''
Problem Description:
Given an array of bird sightings where every element represents a bird type id, 
determine the id of the most frequently sighted type. If more than 1 type has 
been spotted that maximum amount, return the smallest of their ids.

Example: 
arr = [1,1,2,2,3]

There are two each of types 1 and 2, and one sighting of type 3. 
Pick the lower of the two types seen twice: type 1.

Function
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here...
def migratoryBirds(arr):
    # base case
    if not arr:
        return None
    # main case
    birds = sorted(arr)
    birdId = birdCount = 0
    freq = {}
    for bid in birds:               # ~ bid : bird id;
        if bid in freq:
            freq[bid] += 1
        else:
            freq[bid] = 1
        if freq[bid] > birdCount:
            birdId = bid                # store birdId
            birdCount = freq[bid]       # increase counter;
    return birdId


def main():
    try:
        data = [1,1,3,2,2,3] 
        res = migratoryBirds(data) 
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced: {e}")
    
    else:
        print("Program Executed: Success")

    finally:
        print("Program Terminated!")
        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    