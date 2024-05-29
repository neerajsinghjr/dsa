'''
-------------------------------------------------------------------------------------
-> Problem Title: 238. Product of Array Except Self
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/product-of-array-except-self/description/

Reference:-
https://youtu.be/bNvIQI2wAjk?si=9eHktMNMephpRlu6

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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        _stdin: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        if n == 2:
            return [nums[1], nums[0]]

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)

    def ansv3(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space:o(1) i.e, result array ignored
        _choke: none
        _study: this solution works in two iterations
        [+] first loop: we calculate the prefix product for every ith index, excluding
        the ith index value
        [+] second loop: we calculate the respective postfix product for every ith index
        from the end and multiple that postfox product with the prefix product from the
        same ith array.
        """
        prefix_product = 1
        postfix_product = 1
        res = [0 for _ in range(n)]
        # calculate prefix_product from start and store it in result array;;
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]

        # calculate postfix_product from end and map with respective prefix_product
        # and then update the resultant array;;
        for j in range(n - 1, -1, -1):
            res[j] *= postfix_product
            postfix_product *= nums[j]

        return res

    def ansv2(self, nums, n):
        """
        _run: rejected
        _code: o(n), o(1)
        _choke: unable to catch 0 index value
        _study:
        --- choke ---
        [+] choke problem ...
        nums = [-1,1,0,-3,3]
        output = [-9,9,0,-3,3]
        total_product: 9
        expected = [0,0,9,0,0]
        --- explanation ---
        [+] calculate lumpsum product of whole array then divide the product with the ith
        nums index value for specific ith index.
        """
        prod, res = 1, []
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
        print("prod: ", prod)
        for i in range(n):
            cur_prod = prod // nums[i] if nums[i] != 0 else 0
            res.append(cur_prod)
        return res

    def ansv1(self, nums, n):
        """
        _run: TLE
        _code: time: O(n^2), space: o(n)
        _choke: none
        _study: simple multiply and skip current ith num
        """
        res = []
        for i in range(n):
            temp = 1
            for j in range(n):
                if j != i:
                    temp *= nums[j]
            res.append(temp)

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
