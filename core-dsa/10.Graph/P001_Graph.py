'''
-------------------------------------------------------------------------------------
-> Title: Graph - Datastructure
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
    It is used to create single node for a graph.
    '''
    
    # Func : Initialize the vertex node for graph;
    def __init__(self, node):
        self.node = node
        self.adjacent_nodes = {}

    # Func : Add Neighbour to a particular node;
    def add_neighbour(self, to_node, cost):
        # print("Available Neighbour : ", self.adjacent_nodes)
        self.adjacent_nodes[to_node] = cost

    # Func : Get all the Neighbour of a particular vertex;
    def get_neighbour(self, node):
        if not(node in self.adjacent_nodes):
            return {}
        return self.adjacent_nodes[node]


class Graph:
    '''
    Graph::class
    It is used to build the graph datastructure.
    '''

    # Func: Initialize the graph tree;;
    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

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
        # print("Available Neighbour -->> : ", self.vertices)
        self.vertices[from_node].add_neighbour(self.vertices[to_node], cost)
        self.vertices[to_node].add_neighbour(self.vertices[from_node], cost)

    # Func : Return node from graph base on key;;
    def get_vertices(self, node):
        if not(node in self.vertices):
            print(f"Node not found : {node}")

        return self.vertices[node]

    # Func : Return all the key node of graph;;
    def get_vertices(self):
        return self.vertices.keys()


##---Main Execution;;
def main(res=None):
    try:
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