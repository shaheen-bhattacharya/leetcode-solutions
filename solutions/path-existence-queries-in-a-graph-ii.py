class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        inum = [(nums[i], i) for i in range(n)]
        inum.sort()
        cur = 0
        comp = [0] * n
        for i in range(1, n):
            num, idx = inum[i]
            pnum, _ = inum[i-1]
            if num - pnum > maxDiff:
                cur += 1
            comp[idx] = cur
        
        LOG = 16
        up = [[0] * n for _ in range(LOG)]

        for i in range(n):  
            num, idx = inum[i]
            up[0][idx] = num
            l = i+1
            r = n
            while l < r:
                m = (l+r)//2
                num2, idx2 = inum[m]
                if num2 - num <= maxDiff:
                    l = m + 1
                else:
                    r = m
            up[0][idx] = inum[l-1][1]
        
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k-1][up[k-1][i]]
        
        def dist(u, v):
            ret = 0
            if comp[u] != comp[v]:
                return -1
            elif u == v:
                return 0
            if nums[u] > nums[v]:
                u, v = v, u
            for k in range(LOG-1, -1, -1):
                nxt = up[k][u]
                if nums[nxt] < nums[v]:
                    u = nxt
                    ret += 1 << k
            return ret + 1

        res = []
        for u, v in queries:
            res.append(dist(u, v))
        return res