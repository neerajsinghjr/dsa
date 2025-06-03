'''
-------------------------------------------------------------------------------------
-> Problem Title: 496. Next Greater Element I
-> Problem Status: Completed
-> Problem Attempted: 27/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/next-greater-element-i/description/

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
        """
        _stdin:
            arg1: list[int]
            arg2: list[int]
        _stdout: list[int]
        """
        # return self._ansv1(nums1, nums2)
        return self._ansv2(nums1, nums2)
    
    def _ansv2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        _run: accepted
        _code: tc: o(n+m), sc: o(n), rt: 13 ms
        _choke: --- approach follow monotonic decreasing stack ---
        - monotonic decreasing array uses stack only but top element should be smaller than
        target_num;; if yes then push to stack else popping last_num from stack and map the
        target_sum to your last_num;;  would be your answer
        _brief: 
        - using $stack for maintain monotonic sequence; $res having placeholder with default 
        value -1 with exact same number of count as our target nums1
        - for_loop is used to iterate over using nums2 list because we have to look for values
        inside of it.
        - inside as child while_loop, we are using monotonic decreasing apporach; if num is not 
        smaller than the last_num; then pop element from stack and map the last_num to cur_num.
        """
        # NOTE: stack will use it to maintain monotonic decreasing array;;
        stack = [] 
        
        # NOTE: we will update our target index when constraints meetup;;
        res = [-1] * len(nums1)
        
        # NOTE: num:idx mapping from nums1 bcz we'll loose indices when we will iterate over nums2;;
        indices = {num:idx for idx, num in enumerate(nums1)}

        for num in nums2:

            # NOTE: monotonic decreasing array implementation;; 
            # catch here is while loop will iterate, when current num is greater last_num;;
            while stack and stack[-1] < num:
                last_num = stack.pop()
                res[indices[last_num]] = num
            
            # NOTE: stack is updated on the basis of if current $num exist in our nums1 list;;
            if num in nums1:
                stack.append(num)

        return res
    
    def _ansv1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        _run: accepted (brute-force)
        _code: tc: o(n^2), sc: o(1), rt: 49 ms
        _choke: none
        _brief:
        - we are using two loops, first loop for iteratively fetching single values 
        everytime and loop2 to get the next larger value from it.
        - if_constraints_1: if n1 == n2 then we set $flag to true; that menas we have
        found that index from which we will look for next greater element
        - if_constraints_2: if n2 > n2 and flag: then we append value to ans and break
        the loop
        - if def_val is equals to -1 then that means geater value doesnt exist, default
        -1 would be appended to ans list.
        """
        ans = []
        for n1 in nums1:
            flag, def_val = False, -1
            for n2 in nums2:
                if n1 == n2:
                    flag = True
                elif n2 > n1 and flag:
                    ans.append(n2)
                    def_val = n2
                    break
            if def_val == -1:
                ans.append(def_val)
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
