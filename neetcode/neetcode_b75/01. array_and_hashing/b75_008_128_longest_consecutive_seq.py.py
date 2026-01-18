'''
-------------------------------------------------------------------------------------
-> Problem Title: 128. Longest Consecutive Sequence
-> Problem Status: Completed
-> Problem Attempted:18/01/2026
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/longest-consecutive-sequence/description/

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


    def longestConsecutive(self, nums: List[int]) -> int:
        """refer notes more"""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1 
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        return self._ansv3(nums, n)
    
    def _ansv3(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (~BEST)
        _code: tc: o(n), sc: o(n), rt: 48ms, tcz: 84/84
        _choke:
        [+] make sure, avoid counting the same sequence again and again.
        _brief:
        [+] we are using the num_set in this approach to avoid the duplicacy and other
        benefit is that search in set will take o(1) time complexity.
        [+] approach says, converting list to numset to avoid duplicacy
        [+] using a for loop to fetch individual element from num_set and started looking
        for its sequence inside the num_set.
        [+] we only count the sequence only when it is part of earlier non-consecutive
        sequence.
        [+] each time when we count the sequence we use other while loop to count the 
        current length of the sequence.
        [+] pick the max len among the existing the current length and returns it.
        """
        mx_len = 1
        num_set = set(nums)

        for n in num_set:

            # only start counting if n is the start of the sequence;;
            if n-1 not in num_set:
                cur = n
                cur_len = 1

                while cur+1 in num_set:
                    cur_len += 1
                    cur += 1
                
                mx_len = max(mx_len, cur_len)

        return mx_len

    def _ansv2(self, nums: List[int], n: int) -> int:
        """
        _run: rejcted
        _code: na
        _choke:
        [+] mutates set while iterating, causing unstable iteration
        [+] increments value before removal, leading to incorrect element deletion
        [+] missing explicit sequence start condition
        _breif:
        [+] never mutate a collection while iterating over it
        [+] ordering logic must be explicit when simulating sequence traversal
        [+] choosing correct start conditions can eliminate extra bookkeeping
        """
        mx_len = 1
        num_set = set(nums)

        for ns in num_set:
            cr_len = 0
            while ns in num_set:
                ns += 1
                cr_len += 1
                num_set.remove(ns)

            mx_len = max(cr_len, mx_len)

        return mx_len
    
    def _ansv1(self, nums: List[int], n: int):
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(1), rt: 79ms, tcz: 84/84
        _choke:
        [+] make sure to avoid, duplicate element from the list of elements.
        _brief:
        [+] this approach totally revolves around the sorting the provided num list.
        [+] as we have sorted the existing list, so we can expect the all the number
        would be in sorted order.
        [+] we use a single while loop, to count the sequence of the number and count 
        the length of the sequence as well.
        [+] everytime we update the max length of the sequence and get it updated
        """
        i = 0
        nums.sort()     # o(nlogn)
        cr_len, mx_len = 1, 1

        while i < n-1:
            nex = nums[i] + 1

            if not nums[i] == nums[i+1]: # corner case;;
                if nums[i+1] == nex:
                    cr_len += 1
                else:
                    cr_len = 1
                mx_len = max(cr_len, mx_len)

            i += 1
        
        return mx_len


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
