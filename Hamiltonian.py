from Graph import Graph

def hamilton(G, source, end, path = []):
    # if the vertex id is not yet in the path, add it to path
    if source not in set(path):
        path.append(source)

        # if the path is graph.size() and last element is 'end'
        if(len(path) == G.size() and path[G.size()-1] == end):
            print('hamilton path: {}' .format(path)) # find a path and print it
        
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