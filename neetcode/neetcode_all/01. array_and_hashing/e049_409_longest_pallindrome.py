'''
-------------------------------------------------------------------------------------
-> Problem Title: 409. Longest Palindrome
-> Problem Status: Completed
-> Problem Attempted: 24/07/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/longest-palindrome/description/

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

    def longestPalindrome(self, strs: str) -> int:
        """
        _stdin:
            arg: str
        _stdout: int
        """
        # return self._ansv1(strs)
        return self._ansv2(strs)
    
    def _ansv2(self, strs: str) -> int:
        """
        _run: accepted
        _code: tc: O(n), sc: o(k), rt: 0 ms, tcz: 97/97
        _choke: none
        _brief: --- fix for ansv1() --- 
        - this method calculates the length of the longest palindrome that can be built
        using the characters from the input string `s`. 
        - the key principle of forming a palindrome is:
            1.  all characters contributing to the palindrome must appear an even number 
            of times.
            2.  one single character can be placed in the very center of the palindrome.
        - the solution proceeds as follows:
            - It first counts the frequency of each character in the input string `s`
            - It then initializes `longest_palindrome_length` to 0 and a boolean flag 
            `odd_char_flag` to `False`.
            - It iterates through the counts of all characters:
                - For each character's `count`, it adds `(count // 2) * 2` to 
                `longest_palindrome_length`. This ensures that only the largest even 
                portion of characters is used (e.g., if a character appears 5 times, 
                4 of those characters are added; if 4 times, all 4 are added).
                - If a character's `count` is odd (`count % 2 == 1`), it means one 
                instance of that character is left over after forming pairs. This 
                character could potentially be used as the center of the palindrome. 
                The `has_odd_count_char` flag is set to `True` to record that at least 
                one such character exists.
            - Finally, if `has_odd_count_char` is `True` (meaning at least one character 
            had an odd count and could serve as a center), longest_palindrome_length by 1.
        """
        max_len = 0 
        odd_char_flag = False
        charmap = collections.Counter(strs)

        for count in charmap.values():
            # Add the largest even part of the character's count
            # Example: if count is 5, (5 // 2) * 2 = 2 * 2 = 4 is added.
            # Example: if count is 4, (4 // 2) * 2 = 2 * 2 = 4 is added
            max_len += count if count%2 == 0 else count-1 # alternative ie, (count//2)*2
            if count%2 == 1:
                odd_char_flag = True
        
        if odd_char_flag:
            max_len += 1

        return max_len
        
    def _ansv1(self, strs: str) -> int:
        """
        _run: rejected
        _code: tc: o(n), sc: O(k), rt: nan, tcz: 35/97
        _choke:
        [1] Incorrect handling of odd character counts: It only adds characters with 
        `val%2 == 0` (even counts) to `max_len`. For characters with odd counts (e.g., 
        'a' appearing 3 times, 'b' appearing 5 times), it completely ignores their 
        even portion (`count - 1`). For instance, if 'a' appears 3 times, 'aa' (2 
        characters) can be used, and one 'a' is left over for a potential center. The 
        current logic misses adding these `count - 1` characters.
        [2] Flawed central character detection (`x_cnt`): The `x_cnt = 1` condition is 
        only triggered if `val == 1`. This means if a character appears 3, 5, or more 
        times (odd counts), `x_cnt` will not be set, even though such characters can 
        also provide a single character for the palindrome's center. It only detects 
        single-occurrence characters.
        _brief: 
        - This method attempts to find the length of the longest palindrome buildable 
        from the input string `s`.
        - It tries to sum up characters with even counts for `max_len`. It then attempts 
        to account for a potential central character if any character appears exactly once. 
        - However, its logic for handling characters with odd counts (especially those 
        greater than 1) and determining the central character is incomplete.
        """
        charmap = collections.Counter(strs)

        if len(charmap) == 1:
            return charmap.get(strs[0])
        
        max_len, x_cnt = 0, 0
        for key, val in charmap.items():
            if val%2 == 0:
                max_len += val
            if val == 1:
                x_cnt = 1 

        return max_len+1 if x_cnt else max_len


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
