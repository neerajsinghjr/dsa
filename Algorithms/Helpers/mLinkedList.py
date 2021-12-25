"""
Linked List Implementation file for CRUD Operations
"""

class Node:

    """
    init() : constructor
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


    """
    getData() : get the data of node;
    """
    def getData(self):
        return self.data


    """
    setData() : set the data to the required node;
    """
    def setData(self,data):
        self.data = data


class LinkedList:

    """
    init() : constructor;
    """
    def __init__(self, head = None):
        self.head = None


    """
    len() : return the length of the nodes; 
    """
    def __len__(self):
        if(self.head == None):
            return 0
        else:
            count = 0
            node = self.head
            while(node != None):
                node = node.next
                count += 1
            return count


    """
    getItem() : return the specific index node from linked list;
    """
    def __getitem__(self, index):
        return self.head[index]


    """
    print() : list all nodes of linked list
    """
    def show(self):
        node = self.head
        while(node.next != None):
            print(node.data, end=" -> ")
            node = node.next
        print(node.data)


    """
    pushFront() : push elements from front;
    eg, A <- B <- C <- D <- E
    """
    def pushFront(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            prevHead = self.head
            self.head = newNode
            newNode.next = prevHead


    """
    pushBack() : push elements from the end;
    eg, A -> B -> C -> D -> E
    """
    def pushBack(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode


    """
    remove() : remove node for specific index;
    eq, 
    Input : HEAD -> A -> B -> C -> None and index : 2
    Output : HEAD -> A -> C -> None 
    """
    def remove(self, index):
        pass


    """
    pop() : remove node from end;
    eg, 
    Input : A -> B -> C 
    Output  :A -> B -> None  
    """
    def pop(self):
        if(self.head == None):
            return None
        else:
            node = self.head
            prevNode = None
            # Step 1 : Go to one node before end;
            while(node.next != None):
                prevNode = node
                node = node.next
            # Step 2 : Reset the last node;
            prevNode.next = None
            del node                # Delete residual last node;
            

    """
    reverse() : reverse the linked list;
    eg, 
    Input : HEAD -> A -> B -> C -> None 
    Output : A <- B <- C <- HEAD
    """
    def reverse(self):
        if(self.head == None):
            return None
        else:
            node = self.head
            prevNode = None
            # Step 1 : Reverse Links;
            while(node != None):
                temp = node.next 
                node.next = prevNode
                prevNode = node
                node = temp
                # Step 2 : Change Head;
                if(temp == None):
                    self.head = prevNode

            return self.head

                