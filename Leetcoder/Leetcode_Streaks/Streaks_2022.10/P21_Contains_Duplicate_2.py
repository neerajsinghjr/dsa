'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 219. Contains Duplicate II
-> Problem Status: Completed
-> Problem Attempted: 21/10/2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:
    
    ###---Main Execution;;
    def containsNearbyDuplicate(self, nums, k) -> bool:
        n = len(nums)
        if(n <= 1):
            return False
						
        if(n == 2):
            if(nums[0] == nums[1]):
                return (False if(k < 1) else True)
            return False
        
        # return self.ansv1(nums,k,n)
        return self.ansv2(nums,k,n)
    
    
    """
    Run: Accepted
    Code: Optimied Sliding Window | T:O(N) | S:O(N)
    Study:
    This apporach uses the sort of sliding window apporach with hashset.
    1) At first we are iterating the array and storing num:index pair
    2) As we move forward, we fetch the nums[i] previous location and check 
    for difference between the (preLocation - curLocation) <= K
    3) If found then return True else update with the locaton of curIndex
    and then continue
		
		Choke Example:
		Input: nums = [1,0,1,1], k = 1
		Output: true
		~ There can be multiple repetitive numbers like 1 in this case with different index;
    """
    def ansv2(self, nums, k):
        dataset = {}
        for (idx,val) in enumerate(nums):
            if not(val in dataset):
                dataset[val] = idx
            else:
                pre = dataset[val]
                # return (True if(abs(i-j) <= k) else False)            ### Choke 1: See Example in Study Section;
                res = True if(abs(idx-pre) <= k) else False
                if(res):
                    return True
                dataset[val] = idx                                      ### Un-Choke 1: Updating Index;
                
        return False
        
    
 
    """
    Run: Accepted
    Code: Brute Force | O:T(N^2) | O:S(1)
    Study:
    Two Same loop iterating for the every value and returning answer
    """
    def ansv1(self,nums,k,n):
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i] == nums[j] and abs(j-i) <= k):
                    return True
        
        return False
 

##---Main Execution;;
def main(res=None):
    try:
        print(f"res: {res}")
        
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
    