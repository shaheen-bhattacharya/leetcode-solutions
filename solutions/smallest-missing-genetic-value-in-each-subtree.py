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
        maxv = [1] * n
        seen = set()
        def dfs(node):
            if node == -1:
                return 

            seen.add(nums[node])
            miss = maxv[node]
            while miss in seen:
                miss += 1
            res[node] = miss

            pv = maxv[parents[node]]
            maxv[parents[node]] = max(maxv[parents[node]], nums[node])
            dfs(parents[node])
            seen.remove(nums[node])
            maxv[parents[node]] = pv
            return 
        
        for i in range(n):
            if len(adj[i]) == 1:
                dfs(i)
        return res

            

