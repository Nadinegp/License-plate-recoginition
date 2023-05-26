import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for i in range(vertices)]
        self.adj_list = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_list[u].append(v)

    def dfs(self, v, visited):
        visited[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def is_connected(self):
        visited = [False] * self.vertices
        self.dfs(0, visited)
        return all(visited)

    def is_acyclic(self):
        visited = [False] * self.vertices
        stack = [False] * self.vertices
        for i in range(self.vertices):
            if not visited[i]:
                if self.dfs_cycle(i, visited, stack):
                    return False
        return True

    def dfs_cycle(self, v, visited, stack):
        visited[v] = True
        stack[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                if self.dfs_cycle(i, visited, stack):
                    return True
            elif stack[i]:
                return True
        stack[v] = False
        return False

# example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 4)
g.add_edge(0, 4)

print("Adjacency Matrix:", g.adj_matrix)
print("Adjacency List:", g.adj_list)

print("Is Connected:", g.is_connected())
print("Is Acyclic:", g.is_acyclic())

# plot the graph
G = nx.Graph()
for i in range(g.vertices):
    for j in range(i+1, g.vertices):
        if g.adj_matrix[i][j] == 1:
            G.add_edge(i, j)

nx.draw(G, with_labels=True)
plt.show()
