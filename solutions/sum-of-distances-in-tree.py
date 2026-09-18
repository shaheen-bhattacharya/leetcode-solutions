class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        dist = [0] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, par):
            nodes = 1
            for nei in adj[node]:
                if nei == par:
                    continue
                ncnt, tot = dfs(nei, node)
                dist[node] += ncnt + tot
                nodes += ncnt
            return nodes, dist[node]
        dfs(0, -1)
        print(dist)

