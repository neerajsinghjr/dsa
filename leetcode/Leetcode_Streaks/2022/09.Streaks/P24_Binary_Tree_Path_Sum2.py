'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 113. Path Sum II
-> Problem Status: Completed
-> Problem Attempted: 24.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given the root of a binary tree and an integer targetSum, return all
root-to-leaf paths where the sum of the node values in the path equals
targetSum. Each path should be returned as a list of the node values, not
node references.

A root-to-leaf path is a path starting from the root and ending at any leaf
node. A leaf is a node with no children.

 

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    # Main Execution;
    def pathSum(self, root, targetSum) -> List[List[int]]:
        
        self.res = []
        
        self.ansv1(root, targetSum, [], 0)
        # self.ansv2(root, targetSum, [])
        
        return self.res      # array are passed as reference;
    
    
    """
    Run: Accepted
    Code: Optimised | T:O(N) | S:O(N) + STACK(N)
    Study:
    Same approach as described in ansv1(), but the fact here is that instead of tracing
    sum. In this approach we are reducing the current node value from the node value and
    checking if any case target is reduced to zero or not
    if its reached it zero and the current node is leaf node then got the answer else
    move forward for another path;
    """
    def ansv2(self, root, remainingSum, path):
        if not(root): return
        
        path.append(root.val)
        
        if not(root.left) and not(root.right) and (remainingSum == root.val):
            self.res.append(list(path))
        
        self.ansv2(root.left, remainingSum - root.val, res, path)
        
        self.ansv2(root.right, remainingSum - root.val, res, path)        
        
        path.pop()        

    
    """
    Run: Accepted 
    Code: Brute Force | T:O(N) | S:O(N) + STACK
    Study:
    Simple recursively iterating from root to leaf node tracking sum of every node.
    Its the current sum equals to target then append to result else move forward.
    """
    def ansv1(self, nod, target, _path, _sum):
        
        if not(nod): return 

        if not(nod.left) and not(nod.right) and _sum + nod.val == target:
            self.res.append(_path + [nod.val])

        self.ansv1(nod.left, target, _path + [nod.val], _sum + nod.val)

        self.ansv1(nod.right, target, _path + [nod.val], _sum + nod.val)
        


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
    