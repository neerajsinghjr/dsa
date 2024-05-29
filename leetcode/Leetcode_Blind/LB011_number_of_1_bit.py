'''
-------------------------------------------------------------------------------------
-> Problem Title: 191. Number of 1 Bits
-> Problem Status: Completed
-> Problem Attempted: 2024-05-27
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/number-of-1-bits/description/

Reference:-
https://youtu.be/5Km3utixwZs?si=s7JVhHtY28Nnw2qc

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

    def hammingWeight(self, n: int) -> int:
        """
        _stdin:
            arg1: n : __int__
        _stdout: __int__
        """

        # return self.ansv1(n)
        return self.ansv2(n)

    def ansv2(self, n):
        """
        _run: accepted
        _code: ts: o(n), sc: o(1)
        _study:
        --- problem ---
        [+] before: num:  11 - 0b1011
        [+] before: num:  10 - 0b1010
        [+] before: num:  8 - 0b1000
        [+] before: num:  0 - 0b0
        --- explanation ---
        [+] Here in this solution we are directly subtracing the 1 from the num
        then we are proceding ahread and then incrementing the result.
        """
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res

    def ansv1(self, n):
        """
        _run: accepted
        _code: ts: o(k) ie. k < n, sc: o(1)
        _study:
        --- problem ---
        [+] number = 11 (binary: 0b1011)
        [+] before:num:  11 - 0b1011
        [+] before:num:  5 - 0b101
        [+] before:num:  2 - 0b10
        [+] before:num:  1 - 0b1
        [+] before:num:  0 - 0b0
        --- explanantion ---
        [+] problem statement revolves around counting the number of 1's in binary format.
        [+] so what we are doing is we are adding up the modulo of number % 2 to result.
        [+] after everytime we calculate the module result then we are just rigth shifting
        the number of one.
        """
        res = 0
        while n:
            res += n % 2
            n = n >> 1
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
