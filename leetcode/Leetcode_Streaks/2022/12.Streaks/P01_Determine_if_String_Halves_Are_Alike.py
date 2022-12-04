'''
-------------------------------------------------------------------------------------
-> Problem Title: 1704. Determine if String Halves Are Alike\
-> Problem Status: Completed
-> Problem Attempted: 01/12/2022
-> Problem Description: 
-------------------------------------------------------------------------------------

You are given a string s of even length. Split this string into two halves of
equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains
uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false. 

Example 1:

Input: s = "book"
Output: true

Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel.
Therefore, they are alike.


Example 2:
Input: s = "textbook"
Output: false

Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2.
Therefore, they are not alike. Notice that the vowel o is counted twice.

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
    
    ###--- Main Execution;;
    def halvesAreAlike(self, s) -> bool:
        n = len(s)
        if(n%2 != 0):
            return False
        
        # return self.ansv1(s, n)
        return self.ansv2(s, n)
    
    
    def ansv2(self, s, n):
        """
        Run: Accepted
        Code: Optimised | T: O(N) | S:O(1)
        Study:
        Optimised using the String, which reduced the space to O(1).
        """
        mid = n//2
        s1, s2 = s[:mid], s[mid:]
        v1, v2 = 0, 0
        vowels = 'aeiouAEIOU'
        for (c1,c2) in zip(s1,s2):
            if(c1 in vowels): v1 += 1
            if(c2 in vowels): v2 += 1

        return (True if(v1 == v2) else False)
        

    def ansv1(self, s, n):
        """
        Run: Accepted
        Code: Brute Force | T: O(N) | S:O(N)
        Study:
        Simple approach,
        1) Storing the start -> mid and mid -> end in two differnt string.
        2) Check for vowels present inside the string.
        3) return result if two of them have same length else false.
        """
        mid = n//2
        s1, s2 = s[:mid], s[mid:]
        v1, v2 = 0, 0
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        for (c1,c2) in zip(s1,s2):
            if(c1 in vowels): v1 += 1
            if(c2 in vowels): v2 += 1
                
        return (True if(v1 == v2) else False)


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
    