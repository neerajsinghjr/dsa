'''
-------------------------------------------------------------------------------------
-> Problem Title: 1160. Find Words That Can Be Formed by Characters
-> Problem Status: 01/07/2025
-> Problem Attempted: Completed
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class Solution:
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
        _stdin:
            arg1: list[str]
            arg2: chars
        _stdout: int
        """
        # return self._ansv1(words, chars)
        # return self._ansv2(words, chars)
        return self._ansv3(words, chars)
    
    def _ansv3(self, words: List[str], chars: str) -> int:
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(n+k), rt: 68 ms, tcz: 36/36
        _choke: none
        _brief: -- simplified the code structure ---
        - create a frequency map (e.g., a dictionary chars_freq) that stores each character 
        from chars as a key and its count as the value.
        - initialize count = 0 holds the lengths of all good words.
        - create a temporary frequency map (word_freq) for the current word.
            - assume is_current_word_good = True.
            - iterate through each character and its count in word_freq
            - pull the frequency of single char from charmap and wordmap as char_cnt, word_cnt
            - validate if the word_cnt should be smaller than the char_cnt; if not then 
            this is not good_word; else increament the good_len count
        """
        count = 0
        charmap = collections.Counter(chars)
        for word in words:
            is_good_word = True
            wordmap = collections.Counter(word)
            for char, freq in wordmap.items():
                if not freq <= charmap.get(char, 0):
                    is_good_word = False
                    break
            if is_good_word:
                count += len(word)
        return count

    def _ansv2(self, words: List[str], chars: str) -> int:
        """
        _run: accepted
        _code: tc: o(n*k), sc: o(n+k), rt: 68 ms, tcz: 36/36
        _choke: none
        _brief:
        - create a frequency map (e.g., a dictionary chars_freq) that stores each character 
        from chars as a key and its count as the value.
        - initialize count = 0 holds the lengths of all good words.
        - create a temporary frequency map (word_freq) for the current word.
            - assume is_current_word_good = True.
            - iterate through each character and its count in word_freq
            - pull the frequency of single char from charmap and wordmap as char_cnt, word_cnt
            - validate if the word_cnt should be smaller than the char_cnt; if not then 
            this is not good_word; else increament the good_len count
        """
        count = 0
        charmap = collections.Counter(chars)
        for word in words:
            is_good_word = True
            wordmap = collections.Counter(word)
            for ch in wordmap:
                char_cnt = charmap.get(ch, 0)
                word_cnt = wordmap.get(ch, 0)
                if not word_cnt <= char_cnt:
                    is_good_word = False
                    break
            if is_good_word:
                count += len(word)
        return count
    
    def _ansv1(self, words: List[str], chars: str) -> int:
        """
        _run: rejected
        _code: none 
        _choke: logic inproper 
        _brief:
        - charset = set(chars): This creates a set of unique characters from chars.
        - wordset = set(word): This creates a set of unique characters from the current word.
        - len(wordset - charset) == 0: This only checks if all unique characters in word are 
        present among the unique characters in chars. It completely ignores how many times 
        each character actually appears.
        """
        count = 0
        charset = set(chars)
        for word in words:
            wordset = set(word)
            if len(wordset - charset) == 0:
                count += len(word)
        return count


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
