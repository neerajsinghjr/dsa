'''
Problem Description:
Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

Input:
N = 3
value[] = {1,3,4}
x = 2
Output: True
Explanation: In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.

Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output: False
Explanation: For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
from AlgoExpl.Helpers.Classes.LinkedList import LinkedList


## Main Working Function, here...
class Solution:
    
    def detectLoop(self, head):
        if not(head or head.next or head.next.next):
            return False
        return self.helper(head)
    
    
    def helper(self, head):
        slow = fast = head
        while(fast and fast.next):
            # check for slow pointer;
            if not(slow.next):
                return False
            slow = slow.next
            
            # check for fast pointer;
            if not(fast or fast.next.next):
                return False
            fast = fast.next.next
            
            # Loop Exist
            if(slow == fast):
                return True
            
        return False
        

def main():
    try:
        data = []               # ~ data
        obj = Solution()
        res = obj.reverseList(data)
        print(res) if res else print("Empty!")
        
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
    