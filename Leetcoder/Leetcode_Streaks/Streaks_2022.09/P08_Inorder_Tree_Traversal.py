'''
----------------------------------------------------------------------------------------------------
-> Problem Title:  94. Binary Tree Inorder Traversal
-> Problem Status: Completed.
-> Problem Attempted: 04.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given the root of a binary tree, return the inorder traversal of its nodes'
values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ###---Main Execution;;;
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        
        # return self.ansv1(root,[])
        return self.ansv2(root,[])
    
    
    """
    Run: Accepted
    Code: DFS Traversal | T:O(N) | S:O(N)
    Study:
    DFS approached with stack store and pop traversal
    Procedure as follows...
    1) Store all the nodes from left side to stack till bottom end;
    2) then, start Popping one by one node from top of stack;
    3) Check for the right link of the current popped node and update
    the current pointer;
    
    Note: DFS result will be generated from popping top node of stack;;
    """
    def ansv2(self,root,res=None):
        stack = []      # fifo stack;
        cur = root      # root;
        
        #p0:store nodes in stack then pop;
        while(cur or len(stack) > 0):
            # p1:traverse left node to end;
            while(cur != None):
                stack.append(cur)
                cur = cur.left
    
            #p2:popping from end of stack;
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
            
        return res
    
    
    """
    Run: Accepted 
    Code: Brute Force | T:O(N) | S:O(N)
    Study:
    In-Order Traversal says, 
    eg, Left -> Consume -> Right;
    """
    def ansv1(self,root,res=None):
        #p1: base condition;
        if(root == None): return 
        
        #p3:hypothesis left;
        if(root.left): res = self.ansv1(root.left,res)
            
        #p2:induction;
        res.append(root.val)
        
        #p4: hypothese right;
        if(root.right): res = self.ansv1(root.right,res)
        
        return res


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
    