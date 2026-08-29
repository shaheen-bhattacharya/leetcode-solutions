class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dist = [[inf]*n for _ in range(n)]
        for u, v, c in edges:
            self.dist[u][v] = c

        for i in range(n):
            self.dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        if c >= self.dist[u][v]:
            return 
        self.dist[u][v] = c
        for i in range(self.n):
            for j in range(self.n):
                self.dist[i][j] = min(self.dist[i][j], self.dist[i][u] + c + self.dist[v][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        val = self.dist[node1][node2]
        return val if val != inf else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)