'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 393. UTF-8 Validation
-> Problem Status: Completed
-> Problem Attempted: 13.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given an integer array data representing the data, return whether it is a
valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded
characters).

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
rules:

For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0,
followed by n - 1 bytes with the most significant 2 bits being 10. This is how
the UTF-8 encoding would work:

     Number of Bytes   |        UTF-8 Octet Sequence
                       |              (binary)
   --------------------+-----------------------------------------
            1          |   0xxxxxxx
            2          |   110xxxxx 10xxxxxx
            3          |   1110xxxx 10xxxxxx 10xxxxxx
            4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

x denotes a bit in the binary form of a byte that may be either 0 or 1.

Note: The input is an array of integers. Only the least significant 8 bits of
each integer is used to store the data. This means each integer represents
only 1 byte of data.

 

Example 1:

Input: data = [197,130,1]
Output: true

Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:
Input: data = [235,140,4]
Output: false

Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
 
 
Constraints:
1 <= data.length <= 2 * 104
0 <= data[i] <= 255

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
    
    ###---Main Execution;;
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        
        if(n == 0): return False
        
        return self.ansv1(data,n)
        # return self.ansv2(data,n)
    
    
    """
    Run: Accepted
    Code: Optimised | T:O(N) | S:O(1)
    Study:
    The idea is to keep track the number of segments of utf-8 octet sequence left
    we increase / decrease the count based on some cases
    first you need to know that `x >> n` means shift the number `x` `n` bits to the right
    e.g. shift 110xxxxx 5 bits to the right becomes 110 (in binary format)
    e.g. shift 11110xxx 4 bits to the right becomes 1111 (in binary format)
    second, 0bxxxx is a binary literal which means xxxx is a binary number
    alternatively, you can use decimal format but it's not that convenient in this problem
    e.g. 0b1110 -> 14
    e.g. 0b11000000 -> 192
    """
    def ansv2(self,data,n):
        # used to track the remaining number of segments
        remaining = 0
        # iterate each data and perform the following logic
        for d in data:
            
            # case 1: there is no remaining segement left, 
            # then it means we should check the first segement of UTF-8 octet sequence
            # i.e. 0xxxxxxx (for no of. bytes = 1)
            # i.e. 110xxxxx (for no of. bytes = 2)
            # i.e. 1110xxxx (for no of. bytes = 3)
            # i.e. 11110xxx (for no of. bytes = 4)
            
            if(remaining == 0):
                

                if((d >> 5) == 0b110):
                    # case 1.1 - shift `x` 5 bits to the right
                    # i.e making the first (8 - 5) = 3 bits left
                    # e.g (110xxxxx >> 5) becomes 110 (in binary format)
                    # if it is 0b110, 
                    # then it is only possible to form `110xxxxx 10xxxxxx` 
                    # so we set remaining to 1 to look for `10xxxxxx` later
                    
                    remaining = 1
                
                elif((d >> 4) == 0b1110):
                    # case 1.2 -  shift `x` 4 bits to the right
                    # i.e making the first (8 - 4) = 4 bits left
                    # e.g (1110xxxx >> 4) becomes 1110 (in binary format)
                    # if it is 0b1110, 
                    # then it is only possible to form `1110xxxx 10xxxxxx 10xxxxxx`
                    # so we set remaining to 2 to look for `10xxxxxx 10xxxxxx` later

                    remaining = 2
                    
                elif((d >> 3) == 0b11110):
                    # case 1.3 -  shift `x` 3 bits to the right
                    # i.e making the first (8 - 3) = 5 bits left
                    # e.g (11110xxx >> 5) becomes 11110 (in binary format)
                    # if it is 0b11110, 
                    # then it is only possible to form `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
                    # so we set remaining to 3 to look for `10xxxxxx 10xxxxxx 10xxxxxx` later
                    
                    remaining = 3
                    
                else:
                    
                    if((d >> 7) != 0):
                        # case 1.4 -  shift `x` 7 bits to the right
                        # i.e making the first (8 - 7) = 1 bit left
                        # e.g (0xxxxxxx >> 7) becomes 0 (in binary format)
                        # here we cover the last case which is when Number of Bytes = 1
                        # we need to make sure the first bit is 0
                        # otherwise, it is not valid

                        return False
            else:
                
                if((d >> 6) != 0b10):
                    # case 2: check 10xxxxxx
                    # if we enter this part, that means it may be number of bytes 2, 3, or 4.
                    # based on the table in problem statement, we know what's left is just `10xxxxxx`
                    # therefore, we shift `x` 6 bits to the right
                    # i.e making the first (8 - 6) = 2 bits left
                    # e.g (10xxxxxx >> 6) becomes 10 (in binary format)
                    # if the first 2 bits are not 10 (in binary format), then it is not valid
                    
                    return False
                
                else:
                    # otherwise, this segement is ok so we decrease `remaining` by 1
                    remaining -= 1
                    
            
        
        return (True if(remaining == 0) else False)
            
        
    
    """
    Run: 
    Code: Optimized | T:O(N) | S:O(1)
    Study:
    Similarly follows up as already described in ansv2() comments...
    just a little bit difference instead of using remaining we are maintaining count
    and we are using masking in this process to count the number of ones in this 
    approach for 8 bit (0 -> 7).
    """
    def ansv1(self,nums,n):
        # p1: calculate the number of ones's inside a digit;
        def countOnes(num):
            count = 0
            for i in range(7,-1,-1):
                if(num & (1 << i)):
                    count += 1
                else:
                    break
            return count
        
        count = 0
        for num in nums:
            if not(count):
                count = countOnes(num)
                
                # count == 1 and count > 4  => False
                # because first octets like 0xxxxxxx, 110xxxxx, 1110xxxx, 11110xxx
                # single 1's doesn't include in any first octet
                # and same for count is not greater than 4;
                if(count == 1 or count > 4):        
                    return False
                
                # 0th bit UTF-Octet;
                if(count == 0):
                    continue 
                    
                count -= 1
            else:
                count = countOnes(num)
                # Here we are checking for leftovers octets with only one's count is 1 only
                # for eg, 10xxxxxx these values.
                if(count != 1):
                    return False
                else:
                    count -= 1
        
        return (True if(count == 0) else False)
                
        


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
    