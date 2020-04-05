from Graph import *
from Hamiltonian import *

# generate a graph of 100 vertices with edges (0,1), (1,2), (2,3), ...,(98,99) and two additional edges (55,57), (56,58)
# this hamilton algorithm should result in 2 paths
G100 = Graph()
for i in range(0,100,1):
    G100.add_vertex(Vertex(i))

edges100 = []
for i in range(0,100,1):
    edges100.append((i,i+1))

edges100.append((55,57))
edges100.append((56,58))

for e in edges100:
    G100.add_edge(e[0], e[1])

# testing
G100.printGraph()
path100 = []
sourceID = 0
endID = 99
hamilton(G100, sourceID, endID, path100)