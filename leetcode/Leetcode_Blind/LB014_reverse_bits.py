'''
-------------------------------------------------------------------------------------
-> Problem Title: 190. Reverse Bits
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/reverse-bits/description/

Referene:-
https://youtu.be/UcoN6UjAI64?si=THLxMYwM4-n1BWfl

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

    def reverseBits(self, n: int) -> int:
        """
        _stdin:
            arg1: n : __int__
        _stdout: int : __int__
        """
        return self.ansv1(n)

    def ansv1(self, n):
        """
        _run: accepted
        _code: ts: o(n), sc: o(1)
        _study:
        --- problem crux ---
        [+] problem is asking you to just reverse the bit for eg, 0100 => 0010
        --- explanation ---
        [+] we are doing exactly the same in which we are started fetching the digit
        from the right side and started to put into the exact left side in our result
        [+] we use left shift to bit everytime and then bitwise and with 1 (~00001).
        to get the exact bit value.
        [+] then we place the bit value in above step to the left side using the right
        shift and doing bitwise or to add the sum in the result.
        """
        res = 0

        for i in range(32):
            bit = (n >> i) & 1  # extracting right side bit;;
            res = res | (bit << (31 - i))  # placing right side bit to exact left side;;

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
