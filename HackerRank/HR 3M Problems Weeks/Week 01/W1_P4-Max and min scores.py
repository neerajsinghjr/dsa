'''
Problem:
Maria plays college basketball and wants to go pro. 
Each season she maintains a record of her play. 
She tabulates the number of times she breaks her 
season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, 
and she begins counting from there.

Example
scores = [12,24,10,24]
Game  Score  Minimum  Maximum   Min Max
0      12     12       12       0   0
1      24     12       24       0   1
2      10     10       24       1   1
3      24     10       24       1   1

Return [maxCount, minCount]
'''

#!/bin/python3

import math
import os
import random
import re
import sys



def breakingRecords(scores):
    # Write your code here
    """
    Examples...
    first game set minScore and maxScore;
    next games,
    minCount == score < minScore
    maxCount == score > maxScore
    """
    minCount = maxCount = 0
    if scores:
        # Base Case
        minScore = maxScore = scores[0]
        # Main Case
        for score in scores:
            if score < minScore:
                minCount += 1                       ## Min Count;
                minScore = score
            elif score > maxScore:
                maxCount += 1                       ## Max Count;
                maxScore = score
                
    return [maxCount, minCount]


def main():
    res = breakingRecords([12,4,15,16,17,18])
    print(res) if res else print("None")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    