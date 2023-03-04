'''
-------------------------------------------------------------------------------------
-> Problem Title: Graph by non-oops
-> Problem Status: Completed
-> Problem Attempted: 02/03/2025
-> Problem Description: 
-------------------------------------------------------------------------------------

Graph by simple implementation

-------------------------------------------------------------------------------------
'''

from time import time  
from collections import defaultdict, deque

visited = []
vertices = []
neighbours = defaultdict(dict)

##--- Add edges;
def add_edges(source, destination, cost):
    if not source in vertices:
        vertices.append(source)
    if not destination in vertices:
        vertices.append(destination)

    neighbours[source].update({destination : cost})
    neighbours[destination].update({source : cost})


##---Main Execution;;
def main(res=None):

    vertices.append('a')
    vertices.append('b')
    vertices.append('c')
    vertices.append('d')
    vertices.append('e')

    add_edges('a','b', 5)
    add_edges('a','c', 10)
    add_edges('b','a', 15)
    add_edges('b','c', 20)
    add_edges('b','d', 25)
    add_edges('c','a', 30)
    add_edges('c','b', 35)
    add_edges('c','d', 40)
    add_edges('c','e', 45)
    add_edges('d','b', 50)
    add_edges('d','d', 55)
    add_edges('d','e', 60)
    add_edges('e','c', 65)
    add_edges('e','d', 70)

    print("graph vertices: ", vertices)
    print("neighbour : ", neighbours)

    # print_bfs_pattern()
    

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")