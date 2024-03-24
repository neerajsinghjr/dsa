'''
-------------------------------------------------------------------------------------
-> Problem Title: 27. Remove Element
-> Problem Status: Completed
-> Problem Attempted: 2024/03/02
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/remove-element/description/

Reference:-
https://youtu.be/Pcd1ii9P9ZI

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

    def removeElement(self, nums: List[int], val: int) -> int:
        if not (val in nums):
            return len(nums)

        # return self.ansv1(nums, val)
        return self.ansv2(nums, val)
        return self.ansv3(nums, val)

    def ansv3(self, nums, val):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: simple looping copy the value other target values
        and paste it target value index.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    def ansv2(self, nums, val):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        breif: counting the occurrence and remove the target_value.
        """
        count = nums.count(val)
        for _ in range(count):
            nums.remove(val)
        return len(nums)

    def ansv1(self, nums, val):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: none
        brief: Iteratively reomve target_value in a loop and then
        return length.
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


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
