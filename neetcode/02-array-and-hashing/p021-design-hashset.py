'''
-------------------------------------------------------------------------------------
-> Problem Title: 705. Design HashSet
-> Problem Status: Completed
-> Problem Attempted: 2024-03-08
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/design-hashset/description/

Reference:-
https://youtu.be/VymjPQUXjL8

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


##---Main Solution
class Node:

    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next


class MyHashSetV3:
    """
    _run: failed [28/32]
    _code: time: o(1), space: o(n)
    _choke: none
    _study: -- chaining ----
    we first calculate the hash of the given key by using a simple logic where
    we modulo divide the given key with the total length of the map array.
    Due to which there are lot of possiblity that a particular hash key is map
    to two unqiues set of keys provided by user.

    For handling such solution we are using chaining apporach in which we the
    provided key is different but the generated hash is same then we map both the
    key,value pair to the same hash_key.

    for eg,
    map_length = 10
    k1 = 1
    k2 = 11
    generated hash_key for both the keys, (k1 & k2) are 1

    ---- update entry in hash map ----
    map = {
        1: Node(-1, -1) => Node(1) => Node(11)
    }
    """

    def __init__(self):
        # correction #1 : ListNode used as dummy not directly
        self.data = [Node() for i in range(10 ** 4)]

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


class MyHashSetV2:
    """
    _run: accepted (optimial but used internal hash library)
    _code: time: o(1) | space: (n)
    _choke: none
    _study: uses in-build defaultdict to manage and maintain key in
    hashmap.
    """

    def __init__(self):
        self.data = defaultdict(int)

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]


class MyHashSetV1:
    """
    _run: accepted (brute-force)
    _code: time: o(n) | space:o(n)
    _choke: none
    _study: Used list datastructure to manage data in the Hashset and
    insertion is taking o(n) and space also takes (n)
    Internally Its not like Hashset.
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
