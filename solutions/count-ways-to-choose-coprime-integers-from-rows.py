class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = 1_000_000_007
        rows, cols = len(mat), len(mat[0])
        factors = defaultdict(set)
        mt = pow(cols, rows, MOD)

        dp = {}
        def dfs(r, val):
            key = (r, val)
            if key in dp:
                return dp[key]
            if r == rows:
                return 1
            res = 0
            for c in range(cols):
                gv = gcd(val, mat[r][c]) if val != -1 else mat[r][c]
                if gv != 1:
                    res += dfs(r+1, gv)
            dp[key] = res
            return res
        return (MOD + mt - dfs(0, -1))%MOD
                        

                 