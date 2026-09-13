class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 1_000_000_007
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dist = [inf] * (n+1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue
            for nei, w in adj[node]:
                nc = cost + w
                if nc < dist[nei]:
                    dist[nei] = nc
                    heapq.heappush(heap, (nc, nei))

        dp = {}
        def dfs(node):
            if node in dp:
                return dp[node]
            if node == n:
                return 1
            ret = 0
            for nei, w in adj[node]:
                if dist[nei] >= dist[node]:
                    continue
                ret += dfs(nei) % MOD
            dp[node] = ret % MOD
            return ret % MOD
        return dfs(1)

