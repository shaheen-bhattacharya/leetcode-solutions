class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        adj = defaultdict(list)
        scorr = defaultdict(list)
        ecorr = defaultdict(list)
        for i, (s, e) in enumerate(pairs):
            adj[i] = ecorr[e]
        print(adj)
        start = 0
        for i in range(n):
            if len(adj[i]) % 2 == 1:
                start = i
                break
        res = []
        def dfs(node):
            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)
            res.append(pairs[i])
        dfs(start)
        return res