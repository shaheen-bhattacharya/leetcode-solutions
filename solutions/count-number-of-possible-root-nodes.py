class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) - 1
        gadj = defaultdict(list)
        adj = defaultdict(list)
        gset = set([(u, v) for u, v in guesses])

        for u, v in guesses:
            gadj[u].append(v)
            gadj[v].append(u)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        corr = 0
        def dfs(node, par):
            nonlocal corr
            for nei in adj[node]:
                if nei == par:
                    continue
                if (node, nei) in gset:
                    corr += 1
                dfs(nei, node)
        dfs(0, -1)
        print(corr)

                


        
