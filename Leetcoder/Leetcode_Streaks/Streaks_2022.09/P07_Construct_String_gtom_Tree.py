    '''
----------------------------------------------------------------------------------------------------
-> Problem Title: 606. Construct String from Binary Tree
-> Problem Status: Completed.
-> Problem Attempted: 07.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given the root of a binary tree, construct a string consisting of parenthesis
and integers from a binary tree with the preorder traversal way, and return
it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
relationship between the string and the original binary tree.

 
Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to
omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the
first parenthesis pair to break the one-to-one mapping relationship between
the input and the output.
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
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
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    ###---Main Execution;;;
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if(root == None): return ""
        
        if not(root.left and root.right): return f"{root.val}"
        
        # return self.ansv1(root, "",True)
        return self.ansv2(root)
    
    
    """
    Run: Rejected (Bug)
    Code: 
    Study:
    """
    def ansv2(self,root):
        # Case 1: When given root is None;;
        if(root == None):
            return ""
        
        res = str(root.val)
        
        # Case 2: When left recursive func call exist;
        if(root.left):
            res += "({})".format(self.ansv2(root.left))
            
        # Case 3: When both left node and right node are None;;
        if(root.left == None and root.right == None):
            res += ""
        
        # Case 4: When left node is empty but right is not;
        if(root.left == None and root.right != None):
            res += "()"
        
        # Case 5: When right recursive func call exist;
        if(root.right):
            res += "({})".format(self.ansv2(root.right))
        
        return res
            
    
    """
    Run: Rejected (Bug)
    Code: Recursive (Brute Force)
    Study
    
    Here left is used for opening the node brackets and right side is used 
    for closing the node bracket;
    """
    def ansv1(self,root,res="",flag=False):
        # p1: base condition;
        if(root == None): return 
        
        if(flag):
            res += f"{root.val}"
        else:
            res += f"({root.val}" if(root) else ")"
            
        # if(root.val): res += f"({root.val}"
            
        print(f"U:node:res: {root.val}:{res}")
        if(root.left): res = self.ansv1(root.left,res)
        
        # c1: check for () for tree balancing countermeasures;
        if(root.left == None and root.right != None): 
            print(f"S:node:res: {root.val}:{res}")
            res += "()"
        
        # c2: chek for right side reach;
        if(root.right): res = self.ansv1(root.right,res)
            
        # res += "(" if(root.right) else ")"
        
        # c3: right side bracket needs to close, asap
        # when right nodes hits bottom end;
        if not(root.right): res += ")"
            
        print(f"L:node:res: {root.val}:{res}")
            
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
    