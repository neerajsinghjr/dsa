'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 451. Sort Characters By Frequency
-> Problem Status: Completed
-> Problem Attempted: 3/12/2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given a string s, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears in
the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"

Explanation: 'e' appears twice while 'r' and 't' both appear once. So 'e' must
appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"

Explanation: Both 'c' and 'a' appear three times, so both "cccaaa"
and "aaaccc" are valid answers. Note that "cacaca" is incorrect, as the same
characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"

Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect. Note
that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from collections import defaultdict, Counter


##---Main Solution;;
class Solution:
    
    ##--- Main Execution;;
    def frequencySort(self, s: str) -> str:
        n = len(s)
        if(n == 1):
            return n
        
        # return self.ansv1(s, n)
        # return self.ansv2(s, n)
        return self.ansv3(s, n)
    
    
    def ansv3(self, s, n):
        """
        Run: Accepted
        Code: Optimised | T: O(NLOGN) | S: O(N)
        Study:
        Approach tells that,
        1) Make the character counter list using the Counter.
        2) We use the array to map the char with the count.
        3) then, We map the array into the required result.
        """
        char_map = Counter(s)
        arr = [(count, char) for (char,count) in char_map.items()]
        arr.sort(reverse=True)
        return "".join(a[0]*a[1] for a in arr)
    
    
    def ansv2(self, s, n):
        """
        Run: Accepted
        Code: Pythonic | T: O(NLOGN) | S: O(N)
        Study:
        Here in this approach we are using counter from collections.
        Counter(characters) : Return count of items inside dict.
            @returns dict {'a': 1, 'b':5, 'c': 8}
        - Counter(chars).most_common(): Return the occurrences of
        items as list with tuple inside and tuple[0] is item itself
        and tuple[1] is the count of it.
            @return list<tuple> [('e', 2), ('t', 1), ('r', 1)]
        - for eg,
        string = "tree"
        res = Counter(string)     # Counter({'e': 2, 't': 1, 'r': 1})
        res.most_common()         # [('e', 2), ('t', 1), ('r', 1)]
        """
        char_map = Counter(s).most_common()        
        return "".join(char[0]*count for (char, count) in char_map)
        
    
    def ansv1(self, s, n):
        """
        Run: Accepted
        Code: Brute Force | T: O(N + NLOGN + N) ~ O(NLOGN) | S:O(N + N) ~ O(N)
        Study:
        In this approach, we are simply following,
        1) Map every character inside the dictionary with occurence counts.
        2) Sort the dictionary using value in reverse order.
        3) Again map the dictionary into the string to return result.
        """
        res = ""
        char_map = defaultdict(int)
        for char in s:
            char_map[char] += 1
        
        sort_map = dict(
            sorted(char_map.items(), key=lambda item: item[1], reverse=True)
        )
        
        for key,value in sort_map.items():
            i = value
            while(i):
                res += key
                i -= 1
            
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
    