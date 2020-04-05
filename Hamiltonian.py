from Graph import *

def hamilton(G, source, end, path = []):
    print('hamilton called with source={}, path={}'.format(source, path))
    if source not in set(path):
        path.append(source)

        # if the path is graph.size() and last element is 'end'
        if(len(path) == G.size() and path[G.size()-1] == end):
            return path
        
        # source.neighbor doesnt contain 'end'
        if end not in G.vertices[source].neighbor:
            for v in G.vertices[source].neighbor:
                res_path = [i for i in path]
                res_out = hamilton(G, v, end, res_path)
                if res_out is not None:
                    return res_out
            print('path {} is a dead end'.format(path))
        # source.neighbor contains 'end' 
        else:
            # first loop through all neighbors except for 'end'
            for v in G.vertices[source].neighbor:
                if v != end:
                    res_path = [i for i in path]
                    res_out = hamilton(G, v, end, res_path)
                    if res_out is not None:
                        return res_out
            
            # lastly do the case of 'end'
            res_path = [i for i in path]
            res_out = hamilton(G, end, end, res_path)
            if res_out is not None:
                return res_out
            print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(source, path))
                

# generate a graph
G = Graph()
for i in range(0,6,1):
    G.add_vertex(Vertex(i))

edges = [(0,2), (1,2), (0,5), (2,3), (3,5), (3,4), (1,3), (4,5)]
for edge in edges:
    G.add_edge(edge[0], edge[1])

# testing
G.printGraph()
path = []
sourceID = 0
endID = 2
print(hamilton(G, sourceID, endID, path))

