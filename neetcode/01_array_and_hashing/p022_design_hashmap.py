'''
-------------------------------------------------------------------------------------
-> Problem Title: 706. Design HashMap
-> Problem Status: Completed
-> Problem Attempted: 2024-03-08
-> Problem Description:
-------------------------------------------------------------------------------------

Problem:-
https://leetcode.com/problems/design-hashmap/

Reference:-
https://youtu.be/cNWsgbKwwoU

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

    # Objective of this class to provide a node object
    # which will hold key, value and next pointer.

    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    """
    _run: accepted
    _code:  time: o(1), space: o(n)
    _choke: none
    _study: --- chaining ---
    we first calculate the hash of the given key by using a simple logic where
    we modulo divide the given key with the total length of the map array.
    Due to which there are lot of possiblity that a particular hash key.
    there can be two unique values.

    For handling such solution we are using chaining apporach in which we the
    provided key is different but the generated hash is same then we map both the
    key,value pair to the same hash_key.

    for eg,
    map_length = 10
    k1, v1 = 1, 12
    k2, v2 = 11, 13
    generated hash_key for both the keys, (k1 & k2) are 1

    ---- update entry in hash map ----
    map = {
        1: Node(-1, -1) => Node(1, 12) => Node(11, 13)
    }
    """

    def __init__(self):
        self.map = [Node() for i in range(10 ** 4)]

    def _get_hash(self, key):
        return key % len(self.map)

    def put(self, key: int, val: int) -> None:
        index = self._get_hash(key)
        pre = self.map[index]
        cur = pre.next
        while (cur):
            if cur.key == key:
                cur.val = val
                return
            pre, cur = cur, cur.next
        # add new node if value is unique;;
        pre.next = Node(key, val)

    def get(self, key: int) -> int:
        index = self._get_hash(key)
        cur = self.map[index]
        while (cur):
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = self._get_hash(key)
        pre = self.map[index]
        cur = pre.next
        while cur:
            if cur.key == key:
                pre.next = cur.next
            pre, cur = cur, cur.next


class MyHashMapV1:
    """
    _run: rejected[28/37] (brute-force)
    _code: time:o(1), space: o(n)
    _choke: in this solution we have mapped multiple values on the same
    hash_key generated and due to this. Individual values mapped with unique key
    but mapped on same hash_index got override.
    _study: Implemented a solution but failed to store multiple key, value pair
    at the same hash_index.
    To overcome such solution - found out two solution
    1) chaining
    2) open addressing
    """

    def _get_hash_index(self, key):
        return key % 10 ** 4

    def __init__(self):
        # 10**4 from constraints from leetcode;;
        self.data = [-1 for i in range(10 ** 4)]

    def put(self, key: int, value: int) -> None:
        hash_index = self._get_hash_index(key)
        self.data[hash_index] = value

    def get(self, key: int) -> int:
        hash_index = self._get_hash_index(key)
        return self.data[hash_index]

    def remove(self, key: int) -> None:
        hash_index = self._get_hash_index(key)
        self.data[hash_index] = -1


##---Main Execution;;
def main(res=None):
    try:
        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)
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
