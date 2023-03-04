'''
-------------------------------------------------------------------------------------
-> Problem Title: 1791. Find Center of Star Graph
-> Problem Status: Completed
-> Problem Attempted: 25/02/2022
-> Problem Description: 
-------------------------------------------------------------------------------------

There is an undirected star graph consisting of n nodes labeled from 1 to n. A
star graph is a graph where there is one center node and exactly n - 1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi]
indicates that there is an edge between the nodes ui and vi. Return the
center of the given star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
 

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


class Solution:

    
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        atype: List[List[int]]
        rtype: int
        """
        if not edges:
            return 

        # return self.ansv1(edges)
        # return self.ansv2(edges)
        return self.anv3(edges)
    
    def anv3(self, e):
           return (set(e[0]) & set(e[1])).pop()

    def ansv2(self, edges):
        """
        _note: refer to anv1, 
        _study: Here set is used for grepping common center 
        node among other nodes. 
        """
        res = set(edges[0])
        for e in edges[1:]:
            res = res.intersection(e)
        return res.pop()

    def ansv1(self, edges):
        """
        _run: accepted
        _code: brute force , time: o(n), space: o(1)
        _choke: none
        _study: approach is comparaing the common edge among 
        all edges.
        """
        res = None
        edge = edges[0]
        for e in edges[1:]:
            res = e[0] if e[0] in edge else e[1]
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
    