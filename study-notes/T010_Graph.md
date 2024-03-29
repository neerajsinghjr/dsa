```
-------------------------------------------------------------------------------------
-> Title : Graph Notes
-> Author: @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 25/02/2022
-> Updated : 25/02/2022
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q001 : Graph Datastructure ;;
-------------------------------------------------------------------------------------
```

### GRAPH NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### Q001 : Graph Datastructure ;;

Refer : dsa/core_dsa/graph/P001_graph.py

Study : https://www.bogotobogo.com/python/python_graph_data_structures.php

#### Graph Structure :-

In this Graph structure, We have 3 vertices a, b, c.
````
Edges on vertices are like that...
- Edge, a -> b, weight 7 and a -> c, weight 17.
- Edge, b -> c, weight 8 and b -> a, weight 7.
- Edge, c -> a, weight 17 and c -> b, weight 8.

Python Graph structure look like this,
{
	a -> { {b -> 7}, {c -> 17} }
	b -> { {a -> 7}, {c -> 8}  }
	c -> { {b -> 8}, {a -> 17} }
}
````

#### Graph - Terminology :-

- `VERTEX` : A vertex is the most basic part of a graph and it is also called a
  node. Throughout we'll call it note. A vertex may also have additionalc 
  information and we'll call it as payload.

- `EDGE` : An edge is another basic part of a graph, and it connects two
  vertices/ Edges may be one-way or two-way. If the edges in a graph are all
  one-way, the graph is a directed graph, or a digraph.

- `WEIGHT` : Edges may be weighted to show that there is a cost to go from one
  vertex to another. For eg, in a graph of roads that connect one city to
  another, the weight on the edge might represent the distance between the
  two cities or traffic status.

- `GRAPH` : A graph can be represented by `G` where G=(V,E), i.e, V is a set of
  vertices and E is a set of edges. 
  Each edge is a tuple (v,w) is the weight or cost from that vertices -> edge.
  We can add the third variable in the tuple, (V, E, W)
  for eg, Given vertices = {a, b, c, d, e, f}
  then, example set of edges...
  ````
  E = {
	  ('a', 'b', 7), ('a', 'c', 5), ('a', 'f', 3),	# from a -> b, a -> c, a -> f
	  ('b', 'c', 10), ('b', 'd', 15),	# from, b -> c, b -> d
	  ('c', 'f', 2), ('c', 'd', 11),	# from, c -> f, c -> d
	  ('d', 'e', 6), ('d', 'b', 15),	# from d -> e, d -> b
	  ('e', 'b', 6), ('e', 'f', 9), 	# from e -> b, e -> f
  }
  ````

- `Path` : A path in a graph is a sequence of vertices that are connected by
  edges. The unweighted path length is the number of edges in the path (n-1). 
  The weighted path length is the sum of the weights of all the edges in the path.

- `Cycle` : A cycle in a directed graph is a path that starts and ends at the
  same vertex. A graph with no cycles is called an acyclic graph. A directed
  graph with no cycles is called a directed acyclic graph or a DAG.	


-------------------------------------------------------------------------------------