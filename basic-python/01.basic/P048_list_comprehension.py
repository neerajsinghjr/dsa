'''
-------------------------------------------------------------------------------------
-> Title: Iterator Python
-> Attempted: 28/11/2022
-> Description: 
-------------------------------------------------------------------------------------
...

-------------------------------------------------------------------------------------
'''
import time

# iterations = 100000000
# start = time.time()
# mylist = [i+1 for i in range(iterations)]
# end = time.time()
# print(end - start)

iterations = 100000000
start = time.time()
mylist = []
for i in range(iterations):
    mylist.append(i+1)
end = time.time()
print(end - start)