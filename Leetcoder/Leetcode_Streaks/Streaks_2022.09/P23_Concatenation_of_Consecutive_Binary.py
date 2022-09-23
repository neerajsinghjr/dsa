'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1680. Concatenation of Consecutive Binary Numbers
-> Problem Status: Completed
-> Problem Attempted: 23.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given an integer n, return the decimal value of the binary string formed by
concatenating the binary representations of 1 to n in order, modulo 109 + 7.
 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

Example 2:
Input: n = 3
Output: 27

Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11". After 
concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:
Input: n = 12
Output: 505379714

Explanation: The concatenation resultsin "1101110010111011110001001101010111100". 
The decimal value of that is 118505380540. After modulo 109 + 7, the result is 
505379714.
 

Constraints:

1 <= n <= 105

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
    # 11011 -> 16+8+2+1
    def concatenatedBinary(self, n: int) -> int:
        if(n == 1):
            return 1
        
        if(n == 2):
            return 2
        
        # return self.ansv1(n)
        # return self.ansv2(n)
        return self.ansv3(n)
    
    
    """
    Run: Accepted
    Code: Optimized using Bitmap | T:O(N) | S:O(1)
    Study:
    - the idea is to use bit manipulation to set the current number based on the previous number
    - for example, 
    - n = 1, ans = 0b1
    - n = 2 (10), we need to shift 2 bits of the previous ans to the left and add `n`
    - i.e. 1 -> 100 (shift 2 bits to the left) -> 110 (set `10`). ans = 0b110
    - n = 3 (11), we need to shift 2 bits of the previous ans to the left and add `n` 
    - i.e 110 -> 11000 (shift 2 bits to the left) -> 11011 (set `11`). ans = 0b11011
    - n = 4 (100), we need to shift 3 bits of the previous ans to the left and add `n`
    - i.e. 11011 -> 11011000 (shift 3 bits to the left) -> 11011100 (set `100). ans = 0b11011100
    - so now we can see a pattern here
    - we need to shift `l` bits of the previous ans to the left and add the current `i` 
    - how to know `l`? it is not difficult to see `x` only increases when we meet power of 2
    """
    def ansv3(self,n):
        res,bit = 0,0
        Mod = 10**9 + 7
        for i in range(1,n+1):
            # i & (i - 1) means removing the rightmost set bit
            # e.g, bit = 0 (initally)
            #   1 & 0 => (0000 0001) & (0000 0000) => 0 => bit = 1
            #   2 & 1 => (0000 0010) & (0000 0001) => 0 => bit = 2 
            #   3 & 2 => (0000 0011) & (0000 0010) => 1 => bit = 2 ( NO CHANGE)
            # after removal, if it is 0, then it means it is power of 2
            # as all power of 2 only contains 1 set bit
            # if it is power of 2, we increase the bit length `l`
            
            if(i & (i-1) == 0):
                bit += 1
            
            # (res << l) means shifting the orginal answer `l` bits to th left
            # (x | i) means  using OR operation to set the bit
            # for eg, res = (0000 0000) initally,
            # for eg, When bit = 1 (ref. above),
            #  1) Shift $res by $bit, (0000 0000 << 1) -> res = 0000 0000
            #  2) Add(Bitwise Or), $i to $res, (0000 0000) | (0000 0001) => (0000 0001)
            # for eg, now res = (0000 0001), then i = 2, then bit = 2
            #  1) Shift $res by $bit, (0000 0001 << 2) -> (0000 0100) 
            #  2) Add(BitWise Or), $i to $res, (0000 0100) | (0000 0010) => (0000 0110)
                    
            res = ((res << bit) | i) % Mod      # Avoid large binary numbers;
    
        return res 
    
    
    """
    Run: Accepted
    Code: Brute Force ~V2 | T:O(N) | S:O(1)
    Study:
    follow up explanation in ansv1();
    """
    def ansv2(self, n):
        res = ""
        for i in range(1,n+1):
            res += bin(i)[2:]           # bin(88) -> '0b1011000' removing '0b'
            
        return int(res,2) % (10**9 + 7)
    
    
    """
    Run: Accepted
    Code: Brute Force ~V1 | T: O(N) | S:O(1)
    Study:
    Iterating and storing all the decimal number to binary then loop stops;
    Finally, converting to int with base 2 and then modulo with (10**9+7).
    """
    def ansv1(self,n):
        res = ""
        for i in range(1,n+1):
            res += format(i, 'b')           # format to binary number;
            
        return int(res, 2) % (10**9 + 7)


##---Main Execution;;
def main():
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
    