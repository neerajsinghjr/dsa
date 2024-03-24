'''
-------------------------------------------------------------------------------------
-> Problem Title: 1189. Maximum number of balloon
-> Problem Status: Completed
-> Problem Attempted: 2024-03-07
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/maximum-number-of-balloons/?source=submission-ac

Reference:-
https://youtu.be/G9xeB2-7PqY

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

    def maxNumberOfBalloons(self, text: str) -> int:
        # return self.ansv1(text)
        return self.ansv2(text)

    def ansv2(self, text):
        """
        run: accepted
        time: o(n)
        space: o(k) ~ only storing balloon chars map
        choke: none
        brief: optimized in terms of space, similarly mapping given text string
        and then check if the balloon char exists in text_map.
        """
        res, text_map = 0, {}
        for c1 in text:
            # ignore character which are not part of balloon;;
            if c1 in 'balloon':
                text_map[c1] = text_map.get(c1, 0) + 1
        # print("text_map: ", text_map)
        if not text_map:
            return res
        while True:
            for c2 in "balloon":
                # if the character is not in text_map or reduced to count 0, then return direct;;
                if text_map.get(c2, 0) == 0:
                    return res
                text_map[c2] -= 1
            res += 1

        return res

    def ansv1(self, text):
        """
        run: accepted
        time: o(n)
        space: o(k) ~ we are only string specific length string in map 'balloon'
        choke: none
        brief: solution cover 3 steps
         - firstly we map the required `balloon` character occurrence.
         - second we again map the occurrence of `text` string.
         - then we check required balloon chars occurence by dividing the
         occurrence of ballon character in text_map and balloon_map
        """
        res = float('inf')  # infinity in positive;;
        balloon = {}
        text_map = {}
        # balloon map for tra
        for c1 in "balloon":
            balloon[c1] = balloon.get(c1, 0) + 1
        for c2 in text:
            if c2 in "balloon":
                text_map[c2] = text_map.get(c2, 0) + 1
        for c3 in "balloon":
            res = min(res, text_map.get(c3, 0) // balloon[c3])

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
