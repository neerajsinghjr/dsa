'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Basic Methods of Linked List
-> Problem Status: Completed
-> Problem Attempted: 15.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
...

----------------------------------------------------------------------------------------------------
'''

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
