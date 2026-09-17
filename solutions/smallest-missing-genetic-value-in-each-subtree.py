class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        adj = defaultdict(list)
        n = len(parents)
        for i in range(n):
            adj[parents[i]].append(i)
            adj[i].append(parents[i])
        rev = {}
        for i in range(n):
            rev[nums[i]] = i

        res = [0] * n
        seen = set()
        def dfs(node):
            miss = 1
            for nei in adj[node]:
                if nei == parents[node]:
                    continue
                miss = max(miss, dfs(nei))
            seen.add(nums[node])
            while miss in seen:
                miss += 1
            res[node] = miss
            return miss
        dfs(0)
        return res
            
                
                

        dfs(1, set([i for i in range(n)]))
        return res


