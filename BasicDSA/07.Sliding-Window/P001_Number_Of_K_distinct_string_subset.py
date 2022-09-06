'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1876. Substrings of Size Three with Distinct Characters
-> Problem Status: Completed
-> Problem Attempted: 03.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.

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
    
    ###---Main Execution;;;
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        
        if(n <= 2): return 0
        
        return self.ansv1(s,n)
        # return self.ansv2(s,n)
    
    
    """
    Run: Success
    Code: Optimised (Set) | T:O(3*N) | S:(K)
    Study:
    Same approach as follow in ansv1(), but little bit optimised we use 
    set for storing next 3 char value becoz the lookup is O(1) in set
    """
    def ansv2(self,s,n):
        data = set()                # Set
        i = 0
        itr,count = 0,0
        
        while(itr < n):
            i,cur = 0,itr
            while(i < 3 and cur < n):
                if not(s[cur] in data):
                    data.add(s[cur])
                    cur += 1
                    if(len(data) == 3):
                        count += 1              # count updated;
                        data.clear()            # dataset reset;
                else:
                    data.clear()
                    break                                
                    
                i += 1                  # i++
            itr += 1                    # itr++
        
        return count
    
    
    """
    Run: Success
    Code: Brute Force | T:O(3*N) | S:O(1)
    Study: 
    Iterating two loops twice,
    1) First Loop should iterate to N numbers
    2) For every number's index, iterate for next 3 element and check for redundancy.
    and if redundancy found, then skip the loop and go to next number otherwise for 
    3 iteration increase the count+1.
    """
    def ansv1(self,s,n) -> int:
        count = 0
        for i in range(n-3+1):
            temp = ""
            for j in range(i,i+3):
                if not(j < n and s[j] in temp):
                    temp += s[j]
                    if(len(temp) == 3):
                        count += 1
                        temp = ""
                else:
                    break
        
        return count


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
    