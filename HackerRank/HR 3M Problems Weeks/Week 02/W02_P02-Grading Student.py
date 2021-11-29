'''
Problem Description:
Given an array of integers, where all elements but one occur twice, find the unique element.
for eg,
nums = [1,2,3,4,3,2,1]
The Unique Element is 4
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import time


## Main Working Function, here
def checkMultipleOfFive(grade):
    quo = grade/5                       ## Float division;
    mul = quo if quo%5 == 0 else math.ceil(quo)
    newGrade = mul*5
    print("q:",quo,"m:",mul,"|",newGrade)
    print("grade:",grade,"newGrade:",newGrade)
    return newGrade
    
# Basic Solution ~ More Memory and Time;
def gradingStudentsV2(grades):
    # base case;
    if not grades:
        return None
    # main case
    res = []
    for grade in grades:
        if grade < 38:              ## already, failed
            res.append(grade)
        else:
            newGrade = checkMultipleOfFive(grade)
            if(newGrade - grade) < 3:
                res.append(newGrade)
            else:
                res.append(grade)
    return res
            
# Optimised Solution
def gradingStudentsV1(grades):
    size = len(grades)
    for x in range(size):
        if grades[x] >= 38:                     ## only for grade >= 38;
            diff = grades[x] % 5
            if(5-diff) < 3:
                grades[x] += (5-diff)
    return grades

def main():
    try:
        arr = [44,84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40,14,4,29,98,37,23,46,9,79,62,20,38,51,99,59,47,4,86,61,68,17,45,6,1,95,95]
        res = gradingStudentsV2(arr)                            ## Optimised Solution
        res = gradingStudentsV1(arr)                            ## Basic Solution ~ more time and space
        print(res) if res else print("Empty!")
        
    except(Exception) as e:
        print(f"Program Stopped: {e}")
    
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
    