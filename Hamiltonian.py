from Graph import *

def hamilton(G, source, end, path = []):
    if source not in set(path):
        path.append(source)

        # if the path is graph.size() and last element is 'end'
        if(len(path) == G.size() and path[G.size()-1] == end):
            print('hamilton path: {}' .format(path))
        
        # source.neighbor doesnt contain 'end'
        if end not in G.vertices[source].neighbor:
            for v in G.vertices[source].neighbor:
                res_path = [i for i in path]
                hamilton(G, v, end, res_path)
            
        # source.neighbor contains 'end' 
        else:
            # first loop through all neighbors except for 'end'
            for v in G.vertices[source].neighbor:
                if v != end:
                    res_path = [i for i in path]
                    hamilton(G, v, end, res_path)
            
            # lastly do the case of 'end'
            res_path = [i for i in path]
            hamilton(G, end, end, res_path)
                

# generate a graph with 6 vertices
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

