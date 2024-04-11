'''
Problem:
'''
#!/bin/python3

import math
import os
import random
import re
import sys


# Optimised Solution Approach ~ O(n+k)
def divisibleSumPairsV1(ar, k, n):
    # Write your code here
    rem = [0]*k
    for i in range(len(ar)):
        rem[int(ar[i]%k)] += 1
    count = (rem[0]*(rem[0]-1))/2
    if k%2==0 and k>=2:
        count = count + (rem[int(k/2)]*(rem[int(k/2)]-1))/2
        for i in range(1,int((k/2))):
            count = count + rem[i]*rem[k-i]
    else:
        for i in range(1,int((k+1)/2)):
            count = count + rem[i]*rem[k-i]
    return (int(count))


# Brute Force Approach - O(n^2)
def divisibleSumPairsV2(nums, key, size):
    count = 0
    start, end = 0, size
    ## Brute Force
    for i in range(0,size):
        for j in range(i+1,size):
            if(nums[i]+nums[j])%key == 0:
                count += 1
    return count


def main():
    # res = divisibleSumPairsV1([5,4,3,2,0], 5, 5)
    res = divisibleSumPairsV2([5,4,3,2,0], 5, 5)
    print(res) if res else print("Empty!")
        

if __name__ == '__main__':
    print("#------------ Code Starts --------------#")
    main()
    print("#------------ Code Ends ----------------#")
    