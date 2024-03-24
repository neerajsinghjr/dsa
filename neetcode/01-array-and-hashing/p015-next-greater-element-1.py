'''
-------------------------------------------------------------------------------------
-> Problem Title: 496. Next  Greater Element I
-> Problem Status: Completed
-> Problem Attempted: 2024-03-04
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/next-greater-element-i/description/

Reference:-
https://youtu.be/u89i60lYx8U

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

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return self.ansv1(nums1, nums2)
        return self.ansv2(nums1, nums2)

    def ansv2(self, nums1, nums2):
        """
        run: accepted
        time: o(n+m)
        space: o(n)
        choke: none
        brief: --- algo based on monotonic stack solution ---
        - first we map nums1 in hashmap with their respective index
        - second we use stack and pop the element from top if the current element
        from nums2 is greater than top element and update it at needed result index array.
        - Again, same current element store it in stack if that current element belongs to nums1.
        """
        stack = []
        res = [-1] * len(nums1)
        num_map = {n: i for i, n in enumerate(nums1)}

        for num in nums2:
            while stack and num > stack[-1]:
                last_num = stack.pop()
                if last_num in num_map:
                    # updating the next greatest element;;
                    res[num_map[last_num]] = num
            # store num in num_map if num exists in nums1;;
            if num in nums1:
                stack.append(num)

        return res

    def ansv1(self, nums1, nums2):
        """
        run: accepted (brute-force-solution)
        time: o(n*m) ~ o(n^2)
        space: o(k)
        choke: none
        brief: simple brute force apporach iterating first second list under
        first list and checking if first loop value greate than second loop value
        then its ok otherwise append -1.
        """
        res = []
        for n1 in nums1:
            is_matched = False
            is_greater_value_found = False
            for n2 in nums2:
                # if we found the required subset value in nums2;;
                if n2 == n1:
                    is_matched = True
                # if greater value found for required n1 subset value;;
                if n2 > n1 and is_matched:
                    res.append(n2)
                    is_greater_value_found = True
                    break
            # if no greater value found then default value;;
            if not is_greater_value_found:
                res.append(-1)

        return res


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
