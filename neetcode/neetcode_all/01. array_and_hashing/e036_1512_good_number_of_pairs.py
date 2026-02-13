'''
-------------------------------------------------------------------------------------
-> Problem Title:
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
...

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
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        _stdin:
            arg1: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return 0
        # return self._ansv1(nums, n)
        # return self._ansv2(nums, n)
        return self._ansv3(nums, n)
    
    def _ansv3(self, nums: List[int], n: int) -> int:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 49/49
        _choke:
        - remember we are adding the count with the occurence of the particular key.
        _brief:
        - Let's iterate through the array while maintaining a hashmap (freq_map) to store 
        how many times each number has appeared before the current index.
            - At each index i:
            - Let val = arr[i].
            - If val is already in freq_map, it has appeared before.
            - freq_map[val] gives us the number of times val appeared before.
            - This means the current val can form freq_map[val] good pairs with the previous 
            same values.
            - Add that count to the total number of good pairs.
        - increment the count of val in freq_map.
        - for eg, arr = [1, 2, 3, 1, 1]; freq_map = {}; good_pairs = 0;
        i = 0: arr[0] = 1 → Not seen before
                → No good pair
                → freq_map = {1: 1}

        i = 1: arr[1] = 2 → Not seen before
            → No good pair
            → freq_map = {1: 1, 2: 1}

        i = 2: arr[2] = 3 → Not seen before
            → No good pair
            → freq_map = {1: 1, 2: 1, 3: 1}

        i = 3: arr[3] = 1 → Seen before (1: 1)
            → Can form 1 good pair with previous 1
            → good_pairs = 1
            → Update freq_map = {1: 2, 2: 1, 3: 1}

        i = 4: arr[4] = 1 → Seen before (1: 2)
            → Can form 2 good pairs with previous 1s
            → good_pairs = 1 + 2 = 3
            → Update freq_map = {1: 3, 2: 1, 3: 1}
        """
        count = 0
        hashmap = {}
        for num in nums:
            if not hashmap.get(num):
                hashmap[num] = 1
            else:
                count += hashmap[num]
                hashmap[num] += 1
        return count
    
    def _ansv2(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (optimized)
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 49/49
        _choke: none
        _brief:
        - first step is to tally the occurrences of each number in the nums array.
        - initialize a variable, say total_good_pairs, to 0.
        - iterate through your frequency map (or frequency array).
        - for each unique number and its corresponding count k:
            - if k is 2 or greater (meaning you have at least two occurrences of that number),
            calculate the number of good pairs it can form using the formula: k * (k - 1) // 2.
            - add this calculated value to total_good_pairs.
        - finally return the count; thats it !!!
        """
        count = 0
        counters = collections.Counter(nums)
        for k, v in counters.items():
            cnt = (v*(v-1)) // 2
            count += cnt
        return count

    def _ansv1(self, nums: List[int], n: int) -> int:
        """
        _run: accepted (brute-force)
        _code: tc: o(n^2), sc: o(1), rt: 1 ms, tcz: 49/49
        _choke: none
        _brief:
        - nested for_loop comes into the picture, where outer_loop iterate over i index and 
        nested loop iterate over j ~ (i+1) index.
        - if nums[i] == nums[j] then ++count; return final count
        """
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
        return count


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
