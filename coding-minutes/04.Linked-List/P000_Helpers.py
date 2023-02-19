'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Basic Methods of Linked List
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Includes all the basic methods of linked list data-structure;

----------------------------------------------------------------------------------------------------
'''
import os
from random import randint
import P000_Helpers as ll


###---Node Class;;
class Node:
    
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


###---Return length of the linked list;;
def getLength(head):
    count = 0
    while(head != None):
        head = head.next
        count += 1

    return count


###---Insert node at Start Of Linked List;;
def insertAtStart(head,val=None) -> None:
    if(val != None):
        node = Node(val)        
        node.next = head
        head = node

    return head


###---Insert node the mid of the Linked List;;
def insertAtMid(head,val):
    n = getLength(head)
    if(n == 0):
        head.next = Node(val)
    else:
        pre = None
        cur = head
        limit = n//2

        for _ in range(limit):
            pre,cur  = cur,cur.next

        node = Node(val)
        pre.next = node
        node.next = cur

    return head


###---Insert node at the end of Linked List;;
def insertAtEnd(head,val=None):
    if(val != None):
        if(head == None):
            head.next = Node(val)
        else:
            cur = head
            while(cur.next != None):
                cur = cur.next
            cur.next = Node(val)

    return head


###---Print Linked List;;
def printList(head):
    cur = head
    while(cur != None):
        marker = "->" if(cur.next != None) else ""
        print(cur.val,marker,end=" ")
        cur = cur.next
    print("-> NULL")
    
    return 



###---Iterative Reverse Linked List;;
def itrReverse(head):

    if(head == None):
        return head

    if(head.next == None):
        return head

    pre,cur = None,head

    while(cur != None):
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex

    return pre


###---Created Linked List;;
def createLinkedList(nodes=11,start=True):
    head = Node(1)
    for x in range(2,nodes+1):
        if start:
            head = insertAtStart(head,x)
        else:
            head = insertAtEnd(head,x)

    return head


###---Created Linked List ~version2 ;;
def createList(start=1,end=11,fromLeft=False,even=None):
    if(even == None):
        head = Node(start)
    elif(start%2 == 0 and even):
        head = Node(start)
    else:
        head = Node(start+1)
        start += 1

    for x in range(start+1,end+1):
        if(fromLeft):
            if(even == None):
                head = insertAtStart(head,x)
            if(x%2 == 0 and even == True):
                head = insertAtStart(head,x)
            elif not(x%2 and even == True):
                head = insertAtStart(head,x)    
        else:
            if(even == None):
                head = insertAtEnd(head,x)
            elif(x%2 == 0 and even):
                print(f"n:evn: {x}/{even}")
                head = insertAtEnd(head,x)
            elif not(x%2 == 0 and even):
                head = insertAtEnd(head,x)    
            
    return head



## Merge With Extra Space;
def mergeList(list1,list2):

    dummy = ll.Node()
    head = dummy

    while(list1 and list2):
        if(list1.val < list2.val):
            dummy.next = list1
            list1,dummy = list1.next,dummy.next
        else:
            dummy.next = list2
            list2,dummy = list2.next,dummy.next

    if(list2 != None):
        dummy.next = list2
    if(list1 != None):
        dummy.next = list1

    return head.next


## Merge With only Stack Space;
def mergeListV2(list1,list2):
    if(list1 == None): return list2

    if(list2 == None): return list1

    dummy = ll.Node()

    if(list1.val < list2.val):
        dummy  = list1
        dummy.next = mergeListV2(list1.next, list2)
    else:
        dummy = list2
        dummy.next = mergeListV2(list1,list2.next)

    return dummy


### Merge Without Extra Space
def mergeListV3(list1,list2):
    head = ll.Node()
    dummy = head        
    
    while(list1 and list2):
        if(list1.val <= list2.val):
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next
        else:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next

    if(list1 or list2):
        dummy.next = list1 if(list1) else list2

    return head.next


###---Generate Random Linked List;
def createRandomList(n=10,start=1,end=1000,fromLeft=False):
    # First Node of Linked List;
    x = randint(start,end)

    if(fromLeft):
        head = Node(x)
    else:
        head = Node(x)

    # For N-1 node of Linked List;
    for _ in range(1,n):
        x = randint(start,end)
        if(fromLeft):
            head = insertAtStart(head,x)
        else:
            head = insertAtEnd(head,x)

    return head
