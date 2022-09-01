'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1448. Count Good Nodes in Binary Tree
-> Problem Status: Completed
-> Problem Attempted: 01.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 
Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

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
    
    ###---Main Execution;;;
    def goodNodes(self, root: TreeNode) -> int:
        if not(root):
            return 0
        
        if(root.left == None and root.right == None):
            return 1
        
        self.root = root
        
        return self.ansv1(root)
        # return self.ansv2(root)
    
    
    """
    Run: Success
    Code: DFS Solution | T:O(N) | S:O(1) + Stack(N)
    Study:
    This approach is just the coding wise crisp version of ansv1() 
    Same like before maintaining $mx variable for tracking maximum 
    variable while iterating left and similarly for right end.
    Tracking $good variable to count the good nodes, as per question.
    """
    def ansv2(self,root,mx=-10000):
        if(root == None):
            return 0
        
        return (
            (1 if(root.val >= mx) else 0) +
            (self.ansv2(root.left,max(root.val,mx))) +
            (self.ansv2(root.right, max(root.val,mx)))
        )
    
    
    """
    Run: Success 
    Code: Brute Force Recursive(DFS) | T:O(N) | S:O(1) + Stack(N)
    Study:
    This solution works like, we are maintaining a root variable and
    recursively iterating that variable till end node for left and right.
    While trtaversing we are counting the good nodes and setting the 
    maximum weightage node's value in $mx variable.
    
    ### There were two choked scenario for this solution, but handled.
    
    Bottleneck: 
    |#| Choke #1: [2,null,4,10,8,null,4] 
    
    
    |#| Choke #2: [
        -1,5,-2,4,4,2,-2,null,null,-4,null,-2,3,
        null,-2,0,null,-1,null,-3,null,-4,-3,3,
        null,null,null,null,null,null,null,3,-3
    ]
    
    Countermeasure: 
    Previously, I was only checking the good nodes count by comparing the 
    $curNode(~X) with the hard coded root node of the Tree. 
    I overcome this using $mx variable which track and update maximum value
    while iterating thoughout traversal
    """
    def ansv1(self,root,mx=-10000,good=0):         #ie, 1 <= node <= 10^5
        
        if(root == None): return good
        
        if(root.val >= mx):     
            mx = root.val
            good += 1
            
        if(root):
            good = self.ansv1(root.left,mx,good)
        
        if(root):
            good = self.ansv1(root.right,mx,good)
        
        return good
        
        


##---Main Execution;;
def main():
    try:
        # data = []               # ~ data
        # obj = Solution()
        # res = ""
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
    