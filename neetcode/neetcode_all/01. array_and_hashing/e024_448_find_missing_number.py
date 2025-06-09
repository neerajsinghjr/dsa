'''
-------------------------------------------------------------------------------------
-> Problem Title: 448. Find All Numbers Disappeared in an Array
-> Problem Status: Completed
-> Problem Attempted: 08/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

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

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        if n == 1:
            return []

        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        # return self._ansv3(nums, n)
        return self._ansv4(nums, n)
    
    def _ansv4(self, nums: List[int], n: int) -> List[int]:
        """
        _run: accepted (BEST!!!)
        _time: tc: o(n), sc: o(1), rt: 48 ms, tcz: 35/35
        _choke: 
        - keep in mind to take abs value for every ith index value of nums; refer notes in code;
        _brief:
        - long story short here we are counting the index of every number whether its exists or not 
        - how are we counting or tracing the index; by marking the index negative as soon as we trace
        them; you will find any index which is not marked negative means that is missing.
        - for an instance, array = [3,1,4,1]
        - for each value in the array, mark its presence by negative number at its index position; 
        remember index starts from 0.
            - for 3, it will go to index 2 and make its value negative ie, [3,1,-4,1]
            - for 1, it will go to index 0 and make its value negative ie, [-3,1,-4,1]
            - for 4, it will go to index 3 and make its value negative ie, [-3,1,-4,-1]
            - for 1 if you go directly follow the logic then target index is 0; but index 0 is 
            already marked negative on previous run; if you run the logic again blindly then it 
            will reversed the sign this time; it will break the logic; thats why abs is necessary
            then final array would be like this [-3,1,-4,-1]
        - now you've to simply iterate over the array and whenver num is positive then that idx would
        be our missing number; increment the idx and append it to final ans 
        so 2 is not in the list.
        """
        ans = []
        for num in nums:
            # NOTE: abs(nums) bcz we are overriding same nums; 
            # may be possible to encounter negative num next time;; 
            idx = abs(num)-1
            # NOTE: countermeasure for encountering negative num in the next run;;
            nums[idx] = -1 * abs(nums[idx])
        for idx, num in enumerate(nums):
            # NOTE: ans will be those index values which are non-negative marked;;
            if num > 0:
                # NOTE: increment idx before adding to ans; bcz initially we decrementing it;;
                ans.append(idx+1)   

        return ans

    def _ansv3(self, nums: List[int], n: int) -> List[int]:
        """
        _run: accepted (optimized)
        _code: tc: o(n), sc: o(n), rt: 37 ms, tcz: 35/35
        _choke:
        _brief:
        - for_loop_1: we map all nums inside our hashmap with default flag as 1 or True.
        - for_loop_2: we iterate independently from 1 to $n if cur_num is not found inside hashmap
        then its our missing value and appends it to our ans list.
        """
        nmap = {num:1 for num in nums}
        ans = [idx for idx in range(1, n+1) if nmap.get(idx, 0) == 0]
        return ans

    def _ansv2(self, nums: List[int], n: int) -> List[int]:
        """
        _run: accepted (optimized)
        _code: tc: o(n), sc: o(n), rt: 43 ms, tcz: 35/35
        _choke:
        _brief:
        - for_loop_1: optimized this solution using hashmap approach, firstly we map our numbers 
        from 1 to $n inside hashmap with default flag as False
        - for_loop_2: we iterate over our $nums and check if cur_num is present in our hashmap then 
        we update our default set False Flag to True.
        - for_loop_3: we simply pull all the numbers from hashmap where the value are set to False.
        """
        nmap = {idx: False for idx in range(1,n+1)}
        for num in nums:
            nmap[num] = num in nmap
        ans = [k for k, v in nmap.items() if v == False]
        return ans

    def _ansv1(self, nums: List[int], n: int) -> List[int]:
        """
        _run: tle 
        _code: tc: o(n^2), sc: o(1), rt: nan, tc: 31/35
        _choke: none
        _brief:
        - for loop iteration from idx (1 to n) and checking if the current idx is part of nums then 
        skip it else append it to the $ans
        """
        ans = []
        for idx in range(1, n+1):
            if idx not in nums:
                ans.append(idx)
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
