'''
Problem Description:
An avid hiker keeps meticulous records of their hikes. 
During the last hike that took exactly  steps, for every 
step it was noted if it was an uphill, U, or a downhill, D step. 
Hikes always start and end at sea level, and each step up or down 
represents a 1 unit change in altitude. 

We define the following terms:

A mountain is a sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, 
starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, 
find and print the number of valleys walked through.

# Example
steps = 8 paths = [DDUUUUDD]

The hiker first enters a valley 2 units deep. 
Then they climb out and up onto a mountain 2 units high. 
Finally, the hiker returns to sea level and ends the hike.

# Function Description
Complete the countingValleys function in the editor below.
countingValleys has the following parameter(s):
1) int steps: the number of steps on the hike
2) string path: a string describing the path

# Returns
int: the number of valleys traversed
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def countingValleys(steps, paths):
    valley = seaLevel = currentStep = 0
    while(currentStep < steps):
        if paths[currentStep] == "U":
            seaLevel += 1
            if(seaLevel == 0):
                valley += 1
        else:
            seaLevel -= 1
            
        currentStep += 1

    return valley

        

def main():
    try:
        paths = ['D','D','U','U','U','U','D','D']
        steps = 8
        res = countingValleys(steps, paths)
        print("Valleys:",res) if res else print("Empty!")
        
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
    