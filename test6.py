from Graph import *
from Hamiltonian import *

# generate a graph with 6 vertices
#     0-----1
#    /       \
#   5         2
#    \       /  
#     4-----3

G = Graph()
for i in range(0,6,1):
    G.add_vertex(Vertex(i))

edges = [(0,2), (1,2), (0,5), (2,3), (3,5), (3,4), (1,3), (4,5), (0,1), (1,4), (2,4)]
for edge in edges:
    G.add_edge(edge[0], edge[1])

# testing
G.printGraph()
path = []
sourceID = 0
endID = 5
hamilton(G, sourceID, endID, path)