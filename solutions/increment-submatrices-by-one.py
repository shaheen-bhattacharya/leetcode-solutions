class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        diff = [[0] * (n+1) for _ in range(n+1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r2+1][c2] -= 1
            diff[r2][c2+1] -= 1
            diff[r2+1][c2+1] += 1

        res = [[0]*n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if r > 0:
                    diff[r][c] += diff[r-1][c]
                if c > 0:
                    diff[r][c] += diff[r][c-1]
                if r > 0 and c > 0:
                    diff[r][c] -= diff[r-1][c-1]
                res[r][c] = diff[r][c]
        return res
                


