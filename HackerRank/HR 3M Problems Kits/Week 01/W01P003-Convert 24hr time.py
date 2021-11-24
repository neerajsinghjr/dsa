'''
Problem:
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example 1:
Input: time = '12:01:00PM'
Output: '12:01:00PM

Example 2:
Input: Return '12:01:00AM'
Output: '00:01:00AM"
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(time):
    # time : 02:05:20PM
    hour = int(time[:2])
    if "PM" in time:
        if hour != 12:
            hour += 12
    if "AM" in time:
        if hour == 12:
            hour = 00
    
    # Add trailing zeroes to front for `am` and `pm`
    hour = str(hour).zfill(2)
    
    return f"{hour}{time[2:-2]}"
        

def main():
    res = timeConversion("2:00:01")
    print(res) if res else print("Empty!")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    