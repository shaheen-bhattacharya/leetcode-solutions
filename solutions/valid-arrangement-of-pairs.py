class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        adj = defaultdict(list)
        ind = defaultdict(int)
        out = defaultdict(int)
        for u, v in pairs:
            adj[u].append(v)
            ind[v] += 1
            out[u] += 1
        start = pairs[0][0]
        for s, e in pairs:
            if out[s] - ind[s] == 1:
                start = s
                break
        res = []
        def dfs(s):
            # print(s)
            while adj[s]:
                e = adj[s].pop()
                dfs(e)
                res.append([s, e])
        dfs(start)
        return res[::-1]
