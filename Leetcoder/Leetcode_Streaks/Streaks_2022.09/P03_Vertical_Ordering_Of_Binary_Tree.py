'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 987. Vertical Order Traversal of a Binary Tree
-> Problem Status: Pending...
-> Problem Attempted: 04.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions 
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each 
column index starting from the leftmost column and ending on the rightmost column. There may
be multiple nodes in the same row and same column. In such a case, sort these nodes by their
values.

Return the vertical order traversal of the binary tree.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.


Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.


Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be 
ordered by their values.


Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

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
class Solution:

    ###--- BFS Approach: Copied !!!
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        vertical = defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        while queue:
            size = len(queue)
            for _ in range(size):
                node, x, y = queue.popleft()
                vertical[x].append((y, node.val))
                if node.left:
                    queue.append((node.left, x - 1, y + 1))
                if node.right:
                    queue.append((node.right, x + 1, y + 1))
        res = []
        for x in sorted(vertical.keys()):
            res.append([tup[1] for tup in sorted(vertical[x])])
        return res

    
    ###--- DFS Approach: Copied !!!
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, x, y, vertical):
            vertical[x].append((y, root.val))
            if root.left:
                dfs(root.left, x - 1, y + 1, vertical)
            if root.right:
                dfs(root.right, x + 1, y + 1, vertical)
            
        if not root:
            return []
        vertical = defaultdict(list)
        dfs(root, 0, 0, vertical)
        res = []
        for x in sorted(vertical.keys()):
            res.append([tup[1] for tup in sorted(vertical[x])])
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
    