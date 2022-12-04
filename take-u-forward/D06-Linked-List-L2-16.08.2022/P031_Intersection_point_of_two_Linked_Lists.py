'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Intersection of two Linked List
-> Problem Status: Completed
-> Problem Attempted: 16.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists 
intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected 
node.

listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected 
node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected 
node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA 
and headB to your program. If you correctly return the intersected node, then your solution will be 
accepted.

for eg,

Exmaple 1: 
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: 
The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: 
The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

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
    
    #--- Helper Method;;
    def getLength(self,head):
        count = 0
        node = head
        while(node != None):
            count += 1
            node = node.next
        return count
    
    
    #--- MAIN EXECUTION
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if(headA == headB == None): 
            return None 
        
        if(headA != None and headB == None): 
            return None
        
        if(headB != None and headA == None): 
            return None
        
        # return self.ansv1(headA,headB)
        return self.ansv2(headA,headB)
    
    
    """
    Code: Optimised Approach || Time: O(N) || Space: O(1)
    Study: Main criteria is to skip those extra nodes...
    a) First skip extra nodes while calculating length of both the list.
    b) Calculate absolute difference, this is for fetching the number of extra nodes to skip
    c) Skip those nodes from that list which have larger number of nodes from the beginning.
    That's it.
    """
    def ansv2(self,headA,headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        skipSteps = abs(lenA - lenB)
        
        # Skipping nodes from the list having more node to achieve (lenA == lenB);;
        if(lenA > lenB):
            # Skipping steps from List A;;
            for _ in range(skipSteps):
                headA = headA.next
        else:
            # Skipping Steps from List B;;
            for _ in range(skipSteps):          
                headB = headB.next        
        
        # Traversing List for common intersection;;
        while(headA != None and headB != None):
            if(headA == headB):
                return headA
            
            headA = headA.next
            headB = headB.next
            
        return None
    
    
    """ 
    Code: Brute Force || Time: O(N + N) || Space: O(N)
    Study: Scenario is like,
    -> First store all the node in the hashmap or dictionary of headA
    -> then search of the node of second list in hashmap or dictionary.
    """
    def ansv1(self, headA, headB):
        dataset = {}
        
        # S1: Storing Node;;
        node = headB
        while(node != None):
            dataset[node] = node.val
            node = node.next
                           
        node = headA
        # S2: Finding Node;;
        while(node != None):
            if(node in dataset):
                return node
                        
            node = node.next
            
        return None


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
    