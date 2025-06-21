'''
-------------------------------------------------------------------------------------
-> Problem Title: 706. Design HashMap
-> Problem Status: Completed
-> Problem Attempted: 21/06/2025
-> Problem Description:
-------------------------------------------------------------------------------------

Problem Statement:
https://leetcode.com/problems/design-hashmap/description/

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
class MyHashMap_BEST:

    """
    _run: accepted
    _code: tc: o(1), sc: o(1), rt: 47ms, tcz: 37/37
    _choke: none
    - approach will come to end of lifecycle if we gets mix keys like int, char
    - but we can overcome using separate lookups like we can create char_lookups and create 
    index from it too. Just a heads up :)
    _brief: 
    - we formulate this solution on the basis of lookup space (10^6 + 1), all with default(-1)
    - put() methods comes with key and value, map the key with value; that's it 
    - get() methods comes with key, which is already part of lookup; return the lookup[key]
    - remove() method comes with key, re-assign the lookup key to default -1
    """

    def __init__(self):
        self.lookup = [-1] * 1000001
        
    def put(self, key: int, value: int) -> None:
        self.lookup[key] = value

    def get(self, key: int) -> int:
        return self.lookup[key]

    def remove(self, key: int) -> None:
        self.lookup[key] = -1


class Node:

    # Objective of this class to provide a node object 
    # which will hold key, value and next pointer.

    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap_V2:

    """
    _run: accepted
    _code:  tc: o(1), sc: o(n), rt: nan, tcz: 37/37
    _choke: none
    _brief: --- chaining ---
    - we first calculate the hash of the given key by using a simple logic where we modulo 
    divide the given key with the total length of the map array. 
    - due to which there are lot of possiblity that a particular hash key can face two 
    unique values. 
    - for handling such solution we are using chaining approach in whic the provided key is 
    different but the generated hash is same then we map both the (key,value) pair to the 
    same hash_key.
    - for eg,
        - map_length = 10
        - k1, v1 = 1, 12
        - k2, v2 = 11, 13
        - generated hash_key for both the keys, (k1 & k2) is 1
        - update entry in hash map
            map = {
                1: Node(-1, -1) => Node(1, 12) => Node(11, 13)
            }
    """

    def __init__(self):
        self.map = [ Node() for i in range(10**4)] 
        
    def _get_hash(self, key):
        return key % len(self.map)

    def put(self, key: int, val: int) -> None:
        index = self._get_hash(key)
        pre = self.map[index]
        cur = pre.next
        while(cur):
            if cur.key == key:
                cur.val = val
                return
            pre, cur = cur, cur.next
        # add new node if value is unique;;
        pre.next = Node(key, val)

    def get(self, key: int) -> int:
        index = self._get_hash(key)
        cur = self.map[index]
        while(cur):
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


class MyHashMap_V1:

    """
    _run: accepted ~rejected earlier fixed now
    _code: tc:o(1), sc: o(1), rt: 620 ms, tcz: 37/37
    _choke: none
    _brief: 
    --- comment: Mar 08, 2025 ---
    - Last Status: Rejected [tc:o(1), sc: o(n), rt: nan, tcz: 28/37]
    - below solution failed to store multiple key, value pair at the same hash_index. 
    - to overcome such solution - found out two solution 
        - chaining
        - open addressing
    --- comment: Jun 21, 2025 ----
    - fixed choked situation. 
    - choked situation description: earlier we were using 10^4 space to store hash due to 
    functions call as per problem statemen. but the total total can be 10^6 this leads to 
    disparity becuase the hash we were generating like this key % max_len. this leads to 
    disparity like below ...
    - for eg, 
        - max_len = 10 
        - candidate with key = 1 (got place 1 in hashmap)
        - candidate with key = 11 (also got place 1 in hashmap)
        - conclusion: this generate overriding of the data ie. loosing data integrity
    - choked situation fixed: earlier we were using 10^4 hash map. but now i'm using the 10^6+1
    as per question constraints. it fix above problem with unique hash like below ...
    - for eg,
        - max_len = 11 
        - candidate with key = 1 (got place 1 in hashmap)
        - candidate with key = 11 (also got place 0 in hashmap)
        - conclusion: no loosing data integrity
    """

    def _get_hash_index(self, key):
        return key % 1000001

    def __init__(self):
        # 10**4 from constraints from leetcode;;
        self.data = [-1 for i in range(1000001)]
        
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
        res = None
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
