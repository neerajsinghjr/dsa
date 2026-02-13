'''
-------------------------------------------------------------------------------------
-> Problem Title: 705. Design HashSet
-> Problem Status: Completed
-> Problem Attempted: 21/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/design-hashset/description/

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random
import collections


##---Main Solution
class MyHashSet:

    """
    _run: accepted (BEST !!!)
    _code: tc: o(n), sc: o(1), rt: 39 ms, tcz: 33/33
    _choke: 
    - apporach will come to end of lifecycle if we gets mix keys like int, char
    - but we can overcome using separate lookups like we can create char_lookups and create 
    index from it too. Just a heads up :)
    _brief:
    - we formulate this solution on the basis of lookup space (10^6 + 1), all with default False
    - add() methods comes with key, which is already part of lookup; we just set it to True
    - remove() methods comes with key, which is already part of lookup; we just set it to False
    - contain() method comes with key, which is already part of lookup; we just return it
    """
    
    def __init__(self):
        self.lookup = [False] * 1000001

    def add(self, key: int) -> None:
        self.lookup[key] = True

    def remove(self, key: int) -> None:
        self.lookup[key] = False

    def contains(self, key: int) -> bool:
        return self.lookup[key]


class Node:
    
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next


class MyHashSet_V3:

    """
    _run: rejected
    _code: tc: o(1), sc: o(n), rt: nan, tcz: 28/32
    _choke: none
    _brief: -- chaining ----
    - we first calculate the hash of the given key by using a simple logic where we modulo 
    divide the given key with the total length of the map array.
    - due to which there are lot of possiblity that a particular hash key is map to two 
    unqiues set of keys provided by user.
    - for handling such solution we are using chaining apporach in which we the provided key 
    is different but the generated hash is same then we map both the key,value pair to the 
    same hash_key.
    - for eg,
        map_length = 10
        k1 = 1
        k2 = 11
        generated hash_key for both the keys, (k1 & k2) are 1
    - update entry in hash map ----
    map = {
        1: Node(-1, -1) => Node(1) => Node(11)
    }
    - EXPL-FIX: I believe this can be fix if we just use max value which can come as a key 
    to us then we can use max_length as per max key 
    - for eg, if we know k2 = 11 then we can use max_length as 11 instead of 10 
    - in real solution i update the range from 10^4 => (10^6+1)
    - EXPL-FIX Rejected !!!
    """

    def __init__(self):
        # correction #1 : ListNode used as dummy not directly
        self.data = [ Node() for i in range(1000000+1) ]
    
    def _get_hash_index(self, key):
        return key % len(self.data)

    def add(self, key: int) -> None:
        hash_index = self._get_hash_index(key)
        pre_key = self.data[hash_index]
        cur_key = pre_key.next
        while cur_key:
            if cur_key.key == key:
                return
            cur_key = cur_key.next
        pre_key.next = Node(key)
        
    def remove(self, key: int) -> None:
        hash_index = self._get_hash_index(key)
        pre = self.data[hash_index]
        cur = pre.next
        while cur:
            if cur.key == key:
                pre.next = cur.next
            pre, cur = cur, cur.next

    def contains(self, key: int) -> bool:
        hash_index = self._get_hash_index(key)
        cur_key = self.data[hash_index]
        while cur_key:
            if cur_key.key == key:
                return True
            cur_key = cur_key.next
        return False


class MyHashSet_V2:

    """
    _run: accepted (optimial but used internal hash library)
    _code: tc: o(1), sc: (n)
    _choke: none
    _brief: 
    - uses in-build defaultdict to manage and maintain key in hashmap.
    """

    def __init__(self):
        self.data = defaultdict(int)

    def add(self, key: int) -> None:
        self.data[key] = True
        
    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


class MyHashSet_V1:

    """
    _run: accepted (brute-force)
    _code: tc: o(n), sc: o(n)
    _choke: none
    _brief: 
    - used list datastructure to manage data in the hashset and insertion is taking o(n) 
    and space also takes (n)
    - internally Its not like hashset.
    """

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)        

    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        return False


##---Main Execution;;
def main(res=None):
    try:
        res = None
        # Your MyHashSet object will be instantiated and called as such:
        # obj = MyHashSet()
        # obj.add(key)
        # obj.remove(key)
        # param_3 = obj.contains(key)
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
