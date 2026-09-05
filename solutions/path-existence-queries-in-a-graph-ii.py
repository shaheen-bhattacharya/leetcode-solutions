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
        print(comp)
        res = []
        for u, v in queries:
            if comp[u] != comp[v]:
                res.append(-1)
            elif u == v:
                res.append(0)
            else:
                val = abs(nums[v] - nums[u])
                add = val//maxDiff + 1 if val % maxDiff == 0 else val//maxDiff + 1
                res.append(add)
        return res