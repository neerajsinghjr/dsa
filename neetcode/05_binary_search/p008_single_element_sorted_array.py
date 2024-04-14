'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

...

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

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)

    def ansv3(self, nums, n):
        """
        _run: accepted
        _code: time: o(logn), space: o(1)
        _study:
        --- explanation ---
        [+] we initialize l to 0 and r to len(nums) - 1.
        [+] Inside the loop, we calculate the middle index m using (l + r) // 2.
        [+] We ensure that m is an even index, as the single element is guaranteed
        to be at an even index.
        [+] We check if nums[m] is equal to nums[m + 1]. If it is, it means the single
        element is on the right side of m, so we update l to m + 2.
        [+] If nums[m] is not equal to nums[m + 1], it means the single element is on
        the left side of m, so we update r to m.
        [+] Finally, we return nums[l], which is the single element.
        """
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            print("m1: ", m)

            if m % 2 == 1:
                m -= 1  # Ensure mid is even index

            if nums[m] != nums[m + 1]:
                r = m
            else:
                l = m + 2

        return nums[l]

    def ansv2(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _study:
        --- explanation ---
        [+] here we have optimized an apporach a bit using set.
        [+] in set we are storing the values as soon as we get the same value again,
        then we are removing the duplicate value
        [+] at last we will have only single value which is required by the problem
        """
        hashset = set()

        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)

        return hashset.pop()

    def ansv1(self, nums, n):
        """
        _run: accepted
        _code: time: o(n), space; o(n)
        _study:
        --- constraints ---
        [+] given list must have single number so our approach solution
        --- explanation ---
        [+] solution works in two for loop in which one loop contains hashmap in which
        number mapped with its count
        [+] in second for loop, we iterate over the for loop and fetch that value whose
        existence in a singe count
        """
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for key, val in hashmap.items():
            if val == 1:
                return key
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
