'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Add Two Numbers
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

1) The number of nodes in each linked list is in the range [1, 100].
2) 0 <= Node.val <= 9
3) It is guaranteed that the list represents a number that does not have leading zeros.

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


## Main Working Function, here...
class Solution:
    
    """
    Code: Brute Force or Optimised | T:O(1) | S:O(1)
    Study:
    Simple solution would be...
    1) Replace the value of $cur node with the $nex node value;
    2) then, modify $cur->next with the $cur->next->next node link;
    return 
    """
    def deleteNode(self,node):
        if(node != None):
            node.val = node.next.val
            node.next = node.next.next
        return 


def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = ""
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
    