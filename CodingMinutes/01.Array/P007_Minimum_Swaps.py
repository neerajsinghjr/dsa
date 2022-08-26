'''
----------------------------------------------------------------------------------------------------
#Problem Title: Minimum Swaps
#Problem Status: Completed
#Problem Attempted: 12-08-2022
#Problem Description:
----------------------------------------------------------------------------------------------------
Given an array of size N, find the minimum number of swaps needed to make the array as sorted.

for eg,

Example 1:
input: [5,4,3,2,1]
Output: 2

Example 2:
Input: [10,11,5,4,3,2,1]
Output: 4
----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    
    def minimumSwaps(self,nums):
        n = len(nums)

        if(n == 0 or  n == 1):
            return 0

        if(n == 2):
            if(nums[0] > nums[1]):
                return 1

        # return self.ansv1(nums,n)
        return self.ansv2(nums,n)


    def ansv2(self,nums,n):
        res = 0
        dataset = []
        visited = [False]*n 

        for key,value in enumerate(nums):
            dataset.append((value,key))

        dataset.sort()

        for i in range(n):
            prevIndex = dataset[i][1]               # [0]: Value, [1]: Index;;  
            if(i == prevIndex):
                continue
            
            node = i
            cycle = 0
        
            while(visited[node] == False):
                visited[node] = True
                nextNodeIndex = dataset[node][1]
                node = nextNodeIndex
                cycle += 1

            res += (cycle-1) if(cycle > 0) else 0

        return res


    """
    Approach: Optimised
    Analysis: Time: (N) || Space: O(1)
    """
    def ansv1(self,nums,n):
        res = 0
        dataset = {}

        # S1: Map each value w.r.t index;
        for (key,value) in enumerate(nums):
                dataset[value] = key

        temp = sorted(dataset)
        dataset = {key:dataset[key] for key in temp}
        print(dataset)

        visited = [False]*n

        # S2: Internal Loop Count;

        for (key,value) in enumerate(dataset):

            # Case 1: If the node after sorting at the same place, that means no swapping needed;
            prevIndex = dataset[value]
            if(visited == True or key == prevIndex):
                continue
 
            # Case 2: When the index of node changed, swapping needed;
            node = key
            cycle = 0
            while(visited[node] == False):
                print(f"Curnode:{node} Curcycle:{cycle}")
                visited[node] = True
                nextNode = dataset[value]
                print(f"nextNode: {nextNode}")
                node = nextNode
                cycle += 1            
                print(f"exitCycle: {cycle}")

            res += (cycle-1)                # (cycle-1) removing the once extra loop from above;
            print(f"res: {res}")

        return res


def main():

    # try:
    nums = [5,4,3,2,1] 
    obj = Solution()
    res = obj.minimumSwaps(nums)
    print(f"Result: {res}") if res else print("Empty!")
        
    # except(Exception) as e:
    #     print(f"Exception Traced : {e}")
    
    # else:
    #     print("Program Completed : Success")

    # finally:    
    #     print("Program Terminated!")
      

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")
    