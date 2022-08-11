"""
Problem Description:
return max element in bitonic element in array
"""

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,pages,n,k):
        if(n == 0): return -1
        if(n == 1 and k == 1): return pages[0]
        if(n < k): return -1            
        
        res = None
        low,high = max(pages),sum(pages)
        
        while(low <= high):
            mid = low+(high-low)//2
            if(self.isPartitionValid(pages,low,mid,high,n,k)):
                res = mid
                high = mid-1
            else:
                low = mid+1
                
        
        return res
        
    
    # Partition Valid Methods;
    def isPartitionValid(self,arr,low,mid,high,n,k):
        i = pageSum = 0
        studentCount = 1
        while(i < n):
            pageSum += arr[i]
            
            if(pageSum > mid):
                studentCount += 1           # Student Count +1
                pageSum = arr[i]            # Page Sum Reset;
            
            if(studentCount > k):
                return False
            
            i += 1
            
        return True


def main():
    try:
        data = [1,2,3,4,5,6,9,10,11,4,3,2,1,0]               # ~ data
        obj = Solution()
        res = obj.findPages(data,len(data))
        print(res) if res else print("Empty!")
        
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
    