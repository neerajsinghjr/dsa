'''
-------------------------------------------------------------------------------------
-> Problem Title: 347. Top K Frequent Elements
-> Problem Status: Completed
-> Problem Attempted: 2024-03-10
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/top-k-frequent-elements/description/

Reference:-
https://youtu.be/YPTqKIgVk-k

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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        _stdin: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        if k == 1 and n == 1:
            return nums

        # return self.ansv1(nums, k, n)
        # return self.ansv2(nums, k, n)
        return self.ansv3(nums, k, n)

    def ansv3(self, nums, k, n):
        """
        _run: accepted
        _code: timeo (k*nlogn), space; (n)
        _choke: none
        _study:
        [+] We use a dictionary num_map to count the frequency of each element in
        the given list.
        [+] We maintain a min heap (min_heap) to keep track of the k elements with
        the highest frequencies.
        [+] We iterate through num_map and push each element with its frequency into
        the min heap.
        [+] If the size of the heap exceeds k, we pop the element with the lowest frequency.
        [+] Finally, we pop elements from the heap and add them to the result list,
        which is then reversed to  get the elements in descending order of frequency.
        """
        res, num_map = [], {}

        # Count the frequency of each element
        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1

        # Create a min heap to store the elements with their frequencies
        min_heap = []

        for num, freq in num_map.items():
            # Push the element and its frequency to the heap
            heapq.heappush(min_heap, (freq, num))

            # If the heap size exceeds k, pop the element with the lowest frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Pop the elements from the heap and add them to the result list
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            res.append(num)

        # Reverse the result list to get the elements in descending order of frequency
        return res[::-1]

    def ansv2(self, nums, k, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _choke: none
        _study: --- explanation refer ansv1() ---
        code level optimization only
        """
        res, num_map = [], {}
        # first we map the give num with their occurences;
        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1

        # second step we fetch num with their count for every
        # count we map nums.
        # eg, num = 1 comes 3 times then arr[3th] = [1]
        # num = 2 comes 4 times then arr[4th] = [2]
        freq_map = [[] for _ in range(n + 1)]  # improvement #1: default [] as improvement;;
        for num, freq in num_map.items():
            freq_map[freq].append(num)

        # now time we fetch the kth top frequent value as per
        # the reverse index b'coz index shows occurrence here
        for i in range(n, 0, -1):
            for val in freq_map[i]:  # improvement #2: remove if clause not needed;;
                res.append(val)
                k -= 1
            if k == 0:
                break

        return res

    def ansv1(self, nums, k, n):
        """
        _run: accepted
        _code: time: o(n), space: o(n)
        _choke: none
        _study:
        [+] result requirement is that we have to provide the maxium occurrence
        values from the given list.
        [+] challenge i faced is that i was able to map the num with its occurrence.
        But could n't able to figoue out how can i find the max occurence value each
        time the loop is running from the hashmap.
        ---- solution i got from the neetcode guy ----
        [+] steps to solution
        s1: create a hashmap the given num with their respective occurrences.
        s2: then we create a list (~ freq_map) where each index represents the frequency
        from hashmap, and the corresponding value is a list of elements with that frequency.
        s3: we iterate through num_map and populate the buckets with elements.
        s4: we traverse the freq_map in reverse order and add the elements to the result list.
        s5: loop breaks when the result size reaches k and the final result is the first k
        elements from the result list.
        """
        res, num_map = [], {}
        # first we map the give num with their occurences;
        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1

        # second step we fetch num with their count for every
        # count we map nums.
        # eg, num = 1 comes 3 times then arr[3th] = [1]
        # num = 2 comes 4 times then arr[4th] = [2]
        freq_map = [None for _ in range(n + 1)]
        for num, freq in num_map.items():
            if not freq_map[freq]:
                freq_map[freq] = [num]
            else:
                freq_map[freq].append(num)
        print("freq_map: ", freq_map)
        # now time we fetch the kth top frequent value as per
        # the reverse index b'coz index shows occurrence here
        for i in range(n, 0, -1):
            if freq_map[i]:
                for val in freq_map[i]:
                    res.append(val)
                    k -= 1
            if k == 0:
                break

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
