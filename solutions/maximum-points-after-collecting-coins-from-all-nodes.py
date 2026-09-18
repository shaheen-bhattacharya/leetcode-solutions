class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        adj = defaultdict(list)
        pars = {}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs2(node, par):
            pars[node] = par
            for nei in adj[node]:
                if nei == par:
                    continue
                dfs2(nei, node)
        dfs2(0, -1)
        dp = {}

        def dfs(node, mods):
            key = (node, mods) 
            if key in dp:
                return dp[key]

            op1 = -inf
            if mods > 13:
                return 0
            
            op1 = coins[node]//2**mods - k
            for nei in adj[node]:
                if nei == pars[node]:
                    continue
                op1 += dfs(nei, mods)

            op2 = coins[node]//2**(mods+1)
            for nei in adj[node]:
                if nei == pars[node]:
                    continue
                op2 += dfs(nei, mods+1)

            dp[key] = max(op1, op2)
            return dp[key]
        return dfs(0, 0)            