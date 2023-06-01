'''
-------------------------------------------------------------------------------------
-> Title: Find total discontinued graph count
-> Attempted: 04/03/2023
-> Description: 
-------------------------------------------------------------------------------------

Find total discontinued graph count;;

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

    def find_total_discontinued_graph(self):
        count = 0
        path, visited = [], []
        for vertex in self.dict:
            if not(vertex in visited):
                count += 1
                visited = self.check_nested_child_nodes(vertex, visited)
        return count

    def check_nested_child_nodes(self, vertex, visited):
        if not(vertex in visited):
            visited.append(vertex)
            for adjacent in self.dict[vertex]:
                self.check_nested_child_nodes(adjacent, visited)
            return visited


if __name__ == "__main__":
    graph = Graph()

    graph.add('1','2') 
    graph.add('1','3') 
    graph.add('2','4') 
    graph.add('5','6') 
    graph.add('5','7') 
    graph.add('6','8') 
    graph.add('9','10')
    graph.add('11','12')
    graph.add('12','13')
    graph.add('13','14')
    graph.add('13','15')
    graph.add('16','17')
    graph.add('17','18')
    graph.add('18','19')


    print('Graph :',graph.dict)
    print('Graph Edges :',graph.edges())
    print('Total Disjoint Graph : ', graph.find_total_discontinued_graph())