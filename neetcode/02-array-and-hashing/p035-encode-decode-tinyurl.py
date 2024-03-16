'''
-------------------------------------------------------------------------------------
-> Problem Title: 535. Encode and Decode TinyURL
-> Problem Status: Completed
-> Problem Attempted: 2024-03-14
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/encode-and-decode-tinyurl/description/

Reference:-
https://youtu.be/VyBOaboQLGc

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
class Codec:

    """

    """
    def __init__(self):
        self.enc_map = {}
        self.dec_map = {}
        self.base = 'https://http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.enc_map:
            var = str(len(longUrl) + 1)
            tinyUrl = self.base + var
            self.enc_map[longUrl] = tinyUrl
            self.dec_map[tinyUrl] = longUrl

        return self.enc_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dec_map.get(shortUrl)


##---Main Execution;;
def main(res=None):
    try:
        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))
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
