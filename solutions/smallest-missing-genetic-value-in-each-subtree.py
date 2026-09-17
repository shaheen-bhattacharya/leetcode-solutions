class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        adj = defaultdict(list)
        n = len(parents)
        indegree = [0] * n
        for i in range(1, n):
            adj[parents[i]].append(i)
            adj[i].append(parents[i])
            print(i, parents[i])
            indegree[parents[i]] += 1
        print(indegree)
        rev = {}
        for i in range(n):
            rev[nums[i]] = i

        res = [0] * n
        maxv = [1] * n
        sets = defaultdict(set)
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:    
            node = q.popleft()
            if node == -1:
                break
            sets[node].add(nums[node])
            sets[parents[node]].add(nums[node])
            miss = maxv[node]
            while miss in sets[node]:
                miss += 1
            res[node] = miss
            maxv[parents[node]] = max(maxv[parents[node]], miss)
            indegree[parents[node]] -= 1
            if indegree[parents[node]] == 0:
                q.append(parents[node])
        return res

            

