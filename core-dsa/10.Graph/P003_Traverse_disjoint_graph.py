'''
-------------------------------------------------------------------------------------
-> Title: Graph with disjoint vertices
-> Attempted: 04/03/2023
-> Description: 
-------------------------------------------------------------------------------------

Graph with disjoint vertices

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

    def traverse_disjoint_graph(self):
        path, visited = [], []
        for vertex in self.dict:
            self.traverse(vertex, path, visited)
        return path

    def traverse(self, vertex, path, visited):
        if not(vertex in visited):
            visited.append(vertex)
            path.append(vertex)
            for adjacent in self.dict[vertex]:
                self.traverse(adjacent, path, visited)
            return path


if __name__ == "__main__":
    graph = Graph()

    graph.add('1','2') 
    graph.add('1','3') 
    graph.add('2','4') 
    graph.add('5','6') 
    graph.add('5','7') 
    graph.add('6','8') 
    graph.add('9','10')

    print('Dictionary:',graph.dict)
    print('Edges of the Graph:',graph.edges())
    print('Traverse Disjoint Graph : ', graph.traverse_disjoint_graph())