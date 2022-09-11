'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 814. Binary Tree Pruning
-> Problem Status: Completed
-> Problem Attempted: 06.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given the root of a binary tree, return the same tree where every subtree (of
the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:  
Only the red nodes satisfy the property "every subtree not
containing a 1". The diagram on the right represents the answer.

Example 2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.

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
    
    ###---Main Execution;;
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: return None
        
        return self.ansv1(root)
    
    
    """
    Run: Accepted
    Code: Recursive | T:O(N) | S:O(N)
    Study:
    Recursively, traversing every nodes left and right and return nodes only when
    the value of the root exist with value of 1, instead of 0. 
    """
    def ansv1(self,root):
        if(root == None): return None
        
        root.left, root.right = self.ansv1(root.left), self.ansv1(root.right)
        
        return(root if(root.left or root.right or root.val) else None)


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
    