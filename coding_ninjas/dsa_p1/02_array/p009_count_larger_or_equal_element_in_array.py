'''
-------------------------------------------------------------------------------------
-> Problem Title: Count larger or Equal Elements in Array
-> Problem Status: Completed
-> Problem Attempted: 05/06/2023
-> Problem Description: 
-------------------------------------------------------------------------------------
Similar Problem like p007, just here is now we're findging all the larger or
equal to element from another array

Similar problem can be viewed here as well ...
https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381881

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


def countLargerOrEqual(nums1, nums2):
    res = []
    nums2.sort()
    for num in nums1:
        count = count_element(nums2, num)
        print(f">>>> num: {num}, count: {count}")
        res.append(count)
    return res
    
def count_element(nums, target):
    res = None #  Storing the count;;
    lo, hi = 0, len(nums)-1
    while(lo <= hi):
        mid = lo + (hi-lo)//2
        print("mid @start: ", nums[mid])
        if target <= nums[mid]:
            res = mid
            hi = mid-1
        else:
            lo = mid+1
    
    return len(nums)-res if res != None else 0

# Output case 1: [4,2,0]
# nums1 = [13, 20, 50]
# nums2 = [15, 14, 32, 21, 11]
# Output case 2: [4,2,0,3] 
nums1 = [-2, 1, 3, 0]
nums2 = [-1, 0, 2, 1]
res = countLargerOrEqual(nums1, nums2)
print("res: ", res)





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