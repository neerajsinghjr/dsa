'''
-------------------------------------------------------------------------------------
-> Problem Title: 1026. Maximum Difference Between Node and Ancestor
-> Problem Status: Completed
-> Problem Attempted: 09/12/2022
-> Problem Description: 
-------------------------------------------------------------------------------------
Given the root of a binary tree, find the maximum value v for which there
exist different nodes a and b where v = |a.val - b.val| and a is an ancestor
of b.

A node a is an ancestor of b if either: any child of a is equal to b or any
child of a is an ancestor of b.

Example 1:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
Input: root = [1,null,2,null,0,3]
Output: 3   
 
Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

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

    def __init__(self):
        self.res = 0

    #---Main Execution;;
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not(root): 
            return 

        # return self.ansv1(root)
        # return self.ansv2(root)
        return self.ansv3(root)

    def ansv3(self, root):
        """
        _run: accepted
        _code: optimised | time: o(n) | s:o(1) + stack(n)
        _study: refer ansv1 __study__ and __countermeasure__ (ii)
        """
        def dfs(root, low, high):
            if not(root): 
                return
            low,high = min(low,root.val), max(high,root.val)
            temp = max(abs(high-root.val), abs(low-root.val))
            self.res = max(self.res, temp)
            dfs(root.left, low, high)    # left recursive call;
            dfs(root.right, low, high)   # right recursive call;

        dfs(root, root.val, root.val)    # initiate recursive call;
        return self.res

    def ansv2(self, root):
        """
        _run: accepted
        _code: optimised | time: o(n) | s:o(1) + stack(n)
        _study: refer ansv1 __study__ and __countermeasure__ (i)
        """
        res = [0]
        def dfs(root, low, high, res):
            if not(root): 
                return
            low,high = min(low,root.val), max(high,root.val)
            temp = max(abs(high-root.val), abs(low-root.val))
            res[0] = max(res[0], temp)
            dfs(root.left, low, high, res)  # left recursive call;
            dfs(root.right, low, high, res) # right recursive call;

        dfs(root, root.val, root.val, res)   # initiate recursive call;
        return res[0]
    
    def ansv1(self, root):
        """
        _run_: rejected
        _code_: brute force | time : o(n) | space : (1) + stack(n)
        _study_: 
        this approach is good but the implementation is having issues.
        like, using the same variable in recursive calls is not keeping the trace
        of required calculated result. Everytime we return the calculated result 
        to the previous stack call traced function. Then it is replacing the 
        result.
        _countermeasure_:
        i) we can use the array for this scenario, instead of a single variable.
        and that array can be used single variable on 0th index
        ii) we can also use that class property to hold the answer so that it can 
        trace the state of the calculated result. regardless of the recursive calls
        
        """
        def dfs(root, low, high, res=None):
            if(root == None):  
                return res

            low, high = min(low, root.val), max(high, root.val)
            temp = max(abs(low-root.val), abs(high-root.val))
            if res: res = max(res, temp)            # res variable is overriding
            left_res = dfs(root.left, low, high, res)
            right_res = dfs(root.right, low, high, res)

            return max(left_res, right_res)
        
        res1 = dfs(root.left, root.val, root.val)
        res2 = dfs(root.right, root.val, root.val)

        return max(res1, res2)


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
    