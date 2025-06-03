'''
-------------------------------------------------------------------------------------
-> Problem Title: 503. Next Greater Element II
-> Problem Status: Completed
-> Problem Attempted: 01/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/next-greater-element-ii/description/

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

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        if n == 1:
            return [-1]
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        # return self._ansv3(nums, n)
        return self._ansv4(nums, n)
    
    def _ansv4(self, nums: List[int], n: int) -> List[int]:
        """
        _run: accepted
        _code: tc: o(2*n*k), sc: o(n), rt: 17 ms
        _choke: none
        _brief: --- using monostack decreasing   approach --- 
        - single for_loop iterating 2 time and covering same elemen twice means. so that in 
        single iteration if we missed any NGE. we will pick again for NGE when we iterate 
        again from 0th index
        - we are iterating till 2*n that there idx would be greater than > $n. that's why
        modulo is used to reset the iterator to 0th.
        - in stack we are going to append the index to avoid element duplicacy.
        """
        stack = []
        res = [-1] * n
        for raw_idx in range(2*n):
            idx = raw_idx % n
            val = nums[idx]
            while stack and nums[stack[-1]] < val:
                last_num_idx = stack.pop()
                res[last_num_idx] = val
            if raw_idx < n:
                stack.append(raw_idx)
        return res 

    def _ansv3(self, nums: List[int], n: int) -> List[int]:
        """
        _run: not-accepted
        _code: tc: o(n^2), sc: o(1), rt: 972 ms
        _choke:
        _brief:
        - trying re-writing new version for ansv2() solution
        """
        ans = []
        for idx, val in enumerate(nums):
            mx_val, lt_val, rt_val = None, None, None
            # for_loop_1: find greater num towards right from idx position;;
            for x in range(n):
                # check greater value towards right;;
                if not rt_val and x > idx and nums[x] > val:
                    rt_val = nums[x]
                    break
                # check left value towards left;; 
                if not lt_val and x < idx and nums[x] > val:
                    lt_val = nums[x]
            if rt_val is not None:
                mx_val = rt_val
            if lt_val is not None and mx_val == None:
                mx_val = lt_val
            if mx_val == None:
                mx_val = -1
            ans.append(mx_val)
        return ans

    def _ansv2(self, nums: List[int], n: int) -> List[int]:
        """
        _run: accepted
        _code: tc:o (n^2), sc: o(1), rt: 972 ms
        _choke:
        - keep an eye of num[i] constraint: -10^5 <= nums[i] <= 10^5. So Avoid using def_val 
        with -1 value. It will cause isue.
        _brief:
        - simple apporach with two for loop, which is working with o(n^2) timeframe.
        - primary loop iteratively picks one element at a time. 
        - child for_loop_1 looks for larger value from $idx to len(nums) towards right side.
        - if child for_loop_1 failed to trace any larger value then we iterate another child
        for_loop_2 which goes from 0th to $idx index arrray and try to fetch larger value.
        - even after no larger value found then we append -1 as default.
        """
        ans = []
        for idx, val in enumerate(nums):
            max_val = None
            # for_loop_1: find greater num towards right from idx position;;
            for x in range(idx+1, n):
                if nums[x] > val:
                    max_val = nums[x]
                    break
            # for_loop_2: find greater num towards left from 0 to idx position;;
            if max_val == None:
                for y in range(0, idx):
                    if nums[y] > val:
                        max_val = nums[y]
                        break

            max_val = max_val if max_val is not None else -1
            ans.append(max_val)
        return ans
        
    def _ansv1(self, nums: List[int], n: int) -> List[int]:
        """
        _run: rejected
        _run: accepted
        _code: tc:o (n^2), sc: o(1), rt: 972 ms
        _choke:
        - failed to trace larger value towards left side iteration from current idx.
        _brief:
        - simple apporach with two for loop, which is working with o(n^2) timeframe.
        - primary loop iteratively picks one element at a time. 
        - child for_loop_1 looks for larger value from $idx to len(nums) towards right side.
        - for tracing value left side uses a variable which store greater left side while 
        iterating over the same child for_loop.
        """
        ans = []
        rt_val = nums[-1]
        lt_val_mx = None

        for idx, num in enumerate(nums):
            def_val = None
            for j in range(idx+1, n):
                if nums[j] > num:
                    ans.append(nums[j])
                    def_val = nums[j]
                    break
            if def_val == None and idx != n-1:
                ans.append(-1)
            if lt_val_mx == None and rt_val < num:
                lt_val_mx = num
        
        # NOTE: it is also possible that even though you iterated over loop completely 
        # but still u didnt find any value greater than last_num then default(-1)
        lt_val_mx = lt_val_mx or -1 
        ans.append(lt_val_mx)
        return ans


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
