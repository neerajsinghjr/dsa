'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 985. Sum of Even Numbers After Queries
-> Problem Status: Completed
-> Problem Attempted: 21.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

You are given an integer array nums and an array queries where queries[i] =
[vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print
the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith
query.

Example 1:
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]

Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Example 2:
Input: nums = [1], queries = [[4,0]]
Output: [0]
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
1 <= queries.length <= 104
-104 <= vali <= 104
0 <= indexi < nums.length

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
class Solution:
    
    ###--- Main Execution;;
    def sumEvenAfterQueries(self, nums, queries) -> List[int]:
        n = len(nums)
        return self.ansv1(nums, queries, n)
    
    
    """
    Run: Accepted
    Code: Brute Force | T:O(N) | S:O(1)
    Study:
    Approach defines, 
    1) Calculate $evenSum, first of all;
    2) Then, maintain $evenSum by iterating all the queries;
        - Reduce the nums[i], if nums[i] is even;
        - Update the nums[i]+query[val], if nums[i] is even then add to $evenSum;
        - Append to res;
    return to res;
    """
    def ansv1(self, nums, que, n):
        res = []          # result: array of new even sum;
        evenSum = sum(x for x in nums if(x%2 == 0))
        
        for (val,idx) in que:
            # p1: Fallback $evenSum for current num;
            evenSum -= nums[idx] if(nums[idx]%2 == 0) else 0
            nums[idx] = nums[idx] + val
            # p2: Update $evenSum for current even num;
            if(nums[idx]%2 == 0): evenSum += nums[idx]
            # p3: result;
            res.append(evenSum)
        
        return res


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
    