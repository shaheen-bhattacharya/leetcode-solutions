class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        adj = defaultdict(list)
        n = len(parents)
        res = [1] * n
        seen = [0] * 100002
        if 1 not in nums:
            return res
        for i in range(n):
            adj[parents[i]].append(i)
        
        def dfs(i):
            if seen[nums[i]] == 0:
                for ch in adj[i]:
                    dfs(ch)
                seen[nums[i]] = 1
    
        i = nums.index(1)
        miss = 1

        while i >= 0:
            dfs(i)
            while seen[miss]:
                miss += 1
            res[i] = miss
            i = parents[i]
        return res
            

