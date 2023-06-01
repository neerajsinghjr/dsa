'''
-------------------------------------------------------------------------------------
-> Title: Detect cycle in graph
-> Attempted: 05/03/2023
-> Description: 
-------------------------------------------------------------------------------------

Detect cycle in graph;;

-------------------------------------------------------------------------------------
'''

from time import time
from collections import defaultdict


class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def set_edges(self, from_vertex, to_vertex):
		self.graph[from_vertex].append(to_vertex)
		self.graph[to_vertex].append(from_vertex)

	def get_edges(self):
		edges = []
		for (parent, childs) in self.graph.items():
			for child in childs:
				edges.append((parent, child))

		return edges

	def detect_cycle_in_graph(self):
		cycle = None
		parent, visited = -1, []
		for source in self.graph:		
			if not(source in visited):
				# Return the result as soon as cycle found;;
				if not cycle:
					cycle = self.detect_cycle(source, visited, parent)
		return (True if cycle == True else False)

	def detect_cycle(self, source, visited, parent):
		print("cur source : ", source)
		visited.append(source)
		for neighbour in self.graph[source]:
			print("next source  : ", neighbour)
			print("next parent : ", source)
			print("visited till now : ", visited)
			if neighbour in visited:
				print(f"->> visited : source: {source} -> neighbour: {neighbour}")
				print(f"->> parent : {parent} and neighbour: {neighbour}")
			if not(neighbour in visited):
				self.detect_cycle(neighbour, visited, source)
			elif(neighbour != parent):
				print(f"source : {source} ->>> adj neighbour : {neighbour},  ->>> cur_parent : {parent}",)
				return True


##---Main Execution;;
def main():
	graph = Graph()
	
	# G1: Cyclic Graph 
	# graph.set_edges(0,1)
	# graph.set_edges(1,2)
	# graph.set_edges(2,3)
	# graph.set_edges(3,1)

	# # G2: Cyclic  Graph 
	# graph.set_edges(0,1)
	# graph.set_edges(1,2)
	# graph.set_edges(2,0)
	# graph.set_edges(0,3)

	# #	G3: Non-Cyclic AD Graph 
	# graph.set_edges(0,1)
	# graph.set_edges(1,2)
	# graph.set_edges(2,3)

	# G4: Cyclic Graph 
	graph.set_edges(0,1)
	graph.set_edges(1,2)
	graph.set_edges(1,3)
	graph.set_edges(2,3)
	graph.set_edges(2,4)
	graph.set_edges(4,5)

	print("Edges : ", graph.graph)
	print("Is Cycle Exist in Graph  : ", graph.detect_cycle_in_graph())


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time()
    main()
    endTime = time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")