'''
-------------------------------------------------------------------------------------
-> Problem Title: 138. Copy List with Random Pointer
-> Problem Status: Completed
-> Problem Attempted: 01/01/2024
-> Problem Description:
-------------------------------------------------------------------------------------

https://leetcode.com/problems/copy-list-with-random-pointer/description/

-------------------------------------------------------------------------------------
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
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head):
        """
        run: accepted
        time: o(n)
        space: o(n)
        choke: none
        brief:
            - Creating the new deepcopy node;;
            - Linking the new deepcopy node;;
        """
        if not head:
            return head

        cur = head
        hashmap = {}
        # S1: Creating the new deepcopy node;;
        while (cur):
            node = Node(cur.val)
            hashmap[cur] = node
            cur = cur.next

        cur = head
        # S2: Linking the new deepcopy node;;
        while (cur):
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur = cur.next

        return hashmap[head]


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
