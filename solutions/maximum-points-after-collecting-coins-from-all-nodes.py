class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = {}

        def dfs(node, par, mods):
            key = (node, par, mods) 
            if key in dp:
                return dp[key]

            op1 = coins[node] - k
            for nei in adj[node]:
                if nei == par:
                    continue
                op1 += dfs(nei, node, mods)

            op2 = coins[node]//2**(mods+1)
            for nei in adj[node]:
                if nei == par:
                    continue
                op2 += dfs(nei, node, mods+1)

            dp[key] = max(op1, op2)
            return dp[key]
        return dfs(0, -1, 0)            