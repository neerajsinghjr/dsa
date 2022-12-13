'''
-------------------------------------------------------------------------------------
-> Problem Title: 1339. Maximum Product of Splitted Binary Tree
-> Problem Status: Completed
-> Problem Attempted: 12/12/2022
-> Problem Description: 
-------------------------------------------------------------------------------------

Given the root of a binary tree, split the binary tree into two subtrees by
removing one edge such that the product of the sums of the subtrees is
maximized.

Return the maximum product of the sums of the two subtrees. Since the answer
may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after
taking it.


Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110

Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10.
Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90

Explanation: Remove the red edge and get 2 binary trees with sum 15 and
6.Their product is 90 (15*6)
 
Constraints:
The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104

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

    ###--Main-Execution;;
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if(root.left == None and root.right == None):
            return root.val

        return self.ansv1(root)

    def ansv1(self, root):
        """
        _run: accepted
        _code: brute force | time: o(n + n) ~ o(n) | space: o(n) + stack(n) 
        _study: refer hints
        reference from hint section,
        1) we have recursively calculated the sum of a individual subtree
        by adding left_node + right_node + root.val;
        2) stored the every sum inside the list.
        3) doing it recursively, we initally get the sum of the whole subtree
        4) we have taken the stagewise individual subtree _sum and also total_sum 
        from vector, then we find the remaining subtree sum using...
        remaining_tree_sum = _sum * (total - _sum)
        """
        res = []
        mod = pow(10, 9) + 7
        def dfs(root):
            if not(root):
                return 0
            l_sum = dfs(root.left)
            r_sum = dfs(root.right)
            _sum = l_sum + r_sum + root.val         # total sum of tree;
            res.append(_sum)            
            return _sum

        dfs(root)
        max_sum, total_sum = 0, max(res)
        for r in res:
            max_sum = max(max_sum, r*(total_sum-r))
        return max_sum % mod

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
    