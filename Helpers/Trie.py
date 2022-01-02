"""
Implementation of Trie Datastructure;
Called, Prefix Tree;
"""

class Node:
    """
    init() : constructor;
    """
    def __init__(self,data):
        self.data = [None]*26           # 26 Chars in Alphabet
        self.end = False

class Trie:
    """
    init() : constructor
    """
    def __init__(self):
        self.root = Node()
    

    """
    push() : push data to Trie;
    """
    def push(self,data):
        temp = Node()
        if(temp.data[]):
            pass


    """
    find() : find data in Trie;
    """
    def find(self,data):
        pass

