'''
----------------------------------------------------------------------------------------------------
-> Problem Title: 1996. The Number of Weak Characters in the Game
-> Problem Status: Completed
-> Problem Attempted: 09.09.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------

You are playing a game that contains multiple characters, and each of the
characters has two main properties: attack and defense. You are given a 2D
integer array properties where properties[i] = [attacki, defensei] represents
the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and
defense levels strictly greater than this character's attack and defense
levels. More formally, a character i is said to be weak if there exists
another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.


Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0

Explanation: No character has strictly greater attack and defense than the
other. 

Example 2:
Input: properties = [[2,2],[3,3]]
Output: 1

Explanation: The first character is weak because the second character has a
strictly greater attack and defense. 

Example 3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1

Explanation: The third character is weak because the second character has a
strictly greater attack and defense.
 

Constraints:

2 <= properties.length <= 105
properties[i].length == 2
1 <= attacki, defensei <= 105

----------------------------------------------------------------------------------------------------
'''

#!/bin/python3

import os
import re
import sys
import time
import math
import random


###--- Main Solution;;
class Solution:
    
    def numberOfWeakCharacters(self, props: List[List[int]]) -> int:
        n = len(props)
        if(n == 1):
            return 0
        
        # return self.ansv1(props,n)
        return self.ansv2(props,n)
    
    
    """
    Run: Accepted
    Code: Optimised | T:O(NLogN) | S:O(1)
    Study:
    This question approach is based on weak defence so...
     1) Sorting the attack first but group defences larger -> Smaller fashion,
     2) then iterate through simple measure the weakCharacter 
     
    """
    def ansv2(self,props,n):
        maxDefense = 0
        weakCharacter = 0
        
        # Sort:: Sort but group larger value first for the second index value then smaller
        # eg, [[1,1], [1,4]] => [[1,4], [1,1]]
        # props.sort(key=lambda x:(x[0],-x[1]))
                   
        # Sort:Reverse:: Use the negative sign for the first index value;
        # eg, [[1,1], [2,4]] => [[2,4], [1,1]]
        props.sort(key=lambda x:(-x[0], x[1]))
        
        for _,defense in props:
            if(defense < maxDefense):
                weakCharacter += 1
            else:
                maxDefense = defense
        
        return weakCharacter
        
        
    """
    Run: TLE
    Code: Brute Force | T:O(N*N) | S:O(1)
    Study:
    Reach out to the Time Limit Exception, because N => 10^4
    """
    def ansv1(self,props,n):
        weakCharacter = 0
        for i in range(n):
            for j in range(n):
                if(i == j): continue
                if(props[i][0] < props[j][0] and props[i][1] < props[j][1]):
                    weakCharacter += 1
        
        return weakCharacter


##---Main Execution;;
def main():
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
    