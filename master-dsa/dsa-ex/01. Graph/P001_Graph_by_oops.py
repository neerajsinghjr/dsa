'''
-------------------------------------------------------------------------------------
-> Title: Graph by oops
-> Attempted: 25/02/2023
-> Description: 
-------------------------------------------------------------------------------------

Exploration of graph datastructure.

-------------------------------------------------------------------------------------
'''

import os
import re
import sys
import time
import math
import random


class Vertex:
    '''
    Vertex::class 
    '''

    # Func : Initialize the vertex node for graph;;
    def __init__(self, node):
        self.node = node
        self.adjacent_nodes = {}

    # Func : Object Representation;;
    def __str__(self):
        return str(self.node) + ' adjacent: ' + str([aj_node.node for aj_node in self.adjacent_nodes])

    # Func : Add Neighbour to a particular node;;
    def add_neighbour(self, to_node, cost):
        # print("Available Neighbour : ", self.adjacent_nodes)
        self.adjacent_nodes[to_node] = cost

    # Func : Get Specific Neighbour by node key;;
    def get_neighbour(self, node):
        if not(node in self.adjacent_nodes):
            return {}
        return self.adjacent_nodes[node]

    # Func : Get all the Neighbour by key;;
    def get_neighbour_keys(self):
        return self.adjacent_nodes.keys()

    # Func : Get the node value;;
    def get_node(self):
        return self.node

    # Func : Get the weight of the node;;
    def get_weight(self, node):
        return self.adjacent_nodes[node]


class Graph:
    '''
    Graph::class
    '''

    # Func: Initialize the graph tree;;
    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

    # Func: Iterator for iternating graph;;
    def __iter__(self):
        return iter(self.vertices.values())

    # Func: Representation object;;
    def __str__(self):
        return f"Vertex : {self.node}"

    # Func: Add new node to the graph;;
    def add_vertex(self, node):
        # print("Available Vertex : ", self.vertices)
        if node in self.vertices:
            print("Node already present in the graph")
            return 
        vertex = Vertex(node)
        self.vertices[node] = vertex
        self.vertex_count += 1
        return vertex

    # Func: Connect edge with two nodes with cost;;
    def add_edge(self, from_node, to_node, cost=0):
        if not(from_node in self.vertices):
            vertex = Vertex(from_node)
            self.vertices[from_node] = Vertex
        if not(to_node in self.vertices):
            vertex = Vertex(to_node)
            self.vertices[to_node] = vertex
        # Connection will be create bi-direction a->b and b->a.
        self.vertices[from_node].add_neighbour(self.vertices[to_node], cost)
        self.vertices[to_node].add_neighbour(self.vertices[from_node], cost)

    # Func : Return node from graph base on key;;
    def get_vertice(self, node):
        if not(node in self.vertices):
            print(f"Node not found : {node}")

        return self.vertices[node]

    # Func : Return all the key node of graph;;
    def get_vertices_keys(self):
        return self.vertices.keys()


##---Main Execution;;
def main(res=None):
    graph = Graph()
    nodes = ('a', 'b', 'c', 'd', 'e', 'f')
    
    # A1: Create independent node;
    for node in nodes:
        graph.add_vertex(node)

    # A2: Connecting nodes via edges;
    graph.add_edge('a', 'b', 7)  
    graph.add_edge('a', 'c', 9)
    graph.add_edge('a', 'f', 14)
    graph.add_edge('b', 'c', 10)
    graph.add_edge('b', 'd', 15)
    graph.add_edge('c', 'd', 11)
    graph.add_edge('c', 'f', 2)
    graph.add_edge('d', 'e', 6)
    graph.add_edge('e', 'f', 9)

    # A3 : Traversing the Graph;;
    for parent_node in graph:
        print(parent_node)
        for child_node in parent_node.get_neighbour_keys():
            p_id = parent_node.get_node()       # parent node;
            c_id = child_node.get_node()        # child node;
            cost = parent_node.get_weight(child_node)      # Weight of the child node;
            print(f"({p_id}, {c_id}, {cost})")


if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")