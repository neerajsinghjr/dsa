'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 383. Ransom Note
-> Problem Status: Completed
-> Problem Attempted: 25.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the 
letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1) 1 <= ransomNote.length, magazine.length <= 105
2) ransomNote and magazine consist of lowercase English letters.

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random

from collections import Counter


###--- Main Solution;;
class Solution:
    
    #---Main Execution;;
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(ransomNote == magazine):
            return True
        
        # return self.ansv1(ransomNote,magazine)
        # return self.ansv2(ransomNote,magazine)
        return self.ansv3(ransomNote,magazine)
    
    
    """
    Code: Optimized | T:O(R+M) | S:(R+M)
    Study:
    Simple, Counter from 'Collection' return the every char with its number of
    counts. So, using counter on both variable and then subtracting counter of
    $ransomNote with $magazine will result either the None or the leftout 
    key:value pair. 
    """
    def ansv3(self,ransomNote,magazine):        
        return not(Counter(ransomNote) - Counter(magazine))  
    
    
    """
    Code: Optimized | T:(N+R+M) | S:(R+M)
    Study:
    In this approach, we are using Counter from 'collections', which return the 
    individual count of every character in the string.
    then we've iterate over the RansomNote individual char and check the number of
    counts and return False
    """
    def ansv2(self,ransomNote, magazine):
        c1,c2 = Counter(ransomNote), Counter(magazine)
        
        for char in ransomNote:
            if(c1[char] > c2[char]):
                return False
            
        return True
    
    
    """
    Code: Brute Force | T:O(N) | S:O(N)
    Study:
    Easy solution where you've mapped count of every $char from $magazine in hashset,
    then iterate single character from ransomNote and validate the number of counts 
    from the hashset;
    """
    def ansv1(self,ransomNote, magazine):
        data = {}               # map
        
        for char in magazine:
            if(char in data):
                data[char] += 1
            else:
                data[char] = 1
        
        for char in ransomNote:
            if(char not in data): return False
            
            if(data[char] == 0): return False
            
            data[char] -= 1
            
        return True
        

##---Main Execution;;
def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
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
    