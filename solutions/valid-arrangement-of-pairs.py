class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        adj = defaultdict(list)
        scorr = defaultdict(list)
        ecorr = defaultdict(list)
        start = 0
        for i, (s, e) in enumerate(pairs):
            scorr[s].append(i)
            ecorr[e].append(i)

        for i in range(n):
            if len(scorr[pairs[i][1]]) - len(ecorr[pairs[i][0]]) == 1:
                start = i
                break

        res = []
        def dfs(node):
            print(node)
            while scorr[pairs[node][1]]:
                nei = scorr[pairs[node][1]].pop()
                dfs(nei)
            res.append(pairs[node])
        dfs(start)
        return res[::-1]