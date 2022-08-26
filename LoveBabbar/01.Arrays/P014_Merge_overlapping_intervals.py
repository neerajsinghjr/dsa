'''
#Problem Description:
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

#Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

#Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

#Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:
    
    def __init__(self):
        pass


    # Brute Force Approach
    def mergeIntervalsV1(self, intervals):
        res = []
        xr,yr,size = 0,0,len(intervals)
        for x in range(size):
            x1,x2 = intervals[x][0], intervals[x][1]
            for y in range(x+1, size):
                y1,y2 = intervals[y][0],intervals[y][1]
                if(x1 < y1 and y1 < x2):
                    res.append([min(x1,y1),max(x2,y2)])
                elif(x1 < y2 and y2 < x2):
                    res.append([min(x1,y1),max(x2,y2)])
                    
        return res


    # Optimised Approach ~ O(nlogn)
    def mergeIntervalsV2(self, intervals):
        # base case;
        # if not intervals:   return None

        # main case;
        res = []
        intervals.sort(key = lambda x:x[0]) # or intervals.sort() also works
        # print(intervals)
        for (key,currentInt) in enumerate(intervals):
            if key == 0:
                # print("key is zero")
                res.append(currentInt)          # Store first interval by default;
            else:
                lastInt = res[-1]               # LastInterval : Track min and max of last range;
                # Check for Interval in-between the Last Interval
                if(lastInt[1] >= currentInt[0] and currentInt[0] >= lastInt[0]):
                    res[-1][0] = min(lastInt[0], currentInt[0])     # Update Last Min Point;
                    res[-1][1] = max(lastInt[1], currentInt[1])     # Update Last Max Point;
                else:
                    res.append(currentInt)
        return res 

    
def main():
    try:
        nums = [[2,3],[2,6],[15,18],[1,3],[2,6],[8,10],[9,11],[15,18]]
        obj = Solution()
        # res = obj.mergeIntervalsV1(nums)
        res = obj.mergeIntervalsV2(nums)
        print(res) if res else print("Empty!")
        res1 = obj.merge(nums)
        print(res1)
        
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
    