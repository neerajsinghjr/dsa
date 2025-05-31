'''
-------------------------------------------------------------------------------------
-> Problem Title: 1299. Replace Elements with Greatest Element on Right Side
-> Problem Status: Completed
-> Problem Attempted: 09/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

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

    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        stdin:
            arg1: list[int]
        stdout: list[int]
        """
        n = len(arr)
        if n == 1:
            return [-1]

        # return self._ansv1(arr, n)
        return self._ansv2(arr, n)
        # return self._ansv3(arr, n)
        # return self._ansv4(arr, n)
        # return self._ansv5(arr, n)

    def _ansv5(self, arr, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1), rt: 45ms
        _choke: none
        _brief: optimized version of ansv3(). 
        - remove the need of reversing the array at the end.
        - logic refactored too.
        """
        rt_mx, ans = -1, [0]*n
        for i in range(n-1,-1,-1):
            cur_mx = max(rt_mx, arr[i])
            ans[i] = rt_mx  # note: first using the existing val 
            rt_mx = cur_mx  # note: then updating it for next run
        return ans

    def _ansv4(self, arr, n):
        """
        _run: accepted (~best)
        _code: time: o(n), space: o(1), rt: 7ms
        _choke: none
        _brief: optimized version of ansv3(). 
        - remove the need of reversing the array at the end.
        """  
        mx, ans = -1, [0]*n
        for i in range(n-1, -1, -1):
            ans[i] = mx
            if mx < arr[i]:
                mx = arr[i]
        return ans

    def _ansv3(self, arr, n):
        """
        _run: accepted
        _code: time: o(n), space: o(1), rt: 15ms
        _choke: none
        _brief: We started looping from the end of the list to the start.
        - calculate right_max with default(-1)
        - every loop we check for max between right_max and cur index value
        - whoever is bigger we kept that at right_max and also at the array[ith] index.
        """  
        mx, ans = -1, []
        for i in range(n-1, -1, -1):
            ans.append(mx)
            if mx < arr[i]:
                mx = arr[i]
        return ans[::-1]
    
    def _ansv2(self, arr, n):
        """
        _run: accepted
        _code: time: o(n*k), space: o(n), rt: 20ms
        _choke: none
        _brief: optimization of ansv1()
        - we are not using max function on every iteration instead we've optimized it 
        till we have any value greater than our current max.
        """
        ans, mx = [], -1
        for idx in range(n-1):
            if not mx > arr[idx]:
                mx = max(arr[idx + 1:])
            ans.append(mx)
        ans.append(-1)
        return ans

    def _ansv1(self, arr, n):
        """
        _run: tle
        _code: time: o(n*2), space: o(1), rt: inf
        _choke: none
        _brief:
        - simple iterating over a loop and grepping max value from i+1 index onwards 
        till total_length -1
        - at the end adding -1 to our $ans list as the final element.
        """
        ans = []
        for i in range(n-1):
            ans.append(max(arr[i+1:]))
        ans.append(-1)
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
