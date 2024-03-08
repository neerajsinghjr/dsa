'''
-------------------------------------------------------------------------------------
-> Problem Title: 205. Isomorphic Strings
-> Problem Status: 2024/03/03
-> Problem Attempted: Completed
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/isomorphic-strings/description/

Reference:-
https://youtu.be/7yF-U1hLEqQ

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
    def isIsomorphic(self, s, t) -> bool:
        # return self.ansv1(s, t)
        return self.ansv2(s, t)

    def ansv2(self, s, t):
        """
        run: accepted
        time: o(n)
        space: o(n+n) ~ o(n)
        choke: none
        brief: overcome the mapping problem in ansv1()
        Here i've map the every 's' character to respective 't' character.
        if any duplicate character is coming again, then we are checking
        if its the same previously mapped character then they are isomorphic
        otherwise they are not isomorphic.
        """
        s_map, t_map = {}, {}
        for idx in range(len(s)):
            c1, c2 = s[idx], t[idx]
            # check if ith index 's' string already mapped to another string character in s_map;;
            if c1 in s_map and s_map[c1] != c2:
                return False
            # check if ith index 't' string already mapped to another string character in t_map;;
            if c2 in t_map and t_map[c2] != c1:
                return False

            s_map[c1], t_map[c2] = c2, c1

        return True

    def ansv1(self, s, t):
        """
        run: failed to build brute force solution
        time: o(2 * n)
        space: o(2 * n)
        choke: none
        brief: I took the wrong approach. I map character with their occurrence
        for the both cases in the hashmap and due to this, I was not able to
        conclude the final boolean status of isomorphic stirng.
        failed to check if keys for both hashmap or the values of hashmap are equal.
        """
        s_map, t_map = {}, {}
        for sc in s:
            s_map[sc] = s_map.get(sc, 0) + 1
        for tc in t:
            t_map[tc] = t_map.get(tc, 0) + 1

        s_key = s_map.keys()
        t_key = t_map.keys()

        return len(s_key) == len(t_key)


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
