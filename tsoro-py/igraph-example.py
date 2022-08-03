# https://igraph.org/python/tutorial/latest/tutorial.html

import igraph
print(igraph.__version__)

from igraph import *

g = Graph()

# print(g)
g.add_vertices(3)
# print(g)
g.add_edges([(0,1), (1,2)])
# print(g)
g.add_edges([(2, 0)])
# print(g)
g.add_vertices(3)
# print(g)
g.add_edges([(2, 3), (3, 4), (4, 5), (5, 3)])
# print(g)
summary(g)
g.get_eid(2, 3)


# deterministic graph generated, a regular tree graph
# 127 vertices each with two children
g2 = Graph.Tree(127, 2)

# get the first 10 edges
g2.get_edgelist()[0:10]


# stochastic generator
g = Graph.GRG(100, 0.2)

# Setting and retrieving attributes
# use **vs** or **es** as a dictionary, you are assigning attributes to all vertices/edges of the graph
# vs is the vertices attribute
# es is the edge attribute
g.vs
g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

