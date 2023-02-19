'''
Problem Description:
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
    
    def findLongestConseqSubseq(self,nums, n):
        # base case
        if not nums: return nums
        
        # return self.func1(nums, n)
        return self.func2(nums,n)


    def func2(self, nums, n):
        res, count = 0,1
        store = dict.fromkeys(nums, False)
        for key in nums:
            nextKey = key + 1
            if(nextKey in store.keys()):
                store[key] = store[nextKey] = True
                count += 1
                print(f"{key}:{store[key]}/{count}")
            else:
                count = 0
                print(f"{count}")
            res = max(count, res)
        
        return res
    

    def func1(self, nums, n):
        res = count = 0
        nums.sort()                         # BigO(nLogn)
        print(nums)
        for i in range(n-1):
            current = nums[i]
            if(current+1 == nums[i+1]):
                count += 1
            res = max(res,count)

        # Checkpoint for Last Element;
        if(current+1 == nums[n-1]):
            res = max(res, count+1)

        return res


def main():
    try:
        n, nums = 6,[2, 6, 1, 9, 4, 5, 3] #[8, 8, 9, 9, 3, 4]
        obj = Solution()
        res = obj.findLongestConseqSubseq(nums, n)
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
    