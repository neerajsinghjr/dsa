'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1383. Maximum Performance of a Team
-> Problem Status: Completed
-> Problem Attempted: 11.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

You are given two integers n and k and two integer arrays speed and efficiency
both of length n. There are n engineers numbered from 1 to n. speed[i] and
efficiency[i] represent the speed and efficiency of the ith engineer
respectively.

Choose at most k different engineers out of the n engineers to form a team
with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by
the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge
number, return it modulo 109 + 7.

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with
speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7).
That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68

Explanation:
This is the same example as the first but k = 3. We can select engineer 1,
engineer 2 and engineer 5 to get the maximum performance of the team. That is,
performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 

Constraints:
1 <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108

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
from heapq import heappush, heappop

class Solution:
    
    """
    Run: Accepted
    Code: Optimised | T:O(NLogN) | S:O(N)
    Study:
    Simply sort the efficiency array in decreasing order. But since the index numbers        
    between speed and efficiency correspond to each other, we shouldn’t just sort             
    efficiency. Instead, we can create another array that keeps speed and efficiency         
    together.

    We keep the queue with a maximum size of k, and when we add a new worker, we only
    need O(logK) to find the smallest speed in the team now
    
    Steps
    1) Sort efficiency with descending order.
    2) Maintain a min_heap to track the minimum speed of the team.
    3) Update performance after each loop.
    
    """
    def maxPerformance(self, n, speed, efficiency, k) -> int:
        
        engg = sorted(zip(efficiency, speed), reverse=True)
        
        min_heap, sum_of_speed, performance = [], 0, 0
        
        for eff, curr_speed in engg:
            heappush(min_heap, curr_speed)
            if len(min_heap) <= k: 
                sum_of_speed += curr_speed
            else: 
                sum_of_speed += curr_speed - heappop(min_heap)
                
            performance = max(performance, sum_of_speed * eff)
            
        return performance % 1000000007


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
    