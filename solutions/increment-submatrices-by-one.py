class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        radd = [0] * n
        rsub = [0] * n
        cadd = [0] * n
        csub = [0] * n
        for r1, c1, r2, c2 in queries:
            radd[r1] += 1
            rsub[r2] += 1
            cadd[c1] += 1
            csub[c2] += 1

        res = [[0]*n for _ in range(n)]
        
        cur = 0
        for r in range(n):
            cur += radd[r]
            for c in range(n):
                cur += cadd[c]
                res[r][c] = cur
                cur -= csub[c]
            cur -= rsub[r]
        return res
                


