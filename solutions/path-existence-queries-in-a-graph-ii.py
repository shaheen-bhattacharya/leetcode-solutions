class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        inum = [(nums[i], i) for i in range(n)]
        inum.sort()
        cur = 0
        comp = [0] * n
        for i in range(1, n):
            num, idx = inum[i]
            pnum, _ = inum[i-1]
            if num - pnum <= maxDiff:
                cur += 1
            comp[idx] = cur
        
        res = []
        for u, v in queries:
            if comp[u] != comp[v]:
                res.append(-1)
            else:
                res.append(abs(nums[v] - nums[u])//maxDiff + 1)
        return res