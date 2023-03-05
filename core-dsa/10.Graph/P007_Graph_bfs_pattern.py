'''
-------------------------------------------------------------------------------------
-> Title: Graph BFS Pattern
-> Attempted: 04/03/2023
-> Description: 
-------------------------------------------------------------------------------------

Breadth first search graph traversal;;

-------------------------------------------------------------------------------------
'''

from collections import deque, defaultdict 


class Graph:

    def __init__(self):
        self.dict = defaultdict(list)

    def add(self,node,adjacent_node): 
        self.dict[node].append(adjacent_node)
        self.dict[adjacent_node].append(node)

    def edges(self): 
        graph_edges = []
        for node in self.dict: 
            for adjacent_node in self.dict[node]:
                if (adjacent_node, node) not in graph_edges :
                    graph_edges.append((node, adjacent_node))
        return graph_edges

    def show_bfs_pattern(self):
    	bfs_pattern = []
    	vertices = list(self.dict.keys())
    	visited = {vertex: False for vertex in vertices}
    	que = deque()
    	que.append(vertices[0])
    	while(que):
    		node = que.popleft()
    		if visited[node]:
    			continue
    		visited[node] = True
    		bfs_pattern.append(node)
    		for adj in self.dict[node]:
    			for n in adj:
    				if not visited[n]:
    					que.append(n)

    	return bfs_pattern

graph = Graph()

graph.add('1','2') 
graph.add('2','5') 
graph.add('2','3') 
graph.add('4','5') 
graph.add('4','3') 
graph.add('6','4') 
graph.add('6','5')

print('Dictionary:',graph.dict)
print('Edges of the Graph:',graph.edges())
print('BFS Pattern : ', graph.show_bfs_pattern())