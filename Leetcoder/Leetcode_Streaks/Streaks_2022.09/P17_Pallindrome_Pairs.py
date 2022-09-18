'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 336. Palindrome Pairs
-> Problem Status: Ongoing...
-> Problem Attempted: 17.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given a list of unique words, return all the pairs of the distinct indices
(i, j) in the given list, so that the concatenation of the two words words
[i] + words[j] is a palindrome.

 

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]
 

Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.

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
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        
        # return self.ansv1(words,n)
        # return self.ansv2(words,n)
        return self.ansv3(words,n)
    
    """
    Run: ...
    Code: Prefix & Suffix Optimize | T:O(N*K) | S:O(N)
    Study:
    """
    def ansv3(self, words, n):
        res = set()             # avoid duplicate pairs;
        wordMap = {w:i for i,w in enumerate(words)}
        
        # Single iteration for 'n' words;;
        for (i,word) in enumerate(words):
            # Iteration for k length of single string;;
            for j in range(len(word)+1):
                pre,suf = word[:j], word[j:]        # pre:prefix and suf:suffix;
                ipre,isuf = pre[::-1],suf[::-1]     # ipre:inverse prefix and isuf:suffix;
                
                # p1: prefix and inverse prefix are same;
                if(pre == ipre):
                    #p2: check for inverse of suffix;
                    if(isuf in wordMap and wordMap[isuf] != i):
                        res.add((wordMap[isuf], i))
                
                # p3: suffix and isuffix are same;
                if(suf == isuf):
                    # p4: look for ipre in wordMap;
                    if(ipre in wordMap and wordMap[ipre] != i):
                        res.add((i, wordMap[ipre]))
        
        return [r for r in res]
                
                    
    """
    Run: TLE
    Code: Brute Force Optimized(~Mem) | T:O(N^2) | S:O(1)
    Study:
    Follow up ansv1();
    """
    def ansv2(self, words, n):
        res = []
        
        for i in range(n):          # i: index of original list;
            for j in range(n):          # j: index of stored reversed list;
                if(i != j):
                    if(self.isPallindrome(words[i],words[j][::-1]) == True):
                        res.append([i,j])
        
        return res
    
    
    """
    Run: TLE 
    Code: Brute Force | T:O(N^2) | S:O(N)
    Study:
    Simple brute force apporach, we are storing every given string in reverse order
    in a Trie then everytime we iterate we are checking pallindrome of every single
    string with the rest of the string.
    Checking pallindrome is easy...
    - Check one array from start and other from the end at the same time 
    if any case occured where the checkPallindrome() return false, then
    continue for second.
    """
    def ansv1(self, words, n):
        res = []
        trie = {}
        
        # p1: every string mapped with trie in reversed-order;
        # because one string must read of left -> right and so
        # other one should be read from right -> left fashion.
        for (key,word) in enumerate(words):
            trie[key] = word[::-1]
            
        for i in range(n):          # i: index of original list;
            for j in trie:          # j: index of stored reversed list;
                if(i != j):
                    if(self.isPallindrome(words[i],trie[j]) == True):
                        res.append([i,j])
        
        return res 
    
    
    ###---Helper: Checking Pallindrome;
    def isPallindrome(self,src,trg):             
        i,j = 0,0
        n,m = len(src)-1, len(trg)-1
        
        # p1: check till both in size equals;
        while(i <= n and j <= m):
            if not(src[i] == trg[j]):
                return False
            i,j = i+1,j+1
        
        # p2: check for remaining length of source string;
        while(i <= n):
            if not(src[i] == src[n]):
                return False
            i,n = i+1,n-1
        
        # p3: check for remaining letters for target string;
        while(j <= m):
            if not(trg[j] == trg[m]):
                return False
            j,m = j+1,m-1
        
        return True


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
    