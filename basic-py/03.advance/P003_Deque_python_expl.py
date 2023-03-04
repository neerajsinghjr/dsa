'''
-------------------------------------------------------------------------------------
-> Problem Title: Graph by non-oops
-> Problem Status: Completed
-> Problem Attempted: 02/03/2025
-> Problem Description: 
-------------------------------------------------------------------------------------

Deque in Python 

-------------------------------------------------------------------------------------
'''

from collections import deque

que = deque()
que.append(2)
que.append(3)
que.append(5)
que.append(8)
que.append(10)

print("que : ", que)
# pop-left to the que;;
print("pop-left: ", que.popleft())
# pop-right to the right;;
print("pop-right or simple-pop : ", que.pop())
# append to the right
print("append 20 to right or simple append : ", que.append(20), que)
# appending left to the que;;
print("append-left : ", que.appendleft(40), que)
# count the number of element occurences;;
print("count : ", que.count(20))
# extending que
print("before extending que to right : ", que)
que.extend([100,110,120])
print("after extending que to right : ", que)
# extending to the right of the que;;
print("before extending to right : ", que)
que.extendleft([0,1,2])
print("after extending to right: ", que)
# Length of the que;;
print("length of que : ", len(que))