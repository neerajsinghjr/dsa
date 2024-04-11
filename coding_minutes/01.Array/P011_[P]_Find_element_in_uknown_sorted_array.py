'''
Problem Description:
Search an sorted array 
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

    # Helper : Method : Binary Search;
    def binarySearch(self, nums, low, high, target):
        while(low <= high):
            mid = low + (high-low)//2
            if(nums[mid] == target):
                return f"Found: {mid}/{nums[mid]}"
            elif(nums[mid] > target):
                high = mid - 1
            elif(nums[mid] < target):
                low = mid + 1
        return None

    # --------------------------------------
    # Method 1 : Brute Force O(n)
    # --------------------------------------
    def searchUnknowListV1(self, nums, target):
        try: 
            size = 0
            while(size >= 0):                                # BigO(n): Measuing Size of Array;
                if not nums[size]:
                    break
                size += 1

        except IndexError as ie:
            if(size == 0):
                return None
            res = self.binarySearch(nums,0,size-1,target)        # BigO(nLogn): Binary Search;
            return (res if res else None)

        except Exception as e:
            print(f"Fallback Exception : {e}")


    # Helper: SearchLastIndex:
    def getLastIndex(self, nums, low, high, LINEAR=True):

        if LINEAR:
            # Linear Search Approach;
            try:
                while(low <= high):
                    if(nums[low]):
                        low += 1
            except IndexError as ie:
                return (low-1)
            except Exception as e:
                return f"Linear Search Exception : {e}"
                
        else:
            # Binary Search Approach : Between low => high;
            pass


    # ------------------------------------------
    # Method 2 : Binary Search ~O(Logn)
    # ------------------------------------------
    def searchUnknowListV2(self, nums, target):
        try :
            if not nums:    return -1
            start,size = 0,1
            while(size):                                                # Big O(Logn)
                if(nums[size]):
                    start = size
                    size *= 2

        except IndexError as ie:
            end = self.getLastIndex(nums, start, size)                  # Big O(k)
            return self.binarySearch(nums, 0, end-1, target)            # Big O(Logn)

        except Exception as e:
            print(f"Exception Tracked @ {e}")


def main():
    try:
        nums = [
            [1,2,3,4,5,6,7,8,8,9,10,10,22,200,2002,2020,2021,5002],
            [1,2,3,4,5,6,7,8,8,9,10,10,22,207,208,210,211,502],
            [1,2,3,4,5,6,7,8,8,9,10,10,22,207,208,210,211,502],
        ] 
        target = [2002, 211, 1001]
        obj = Solution()
        for i in range(len(nums)):
            res1 = obj.searchUnknowListV1(nums=nums[i], target=target[i])
            print(res1) if res1 else print("Empty!")
            res2 = obj.searchUnknowListV2(nums=nums[i], target=target[i])
            print(res2) if res2 else print("Empty!")
        
        
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
    