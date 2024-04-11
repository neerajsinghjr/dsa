'''
Problem Description: 
Given an unsorted array arr[] of size N having both negative and positive integers. 
The task is place all negative element at the end of array without changing the 
order of positive element and negative element.

Example 1:
Input : arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 1  3  2  11  6  -1  -7  -5

Example 2:
Input : arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output : 7  9  10  11  -5  -3  -4  -1

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

    """
    Method 1: Working Fine!!!
    """
    def segregateElements_V1(self, arr, n):
        a = []
        b = []
        for i in arr:
            if (i>=0):
                a.append(i)
            else:
                b.append(i)
        arr[:]=a+b
        return arr
        
    """
    Method 2: not Working Correctly, because index of negative number is placed wrongly
    check above solution;
    """
    def segregateElements_V2(self, arr, n):
        idx, res = 0, [0]*n
        left, right = 0, n-1
        while(idx < n):
            if(arr[idx] >= 0):
                # print("if:",arr[idx],'>>>', idx)
                res[left] = arr[idx]
                left += 1
            else:
                # print("else:",arr[idx],'>>>', idx)
                res[right] = arr[idx]
                right -= 1
            idx += 1
        
        # print("arr:",arr)
        # print("res:", res)
        
        return res

    
def main():
    try:
        # Output : [-110, -90, -80, -40, -11, -10, -2, 20, 30, 40, 50, 150, 200, 210, 230]
        data = [ 0, 20, -11, -110, 30, 40, -2, 230, -10, -40, 50, 150, 200,-80, -90, 210 ]
        # data = [1, -1, 3, 2, -7, -5, 11, 6]
        print(data)
        obj = Solution()
        data = obj.segregateElements_V1(data, len(data))
        # data = obj.segregateElements_V2(data, len(data))
        print(data) if data else print("Empty!")
        
    except(Exception) as e:
        print(f"Exception Traced : {e}")
    
    else:
        print("Program Completion : Success")

    finally:
        print("Program Terminated!")

        

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    
