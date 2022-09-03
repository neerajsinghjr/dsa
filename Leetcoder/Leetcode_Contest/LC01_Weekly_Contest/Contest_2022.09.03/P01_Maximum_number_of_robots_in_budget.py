'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 6143. Maximum Number of Robots Within Budget
-> Problem Status: Ongoing...
-> Problem Attempted: 03.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of 
length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. 
You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where 
max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of r
unning costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed 
budget

Example 1:

Input: chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25
Output: 3 
Explanation:  
It is possible to run all individual and consecutive pairs of robots within budget. 
To obtain answer 3, consider the first 3 robots. 
The total cost will be max(3,6,1) + 3 * sum(2,1,3) = 6 + 3 * 6 = 24
which is less than 25. It can be shown that it is not possible to run more
than 3 consecutive robots within budget, so we return 3. Example 2:

Input: chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19
Output: 0
Explanation: No robot can be run that does not exceed the budget, so we return 0.
 

Constraints:

chargeTimes.length == runningCosts.length == n
1 <= n <= 5 * 104
1 <= chargeTimes[i], runningCosts[i] <= 105
1 <= budget <= 1015

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
    
    def maximumRobots(self, chargeTimes, runningCosts, budget) -> int:
        
        k = 0
        flag = False
        threshold = None
        ct = len(chargeTimes)
        rc = len(runningCosts)
        
        curMaxUsage = chargeTimes[0] + runningCosts[0]
        if(curMaxUsage > budget):
            return k

        i = 1
        
        flag = True
        
        while(i < ct and i < rc):
            k = (k+1) if(k+1) < ct else k
            curMaxUsage = max(chargeTimes[:i]) + k*sum(runningCosts[:i])
            print(f"curMaxUsage: {curMaxUsage}")
            if(curMaxUsage > budget): 
                k  = k - 1
                break
            i += 1
        
        return k
        


##---Main Execution;;
def main():
    try:
        chargeTimes = [8,76,74,9,75,71,71,42,15,58,88,38,56,59,10,11]
        runningCosts = [1,92,41,63,22,37,37,8,68,97,39,59,45,50,29,37]
        budget = 412
        obj = Solution()
        res = obj.maximumRobots(chargeTimes, runningCosts, budget)
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
    