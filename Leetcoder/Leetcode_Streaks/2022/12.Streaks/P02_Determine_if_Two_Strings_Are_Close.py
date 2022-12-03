'''
-------------------------------------------------------------------------------------
-> Problem Title: 1657. Determine if Two Strings Are Close
-> Problem Status: Ongoing...
-> Problem Attempted: 03/12/2022
-> Problem Description: 
-------------------------------------------------------------------------------------

Two strings are considered close if you can attain one from the other using
the following operations:

Operation 1: Swap any two existing characters. For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into
another existing character, and do the same with the other character. For
example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close,
and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true

Explanation: You can attain word2 from word1 in 2 operations. 
Apply Operation 1: "abc" -> "acb" 
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false

Explanation: It is impossible to attain word2 from word1, or vice versa, in
any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

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
from collections import Counter
class Solution:
    
    ###---Main Execution;;
    def closeStrings(self, word1, word2) -> bool:
        n1, n2 = len(word1), len(word2)
        if not(n1 == n2):
            return False
        
        # return self.ansv1(word1, word2, n1, n2)
        return self.ansv2(word1, word2, n1, n2)
    
    
    def ansv2(self, w1, w2, n1, n2):
        """
        ~ Run: Accepted 
        ~ Code: Optimised | T: O(NLONG) | S:O(N)
        ~ study:
        In this approach, first step we take is to measure the count of 
        single individual character count using the Counter collection
        function. 
        Then, We 've sorted only the values of the Counter not the key.
        because here the values shows the required occurences of character 
        that can fill up that space using switch or swap.
        Then, We have only check uniquness of the character by converting 
        string into sets.
        """
        freq_w1 = sorted(Counter(w1).values())  # Single character count of word_1;
        freq_w2 = sorted(Counter(w2).values())  # Single character count of word_2;
        
        return (freq_w1 == freq_w2) and (set(w1) == set(w2))
    
    
    def ansv1(self, word1, word2, n1, n2):
        """
        ~ Run: Rejected (Passed 132/152)
        ~ Code: Brute Force | T: O(NLOGN) | S: O(N)
        ~ Study:
        In this approach, we first sorted the whole string. So that 
        we can trace the sequence of the character inside the string.
        Then, we have Count the character using Counter.
        Then, check if the keys of both words are same and also check 
        whether the sum of the frequencies in both Counter are same.
        ~ Choke:
        Input : Word1 : "abbzzca", Word 2: babzzcz"
        Output : true
        Expected : false
        """
        w1, w2 = sorted(word1), sorted(word2)
        w1, w2 = Counter(w1), Counter(w2)
        
        return (w1.keys() == w2.keys()) and (w1.values() == w2.values())


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
    