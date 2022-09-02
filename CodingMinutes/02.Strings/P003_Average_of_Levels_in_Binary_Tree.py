'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 637. Average of Levels in Binary Tree
-> Problem Status: Completed
-> Problem Attempted: 02.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the root of a binary tree, return the average value of the nodes on each level in the form of 
an array. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].


Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

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

from collections import deque


class Solution:
    
    ###---Main Execution;;;
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if(root == None):
            return  [0]
        
        return self.ansv1(root)
        # return self.ansv2(root)
    
    
    """
    Run: Success
    Code: BFS Approach | T:O(N) | S:(N) ~ Queue Space
    Study:
    In BFS, we travel level by level each rows...
    1) Starting up store the root node in queue
    2) While iterating and popping left from queue, we are 
    counting the level wise nodes and storing sum of every node
    in level wise fashion.
    3) Finally return the resultant list.
    
    """
    def ansv2(self,root):
        res = []        
        q = deque()
        q.append(root)
        
        while(q):
            c,mx = 0,0
            qlen = len(q)
            for _ in range(len(q)):
                cur = q.popleft()
                c,mx = c+1, mx+cur.val
                if(cur.left): q.append(cur.left)
                if(cur.right): q.append(cur.right)
            
            # Store result;
            res.append(mx/c)
        
        return res 
    
    
    """
    Run: Failed
    Code: Brute Force (BFS) | T:O(N) | S:O(1)
    Study:
    """
    def ansv1(self,root):
        res = []
        
        que = deque()
        que.append(root)            # Default ROOT node;
        que.append(None)            # Trace LEVEL End;
        
        mx,c = 0,0
        while(que):
            cur = que.popleft()
            print(f"cur: {cur}")
            if(cur == None):
                res.append(mx/c)
                mx,c = 0,0
                que.append(None)
                if(len(que) == 0):
                    print(f"que: {que}")
                    break
            else:
                c,mx = c+1, mx+cur.val
                if(cur.left): que.append(cur.left)
                if(cur.right): que.append(cur.right)
        
        return res
        


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
    