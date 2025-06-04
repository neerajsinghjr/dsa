'''
-------------------------------------------------------------------------------------
-> Problem Title: 49. Group Anagrams
-> Problem Status: Completed
-> Problem Attempted: 05/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/group-anagrams/description/

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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        _stdin:
            arg1: list[str]
        _stdout:
            list[list[str]]
        """
        n = len(strs)
        if n == 1:
            return [strs]
        # return self._ansv1(strs, n)
        return self._ansv2(strs, n)
    
    def _get_char_count(self, word):
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        return tuple(count)
    
    def _ansv2(self, strs: List[str], n: int) -> List[List[str]]:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n), rt: 23 ms
        _choke: none
        _brief:
        - this solution also uses the same approach like in ansv1() but only things removed
        is sorted which was taking the o(nlogn) time
        - instead of that we are counting the ascii character distance and storing it as 
        index in an count array like
        - for grouping the anagram, we just map the particular string into the array index. 
        for eg, 'eat', 'tea' both have same count index that means they are anagram.
        --- how 'eat', and 'tea' are same ---
        we have taken array with 26th indices for holding occurence of character in 
        above example. 
        To assign index for single character in the array, we use ascii index.
        
        count = []
        count[ord('e') - ord('a')] += 1
        
        here, ord('e') is 101 and ord('a') is 97 
        so now the count will point to 4th index and we increament it by 1

        count[4] += 1   
        
        in simple word we map occurence of 'e' as 1.
        """
        ans = []
        groups = {}
        for s in strs:
            key = self._get_char_count(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return [v for k,v in groups.items()]

    
    def _ansv1(self, strs: List[str], n: int) -> List[List[str]]:
        """
        _run: accepted
        _code: tc: o(nlogn), sc: o(n), rt: 11 ms 
        _choke: none
        _brief:
        - approach based on sorting the string as anagram are jumble words only. 
        - expectancy is if we sort words them we can easily match the similary amongs them
        - sorted words need to be converted to tuple to be used as unique hash which furhter 
        map to the hashmap groups.
        - final iteration is just to pull collection words from every key and put in ans
        """
        ans = []
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        ans = [kv for kg, kv in groups.items()]
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
