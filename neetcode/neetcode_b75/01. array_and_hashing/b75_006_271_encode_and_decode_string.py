'''
-------------------------------------------------------------------------------------
-> Problem Title: 271. Encode and Decode Strings
-> Problem Status: Ongoing...
-> Problem Attempted: 18/01/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/encode-and-decode-strings/description/

other, online ide
https://neetcode.io/problems/string-encode-and-decode/question?list=blind75


leetcode 271 — encode and decode strings

[+] you are given a list of strings
[+] you need to encode this list into a single string
[+] the encoded string should be decodable back to the original list
[+] implement two functions:
[+] encode(strs: list[str]) -> str
[+] decode(s: str) -> list[str]
[+] no restriction on characters inside the strings
[+] strings may contain any ascii characters, including symbols and digits
[+] decoding must return the exact original list, in the same order

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


##---Main Solution
class Solution:


    def encode(self, strs: List[str]) -> str:
        """
        _run: accepted
        _code: tc: o(n), sc: o(1)
        _choke: 
        [+] don't think of converting simple string by concatenating the list of string
        into one string in one go. Because here raw string can contains alphabets, comma,
        digits etc.
        _brief:
        [+] our choke approach of simply concatenating the list of string words into a 
        flatten string
        [+] in addition to above we are also calculating the size of every string from list
        and concatenating into the new string called $sizes and append it in as prefix into
        our main raw message with a delimiter say a hash sign(#)
        [+] for eg,
            strs = ["Hello", "World"]
            encoded_str_format = f"{sizes}#{raw_message}"
            encoded_str_message = f"{5,5}#{HelloWorld}"
        """
        if not strs:
            return ""
        sizes = ""  # format: "5,5"
        msg = ""    # format: "HelloWorld"
        rslt = ""   # format: f"{sizes}#{msg}"
        for s in strs:
            sizes += str(len(s)) + ","
            msg += s
        rslt = f"{sizes}#{msg}"
        # print(f"{rslt=}")
        return rslt

    def decode(self, s: str) -> List[str]:
        """
        _run: accepted
        _code: tc: o(n), sc: o(n)
        _choke: nan
        _brief:
        [+] in this method we are simple decoding the encoded format, which is nothing 
        but f"{sizes}#{raw_message}
        [+] below is the simple code to fetch the format the string only
        """
        n = len(s)        
        if n == 0:
            return []
        
        # Decoding the actual sizes of messages;;
        dl = 0
        while dl < len(s):
            if s[dl] == "#":
                break
            dl += 1
        sizes = s[0:dl-1].split(',')
        msg = s[dl+1:]
        
        # Decoding the messages using the sizes;;
        idx = 0
        rslt= []
        for sz in sizes:
            sz_int = idx + int(sz)
            rslt.append(msg[idx:sz_int])
            idx = int(sz_int)
        
        return rslt


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
