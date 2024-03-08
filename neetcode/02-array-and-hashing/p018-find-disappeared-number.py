'''
-------------------------------------------------------------------------------------
-> Problem Title: 448. Find Disappeared Number
-> Problem Status: Completed
-> Problem Attempted: 2024-03-05
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Reference:-
https://youtu.be/8i-f24YFWC4

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return []

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)

    def ansv3(self, nums, n):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: remember to take abs value for every ith index value of nums.
        brief:
        - For each value in the array mark its presence by making the number
        negative at that place in array
        - For eg, array = [3,1,4,1] , (take abs value)
            - for 3, i will go to index 2 and make its value negative ie, [3,1,-4,1]
            - for 1, i will go to index 0 and make its value negative ie, [-3,1,-4,1]
            - for 4, i will go to index 3 and make its value negative ie, [-3,1,-4,-1]
            - for 1 (take abs value), i will go to index 0 as it is already -ve do nothing.
            present array: [-3,1,-4,-1]
        - At last I will have [-3,1,-4,-1]. Now i will iterate over the array, whichever idx
        has positive value that number will not be in the array so as we have (nums[1] > 0)
        so 2 is not in the list.
        """
        res = []
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -1 * abs(nums[idx])
        for idx, num in enumerate(nums):
            if num > 0:
                res.append(idx + 1)

        return res

    def ansv2(self, nums, n):
        """
        run: accepted
        time: o(n+n)
        space: o(n+n)
        choke: none
        brief: Approach using map to get the value with o(1) time and rest of the
        logic is same.
        """
        res, num_map = [], {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        for i in range(1, n + 1):
            if not num_map.get(i):
                res.append(i)
        return res

    def ansv1(self, nums, n):
        """
        run: TLE (brute-force)
        time: o(n^2)
        space: o(1) i.e res ~ o(n) Problem Constraints
        choke:
        brief:
        """
        res = []
        for i in range(1, n + 1):
            if i not in nums:
                res.append(i)
        return res


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
