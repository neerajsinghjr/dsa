'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1457. Pseudo-Palindromic Paths in a Binary Tree
-> Problem Status: Completed
-> Problem Attempted: 14.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

Given a binary tree where node values are digits from 1 to 9. A path in the
binary tree is said to be pseudo-palindromic if at least one permutation of
the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf
nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2 

Explanation: The figure above represents the given binary tree. There are
three paths going from the root node to leaf nodes: the red path [2,3,3], the
green path [2,1,1], and the path [2,3,1]. Among these paths only red path and
green path are pseudo-palindromic paths since the red path [2,3,3] can be
rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be
rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 

Explanation: The figure above represents the given binary tree. There are
three paths going from the root node to leaf nodes: the green path [2,1,1],
the path [2,1,3,1], and the path [2,1]. Among these paths only the green path
is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1
 

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9

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
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # traverse the tree, the set pairs maintains the number of each element
        # If you already have the same element in pairs, then remove it
        # Else, add it to pairs

        # In the leaf, if the set is empty, then its an even palindrome.
        # In the leaf, if the set has 1 element , its an odd palindrome.
        # In th leaf, if the set has > 1 elements, its not a palindrome.
        
        def traverse(node, pairs):
            if not node:
                return 0
            
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)
            
            if not node.left and not node.right:
                return 1 if len(pairs) <= 1 else 0
            
            # correct!!
            left = traverse(node.left, set(pairs))
            right = traverse(node.right, set(pairs))
            
            # wrong, becasue pairs will change after we traversed node.left or node.right!
            # left = traverse(node.left, pairs)
            # right = traverse(node.right, pairs)
            
            return left + right
        
        return traverse(root, set())
    
    
    ###---Main Execution;;
    def pseudoPalindromicPathsV2 (self, root: Optional[TreeNode]) -> int:
        if not(root): 
            return 0
        
        if(root.left == None and root.right == None):
            return 1
        
        # return self.ansv1(root,"",0)
        return self.ansv2(root,set())
        # return self.ansv3(root,"",{})
    
    
    """
    Run:
    Code: Optimise using Bit Map | T:O(N) | S:O()
    Study:
    """
    def ansv3(self,root):
        pass
    
    
    """
    Run:
    Code: Optimise using Set
    Study:
    """
    def ansv2(self, root, data=None):
        if(root == None): 
            return 0
        
        if(root.val in data):
            data.remove(root.val)
        else:
            data.add(root.val)
        
        if not(root.left and root.right):
            return (1 if(len(data) <= 1) else 0)
            
        if(root.left): 
            left = self.ansv2(root.left, set(data))
        
        if(root.right): 
            right = self.ansv2(root.right, set(data))
        
        return left+right
    
    
    """
    Run: 
    Code: Brute Force 
    Study:
    """
    def ansv1(self, root, data=None, res=None):
        if(root == None): return 
        
        if(root.val in data): 
            data.add(root.val)
        else:
            data.remove(root.val)
        
        if(root.left): res = self.ansv1(root.left, data, res)
            
        if(root.right): res = self.ansv1(root.right, data, res)
            
        print(f"@data -> {data}")
        
        res = self.checkPallindrome(data)
        
        print(f"@res -> {res}")
        
        return res  
    
    
    ###--- Helpers;;
    def checkPallindrome(self, data, res=0):
        print(f"@START -> {data}")
        i,n = 0,len(data)
        while(i <= n-1):

            # p1: make shuffle;
            x,num = 1,data[0]              # Swapping From Start;
            while(x <= n-1):
                data[x-1] = data[x]
                x += 1              # nested iter1++
            else:
                data[n-1] = num

            #p2: check for pallindrome;
            l,r = 0,n-1
            while(l <= r):
                if not(data[l] == data[r]):
                    break

                l,r = l+1,r-1       # nested iter2 ++

            else:
                res += 1

            print(f"data:res -> {data}:{res}")

            i += 1      ## main iter++

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
    