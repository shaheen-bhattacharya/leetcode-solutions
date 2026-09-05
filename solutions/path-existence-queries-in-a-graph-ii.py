class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        for i in range(n):
            nodes[nums[i]].append(i)
        
        keys = list(sorted(nodes.keys()))
        corr = {}
        nk = len(keys)
        for i in range(len(keys)):
            corr[keys[i]] = i
        
        def solve(u, v):
            dist = [inf] * n
            dist[u] = 0
            q = deque([(0, u)])
            while q:
                d, node = q.popleft()
                if node == v:
                    return d
                if d > dist[node]:
                    continue
                i = corr[nums[u]]
                j = i
                while j < nk and keys[j] - keys[i] <= maxDiff:
                    for nei in nodes[keys[j]]:
                        if nei == node:
                            continue
                        nd = d + 1
                        if nd < dist[nei]:
                            dist[nei] = nd
                            q.append((nd, nei))
                    j += 1
                j = i-1
                while j >= 0 and keys[i] - keys[j] <= maxDiff:
                    for nei in nodes[keys[j]]:
                        nd = d + 1
                        if nd < dist[nei]:
                            dist[nei] = nd
                            q.append((nd, nei))
                    j -= 1
            return -1
        
        res = []
        for u, v in queries:
            res.append(solve(u, v))
        return res
        
    
