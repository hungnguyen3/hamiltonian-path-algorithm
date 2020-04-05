from Graph import *
from Hamiltonian import *

# generate a graph of 200 vertices with edges (0,1), (1,2), (2,3), ...,(98,99) and 4 additional edges (55,57), (56,58), (155,157), (156,158)
# this hamilton algorithm should result in 4 paths

G200 = Graph()
for i in range(0,200,1):
    G200.add_vertex(Vertex(i))

edges200 = []
for i in range(0,200,1):
    edges200.append((i,i+1))

edges200.append((55,57))
edges200.append((56,58))

edges200.append((155,157))
edges200.append((156,158))

for e in edges200:
    G200.add_edge(e[0], e[1])

# testing
G200.printGraph()
path200 = []
sourceID = 0
endID = 199
hamilton(G200, sourceID, endID, path200)