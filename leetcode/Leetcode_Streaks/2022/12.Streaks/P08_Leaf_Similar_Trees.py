	'''
-------------------------------------------------------------------------------------
-> Problem Title: 872. Leaf-Similar Trees
-> Problem Status: Completed
-> Problem Attempted: 08/12/2022
-> Problem Description: 
-------------------------------------------------------------------------------------
Consider all the leaves of a binary tree, from left to right order, the values
of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
8).

Two binary trees are considered leaf-similar if their leaf value sequence is
the same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.
 
Example 1:
Input: 
root1 = [3,5,1,6,2,9,8,null,null,7,4], 
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 
Constraints:
The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

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

    ##---Main Execution
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not(root1 and root2):
            return False
      
        # return self.ansv1(root1, root2)
        return self.ansv2(root1, root2)
    
    def ansv2(self, root1, root2):
        """
        Run: Accepted
        Code: Python Optimised | T:O(N+M) | S:O(N+M) + STACK(N+M)
        Study:
        Python Optimised code, in this generator are using for loop.
        Everytime a single value of the root node is returned back 
        to the previously recursive calling function.
        """
        def leafs(root):
            if(root.left or root.right):
                if(root.left):
                    for value in leafs(root.left):
                        yield value
                if(root.right):
                    for value in leafs(root.right):
                        yield value
            else:
                yield root.val

        return list(leafs(root1)) == list(leafs(root2))
        
    def ansv1(self, root1, root2):
        """
        Run: Accepted
        Code: Brute Force | T:O(N+M) | S:O(N+M) + STACK(N+M)
        Study:
        Simple approach, traversing with the inorder style traversal till 
        the end of the node and storing all leafs node inside the lists 
        and check if both equals or not;
        """
        def leafs(root, res):
            if(root.left == None and root.right == None):
                res.append(root.val)

            if(root.left): res = leafs(root.left, res)
            if(root.right): res = leafs(root.right, res)

            return res

        return leafs(root1, []) == leafs(root2, [])


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
    