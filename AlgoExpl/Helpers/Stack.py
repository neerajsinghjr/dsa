"""
Implementation of Stack Datastructure in  Python
"""

class Stack:

    """
    init() : constructor;
    """
    def __init__(self,limit=100):
        self.index = -1                         # Top counter tracker;
        self.stack = limit[0]*1000              # Stack array based on limit, if any;


    """
    len() : return length of the stack
    """
    def __len__(self):
        if(self.stack == None):
            return 0
        return len(self.stack)


    """
    empty() : check for empty function;
    """
    def empty(self):
        if(self.index == -1 or len(self.stack) == 0):
            return True
        return False


    """
    show() : print all elements of stack;
    """
    def show(self):
        if(self.empty()):
            print("Stack Empty")
        else:
            while(self.index > -1):
                print(self.stack[self.index])
                self.index -= 1
        

    """
    append() : add element to stack;
    """
    def append(self,data):
        # If Limit is applicable;
        if(self.limit):
            if(self.index > self.limit):
                self.index += 1
                print(self.index)
                self.stack[self.index] = data 
            else:
                print(f"Stack reached Limit {self.limit}")
        else:    
            print(self.stack)
            self.index += 1
            print(self.index,"else")
            self.stack[self.index] = data
            print(self.index, self.stack[self.index])
        


    """
    pop() : pop element from top;
    """
    def pop(self):
        pass


    """
    remove() : remove element as per index
    """
    def remove(self):
        pass

