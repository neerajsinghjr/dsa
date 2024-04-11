'''
-------------------------------------------------------------------------------------
-> Problem Title: 189. Rotate Array
-> Problem Status: Completed
-> Problem Attempted: 2024-04-07
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/rotate-array/description/

Reference:-
https://youtu.be/BHr381Guz3Y

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

    def rotate(self, nums: List[int], k: int) -> None:
        """
        _stdin:
            arg1: list[int]
            arg2: int
        _stdout: none
        """
        n = len(nums)
        # case 1: if k = 0 and n == k, then return nums only;;
        if k == 0 or n == k:
            return nums
        # case 2: if k > n then modulo it because rotation also leads;;
        if k > n:
            k = k % n

        # return self.ansv1(nums, n, k)
        # return self.ansv2(nums, n, k)
        return self.ansv3(nums, n, k)

    def ansv3(self, nums, n, k):
        """
        _run: accepted (optimized)
        _code: time: o(n), space: o(1)
        _study:
        --- explanation crux --
        [+] problem, nums = [1,2,3,4,5,6,7], k = 3
        [+] required, output = [5,6,7,1,2,3,4]
        [+] first reverse the array: [7,6,5,4,3,2,1]
        [+] reverse the first k element reverse from 0th => k
        [+] reverse the rest of element after the kth => len(nums)
        [+] conclusion output = [7,6,5,1,2,3,4]
        """

        def _reverse(nums, lo, hi):
            while lo <= hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo, hi = lo + 1, hi - 1
            return

            # s1: reverse the whole array in one short;;

        _reverse(nums, 0, n - 1)

        # s2: reverse the first k element from 0th => kth
        _reverse(nums, 0, k - 1)

        # s3: reverse the nums from kth => len(nums);;
        _reverse(nums, k, n - 1)

        return

    def ansv2(self, nums, n, k):
        """
        _run: accepted (brute-force)
        _code: time: o(n), space: (n)
        _study:
        --- explanation ---
        [+] first we detach the element from 0 to kth element called left element.
        [+] second we detach the element from (n-k)th to nth index element called right side.
        [+] merge both in the nums array itself only.
        """
        left = nums[:-k]  # element from 0 to kth elements;;
        right = nums[-k:]  # element from n-k to nth elements;;
        nums.clear()
        nums.extend(right)
        nums.extend(left)

    def ansv1(self, nums, n, k):
        """
        _run: TLE [37/38]
        _code: time: o(k*n) ~ o(n^2), space: o(1)
        _study:
        --- constraints ---
        [+] tried to optimized it in terms of space but time boundation exceeds
        --- explanation ---
        [+] rotate the single array kth times by fetching the last_element and putting
        it in the first index element.
        """

        def _rotate(self, nums, n, k):
            n = n - 1
            last_element = nums[-1]
            while (n):
                nums[n] = nums[n - 1]
                n = n - 1
            nums[0] = last_element
            return nums

        while k:
            _rotate(nums, n, k)
            k = k - 1
        return


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
