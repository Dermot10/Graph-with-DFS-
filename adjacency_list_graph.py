# creating an undirected graph with an adjacency list to hold the paths
# Better for sparse graphs but slower for dense graphs


# Each Vertex will hold an adjacency list which will hold their respective neighbouring paths
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = []

# class method to add neighbouring path to a vertex if not found within the vertex's adjacency list

    def add_neighbours(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

# Graph class


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

# evalauting the existence of vertices
# for each key and value pair in the dictionary add the neighbour into their adjacency list

    def add_paths(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbours(v)
                if key == v:
                    value.add_neighbours(u)
            return True
        else:
            return False

# helper function to print the keys from the dictionary in a sorted list
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours))


if __name__ == "__main__":
    # Graph object instantiated and vertexes created and added to the graph object
    g = Graph()
    g.add_vertex(Vertex("A"))
    g.add_vertex(Vertex("B"))
    g.add_vertex(Vertex("C"))
    g.add_vertex(Vertex("D"))
    g.add_vertex(Vertex("E"))
    g.add_vertex(Vertex("F"))
    g.add_vertex(Vertex("G"))
    g.add_vertex(Vertex("H"))
    g.add_vertex(Vertex("I"))
    g.add_vertex(Vertex("J"))
    for i in range(ord("A"), ord("K")):
        g.add_vertex(chr(i))

# dictionary with vertices and respective neighbours
# DFS algorithm using dictionary Key and value pairs
edges = {
    "A": ["B", "E"],
    "B": ["A", "F"],
    "C": ["G"],
    "D": ["E", "H"],
    "E": ["A", "D", "H"],
    "F": ["B", "G", "I", "J"],
    "G": ["C", "F", "J"],
    "H": ["D", "E", "I"],
    "I": ["F", "H"],
    "J": ["F", "G"]
}

visited = set()


def dfs(visited, edges, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in edges[node]:
            dfs(visited, edges, neighbour)


# Alterantively neighbours can be stored in standard adjacency list
paths = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH',
         'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for path in paths:
    g.add_paths(path[:1], path[1:])

print("Adjanceny List of Vertex Edges:")
g.print_graph()
print(" ")
print("Depth-First Search: ")
dfs(visited, edges, "F")
