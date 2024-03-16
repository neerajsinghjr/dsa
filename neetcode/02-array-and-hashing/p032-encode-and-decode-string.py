'''
-------------------------------------------------------------------------------------
-> Problem Title: 659. Encoding and Decoding String (Leetcode Premium)
-> Problem Status: Ongoing...
-> Problem Attempted:
-> Problem Description:
-------------------------------------------------------------------------------------

Problems:-
https://leetcode.com/problems/encode-and-decode-strings/
https://www.lintcode.com/problem/659/

Reference:-
https://youtu.be/B1k_sxOSgv8

Problem Description:-
Design an algorithm to encode a list of strings to a string. The encoded string is
then sent over the network and is decoded back to the original list of strings.

Because the string may contain any of the 256 legal ASCII characters, your algorithm
must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode"
and "decode" algorithms on your own

--- Example 1 ---
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

--- Example 2 ---
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Problem Constraints:
string can include alphabets or any other special character like .,!@#$%^&*() etc.

Because the string may contain any of the 256 legal ASCII characters, your algorithm
must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode"
and "decode" algorithms on your own

Problem Code Snippet:
Please implement encode and decode

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        pass

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        pass
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
    """
    _run: accepted
    _code: time: o(n), space: o(1)
    _study:
    --- explanation ----
    [+] In the encode function, each string in the list strs is encoded as
    'length#string', where length is the length of the string and string is
    the actual string. These encoded strings are concatenated together using
    a pount sign as a separator.
    [+] In the decode function, the encoded string is parsed to extract
    individual strings. We use a while loop to iterate over the encoded string.
    For each iteration, we find the colon index to determine the length of the
    next string. Then, we extract the string using string slicing and append it
    to the decoded_strings list.
    [+] Finally, we update the index i to continue parsing the remaining encoded
    string.
    """
    def encode(self, strs):
        return self._encode(strs)

    def decode(self, strs):
        return self._decode(strs)

    def _encode(strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def _decode(s):
        i, res = 0, []

        while i < len(s):
            j = i
            # iterate over the list to stored delimiter;;
            while s[j] != '#':
                j += 1

            # finding the length variable stored in string;;
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

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
