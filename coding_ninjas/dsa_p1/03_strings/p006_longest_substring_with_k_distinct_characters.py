'''
-------------------------------------------------------------------------------------
-> Problem Title: Longest Substring With K Distinct Characters
-> Problem Status: Completed
-> Problem Attempted: 02/10/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms/content/118626/offering/1377986?leftPanelTab=1

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
def getLengthofLongestSubstring(ch, k):
    # Write your code here.
    if not ch: 
    	return 0
    
    return ans_v4(ch, k)
    # return ans_v1(ch, k)
    # return ans_v2(ch, k)
    # return ans_v3(ch, k)


def ans_v4(s, k):
    if k <= 0:
        return ""

    max_length = 0
    max_length_substring = ""
    start = 0
    char_count = {}  # Dictionary to keep track of character frequencies

    for end in range(len(s)):
        # Add the character at the end of the window to the char_count dictionary
        char = s[end]
        char_count[char] = char_count.get(char, 0) + 1

        # If the number of distinct characters exceeds 'k', shrink the window from the left
        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0
                del char_count[left_char]
            start += 1

        # Update the maximum length if the current window is longer
        if end - start + 1 > max_length:
        	# return max_length of subs
t            max_length = end - start + 1
            # return longest substring;
            # max_length_substring = s[start:end + 1]

    return max_length


def ans_v3(ch, k):
    # breif:
    # - We need to first find the exact window with k distinct element
    # by using the j pointer.
    # - But, when window having k+1 unique element then you have start
    # deleting the element from the start using the i pointer.
    # - i pointer manage removal of element from the window
    # - j pointer manage to add element in window;;

    n = len(ch)
    i, j = 0, 0
    result = 0
    char_map = {}
    while(j < n):
        # print("len:",len(char_map.keys()), 'k:',k, 'char:', ch[j])
        if len(char_map.keys()) <= k:
            result = max(result, sum(char_map.values()))    
            char_map[ch[j]] = char_map[ch[j]]+1 \
                if ch[j] in char_map  else 1
            # print("if: ", char_map)
            # print("result: ", result)
            # j pointer to add new item to window;;
            j += 1
        else:
            print("else: ", char_map, 'for: ', ch[i])
            while(len(char_map.keys()) > k):
                if char_map.get(ch[i]) == 0:
                    # print("else::if: ", char_map, 'for: ', ch[i])
                    char_map.pop(ch[i])
                else:
                    # print("else::else: ", char_map, 'for: ', ch[i])
                    char_map[ch[i]] -= 1
                # print("else::final char_map: ", char_map)
                # i pointer to remove item from window;;
                i += 1

    return result


def ans_v2(ch, limit):
	# brief: Didn't work out either because tried to calculate
	# unique and duplicate character from string manipulation;
    n = len(ch)
    unique = 0
    duplicate = 0
    char_set = []
    for c in ch:
        print("loop c: ", c)
        if c in char_set and unique > limit:
            # Note: Functionality to store the characters 
            # in char_set and increment the counters;;
            unique = unique + 1 if not(c in char_set) else unique
            duplicate += 1
            char_set.add(c)
        else:
            # Note: functionality to remove the characters
            # from char_set and reset the current distinct
            # character count;;
            unique -= 1
            duplicate -= 1

    return unique + duplicate


def ans_v1(ch, limit, n):
	# brief: Not working because of bad solution approached;
	# It was a sliding window protcol but tried to count with 
	# unique_character only with string manipulation.
    n = len(ch)
    max_chars = 0
    unique_chars = 0
    char_set = set()
    for c in ch:
        if c in char_set or unique_chars > limit:
            # Note: Functionality to store the characters 
            # in char_set and increment the counters;;
            visited_chars.add(c)
            unique_chars = unique_chars + 1 if not(c in char_set) else unique_chars
            max_chars = max(max_chars, len(char_set))
        else:
            # Note: functionality to remove the characters
            # from char_set and reset the current distinct
            # character count;;
            print("else c: ", c, "dc: ", unique_chars, "mc:", max_chars, "cs: ", len(char_set))

    return max_chars


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
    