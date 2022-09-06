'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1763. Longest Nice Substring
-> Problem Status: Ongoing...
-> Problem Attempted: 04.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
 
A string s is nice if, for every letter of the alphabet that s contains, it
appears both in  uppercase and lowercase. For example, "abABB" is nice
because 'A' and 'a' appear, and 'B'  and 'b' appear. However, "abA" is not
because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are
multiple, return the substring of the earliest occurrence. If there are none,
return an empty string.

Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the 
alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole
string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:
1 <= s.length <= 100
s consists of uppercase and lowercase English letters.

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
    
   def __init__(self):
    pass


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
    