	'''
-------------------------------------------------------------------------------------
-> Problem Title: 938.Range Sum of BST
-> Problem Status: Completed
-> Problem Attempted: 07/12/2022
-> Problem Description: 
-------------------------------------------------------------------------------------

Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range
[low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 
Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

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
    
    #---Main-Execution;;
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if not(root):
            return root
        
        return self.ansv1(root, low, high)

    def ansv1(self,root,low,high,res=0):
        """
        Run: Success
        Code: Brute Force | T:O(N) L S:O(1) + STACK(N)
        Study:
        Simple recursively ierating all the nodes in the BST
        and checking each node in between LOW and HIGH.
        if its in between then add it to $res otherwise skip.
        """
        if(root == None):
            return 
              
        if(root.val in range(low,high+1)):
            res += root.val
        
        if(root.left):
            res = self.ansv1(root.left,low,high,res)
        if(root.right):
            res = self.ansv1(root.right,low,high,res)
            
        return res


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
    