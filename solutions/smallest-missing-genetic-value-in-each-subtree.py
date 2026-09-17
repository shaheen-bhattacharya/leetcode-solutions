class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        sl = SortedList([i for i in range(1, 100001)])
        adj = defaultdict(list)
        n = len(parents)
        for i in range(n):
            adj[parents[i]].append(i)
            adj[i].append(parents[i])

        res = [0] * n
        def dfs(node):
            for nei in adj[node]:
                if nei == parents[node]:
                    continue
                dfs(nei)
            sl.remove(nums[node])
            res[node] = sl[0]
        dfs(0)
        return res

