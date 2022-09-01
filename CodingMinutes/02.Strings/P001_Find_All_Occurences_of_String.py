'''
----------------------------------------------------------------------------------------------------
-> Problem Title: Find all occurrence of a word inside string
-> Problem Status: Ongoing...
-> Problem Attempted: 30.08.2022
-> Problem Description: 
----------------------------------------------------------------------------------------------------
Find all occurences of a given word inside the string.

Example 1:
Input: String = "My name is Zora but my second name is Xerx.", word = "name"
Output: [3, 30]

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

    def findOccurrence(self,para,word):
    	if(word == "" or para == ""):
    		return []

    	return self.ansv1(para,word)



    """
    Run: Success
    Code: Brute Force | T:O(N) | S:(N)
    Study:
    Simple iteratively find all the word inside the paragraph from start index to 
    end index and iteratively increase the start index whenever any index if found.
    """
    def ansv1(self,para,word):
    	idx,res = 0,[]
    	start,end = 0,len(para)

    	while(start <= end):
    		idx = para.find(word,start,end)
    		if(idx == -1): break
    		res.append(idx)
    		start += idx

    	return res


##---Main Execution;;
def main():
    try:
        para = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,\
		molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum \
 		numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium \
		optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis \
		obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam \
		nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit, \
		tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit, \
		quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos \
		sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam\
		recusandae alias error harum maxime adipisci amet laborum. Perspiciatis \
		minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit \
		quibusdam sed amet tempora. Sit laborum ab, eius fugit doloribus tenetur\
		fugiat, temporibus enim commodi iusto libero magni deleniti quod quam \
		consequuntur! Commodi minima excepturi repudiandae velit hic maxime\
		doloremque. Quaerat provident commodi consectetur veniam similique a\
		earum omnis ipsum saepe, voluptas, hic voluptates pariatur est explicabo \
		fugiat, dolorum eligendi quam cupiditate excepturi mollitia maiores labore \
		suscipit quas? Nulla, placeat. voluptatem quaerat non architecto ab laudantium \
		modi minima sunt esse temporibus sint culpa, recusandae aliquam numquam \
		totam ratione voluptas quod exercitationem fuga. Possimus quis earum veniam \
		quasi aliquam eligendi, placeat qui corporis!"

        word = "vol"
        obj = Solution()
        res = obj.findOccurrence(para, word)
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
    