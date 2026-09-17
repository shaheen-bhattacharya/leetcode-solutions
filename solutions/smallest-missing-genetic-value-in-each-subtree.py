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

        def gset(node):
            ret = set([node])
            for nei in adj[node]:
                if nei == parents[node]:
                    continue
                ret |= gset(nei)
            return ret
        
        res = [0] * n
        def dfs(mv, allowed):
            print(allowed)
            if len(allowed) == 1:
                res[rev[mv]] = mv + 1
                return 
            node = rev[mv] if mv in rev else -2
            rem = gset(node) if node != -2 else set()
            allowed -= rem
            if node != -2:
                allowed.add(node)

            for nd in rem:
                if nd != node:
                    res[nd] = mv
            dfs(mv+1, allowed)

        dfs(1, set([i for i in range(n)]))
        return res


