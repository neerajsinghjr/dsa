"""
Implementation of Trie Datastructure;
Called, Prefix Tree;
"""
d
class Node:
    """
    init() : constructor;
    """
    def __init__(self,data):
        self.data = dict


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
        if(self.root is not None):
            if(type(data) == list):
                for word in data:
                    self._push(self.root,word)
            else:
                self._push(self.root,data)
        else:
            self.root = 

    
    """
    _push() : _push method init
    """
    def _push(self,root,word):
        if(root is not None):
            for letter in word:
                if(letter not in root[letter]):
                    root = root[letter]
                root = root[letter]
            root['end'] = True
        return 
            

    """
    find() : find data in Trie;
    """
    def find(self,query):
        current = self.root 
        for q in query:
            if(q not in current[q]):
                return False
            current = current[q]
        if(current['end'] == True):         # Check For End Value;
            return True
        return False


