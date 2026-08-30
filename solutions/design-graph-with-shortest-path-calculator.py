class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = defaultdict(list)

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.adj[u].append((v, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [inf] * self.n
        heap = [(0, node1)]
        dist[node1] = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if cost >= dist[node]:
                continue
            for nei, c in self.adj[node]:
                nc = cost + c
                if nc < dist[nei]:
                    dist[nei] = nc
                    heapq.heappush(heap, (dist[nei], nei))
        return dist[node2] if dist[node2] != inf else -1
                


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)