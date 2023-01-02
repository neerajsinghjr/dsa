'''
-------------------------------------------------------------------------------------
-> Problem Title: 290. Word Pattern
-> Problem Status: Completed
-> Problem Attempted: 01-01-2023
-> Problem Description: 
-------------------------------------------------------------------------------------
     
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.

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
    A bijection is both onto and one-to-one.

    The conditions for bijectivity are satisfied if and only if the
    following is true:

    The counts of distinct elements in two groups and the count of distinct
    mappings are all equal. In terms of the figure, the count of the orange
    dots, the count of the green dots, and the count of arrows must all be
    equal. We can count the first two using len(set()) and the third one by
    len(set(zip_longest())).
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        atype: str ~pattern
        rtype: bool
        """
        return self.ansv1(pattern, s)

    
    def ansv1(self, pattern, s):
        """
        _run:
        _code:
        _choke:
        _study:
        """
        s = s.split(" ")
        res = (len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern,s))))
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
    