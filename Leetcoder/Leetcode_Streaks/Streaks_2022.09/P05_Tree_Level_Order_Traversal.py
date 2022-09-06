'''
----------------------------------------------------------------------------------------------------
-> Problem Title:  429. N-ary Tree Level Order Traversal
-> Problem Status: Completed.
-> Problem Attempted: 04.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 

Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 104]

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

class Solution:
    
    ###---Main Execution;;;
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not(root): return []
        
        return self.ansv1(root)
        # return self.ansv2(root)

    
    """
    Run: Success
    Code: BFS | T:O(N) | S:O(M)
    Study:
    This approach is similar to the first one in ansv1(), but implementation
    is different.
    In this approach, level wise nodes are stored in list by using for loop
    after inserting nodes inside the level[], append level to the main res[]
    """
    def ansv2(self,root):
        res = []
        que = deque([root])
        while(que):
            level = []          # Store Level Nodes;
            for _ in range(len(que)):
                node = que.popleft()
                # Store the level node;
                level += [node.val]
                # Popped node can have many children 
                for n in node.children:
                    que.append(n)
                        
            res.append(level)
        
        return res
            
        
    
    """
    Run: Success
    Code: BFS | T:O(N) | T:O(N)
    Study:
    Simply Traversing tree level wise by using queue, 
    1) Inserted default root nodes first as list for iteration.
    2) Then start add popping nodes from the left of it
    3) Start appending the nodes from the right of the queue
    4) For every level node break, we have set None as a delimiter;
    NOTE: Delimiter should be set only when the que is not empty for
    the upcoming level of row and nodes otherwise break
        
    for eg,
        root = [1,null,3,2,4,null,5,6]
        que = [1,NONE,3,2,4,NONE,5,6]
    ie, NONE shows end of the row.
        
    """   
    def ansv1(self,root):
        res,temp = [],[]
        
        que = deque([root])
        que.append(None)             # X: Delimiter for the row end;
        
        while(len(que)):
            
            root = que.popleft()
            
            if(root): temp.append(root.val) 
            
            if(root == None):
                if(temp): res.append(temp)
                if(que): que.append(None)
                temp = []              
            else:
                for n in root.children: que.append(n)
                    
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
    