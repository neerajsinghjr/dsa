'''
-------------------------------------------------------------------------------------
-> Title: Graph DFS Pattern
-> Attempted: 04/03/2023
-> Description: 
-------------------------------------------------------------------------------------

Graph DFS Pattern

-------------------------------------------------------------------------------------
'''

from time import time
from collections import defaultdict


class Graph:

	def __init__(self):
		self.dict = defaultdict(list)

	def get_edges(self):
		edges = []
		# A1: Find the parent vertex;;
		for vertex in self.dict:
			# A2: Find the child vertex;;
			for neighbour in self.dict[vertex]:
				edges.append((vertex, neighbour))
		return edges

	def set_edges(self, from_vertex, to_vertex):
		self.dict[from_vertex].append(to_vertex)
		self.dict[to_vertex].append(from_vertex)

	def show_dfs_pattern(self):
		visited, dfs_pattern = [], []
		for vertex in self.dict:
			self.make_dfs_pattern(vertex, visited, dfs_pattern)
		return dfs_pattern

	def make_dfs_pattern(self, vertex, visited, dfs_pattern):
		if not(vertex in visited):
			visited.append(vertex)
			dfs_pattern.append(vertex)
			for neighbour in vertex:
				self.make_dfs_pattern(neighbour, visited, dfs_pattern)

			return dfs_pattern


##---Main Execution;;
def main():
	graph = Graph()

	graph.set_edges('1','2') 
	graph.set_edges('2','5') 
	graph.set_edges('2','3') 
	graph.set_edges('4','5') 
	graph.set_edges('4','3') 
	graph.set_edges('6','4') 
	graph.set_edges('6','5')

	print("Graph : ", graph.dict)
	# print("Edges : ", graph.get_edges())
	print("DFS Pattern : ", graph.show_dfs_pattern())


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")