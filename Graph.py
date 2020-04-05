# class vertex is just an id(name) associated with a particular vertex
class Vertex:
    # constructor for a vertex
    def __init__(self, id):
        self.id = id
        self.neighbor = list()

    # add a vertex to a neighbor list
    def addNeighbor(self, v):
        if v not in self.neighbor:
            self.neighbor.append(v)
            self.neighbor.sort()

class Graph:
    vertices = {}

    # add a vertex to graph vertices dictionary
    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.id not in self.vertices:
            self.vertices[v.id] = v
            return True
        else:
            return False

    # add an edge by adding v1 to v2.neighbor && v2 to v1.neighbor
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            for key, value in self.vertices.items():
                if key == v1:
                    value.addNeighbor(v2)
                if key == v2:
                    value.addNeighbor(v1)
            return True
        else:
            return False

    # print out the graph
    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(key) + str(self.vertices[key].neighbor))


# test to see if graph is working
g = Graph()
for i in range(0,10,1):
    g.add_vertex(Vertex(i))

edges = [(0,1), (1,2), (2,3), (4,5), (5,9)]
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.printGraph()

