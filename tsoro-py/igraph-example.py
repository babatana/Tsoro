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


# deterministic graph generated
g2 = Graph.Tree(127, 2)

