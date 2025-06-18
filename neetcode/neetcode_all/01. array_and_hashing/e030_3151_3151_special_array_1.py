'''
-------------------------------------------------------------------------------------
-> Problem Title: 3151. Special Array I
-> Problem Status: Completed
-> Problem Attempted: 18/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/special-array-i/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:

    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        _stdin:
            arg1: list[int]
        _stdout: bool
        """
        n = len(nums)
        if n == 1:
            return True
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        return self._ansv3(nums, n)
    
    def _ansv3(self, nums: List[int], n: int) -> bool:
        """
        _run: accepted
        _code: tc; o(n), sc: o(1), rt: 0 ms, tca: 852/852
        _choke: none
        _brief:
        - we are calculating the mod for cur_num and nex_num and if they mod parity is equals
        that means priority is mismatched 
        """
        for idx in range(1, n):
            if nums[idx-1]%2 == nums[idx]%2:
                return False
        return True

    def _ansv2(self, nums: List[int], n: int) -> bool:
        """
        _run: accepted
        _code: tc; o(n), sc: o(1), rt: 3 ms, tca: 852/852
        _choke: none
        _brief: --- optimized version for _ansv1() ---
        - its a simple flag based solution where we first check if the start index value is 
        even or odd
        - then from the next iteration we check opposite parity of the flag value.
        - if the cur_num's parity match with the flag's parity then we are ok; else False 
        """
        is_even = not (nums[0] % 2 == 0)
        for idx in range(1, n):
            if is_even:
                if nums[idx]%2 != 0:
                    return False
            else:
                if nums[idx]%2 == 0:
                    return False
            is_even = not is_even
        return True

    def _ansv1(self, nums: List[int], n: int) -> bool:
        """
        _run: accepted
        _code: tc; o(n), sc: o(1), rt: 3 ms, tca: 852/852
        _choke: none
        _brief:
        - its a simple flag based solution where we first check if the start index value is 
        even or odd
        - then from the next iteration we check opposite parity of the flag value.
        - if the cur_num's parity match with the flag's parity then we are ok; else False 
        """
        is_even = (nums[0] % 2 == 0)
        for num in nums:
            if is_even:
                if num%2 != 0:
                    return False
            else:
                if num%2 == 0:
                    return False
            is_even = not is_even
        return True


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
