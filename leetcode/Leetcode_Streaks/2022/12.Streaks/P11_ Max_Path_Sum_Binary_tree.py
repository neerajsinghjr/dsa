'''
-------------------------------------------------------------------------------------
-> Problem Title: 124. Binary Tree Maximum Path Sum
-> Problem Status: Ongoing...
-> Problem Attempted: 12-12-2022
-> Problem Description: 
-------------------------------------------------------------------------------------

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them. A node can only appear in
the sequence at most once. Note that the path does not need to pass through
the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty
path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42

Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7= 42.
 

Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        atype: obj (obj of tree_node)
        rtype: int (sum of the path)
        """
        if not(root):
            return 0
        if(root.left == None and root.right == None):
            return root.val
        
        # return self.ansv1(root)
        return self.ansv2(root)

    def ansv1(self, root):
        """
        _run: accepted
        _code: optimised | time: o(n) | space: o(1) + stack(n)
        _study:
        traced the sum of the parent and two siblings nodes first 
        then recursively check for max sum
        """
        res = [root.val]

        def dfs(root):
            if not root: return 0
            # S1: Make dfs recursive calls;
            left_val, right_val = dfs(root.left), dfs(root.right)
            # S2: Handling negative node case;
            left_val, right_val = max(left_val, 0), max(right_val, 0)
            # S3: Check for maximum current result;
            res[0] = max(res[0], root.val + left_val + right_val)
            
            return (root.val + max(left_val, right_val))
        
        dfs(root)
        return res[0]


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
    