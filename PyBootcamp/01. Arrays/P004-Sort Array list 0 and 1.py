'''
Problem Description:
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated into ascending order.
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
    def sort012(self,arr):
        if arr:
            temp = dict()
            temp[0] = temp[1] = temp[2] = 0
            # Step 1: Using Dict;
            for num in arr:
                if(temp[num] is None):
                    temp[num] = 1
                else:
                    temp[num] += 1
            # Step 2: Updating the List;
            arrIndex = 0                       # Array Index Default 0;
            for i in [0,1,2]:
                if(temp[i] != 0):
                    x = temp[i]
                    while(x > 0):
                        if(x > 0):
                            arr[arrIndex] = i  
                            arrIndex += 1       
                            x = x - 1           
                else:
                    break
        
        return arr if arr else []



def main():
    try:
        arr = [0,1,2,2,2,2,2,1,0,1,0,0,0,1,0,2,1,0,0,1,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,1,1,1,1,0,0,2,2,2,1,1,0]
        obj = Solution()
        obj.sort012(arr)
        print(arr) if arr else print("Empty!")
        
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
    