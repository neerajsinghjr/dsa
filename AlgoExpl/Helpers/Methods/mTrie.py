"""
Trie | mHelpers
"""

"""
Trie() : Create Trie Structure;
"""
def Trie(words):
    _end = "end"                # Delimiter
    root = dict()               # Default dict()
    for word in words:          # Words = ["bar","baz"] 
        current = root
        for letter in word:     # Word = ["b","a","r"]
            current = current.setdefault(letter,{})
        current[_end] = _end    # Terminator;
    return root


"""
find() : find inside Trie structure;
"""
def find(root,word):
    _end = "end"
    for letter in word:
        if(letter not in root[letter]):
            return False
        root = root[letter]
    return _end in root[_end]

