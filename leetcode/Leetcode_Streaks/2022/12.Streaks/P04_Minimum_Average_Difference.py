	'''
-------------------------------------------------------------------------------------
-> Problem Title: 2256. Minimum Average Difference
-> Problem Status: Ongoing
-> Problem Attempted: 04-12-2022
-> Problem Description: 
-------------------------------------------------------------------------------------
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the
average of the first i + 1 elements of nums and the average of the last n -
i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple
such indices, return the smallest one.

Note:
The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.
 
Example 1:
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- Average Difference :-
    index[0]: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- Average Difference :-
    index[1]: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- Average Difference :-
    index[2]: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- Average Difference :-
    index[3]: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- Average Difference :-
    index[4]: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- Average Difference :-
    index[5]: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.

The average difference of index 3 is the minimum average difference so return 3.

Example 2:
Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
 
Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

class Solution:

    #---Main Execution;;
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        atype: list
        rtype: int [index]
        """
        n = len(nums)
        if(n == 1):
            return 0
    
        return self.ansv1(nums, n)

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: brute force | time:O(n) | space 
        _study:
        simple approach, just calculate the required average and 
        iterate loop from left and rigth side of loop.     
        """
        _max = 100000 # 10^5
        res = [_max, _max]
        left_sum, total_sum = 0, sum(nums)

        for i,v in enumerate(nums):
            left_sum += v
            left_avg = left_sum//(i+1)

            # when we are at the last index, the right hand side sum is 0. 
            # (To aviod divide by zero error)
            right_avg = (total_sum-left_sum)//(n-i-1) if n-i-1!=0 else 0
            # absolute difference here.
            abs_diff = abs(left_avg-right_avg)
            
            # min will take care of "If there are multiple such indices, 
            # return the smallest one."
            res = min(res,[abs_diff,i])

        return res[1]

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
    