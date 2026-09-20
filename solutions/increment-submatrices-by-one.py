class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        lazy = [[0] * n for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            lazy[r1][c1] += 1
            lazy[r2][c2] -= 1

        res = [[0]*n for _ in range(n)]
        
        cur = 0
        for r in range(n):
            for c in range(n):
                val = lazy[r][c]
                if val > 0:
                    cur += val
                    res[r][c] = cur
                else:
                    res[r][c] = cur
                    cur += val
        return res
                


