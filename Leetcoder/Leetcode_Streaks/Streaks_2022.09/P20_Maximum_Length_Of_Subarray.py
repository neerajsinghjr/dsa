'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 718. Maximum Length of Repeated Subarray
-> Problem Status: Completed
-> Problem Attempted: 20.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given two integer arrays nums1 and nums2, return the maximum length of a
subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
from collections import Counter

class Solution:
    
    ###---Main Execution;;;
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1), len(nums2)
        
        if(n == m == 1):
            if(n == m): 
                return 1
            return 0
        
        return self.ansv1(nums1,nums2,n,m)
        # return self.ansv2(nums1,nums2,n,m)
    
    
    """
    Run: Accepted 
    Code: DP Optimized : T:O(N*M) | S:O(N*M)
    Study: 
    DP Approach - Similar to 1143. Longest Common Subsequence.
    For reference: https://www.youtube.com/watch?v=Zg3HBicw4LU&ab_channel=Pepcoding
    """
    def ansv2(self,nums1,nums2,n,m):
        # dp[i][j] means the length of repeated subarray of nums1[:i] and nums2[:j]
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        maxlen = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                
                # if both character is same
                if(nums1[i-1] == nums2[j-1]):
                    
                    # then we add 1 to the previous state, which is dp[i - 1][j - 1]
                    # in other word, we extend the repeated subarray by 1
                    # e.g. a = [1], b = [1], length of repeated array is 1
                    #      a = [1,2], b = [1,2], length of repeated array is the previous result + 1 = 2
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                    # record the maxlen here
                    maxlen = max(maxlen, dp[i][j])
                
                # else
                    # if you are looking for longest common sequence,
                    # then you put dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); here
                    # however, this problem is looking for subarray,
                    # since both character is not equal, which means we need to break it here
                    # hence, set dp[i][j] to 0
                    

        return maxlen
    
    
    """
    Run: Rejected
    Code: Brute Force | T:O(N^2) | S:O(1)
    Study:
    Iterating two loops at the same time but managaing only finding the respective subarray 
    in the another loop;
    """
    def ansv1(self,nums1,nums2,n,m):
        maxlen = 0
        i,j,count = 0,0,0
        n,m = len(nums1),len(nums2)
        while(i < n):
            while(j < m):
                print(f"i:j -> {i}:{j}")
                # case 1: When, nums1[i] eq nums2[j];
                if(i < n and j < m and nums1[i] == nums2[j]):
                    while(j < m and i < n):
                        if(nums1[i] == nums2[j]):
                            maxlen = max(maxlen,count+1)
                            i,j = i+1,j+1
                        else:
                            j,count = 0,0
                            break
                # case 2: When, nums1[j] not eq nums2[i];
                else:
                    j += 1          #iter2 ++
            
            print(f"i:j -> {i}:{j}")
            i += 1          # iter1++

        return maxlen


##---Main Execution;;
def main():
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
    