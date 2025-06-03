'''
-------------------------------------------------------------------------------------
-> Problem Title: 1408. String Matching in an Array
-> Problem Status: Completed
-> Problem Attempted: 20/05/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/string-matching-in-an-array/submissions/

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
    
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        _stdin:
            args: list[str]
        _stoudt: list[str]
        """
        n = len(words)
        if n == 1:
            return []
        # return self._ansv1(words, n)
        # return self._ansv2(words, n)
        # return self._ansv3(words, n)
        return self._ansv4(words, n)
    
    def _ansv4(self, words: List[str], n: int) -> List[str]:
        """
        _run:
        _code: tc: o(n*k), sc: o(1), rt: 3 ms
        _choke: none
        _brief: 
        - simple counting apporach, we have making the all words in a delimited character
        separated string.
        - iterately using every word and counting the appearance in the text 
        - if_contraints_1: counting each word appearance > 1 then its a substring. 
        """
        text = "#".join(words)  # unique separator to avoid false positives
        return [w for w in words if text.count(w) > 1]

    def _ansv3(self, words: List[str], n: int) -> List[str]:
        """
        _run: accepted (optimized for _ansv2())
        _code: tc: o(n*k), sc: o(1), rt: 0ms
        _choke: na
        _brief:
        - crux of this approach is kind of sorting words based on length. because it is 
        more likely sorter length words would be substring of bigger length words.
        - then the two loop, checking one word from one loop in nested second loop.
        - as soon as one substring is traced then we can break the loop and check for
        another one.
        """
        ans = []
        words.sort(key=len) # sorted based on length of words;;
        for i in range(n):
            for j in range(i+1, n):
                if words[i] in words[j] and words[i] not in ans:
                    ans.append(words[i])
                    break
        return ans

    def _ansv2(self, words: List[str], n: int) -> List[str]:
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(1), rt: 1ms
        _choke: na
        _brief:
        - crux of this approach is kind of sorting words based on length. because it is 
        more likely sorter length words would be substring of bigger length words.
        - then the two loop, checking one word from one loop in nested second loop.
        - as soon as one substring is traced then we can break the loop and check for
        another one.
        """
        ans = set()
        words.sort(key=len) # sorted based on length of words;;
        for i in range(n):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    ans.add(words[i])
                    break
        return list(ans)

    def _ansv1(self, words: List[str], n:int) -> List[str]:
        """
        _run: accepted
        _code: tc: o(n^2), sc: o(n), rt: 3ms
        _choke:
        - before adding a word to ans make sure its unqiue else ignore.
        _breif:
        - iterating two loops over time, picking one word from loop_1 and checking existing
        in loop_2.
        - if word is unique then append it to the $ans_list and return it back.
        """
        ans = []
        for w1 in words:
            for w2 in words:
                if w1 == w2:
                    continue
                elif w1 in w2 and w1 not in ans:
                    ans.append(w1)
        return ans


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
