'''
-------------------------------------------------------------------------------------
-> Problem Title: 27. Remove Element
-> Problem Status: Completed
-> Problem Attempted: 21/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/remove-element/description/

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
        """
        _stdin:
            arg1: list[int]
            arg2: int
        _stdout: int
        """
        if not val in nums:
            return len(nums)

        # return self._ansv1(nums, val) 
        # return self._ansv2(nums, val)
        return self._ansv3(nums, val)
    
    def _ansv3(self, nums: List[int], val: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 0 ms
        _choke:
        -brief:
        - simple approach using two pointer. pointer p1 is from for loop and pointer p2
        is manually controlled inside the logic. 
        - p1 will flow like normal but p2 will increment when we find value other then 
        the target value and we will copy the swap value from p2 -> p1
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def _ansv2(self, nums: List[int], val: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 0 ms
        _choke:
        - this one is better because here we know exactly that for loop will iterate kth 
        number of times $val present inside the nums array
        _brief:
        - its just another way of writing the ansv1() approach using the count method.
        """
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

    
    def _ansv1(self, nums: List[int], val: int) -> int:
        """
        _run: accepted
        _code: tc: o(k*n), sc: o(1), rt: 0 ms
        _choke:
        - this approach is o(n)
        _brief:
        - while loop which runs till our targetted value is present inside the nums array
        - if its present inside it then remove it till its last existence
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
