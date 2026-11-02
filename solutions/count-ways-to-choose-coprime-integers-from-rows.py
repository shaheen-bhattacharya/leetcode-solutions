class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007
        rows, cols = len(mat), len(mat[0])
        factors = defaultdict(set)

        for i in range(1, 151):
            for d in range(i, 151, i):
                factors[d].add(i)
        rc = [[0]*151 for _ in range(rows)]
        mt = pow(cols, rows, MOD)

        for r in range(rows):
            for c in range(cols):
                for f in factors[mat[r][c]]:
                    rc[r][f] += 1

        # dp = [[0]*151 for _ in range(rows)]

        dp = [0] * 151

        for d in range(150, 0, -1):
            ways = 1

            for r in range(rows):
                ways = ways * rc[r][d] % MOD

            for multiple in range(d * 2, 151, d):
                ways -= dp[multiple]

            dp[d] = ways % MOD
        return dp[1] % MOD
        
                        