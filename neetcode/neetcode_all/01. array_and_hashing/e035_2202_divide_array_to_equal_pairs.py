'''
-------------------------------------------------------------------------------------
-> Problem Title: 2206. Divide Array Into Equal Pairs
-> Problem Status: Completed
-> Problem Attempted: 26/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/divide-array-into-equal-pairs/description/

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

    def divideArray(self, nums: List[int]) -> bool:
        """
        _stdin:
            arg1: list[int]
        _stdout: bool
        """
        n = len(nums)
        if n == 1:
            return False
        # return self._ansv0(nums, n)
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        return self._ansv3(nums, n)

    def _ansv3(self, nums: List[int], n: int) -> bool:
        """
        _run: accpeted
        _code: tc: o(n), sc: o(n), rt: 2 ms, tcz: 137/137
        _choke: none
        _brief: --- basis of my ansv0() ---
        - under the hood logic here is that if we have 2*n nums and we are expecting n pair of
        duplet; then there would be tight n couples available which there is any mismatch then 
        its impossible to create n pairs of duplet
        - created a hashmap with nums counts; later we iterate over the hashmap and validate if 
        there is any value count which map to a key which count is odd in number; than our ans is 
        False othewise it is True        
        """
        counters = {}
        for num in nums:
            counters[num] = counters.get(num, 0) + 1
        for key, val in counters.items():
            if val%2 != 0:
                return False
        return True

    def _ansv2(self, nums: List[int], n: int) -> bool:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1), rt: 1 ms, tcz: 1 ms
        _choke:
        - whenever you see this type of contraints [1 <= nums[i] <= 500], and if your solution 
        based defining any storage space like this; (count_sort = [-1] * 501), then never use 
        0 based as default value. 
        - it could leads to ambigious values. try this submitting this solution using it.
        _brief:
        - observed question will use 1 <= nums[i] <= 500 and 1 <= n <= 500; then using these 
        constraints i think of using counting_sort mechanism to count the pair.
        - tracing the pair approach is similar like toggling on/off a index place if the pair 
        observed; and increment the count in reality.
        - finally if count >= n//2 than True; else False
        """
        count = 0
        count_sort = [-1] * 501
        for idx in nums:
            if count_sort[idx-1] == -1:
                count_sort[idx-1] = idx-1
            else:
                count_sort[idx-1] = -1
                count += 1
        return True if count >= n//2 else False

    def _ansv1(self, nums: List[int], n: int) -> bool:
        """
        _run: accpeted
        _code: tc: o(n), sc: o(n), rt: 2 ms, tcz: 137/137
        _choke: none
        _brief:
        - to check for pair we have to look for same type of candidates; if such candidates
        found then return True; else False
        - to map such we're iterating over the nums list and each time when we trace num 
        for the first time then we store it inside a set; 
        - and next time when we trace same num then we increment our ++count and remove 
        the candidate from our pairs set; to avoid duplicacy
        - finally we check if our pairs are greater than n//2 than True; else False
        """
        count = 0
        pairs = set()
        for num in nums:
            if num not in pairs:
                pairs.add(num)
            else:
                pairs.remove(num)
                count += 1
        return True if count >= n//2 else False

    def _ansv0(self, nums: List[int], n: int) -> bool:
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(n), rt: 5 ms, tcz: 127/137
        _choke: none
        _brief:
        - initial step is to sort the given nums array
        - now iterate through the array in increments of two (i.e., i, i+2, i+4, and so on).
        - for each i, you will compare the element at nums[i] with the element at nums[i+1].
        - if at any point, nums[i] is not equal to nums[i+1], it signifies that you have 
        encountered an element that cannot be paired with its adjacent counterpart. 
        - in this case it's impossible to form the required pairs; return False else True
        """
        count = 0
        num_sort = sorted(nums)
        for idx in range(0, n, 2):
            if not(num_sort[idx] == num_sort[idx+1]):
                return False
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
