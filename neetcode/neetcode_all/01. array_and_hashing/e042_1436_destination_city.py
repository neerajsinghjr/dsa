'''
-------------------------------------------------------------------------------------
-> Problem Title: 1436. Destination City
-> Problem Status: Completed
-> Problem Attempted: 06/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/destination-city/description/

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
from typing import List


##---Main Solution
class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        """
        _stdin:
            arg1: list[list[str]]
        _stdout: str
        """
        n = len(paths)
        if n == 1:
            return paths[0][1]
        # return self._ansv1(paths, n)
        return self._ansv2(paths, n)
    
    def _ansv2(self, paths: List[List[str]], n: int) -> str:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 0 ms, tcz: 104/104
        _choke:
        _brief:
        - this solution optimizes the search for the destination city using a set for 
        efficient lookups.
        - it first populates a set with all unique source cities from the given paths.
        - then, it iterates through all destination cities.
        - for each destination city, it checks if that city is present in the set of 
        source cities.
        - the first destination city found that is NOT in the set of source cities is 
        identified and returned as the unique destination city.
        """
        src_city_set = set()
        for src, _ in paths:
            src_city_set.add(src)
        for _, des in paths:
            if des not in src_city_set:
                return des

    def _ansv1(self, paths: List[List[str]], n: int) -> str:
        """
        _run: accepted
        _code: tc: o(n^2), sc: o(1), rt: 2 ms, tcz: 104/104 
        _choke: none
        _brief:
        - this solution employs a brute-force approach to identify the destination city.
        - it iterates through each city designated as a destination.
        - for every destination city, it then checks all source cities to determine if any 
        path originates from it.
        - if a destination city is found that does not appear as a source city in any path, 
        it is returned as the final destination.
        """
        for _, des in paths:
            is_final_city = True
            for src, _ in paths:
                if src == des:
                    is_final_city = False
                    break
            if is_final_city:
                return des


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
