'''
-------------------------------------------------------------------------------------
-> Problem Title: 2264. Largest 3-Same-Digit Number in String
-> Problem Status: 02/07/2025
-> Problem Attempted: Completed
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/largest-3-same-digit-number-in-string/

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

    def largestGoodInteger(self, nums: str) -> str:
        """
        _stdin:
            arg1: str
        _stdout: str
        """
        n = len(nums)
        if n == 3:
            if nums == f"{nums[0]*3}":
                return nums
            return ""

        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        # return self._ansv3(nums, n)
        return self._ansv4(nums, n)

    def _ansv4(self, nums: str, n: int) -> str:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 1 ms: tcz: 141/141
        _choke: none
        _brief: 
        - highlights 1 :: str can be multiplied like integers
        - highlights 2 :: str can be compared like integers
        - highlights 3 :: problem wants to return the max consecutive sequence. even if "333" 
        sequence comes earlier than "999". but ask is it return "999" as valid answer
        - single for_loop we naively compare current - idx == idx+1 == idx+2 if nums of these 
        indices matches; if matched than compare which one is bigger and keep it and move 
        forward in the for_loop
        - finally return the max str digit
        """
        max_good_int = ""
        for i in range(n-2):
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                cur_good_int = nums[i] * 3
                if cur_good_int > max_good_int:
                    max_good_int = cur_good_int
        return max_good_int
    
    def _ansv3(self, nums: str, n: int) -> str:
        """
        _run: accepted 
        _code: tc: o(n), sc: o(1), rt: 6 ms, tcz: 76/141
        _choke: none
        _brief: --- fixed version for ansv2() ---
        - highlights 1 :: str can be multiplied like integers
        - highlights 2 :: str can be compared like integers
        - highlights 3 :: problem wants to return the max consecutive sequence. even if "333" 
        sequence comes earlier than "999". but ask is it return "999" as valid answer
        - from every while_loop index we predict next good integer by multipying 3 times 
        existing str if its match the real nums then its a good match;
        - if its a good match than we compare and keep the bigger one; finally return it
        """
        i = 0
        max_num = ""
        while i < n:
            if i+2 < n:
                cur_num = f"{nums[i]*3}"
                if nums[i:i+3] == cur_num:
                    if cur_num > max_num:
                        max_num = cur_num
                    i += 3
                else:
                    i += 1
            else:
                break
        return max_num

    
    def _ansv2(self, nums: str, n: int) -> str:
        """
        _run: rejected
        _code: tc: o(n), sc: o(1), rt: nan, tcz: 76/141
        _choke:
        - misread the problem statment. problem was asking to return the max digit present 
        inside the given string.
        _brief:
        - from every while_loop index we predict next good integer by multipying 3 times 
        existing str if its match the real nums then its a good match;
        - we handled the 3xZeroes separately. its there is zero's trio than we ignores it 
        and look for another one other than 3xZeroes. 
        - This were we got choked by choke situation !!!
        """
        i = 0
        avoid_3x0s = "000"
        avoid_3x0s_flag = None
        while i < n:
            if i+2 < n:
                exp_num = f"{nums[i]*3}"
                if nums[i:i+3] == exp_num:
                    avoid_3x0s_flag = avoid_3x0s == exp_num
                    if not avoid_3x0s_flag:
                        return exp_num
                    i += 3
                else:
                    i += 1
            else:
                break
        return avoid_3x0s if avoid_3x0s_flag else ""


    def _ansv1(self, nums: str, n: int) -> str:
        """
        _run: rejected
        _code: tc: o(n), sc: (1), rt: nan, tcz: ??? 
        _choke: none
        _brief: ???
        """
        res = []
        i, n = 0, len(nums)
        while i < n:
            num = nums[i]
            for j in range(i+1, n):
                is_len_good = len(num) == 3
                if nums[i] != nums[j] or is_len_good:
                    break
                num += nums[j]
            i = j + 1
        res = res + [""]
        return res[0]


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
