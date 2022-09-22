'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 557. Reverse Words in a String III
-> Problem Status: Completed
-> Problem Attempted: 22.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space

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
    def reverseWords(self, s: str) -> str:
        n = len(s)
        if(n <= 1): 
            return s
        
        # return self.ansv1(s,n)
        # return self.ansv2(s,n)
        return self.anvs3(s,n)
    
    """
    Run: Accepted
    Code: Brute Force | T:O(N*K) | S:O(1)
    Study:
    
    """
    def anvs3(self,s,n):
        i = 0
        res = ""
        flag = False
        start = 0
        while(i < n):
            if(i == n-1 or s[i] == " "):
                cur = i-1 if(s[i] == ' ') else i        # trailing space check
                
                while(cur >= start):
                    res += s[cur]
                    cur -= 1            # iter2--
                    
                res += ' ' if(s[i] == ' ') else ''      # in-between spaces
                start = i + 1
                
            i += 1          # iter1++
        
        return res
    
    
    """
    Run: Accepted
    Code: Pythonic V2 | T:O(N) | S:O(N)
    Study:
    Follow note's thread of ansv1()
    """
    def ansv2(self,s,n):
        return "".join(word[::-1] for word in s.splits())
            
    
    """
    Run: Accepted
    Code: Pythonic V1 | T:O(N) | S:O(N)
    Study:
    Steps to approach...
    # step1: split the string
    #   split() = ["Let's","take","LeetCode","contest"]
    # step2: reverse the list 
    #   s.split()[::-1] = ["contest","LeetCode","take","Let's"]
    # step3: convert each element to string separated by space
    #   ' '.join(s.split()[::-1]) = "contest LeetCode take Let's"
    # step4: reverse the string 
    #   ' '.join(s.split()[::-1])[::-1] = "s'teL ekat edoCteeL tsetnoc"    
    """   
    def ansv1(self,s,n):
        
        return " ".join(s.split()[::-1])[::-1]


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
    