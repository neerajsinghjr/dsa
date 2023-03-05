'''
-------------------------------------------------------------------------------------
-> Problem Title: 997. Find the Town Judge
-> Problem Status: Completed
-> Problem Attempted: 05/03/2023
-> Problem Description: 
-------------------------------------------------------------------------------------

In a town, there are n people labeled from 1 to n. There is a rumor that one
of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody. Everybody (except for the town judge) trusts the
town judge. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the
person labeled ai trusts the person labeled bi. If a trust relationship does
not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be
identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:
-> 1 <= n <= 1000
-> 0 <= trust.length <= 104
-> trust[i].length == 2
-> All the pairs of trust are unique.
-> ai != bi
-> 1 <= ai, bi <= n

-------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random



from collections import defaultdict

class Solution:

    def findJudge(self, n: int, trust) -> int:
        if(n == 1):
            return 1
        
        return self.ansv1(n, trust)
        # return self.ansv2(n, trust)
        
    def ansv2(self, n, trust):
        """
        _run: accepted
        _code: time: (n), space: o(n)
        _choke: na
        _study: simply mapping indegree and outdegee of graph.
        for indegree marking as (+1) and outdegree as (-1)
        and at end person who have gathered trust == (n-1). 
        It should be the town judge.
        edge = [first, second]
        i,e 1st trust 2nd but can't say same for 2nd person
        """
        trust_map = defaultdict(lambda: 0)
        for tr in trust:
            trust_map[tr[0]] -= 1
            trust_map[tr[1]] += 1

        for key,value in trust_map.items():
            if(value == n-1):
                return key

        return -1

    def ansv1(self, n, trust):
        """
        _run: rejected
        _code: time: o(n), space: o(n)
        _choke: refer choke scenario
        _study: simply marking +1 for those who are gaining trust
        and 0 for those not gaining anything or not giving trust.
        at the end we are fetching only those who doesnt give trust.
        In this case which is person with zero trust.
        """
        hashmap = dict()
        # Mapping Every trust;;
        for tr in trust:
            if tr[0] in hashmap:
                hashmap[tr[0]] += 1
            else:
                hashmap[tr[0]] = 1
                # Tracking second person trust;;
                if not(tr[1] in hashmap):
                    hashmap[tr[1]] = 0
        print("hashmap : ", hashmap)
        # Finding Town Judge;;
        for k,v in hashmap.items():
            if not(v):
                return k
        return -1


##---Main Execution;;
def main(res=None):
    """
        Choke scenario for ansv1();
        n = 4
        trust : [[1,3],[1,4],[2,3]]
        output : 3
        expected : -1
    """
    try:
    	data = []				
        obj = Solution()	
        res = None
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