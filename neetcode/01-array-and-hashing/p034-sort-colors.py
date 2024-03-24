'''
-------------------------------------------------------------------------------------
-> Problem Title: 75. Sort Colors
-> Problem Status: Completed
-> Problem Attempted: 2024-03-12
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/sort-colors/

Reference:-
https://youtu.be/4xbWSRZHqac

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

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)

    def ansv3(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1)
        _study:
        --- dutch national flag algorithm ---
        Dutch National Flag (DNF) algorithm, which is commonly used to sort
        an array of objects with three distinct keys.
        --- solution brief ---
        [+] Initialize three pointers: i, j, and k.
        i is used for iterating through the array.
        j is used to keep track of the boundary between red (0) and white (1).
        k is used to keep track of the boundary between white (1) and blue (2).

        [+] Iterate through the array using the i pointer.
        If nums[i] is 0, swap nums[i] with nums[j] to move 0s to the beginning.
        If nums[i] is 2, swap nums[i] with nums[k] to move 2s to the end.
        If nums[i] is 1, leave it in place, and move to the next element.

        [+] Continue the process until i crosses the boundary defined by k.

        ---- key idea ---
        The key idea is to maintain three segments in the array:
        The segment before j contains only 0s.
        The segment between j and k contains only 1s.
        The segment after k contains only 2s.
        """
        i, j, k = 0, 0, n - 1

        while i <= k:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            else:
                i += 1

        return

    def ansv2(self, nums, n):
        """
        _run: accepted
        _code: time:(n+n), space: o(n)
        _study:
        --- approach ---
        simple approach there can be only three type of values 0, 1, 2 inside
        the array. then using a hashmap we have count the occurrences of 0,1,2
        in the nums
        then as per the occurrence we statically update the values inside the nums.
        """
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        idx = 0
        for key in [0, 1, 2]:
            val = hashmap.get(key, 0)
            while val > 0:
                nums[idx] = key
                val = val - 1
                idx += 1

        return

    def ansv1(self, nums, n):
        """
        _run: accepted (brute-force)
        _code: time: o(nlogn), space: o(1)
        _study: simple inplace sorting function python specific solution=
        """
        return nums.sort()


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
