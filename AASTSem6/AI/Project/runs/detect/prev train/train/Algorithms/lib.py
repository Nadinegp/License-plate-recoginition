import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = [[] for _ in range(self.V)]  # Initialize an empty adjacency list for each vertex

    def addEdge(self, src, dest):
        self.adjList[src].append(dest)  # Add destination to the adjacency list of source
        self.adjList[dest].append(src)  # Add source to the adjacency list of destination
        print(self.adjList)

    def isConnected(self):
        visited = [False] * self.V
        # print(visited)  # Initialize a visited array to keep track of visited vertices
        self.dfs(0, visited)  # Perform depth-first search starting from the first vertex

        return all(visited)  # Return True if all vertices are visited, indicating the graph is connected

    def isAcyclic(self):
        visited = [False] * self.V  # Initialize a visited array to keep track of visited vertices
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, -1):  # Check if there is a cycle starting from each unvisited vertex
                    return False  # If a cycle is found, return False

        return True  # If no cycles are found, return True

    def dfs(self, v, visited):
        visited[v] = True  # Mark the current vertex as visited
        # print(visited)
        # print(self.adjList)
        for i in self.adjList[v]:  # Visit all adjacent vertices
            print("i is here ",i, "okay:",self.adjList[i])
            if not visited[i]:
                print("flag",i)
                self.dfs(i, visited)  # Recursively perform depth-first search on unvisited adjacent vertices

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True  # Mark the current vertex as visited
        for i in self.adjList[v]:  # Visit all adjacent vertices
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):  # Recursively check for cycles starting from the adjacent vertices
                    return True  # If a cycle is found, return True
            elif i != parent:
                return True  # If an adjacent vertex is visited and not the parent, it indicates a cycle

        return False  # If no cycles are found, return False

    def drawGraph(self):
        G = nx.Graph()
        G.add_nodes_from(range(self.V))  # Add nodes to the graph
        for i in range(self.V):
            for j in self.adjList[i]:
                G.add_edge(i, j)  # Add edges to the graph based on the adjacency list

        pos = nx.spring_layout(G)  # Determine the positions of nodes using the Spring layout algorithm
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', width=1.5)  # Draw the graph with styling options
        plt.show()  # Display the graph

if __name__ == '__main__':
    graph = Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    print("Adjacency List:")
    for i in range(graph.V):
        print(i, ": ", end="")
        for j in graph.adjList[i]:
            print(j, end=" ")
        print()

    print("Is connected:", graph.isConnected())
    print("Is acyclic:", graph.isAcyclic())

    graph.drawGraph()
