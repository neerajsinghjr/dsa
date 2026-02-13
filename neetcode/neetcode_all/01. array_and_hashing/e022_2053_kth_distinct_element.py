'''
-------------------------------------------------------------------------------------
-> Problem Title: 2053. Kth Distinct String in an Array
-> Problem Status: Completed
-> Problem Attempted: 06/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from collections import Counter


##---Main Solution
class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        _stdin:
            arg1: list[str]
            arg2: int
        _stdout: str
        """
        n = len(arr)
        if n == 1:
            return arr[0]
        # return self._ansv1(arr, n, k)
        return self._ansv2(arr, n, k)
    
    def _ansv2(self, nums: List[str], n: int, k: int) -> str:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 4ms
        _choke: none
        _brief:
        - first pass counts frequencies of all strings. using collections.Counter is often cleaner 
        and more efficient than a manual loop for this.
        - second pass terate through the original array to find the Kth distinct string. this leverages 
        the original order of elements in `nums`. 
        - if $str is unique then we are decrementing the $k till k == 0 and returning $str
        """
        counts = Counter(nums)
        for s in nums:
            if counts[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
    
    def _ansv1(self, nums: List[str], n: int , k: int) -> str:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms
        _choke:
        _brief:
        - mapping every chars in hashmap with its relative occurences
        - pulling out only those character who are equals to 1 only or which are unique in nature
        - return the (k-1)th from it as ans its (k-1)th unique element exist else empty string.
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        ans = [k for k,v in hashmap.items() if v == 1]
        return ans[k-1] if k <= len(ans) else ""


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
