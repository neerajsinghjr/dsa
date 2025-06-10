'''
-------------------------------------------------------------------------------------
-> Problem Title: 347. Top K Frequent Elements
-> Problem Status: Completed
-> Problem Attempted: 10/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/top-k-frequent-elements/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import heapq
import collections


##---Main Solution
class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        _stdin:
            arg1: list[int]
        _stdout: list[int]
        """
        n = len(nums)
        # return self._ansv1(nums, n, k)
        # return self._ansv2(nums, n, k)
        return self._ansv3(nums, n, k)
    
    def _ansv3(self, nums: List[int], n: int, k: int) -> List[int]:
        """
        _run: accepted 
        _code: tc: o(n), sc: o(n), rt: 3 ms, tcz: 21/21
        _choke:
        _brief:
        - s1: hashmap, use a frequency_map to get number -> count for all elements. o(n) time.
        - s2: create an empty min-heap. We'll store (frequency, number) tuples in the heap. 
        python's heapq module is a min-heap.
        - s3: populating the heap...
            - iterate through each (num, count) pair in frequency_map.
            - if the heap's size is less than k: Simply push (count, num) onto the heap
            - if the heap's size is equal to k
                - check the smallest element in the heap (the root), which is heap[0][0].
                - if current count is greater than heap[0][0] then we will ...
                    - pop the root element (heapq.heappop)
                    - push the existing element into heap like heap.heappush((count, num))
        - s4: once all frequency_map items are processed, the heap will contain the kth most 
        frequent elements (or fewer, if there are less than k unique elements). extract the 
        numbers from the heap.
        - for eg, [1,1,1,2,2,3]
            - hashmap=Counter({1: 3, 2: 2, 3: 1})
            - if: min_heap=[(3, 1)]
            - if: min_heap=[(2, 2), (3, 1)]
            - else: min_heap=[(2, 2), (3, 1)]
            - end: min_heap=[(2, 2), (3, 1)]
            - ans=[2, 1]
        """
        # Step 1: Hashmap creation;
        hashmap = collections.Counter(nums)

        # Step 2: MinHeap Creation;
        min_heap = []
        for num, count in hashmap.items():
            if len(min_heap) < k:
                # If the heap is not yet full, just add the element
                heapq.heappush(min_heap, (count, num))
            else:
                # If the heap is full (size k), check if the current element's frequency
                # is greater than the smallest frequency in the heap (heap[0][0])
                if count > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (count, num))

        # Step 3: Pull Kth Top Frequenct Element;;
        ans = []
        while min_heap:
           ans.append(heapq.heappop(min_heap)[1])

        # Step 4: if order matters then we have to reverse it at end;;
        # ans.reverse()

        return ans

    def _ansv2(self, nums: List[int], n: int, k: int) -> List[int]:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 12ms, tcz: 21/21
        _choke:
        _brief: --- based on bucketsort algorithm ---
        - REMARK: in ansv1() we have to use the sorting algo which takes o(nlogn); because we had 
        to sort the tuple like [(num, count)...] into decreasing order on the basis of count
        - in this method we kept everything same but instead of using sorting algo, we use bucket
        sorting; in other words we map our hashmap {num:count} into buckets;
        - we create buckets using an array of lists, where the index represents a count, and  
        the list at that index contains all numbers that have that frequency.
        - now iterate through the buckets array from the highest frequency index down to 1 and add
        numbers to your result list until you have k elements.
        """
        ans = []
        hashmap = collections.Counter(nums)
        buckets = [[] for _ in range(n+1)] # don't use [[]] * (n+1);;
        # bucket creation;;
        for num, count in hashmap.items():
            buckets[count].append(num)
        # pulling kth top element;;
        for count in range(n, -1, -1):
            for num in buckets[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans

    def _ansv1(self, nums: List[int], n: int, k: int) -> List[int]:
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(n), rt: 8 ms, tcz: 21/21
        _choke: --- major drawback ---
        -  This is a correct approach but might not be optimal if $n is very large and $k is 
        relatively small. then o(nlogn) from sorting is the bottleneck.
        _brief:
        - count frequencies of all numbers; then sort based on these frequencies; then pick 
        the top k element
        - we map the num with its occurence inside a hashmap
        - we need to sort the hashmap on the basis of count. to sort this hashmap content on
        the basis of count; we convert it into list of tuple like [(num, count) ... ]
        - at the end we pull out the k element from the start and return it as answer 
        """
        cnt = 1
        num_map = collections.Counter(nums)
        num_cnt = [(num, count) for num, count in num_map.items()]
        num_sort = sorted(num_cnt, key=lambda x: x[1], reverse=True)
        ans = [num for num, cnt in num_sort[:k]]
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
