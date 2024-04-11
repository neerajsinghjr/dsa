'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/majority-element/description/

Reference:-
https://youtu.be/7pnhv842keE

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

    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # return self.ansv1(nums, n)
        # return self.ansv2(nums, n)
        return self.ansv3(nums, n)
        # return self.ansv4(nums, n)

    def ansv4(self, nums, n):
        """
        run: accepted
        time: o(nlogn)
        space: o(1)
        choke: none
        brief: --- assumption here is that the majority element always exists ---
        a) The list nums is sorted in ascending order. Sorting helps bring
        the majority element to the middle of the sorted list.
        b) return nums[n//2]: Since the list is sorted, the majority element
        will be at the index ⌊n/2⌋ (integer division).
        because, in a sorted list, the majority element (appearing more than ⌊n/2⌋ times)
        will have more occurrences than any other element, and hence, it will
        be positioned at the middle.
        """
        nums.sort()
        return nums[n // 2]

    def ansv3(self, nums, n):
        """
        run: accepted
        time: o(n)
        space: o(1)
        choke: There has to be majority element in the list to work.
        brief: Based on algo --- Boyer Moore ---
        There has to be a majority element in the provided list to implement
        the algorithms. Otherwise it can provide the ambiguous result.
        """
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if res == num else -1

        return res

    def ansv2(self, nums, n):
        """
        run: accepted (brute-force-code-level-optimization)
        time: o(n)
        space: o (n)
        choke: none
        brief: hashmap elements with their occurence and iterative over hashmap
        and look for majority element.
        """
        limit = n // 2
        hashmap = {}
        res, max_count = 0, 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            res = num if hashmap[num] > max_count else res
            max_count = max(max_count, hashmap[num])

        return res

    def ansv1(self, nums, n):
        """
        run: accepted (brute-force)
        time: o(n + k)
        space: o (n)
        choke: none
        brief: hashmap elements with their occurence and iterative over hashmap
        and look for majority element.
        """
        limit = n // 2
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for k, v in hashmap.items():
            if v > limit:
                return k
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
