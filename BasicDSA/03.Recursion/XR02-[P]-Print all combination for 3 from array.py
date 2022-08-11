'''
Problem Description:
Print all combination of three from given array elements;
eg, 
nums = [1,2,3,4,5,6,7] 
Return : 123,124,125,126,127,234,235,236,237,345,346,347,456,457,567

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
    
    # __main__
    def printCombos(self, nums, combos=3):
        # base case;
        if not nums: return nums

        # main case;
        bufs = [0]*combos
        size = len(nums)
        self.bruteForce(nums)
        # return self.bruteForce(self, nums)
        # return self.bufferRecursion(nums, [0]*3, 0, 0)          
        return self.recursionBacktracking(nums, bufs, 0, 0, size, []) # startIdx: 0/res = []/numIdx: 0;


    # Method 3 : Recursion Backtracking
    def recursionBacktracking(self, nums, bufs, numsIdx, bufsIdx, size, res):
        # BaseCase: When buffer full;
        if(bufsIdx == len(bufs)):
            res.append(bufs)
            print(f"buf@end res:{res}")
            return 
        
        # BaseCase : When nums full;
        if(numsIdx == len(nums)):
            print("numIndx@end : {numsIdx}")
            return 
        
        # MainCase
        for i in range(numsIdx, size):
            print(f"startIdx/bufs: {numsIdx}/{bufs}")
            bufs[bufsIdx] = nums[numsIdx]
            print(f"bufs: {bufs}")
            self.recursionBacktracking(nums, bufs, numsIdx+1, bufsIdx+1, size, res)
            print("bufs-1: ",bufs)
            bufsIdx -= 1

        return res


    # Method 2 : Buffer Recursion;
    def bufferRecursion(self, nums, bufs, numIdx, bufsIdx):
        # BaseCase : When Buffer is Full;
        if(bufsIdx == 3):
            print(bufs, end=" ")
            return 
        
        # BaseCase : When nums reaced ends;
        if(numIdx == len(nums)):
            return
        
        # MainCase : Loop Iterating
        for idx in range(numIdx, len(nums)-1):
            bufs[bufsIdx] = nums[idx]
            self.getCombos(nums, bufs, idx+1, bufsIdx+1)

        return


    # Method 1 : Brute Force Solution ~ BigO(n^3)
    def bruteForce(self, nums):
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                for k in range(j+1, size):
                    print(f"{nums[i]}{nums[j]}{nums[k]}", end = " ")

        return None
    


def main():
    try:
        # nums = [1,2,3,4,5,6,7]
        nums = [1,2,3,4,5]
        obj = Solution()
        obj.printCombos(nums)
        # print(end="\n")
        # obj.printCombosV2(nums)
        # print(end="\n")
        
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
    