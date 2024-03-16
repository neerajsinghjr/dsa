'''
-------------------------------------------------------------------------------------
-> Problem Title: 560. Subarray Sum Equals K
-> Problem Status: Completed
-> Problem Attempted: 2024-03-16
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/subarray-sum-equals-k/description/

Reference:-
https://youtu.be/fFVZt-6sgyo

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
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        _stdin: list[int]
        _stdout: int
        """
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == k else 0

        # return self.ansv1(nums, k, n)
        return self.ansv2(nums, k, n)

    def ansv2(self, nums, k, n):
        """
        _run: accepted
        _code: time: o(n), space: (n)
        _study: --- optimal ----
        --- explanation ---
        [+] we use `cur_sum` to keep track of the cumulative sum of elements
        encountered so far.
        [+] we use a hashmap `prefix_sum` to store the frequencies of prefix sums.
        The key represents the prefix sum, and the value represents the count of
        occurrences of that prefix sum.
        [+] for each element num in the nums array, we update the prefix_sum and
        check if there is a subarray with sum equal to k by looking up (prefix_sum - k)
        in the prefix_sum hashmap. If found, we increment the count by the frequency
        of that prefix sum.
        [+] Finally, we update the sum_count with the current prefix sum's frequency.
        """

        count = 0  # this will hold the count of subarrays equals k;;
        cur_sum = 0  # this will hold the cumulative sum on every iteration;;

        # prefix_sum this will hold the prefix sum with its number of counts;;
        # default if 0 prefix_sum is mapped with 1 occurence, refer ansv1() ~choked;;
        prefix_sum = {0: 1}

        for n in nums:
            cur_sum += n
            difference = cur_sum - k

            # first we have to store the current difference value with the existing result;;
            count += prefix_sum.get(difference, 0)

            # now increment the exisiting of cur_sum by scale 1 in the prefix_sum hashmap;;
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return count

    def ansv1(self, nums, k, n):
        """
        _run: TLE[83/93]
        _code: time: o(n^2), space: o(1)
        _study: --- brute-force ---
        --- choke ---
        choke 1 : nums = [1,-1, 0], k = 0, output = 2, expected = 3
        choke_fix 1 : remove the break statement
        choke 2 : nums = [0,0], k = 0, output = 2, expected = 3
        choke_fix 2 :
        --- explanation ---
        simple and brute force apporach in which check sum of one value with
        rest of the number inside in the num list. if the target sum is equals
        to k, then increase the count else ignore.
        """
        count = 0
        for i in range(n):
            cur_sum = nums[i]
            if cur_sum == k:
                count += 1

            # choke_fix 2 :  earlier the below for loop was in the else block
            # that causes the choke_2 scenario. to avoid this i've marked the
            # for loop independent;;

            for j in range(i + 1, n):
                cur_sum += nums[j]
                if cur_sum == k:
                    count += 1
                    # break # choke_fix 1
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
