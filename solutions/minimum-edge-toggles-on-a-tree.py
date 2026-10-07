class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        adj = defaultdict(list)
        rev = {}
        for i, (u, v) in enumerate(edges):
            adj[u].append(v)
            adj[v].append(u)
            rev[(u, v)] = i
            rev[(v, u)] = i

        res = []
        def dfs(par, node, changed):
            if len(adj[node]) == 1 and changed:
                return inf 
            amt = 0
            for nei in adj[node]:
                if start[nei] != target[nei]:
                    amt += 1
            for nei in adj[node]:
                if nei == par:
                    continue
                edge = (node, nei)
                idx = rev[edge]
                

        val = dfs(-1, 0, start[0]==target[0])
        return res if val != inf else res
                
